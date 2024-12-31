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


class UpdateVMMetadataBody(object):
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
        'metadata': 'dict(str, str)',
        'merge': 'bool'
    }

    attribute_map = {
        'metadata': 'metadata',
        'merge': 'merge'
    }

    def __init__(self, metadata=None, merge=None, _configuration=None):  # noqa: E501
        """UpdateVMMetadataBody - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._metadata = None
        self._merge = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if merge is not None:
            self.merge = merge

    @property
    def metadata(self):
        """Gets the metadata of this UpdateVMMetadataBody.  # noqa: E501


        :return: The metadata of this UpdateVMMetadataBody.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this UpdateVMMetadataBody.


        :param metadata: The metadata of this UpdateVMMetadataBody.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def merge(self):
        """Gets the merge of this UpdateVMMetadataBody.  # noqa: E501


        :return: The merge of this UpdateVMMetadataBody.  # noqa: E501
        :rtype: bool
        """
        return self._merge

    @merge.setter
    def merge(self, merge):
        """Sets the merge of this UpdateVMMetadataBody.


        :param merge: The merge of this UpdateVMMetadataBody.  # noqa: E501
        :type: bool
        """

        self._merge = merge

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
        if issubclass(UpdateVMMetadataBody, dict):
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
        if not isinstance(other, UpdateVMMetadataBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateVMMetadataBody):
            return True

        return self.to_dict() != other.to_dict()
