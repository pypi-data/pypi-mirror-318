from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DbNode(_message.Message):
    __slots__ = ('name', 'properties')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    properties: DbNodeProperties

    def __init__(self, name: _Optional[str]=..., properties: _Optional[_Union[DbNodeProperties, _Mapping]]=...) -> None:
        ...

class DbNodeProperties(_message.Message):
    __slots__ = ('ocid', 'ocpu_count', 'memory_size_gb', 'db_node_storage_size_gb', 'db_server_ocid', 'hostname', 'state', 'total_cpu_core_count')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[DbNodeProperties.State]
        PROVISIONING: _ClassVar[DbNodeProperties.State]
        AVAILABLE: _ClassVar[DbNodeProperties.State]
        UPDATING: _ClassVar[DbNodeProperties.State]
        STOPPING: _ClassVar[DbNodeProperties.State]
        STOPPED: _ClassVar[DbNodeProperties.State]
        STARTING: _ClassVar[DbNodeProperties.State]
        TERMINATING: _ClassVar[DbNodeProperties.State]
        TERMINATED: _ClassVar[DbNodeProperties.State]
        FAILED: _ClassVar[DbNodeProperties.State]
    STATE_UNSPECIFIED: DbNodeProperties.State
    PROVISIONING: DbNodeProperties.State
    AVAILABLE: DbNodeProperties.State
    UPDATING: DbNodeProperties.State
    STOPPING: DbNodeProperties.State
    STOPPED: DbNodeProperties.State
    STARTING: DbNodeProperties.State
    TERMINATING: DbNodeProperties.State
    TERMINATED: DbNodeProperties.State
    FAILED: DbNodeProperties.State
    OCID_FIELD_NUMBER: _ClassVar[int]
    OCPU_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    DB_NODE_STORAGE_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    DB_SERVER_OCID_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CPU_CORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    ocid: str
    ocpu_count: int
    memory_size_gb: int
    db_node_storage_size_gb: int
    db_server_ocid: str
    hostname: str
    state: DbNodeProperties.State
    total_cpu_core_count: int

    def __init__(self, ocid: _Optional[str]=..., ocpu_count: _Optional[int]=..., memory_size_gb: _Optional[int]=..., db_node_storage_size_gb: _Optional[int]=..., db_server_ocid: _Optional[str]=..., hostname: _Optional[str]=..., state: _Optional[_Union[DbNodeProperties.State, str]]=..., total_cpu_core_count: _Optional[int]=...) -> None:
        ...