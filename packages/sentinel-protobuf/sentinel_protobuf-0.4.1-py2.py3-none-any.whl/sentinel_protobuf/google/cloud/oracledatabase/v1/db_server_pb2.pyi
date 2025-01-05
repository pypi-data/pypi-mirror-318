from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DbServer(_message.Message):
    __slots__ = ('name', 'display_name', 'properties')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    properties: DbServerProperties

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., properties: _Optional[_Union[DbServerProperties, _Mapping]]=...) -> None:
        ...

class DbServerProperties(_message.Message):
    __slots__ = ('ocid', 'ocpu_count', 'max_ocpu_count', 'memory_size_gb', 'max_memory_size_gb', 'db_node_storage_size_gb', 'max_db_node_storage_size_gb', 'vm_count', 'state', 'db_node_ids')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[DbServerProperties.State]
        CREATING: _ClassVar[DbServerProperties.State]
        AVAILABLE: _ClassVar[DbServerProperties.State]
        UNAVAILABLE: _ClassVar[DbServerProperties.State]
        DELETING: _ClassVar[DbServerProperties.State]
        DELETED: _ClassVar[DbServerProperties.State]
    STATE_UNSPECIFIED: DbServerProperties.State
    CREATING: DbServerProperties.State
    AVAILABLE: DbServerProperties.State
    UNAVAILABLE: DbServerProperties.State
    DELETING: DbServerProperties.State
    DELETED: DbServerProperties.State
    OCID_FIELD_NUMBER: _ClassVar[int]
    OCPU_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_OCPU_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMORY_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    DB_NODE_STORAGE_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    MAX_DB_NODE_STORAGE_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    VM_COUNT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DB_NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    ocid: str
    ocpu_count: int
    max_ocpu_count: int
    memory_size_gb: int
    max_memory_size_gb: int
    db_node_storage_size_gb: int
    max_db_node_storage_size_gb: int
    vm_count: int
    state: DbServerProperties.State
    db_node_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, ocid: _Optional[str]=..., ocpu_count: _Optional[int]=..., max_ocpu_count: _Optional[int]=..., memory_size_gb: _Optional[int]=..., max_memory_size_gb: _Optional[int]=..., db_node_storage_size_gb: _Optional[int]=..., max_db_node_storage_size_gb: _Optional[int]=..., vm_count: _Optional[int]=..., state: _Optional[_Union[DbServerProperties.State, str]]=..., db_node_ids: _Optional[_Iterable[str]]=...) -> None:
        ...