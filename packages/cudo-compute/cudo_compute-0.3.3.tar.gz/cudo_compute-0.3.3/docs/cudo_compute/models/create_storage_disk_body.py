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


class CreateStorageDiskBody(object):
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
        'disk': 'Disk'
    }

    attribute_map = {
        'data_center_id': 'dataCenterId',
        'disk': 'disk'
    }

    def __init__(self, data_center_id=None, disk=None, _configuration=None):  # noqa: E501
        """CreateStorageDiskBody - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._data_center_id = None
        self._disk = None
        self.discriminator = None

        if data_center_id is not None:
            self.data_center_id = data_center_id
        if disk is not None:
            self.disk = disk

    @property
    def data_center_id(self):
        """Gets the data_center_id of this CreateStorageDiskBody.  # noqa: E501


        :return: The data_center_id of this CreateStorageDiskBody.  # noqa: E501
        :rtype: str
        """
        return self._data_center_id

    @data_center_id.setter
    def data_center_id(self, data_center_id):
        """Sets the data_center_id of this CreateStorageDiskBody.


        :param data_center_id: The data_center_id of this CreateStorageDiskBody.  # noqa: E501
        :type: str
        """

        self._data_center_id = data_center_id

    @property
    def disk(self):
        """Gets the disk of this CreateStorageDiskBody.  # noqa: E501


        :return: The disk of this CreateStorageDiskBody.  # noqa: E501
        :rtype: Disk
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """Sets the disk of this CreateStorageDiskBody.


        :param disk: The disk of this CreateStorageDiskBody.  # noqa: E501
        :type: Disk
        """

        self._disk = disk

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
        if issubclass(CreateStorageDiskBody, dict):
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
        if not isinstance(other, CreateStorageDiskBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateStorageDiskBody):
            return True

        return self.to_dict() != other.to_dict()
