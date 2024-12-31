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


class ListDataCenterMachineTypePricesResponseMachineTypePrice(object):
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
        'uid': 'str',
        'machine_type': 'str',
        'commitment_term': 'str',
        'gpu_price_hr': 'Decimal',
        'vcpu_price_hr': 'Decimal',
        'memory_gib_price_hr': 'Decimal'
    }

    attribute_map = {
        'uid': 'uid',
        'machine_type': 'machineType',
        'commitment_term': 'commitmentTerm',
        'gpu_price_hr': 'gpuPriceHr',
        'vcpu_price_hr': 'vcpuPriceHr',
        'memory_gib_price_hr': 'memoryGibPriceHr'
    }

    def __init__(self, uid=None, machine_type=None, commitment_term=None, gpu_price_hr=None, vcpu_price_hr=None, memory_gib_price_hr=None, _configuration=None):  # noqa: E501
        """ListDataCenterMachineTypePricesResponseMachineTypePrice - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._uid = None
        self._machine_type = None
        self._commitment_term = None
        self._gpu_price_hr = None
        self._vcpu_price_hr = None
        self._memory_gib_price_hr = None
        self.discriminator = None

        self.uid = uid
        self.machine_type = machine_type
        self.commitment_term = commitment_term
        self.gpu_price_hr = gpu_price_hr
        self.vcpu_price_hr = vcpu_price_hr
        self.memory_gib_price_hr = memory_gib_price_hr

    @property
    def uid(self):
        """Gets the uid of this ListDataCenterMachineTypePricesResponseMachineTypePrice.  # noqa: E501


        :return: The uid of this ListDataCenterMachineTypePricesResponseMachineTypePrice.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ListDataCenterMachineTypePricesResponseMachineTypePrice.


        :param uid: The uid of this ListDataCenterMachineTypePricesResponseMachineTypePrice.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

    @property
    def machine_type(self):
        """Gets the machine_type of this ListDataCenterMachineTypePricesResponseMachineTypePrice.  # noqa: E501


        :return: The machine_type of this ListDataCenterMachineTypePricesResponseMachineTypePrice.  # noqa: E501
        :rtype: str
        """
        return self._machine_type

    @machine_type.setter
    def machine_type(self, machine_type):
        """Sets the machine_type of this ListDataCenterMachineTypePricesResponseMachineTypePrice.


        :param machine_type: The machine_type of this ListDataCenterMachineTypePricesResponseMachineTypePrice.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and machine_type is None:
            raise ValueError("Invalid value for `machine_type`, must not be `None`")  # noqa: E501

        self._machine_type = machine_type

    @property
    def commitment_term(self):
        """Gets the commitment_term of this ListDataCenterMachineTypePricesResponseMachineTypePrice.  # noqa: E501


        :return: The commitment_term of this ListDataCenterMachineTypePricesResponseMachineTypePrice.  # noqa: E501
        :rtype: str
        """
        return self._commitment_term

    @commitment_term.setter
    def commitment_term(self, commitment_term):
        """Sets the commitment_term of this ListDataCenterMachineTypePricesResponseMachineTypePrice.


        :param commitment_term: The commitment_term of this ListDataCenterMachineTypePricesResponseMachineTypePrice.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and commitment_term is None:
            raise ValueError("Invalid value for `commitment_term`, must not be `None`")  # noqa: E501

        self._commitment_term = commitment_term

    @property
    def gpu_price_hr(self):
        """Gets the gpu_price_hr of this ListDataCenterMachineTypePricesResponseMachineTypePrice.  # noqa: E501


        :return: The gpu_price_hr of this ListDataCenterMachineTypePricesResponseMachineTypePrice.  # noqa: E501
        :rtype: Decimal
        """
        return self._gpu_price_hr

    @gpu_price_hr.setter
    def gpu_price_hr(self, gpu_price_hr):
        """Sets the gpu_price_hr of this ListDataCenterMachineTypePricesResponseMachineTypePrice.


        :param gpu_price_hr: The gpu_price_hr of this ListDataCenterMachineTypePricesResponseMachineTypePrice.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and gpu_price_hr is None:
            raise ValueError("Invalid value for `gpu_price_hr`, must not be `None`")  # noqa: E501

        self._gpu_price_hr = gpu_price_hr

    @property
    def vcpu_price_hr(self):
        """Gets the vcpu_price_hr of this ListDataCenterMachineTypePricesResponseMachineTypePrice.  # noqa: E501


        :return: The vcpu_price_hr of this ListDataCenterMachineTypePricesResponseMachineTypePrice.  # noqa: E501
        :rtype: Decimal
        """
        return self._vcpu_price_hr

    @vcpu_price_hr.setter
    def vcpu_price_hr(self, vcpu_price_hr):
        """Sets the vcpu_price_hr of this ListDataCenterMachineTypePricesResponseMachineTypePrice.


        :param vcpu_price_hr: The vcpu_price_hr of this ListDataCenterMachineTypePricesResponseMachineTypePrice.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and vcpu_price_hr is None:
            raise ValueError("Invalid value for `vcpu_price_hr`, must not be `None`")  # noqa: E501

        self._vcpu_price_hr = vcpu_price_hr

    @property
    def memory_gib_price_hr(self):
        """Gets the memory_gib_price_hr of this ListDataCenterMachineTypePricesResponseMachineTypePrice.  # noqa: E501


        :return: The memory_gib_price_hr of this ListDataCenterMachineTypePricesResponseMachineTypePrice.  # noqa: E501
        :rtype: Decimal
        """
        return self._memory_gib_price_hr

    @memory_gib_price_hr.setter
    def memory_gib_price_hr(self, memory_gib_price_hr):
        """Sets the memory_gib_price_hr of this ListDataCenterMachineTypePricesResponseMachineTypePrice.


        :param memory_gib_price_hr: The memory_gib_price_hr of this ListDataCenterMachineTypePricesResponseMachineTypePrice.  # noqa: E501
        :type: Decimal
        """
        if self._configuration.client_side_validation and memory_gib_price_hr is None:
            raise ValueError("Invalid value for `memory_gib_price_hr`, must not be `None`")  # noqa: E501

        self._memory_gib_price_hr = memory_gib_price_hr

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
        if issubclass(ListDataCenterMachineTypePricesResponseMachineTypePrice, dict):
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
        if not isinstance(other, ListDataCenterMachineTypePricesResponseMachineTypePrice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListDataCenterMachineTypePricesResponseMachineTypePrice):
            return True

        return self.to_dict() != other.to_dict()
