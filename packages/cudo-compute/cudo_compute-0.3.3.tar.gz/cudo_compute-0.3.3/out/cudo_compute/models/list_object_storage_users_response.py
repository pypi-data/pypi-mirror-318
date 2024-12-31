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


class ListObjectStorageUsersResponse(object):
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
        'users': 'list[ObjectStorageUser]',
        'total_count': 'int',
        'page_number': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'users': 'users',
        'total_count': 'totalCount',
        'page_number': 'pageNumber',
        'page_size': 'pageSize'
    }

    def __init__(self, users=None, total_count=None, page_number=None, page_size=None, _configuration=None):  # noqa: E501
        """ListObjectStorageUsersResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._users = None
        self._total_count = None
        self._page_number = None
        self._page_size = None
        self.discriminator = None

        self.users = users
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size

    @property
    def users(self):
        """Gets the users of this ListObjectStorageUsersResponse.  # noqa: E501


        :return: The users of this ListObjectStorageUsersResponse.  # noqa: E501
        :rtype: list[ObjectStorageUser]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this ListObjectStorageUsersResponse.


        :param users: The users of this ListObjectStorageUsersResponse.  # noqa: E501
        :type: list[ObjectStorageUser]
        """
        if self._configuration.client_side_validation and users is None:
            raise ValueError("Invalid value for `users`, must not be `None`")  # noqa: E501

        self._users = users

    @property
    def total_count(self):
        """Gets the total_count of this ListObjectStorageUsersResponse.  # noqa: E501


        :return: The total_count of this ListObjectStorageUsersResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListObjectStorageUsersResponse.


        :param total_count: The total_count of this ListObjectStorageUsersResponse.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and total_count is None:
            raise ValueError("Invalid value for `total_count`, must not be `None`")  # noqa: E501

        self._total_count = total_count

    @property
    def page_number(self):
        """Gets the page_number of this ListObjectStorageUsersResponse.  # noqa: E501


        :return: The page_number of this ListObjectStorageUsersResponse.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ListObjectStorageUsersResponse.


        :param page_number: The page_number of this ListObjectStorageUsersResponse.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and page_number is None:
            raise ValueError("Invalid value for `page_number`, must not be `None`")  # noqa: E501

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this ListObjectStorageUsersResponse.  # noqa: E501


        :return: The page_size of this ListObjectStorageUsersResponse.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListObjectStorageUsersResponse.


        :param page_size: The page_size of this ListObjectStorageUsersResponse.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and page_size is None:
            raise ValueError("Invalid value for `page_size`, must not be `None`")  # noqa: E501

        self._page_size = page_size

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
        if issubclass(ListObjectStorageUsersResponse, dict):
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
        if not isinstance(other, ListObjectStorageUsersResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListObjectStorageUsersResponse):
            return True

        return self.to_dict() != other.to_dict()
