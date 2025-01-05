from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.netapp.v1 import common_pb2 as _common_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetStoragePoolRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListStoragePoolsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "order_by", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListStoragePoolsResponse(_message.Message):
    __slots__ = ("storage_pools", "next_page_token", "unreachable")
    STORAGE_POOLS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    storage_pools: _containers.RepeatedCompositeFieldContainer[StoragePool]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, storage_pools: _Optional[_Iterable[_Union[StoragePool, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateStoragePoolRequest(_message.Message):
    __slots__ = ("parent", "storage_pool_id", "storage_pool")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POOL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    storage_pool_id: str
    storage_pool: StoragePool
    def __init__(self, parent: _Optional[str] = ..., storage_pool_id: _Optional[str] = ..., storage_pool: _Optional[_Union[StoragePool, _Mapping]] = ...) -> None: ...

class UpdateStoragePoolRequest(_message.Message):
    __slots__ = ("update_mask", "storage_pool")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POOL_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    storage_pool: StoragePool
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., storage_pool: _Optional[_Union[StoragePool, _Mapping]] = ...) -> None: ...

class DeleteStoragePoolRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class SwitchActiveReplicaZoneRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class StoragePool(_message.Message):
    __slots__ = ("name", "service_level", "capacity_gib", "volume_capacity_gib", "volume_count", "state", "state_details", "create_time", "description", "labels", "network", "active_directory", "kms_config", "ldap_enabled", "psa_range", "encryption_type", "global_access_allowed", "allow_auto_tiering", "replica_zone", "zone")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[StoragePool.State]
        READY: _ClassVar[StoragePool.State]
        CREATING: _ClassVar[StoragePool.State]
        DELETING: _ClassVar[StoragePool.State]
        UPDATING: _ClassVar[StoragePool.State]
        RESTORING: _ClassVar[StoragePool.State]
        DISABLED: _ClassVar[StoragePool.State]
        ERROR: _ClassVar[StoragePool.State]
    STATE_UNSPECIFIED: StoragePool.State
    READY: StoragePool.State
    CREATING: StoragePool.State
    DELETING: StoragePool.State
    UPDATING: StoragePool.State
    RESTORING: StoragePool.State
    DISABLED: StoragePool.State
    ERROR: StoragePool.State
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_GIB_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CAPACITY_GIB_FIELD_NUMBER: _ClassVar[int]
    VOLUME_COUNT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    KMS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LDAP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PSA_RANGE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_ACCESS_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    ALLOW_AUTO_TIERING_FIELD_NUMBER: _ClassVar[int]
    REPLICA_ZONE_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    name: str
    service_level: _common_pb2.ServiceLevel
    capacity_gib: int
    volume_capacity_gib: int
    volume_count: int
    state: StoragePool.State
    state_details: str
    create_time: _timestamp_pb2.Timestamp
    description: str
    labels: _containers.ScalarMap[str, str]
    network: str
    active_directory: str
    kms_config: str
    ldap_enabled: bool
    psa_range: str
    encryption_type: _common_pb2.EncryptionType
    global_access_allowed: bool
    allow_auto_tiering: bool
    replica_zone: str
    zone: str
    def __init__(self, name: _Optional[str] = ..., service_level: _Optional[_Union[_common_pb2.ServiceLevel, str]] = ..., capacity_gib: _Optional[int] = ..., volume_capacity_gib: _Optional[int] = ..., volume_count: _Optional[int] = ..., state: _Optional[_Union[StoragePool.State, str]] = ..., state_details: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., description: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., network: _Optional[str] = ..., active_directory: _Optional[str] = ..., kms_config: _Optional[str] = ..., ldap_enabled: bool = ..., psa_range: _Optional[str] = ..., encryption_type: _Optional[_Union[_common_pb2.EncryptionType, str]] = ..., global_access_allowed: bool = ..., allow_auto_tiering: bool = ..., replica_zone: _Optional[str] = ..., zone: _Optional[str] = ...) -> None: ...
