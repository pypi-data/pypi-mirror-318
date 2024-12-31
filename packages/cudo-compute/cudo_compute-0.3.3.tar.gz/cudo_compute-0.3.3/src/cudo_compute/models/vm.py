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


class VM(object):
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
        'datacenter_id': 'str',
        'machine_type': 'str',
        'region_id': 'str',
        'region_name': 'str',
        'id': 'str',
        'external_ip_address': 'str',
        'internal_ip_address': 'str',
        'public_ip_address': 'str',
        'memory': 'int',
        'cpu_model': 'str',
        'vcpus': 'int',
        'gpu_model': 'str',
        'gpu_model_id': 'str',
        'gpu_quantity': 'int',
        'boot_disk_size_gib': 'int',
        'renewable_energy': 'bool',
        'image_id': 'str',
        'public_image_id': 'str',
        'public_image_name': 'str',
        'private_image_id': 'str',
        'image_name': 'str',
        'create_by': 'str',
        'nics': 'list[VMNIC]',
        'rules': 'list[SecurityGroupRule]',
        'security_group_ids': 'list[str]',
        'short_state': 'str',
        'boot_disk': 'Disk',
        'storage_disks': 'list[Disk]',
        'metadata': 'dict(str, str)',
        'state': 'VmState',
        'create_time': 'datetime',
        'expire_time': 'datetime',
        'price': 'VMPrice',
        'commitment_term': 'CommitmentTerm',
        'commitment_end_time': 'datetime'
    }

    attribute_map = {
        'datacenter_id': 'datacenterId',
        'machine_type': 'machineType',
        'region_id': 'regionId',
        'region_name': 'regionName',
        'id': 'id',
        'external_ip_address': 'externalIpAddress',
        'internal_ip_address': 'internalIpAddress',
        'public_ip_address': 'publicIpAddress',
        'memory': 'memory',
        'cpu_model': 'cpuModel',
        'vcpus': 'vcpus',
        'gpu_model': 'gpuModel',
        'gpu_model_id': 'gpuModelId',
        'gpu_quantity': 'gpuQuantity',
        'boot_disk_size_gib': 'bootDiskSizeGib',
        'renewable_energy': 'renewableEnergy',
        'image_id': 'imageId',
        'public_image_id': 'publicImageId',
        'public_image_name': 'publicImageName',
        'private_image_id': 'privateImageId',
        'image_name': 'imageName',
        'create_by': 'createBy',
        'nics': 'nics',
        'rules': 'rules',
        'security_group_ids': 'securityGroupIds',
        'short_state': 'shortState',
        'boot_disk': 'bootDisk',
        'storage_disks': 'storageDisks',
        'metadata': 'metadata',
        'state': 'state',
        'create_time': 'createTime',
        'expire_time': 'expireTime',
        'price': 'price',
        'commitment_term': 'commitmentTerm',
        'commitment_end_time': 'commitmentEndTime'
    }

    def __init__(self, datacenter_id=None, machine_type=None, region_id=None, region_name=None, id=None, external_ip_address=None, internal_ip_address=None, public_ip_address=None, memory=None, cpu_model=None, vcpus=None, gpu_model=None, gpu_model_id=None, gpu_quantity=None, boot_disk_size_gib=None, renewable_energy=None, image_id=None, public_image_id=None, public_image_name=None, private_image_id=None, image_name=None, create_by=None, nics=None, rules=None, security_group_ids=None, short_state=None, boot_disk=None, storage_disks=None, metadata=None, state=None, create_time=None, expire_time=None, price=None, commitment_term=None, commitment_end_time=None, _configuration=None):  # noqa: E501
        """VM - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._datacenter_id = None
        self._machine_type = None
        self._region_id = None
        self._region_name = None
        self._id = None
        self._external_ip_address = None
        self._internal_ip_address = None
        self._public_ip_address = None
        self._memory = None
        self._cpu_model = None
        self._vcpus = None
        self._gpu_model = None
        self._gpu_model_id = None
        self._gpu_quantity = None
        self._boot_disk_size_gib = None
        self._renewable_energy = None
        self._image_id = None
        self._public_image_id = None
        self._public_image_name = None
        self._private_image_id = None
        self._image_name = None
        self._create_by = None
        self._nics = None
        self._rules = None
        self._security_group_ids = None
        self._short_state = None
        self._boot_disk = None
        self._storage_disks = None
        self._metadata = None
        self._state = None
        self._create_time = None
        self._expire_time = None
        self._price = None
        self._commitment_term = None
        self._commitment_end_time = None
        self.discriminator = None

        if datacenter_id is not None:
            self.datacenter_id = datacenter_id
        if machine_type is not None:
            self.machine_type = machine_type
        if region_id is not None:
            self.region_id = region_id
        if region_name is not None:
            self.region_name = region_name
        if id is not None:
            self.id = id
        if external_ip_address is not None:
            self.external_ip_address = external_ip_address
        if internal_ip_address is not None:
            self.internal_ip_address = internal_ip_address
        if public_ip_address is not None:
            self.public_ip_address = public_ip_address
        if memory is not None:
            self.memory = memory
        if cpu_model is not None:
            self.cpu_model = cpu_model
        if vcpus is not None:
            self.vcpus = vcpus
        if gpu_model is not None:
            self.gpu_model = gpu_model
        if gpu_model_id is not None:
            self.gpu_model_id = gpu_model_id
        if gpu_quantity is not None:
            self.gpu_quantity = gpu_quantity
        if boot_disk_size_gib is not None:
            self.boot_disk_size_gib = boot_disk_size_gib
        if renewable_energy is not None:
            self.renewable_energy = renewable_energy
        if image_id is not None:
            self.image_id = image_id
        if public_image_id is not None:
            self.public_image_id = public_image_id
        if public_image_name is not None:
            self.public_image_name = public_image_name
        if private_image_id is not None:
            self.private_image_id = private_image_id
        if image_name is not None:
            self.image_name = image_name
        if create_by is not None:
            self.create_by = create_by
        if nics is not None:
            self.nics = nics
        if rules is not None:
            self.rules = rules
        if security_group_ids is not None:
            self.security_group_ids = security_group_ids
        if short_state is not None:
            self.short_state = short_state
        if boot_disk is not None:
            self.boot_disk = boot_disk
        if storage_disks is not None:
            self.storage_disks = storage_disks
        if metadata is not None:
            self.metadata = metadata
        if state is not None:
            self.state = state
        if create_time is not None:
            self.create_time = create_time
        if expire_time is not None:
            self.expire_time = expire_time
        if price is not None:
            self.price = price
        if commitment_term is not None:
            self.commitment_term = commitment_term
        if commitment_end_time is not None:
            self.commitment_end_time = commitment_end_time

    @property
    def datacenter_id(self):
        """Gets the datacenter_id of this VM.  # noqa: E501


        :return: The datacenter_id of this VM.  # noqa: E501
        :rtype: str
        """
        return self._datacenter_id

    @datacenter_id.setter
    def datacenter_id(self, datacenter_id):
        """Sets the datacenter_id of this VM.


        :param datacenter_id: The datacenter_id of this VM.  # noqa: E501
        :type: str
        """

        self._datacenter_id = datacenter_id

    @property
    def machine_type(self):
        """Gets the machine_type of this VM.  # noqa: E501


        :return: The machine_type of this VM.  # noqa: E501
        :rtype: str
        """
        return self._machine_type

    @machine_type.setter
    def machine_type(self, machine_type):
        """Sets the machine_type of this VM.


        :param machine_type: The machine_type of this VM.  # noqa: E501
        :type: str
        """

        self._machine_type = machine_type

    @property
    def region_id(self):
        """Gets the region_id of this VM.  # noqa: E501


        :return: The region_id of this VM.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this VM.


        :param region_id: The region_id of this VM.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def region_name(self):
        """Gets the region_name of this VM.  # noqa: E501


        :return: The region_name of this VM.  # noqa: E501
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this VM.


        :param region_name: The region_name of this VM.  # noqa: E501
        :type: str
        """

        self._region_name = region_name

    @property
    def id(self):
        """Gets the id of this VM.  # noqa: E501


        :return: The id of this VM.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VM.


        :param id: The id of this VM.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def external_ip_address(self):
        """Gets the external_ip_address of this VM.  # noqa: E501


        :return: The external_ip_address of this VM.  # noqa: E501
        :rtype: str
        """
        return self._external_ip_address

    @external_ip_address.setter
    def external_ip_address(self, external_ip_address):
        """Sets the external_ip_address of this VM.


        :param external_ip_address: The external_ip_address of this VM.  # noqa: E501
        :type: str
        """

        self._external_ip_address = external_ip_address

    @property
    def internal_ip_address(self):
        """Gets the internal_ip_address of this VM.  # noqa: E501


        :return: The internal_ip_address of this VM.  # noqa: E501
        :rtype: str
        """
        return self._internal_ip_address

    @internal_ip_address.setter
    def internal_ip_address(self, internal_ip_address):
        """Sets the internal_ip_address of this VM.


        :param internal_ip_address: The internal_ip_address of this VM.  # noqa: E501
        :type: str
        """

        self._internal_ip_address = internal_ip_address

    @property
    def public_ip_address(self):
        """Gets the public_ip_address of this VM.  # noqa: E501


        :return: The public_ip_address of this VM.  # noqa: E501
        :rtype: str
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        """Sets the public_ip_address of this VM.


        :param public_ip_address: The public_ip_address of this VM.  # noqa: E501
        :type: str
        """

        self._public_ip_address = public_ip_address

    @property
    def memory(self):
        """Gets the memory of this VM.  # noqa: E501


        :return: The memory of this VM.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this VM.


        :param memory: The memory of this VM.  # noqa: E501
        :type: int
        """

        self._memory = memory

    @property
    def cpu_model(self):
        """Gets the cpu_model of this VM.  # noqa: E501


        :return: The cpu_model of this VM.  # noqa: E501
        :rtype: str
        """
        return self._cpu_model

    @cpu_model.setter
    def cpu_model(self, cpu_model):
        """Sets the cpu_model of this VM.


        :param cpu_model: The cpu_model of this VM.  # noqa: E501
        :type: str
        """

        self._cpu_model = cpu_model

    @property
    def vcpus(self):
        """Gets the vcpus of this VM.  # noqa: E501


        :return: The vcpus of this VM.  # noqa: E501
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this VM.


        :param vcpus: The vcpus of this VM.  # noqa: E501
        :type: int
        """

        self._vcpus = vcpus

    @property
    def gpu_model(self):
        """Gets the gpu_model of this VM.  # noqa: E501


        :return: The gpu_model of this VM.  # noqa: E501
        :rtype: str
        """
        return self._gpu_model

    @gpu_model.setter
    def gpu_model(self, gpu_model):
        """Sets the gpu_model of this VM.


        :param gpu_model: The gpu_model of this VM.  # noqa: E501
        :type: str
        """

        self._gpu_model = gpu_model

    @property
    def gpu_model_id(self):
        """Gets the gpu_model_id of this VM.  # noqa: E501


        :return: The gpu_model_id of this VM.  # noqa: E501
        :rtype: str
        """
        return self._gpu_model_id

    @gpu_model_id.setter
    def gpu_model_id(self, gpu_model_id):
        """Sets the gpu_model_id of this VM.


        :param gpu_model_id: The gpu_model_id of this VM.  # noqa: E501
        :type: str
        """

        self._gpu_model_id = gpu_model_id

    @property
    def gpu_quantity(self):
        """Gets the gpu_quantity of this VM.  # noqa: E501


        :return: The gpu_quantity of this VM.  # noqa: E501
        :rtype: int
        """
        return self._gpu_quantity

    @gpu_quantity.setter
    def gpu_quantity(self, gpu_quantity):
        """Sets the gpu_quantity of this VM.


        :param gpu_quantity: The gpu_quantity of this VM.  # noqa: E501
        :type: int
        """

        self._gpu_quantity = gpu_quantity

    @property
    def boot_disk_size_gib(self):
        """Gets the boot_disk_size_gib of this VM.  # noqa: E501


        :return: The boot_disk_size_gib of this VM.  # noqa: E501
        :rtype: int
        """
        return self._boot_disk_size_gib

    @boot_disk_size_gib.setter
    def boot_disk_size_gib(self, boot_disk_size_gib):
        """Sets the boot_disk_size_gib of this VM.


        :param boot_disk_size_gib: The boot_disk_size_gib of this VM.  # noqa: E501
        :type: int
        """

        self._boot_disk_size_gib = boot_disk_size_gib

    @property
    def renewable_energy(self):
        """Gets the renewable_energy of this VM.  # noqa: E501


        :return: The renewable_energy of this VM.  # noqa: E501
        :rtype: bool
        """
        return self._renewable_energy

    @renewable_energy.setter
    def renewable_energy(self, renewable_energy):
        """Sets the renewable_energy of this VM.


        :param renewable_energy: The renewable_energy of this VM.  # noqa: E501
        :type: bool
        """

        self._renewable_energy = renewable_energy

    @property
    def image_id(self):
        """Gets the image_id of this VM.  # noqa: E501


        :return: The image_id of this VM.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this VM.


        :param image_id: The image_id of this VM.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def public_image_id(self):
        """Gets the public_image_id of this VM.  # noqa: E501


        :return: The public_image_id of this VM.  # noqa: E501
        :rtype: str
        """
        return self._public_image_id

    @public_image_id.setter
    def public_image_id(self, public_image_id):
        """Sets the public_image_id of this VM.


        :param public_image_id: The public_image_id of this VM.  # noqa: E501
        :type: str
        """

        self._public_image_id = public_image_id

    @property
    def public_image_name(self):
        """Gets the public_image_name of this VM.  # noqa: E501


        :return: The public_image_name of this VM.  # noqa: E501
        :rtype: str
        """
        return self._public_image_name

    @public_image_name.setter
    def public_image_name(self, public_image_name):
        """Sets the public_image_name of this VM.


        :param public_image_name: The public_image_name of this VM.  # noqa: E501
        :type: str
        """

        self._public_image_name = public_image_name

    @property
    def private_image_id(self):
        """Gets the private_image_id of this VM.  # noqa: E501


        :return: The private_image_id of this VM.  # noqa: E501
        :rtype: str
        """
        return self._private_image_id

    @private_image_id.setter
    def private_image_id(self, private_image_id):
        """Sets the private_image_id of this VM.


        :param private_image_id: The private_image_id of this VM.  # noqa: E501
        :type: str
        """

        self._private_image_id = private_image_id

    @property
    def image_name(self):
        """Gets the image_name of this VM.  # noqa: E501


        :return: The image_name of this VM.  # noqa: E501
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this VM.


        :param image_name: The image_name of this VM.  # noqa: E501
        :type: str
        """

        self._image_name = image_name

    @property
    def create_by(self):
        """Gets the create_by of this VM.  # noqa: E501


        :return: The create_by of this VM.  # noqa: E501
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this VM.


        :param create_by: The create_by of this VM.  # noqa: E501
        :type: str
        """

        self._create_by = create_by

    @property
    def nics(self):
        """Gets the nics of this VM.  # noqa: E501


        :return: The nics of this VM.  # noqa: E501
        :rtype: list[VMNIC]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this VM.


        :param nics: The nics of this VM.  # noqa: E501
        :type: list[VMNIC]
        """

        self._nics = nics

    @property
    def rules(self):
        """Gets the rules of this VM.  # noqa: E501


        :return: The rules of this VM.  # noqa: E501
        :rtype: list[SecurityGroupRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this VM.


        :param rules: The rules of this VM.  # noqa: E501
        :type: list[SecurityGroupRule]
        """

        self._rules = rules

    @property
    def security_group_ids(self):
        """Gets the security_group_ids of this VM.  # noqa: E501


        :return: The security_group_ids of this VM.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        """Sets the security_group_ids of this VM.


        :param security_group_ids: The security_group_ids of this VM.  # noqa: E501
        :type: list[str]
        """

        self._security_group_ids = security_group_ids

    @property
    def short_state(self):
        """Gets the short_state of this VM.  # noqa: E501


        :return: The short_state of this VM.  # noqa: E501
        :rtype: str
        """
        return self._short_state

    @short_state.setter
    def short_state(self, short_state):
        """Sets the short_state of this VM.


        :param short_state: The short_state of this VM.  # noqa: E501
        :type: str
        """

        self._short_state = short_state

    @property
    def boot_disk(self):
        """Gets the boot_disk of this VM.  # noqa: E501


        :return: The boot_disk of this VM.  # noqa: E501
        :rtype: Disk
        """
        return self._boot_disk

    @boot_disk.setter
    def boot_disk(self, boot_disk):
        """Sets the boot_disk of this VM.


        :param boot_disk: The boot_disk of this VM.  # noqa: E501
        :type: Disk
        """

        self._boot_disk = boot_disk

    @property
    def storage_disks(self):
        """Gets the storage_disks of this VM.  # noqa: E501


        :return: The storage_disks of this VM.  # noqa: E501
        :rtype: list[Disk]
        """
        return self._storage_disks

    @storage_disks.setter
    def storage_disks(self, storage_disks):
        """Sets the storage_disks of this VM.


        :param storage_disks: The storage_disks of this VM.  # noqa: E501
        :type: list[Disk]
        """

        self._storage_disks = storage_disks

    @property
    def metadata(self):
        """Gets the metadata of this VM.  # noqa: E501


        :return: The metadata of this VM.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this VM.


        :param metadata: The metadata of this VM.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def state(self):
        """Gets the state of this VM.  # noqa: E501


        :return: The state of this VM.  # noqa: E501
        :rtype: VmState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this VM.


        :param state: The state of this VM.  # noqa: E501
        :type: VmState
        """

        self._state = state

    @property
    def create_time(self):
        """Gets the create_time of this VM.  # noqa: E501


        :return: The create_time of this VM.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this VM.


        :param create_time: The create_time of this VM.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def expire_time(self):
        """Gets the expire_time of this VM.  # noqa: E501


        :return: The expire_time of this VM.  # noqa: E501
        :rtype: datetime
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this VM.


        :param expire_time: The expire_time of this VM.  # noqa: E501
        :type: datetime
        """

        self._expire_time = expire_time

    @property
    def price(self):
        """Gets the price of this VM.  # noqa: E501


        :return: The price of this VM.  # noqa: E501
        :rtype: VMPrice
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this VM.


        :param price: The price of this VM.  # noqa: E501
        :type: VMPrice
        """

        self._price = price

    @property
    def commitment_term(self):
        """Gets the commitment_term of this VM.  # noqa: E501


        :return: The commitment_term of this VM.  # noqa: E501
        :rtype: CommitmentTerm
        """
        return self._commitment_term

    @commitment_term.setter
    def commitment_term(self, commitment_term):
        """Sets the commitment_term of this VM.


        :param commitment_term: The commitment_term of this VM.  # noqa: E501
        :type: CommitmentTerm
        """

        self._commitment_term = commitment_term

    @property
    def commitment_end_time(self):
        """Gets the commitment_end_time of this VM.  # noqa: E501


        :return: The commitment_end_time of this VM.  # noqa: E501
        :rtype: datetime
        """
        return self._commitment_end_time

    @commitment_end_time.setter
    def commitment_end_time(self, commitment_end_time):
        """Sets the commitment_end_time of this VM.


        :param commitment_end_time: The commitment_end_time of this VM.  # noqa: E501
        :type: datetime
        """

        self._commitment_end_time = commitment_end_time

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
        if issubclass(VM, dict):
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
        if not isinstance(other, VM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VM):
            return True

        return self.to_dict() != other.to_dict()
