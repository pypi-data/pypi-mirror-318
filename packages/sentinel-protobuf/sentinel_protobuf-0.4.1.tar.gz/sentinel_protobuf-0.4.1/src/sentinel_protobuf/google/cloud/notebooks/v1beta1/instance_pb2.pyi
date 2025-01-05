from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.notebooks.v1beta1 import environment_pb2 as _environment_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ReservationAffinity(_message.Message):
    __slots__ = ('consume_reservation_type', 'key', 'values')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[ReservationAffinity.Type]
        NO_RESERVATION: _ClassVar[ReservationAffinity.Type]
        ANY_RESERVATION: _ClassVar[ReservationAffinity.Type]
        SPECIFIC_RESERVATION: _ClassVar[ReservationAffinity.Type]
    TYPE_UNSPECIFIED: ReservationAffinity.Type
    NO_RESERVATION: ReservationAffinity.Type
    ANY_RESERVATION: ReservationAffinity.Type
    SPECIFIC_RESERVATION: ReservationAffinity.Type
    CONSUME_RESERVATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    consume_reservation_type: ReservationAffinity.Type
    key: str
    values: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, consume_reservation_type: _Optional[_Union[ReservationAffinity.Type, str]]=..., key: _Optional[str]=..., values: _Optional[_Iterable[str]]=...) -> None:
        ...

