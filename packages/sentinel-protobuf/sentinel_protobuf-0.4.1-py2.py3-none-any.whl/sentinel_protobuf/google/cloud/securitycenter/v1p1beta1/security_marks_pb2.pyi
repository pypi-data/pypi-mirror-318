from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class SecurityMarks(_message.Message):
    __slots__ = ('name', 'marks', 'canonical_name')

    class MarksEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    MARKS_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    marks: _containers.ScalarMap[str, str]
    canonical_name: str

    def __init__(self, name: _Optional[str]=..., marks: _Optional[_Mapping[str, str]]=..., canonical_name: _Optional[str]=...) -> None:
        ...