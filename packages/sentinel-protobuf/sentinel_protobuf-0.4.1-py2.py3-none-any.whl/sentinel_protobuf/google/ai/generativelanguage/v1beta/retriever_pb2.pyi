from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Corpus(_message.Message):
    __slots__ = ('name', 'display_name', 'create_time', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Document(_message.Message):
    __slots__ = ('name', 'display_name', 'custom_metadata', 'update_time', 'create_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_METADATA_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    custom_metadata: _containers.RepeatedCompositeFieldContainer[CustomMetadata]
    update_time: _timestamp_pb2.Timestamp
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., custom_metadata: _Optional[_Iterable[_Union[CustomMetadata, _Mapping]]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class StringList(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, values: _Optional[_Iterable[str]]=...) -> None:
        ...

class CustomMetadata(_message.Message):
    __slots__ = ('string_value', 'string_list_value', 'numeric_value', 'key')
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_LIST_VALUE_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_VALUE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    string_value: str
    string_list_value: StringList
    numeric_value: float
    key: str

    def __init__(self, string_value: _Optional[str]=..., string_list_value: _Optional[_Union[StringList, _Mapping]]=..., numeric_value: _Optional[float]=..., key: _Optional[str]=...) -> None:
        ...

class MetadataFilter(_message.Message):
    __slots__ = ('key', 'conditions')
    KEY_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    key: str
    conditions: _containers.RepeatedCompositeFieldContainer[Condition]

    def __init__(self, key: _Optional[str]=..., conditions: _Optional[_Iterable[_Union[Condition, _Mapping]]]=...) -> None:
        ...

class Condition(_message.Message):
    __slots__ = ('string_value', 'numeric_value', 'operation')

    class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATOR_UNSPECIFIED: _ClassVar[Condition.Operator]
        LESS: _ClassVar[Condition.Operator]
        LESS_EQUAL: _ClassVar[Condition.Operator]
        EQUAL: _ClassVar[Condition.Operator]
        GREATER_EQUAL: _ClassVar[Condition.Operator]
        GREATER: _ClassVar[Condition.Operator]
        NOT_EQUAL: _ClassVar[Condition.Operator]
        INCLUDES: _ClassVar[Condition.Operator]
        EXCLUDES: _ClassVar[Condition.Operator]
    OPERATOR_UNSPECIFIED: Condition.Operator
    LESS: Condition.Operator
    LESS_EQUAL: Condition.Operator
    EQUAL: Condition.Operator
    GREATER_EQUAL: Condition.Operator
    GREATER: Condition.Operator
    NOT_EQUAL: Condition.Operator
    INCLUDES: Condition.Operator
    EXCLUDES: Condition.Operator
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    string_value: str
    numeric_value: float
    operation: Condition.Operator

    def __init__(self, string_value: _Optional[str]=..., numeric_value: _Optional[float]=..., operation: _Optional[_Union[Condition.Operator, str]]=...) -> None:
        ...

class Chunk(_message.Message):
    __slots__ = ('name', 'data', 'custom_metadata', 'create_time', 'update_time', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Chunk.State]
        STATE_PENDING_PROCESSING: _ClassVar[Chunk.State]
        STATE_ACTIVE: _ClassVar[Chunk.State]
        STATE_FAILED: _ClassVar[Chunk.State]
    STATE_UNSPECIFIED: Chunk.State
    STATE_PENDING_PROCESSING: Chunk.State
    STATE_ACTIVE: Chunk.State
    STATE_FAILED: Chunk.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    data: ChunkData
    custom_metadata: _containers.RepeatedCompositeFieldContainer[CustomMetadata]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    state: Chunk.State

    def __init__(self, name: _Optional[str]=..., data: _Optional[_Union[ChunkData, _Mapping]]=..., custom_metadata: _Optional[_Iterable[_Union[CustomMetadata, _Mapping]]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[Chunk.State, str]]=...) -> None:
        ...

class ChunkData(_message.Message):
    __slots__ = ('string_value',)
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    string_value: str

    def __init__(self, string_value: _Optional[str]=...) -> None:
        ...