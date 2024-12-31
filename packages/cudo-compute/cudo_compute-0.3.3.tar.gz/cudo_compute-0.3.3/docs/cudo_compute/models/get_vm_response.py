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


class GetVMResponse(object):
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
        'vm': 'VM',
        'vcpu_price_hr': 'Decimal',
        'total_vcpu_price_hr': 'Decimal',
        'memory_gib_price_hr': 'Decimal',
        'total_memory_price_hr': 'Decimal',
        'gpu_price_hr': 'Decimal',
        'total_gpu_price_hr': 'Decimal',
        'storage_gib_price_hr': 'Decimal',
        'total_storage_price_hr': 'Decimal',
        'ipv4_price_hr': 'Decimal',
        'total_price_hr': 'Decimal'
    }

    attribute_map = {
        'vm': 'VM',
        'vcpu_price_hr': 'vcpuPriceHr',
        'total_vcpu_price_hr': 'totalVcpuPriceHr',
        'memory_gib_price_hr': 'memoryGibPriceHr',
        'total_memory_price_hr': 'totalMemoryPriceHr',
        'gpu_price_hr': 'gpuPriceHr',
        'total_gpu_price_hr': 'totalGpuPriceHr',
        'storage_gib_price_hr': 'storageGibPriceHr',
        'total_storage_price_hr': 'totalStoragePriceHr',
        'ipv4_price_hr': 'ipv4PriceHr',
        'total_price_hr': 'totalPriceHr'
    }

    def __init__(self, vm=None, vcpu_price_hr=None, total_vcpu_price_hr=None, memory_gib_price_hr=None, total_memory_price_hr=None, gpu_price_hr=None, total_gpu_price_hr=None, storage_gib_price_hr=None, total_storage_price_hr=None, ipv4_price_hr=None, total_price_hr=None, _configuration=None):  # noqa: E501
        """GetVMResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._vm = None
        self._vcpu_price_hr = None
        self._total_vcpu_price_hr = None
        self._memory_gib_price_hr = None
        self._total_memory_price_hr = None
        self._gpu_price_hr = None
        self._total_gpu_price_hr = None
        self._storage_gib_price_hr = None
        self._total_storage_price_hr = None
        self._ipv4_price_hr = None
        self._total_price_hr = None
        self.discriminator = None

        self.vm = vm
        self.vcpu_price_hr = vcpu_price_hr
        self.total_vcpu_price_hr = total_vcpu_price_hr
        self.memory_gib_price_hr = memory_gib_price_hr
        self.total_memory_price_hr = total_memory_price_hr
        self.gpu_price_hr = gpu_price_hr
        self.total_gpu_price_hr = total_gpu_price_hr
        self.storage_gib_price_hr = storage_gib_price_hr
        self.total_storage_price_hr = total_storage_price_hr
        self.ipv4_price_hr = ipv4_price_hr
        self.total_price_hr = total_price_hr

    @property
    def vm(self):
        """Gets the vm of this GetVMResponse.  # noqa: E501


        :return: The vm of this GetVMResponse.  # noqa: E501
        :rtype: VM
        """
        return self._vm

    @vm.setter
    def vm(self, vm):
        """Sets the vm of this GetVMResponse.


        :param vm: The vm of this GetVMResponse.  # noqa: E501
        :type: VM
        """
        if self._configuration.client_side_validation and vm is None:
            raise ValueError("Invalid value for `vm`, must not be `None`")  # noqa: E501

        self._vm = vm

    @property
    def vcpu_price_hr(self):
        """Gets the vcpu_price_hr of this GetVMResponse.  # noqa: E501


        :return: The vcpu_price_hr of this GetVMResponse.  # noqa: E501
        :rtype: Decimal
        """
        return self._vcpu_price_hr

    @vcpu_price_hr.setter
    def vcpu_price_hr(self, vcpu_price_hr):
        """Sets the vcpu_price_hr of this GetVMResponse.


        :param vcpu_price_hr: The vcpu_price_hr of this GetVMResponse.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and vcpu_price_hr is None:
            raise ValueError("Invalid value for `vcpu_price_hr`, must not be `None`")  # noqa: E501

        self._vcpu_price_hr = vcpu_price_hr

    @property
    def total_vcpu_price_hr(self):
        """Gets the total_vcpu_price_hr of this GetVMResponse.  # noqa: E501


        :return: The total_vcpu_price_hr of this GetVMResponse.  # noqa: E501
        :rtype: Decimal
        """
        return self._total_vcpu_price_hr

    @total_vcpu_price_hr.setter
    def total_vcpu_price_hr(self, total_vcpu_price_hr):
        """Sets the total_vcpu_price_hr of this GetVMResponse.


        :param total_vcpu_price_hr: The total_vcpu_price_hr of this GetVMResponse.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and total_vcpu_price_hr is None:
            raise ValueError("Invalid value for `total_vcpu_price_hr`, must not be `None`")  # noqa: E501

        self._total_vcpu_price_hr = total_vcpu_price_hr

    @property
    def memory_gib_price_hr(self):
        """Gets the memory_gib_price_hr of this GetVMResponse.  # noqa: E501


        :return: The memory_gib_price_hr of this GetVMResponse.  # noqa: E501
        :rtype: Decimal
        """
        return self._memory_gib_price_hr

    @memory_gib_price_hr.setter
    def memory_gib_price_hr(self, memory_gib_price_hr):
        """Sets the memory_gib_price_hr of this GetVMResponse.


        :param memory_gib_price_hr: The memory_gib_price_hr of this GetVMResponse.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and memory_gib_price_hr is None:
            raise ValueError("Invalid value for `memory_gib_price_hr`, must not be `None`")  # noqa: E501

        self._memory_gib_price_hr = memory_gib_price_hr

    @property
    def total_memory_price_hr(self):
        """Gets the total_memory_price_hr of this GetVMResponse.  # noqa: E501


        :return: The total_memory_price_hr of this GetVMResponse.  # noqa: E501
        :rtype: Decimal
        """
        return self._total_memory_price_hr

    @total_memory_price_hr.setter
    def total_memory_price_hr(self, total_memory_price_hr):
        """Sets the total_memory_price_hr of this GetVMResponse.


        :param total_memory_price_hr: The total_memory_price_hr of this GetVMResponse.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and total_memory_price_hr is None:
            raise ValueError("Invalid value for `total_memory_price_hr`, must not be `None`")  # noqa: E501

        self._total_memory_price_hr = total_memory_price_hr

    @property
    def gpu_price_hr(self):
        """Gets the gpu_price_hr of this GetVMResponse.  # noqa: E501


        :return: The gpu_price_hr of this GetVMResponse.  # noqa: E501
        :rtype: Decimal
        """
        return self._gpu_price_hr

    @gpu_price_hr.setter
    def gpu_price_hr(self, gpu_price_hr):
        """Sets the gpu_price_hr of this GetVMResponse.


        :param gpu_price_hr: The gpu_price_hr of this GetVMResponse.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and gpu_price_hr is None:
            raise ValueError("Invalid value for `gpu_price_hr`, must not be `None`")  # noqa: E501

        self._gpu_price_hr = gpu_price_hr

    @property
    def total_gpu_price_hr(self):
        """Gets the total_gpu_price_hr of this GetVMResponse.  # noqa: E501


        :return: The total_gpu_price_hr of this GetVMResponse.  # noqa: E501
        :rtype: Decimal
        """
        return self._total_gpu_price_hr

    @total_gpu_price_hr.setter
    def total_gpu_price_hr(self, total_gpu_price_hr):
        """Sets the total_gpu_price_hr of this GetVMResponse.


        :param total_gpu_price_hr: The total_gpu_price_hr of this GetVMResponse.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and total_gpu_price_hr is None:
            raise ValueError("Invalid value for `total_gpu_price_hr`, must not be `None`")  # noqa: E501

        self._total_gpu_price_hr = total_gpu_price_hr

    @property
    def storage_gib_price_hr(self):
        """Gets the storage_gib_price_hr of this GetVMResponse.  # noqa: E501


        :return: The storage_gib_price_hr of this GetVMResponse.  # noqa: E501
        :rtype: Decimal
        """
        return self._storage_gib_price_hr

    @storage_gib_price_hr.setter
    def storage_gib_price_hr(self, storage_gib_price_hr):
        """Sets the storage_gib_price_hr of this GetVMResponse.


        :param storage_gib_price_hr: The storage_gib_price_hr of this GetVMResponse.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and storage_gib_price_hr is None:
            raise ValueError("Invalid value for `storage_gib_price_hr`, must not be `None`")  # noqa: E501

        self._storage_gib_price_hr = storage_gib_price_hr

    @property
    def total_storage_price_hr(self):
        """Gets the total_storage_price_hr of this GetVMResponse.  # noqa: E501


        :return: The total_storage_price_hr of this GetVMResponse.  # noqa: E501
        :rtype: Decimal
        """
        return self._total_storage_price_hr

    @total_storage_price_hr.setter
    def total_storage_price_hr(self, total_storage_price_hr):
        """Sets the total_storage_price_hr of this GetVMResponse.


        :param total_storage_price_hr: The total_storage_price_hr of this GetVMResponse.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and total_storage_price_hr is None:
            raise ValueError("Invalid value for `total_storage_price_hr`, must not be `None`")  # noqa: E501

        self._total_storage_price_hr = total_storage_price_hr

    @property
    def ipv4_price_hr(self):
        """Gets the ipv4_price_hr of this GetVMResponse.  # noqa: E501


        :return: The ipv4_price_hr of this GetVMResponse.  # noqa: E501
        :rtype: Decimal
        """
        return self._ipv4_price_hr

    @ipv4_price_hr.setter
    def ipv4_price_hr(self, ipv4_price_hr):
        """Sets the ipv4_price_hr of this GetVMResponse.


        :param ipv4_price_hr: The ipv4_price_hr of this GetVMResponse.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and ipv4_price_hr is None:
            raise ValueError("Invalid value for `ipv4_price_hr`, must not be `None`")  # noqa: E501

        self._ipv4_price_hr = ipv4_price_hr

    @property
    def total_price_hr(self):
        """Gets the total_price_hr of this GetVMResponse.  # noqa: E501


        :return: The total_price_hr of this GetVMResponse.  # noqa: E501
        :rtype: Decimal
        """
        return self._total_price_hr

    @total_price_hr.setter
    def total_price_hr(self, total_price_hr):
        """Sets the total_price_hr of this GetVMResponse.


        :param total_price_hr: The total_price_hr of this GetVMResponse.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and total_price_hr is None:
            raise ValueError("Invalid value for `total_price_hr`, must not be `None`")  # noqa: E501

        self._total_price_hr = total_price_hr

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
        if issubclass(GetVMResponse, dict):
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
        if not isinstance(other, GetVMResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetVMResponse):
            return True

        return self.to_dict() != other.to_dict()
