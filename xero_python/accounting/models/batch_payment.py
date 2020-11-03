# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.4.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class BatchPayment(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "account": "Account",
        "reference": "str",
        "particulars": "str",
        "code": "str",
        "details": "str",
        "narrative": "str",
        "batch_payment_id": "str",
        "date_string": "str",
        "date": "date[ms-format]",
        "amount": "float",
        "payments": "list[Payment]",
        "type": "str",
        "status": "str",
        "total_amount": "str",
        "updated_date_utc": "datetime[ms-format]",
        "is_reconciled": "str",
    }

    attribute_map = {
        "account": "Account",
        "reference": "Reference",
        "particulars": "Particulars",
        "code": "Code",
        "details": "Details",
        "narrative": "Narrative",
        "batch_payment_id": "BatchPaymentID",
        "date_string": "DateString",
        "date": "Date",
        "amount": "Amount",
        "payments": "Payments",
        "type": "Type",
        "status": "Status",
        "total_amount": "TotalAmount",
        "updated_date_utc": "UpdatedDateUTC",
        "is_reconciled": "IsReconciled",
    }

    def __init__(
        self,
        account=None,
        reference=None,
        particulars=None,
        code=None,
        details=None,
        narrative=None,
        batch_payment_id=None,
        date_string=None,
        date=None,
        amount=None,
        payments=None,
        type=None,
        status=None,
        total_amount=None,
        updated_date_utc=None,
        is_reconciled=None,
    ):  # noqa: E501
        """BatchPayment - a model defined in OpenAPI"""  # noqa: E501

        self._account = None
        self._reference = None
        self._particulars = None
        self._code = None
        self._details = None
        self._narrative = None
        self._batch_payment_id = None
        self._date_string = None
        self._date = None
        self._amount = None
        self._payments = None
        self._type = None
        self._status = None
        self._total_amount = None
        self._updated_date_utc = None
        self._is_reconciled = None
        self.discriminator = None

        if account is not None:
            self.account = account
        if reference is not None:
            self.reference = reference
        if particulars is not None:
            self.particulars = particulars
        if code is not None:
            self.code = code
        if details is not None:
            self.details = details
        if narrative is not None:
            self.narrative = narrative
        if batch_payment_id is not None:
            self.batch_payment_id = batch_payment_id
        if date_string is not None:
            self.date_string = date_string
        if date is not None:
            self.date = date
        if amount is not None:
            self.amount = amount
        if payments is not None:
            self.payments = payments
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if total_amount is not None:
            self.total_amount = total_amount
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if is_reconciled is not None:
            self.is_reconciled = is_reconciled

    @property
    def account(self):
        """Gets the account of this BatchPayment.  # noqa: E501


        :return: The account of this BatchPayment.  # noqa: E501
        :rtype: Account
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this BatchPayment.


        :param account: The account of this BatchPayment.  # noqa: E501
        :type: Account
        """

        self._account = account

    @property
    def reference(self):
        """Gets the reference of this BatchPayment.  # noqa: E501

        (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero.  # noqa: E501

        :return: The reference of this BatchPayment.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this BatchPayment.

        (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero.  # noqa: E501

        :param reference: The reference of this BatchPayment.  # noqa: E501
        :type: str
        """
        if reference is not None and len(reference) > 12:
            raise ValueError(
                "Invalid value for `reference`, "
                "length must be less than or equal to `12`"
            )  # noqa: E501

        self._reference = reference

    @property
    def particulars(self):
        """Gets the particulars of this BatchPayment.  # noqa: E501

        (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero.  # noqa: E501

        :return: The particulars of this BatchPayment.  # noqa: E501
        :rtype: str
        """
        return self._particulars

    @particulars.setter
    def particulars(self, particulars):
        """Sets the particulars of this BatchPayment.

        (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero.  # noqa: E501

        :param particulars: The particulars of this BatchPayment.  # noqa: E501
        :type: str
        """
        if particulars is not None and len(particulars) > 12:
            raise ValueError(
                "Invalid value for `particulars`, "
                "length must be less than or equal to `12`"
            )  # noqa: E501

        self._particulars = particulars

    @property
    def code(self):
        """Gets the code of this BatchPayment.  # noqa: E501

        (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero.  # noqa: E501

        :return: The code of this BatchPayment.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this BatchPayment.

        (NZ Only) Optional references for the batch payment transaction. It will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement you import into Xero.  # noqa: E501

        :param code: The code of this BatchPayment.  # noqa: E501
        :type: str
        """
        if code is not None and len(code) > 12:
            raise ValueError(
                "Invalid value for `code`, " "length must be less than or equal to `12`"
            )  # noqa: E501

        self._code = code

    @property
    def details(self):
        """Gets the details of this BatchPayment.  # noqa: E501

        (Non-NZ Only) These details are sent to the org’s bank as a reference for the batch payment transaction. They will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement imported into Xero. Maximum field length = 18  # noqa: E501

        :return: The details of this BatchPayment.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this BatchPayment.

        (Non-NZ Only) These details are sent to the org’s bank as a reference for the batch payment transaction. They will also show with the batch payment transaction in the bank reconciliation Find & Match screen. Depending on your individual bank, the detail may also show on the bank statement imported into Xero. Maximum field length = 18  # noqa: E501

        :param details: The details of this BatchPayment.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def narrative(self):
        """Gets the narrative of this BatchPayment.  # noqa: E501

        (UK Only) Only shows on the statement line in Xero. Max length =18  # noqa: E501

        :return: The narrative of this BatchPayment.  # noqa: E501
        :rtype: str
        """
        return self._narrative

    @narrative.setter
    def narrative(self, narrative):
        """Sets the narrative of this BatchPayment.

        (UK Only) Only shows on the statement line in Xero. Max length =18  # noqa: E501

        :param narrative: The narrative of this BatchPayment.  # noqa: E501
        :type: str
        """
        if narrative is not None and len(narrative) > 18:
            raise ValueError(
                "Invalid value for `narrative`, "
                "length must be less than or equal to `18`"
            )  # noqa: E501

        self._narrative = narrative

    @property
    def batch_payment_id(self):
        """Gets the batch_payment_id of this BatchPayment.  # noqa: E501

        The Xero generated unique identifier for the bank transaction (read-only)  # noqa: E501

        :return: The batch_payment_id of this BatchPayment.  # noqa: E501
        :rtype: str
        """
        return self._batch_payment_id

    @batch_payment_id.setter
    def batch_payment_id(self, batch_payment_id):
        """Sets the batch_payment_id of this BatchPayment.

        The Xero generated unique identifier for the bank transaction (read-only)  # noqa: E501

        :param batch_payment_id: The batch_payment_id of this BatchPayment.  # noqa: E501
        :type: str
        """

        self._batch_payment_id = batch_payment_id

    @property
    def date_string(self):
        """Gets the date_string of this BatchPayment.  # noqa: E501

        Date the payment is being made (YYYY-MM-DD) e.g. 2009-09-06  # noqa: E501

        :return: The date_string of this BatchPayment.  # noqa: E501
        :rtype: str
        """
        return self._date_string

    @date_string.setter
    def date_string(self, date_string):
        """Sets the date_string of this BatchPayment.

        Date the payment is being made (YYYY-MM-DD) e.g. 2009-09-06  # noqa: E501

        :param date_string: The date_string of this BatchPayment.  # noqa: E501
        :type: str
        """

        self._date_string = date_string

    @property
    def date(self):
        """Gets the date of this BatchPayment.  # noqa: E501

        Date the payment is being made (YYYY-MM-DD) e.g. 2009-09-06  # noqa: E501

        :return: The date of this BatchPayment.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this BatchPayment.

        Date the payment is being made (YYYY-MM-DD) e.g. 2009-09-06  # noqa: E501

        :param date: The date of this BatchPayment.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def amount(self):
        """Gets the amount of this BatchPayment.  # noqa: E501

        The amount of the payment. Must be less than or equal to the outstanding amount owing on the invoice e.g. 200.00  # noqa: E501

        :return: The amount of this BatchPayment.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this BatchPayment.

        The amount of the payment. Must be less than or equal to the outstanding amount owing on the invoice e.g. 200.00  # noqa: E501

        :param amount: The amount of this BatchPayment.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def payments(self):
        """Gets the payments of this BatchPayment.  # noqa: E501

        An array of payments  # noqa: E501

        :return: The payments of this BatchPayment.  # noqa: E501
        :rtype: list[Payment]
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this BatchPayment.

        An array of payments  # noqa: E501

        :param payments: The payments of this BatchPayment.  # noqa: E501
        :type: list[Payment]
        """

        self._payments = payments

    @property
    def type(self):
        """Gets the type of this BatchPayment.  # noqa: E501

        PAYBATCH for bill payments or RECBATCH for sales invoice payments (read-only)  # noqa: E501

        :return: The type of this BatchPayment.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BatchPayment.

        PAYBATCH for bill payments or RECBATCH for sales invoice payments (read-only)  # noqa: E501

        :param type: The type of this BatchPayment.  # noqa: E501
        :type: str
        """
        allowed_values = ["PAYBATCH", "RECBATCH", "None"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}".format(  # noqa: E501
                    type, allowed_values
                )
            )

        self._type = type

    @property
    def status(self):
        """Gets the status of this BatchPayment.  # noqa: E501

        AUTHORISED or DELETED (read-only). New batch payments will have a status of AUTHORISED. It is not possible to delete batch payments via the API.  # noqa: E501

        :return: The status of this BatchPayment.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BatchPayment.

        AUTHORISED or DELETED (read-only). New batch payments will have a status of AUTHORISED. It is not possible to delete batch payments via the API.  # noqa: E501

        :param status: The status of this BatchPayment.  # noqa: E501
        :type: str
        """
        allowed_values = ["AUTHORISED", "DELETED", "None"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                    status, allowed_values
                )
            )

        self._status = status

    @property
    def total_amount(self):
        """Gets the total_amount of this BatchPayment.  # noqa: E501

        The total of the payments that make up the batch (read-only)  # noqa: E501

        :return: The total_amount of this BatchPayment.  # noqa: E501
        :rtype: str
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this BatchPayment.

        The total of the payments that make up the batch (read-only)  # noqa: E501

        :param total_amount: The total_amount of this BatchPayment.  # noqa: E501
        :type: str
        """

        self._total_amount = total_amount

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this BatchPayment.  # noqa: E501

        UTC timestamp of last update to the payment  # noqa: E501

        :return: The updated_date_utc of this BatchPayment.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this BatchPayment.

        UTC timestamp of last update to the payment  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this BatchPayment.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def is_reconciled(self):
        """Gets the is_reconciled of this BatchPayment.  # noqa: E501

        Booelan that tells you if the batch payment has been reconciled (read-only)  # noqa: E501

        :return: The is_reconciled of this BatchPayment.  # noqa: E501
        :rtype: str
        """
        return self._is_reconciled

    @is_reconciled.setter
    def is_reconciled(self, is_reconciled):
        """Sets the is_reconciled of this BatchPayment.

        Booelan that tells you if the batch payment has been reconciled (read-only)  # noqa: E501

        :param is_reconciled: The is_reconciled of this BatchPayment.  # noqa: E501
        :type: str
        """

        self._is_reconciled = is_reconciled
