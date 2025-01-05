from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class VariableState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VARIABLE_STATE_UNSPECIFIED: _ClassVar[VariableState]
    UPDATED: _ClassVar[VariableState]
    DELETED: _ClassVar[VariableState]
VARIABLE_STATE_UNSPECIFIED: VariableState
UPDATED: VariableState
DELETED: VariableState

class RuntimeConfig(_message.Message):
    __slots__ = ('name', 'description')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class Variable(_message.Message):
    __slots__ = ('name', 'value', 'text', 'update_time', 'state')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: bytes
    text: str
    update_time: _timestamp_pb2.Timestamp
    state: VariableState

    def __init__(self, name: _Optional[str]=..., value: _Optional[bytes]=..., text: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[VariableState, str]]=...) -> None:
        ...

class EndCondition(_message.Message):
    __slots__ = ('cardinality',)

    class Cardinality(_message.Message):
        __slots__ = ('path', 'number')
        PATH_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        path: str
        number: int

        def __init__(self, path: _Optional[str]=..., number: _Optional[int]=...) -> None:
            ...
    CARDINALITY_FIELD_NUMBER: _ClassVar[int]
    cardinality: EndCondition.Cardinality

    def __init__(self, cardinality: _Optional[_Union[EndCondition.Cardinality, _Mapping]]=...) -> None:
        ...

class Waiter(_message.Message):
    __slots__ = ('name', 'timeout', 'failure', 'success', 'create_time', 'done', 'error')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DONE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    name: str
    timeout: _duration_pb2.Duration
    failure: EndCondition
    success: EndCondition
    create_time: _timestamp_pb2.Timestamp
    done: bool
    error: _status_pb2.Status

    def __init__(self, name: _Optional[str]=..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., failure: _Optional[_Union[EndCondition, _Mapping]]=..., success: _Optional[_Union[EndCondition, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., done: bool=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...