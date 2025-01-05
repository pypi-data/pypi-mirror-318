from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class IndexField(_message.Message):
    __slots__ = ('field_path', 'mode')

    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[IndexField.Mode]
        ASCENDING: _ClassVar[IndexField.Mode]
        DESCENDING: _ClassVar[IndexField.Mode]
        ARRAY_CONTAINS: _ClassVar[IndexField.Mode]
    MODE_UNSPECIFIED: IndexField.Mode
    ASCENDING: IndexField.Mode
    DESCENDING: IndexField.Mode
    ARRAY_CONTAINS: IndexField.Mode
    FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    field_path: str
    mode: IndexField.Mode

    def __init__(self, field_path: _Optional[str]=..., mode: _Optional[_Union[IndexField.Mode, str]]=...) -> None:
        ...

class Index(_message.Message):
    __slots__ = ('name', 'collection_id', 'fields', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Index.State]
        CREATING: _ClassVar[Index.State]
        READY: _ClassVar[Index.State]
        ERROR: _ClassVar[Index.State]
    STATE_UNSPECIFIED: Index.State
    CREATING: Index.State
    READY: Index.State
    ERROR: Index.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    collection_id: str
    fields: _containers.RepeatedCompositeFieldContainer[IndexField]
    state: Index.State

    def __init__(self, name: _Optional[str]=..., collection_id: _Optional[str]=..., fields: _Optional[_Iterable[_Union[IndexField, _Mapping]]]=..., state: _Optional[_Union[Index.State, str]]=...) -> None:
        ...