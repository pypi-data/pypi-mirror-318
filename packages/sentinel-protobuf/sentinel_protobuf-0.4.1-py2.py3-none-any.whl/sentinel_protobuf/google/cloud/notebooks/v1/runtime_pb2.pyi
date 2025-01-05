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

class Runtime(_message.Message):
    __slots__ = ("name", "virtual_machine", "state", "health_state", "access_config", "software_config", "metrics", "create_time", "update_time")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Runtime.State]
        STARTING: _ClassVar[Runtime.State]
        PROVISIONING: _ClassVar[Runtime.State]
        ACTIVE: _ClassVar[Runtime.State]
        STOPPING: _ClassVar[Runtime.State]
        STOPPED: _ClassVar[Runtime.State]
        DELETING: _ClassVar[Runtime.State]
        UPGRADING: _ClassVar[Runtime.State]
        INITIALIZING: _ClassVar[Runtime.State]
    STATE_UNSPECIFIED: Runtime.State
    STARTING: Runtime.State
    PROVISIONING: Runtime.State
    ACTIVE: Runtime.State
    STOPPING: Runtime.State
    STOPPED: Runtime.State
    DELETING: Runtime.State
    UPGRADING: Runtime.State
    INITIALIZING: Runtime.State
    class HealthState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HEALTH_STATE_UNSPECIFIED: _ClassVar[Runtime.HealthState]
        HEALTHY: _ClassVar[Runtime.HealthState]
        UNHEALTHY: _ClassVar[Runtime.HealthState]
        AGENT_NOT_INSTALLED: _ClassVar[Runtime.HealthState]
        AGENT_NOT_RUNNING: _ClassVar[Runtime.HealthState]
    HEALTH_STATE_UNSPECIFIED: Runtime.HealthState
    HEALTHY: Runtime.HealthState
    UNHEALTHY: Runtime.HealthState
    AGENT_NOT_INSTALLED: Runtime.HealthState
    AGENT_NOT_RUNNING: Runtime.HealthState
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_MACHINE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    HEALTH_STATE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    virtual_machine: VirtualMachine
    state: Runtime.State
    health_state: Runtime.HealthState
    access_config: RuntimeAccessConfig
    software_config: RuntimeSoftwareConfig
    metrics: RuntimeMetrics
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., virtual_machine: _Optional[_Union[VirtualMachine, _Mapping]] = ..., state: _Optional[_Union[Runtime.State, str]] = ..., health_state: _Optional[_Union[Runtime.HealthState, str]] = ..., access_config: _Optional[_Union[RuntimeAccessConfig, _Mapping]] = ..., software_config: _Optional[_Union[RuntimeSoftwareConfig, _Mapping]] = ..., metrics: _Optional[_Union[RuntimeMetrics, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RuntimeAcceleratorConfig(_message.Message):
    __slots__ = ("type", "core_count")
    class AcceleratorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCELERATOR_TYPE_UNSPECIFIED: _ClassVar[RuntimeAcceleratorConfig.AcceleratorType]
        NVIDIA_TESLA_K80: _ClassVar[RuntimeAcceleratorConfig.AcceleratorType]
        NVIDIA_TESLA_P100: _ClassVar[RuntimeAcceleratorConfig.AcceleratorType]
        NVIDIA_TESLA_V100: _ClassVar[RuntimeAcceleratorConfig.AcceleratorType]
        NVIDIA_TESLA_P4: _ClassVar[RuntimeAcceleratorConfig.AcceleratorType]
        NVIDIA_TESLA_T4: _ClassVar[RuntimeAcceleratorConfig.AcceleratorType]
        NVIDIA_TESLA_A100: _ClassVar[RuntimeAcceleratorConfig.AcceleratorType]
        TPU_V2: _ClassVar[RuntimeAcceleratorConfig.AcceleratorType]
        TPU_V3: _ClassVar[RuntimeAcceleratorConfig.AcceleratorType]
        NVIDIA_TESLA_T4_VWS: _ClassVar[RuntimeAcceleratorConfig.AcceleratorType]
        NVIDIA_TESLA_P100_VWS: _ClassVar[RuntimeAcceleratorConfig.AcceleratorType]
        NVIDIA_TESLA_P4_VWS: _ClassVar[RuntimeAcceleratorConfig.AcceleratorType]
    ACCELERATOR_TYPE_UNSPECIFIED: RuntimeAcceleratorConfig.AcceleratorType
    NVIDIA_TESLA_K80: RuntimeAcceleratorConfig.AcceleratorType
    NVIDIA_TESLA_P100: RuntimeAcceleratorConfig.AcceleratorType
    NVIDIA_TESLA_V100: RuntimeAcceleratorConfig.AcceleratorType
    NVIDIA_TESLA_P4: RuntimeAcceleratorConfig.AcceleratorType
    NVIDIA_TESLA_T4: RuntimeAcceleratorConfig.AcceleratorType
    NVIDIA_TESLA_A100: RuntimeAcceleratorConfig.AcceleratorType
    TPU_V2: RuntimeAcceleratorConfig.AcceleratorType
    TPU_V3: RuntimeAcceleratorConfig.AcceleratorType
    NVIDIA_TESLA_T4_VWS: RuntimeAcceleratorConfig.AcceleratorType
    NVIDIA_TESLA_P100_VWS: RuntimeAcceleratorConfig.AcceleratorType
    NVIDIA_TESLA_P4_VWS: RuntimeAcceleratorConfig.AcceleratorType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    type: RuntimeAcceleratorConfig.AcceleratorType
    core_count: int
    def __init__(self, type: _Optional[_Union[RuntimeAcceleratorConfig.AcceleratorType, str]] = ..., core_count: _Optional[int] = ...) -> None: ...

class EncryptionConfig(_message.Message):
    __slots__ = ("kms_key",)
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    kms_key: str
    def __init__(self, kms_key: _Optional[str] = ...) -> None: ...

class LocalDisk(_message.Message):
    __slots__ = ("auto_delete", "boot", "device_name", "guest_os_features", "index", "initialize_params", "interface", "kind", "licenses", "mode", "source", "type")
    class RuntimeGuestOsFeature(_message.Message):
        __slots__ = ("type",)
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: str
        def __init__(self, type: _Optional[str] = ...) -> None: ...
    AUTO_DELETE_FIELD_NUMBER: _ClassVar[int]
    BOOT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    GUEST_OS_FEATURES_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    INITIALIZE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    LICENSES_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    auto_delete: bool
    boot: bool
    device_name: str
    guest_os_features: _containers.RepeatedCompositeFieldContainer[LocalDisk.RuntimeGuestOsFeature]
    index: int
    initialize_params: LocalDiskInitializeParams
    interface: str
    kind: str
    licenses: _containers.RepeatedScalarFieldContainer[str]
    mode: str
    source: str
    type: str
    def __init__(self, auto_delete: bool = ..., boot: bool = ..., device_name: _Optional[str] = ..., guest_os_features: _Optional[_Iterable[_Union[LocalDisk.RuntimeGuestOsFeature, _Mapping]]] = ..., index: _Optional[int] = ..., initialize_params: _Optional[_Union[LocalDiskInitializeParams, _Mapping]] = ..., interface: _Optional[str] = ..., kind: _Optional[str] = ..., licenses: _Optional[_Iterable[str]] = ..., mode: _Optional[str] = ..., source: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class LocalDiskInitializeParams(_message.Message):
    __slots__ = ("description", "disk_name", "disk_size_gb", "disk_type", "labels")
    class DiskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISK_TYPE_UNSPECIFIED: _ClassVar[LocalDiskInitializeParams.DiskType]
        PD_STANDARD: _ClassVar[LocalDiskInitializeParams.DiskType]
        PD_SSD: _ClassVar[LocalDiskInitializeParams.DiskType]
        PD_BALANCED: _ClassVar[LocalDiskInitializeParams.DiskType]
        PD_EXTREME: _ClassVar[LocalDiskInitializeParams.DiskType]
    DISK_TYPE_UNSPECIFIED: LocalDiskInitializeParams.DiskType
    PD_STANDARD: LocalDiskInitializeParams.DiskType
    PD_SSD: LocalDiskInitializeParams.DiskType
    PD_BALANCED: LocalDiskInitializeParams.DiskType
    PD_EXTREME: LocalDiskInitializeParams.DiskType
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISK_NAME_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    description: str
    disk_name: str
    disk_size_gb: int
    disk_type: LocalDiskInitializeParams.DiskType
    labels: _containers.ScalarMap[str, str]
    def __init__(self, description: _Optional[str] = ..., disk_name: _Optional[str] = ..., disk_size_gb: _Optional[int] = ..., disk_type: _Optional[_Union[LocalDiskInitializeParams.DiskType, str]] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class RuntimeAccessConfig(_message.Message):
    __slots__ = ("access_type", "runtime_owner", "proxy_uri")
    class RuntimeAccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RUNTIME_ACCESS_TYPE_UNSPECIFIED: _ClassVar[RuntimeAccessConfig.RuntimeAccessType]
        SINGLE_USER: _ClassVar[RuntimeAccessConfig.RuntimeAccessType]
        SERVICE_ACCOUNT: _ClassVar[RuntimeAccessConfig.RuntimeAccessType]
    RUNTIME_ACCESS_TYPE_UNSPECIFIED: RuntimeAccessConfig.RuntimeAccessType
    SINGLE_USER: RuntimeAccessConfig.RuntimeAccessType
    SERVICE_ACCOUNT: RuntimeAccessConfig.RuntimeAccessType
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_OWNER_FIELD_NUMBER: _ClassVar[int]
    PROXY_URI_FIELD_NUMBER: _ClassVar[int]
    access_type: RuntimeAccessConfig.RuntimeAccessType
    runtime_owner: str
    proxy_uri: str
    def __init__(self, access_type: _Optional[_Union[RuntimeAccessConfig.RuntimeAccessType, str]] = ..., runtime_owner: _Optional[str] = ..., proxy_uri: _Optional[str] = ...) -> None: ...

class RuntimeSoftwareConfig(_message.Message):
    __slots__ = ("notebook_upgrade_schedule", "enable_health_monitoring", "idle_shutdown", "idle_shutdown_timeout", "install_gpu_driver", "custom_gpu_driver_path", "post_startup_script", "kernels", "upgradeable", "post_startup_script_behavior", "disable_terminal", "version")
    class PostStartupScriptBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        POST_STARTUP_SCRIPT_BEHAVIOR_UNSPECIFIED: _ClassVar[RuntimeSoftwareConfig.PostStartupScriptBehavior]
        RUN_EVERY_START: _ClassVar[RuntimeSoftwareConfig.PostStartupScriptBehavior]
        DOWNLOAD_AND_RUN_EVERY_START: _ClassVar[RuntimeSoftwareConfig.PostStartupScriptBehavior]
    POST_STARTUP_SCRIPT_BEHAVIOR_UNSPECIFIED: RuntimeSoftwareConfig.PostStartupScriptBehavior
    RUN_EVERY_START: RuntimeSoftwareConfig.PostStartupScriptBehavior
    DOWNLOAD_AND_RUN_EVERY_START: RuntimeSoftwareConfig.PostStartupScriptBehavior
    NOTEBOOK_UPGRADE_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_HEALTH_MONITORING_FIELD_NUMBER: _ClassVar[int]
    IDLE_SHUTDOWN_FIELD_NUMBER: _ClassVar[int]
    IDLE_SHUTDOWN_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    INSTALL_GPU_DRIVER_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_GPU_DRIVER_PATH_FIELD_NUMBER: _ClassVar[int]
    POST_STARTUP_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    KERNELS_FIELD_NUMBER: _ClassVar[int]
    UPGRADEABLE_FIELD_NUMBER: _ClassVar[int]
    POST_STARTUP_SCRIPT_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    DISABLE_TERMINAL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    notebook_upgrade_schedule: str
    enable_health_monitoring: bool
    idle_shutdown: bool
    idle_shutdown_timeout: int
    install_gpu_driver: bool
    custom_gpu_driver_path: str
    post_startup_script: str
    kernels: _containers.RepeatedCompositeFieldContainer[_environment_pb2.ContainerImage]
    upgradeable: bool
    post_startup_script_behavior: RuntimeSoftwareConfig.PostStartupScriptBehavior
    disable_terminal: bool
    version: str
    def __init__(self, notebook_upgrade_schedule: _Optional[str] = ..., enable_health_monitoring: bool = ..., idle_shutdown: bool = ..., idle_shutdown_timeout: _Optional[int] = ..., install_gpu_driver: bool = ..., custom_gpu_driver_path: _Optional[str] = ..., post_startup_script: _Optional[str] = ..., kernels: _Optional[_Iterable[_Union[_environment_pb2.ContainerImage, _Mapping]]] = ..., upgradeable: bool = ..., post_startup_script_behavior: _Optional[_Union[RuntimeSoftwareConfig.PostStartupScriptBehavior, str]] = ..., disable_terminal: bool = ..., version: _Optional[str] = ...) -> None: ...

class RuntimeMetrics(_message.Message):
    __slots__ = ("system_metrics",)
    class SystemMetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SYSTEM_METRICS_FIELD_NUMBER: _ClassVar[int]
    system_metrics: _containers.ScalarMap[str, str]
    def __init__(self, system_metrics: _Optional[_Mapping[str, str]] = ...) -> None: ...

class RuntimeShieldedInstanceConfig(_message.Message):
    __slots__ = ("enable_secure_boot", "enable_vtpm", "enable_integrity_monitoring")
    ENABLE_SECURE_BOOT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_VTPM_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INTEGRITY_MONITORING_FIELD_NUMBER: _ClassVar[int]
    enable_secure_boot: bool
    enable_vtpm: bool
    enable_integrity_monitoring: bool
    def __init__(self, enable_secure_boot: bool = ..., enable_vtpm: bool = ..., enable_integrity_monitoring: bool = ...) -> None: ...

class VirtualMachine(_message.Message):
    __slots__ = ("instance_name", "instance_id", "virtual_machine_config")
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_MACHINE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    instance_name: str
    instance_id: str
    virtual_machine_config: VirtualMachineConfig
    def __init__(self, instance_name: _Optional[str] = ..., instance_id: _Optional[str] = ..., virtual_machine_config: _Optional[_Union[VirtualMachineConfig, _Mapping]] = ...) -> None: ...

class VirtualMachineConfig(_message.Message):
    __slots__ = ("zone", "machine_type", "container_images", "data_disk", "encryption_config", "shielded_instance_config", "accelerator_config", "network", "subnet", "internal_ip_only", "tags", "guest_attributes", "metadata", "labels", "nic_type", "reserved_ip_range", "boot_image")
    class NicType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED_NIC_TYPE: _ClassVar[VirtualMachineConfig.NicType]
        VIRTIO_NET: _ClassVar[VirtualMachineConfig.NicType]
        GVNIC: _ClassVar[VirtualMachineConfig.NicType]
    UNSPECIFIED_NIC_TYPE: VirtualMachineConfig.NicType
    VIRTIO_NET: VirtualMachineConfig.NicType
    GVNIC: VirtualMachineConfig.NicType
    class BootImage(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GuestAttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ZONE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_IMAGES_FIELD_NUMBER: _ClassVar[int]
    DATA_DISK_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_IP_ONLY_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    GUEST_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESERVED_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    BOOT_IMAGE_FIELD_NUMBER: _ClassVar[int]
    zone: str
    machine_type: str
    container_images: _containers.RepeatedCompositeFieldContainer[_environment_pb2.ContainerImage]
    data_disk: LocalDisk
    encryption_config: EncryptionConfig
    shielded_instance_config: RuntimeShieldedInstanceConfig
    accelerator_config: RuntimeAcceleratorConfig
    network: str
    subnet: str
    internal_ip_only: bool
    tags: _containers.RepeatedScalarFieldContainer[str]
    guest_attributes: _containers.ScalarMap[str, str]
    metadata: _containers.ScalarMap[str, str]
    labels: _containers.ScalarMap[str, str]
    nic_type: VirtualMachineConfig.NicType
    reserved_ip_range: str
    boot_image: VirtualMachineConfig.BootImage
    def __init__(self, zone: _Optional[str] = ..., machine_type: _Optional[str] = ..., container_images: _Optional[_Iterable[_Union[_environment_pb2.ContainerImage, _Mapping]]] = ..., data_disk: _Optional[_Union[LocalDisk, _Mapping]] = ..., encryption_config: _Optional[_Union[EncryptionConfig, _Mapping]] = ..., shielded_instance_config: _Optional[_Union[RuntimeShieldedInstanceConfig, _Mapping]] = ..., accelerator_config: _Optional[_Union[RuntimeAcceleratorConfig, _Mapping]] = ..., network: _Optional[str] = ..., subnet: _Optional[str] = ..., internal_ip_only: bool = ..., tags: _Optional[_Iterable[str]] = ..., guest_attributes: _Optional[_Mapping[str, str]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., labels: _Optional[_Mapping[str, str]] = ..., nic_type: _Optional[_Union[VirtualMachineConfig.NicType, str]] = ..., reserved_ip_range: _Optional[str] = ..., boot_image: _Optional[_Union[VirtualMachineConfig.BootImage, _Mapping]] = ...) -> None: ...
