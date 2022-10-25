=============
Pay with SEPA
=============

SEPA, the Single Euro Payments Area, is a payment-integration initiative of the European Union to
simplify bank transfers denominated in euros. SEPA allows you to send payment orders to your
bank to automate bank wire transfers.

SEPA is supported by the banks of the 27 EU member states, as well as:

EFTA countries:

- Iceland;
- Liechtenstein;
- Norway;
- Switzerland.

Non-EEA SEPA countries:

- Andorra;
- Monaco;
- San Marino;
- United Kingdom;
- Vatican City State.

Non-EEA territories:

- Saint-Pierre-et-Miquelon;
- Guernsey;
- Jersey;
- Isle of Man.

When paying a bill in Odoo, you can select SEPA mandates as a payment option. At the day's end,
you can generate the SEPA file containing all bank wire transfers and send it to the bank.

By default, the file follows the SEPA Credit Transfer **'pain.001.001.03'** specifications. This is
a well-defined standard among banks. However, for Swiss and German companies, other formats are used
**'pain.001.001.03.ch.02'** for Switzerland and **'pain.001.003.03'** for Germany.

Once the payments are processed by your bank, you can directly import the account statement in
Odoo. The bank reconciliation process will seamlessly match the SEPA orders you sent to your bank
with actual bank statements.

Configuration
=============

Activate the SEPA Credit Transfer (SCT)
---------------------------------------

To pay suppliers with SEPA, you must activate the **SEPA Credit Transfer** setting.
To do so, go to :menuselection:`Accounting app --> Configuration --> Settings -->
Vendor Payments: --> SEPA Credit Transfer (SCT)`. By activating the setting and filling in with your
company data, you will be able to add the SCT option when paying your vendor.

.. note::

   According to the localization package installed, the **SEPA Direct Debit** and
   **SEPA Credit Transfer** modules may be installed by default. If not, they need to be installed.
   You can see how in the :doc:`/applications/general/apps_modules` page.

Activate SEPA payment methods on banks
--------------------------------------

From the accounting dashboard, click on the drop-down menu (:guilabel:`⋮`) on your bank journal and
go to :guilabel:`Configuration`. To activate SEPA, click the :guilabel:`Outgoing Payments` tab for
outgoing payments. You can add, if not already present, SEPA Credit Transfer as a payment method.

Make sure to specify the IBAN account number (domestic account number do not work with SEPA) and the
BIC (bank identifier code) in the :guilabel:`Journal Entries` tab.

Registering Payments
--------------------

You can register and vendor payments made with SEPA. To do so, go to
:menuselection:`Accounting app --> Purchases --> Payments`. Register your payment and select a
payment method by Sepa Credit Transfer.

The first time you pay a vendor with SEPA, you will have to fill in the
:guilabel:`Recipient Bank Account` field with the bank name, IBAN, and BIC (Bank Identifier Code).
Odoo automatically verifies if the IBAN format is respected.

For future payments to this vendor, Odoo will automatically suggest you the bank account, but it
remains possible to select a new one.
Once your payment is registered, do not forget to confirm it. You can also pay vendor bills from the
bill directly using the :guilabel:`Register Payment` button at the top of a vendor bill.
The form is the same, but the payment is directly linked to the bill and will be automatically
reconciled with it.