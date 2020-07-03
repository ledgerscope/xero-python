# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.2.6
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class ExpenseClaim(BaseModel):
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
        "expense_claim_id": "str",
        "status": "str",
        "payments": "list[Payment]",
        "user": "User",
        "receipts": "list[Receipt]",
        "updated_date_utc": "datetime[ms-format]",
        "total": "float",
        "amount_due": "float",
        "amount_paid": "float",
        "payment_due_date": "date[ms-format]",
        "reporting_date": "date[ms-format]",
        "receipt_id": "str",
    }

    attribute_map = {
        "expense_claim_id": "ExpenseClaimID",
        "status": "Status",
        "payments": "Payments",
        "user": "User",
        "receipts": "Receipts",
        "updated_date_utc": "UpdatedDateUTC",
        "total": "Total",
        "amount_due": "AmountDue",
        "amount_paid": "AmountPaid",
        "payment_due_date": "PaymentDueDate",
        "reporting_date": "ReportingDate",
        "receipt_id": "ReceiptID",
    }

    def __init__(
        self,
        expense_claim_id=None,
        status=None,
        payments=None,
        user=None,
        receipts=None,
        updated_date_utc=None,
        total=None,
        amount_due=None,
        amount_paid=None,
        payment_due_date=None,
        reporting_date=None,
        receipt_id=None,
    ):  # noqa: E501
        """ExpenseClaim - a model defined in OpenAPI"""  # noqa: E501

        self._expense_claim_id = None
        self._status = None
        self._payments = None
        self._user = None
        self._receipts = None
        self._updated_date_utc = None
        self._total = None
        self._amount_due = None
        self._amount_paid = None
        self._payment_due_date = None
        self._reporting_date = None
        self._receipt_id = None
        self.discriminator = None

        if expense_claim_id is not None:
            self.expense_claim_id = expense_claim_id
        if status is not None:
            self.status = status
        if payments is not None:
            self.payments = payments
        if user is not None:
            self.user = user
        if receipts is not None:
            self.receipts = receipts
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if total is not None:
            self.total = total
        if amount_due is not None:
            self.amount_due = amount_due
        if amount_paid is not None:
            self.amount_paid = amount_paid
        if payment_due_date is not None:
            self.payment_due_date = payment_due_date
        if reporting_date is not None:
            self.reporting_date = reporting_date
        if receipt_id is not None:
            self.receipt_id = receipt_id

    @property
    def expense_claim_id(self):
        """Gets the expense_claim_id of this ExpenseClaim.  # noqa: E501

        Xero generated unique identifier for an expense claim  # noqa: E501

        :return: The expense_claim_id of this ExpenseClaim.  # noqa: E501
        :rtype: str
        """
        return self._expense_claim_id

    @expense_claim_id.setter
    def expense_claim_id(self, expense_claim_id):
        """Sets the expense_claim_id of this ExpenseClaim.

        Xero generated unique identifier for an expense claim  # noqa: E501

        :param expense_claim_id: The expense_claim_id of this ExpenseClaim.  # noqa: E501
        :type: str
        """

        self._expense_claim_id = expense_claim_id

    @property
    def status(self):
        """Gets the status of this ExpenseClaim.  # noqa: E501

        Current status of an expense claim – see status types  # noqa: E501

        :return: The status of this ExpenseClaim.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExpenseClaim.

        Current status of an expense claim – see status types  # noqa: E501

        :param status: The status of this ExpenseClaim.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "SUBMITTED",
            "AUTHORISED",
            "PAID",
            "VOIDED",
            "DELETED",
        ]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                    status, allowed_values
                )
            )

        self._status = status

    @property
    def payments(self):
        """Gets the payments of this ExpenseClaim.  # noqa: E501

        See Payments  # noqa: E501

        :return: The payments of this ExpenseClaim.  # noqa: E501
        :rtype: list[Payment]
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this ExpenseClaim.

        See Payments  # noqa: E501

        :param payments: The payments of this ExpenseClaim.  # noqa: E501
        :type: list[Payment]
        """

        self._payments = payments

    @property
    def user(self):
        """Gets the user of this ExpenseClaim.  # noqa: E501


        :return: The user of this ExpenseClaim.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ExpenseClaim.


        :param user: The user of this ExpenseClaim.  # noqa: E501
        :type: User
        """

        self._user = user

    @property
    def receipts(self):
        """Gets the receipts of this ExpenseClaim.  # noqa: E501


        :return: The receipts of this ExpenseClaim.  # noqa: E501
        :rtype: list[Receipt]
        """
        return self._receipts

    @receipts.setter
    def receipts(self, receipts):
        """Sets the receipts of this ExpenseClaim.


        :param receipts: The receipts of this ExpenseClaim.  # noqa: E501
        :type: list[Receipt]
        """

        self._receipts = receipts

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this ExpenseClaim.  # noqa: E501

        Last modified date UTC format  # noqa: E501

        :return: The updated_date_utc of this ExpenseClaim.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this ExpenseClaim.

        Last modified date UTC format  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this ExpenseClaim.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def total(self):
        """Gets the total of this ExpenseClaim.  # noqa: E501

        The total of an expense claim being paid  # noqa: E501

        :return: The total of this ExpenseClaim.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ExpenseClaim.

        The total of an expense claim being paid  # noqa: E501

        :param total: The total of this ExpenseClaim.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def amount_due(self):
        """Gets the amount_due of this ExpenseClaim.  # noqa: E501

        The amount due to be paid for an expense claim  # noqa: E501

        :return: The amount_due of this ExpenseClaim.  # noqa: E501
        :rtype: float
        """
        return self._amount_due

    @amount_due.setter
    def amount_due(self, amount_due):
        """Sets the amount_due of this ExpenseClaim.

        The amount due to be paid for an expense claim  # noqa: E501

        :param amount_due: The amount_due of this ExpenseClaim.  # noqa: E501
        :type: float
        """

        self._amount_due = amount_due

    @property
    def amount_paid(self):
        """Gets the amount_paid of this ExpenseClaim.  # noqa: E501

        The amount still to pay for an expense claim  # noqa: E501

        :return: The amount_paid of this ExpenseClaim.  # noqa: E501
        :rtype: float
        """
        return self._amount_paid

    @amount_paid.setter
    def amount_paid(self, amount_paid):
        """Sets the amount_paid of this ExpenseClaim.

        The amount still to pay for an expense claim  # noqa: E501

        :param amount_paid: The amount_paid of this ExpenseClaim.  # noqa: E501
        :type: float
        """

        self._amount_paid = amount_paid

    @property
    def payment_due_date(self):
        """Gets the payment_due_date of this ExpenseClaim.  # noqa: E501

        The date when the expense claim is due to be paid YYYY-MM-DD  # noqa: E501

        :return: The payment_due_date of this ExpenseClaim.  # noqa: E501
        :rtype: date
        """
        return self._payment_due_date

    @payment_due_date.setter
    def payment_due_date(self, payment_due_date):
        """Sets the payment_due_date of this ExpenseClaim.

        The date when the expense claim is due to be paid YYYY-MM-DD  # noqa: E501

        :param payment_due_date: The payment_due_date of this ExpenseClaim.  # noqa: E501
        :type: date
        """

        self._payment_due_date = payment_due_date

    @property
    def reporting_date(self):
        """Gets the reporting_date of this ExpenseClaim.  # noqa: E501

        The date the expense claim will be reported in Xero YYYY-MM-DD  # noqa: E501

        :return: The reporting_date of this ExpenseClaim.  # noqa: E501
        :rtype: date
        """
        return self._reporting_date

    @reporting_date.setter
    def reporting_date(self, reporting_date):
        """Sets the reporting_date of this ExpenseClaim.

        The date the expense claim will be reported in Xero YYYY-MM-DD  # noqa: E501

        :param reporting_date: The reporting_date of this ExpenseClaim.  # noqa: E501
        :type: date
        """

        self._reporting_date = reporting_date

    @property
    def receipt_id(self):
        """Gets the receipt_id of this ExpenseClaim.  # noqa: E501

        The Xero identifier for the Receipt e.g.  e59a2c7f-1306-4078-a0f3-73537afcbba9  # noqa: E501

        :return: The receipt_id of this ExpenseClaim.  # noqa: E501
        :rtype: str
        """
        return self._receipt_id

    @receipt_id.setter
    def receipt_id(self, receipt_id):
        """Sets the receipt_id of this ExpenseClaim.

        The Xero identifier for the Receipt e.g.  e59a2c7f-1306-4078-a0f3-73537afcbba9  # noqa: E501

        :param receipt_id: The receipt_id of this ExpenseClaim.  # noqa: E501
        :type: str
        """

        self._receipt_id = receipt_id
