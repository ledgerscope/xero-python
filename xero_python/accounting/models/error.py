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


class Error(BaseModel):
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
        "error_number": "int",
        "type": "str",
        "message": "str",
        "elements": "list[Element]",
    }

    attribute_map = {
        "error_number": "ErrorNumber",
        "type": "Type",
        "message": "Message",
        "elements": "Elements",
    }

    def __init__(
        self, error_number=None, type=None, message=None, elements=None
    ):  # noqa: E501
        """Error - a model defined in OpenAPI"""  # noqa: E501

        self._error_number = None
        self._type = None
        self._message = None
        self._elements = None
        self.discriminator = None

        if error_number is not None:
            self.error_number = error_number
        if type is not None:
            self.type = type
        if message is not None:
            self.message = message
        if elements is not None:
            self.elements = elements

    @property
    def error_number(self):
        """Gets the error_number of this Error.  # noqa: E501

        Exception number  # noqa: E501

        :return: The error_number of this Error.  # noqa: E501
        :rtype: int
        """
        return self._error_number

    @error_number.setter
    def error_number(self, error_number):
        """Sets the error_number of this Error.

        Exception number  # noqa: E501

        :param error_number: The error_number of this Error.  # noqa: E501
        :type: int
        """

        self._error_number = error_number

    @property
    def type(self):
        """Gets the type of this Error.  # noqa: E501

        Exception type  # noqa: E501

        :return: The type of this Error.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Error.

        Exception type  # noqa: E501

        :param type: The type of this Error.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def message(self):
        """Gets the message of this Error.  # noqa: E501

        Exception message  # noqa: E501

        :return: The message of this Error.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Error.

        Exception message  # noqa: E501

        :param message: The message of this Error.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def elements(self):
        """Gets the elements of this Error.  # noqa: E501

        Array of Elements of validation Errors  # noqa: E501

        :return: The elements of this Error.  # noqa: E501
        :rtype: list[Element]
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """Sets the elements of this Error.

        Array of Elements of validation Errors  # noqa: E501

        :param elements: The elements of this Error.  # noqa: E501
        :type: list[Element]
        """

        self._elements = elements
