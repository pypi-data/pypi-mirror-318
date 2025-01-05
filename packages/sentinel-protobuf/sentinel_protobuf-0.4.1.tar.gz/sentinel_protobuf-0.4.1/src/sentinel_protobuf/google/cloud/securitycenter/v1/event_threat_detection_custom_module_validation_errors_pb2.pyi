from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CustomModuleValidationErrors(_message.Message):
    __slots__ = ("errors",)
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[CustomModuleValidationError]
    def __init__(self, errors: _Optional[_Iterable[_Union[CustomModuleValidationError, _Mapping]]] = ...) -> None: ...

class CustomModuleValidationError(_message.Message):
    __slots__ = ("description", "field_path", "start", "end")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    description: str
    field_path: str
    start: Position
    end: Position
    def __init__(self, description: _Optional[str] = ..., field_path: _Optional[str] = ..., start: _Optional[_Union[Position, _Mapping]] = ..., end: _Optional[_Union[Position, _Mapping]] = ...) -> None: ...

class Position(_message.Message):
    __slots__ = ("line_number", "column_number")
    LINE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NUMBER_FIELD_NUMBER: _ClassVar[int]
    line_number: int
    column_number: int
    def __init__(self, line_number: _Optional[int] = ..., column_number: _Optional[int] = ...) -> None: ...
