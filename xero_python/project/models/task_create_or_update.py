# coding: utf-8

"""
    Xero Projects API

    This is the Xero Projects API  # noqa: E501

    OpenAPI spec version: 2.2.6
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class TaskCreateOrUpdate(BaseModel):
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
        "name": "str",
        "rate": "Amount",
        "charge_type": "ChargeType",
        "estimate_minutes": "int",
    }

    attribute_map = {
        "name": "name",
        "rate": "rate",
        "charge_type": "chargeType",
        "estimate_minutes": "estimateMinutes",
    }

    def __init__(
        self, name=None, rate=None, charge_type=None, estimate_minutes=None
    ):  # noqa: E501
        """TaskCreateOrUpdate - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._rate = None
        self._charge_type = None
        self._estimate_minutes = None
        self.discriminator = None

        self.name = name
        self.rate = rate
        self.charge_type = charge_type
        if estimate_minutes is not None:
            self.estimate_minutes = estimate_minutes

    @property
    def name(self):
        """Gets the name of this TaskCreateOrUpdate.  # noqa: E501

        Name of the task. Max length 100 characters.  # noqa: E501

        :return: The name of this TaskCreateOrUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskCreateOrUpdate.

        Name of the task. Max length 100 characters.  # noqa: E501

        :param name: The name of this TaskCreateOrUpdate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def rate(self):
        """Gets the rate of this TaskCreateOrUpdate.  # noqa: E501


        :return: The rate of this TaskCreateOrUpdate.  # noqa: E501
        :rtype: Amount
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this TaskCreateOrUpdate.


        :param rate: The rate of this TaskCreateOrUpdate.  # noqa: E501
        :type: Amount
        """
        if rate is None:
            raise ValueError(
                "Invalid value for `rate`, must not be `None`"
            )  # noqa: E501

        self._rate = rate

    @property
    def charge_type(self):
        """Gets the charge_type of this TaskCreateOrUpdate.  # noqa: E501


        :return: The charge_type of this TaskCreateOrUpdate.  # noqa: E501
        :rtype: ChargeType
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this TaskCreateOrUpdate.


        :param charge_type: The charge_type of this TaskCreateOrUpdate.  # noqa: E501
        :type: ChargeType
        """
        if charge_type is None:
            raise ValueError(
                "Invalid value for `charge_type`, must not be `None`"
            )  # noqa: E501

        self._charge_type = charge_type

    @property
    def estimate_minutes(self):
        """Gets the estimate_minutes of this TaskCreateOrUpdate.  # noqa: E501

        Estimated time to perform the task. EstimateMinutes has to be greater than 0 if provided.  # noqa: E501

        :return: The estimate_minutes of this TaskCreateOrUpdate.  # noqa: E501
        :rtype: int
        """
        return self._estimate_minutes

    @estimate_minutes.setter
    def estimate_minutes(self, estimate_minutes):
        """Sets the estimate_minutes of this TaskCreateOrUpdate.

        Estimated time to perform the task. EstimateMinutes has to be greater than 0 if provided.  # noqa: E501

        :param estimate_minutes: The estimate_minutes of this TaskCreateOrUpdate.  # noqa: E501
        :type: int
        """

        self._estimate_minutes = estimate_minutes
