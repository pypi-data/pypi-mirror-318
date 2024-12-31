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


class SshKey(object):
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
        'id': 'str',
        'create_time': 'datetime',
        'public_key': 'str',
        'fingerprint': 'str',
        'type': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'createTime',
        'public_key': 'publicKey',
        'fingerprint': 'fingerprint',
        'type': 'type',
        'comment': 'comment'
    }

    def __init__(self, id=None, create_time=None, public_key=None, fingerprint=None, type=None, comment=None, _configuration=None):  # noqa: E501
        """SshKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._create_time = None
        self._public_key = None
        self._fingerprint = None
        self._type = None
        self._comment = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_time is not None:
            self.create_time = create_time
        self.public_key = public_key
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if type is not None:
            self.type = type
        if comment is not None:
            self.comment = comment

    @property
    def id(self):
        """Gets the id of this SshKey.  # noqa: E501


        :return: The id of this SshKey.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SshKey.


        :param id: The id of this SshKey.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this SshKey.  # noqa: E501


        :return: The create_time of this SshKey.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this SshKey.


        :param create_time: The create_time of this SshKey.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def public_key(self):
        """Gets the public_key of this SshKey.  # noqa: E501


        :return: The public_key of this SshKey.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this SshKey.


        :param public_key: The public_key of this SshKey.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and public_key is None:
            raise ValueError("Invalid value for `public_key`, must not be `None`")  # noqa: E501

        self._public_key = public_key

    @property
    def fingerprint(self):
        """Gets the fingerprint of this SshKey.  # noqa: E501


        :return: The fingerprint of this SshKey.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this SshKey.


        :param fingerprint: The fingerprint of this SshKey.  # noqa: E501
        :type: str
        """

        self._fingerprint = fingerprint

    @property
    def type(self):
        """Gets the type of this SshKey.  # noqa: E501


        :return: The type of this SshKey.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SshKey.


        :param type: The type of this SshKey.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def comment(self):
        """Gets the comment of this SshKey.  # noqa: E501


        :return: The comment of this SshKey.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this SshKey.


        :param comment: The comment of this SshKey.  # noqa: E501
        :type: str
        """

        self._comment = comment

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
        if issubclass(SshKey, dict):
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
        if not isinstance(other, SshKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SshKey):
            return True

        return self.to_dict() != other.to_dict()
