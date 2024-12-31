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


class DiskStoragePriceHr(object):
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
        'storage_class': 'VMDataCenterStorageClass',
        'disk_gib_price_hr': 'Decimal',
        'snapshot_gib_price_hr': 'Decimal'
    }

    attribute_map = {
        'storage_class': 'storageClass',
        'disk_gib_price_hr': 'diskGibPriceHr',
        'snapshot_gib_price_hr': 'snapshotGibPriceHr'
    }

    def __init__(self, storage_class=None, disk_gib_price_hr=None, snapshot_gib_price_hr=None, _configuration=None):  # noqa: E501
        """DiskStoragePriceHr - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._storage_class = None
        self._disk_gib_price_hr = None
        self._snapshot_gib_price_hr = None
        self.discriminator = None

        if storage_class is not None:
            self.storage_class = storage_class
        if disk_gib_price_hr is not None:
            self.disk_gib_price_hr = disk_gib_price_hr
        if snapshot_gib_price_hr is not None:
            self.snapshot_gib_price_hr = snapshot_gib_price_hr

    @property
    def storage_class(self):
        """Gets the storage_class of this DiskStoragePriceHr.  # noqa: E501


        :return: The storage_class of this DiskStoragePriceHr.  # noqa: E501
        :rtype: VMDataCenterStorageClass
        """
        return self._storage_class

    @storage_class.setter
    def storage_class(self, storage_class):
        """Sets the storage_class of this DiskStoragePriceHr.


        :param storage_class: The storage_class of this DiskStoragePriceHr.  # noqa: E501
        :type: VMDataCenterStorageClass
        """

        self._storage_class = storage_class

    @property
    def disk_gib_price_hr(self):
        """Gets the disk_gib_price_hr of this DiskStoragePriceHr.  # noqa: E501


        :return: The disk_gib_price_hr of this DiskStoragePriceHr.  # noqa: E501
        :rtype: Decimal
        """
        return self._disk_gib_price_hr

    @disk_gib_price_hr.setter
    def disk_gib_price_hr(self, disk_gib_price_hr):
        """Sets the disk_gib_price_hr of this DiskStoragePriceHr.


        :param disk_gib_price_hr: The disk_gib_price_hr of this DiskStoragePriceHr.  # noqa: E501
        :type: Decimal
        """

        self._disk_gib_price_hr = disk_gib_price_hr

    @property
    def snapshot_gib_price_hr(self):
        """Gets the snapshot_gib_price_hr of this DiskStoragePriceHr.  # noqa: E501


        :return: The snapshot_gib_price_hr of this DiskStoragePriceHr.  # noqa: E501
        :rtype: Decimal
        """
        return self._snapshot_gib_price_hr

    @snapshot_gib_price_hr.setter
    def snapshot_gib_price_hr(self, snapshot_gib_price_hr):
        """Sets the snapshot_gib_price_hr of this DiskStoragePriceHr.


        :param snapshot_gib_price_hr: The snapshot_gib_price_hr of this DiskStoragePriceHr.  # noqa: E501
        :type: Decimal
        """

        self._snapshot_gib_price_hr = snapshot_gib_price_hr

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
        if issubclass(DiskStoragePriceHr, dict):
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
        if not isinstance(other, DiskStoragePriceHr):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DiskStoragePriceHr):
            return True

        return self.to_dict() != other.to_dict()
