from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class TableReadOptions(_message.Message):
    __slots__ = ('selected_fields', 'row_restriction')
    SELECTED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    ROW_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    selected_fields: _containers.RepeatedScalarFieldContainer[str]
    row_restriction: str

    def __init__(self, selected_fields: _Optional[_Iterable[str]]=..., row_restriction: _Optional[str]=...) -> None:
        ...