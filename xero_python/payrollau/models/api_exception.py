# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    OpenAPI spec version: 2.4.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class APIException(BaseModel):
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
    openapi_types = {"error_number": "float", "type": "str", "message": "str"}

    attribute_map = {
        "error_number": "ErrorNumber",
        "type": "Type",
        "message": "Message",
    }

    def __init__(self, error_number=None, type=None, message=None):  # noqa: E501
        """APIException - a model defined in OpenAPI"""  # noqa: E501

        self._error_number = None
        self._type = None
        self._message = None
        self.discriminator = None

        if error_number is not None:
            self.error_number = error_number
        if type is not None:
            self.type = type
        if message is not None:
            self.message = message

    @property
    def error_number(self):
        """Gets the error_number of this APIException.  # noqa: E501

        The error number  # noqa: E501

        :return: The error_number of this APIException.  # noqa: E501
        :rtype: float
        """
        return self._error_number

    @error_number.setter
    def error_number(self, error_number):
        """Sets the error_number of this APIException.

        The error number  # noqa: E501

        :param error_number: The error_number of this APIException.  # noqa: E501
        :type: float
        """

        self._error_number = error_number

    @property
    def type(self):
        """Gets the type of this APIException.  # noqa: E501

        The type of error  # noqa: E501

        :return: The type of this APIException.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this APIException.

        The type of error  # noqa: E501

        :param type: The type of this APIException.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def message(self):
        """Gets the message of this APIException.  # noqa: E501

        The message describing the error  # noqa: E501

        :return: The message of this APIException.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this APIException.

        The message describing the error  # noqa: E501

        :param message: The message of this APIException.  # noqa: E501
        :type: str
        """

        self._message = message
