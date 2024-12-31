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

from src.cudo_compute.configuration import Configuration


class RemoveProjectUserPermissionBody(object):
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
        'data_center_id': 'str',
        'billing_account_id': 'str',
        'user_id': 'str',
        'role': 'Role'
    }

    attribute_map = {
        'data_center_id': 'dataCenterId',
        'billing_account_id': 'billingAccountId',
        'user_id': 'userId',
        'role': 'role'
    }

    def __init__(self, data_center_id=None, billing_account_id=None, user_id=None, role=None, _configuration=None):  # noqa: E501
        """RemoveProjectUserPermissionBody - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._data_center_id = None
        self._billing_account_id = None
        self._user_id = None
        self._role = None
        self.discriminator = None

        if data_center_id is not None:
            self.data_center_id = data_center_id
        if billing_account_id is not None:
            self.billing_account_id = billing_account_id
        self.user_id = user_id
        self.role = role

    @property
    def data_center_id(self):
        """Gets the data_center_id of this RemoveProjectUserPermissionBody.  # noqa: E501


        :return: The data_center_id of this RemoveProjectUserPermissionBody.  # noqa: E501
        :rtype: str
        """
        return self._data_center_id

    @data_center_id.setter
    def data_center_id(self, data_center_id):
        """Sets the data_center_id of this RemoveProjectUserPermissionBody.


        :param data_center_id: The data_center_id of this RemoveProjectUserPermissionBody.  # noqa: E501
        :type: str
        """

        self._data_center_id = data_center_id

    @property
    def billing_account_id(self):
        """Gets the billing_account_id of this RemoveProjectUserPermissionBody.  # noqa: E501


        :return: The billing_account_id of this RemoveProjectUserPermissionBody.  # noqa: E501
        :rtype: str
        """
        return self._billing_account_id

    @billing_account_id.setter
    def billing_account_id(self, billing_account_id):
        """Sets the billing_account_id of this RemoveProjectUserPermissionBody.


        :param billing_account_id: The billing_account_id of this RemoveProjectUserPermissionBody.  # noqa: E501
        :type: str
        """

        self._billing_account_id = billing_account_id

    @property
    def user_id(self):
        """Gets the user_id of this RemoveProjectUserPermissionBody.  # noqa: E501


        :return: The user_id of this RemoveProjectUserPermissionBody.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this RemoveProjectUserPermissionBody.


        :param user_id: The user_id of this RemoveProjectUserPermissionBody.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def role(self):
        """Gets the role of this RemoveProjectUserPermissionBody.  # noqa: E501


        :return: The role of this RemoveProjectUserPermissionBody.  # noqa: E501
        :rtype: Role
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this RemoveProjectUserPermissionBody.


        :param role: The role of this RemoveProjectUserPermissionBody.  # noqa: E501
        :type: Role
        """
        if self._configuration.client_side_validation and role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

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
        if issubclass(RemoveProjectUserPermissionBody, dict):
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
        if not isinstance(other, RemoveProjectUserPermissionBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RemoveProjectUserPermissionBody):
            return True

        return self.to_dict() != other.to_dict()
