from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DiskEncryption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DISK_ENCRYPTION_UNSPECIFIED: _ClassVar[DiskEncryption]
    GMEK: _ClassVar[DiskEncryption]
    CMEK: _ClassVar[DiskEncryption]

class DiskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DISK_TYPE_UNSPECIFIED: _ClassVar[DiskType]
    PD_STANDARD: _ClassVar[DiskType]
    PD_SSD: _ClassVar[DiskType]
    PD_BALANCED: _ClassVar[DiskType]
    PD_EXTREME: _ClassVar[DiskType]
DISK_ENCRYPTION_UNSPECIFIED: DiskEncryption
GMEK: DiskEncryption
CMEK: DiskEncryption
DISK_TYPE_UNSPECIFIED: DiskType
PD_STANDARD: DiskType
PD_SSD: DiskType
PD_BALANCED: DiskType
PD_EXTREME: DiskType

class NetworkInterface(_message.Message):
    __slots__ = ('network', 'subnet', 'nic_type')

    class NicType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NIC_TYPE_UNSPECIFIED: _ClassVar[NetworkInterface.NicType]
        VIRTIO_NET: _ClassVar[NetworkInterface.NicType]
        GVNIC: _ClassVar[NetworkInterface.NicType]
    NIC_TYPE_UNSPECIFIED: NetworkInterface.NicType
    VIRTIO_NET: NetworkInterface.NicType
    GVNIC: NetworkInterface.NicType
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    NIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    network: str
    subnet: str
    nic_type: NetworkInterface.NicType

    def __init__(self, network: _Optional[str]=..., subnet: _Optional[str]=..., nic_type: _Optional[_Union[NetworkInterface.NicType, str]]=...) -> None:
        ...

class VmImage(_message.Message):
    __slots__ = ('project', 'name', 'family')
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    project: str
    name: str
    family: str

    def __init__(self, project: _Optional[str]=..., name: _Optional[str]=..., family: _Optional[str]=...) -> None:
        ...

class ContainerImage(_message.Message):
    __slots__ = ('repository', 'tag')
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    repository: str
    tag: str

    def __init__(self, repository: _Optional[str]=..., tag: _Optional[str]=...) -> None:
        ...

class AcceleratorConfig(_message.Message):
    __slots__ = ('type', 'core_count')

    class AcceleratorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCELERATOR_TYPE_UNSPECIFIED: _ClassVar[AcceleratorConfig.AcceleratorType]
        NVIDIA_TESLA_P100: _ClassVar[AcceleratorConfig.AcceleratorType]
        NVIDIA_TESLA_V100: _ClassVar[AcceleratorConfig.AcceleratorType]
        NVIDIA_TESLA_P4: _ClassVar[AcceleratorConfig.AcceleratorType]
        NVIDIA_TESLA_T4: _ClassVar[AcceleratorConfig.AcceleratorType]
        NVIDIA_TESLA_A100: _ClassVar[AcceleratorConfig.AcceleratorType]
        NVIDIA_A100_80GB: _ClassVar[AcceleratorConfig.AcceleratorType]
        NVIDIA_L4: _ClassVar[AcceleratorConfig.AcceleratorType]
        NVIDIA_TESLA_T4_VWS: _ClassVar[AcceleratorConfig.AcceleratorType]
        NVIDIA_TESLA_P100_VWS: _ClassVar[AcceleratorConfig.AcceleratorType]
        NVIDIA_TESLA_P4_VWS: _ClassVar[AcceleratorConfig.AcceleratorType]
    ACCELERATOR_TYPE_UNSPECIFIED: AcceleratorConfig.AcceleratorType
    NVIDIA_TESLA_P100: AcceleratorConfig.AcceleratorType
    NVIDIA_TESLA_V100: AcceleratorConfig.AcceleratorType
    NVIDIA_TESLA_P4: AcceleratorConfig.AcceleratorType
    NVIDIA_TESLA_T4: AcceleratorConfig.AcceleratorType
    NVIDIA_TESLA_A100: AcceleratorConfig.AcceleratorType
    NVIDIA_A100_80GB: AcceleratorConfig.AcceleratorType
    NVIDIA_L4: AcceleratorConfig.AcceleratorType
    NVIDIA_TESLA_T4_VWS: AcceleratorConfig.AcceleratorType
    NVIDIA_TESLA_P100_VWS: AcceleratorConfig.AcceleratorType
    NVIDIA_TESLA_P4_VWS: AcceleratorConfig.AcceleratorType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    type: AcceleratorConfig.AcceleratorType
    core_count: int

    def __init__(self, type: _Optional[_Union[AcceleratorConfig.AcceleratorType, str]]=..., core_count: _Optional[int]=...) -> None:
        ...

