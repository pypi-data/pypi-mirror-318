from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Index(_message.Message):
    __slots__ = ('project_id', 'index_id', 'kind', 'ancestor', 'properties', 'state')

    class AncestorMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANCESTOR_MODE_UNSPECIFIED: _ClassVar[Index.AncestorMode]
        NONE: _ClassVar[Index.AncestorMode]
        ALL_ANCESTORS: _ClassVar[Index.AncestorMode]
    ANCESTOR_MODE_UNSPECIFIED: Index.AncestorMode
    NONE: Index.AncestorMode
    ALL_ANCESTORS: Index.AncestorMode

    class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DIRECTION_UNSPECIFIED: _ClassVar[Index.Direction]
        ASCENDING: _ClassVar[Index.Direction]
        DESCENDING: _ClassVar[Index.Direction]
    DIRECTION_UNSPECIFIED: Index.Direction
    ASCENDING: Index.Direction
    DESCENDING: Index.Direction

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Index.State]
        CREATING: _ClassVar[Index.State]
        READY: _ClassVar[Index.State]
        DELETING: _ClassVar[Index.State]
        ERROR: _ClassVar[Index.State]
    STATE_UNSPECIFIED: Index.State
    CREATING: Index.State
    READY: Index.State
    DELETING: Index.State
    ERROR: Index.State

    class IndexedProperty(_message.Message):
        __slots__ = ('name', 'direction')
        NAME_FIELD_NUMBER: _ClassVar[int]
        DIRECTION_FIELD_NUMBER: _ClassVar[int]
        name: str
        direction: Index.Direction

        def __init__(self, name: _Optional[str]=..., direction: _Optional[_Union[Index.Direction, str]]=...) -> None:
            ...
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    index_id: str
    kind: str
    ancestor: Index.AncestorMode
    properties: _containers.RepeatedCompositeFieldContainer[Index.IndexedProperty]
    state: Index.State

    def __init__(self, project_id: _Optional[str]=..., index_id: _Optional[str]=..., kind: _Optional[str]=..., ancestor: _Optional[_Union[Index.AncestorMode, str]]=..., properties: _Optional[_Iterable[_Union[Index.IndexedProperty, _Mapping]]]=..., state: _Optional[_Union[Index.State, str]]=...) -> None:
        ...