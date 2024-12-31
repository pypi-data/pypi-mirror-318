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


class ObjectStorageKey(object):
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
        'access_key': 'str',
        'create_by': 'str',
        'create_time': 'datetime',
        'id': 'str',
        'secret_key': 'str'
    }

    attribute_map = {
        'access_key': 'accessKey',
        'create_by': 'createBy',
        'create_time': 'createTime',
        'id': 'id',
        'secret_key': 'secretKey'
    }

    def __init__(self, access_key=None, create_by=None, create_time=None, id=None, secret_key=None, _configuration=None):  # noqa: E501
        """ObjectStorageKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_key = None
        self._create_by = None
        self._create_time = None
        self._id = None
        self._secret_key = None
        self.discriminator = None

        if access_key is not None:
            self.access_key = access_key
        if create_by is not None:
            self.create_by = create_by
        if create_time is not None:
            self.create_time = create_time
        if id is not None:
            self.id = id
        if secret_key is not None:
            self.secret_key = secret_key

    @property
    def access_key(self):
        """Gets the access_key of this ObjectStorageKey.  # noqa: E501


        :return: The access_key of this ObjectStorageKey.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this ObjectStorageKey.


        :param access_key: The access_key of this ObjectStorageKey.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    @property
    def create_by(self):
        """Gets the create_by of this ObjectStorageKey.  # noqa: E501


        :return: The create_by of this ObjectStorageKey.  # noqa: E501
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this ObjectStorageKey.


        :param create_by: The create_by of this ObjectStorageKey.  # noqa: E501
        :type: str
        """

        self._create_by = create_by

    @property
    def create_time(self):
        """Gets the create_time of this ObjectStorageKey.  # noqa: E501


        :return: The create_time of this ObjectStorageKey.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ObjectStorageKey.


        :param create_time: The create_time of this ObjectStorageKey.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def id(self):
        """Gets the id of this ObjectStorageKey.  # noqa: E501


        :return: The id of this ObjectStorageKey.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ObjectStorageKey.


        :param id: The id of this ObjectStorageKey.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def secret_key(self):
        """Gets the secret_key of this ObjectStorageKey.  # noqa: E501


        :return: The secret_key of this ObjectStorageKey.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this ObjectStorageKey.


        :param secret_key: The secret_key of this ObjectStorageKey.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

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
        if issubclass(ObjectStorageKey, dict):
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
        if not isinstance(other, ObjectStorageKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ObjectStorageKey):
            return True

        return self.to_dict() != other.to_dict()
