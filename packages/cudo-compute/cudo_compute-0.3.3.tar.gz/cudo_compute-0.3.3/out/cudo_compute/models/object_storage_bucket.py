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


class ObjectStorageBucket(object):
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
        'project_id': 'str',
        'data_center_id': 'str',
        'id': 'str',
        'endpoint': 'str',
        'object_count': 'str',
        'size_bytes': 'str',
        'billable_bytes': 'str',
        'storage_gib_price_hr': 'Decimal'
    }

    attribute_map = {
        'project_id': 'projectId',
        'data_center_id': 'dataCenterId',
        'id': 'id',
        'endpoint': 'endpoint',
        'object_count': 'objectCount',
        'size_bytes': 'sizeBytes',
        'billable_bytes': 'billableBytes',
        'storage_gib_price_hr': 'storageGibPriceHr'
    }

    def __init__(self, project_id=None, data_center_id=None, id=None, endpoint=None, object_count=None, size_bytes=None, billable_bytes=None, storage_gib_price_hr=None, _configuration=None):  # noqa: E501
        """ObjectStorageBucket - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._project_id = None
        self._data_center_id = None
        self._id = None
        self._endpoint = None
        self._object_count = None
        self._size_bytes = None
        self._billable_bytes = None
        self._storage_gib_price_hr = None
        self.discriminator = None

        self.project_id = project_id
        self.data_center_id = data_center_id
        self.id = id
        if endpoint is not None:
            self.endpoint = endpoint
        if object_count is not None:
            self.object_count = object_count
        if size_bytes is not None:
            self.size_bytes = size_bytes
        if billable_bytes is not None:
            self.billable_bytes = billable_bytes
        if storage_gib_price_hr is not None:
            self.storage_gib_price_hr = storage_gib_price_hr

    @property
    def project_id(self):
        """Gets the project_id of this ObjectStorageBucket.  # noqa: E501


        :return: The project_id of this ObjectStorageBucket.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ObjectStorageBucket.


        :param project_id: The project_id of this ObjectStorageBucket.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and project_id is None:
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def data_center_id(self):
        """Gets the data_center_id of this ObjectStorageBucket.  # noqa: E501


        :return: The data_center_id of this ObjectStorageBucket.  # noqa: E501
        :rtype: str
        """
        return self._data_center_id

    @data_center_id.setter
    def data_center_id(self, data_center_id):
        """Sets the data_center_id of this ObjectStorageBucket.


        :param data_center_id: The data_center_id of this ObjectStorageBucket.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and data_center_id is None:
            raise ValueError("Invalid value for `data_center_id`, must not be `None`")  # noqa: E501

        self._data_center_id = data_center_id

    @property
    def id(self):
        """Gets the id of this ObjectStorageBucket.  # noqa: E501


        :return: The id of this ObjectStorageBucket.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ObjectStorageBucket.


        :param id: The id of this ObjectStorageBucket.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def endpoint(self):
        """Gets the endpoint of this ObjectStorageBucket.  # noqa: E501


        :return: The endpoint of this ObjectStorageBucket.  # noqa: E501
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """Sets the endpoint of this ObjectStorageBucket.


        :param endpoint: The endpoint of this ObjectStorageBucket.  # noqa: E501
        :type: str
        """

        self._endpoint = endpoint

    @property
    def object_count(self):
        """Gets the object_count of this ObjectStorageBucket.  # noqa: E501


        :return: The object_count of this ObjectStorageBucket.  # noqa: E501
        :rtype: str
        """
        return self._object_count

    @object_count.setter
    def object_count(self, object_count):
        """Sets the object_count of this ObjectStorageBucket.


        :param object_count: The object_count of this ObjectStorageBucket.  # noqa: E501
        :type: str
        """

        self._object_count = object_count

    @property
    def size_bytes(self):
        """Gets the size_bytes of this ObjectStorageBucket.  # noqa: E501


        :return: The size_bytes of this ObjectStorageBucket.  # noqa: E501
        :rtype: str
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this ObjectStorageBucket.


        :param size_bytes: The size_bytes of this ObjectStorageBucket.  # noqa: E501
        :type: str
        """

        self._size_bytes = size_bytes

    @property
    def billable_bytes(self):
        """Gets the billable_bytes of this ObjectStorageBucket.  # noqa: E501


        :return: The billable_bytes of this ObjectStorageBucket.  # noqa: E501
        :rtype: str
        """
        return self._billable_bytes

    @billable_bytes.setter
    def billable_bytes(self, billable_bytes):
        """Sets the billable_bytes of this ObjectStorageBucket.


        :param billable_bytes: The billable_bytes of this ObjectStorageBucket.  # noqa: E501
        :type: str
        """

        self._billable_bytes = billable_bytes

    @property
    def storage_gib_price_hr(self):
        """Gets the storage_gib_price_hr of this ObjectStorageBucket.  # noqa: E501


        :return: The storage_gib_price_hr of this ObjectStorageBucket.  # noqa: E501
        :rtype: Decimal
        """
        return self._storage_gib_price_hr

    @storage_gib_price_hr.setter
    def storage_gib_price_hr(self, storage_gib_price_hr):
        """Sets the storage_gib_price_hr of this ObjectStorageBucket.


        :param storage_gib_price_hr: The storage_gib_price_hr of this ObjectStorageBucket.  # noqa: E501
        :type: Decimal
        """

        self._storage_gib_price_hr = storage_gib_price_hr

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
        if issubclass(ObjectStorageBucket, dict):
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
        if not isinstance(other, ObjectStorageBucket):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ObjectStorageBucket):
            return True

        return self.to_dict() != other.to_dict()