class ShieldedInstanceConfig(_message.Message):
    __slots__ = ('enable_secure_boot', 'enable_vtpm', 'enable_integrity_monitoring')
    ENABLE_SECURE_BOOT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_VTPM_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INTEGRITY_MONITORING_FIELD_NUMBER: _ClassVar[int]
    enable_secure_boot: bool
    enable_vtpm: bool
    enable_integrity_monitoring: bool

    def __init__(self, enable_secure_boot: bool=..., enable_vtpm: bool=..., enable_integrity_monitoring: bool=...) -> None:
        ...

class GPUDriverConfig(_message.Message):
    __slots__ = ('enable_gpu_driver', 'custom_gpu_driver_path')
    ENABLE_GPU_DRIVER_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_GPU_DRIVER_PATH_FIELD_NUMBER: _ClassVar[int]
    enable_gpu_driver: bool
    custom_gpu_driver_path: str

    def __init__(self, enable_gpu_driver: bool=..., custom_gpu_driver_path: _Optional[str]=...) -> None:
        ...

class DataDisk(_message.Message):
    __slots__ = ('disk_size_gb', 'disk_type', 'disk_encryption', 'kms_key')
    DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISK_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    disk_size_gb: int
    disk_type: DiskType
    disk_encryption: DiskEncryption
    kms_key: str

    def __init__(self, disk_size_gb: _Optional[int]=..., disk_type: _Optional[_Union[DiskType, str]]=..., disk_encryption: _Optional[_Union[DiskEncryption, str]]=..., kms_key: _Optional[str]=...) -> None:
        ...

class BootDisk(_message.Message):
    __slots__ = ('disk_size_gb', 'disk_type', 'disk_encryption', 'kms_key')
    DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISK_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    disk_size_gb: int
    disk_type: DiskType
    disk_encryption: DiskEncryption
    kms_key: str

    def __init__(self, disk_size_gb: _Optional[int]=..., disk_type: _Optional[_Union[DiskType, str]]=..., disk_encryption: _Optional[_Union[DiskEncryption, str]]=..., kms_key: _Optional[str]=...) -> None:
        ...

class ServiceAccount(_message.Message):
    __slots__ = ('email', 'scopes')
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    email: str
    scopes: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, email: _Optional[str]=..., scopes: _Optional[_Iterable[str]]=...) -> None:
        ...

class GceSetup(_message.Message):
    __slots__ = ('machine_type', 'accelerator_configs', 'service_accounts', 'vm_image', 'container_image', 'boot_disk', 'data_disks', 'shielded_instance_config', 'network_interfaces', 'disable_public_ip', 'tags', 'metadata', 'enable_ip_forwarding', 'gpu_driver_config')

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    VM_IMAGE_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_IMAGE_FIELD_NUMBER: _ClassVar[int]
    BOOT_DISK_FIELD_NUMBER: _ClassVar[int]
    DATA_DISKS_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    DISABLE_PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ENABLE_IP_FORWARDING_FIELD_NUMBER: _ClassVar[int]
    GPU_DRIVER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    machine_type: str
    accelerator_configs: _containers.RepeatedCompositeFieldContainer[AcceleratorConfig]
    service_accounts: _containers.RepeatedCompositeFieldContainer[ServiceAccount]
    vm_image: VmImage
    container_image: ContainerImage
    boot_disk: BootDisk
    data_disks: _containers.RepeatedCompositeFieldContainer[DataDisk]
    shielded_instance_config: ShieldedInstanceConfig
    network_interfaces: _containers.RepeatedCompositeFieldContainer[NetworkInterface]
    disable_public_ip: bool
    tags: _containers.RepeatedScalarFieldContainer[str]
    metadata: _containers.ScalarMap[str, str]
    enable_ip_forwarding: bool
    gpu_driver_config: GPUDriverConfig

    def __init__(self, machine_type: _Optional[str]=..., accelerator_configs: _Optional[_Iterable[_Union[AcceleratorConfig, _Mapping]]]=..., service_accounts: _Optional[_Iterable[_Union[ServiceAccount, _Mapping]]]=..., vm_image: _Optional[_Union[VmImage, _Mapping]]=..., container_image: _Optional[_Union[ContainerImage, _Mapping]]=..., boot_disk: _Optional[_Union[BootDisk, _Mapping]]=..., data_disks: _Optional[_Iterable[_Union[DataDisk, _Mapping]]]=..., shielded_instance_config: _Optional[_Union[ShieldedInstanceConfig, _Mapping]]=..., network_interfaces: _Optional[_Iterable[_Union[NetworkInterface, _Mapping]]]=..., disable_public_ip: bool=..., tags: _Optional[_Iterable[str]]=..., metadata: _Optional[_Mapping[str, str]]=..., enable_ip_forwarding: bool=..., gpu_driver_config: _Optional[_Union[GPUDriverConfig, _Mapping]]=...) -> None:
        ...