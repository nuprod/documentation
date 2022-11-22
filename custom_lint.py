import re
from sphinxlint import *


# https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#sections
HEADINGS_CHARACTERS = [
    '#', '*', '=', '-', '^', '"', '\'',
    # TODO COMPLETE https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#sections
]
HEADINGS_REGEX = "(%s)\n" % (
    "|".join(
        f"(\\{character}+)" for character in HEADINGS_CHARACTERS
    )
)

@checker(".rst")
def check_headers(file, lines, options=None):
    """Search for roles missing their closing backticks.

    Bad:  :fct:`foo
    Good: :fct:`foo`
    """
    toskip = set()
    file_headers_characters = []  # TODO check ordering of headers
    for lno, line in enumerate(lines, start=1):
        if toskip and toskip.pop():
            continue
        if re.match(HEADINGS_REGEX, line):
            # TODO verify line content only consists of heading markers and \n
            # ---'--- shouldn't work (but maybe already catched by sphinx build ?)
            delimiting_char = line[0]
            if delimiting_char not in file_headers_characters:
                file_headers_characters.append(delimiting_char)

            if re.match(HEADINGS_REGEX, lines[lno+1]):
                # Header in 3 lines
                heading_lines = [line, lines[lno], lines[lno+1]]
                heading_text = lines[lno]
                post_heading_line_number = lno+2
                toskip.add(lno+1)
                toskip.add(lno+2)
            else:
                # Header in 2 lines
                heading_lines = [lines[lno-2], line]
                heading_text = lines[lno-2]
                post_heading_line_number = lno

            # print("".join(heading_lines))
            if not all(
                len(heading_line) == len(heading_text)
                for heading_line in heading_lines
            ):
                yield lno, "heading formatting line length doesn't match heading size."

            # TODO verify empty line above heading
            if lines[post_heading_line_number] != "\n":
                yield post_heading_line_number, "missing empty line after heading"


if __name__ == "__main__":
    sys.exit(main())
