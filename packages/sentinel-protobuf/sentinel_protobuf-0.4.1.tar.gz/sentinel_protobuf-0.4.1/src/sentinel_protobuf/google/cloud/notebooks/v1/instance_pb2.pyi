from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.notebooks.v1 import environment_pb2 as _environment_pb2
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
    __slots__ = ('name', 'vm_image', 'container_image', 'post_startup_script', 'proxy_uri', 'instance_owners', 'service_account', 'service_account_scopes', 'machine_type', 'accelerator_config', 'state', 'install_gpu_driver', 'custom_gpu_driver_path', 'boot_disk_type', 'boot_disk_size_gb', 'data_disk_type', 'data_disk_size_gb', 'no_remove_data_disk', 'disk_encryption', 'kms_key', 'disks', 'shielded_instance_config', 'no_public_ip', 'no_proxy_access', 'network', 'subnet', 'labels', 'metadata', 'tags', 'upgrade_history', 'nic_type', 'reservation_affinity', 'creator', 'can_ip_forward', 'create_time', 'update_time')

    class AcceleratorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCELERATOR_TYPE_UNSPECIFIED: _ClassVar[Instance.AcceleratorType]
        NVIDIA_TESLA_K80: _ClassVar[Instance.AcceleratorType]
        NVIDIA_TESLA_P100: _ClassVar[Instance.AcceleratorType]
        NVIDIA_TESLA_V100: _ClassVar[Instance.AcceleratorType]
        NVIDIA_TESLA_P4: _ClassVar[Instance.AcceleratorType]
        NVIDIA_TESLA_T4: _ClassVar[Instance.AcceleratorType]
        NVIDIA_TESLA_A100: _ClassVar[Instance.AcceleratorType]
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
    NVIDIA_TESLA_A100: Instance.AcceleratorType
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
        PD_EXTREME: _ClassVar[Instance.DiskType]
    DISK_TYPE_UNSPECIFIED: Instance.DiskType
    PD_STANDARD: Instance.DiskType
    PD_SSD: Instance.DiskType
    PD_BALANCED: Instance.DiskType
    PD_EXTREME: Instance.DiskType

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

    class Disk(_message.Message):
        __slots__ = ('auto_delete', 'boot', 'device_name', 'disk_size_gb', 'guest_os_features', 'index', 'interface', 'kind', 'licenses', 'mode', 'source', 'type')

        class GuestOsFeature(_message.Message):
            __slots__ = ('type',)
            TYPE_FIELD_NUMBER: _ClassVar[int]
            type: str

            def __init__(self, type: _Optional[str]=...) -> None:
                ...
        AUTO_DELETE_FIELD_NUMBER: _ClassVar[int]
        BOOT_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
        GUEST_OS_FEATURES_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_FIELD_NUMBER: _ClassVar[int]
        KIND_FIELD_NUMBER: _ClassVar[int]
        LICENSES_FIELD_NUMBER: _ClassVar[int]
        MODE_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        auto_delete: bool
        boot: bool
        device_name: str
        disk_size_gb: int
        guest_os_features: _containers.RepeatedCompositeFieldContainer[Instance.Disk.GuestOsFeature]
        index: int
        interface: str
        kind: str
        licenses: _containers.RepeatedScalarFieldContainer[str]
        mode: str
        source: str
        type: str

        def __init__(self, auto_delete: bool=..., boot: bool=..., device_name: _Optional[str]=..., disk_size_gb: _Optional[int]=..., guest_os_features: _Optional[_Iterable[_Union[Instance.Disk.GuestOsFeature, _Mapping]]]=..., index: _Optional[int]=..., interface: _Optional[str]=..., kind: _Optional[str]=..., licenses: _Optional[_Iterable[str]]=..., mode: _Optional[str]=..., source: _Optional[str]=..., type: _Optional[str]=...) -> None:
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

    class UpgradeHistoryEntry(_message.Message):
        __slots__ = ('snapshot', 'vm_image', 'container_image', 'framework', 'version', 'state', 'create_time', 'target_image', 'action', 'target_version')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[Instance.UpgradeHistoryEntry.State]
            STARTED: _ClassVar[Instance.UpgradeHistoryEntry.State]
            SUCCEEDED: _ClassVar[Instance.UpgradeHistoryEntry.State]
            FAILED: _ClassVar[Instance.UpgradeHistoryEntry.State]
        STATE_UNSPECIFIED: Instance.UpgradeHistoryEntry.State
        STARTED: Instance.UpgradeHistoryEntry.State
        SUCCEEDED: Instance.UpgradeHistoryEntry.State
        FAILED: Instance.UpgradeHistoryEntry.State

        class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ACTION_UNSPECIFIED: _ClassVar[Instance.UpgradeHistoryEntry.Action]
            UPGRADE: _ClassVar[Instance.UpgradeHistoryEntry.Action]
            ROLLBACK: _ClassVar[Instance.UpgradeHistoryEntry.Action]
        ACTION_UNSPECIFIED: Instance.UpgradeHistoryEntry.Action
        UPGRADE: Instance.UpgradeHistoryEntry.Action
        ROLLBACK: Instance.UpgradeHistoryEntry.Action
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        VM_IMAGE_FIELD_NUMBER: _ClassVar[int]
        CONTAINER_IMAGE_FIELD_NUMBER: _ClassVar[int]
        FRAMEWORK_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
        TARGET_IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        TARGET_VERSION_FIELD_NUMBER: _ClassVar[int]
        snapshot: str
        vm_image: str
        container_image: str
        framework: str
        version: str
        state: Instance.UpgradeHistoryEntry.State
        create_time: _timestamp_pb2.Timestamp
        target_image: str
        action: Instance.UpgradeHistoryEntry.Action
        target_version: str

        def __init__(self, snapshot: _Optional[str]=..., vm_image: _Optional[str]=..., container_image: _Optional[str]=..., framework: _Optional[str]=..., version: _Optional[str]=..., state: _Optional[_Union[Instance.UpgradeHistoryEntry.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target_image: _Optional[str]=..., action: _Optional[_Union[Instance.UpgradeHistoryEntry.Action, str]]=..., target_version: _Optional[str]=...) -> None:
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
    SERVICE_ACCOUNT_SCOPES_FIELD_NUMBER: _ClassVar[int]
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
    DISKS_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NO_PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    NO_PROXY_ACCESS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_HISTORY_FIELD_NUMBER: _ClassVar[int]
    NIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
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
    service_account_scopes: _containers.RepeatedScalarFieldContainer[str]
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
    disks: _containers.RepeatedCompositeFieldContainer[Instance.Disk]
    shielded_instance_config: Instance.ShieldedInstanceConfig
    no_public_ip: bool
    no_proxy_access: bool
    network: str
    subnet: str
    labels: _containers.ScalarMap[str, str]
    metadata: _containers.ScalarMap[str, str]
    tags: _containers.RepeatedScalarFieldContainer[str]
    upgrade_history: _containers.RepeatedCompositeFieldContainer[Instance.UpgradeHistoryEntry]
    nic_type: Instance.NicType
    reservation_affinity: ReservationAffinity
    creator: str
    can_ip_forward: bool
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., vm_image: _Optional[_Union[_environment_pb2.VmImage, _Mapping]]=..., container_image: _Optional[_Union[_environment_pb2.ContainerImage, _Mapping]]=..., post_startup_script: _Optional[str]=..., proxy_uri: _Optional[str]=..., instance_owners: _Optional[_Iterable[str]]=..., service_account: _Optional[str]=..., service_account_scopes: _Optional[_Iterable[str]]=..., machine_type: _Optional[str]=..., accelerator_config: _Optional[_Union[Instance.AcceleratorConfig, _Mapping]]=..., state: _Optional[_Union[Instance.State, str]]=..., install_gpu_driver: bool=..., custom_gpu_driver_path: _Optional[str]=..., boot_disk_type: _Optional[_Union[Instance.DiskType, str]]=..., boot_disk_size_gb: _Optional[int]=..., data_disk_type: _Optional[_Union[Instance.DiskType, str]]=..., data_disk_size_gb: _Optional[int]=..., no_remove_data_disk: bool=..., disk_encryption: _Optional[_Union[Instance.DiskEncryption, str]]=..., kms_key: _Optional[str]=..., disks: _Optional[_Iterable[_Union[Instance.Disk, _Mapping]]]=..., shielded_instance_config: _Optional[_Union[Instance.ShieldedInstanceConfig, _Mapping]]=..., no_public_ip: bool=..., no_proxy_access: bool=..., network: _Optional[str]=..., subnet: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., metadata: _Optional[_Mapping[str, str]]=..., tags: _Optional[_Iterable[str]]=..., upgrade_history: _Optional[_Iterable[_Union[Instance.UpgradeHistoryEntry, _Mapping]]]=..., nic_type: _Optional[_Union[Instance.NicType, str]]=..., reservation_affinity: _Optional[_Union[ReservationAffinity, _Mapping]]=..., creator: _Optional[str]=..., can_ip_forward: bool=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...