from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Execution(_message.Message):
    __slots__ = ('name', 'display_name', 'state', 'etag', 'labels', 'create_time', 'update_time', 'schema_title', 'schema_version', 'metadata', 'description')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Execution.State]
        NEW: _ClassVar[Execution.State]
        RUNNING: _ClassVar[Execution.State]
        COMPLETE: _ClassVar[Execution.State]
        FAILED: _ClassVar[Execution.State]
        CACHED: _ClassVar[Execution.State]
        CANCELLED: _ClassVar[Execution.State]
    STATE_UNSPECIFIED: Execution.State
    NEW: Execution.State
    RUNNING: Execution.State
    COMPLETE: Execution.State
    FAILED: Execution.State
    CACHED: Execution.State
    CANCELLED: Execution.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_TITLE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    state: Execution.State
    etag: str
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    schema_title: str
    schema_version: str
    metadata: _struct_pb2.Struct
    description: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., state: _Optional[_Union[Execution.State, str]]=..., etag: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., schema_title: _Optional[str]=..., schema_version: _Optional[str]=..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., description: _Optional[str]=...) -> None:
        ...