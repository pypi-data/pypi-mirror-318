from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ('target', 'resume_marker')
    TARGET_FIELD_NUMBER: _ClassVar[int]
    RESUME_MARKER_FIELD_NUMBER: _ClassVar[int]
    target: str
    resume_marker: bytes

    def __init__(self, target: _Optional[str]=..., resume_marker: _Optional[bytes]=...) -> None:
        ...

class ChangeBatch(_message.Message):
    __slots__ = ('changes',)
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[Change]

    def __init__(self, changes: _Optional[_Iterable[_Union[Change, _Mapping]]]=...) -> None:
        ...

class Change(_message.Message):
    __slots__ = ('element', 'state', 'data', 'resume_marker', 'continued')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXISTS: _ClassVar[Change.State]
        DOES_NOT_EXIST: _ClassVar[Change.State]
        INITIAL_STATE_SKIPPED: _ClassVar[Change.State]
        ERROR: _ClassVar[Change.State]
    EXISTS: Change.State
    DOES_NOT_EXIST: Change.State
    INITIAL_STATE_SKIPPED: Change.State
    ERROR: Change.State
    ELEMENT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    RESUME_MARKER_FIELD_NUMBER: _ClassVar[int]
    CONTINUED_FIELD_NUMBER: _ClassVar[int]
    element: str
    state: Change.State
    data: _any_pb2.Any
    resume_marker: bytes
    continued: bool

    def __init__(self, element: _Optional[str]=..., state: _Optional[_Union[Change.State, str]]=..., data: _Optional[_Union[_any_pb2.Any, _Mapping]]=..., resume_marker: _Optional[bytes]=..., continued: bool=...) -> None:
        ...