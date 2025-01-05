from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class TableDisplayOptions(_message.Message):
    __slots__ = ('shown_columns',)
    SHOWN_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    shown_columns: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, shown_columns: _Optional[_Iterable[str]]=...) -> None:
        ...