from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1beta1 import machine_resources_pb2 as _machine_resources_pb2
from google.cloud.aiplatform.v1beta1 import service_networking_pb2 as _service_networking_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PersistentResource(_message.Message):
    __slots__ = ("name", "display_name", "resource_pools", "state", "error", "create_time", "start_time", "update_time", "labels", "network", "psc_interface_config", "encryption_spec", "resource_runtime_spec", "resource_runtime", "reserved_ip_ranges", "satisfies_pzs", "satisfies_pzi")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PersistentResource.State]
        PROVISIONING: _ClassVar[PersistentResource.State]
        RUNNING: _ClassVar[PersistentResource.State]
        STOPPING: _ClassVar[PersistentResource.State]
        ERROR: _ClassVar[PersistentResource.State]
        REBOOTING: _ClassVar[PersistentResource.State]
        UPDATING: _ClassVar[PersistentResource.State]
    STATE_UNSPECIFIED: PersistentResource.State
    PROVISIONING: PersistentResource.State
    RUNNING: PersistentResource.State
    STOPPING: PersistentResource.State
    ERROR: PersistentResource.State
    REBOOTING: PersistentResource.State
    UPDATING: PersistentResource.State
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOLS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    PSC_INTERFACE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_RUNTIME_SPEC_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    RESERVED_IP_RANGES_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    resource_pools: _containers.RepeatedCompositeFieldContainer[ResourcePool]
    state: PersistentResource.State
    error: _status_pb2.Status
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    network: str
    psc_interface_config: _service_networking_pb2.PscInterfaceConfig
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    resource_runtime_spec: ResourceRuntimeSpec
    resource_runtime: ResourceRuntime
    reserved_ip_ranges: _containers.RepeatedScalarFieldContainer[str]
    satisfies_pzs: bool
    satisfies_pzi: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., resource_pools: _Optional[_Iterable[_Union[ResourcePool, _Mapping]]] = ..., state: _Optional[_Union[PersistentResource.State, str]] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., network: _Optional[str] = ..., psc_interface_config: _Optional[_Union[_service_networking_pb2.PscInterfaceConfig, _Mapping]] = ..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]] = ..., resource_runtime_spec: _Optional[_Union[ResourceRuntimeSpec, _Mapping]] = ..., resource_runtime: _Optional[_Union[ResourceRuntime, _Mapping]] = ..., reserved_ip_ranges: _Optional[_Iterable[str]] = ..., satisfies_pzs: bool = ..., satisfies_pzi: bool = ...) -> None: ...

class ResourcePool(_message.Message):
    __slots__ = ("id", "machine_spec", "replica_count", "disk_spec", "used_replica_count", "autoscaling_spec")
    class AutoscalingSpec(_message.Message):
        __slots__ = ("min_replica_count", "max_replica_count")
        MIN_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
        MAX_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
        min_replica_count: int
        max_replica_count: int
        def __init__(self, min_replica_count: _Optional[int] = ..., max_replica_count: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    MACHINE_SPEC_FIELD_NUMBER: _ClassVar[int]
    REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    DISK_SPEC_FIELD_NUMBER: _ClassVar[int]
    USED_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_SPEC_FIELD_NUMBER: _ClassVar[int]
    id: str
    machine_spec: _machine_resources_pb2.MachineSpec
    replica_count: int
    disk_spec: _machine_resources_pb2.DiskSpec
    used_replica_count: int
    autoscaling_spec: ResourcePool.AutoscalingSpec
    def __init__(self, id: _Optional[str] = ..., machine_spec: _Optional[_Union[_machine_resources_pb2.MachineSpec, _Mapping]] = ..., replica_count: _Optional[int] = ..., disk_spec: _Optional[_Union[_machine_resources_pb2.DiskSpec, _Mapping]] = ..., used_replica_count: _Optional[int] = ..., autoscaling_spec: _Optional[_Union[ResourcePool.AutoscalingSpec, _Mapping]] = ...) -> None: ...

class ResourceRuntimeSpec(_message.Message):
    __slots__ = ("service_account_spec", "ray_spec")
    SERVICE_ACCOUNT_SPEC_FIELD_NUMBER: _ClassVar[int]
    RAY_SPEC_FIELD_NUMBER: _ClassVar[int]
    service_account_spec: ServiceAccountSpec
    ray_spec: RaySpec
    def __init__(self, service_account_spec: _Optional[_Union[ServiceAccountSpec, _Mapping]] = ..., ray_spec: _Optional[_Union[RaySpec, _Mapping]] = ...) -> None: ...

class RaySpec(_message.Message):
    __slots__ = ("image_uri", "nfs_mounts", "resource_pool_images", "head_node_resource_pool_id", "ray_metric_spec", "ray_logs_spec")
    class ResourcePoolImagesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    NFS_MOUNTS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POOL_IMAGES_FIELD_NUMBER: _ClassVar[int]
    HEAD_NODE_RESOURCE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    RAY_METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    RAY_LOGS_SPEC_FIELD_NUMBER: _ClassVar[int]
    image_uri: str
    nfs_mounts: _containers.RepeatedCompositeFieldContainer[_machine_resources_pb2.NfsMount]
    resource_pool_images: _containers.ScalarMap[str, str]
    head_node_resource_pool_id: str
    ray_metric_spec: RayMetricSpec
    ray_logs_spec: RayLogsSpec
    def __init__(self, image_uri: _Optional[str] = ..., nfs_mounts: _Optional[_Iterable[_Union[_machine_resources_pb2.NfsMount, _Mapping]]] = ..., resource_pool_images: _Optional[_Mapping[str, str]] = ..., head_node_resource_pool_id: _Optional[str] = ..., ray_metric_spec: _Optional[_Union[RayMetricSpec, _Mapping]] = ..., ray_logs_spec: _Optional[_Union[RayLogsSpec, _Mapping]] = ...) -> None: ...

class ResourceRuntime(_message.Message):
    __slots__ = ("access_uris", "notebook_runtime_template")
    class AccessUrisEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACCESS_URIS_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_RUNTIME_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    access_uris: _containers.ScalarMap[str, str]
    notebook_runtime_template: str
    def __init__(self, access_uris: _Optional[_Mapping[str, str]] = ..., notebook_runtime_template: _Optional[str] = ...) -> None: ...

class ServiceAccountSpec(_message.Message):
    __slots__ = ("enable_custom_service_account", "service_account")
    ENABLE_CUSTOM_SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    enable_custom_service_account: bool
    service_account: str
    def __init__(self, enable_custom_service_account: bool = ..., service_account: _Optional[str] = ...) -> None: ...

class RayMetricSpec(_message.Message):
    __slots__ = ("disabled",)
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    disabled: bool
    def __init__(self, disabled: bool = ...) -> None: ...

class RayLogsSpec(_message.Message):
    __slots__ = ("disabled",)
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    disabled: bool
    def __init__(self, disabled: bool = ...) -> None: ...
