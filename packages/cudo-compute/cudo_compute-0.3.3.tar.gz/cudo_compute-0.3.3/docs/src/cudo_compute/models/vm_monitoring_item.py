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


class VMMonitoringItem(object):
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
        'cpu': 'float',
        'disk_rd_bytes': 'int',
        'disk_rd_iops': 'int',
        'disk_wr_bytes': 'int',
        'disk_wr_iops': 'int',
        'memory': 'int',
        'net_rx': 'int',
        'net_tx': 'int',
        'timestamp': 'str'
    }

    attribute_map = {
        'cpu': 'cpu',
        'disk_rd_bytes': 'diskRdBytes',
        'disk_rd_iops': 'diskRdIops',
        'disk_wr_bytes': 'diskWrBytes',
        'disk_wr_iops': 'diskWrIops',
        'memory': 'memory',
        'net_rx': 'netRx',
        'net_tx': 'netTx',
        'timestamp': 'timestamp'
    }

    def __init__(self, cpu=None, disk_rd_bytes=None, disk_rd_iops=None, disk_wr_bytes=None, disk_wr_iops=None, memory=None, net_rx=None, net_tx=None, timestamp=None, _configuration=None):  # noqa: E501
        """VMMonitoringItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cpu = None
        self._disk_rd_bytes = None
        self._disk_rd_iops = None
        self._disk_wr_bytes = None
        self._disk_wr_iops = None
        self._memory = None
        self._net_rx = None
        self._net_tx = None
        self._timestamp = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if disk_rd_bytes is not None:
            self.disk_rd_bytes = disk_rd_bytes
        if disk_rd_iops is not None:
            self.disk_rd_iops = disk_rd_iops
        if disk_wr_bytes is not None:
            self.disk_wr_bytes = disk_wr_bytes
        if disk_wr_iops is not None:
            self.disk_wr_iops = disk_wr_iops
        if memory is not None:
            self.memory = memory
        if net_rx is not None:
            self.net_rx = net_rx
        if net_tx is not None:
            self.net_tx = net_tx
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def cpu(self):
        """Gets the cpu of this VMMonitoringItem.  # noqa: E501


        :return: The cpu of this VMMonitoringItem.  # noqa: E501
        :rtype: float
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this VMMonitoringItem.


        :param cpu: The cpu of this VMMonitoringItem.  # noqa: E501
        :type: float
        """

        self._cpu = cpu

    @property
    def disk_rd_bytes(self):
        """Gets the disk_rd_bytes of this VMMonitoringItem.  # noqa: E501


        :return: The disk_rd_bytes of this VMMonitoringItem.  # noqa: E501
        :rtype: int
        """
        return self._disk_rd_bytes

    @disk_rd_bytes.setter
    def disk_rd_bytes(self, disk_rd_bytes):
        """Sets the disk_rd_bytes of this VMMonitoringItem.


        :param disk_rd_bytes: The disk_rd_bytes of this VMMonitoringItem.  # noqa: E501
        :type: int
        """

        self._disk_rd_bytes = disk_rd_bytes

    @property
    def disk_rd_iops(self):
        """Gets the disk_rd_iops of this VMMonitoringItem.  # noqa: E501


        :return: The disk_rd_iops of this VMMonitoringItem.  # noqa: E501
        :rtype: int
        """
        return self._disk_rd_iops

    @disk_rd_iops.setter
    def disk_rd_iops(self, disk_rd_iops):
        """Sets the disk_rd_iops of this VMMonitoringItem.


        :param disk_rd_iops: The disk_rd_iops of this VMMonitoringItem.  # noqa: E501
        :type: int
        """

        self._disk_rd_iops = disk_rd_iops

    @property
    def disk_wr_bytes(self):
        """Gets the disk_wr_bytes of this VMMonitoringItem.  # noqa: E501


        :return: The disk_wr_bytes of this VMMonitoringItem.  # noqa: E501
        :rtype: int
        """
        return self._disk_wr_bytes

    @disk_wr_bytes.setter
    def disk_wr_bytes(self, disk_wr_bytes):
        """Sets the disk_wr_bytes of this VMMonitoringItem.


        :param disk_wr_bytes: The disk_wr_bytes of this VMMonitoringItem.  # noqa: E501
        :type: int
        """

        self._disk_wr_bytes = disk_wr_bytes

    @property
    def disk_wr_iops(self):
        """Gets the disk_wr_iops of this VMMonitoringItem.  # noqa: E501


        :return: The disk_wr_iops of this VMMonitoringItem.  # noqa: E501
        :rtype: int
        """
        return self._disk_wr_iops

    @disk_wr_iops.setter
    def disk_wr_iops(self, disk_wr_iops):
        """Sets the disk_wr_iops of this VMMonitoringItem.


        :param disk_wr_iops: The disk_wr_iops of this VMMonitoringItem.  # noqa: E501
        :type: int
        """

        self._disk_wr_iops = disk_wr_iops

    @property
    def memory(self):
        """Gets the memory of this VMMonitoringItem.  # noqa: E501


        :return: The memory of this VMMonitoringItem.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this VMMonitoringItem.


        :param memory: The memory of this VMMonitoringItem.  # noqa: E501
        :type: int
        """

        self._memory = memory

    @property
    def net_rx(self):
        """Gets the net_rx of this VMMonitoringItem.  # noqa: E501


        :return: The net_rx of this VMMonitoringItem.  # noqa: E501
        :rtype: int
        """
        return self._net_rx

    @net_rx.setter
    def net_rx(self, net_rx):
        """Sets the net_rx of this VMMonitoringItem.


        :param net_rx: The net_rx of this VMMonitoringItem.  # noqa: E501
        :type: int
        """

        self._net_rx = net_rx

    @property
    def net_tx(self):
        """Gets the net_tx of this VMMonitoringItem.  # noqa: E501


        :return: The net_tx of this VMMonitoringItem.  # noqa: E501
        :rtype: int
        """
        return self._net_tx

    @net_tx.setter
    def net_tx(self, net_tx):
        """Sets the net_tx of this VMMonitoringItem.


        :param net_tx: The net_tx of this VMMonitoringItem.  # noqa: E501
        :type: int
        """

        self._net_tx = net_tx

    @property
    def timestamp(self):
        """Gets the timestamp of this VMMonitoringItem.  # noqa: E501


        :return: The timestamp of this VMMonitoringItem.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this VMMonitoringItem.


        :param timestamp: The timestamp of this VMMonitoringItem.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

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
        if issubclass(VMMonitoringItem, dict):
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
        if not isinstance(other, VMMonitoringItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VMMonitoringItem):
            return True

        return self.to_dict() != other.to_dict()
