from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SqlResult(_message.Message):
    __slots__ = ("columns", "rows")
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedCompositeFieldContainer[SqlResultColumn]
    rows: _containers.RepeatedCompositeFieldContainer[SqlResultRow]
    def __init__(self, columns: _Optional[_Iterable[_Union[SqlResultColumn, _Mapping]]] = ..., rows: _Optional[_Iterable[_Union[SqlResultRow, _Mapping]]] = ...) -> None: ...

class SqlResultColumn(_message.Message):
    __slots__ = ("name", "type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class SqlResultRow(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[SqlResultValue]
    def __init__(self, values: _Optional[_Iterable[_Union[SqlResultValue, _Mapping]]] = ...) -> None: ...

class SqlResultValue(_message.Message):
    __slots__ = ("value", "null_value")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NULL_VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    null_value: bool
    def __init__(self, value: _Optional[str] = ..., null_value: bool = ...) -> None: ...
