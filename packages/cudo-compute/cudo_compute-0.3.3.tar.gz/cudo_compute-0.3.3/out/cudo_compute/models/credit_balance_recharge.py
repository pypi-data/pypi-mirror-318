# coding: utf-8

"""
    Cudo Compute service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cudo_compute.configuration import Configuration


class CreditBalanceRecharge(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'low': 'Decimal',
        'high': 'Decimal',
        'auto_recharge': 'bool',
        'transaction': 'Transaction'
    }

    attribute_map = {
        'low': 'low',
        'high': 'high',
        'auto_recharge': 'autoRecharge',
        'transaction': 'transaction'
    }

    def __init__(self, low=None, high=None, auto_recharge=None, transaction=None, _configuration=None):  # noqa: E501
        """CreditBalanceRecharge - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._low = None
        self._high = None
        self._auto_recharge = None
        self._transaction = None
        self.discriminator = None

        self.low = low
        self.high = high
        self.auto_recharge = auto_recharge
        if transaction is not None:
            self.transaction = transaction

    @property
    def low(self):
        """Gets the low of this CreditBalanceRecharge.  # noqa: E501


        :return: The low of this CreditBalanceRecharge.  # noqa: E501
        :rtype: Decimal
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this CreditBalanceRecharge.


        :param low: The low of this CreditBalanceRecharge.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and low is None:
            raise ValueError("Invalid value for `low`, must not be `None`")  # noqa: E501

        self._low = low

    @property
    def high(self):
        """Gets the high of this CreditBalanceRecharge.  # noqa: E501


        :return: The high of this CreditBalanceRecharge.  # noqa: E501
        :rtype: Decimal
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this CreditBalanceRecharge.


        :param high: The high of this CreditBalanceRecharge.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and high is None:
            raise ValueError("Invalid value for `high`, must not be `None`")  # noqa: E501

        self._high = high

    @property
    def auto_recharge(self):
        """Gets the auto_recharge of this CreditBalanceRecharge.  # noqa: E501


        :return: The auto_recharge of this CreditBalanceRecharge.  # noqa: E501
        :rtype: bool
        """
        return self._auto_recharge

    @auto_recharge.setter
    def auto_recharge(self, auto_recharge):
        """Sets the auto_recharge of this CreditBalanceRecharge.


        :param auto_recharge: The auto_recharge of this CreditBalanceRecharge.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and auto_recharge is None:
            raise ValueError("Invalid value for `auto_recharge`, must not be `None`")  # noqa: E501

        self._auto_recharge = auto_recharge

    @property
    def transaction(self):
        """Gets the transaction of this CreditBalanceRecharge.  # noqa: E501


        :return: The transaction of this CreditBalanceRecharge.  # noqa: E501
        :rtype: Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this CreditBalanceRecharge.


        :param transaction: The transaction of this CreditBalanceRecharge.  # noqa: E501
        :type: Transaction
        """

        self._transaction = transaction

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CreditBalanceRecharge, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreditBalanceRecharge):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreditBalanceRecharge):
            return True

        return self.to_dict() != other.to_dict()