class Instance(_message.Message):
    __slots__ = ('name', 'vm_image', 'container_image', 'post_startup_script', 'proxy_uri', 'instance_owners', 'service_account', 'machine_type', 'accelerator_config', 'state', 'install_gpu_driver', 'custom_gpu_driver_path', 'boot_disk_type', 'boot_disk_size_gb', 'data_disk_type', 'data_disk_size_gb', 'no_remove_data_disk', 'disk_encryption', 'kms_key', 'no_public_ip', 'no_proxy_access', 'network', 'subnet', 'labels', 'metadata', 'nic_type', 'reservation_affinity', 'can_ip_forward', 'create_time', 'update_time')

    class AcceleratorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCELERATOR_TYPE_UNSPECIFIED: _ClassVar[Instance.AcceleratorType]
        NVIDIA_TESLA_K80: _ClassVar[Instance.AcceleratorType]
        NVIDIA_TESLA_P100: _ClassVar[Instance.AcceleratorType]
        NVIDIA_TESLA_V100: _ClassVar[Instance.AcceleratorType]
        NVIDIA_TESLA_P4: _ClassVar[Instance.AcceleratorType]
        NVIDIA_TESLA_T4: _ClassVar[Instance.AcceleratorType]
        NVIDIA_TESLA_T4_VWS: _ClassVar[Instance.AcceleratorType]
        NVIDIA_TESLA_P100_VWS: _ClassVar[Instance.AcceleratorType]
        NVIDIA_TESLA_P4_VWS: _ClassVar[Instance.AcceleratorType]
        TPU_V2: _ClassVar[Instance.AcceleratorType]
        TPU_V3: _ClassVar[Instance.AcceleratorType]
    ACCELERATOR_TYPE_UNSPECIFIED: Instance.AcceleratorType
    NVIDIA_TESLA_K80: Instance.AcceleratorType
    NVIDIA_TESLA_P100: Instance.AcceleratorType
    NVIDIA_TESLA_V100: Instance.AcceleratorType
    NVIDIA_TESLA_P4: Instance.AcceleratorType
    NVIDIA_TESLA_T4: Instance.AcceleratorType
    NVIDIA_TESLA_T4_VWS: Instance.AcceleratorType
    NVIDIA_TESLA_P100_VWS: Instance.AcceleratorType
    NVIDIA_TESLA_P4_VWS: Instance.AcceleratorType
    TPU_V2: Instance.AcceleratorType
    TPU_V3: Instance.AcceleratorType

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Instance.State]
        STARTING: _ClassVar[Instance.State]
        PROVISIONING: _ClassVar[Instance.State]
        ACTIVE: _ClassVar[Instance.State]
        STOPPING: _ClassVar[Instance.State]
        STOPPED: _ClassVar[Instance.State]
        DELETED: _ClassVar[Instance.State]
        UPGRADING: _ClassVar[Instance.State]
        INITIALIZING: _ClassVar[Instance.State]
        REGISTERING: _ClassVar[Instance.State]
        SUSPENDING: _ClassVar[Instance.State]
        SUSPENDED: _ClassVar[Instance.State]
    STATE_UNSPECIFIED: Instance.State
    STARTING: Instance.State
    PROVISIONING: Instance.State
    ACTIVE: Instance.State
    STOPPING: Instance.State
    STOPPED: Instance.State
    DELETED: Instance.State
    UPGRADING: Instance.State
    INITIALIZING: Instance.State
    REGISTERING: Instance.State
    SUSPENDING: Instance.State
    SUSPENDED: Instance.State

    class DiskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISK_TYPE_UNSPECIFIED: _ClassVar[Instance.DiskType]
        PD_STANDARD: _ClassVar[Instance.DiskType]
        PD_SSD: _ClassVar[Instance.DiskType]
        PD_BALANCED: _ClassVar[Instance.DiskType]
    DISK_TYPE_UNSPECIFIED: Instance.DiskType
    PD_STANDARD: Instance.DiskType
    PD_SSD: Instance.DiskType
    PD_BALANCED: Instance.DiskType

    class DiskEncryption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISK_ENCRYPTION_UNSPECIFIED: _ClassVar[Instance.DiskEncryption]
        GMEK: _ClassVar[Instance.DiskEncryption]
        CMEK: _ClassVar[Instance.DiskEncryption]
    DISK_ENCRYPTION_UNSPECIFIED: Instance.DiskEncryption
    GMEK: Instance.DiskEncryption
    CMEK: Instance.DiskEncryption

    class NicType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED_NIC_TYPE: _ClassVar[Instance.NicType]
        VIRTIO_NET: _ClassVar[Instance.NicType]
        GVNIC: _ClassVar[Instance.NicType]
    UNSPECIFIED_NIC_TYPE: Instance.NicType
    VIRTIO_NET: Instance.NicType
    GVNIC: Instance.NicType

    class AcceleratorConfig(_message.Message):
        __slots__ = ('type', 'core_count')
        TYPE_FIELD_NUMBER: _ClassVar[int]
        CORE_COUNT_FIELD_NUMBER: _ClassVar[int]
        type: Instance.AcceleratorType
        core_count: int

        def __init__(self, type: _Optional[_Union[Instance.AcceleratorType, str]]=..., core_count: _Optional[int]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VM_IMAGE_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_IMAGE_FIELD_NUMBER: _ClassVar[int]
    POST_STARTUP_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    PROXY_URI_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_OWNERS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    INSTALL_GPU_DRIVER_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_GPU_DRIVER_PATH_FIELD_NUMBER: _ClassVar[int]
    BOOT_DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    BOOT_DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    DATA_DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    NO_REMOVE_DATA_DISK_FIELD_NUMBER: _ClassVar[int]
    DISK_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    NO_PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    NO_PROXY_ACCESS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    CAN_IP_FORWARD_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    vm_image: _environment_pb2.VmImage
    container_image: _environment_pb2.ContainerImage
    post_startup_script: str
    proxy_uri: str
    instance_owners: _containers.RepeatedScalarFieldContainer[str]
    service_account: str
    machine_type: str
    accelerator_config: Instance.AcceleratorConfig
    state: Instance.State
    install_gpu_driver: bool
    custom_gpu_driver_path: str
    boot_disk_type: Instance.DiskType
    boot_disk_size_gb: int
    data_disk_type: Instance.DiskType
    data_disk_size_gb: int
    no_remove_data_disk: bool
    disk_encryption: Instance.DiskEncryption
    kms_key: str
    no_public_ip: bool
    no_proxy_access: bool
    network: str
    subnet: str
    labels: _containers.ScalarMap[str, str]
    metadata: _containers.ScalarMap[str, str]
    nic_type: Instance.NicType
    reservation_affinity: ReservationAffinity
    can_ip_forward: bool
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., vm_image: _Optional[_Union[_environment_pb2.VmImage, _Mapping]]=..., container_image: _Optional[_Union[_environment_pb2.ContainerImage, _Mapping]]=..., post_startup_script: _Optional[str]=..., proxy_uri: _Optional[str]=..., instance_owners: _Optional[_Iterable[str]]=..., service_account: _Optional[str]=..., machine_type: _Optional[str]=..., accelerator_config: _Optional[_Union[Instance.AcceleratorConfig, _Mapping]]=..., state: _Optional[_Union[Instance.State, str]]=..., install_gpu_driver: bool=..., custom_gpu_driver_path: _Optional[str]=..., boot_disk_type: _Optional[_Union[Instance.DiskType, str]]=..., boot_disk_size_gb: _Optional[int]=..., data_disk_type: _Optional[_Union[Instance.DiskType, str]]=..., data_disk_size_gb: _Optional[int]=..., no_remove_data_disk: bool=..., disk_encryption: _Optional[_Union[Instance.DiskEncryption, str]]=..., kms_key: _Optional[str]=..., no_public_ip: bool=..., no_proxy_access: bool=..., network: _Optional[str]=..., subnet: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., metadata: _Optional[_Mapping[str, str]]=..., nic_type: _Optional[_Union[Instance.NicType, str]]=..., reservation_affinity: _Optional[_Union[ReservationAffinity, _Mapping]]=..., can_ip_forward: bool=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...