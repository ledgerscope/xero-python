# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class SalaryAndWage(BaseModel):
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
        "salary_and_wages_id": "str",
        "earnings_rate_id": "str",
        "number_of_units_per_week": "float",
        "rate_per_unit": "float",
        "number_of_units_per_day": "float",
        "effective_from": "date",
        "annual_salary": "float",
        "status": "str",
        "payment_type": "str",
    }

    attribute_map = {
        "salary_and_wages_id": "salaryAndWagesID",
        "earnings_rate_id": "earningsRateID",
        "number_of_units_per_week": "numberOfUnitsPerWeek",
        "rate_per_unit": "ratePerUnit",
        "number_of_units_per_day": "numberOfUnitsPerDay",
        "effective_from": "effectiveFrom",
        "annual_salary": "annualSalary",
        "status": "status",
        "payment_type": "paymentType",
    }

    def __init__(
        self,
        salary_and_wages_id=None,
        earnings_rate_id=None,
        number_of_units_per_week=None,
        rate_per_unit=None,
        number_of_units_per_day=None,
        effective_from=None,
        annual_salary=None,
        status=None,
        payment_type=None,
    ):  # noqa: E501
        """SalaryAndWage - a model defined in OpenAPI"""  # noqa: E501

        self._salary_and_wages_id = None
        self._earnings_rate_id = None
        self._number_of_units_per_week = None
        self._rate_per_unit = None
        self._number_of_units_per_day = None
        self._effective_from = None
        self._annual_salary = None
        self._status = None
        self._payment_type = None
        self.discriminator = None

        if salary_and_wages_id is not None:
            self.salary_and_wages_id = salary_and_wages_id
        self.earnings_rate_id = earnings_rate_id
        self.number_of_units_per_week = number_of_units_per_week
        if rate_per_unit is not None:
            self.rate_per_unit = rate_per_unit
        if number_of_units_per_day is not None:
            self.number_of_units_per_day = number_of_units_per_day
        self.effective_from = effective_from
        self.annual_salary = annual_salary
        self.status = status
        self.payment_type = payment_type

    @property
    def salary_and_wages_id(self):
        """Gets the salary_and_wages_id of this SalaryAndWage.  # noqa: E501

        Xero unique identifier for a salary and wages record  # noqa: E501

        :return: The salary_and_wages_id of this SalaryAndWage.  # noqa: E501
        :rtype: str
        """
        return self._salary_and_wages_id

    @salary_and_wages_id.setter
    def salary_and_wages_id(self, salary_and_wages_id):
        """Sets the salary_and_wages_id of this SalaryAndWage.

        Xero unique identifier for a salary and wages record  # noqa: E501

        :param salary_and_wages_id: The salary_and_wages_id of this SalaryAndWage.  # noqa: E501
        :type: str
        """

        self._salary_and_wages_id = salary_and_wages_id

    @property
    def earnings_rate_id(self):
        """Gets the earnings_rate_id of this SalaryAndWage.  # noqa: E501

        Xero unique identifier for an earnings rate  # noqa: E501

        :return: The earnings_rate_id of this SalaryAndWage.  # noqa: E501
        :rtype: str
        """
        return self._earnings_rate_id

    @earnings_rate_id.setter
    def earnings_rate_id(self, earnings_rate_id):
        """Sets the earnings_rate_id of this SalaryAndWage.

        Xero unique identifier for an earnings rate  # noqa: E501

        :param earnings_rate_id: The earnings_rate_id of this SalaryAndWage.  # noqa: E501
        :type: str
        """
        if earnings_rate_id is None:
            raise ValueError(
                "Invalid value for `earnings_rate_id`, must not be `None`"
            )  # noqa: E501

        self._earnings_rate_id = earnings_rate_id

    @property
    def number_of_units_per_week(self):
        """Gets the number_of_units_per_week of this SalaryAndWage.  # noqa: E501

        The Number of Units per week for the corresponding salary and wages  # noqa: E501

        :return: The number_of_units_per_week of this SalaryAndWage.  # noqa: E501
        :rtype: float
        """
        return self._number_of_units_per_week

    @number_of_units_per_week.setter
    def number_of_units_per_week(self, number_of_units_per_week):
        """Sets the number_of_units_per_week of this SalaryAndWage.

        The Number of Units per week for the corresponding salary and wages  # noqa: E501

        :param number_of_units_per_week: The number_of_units_per_week of this SalaryAndWage.  # noqa: E501
        :type: float
        """
        if number_of_units_per_week is None:
            raise ValueError(
                "Invalid value for `number_of_units_per_week`, must not be `None`"
            )  # noqa: E501

        self._number_of_units_per_week = number_of_units_per_week

    @property
    def rate_per_unit(self):
        """Gets the rate_per_unit of this SalaryAndWage.  # noqa: E501

        The rate of each unit for the corresponding salary and wages  # noqa: E501

        :return: The rate_per_unit of this SalaryAndWage.  # noqa: E501
        :rtype: float
        """
        return self._rate_per_unit

    @rate_per_unit.setter
    def rate_per_unit(self, rate_per_unit):
        """Sets the rate_per_unit of this SalaryAndWage.

        The rate of each unit for the corresponding salary and wages  # noqa: E501

        :param rate_per_unit: The rate_per_unit of this SalaryAndWage.  # noqa: E501
        :type: float
        """

        self._rate_per_unit = rate_per_unit

    @property
    def number_of_units_per_day(self):
        """Gets the number_of_units_per_day of this SalaryAndWage.  # noqa: E501

        The Number of Units per day for the corresponding salary and wages  # noqa: E501

        :return: The number_of_units_per_day of this SalaryAndWage.  # noqa: E501
        :rtype: float
        """
        return self._number_of_units_per_day

    @number_of_units_per_day.setter
    def number_of_units_per_day(self, number_of_units_per_day):
        """Sets the number_of_units_per_day of this SalaryAndWage.

        The Number of Units per day for the corresponding salary and wages  # noqa: E501

        :param number_of_units_per_day: The number_of_units_per_day of this SalaryAndWage.  # noqa: E501
        :type: float
        """

        self._number_of_units_per_day = number_of_units_per_day

    @property
    def effective_from(self):
        """Gets the effective_from of this SalaryAndWage.  # noqa: E501

        The effective date of the corresponding salary and wages  # noqa: E501

        :return: The effective_from of this SalaryAndWage.  # noqa: E501
        :rtype: date
        """
        return self._effective_from

    @effective_from.setter
    def effective_from(self, effective_from):
        """Sets the effective_from of this SalaryAndWage.

        The effective date of the corresponding salary and wages  # noqa: E501

        :param effective_from: The effective_from of this SalaryAndWage.  # noqa: E501
        :type: date
        """
        if effective_from is None:
            raise ValueError(
                "Invalid value for `effective_from`, must not be `None`"
            )  # noqa: E501

        self._effective_from = effective_from

    @property
    def annual_salary(self):
        """Gets the annual_salary of this SalaryAndWage.  # noqa: E501

        The annual salary  # noqa: E501

        :return: The annual_salary of this SalaryAndWage.  # noqa: E501
        :rtype: float
        """
        return self._annual_salary

    @annual_salary.setter
    def annual_salary(self, annual_salary):
        """Sets the annual_salary of this SalaryAndWage.

        The annual salary  # noqa: E501

        :param annual_salary: The annual_salary of this SalaryAndWage.  # noqa: E501
        :type: float
        """
        if annual_salary is None:
            raise ValueError(
                "Invalid value for `annual_salary`, must not be `None`"
            )  # noqa: E501

        self._annual_salary = annual_salary

    @property
    def status(self):
        """Gets the status of this SalaryAndWage.  # noqa: E501

        The current status of the corresponding salary and wages  # noqa: E501

        :return: The status of this SalaryAndWage.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SalaryAndWage.

        The current status of the corresponding salary and wages  # noqa: E501

        :param status: The status of this SalaryAndWage.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError(
                "Invalid value for `status`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["Active", "Pending", "History", "None"]  # noqa: E501

        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                        status, allowed_values
                    )
                )

        self._status = status

    @property
    def payment_type(self):
        """Gets the payment_type of this SalaryAndWage.  # noqa: E501

        The type of the payment of the corresponding salary and wages  # noqa: E501

        :return: The payment_type of this SalaryAndWage.  # noqa: E501
        :rtype: str
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this SalaryAndWage.

        The type of the payment of the corresponding salary and wages  # noqa: E501

        :param payment_type: The payment_type of this SalaryAndWage.  # noqa: E501
        :type: str
        """
        if payment_type is None:
            raise ValueError(
                "Invalid value for `payment_type`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["Salary", "Hourly", "None"]  # noqa: E501

        if payment_type:
            if payment_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `payment_type` ({0}), must be one of {1}".format(  # noqa: E501
                        payment_type, allowed_values
                    )
                )

        self._payment_type = payment_type
