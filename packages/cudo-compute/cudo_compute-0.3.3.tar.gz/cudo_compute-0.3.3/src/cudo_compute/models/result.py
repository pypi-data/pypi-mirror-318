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


class Result(object):
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
        'resource_type': 'str',
        'resource_name': 'str',
        'score': 'float',
        'billing_account': 'BillingAccountResult',
        'project': 'ProjectResult',
        'virtual_machine': 'VirtualMachineResult',
        'disk': 'DiskResult',
        'image': 'ImageResult',
        'network': 'NetworkResult'
    }

    attribute_map = {
        'resource_type': 'resourceType',
        'resource_name': 'resourceName',
        'score': 'score',
        'billing_account': 'billingAccount',
        'project': 'project',
        'virtual_machine': 'virtualMachine',
        'disk': 'disk',
        'image': 'image',
        'network': 'network'
    }

    def __init__(self, resource_type=None, resource_name=None, score=None, billing_account=None, project=None, virtual_machine=None, disk=None, image=None, network=None, _configuration=None):  # noqa: E501
        """Result - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._resource_type = None
        self._resource_name = None
        self._score = None
        self._billing_account = None
        self._project = None
        self._virtual_machine = None
        self._disk = None
        self._image = None
        self._network = None
        self.discriminator = None

        if resource_type is not None:
            self.resource_type = resource_type
        if resource_name is not None:
            self.resource_name = resource_name
        if score is not None:
            self.score = score
        if billing_account is not None:
            self.billing_account = billing_account
        if project is not None:
            self.project = project
        if virtual_machine is not None:
            self.virtual_machine = virtual_machine
        if disk is not None:
            self.disk = disk
        if image is not None:
            self.image = image
        if network is not None:
            self.network = network

    @property
    def resource_type(self):
        """Gets the resource_type of this Result.  # noqa: E501


        :return: The resource_type of this Result.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Result.


        :param resource_type: The resource_type of this Result.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def resource_name(self):
        """Gets the resource_name of this Result.  # noqa: E501


        :return: The resource_name of this Result.  # noqa: E501
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this Result.


        :param resource_name: The resource_name of this Result.  # noqa: E501
        :type: str
        """

        self._resource_name = resource_name

    @property
    def score(self):
        """Gets the score of this Result.  # noqa: E501


        :return: The score of this Result.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this Result.


        :param score: The score of this Result.  # noqa: E501
        :type: float
        """

        self._score = score

    @property
    def billing_account(self):
        """Gets the billing_account of this Result.  # noqa: E501


        :return: The billing_account of this Result.  # noqa: E501
        :rtype: BillingAccountResult
        """
        return self._billing_account

    @billing_account.setter
    def billing_account(self, billing_account):
        """Sets the billing_account of this Result.


        :param billing_account: The billing_account of this Result.  # noqa: E501
        :type: BillingAccountResult
        """

        self._billing_account = billing_account

    @property
    def project(self):
        """Gets the project of this Result.  # noqa: E501


        :return: The project of this Result.  # noqa: E501
        :rtype: ProjectResult
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Result.


        :param project: The project of this Result.  # noqa: E501
        :type: ProjectResult
        """

        self._project = project

    @property
    def virtual_machine(self):
        """Gets the virtual_machine of this Result.  # noqa: E501


        :return: The virtual_machine of this Result.  # noqa: E501
        :rtype: VirtualMachineResult
        """
        return self._virtual_machine

    @virtual_machine.setter
    def virtual_machine(self, virtual_machine):
        """Sets the virtual_machine of this Result.


        :param virtual_machine: The virtual_machine of this Result.  # noqa: E501
        :type: VirtualMachineResult
        """

        self._virtual_machine = virtual_machine

    @property
    def disk(self):
        """Gets the disk of this Result.  # noqa: E501


        :return: The disk of this Result.  # noqa: E501
        :rtype: DiskResult
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """Sets the disk of this Result.


        :param disk: The disk of this Result.  # noqa: E501
        :type: DiskResult
        """

        self._disk = disk

    @property
    def image(self):
        """Gets the image of this Result.  # noqa: E501


        :return: The image of this Result.  # noqa: E501
        :rtype: ImageResult
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Result.


        :param image: The image of this Result.  # noqa: E501
        :type: ImageResult
        """

        self._image = image

    @property
    def network(self):
        """Gets the network of this Result.  # noqa: E501


        :return: The network of this Result.  # noqa: E501
        :rtype: NetworkResult
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this Result.


        :param network: The network of this Result.  # noqa: E501
        :type: NetworkResult
        """

        self._network = network

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
        if issubclass(Result, dict):
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
        if not isinstance(other, Result):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Result):
            return True

        return self.to_dict() != other.to_dict()
