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


class ImageResult(object):
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
        'id': 'str',
        'data_center_id': 'str',
        'size_gib': 'int',
        'create_time': 'datetime'
    }

    attribute_map = {
        'project_id': 'projectId',
        'id': 'id',
        'data_center_id': 'dataCenterId',
        'size_gib': 'sizeGib',
        'create_time': 'createTime'
    }

    def __init__(self, project_id=None, id=None, data_center_id=None, size_gib=None, create_time=None, _configuration=None):  # noqa: E501
        """ImageResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._project_id = None
        self._id = None
        self._data_center_id = None
        self._size_gib = None
        self._create_time = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if id is not None:
            self.id = id
        if data_center_id is not None:
            self.data_center_id = data_center_id
        if size_gib is not None:
            self.size_gib = size_gib
        if create_time is not None:
            self.create_time = create_time

    @property
    def project_id(self):
        """Gets the project_id of this ImageResult.  # noqa: E501


        :return: The project_id of this ImageResult.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ImageResult.


        :param project_id: The project_id of this ImageResult.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def id(self):
        """Gets the id of this ImageResult.  # noqa: E501


        :return: The id of this ImageResult.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImageResult.


        :param id: The id of this ImageResult.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def data_center_id(self):
        """Gets the data_center_id of this ImageResult.  # noqa: E501


        :return: The data_center_id of this ImageResult.  # noqa: E501
        :rtype: str
        """
        return self._data_center_id

    @data_center_id.setter
    def data_center_id(self, data_center_id):
        """Sets the data_center_id of this ImageResult.


        :param data_center_id: The data_center_id of this ImageResult.  # noqa: E501
        :type: str
        """

        self._data_center_id = data_center_id

    @property
    def size_gib(self):
        """Gets the size_gib of this ImageResult.  # noqa: E501


        :return: The size_gib of this ImageResult.  # noqa: E501
        :rtype: int
        """
        return self._size_gib

    @size_gib.setter
    def size_gib(self, size_gib):
        """Sets the size_gib of this ImageResult.


        :param size_gib: The size_gib of this ImageResult.  # noqa: E501
        :type: int
        """

        self._size_gib = size_gib

    @property
    def create_time(self):
        """Gets the create_time of this ImageResult.  # noqa: E501


        :return: The create_time of this ImageResult.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ImageResult.


        :param create_time: The create_time of this ImageResult.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

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
        if issubclass(ImageResult, dict):
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
        if not isinstance(other, ImageResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImageResult):
            return True

        return self.to_dict() != other.to_dict()
