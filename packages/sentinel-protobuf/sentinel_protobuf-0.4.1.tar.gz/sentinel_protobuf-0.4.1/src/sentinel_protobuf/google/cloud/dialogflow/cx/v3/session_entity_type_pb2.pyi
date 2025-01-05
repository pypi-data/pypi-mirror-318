from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.cx.v3 import entity_type_pb2 as _entity_type_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SessionEntityType(_message.Message):
    __slots__ = ('name', 'entity_override_mode', 'entities')

    class EntityOverrideMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENTITY_OVERRIDE_MODE_UNSPECIFIED: _ClassVar[SessionEntityType.EntityOverrideMode]
        ENTITY_OVERRIDE_MODE_OVERRIDE: _ClassVar[SessionEntityType.EntityOverrideMode]
        ENTITY_OVERRIDE_MODE_SUPPLEMENT: _ClassVar[SessionEntityType.EntityOverrideMode]
    ENTITY_OVERRIDE_MODE_UNSPECIFIED: SessionEntityType.EntityOverrideMode
    ENTITY_OVERRIDE_MODE_OVERRIDE: SessionEntityType.EntityOverrideMode
    ENTITY_OVERRIDE_MODE_SUPPLEMENT: SessionEntityType.EntityOverrideMode
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_OVERRIDE_MODE_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    entity_override_mode: SessionEntityType.EntityOverrideMode
    entities: _containers.RepeatedCompositeFieldContainer[_entity_type_pb2.EntityType.Entity]

    def __init__(self, name: _Optional[str]=..., entity_override_mode: _Optional[_Union[SessionEntityType.EntityOverrideMode, str]]=..., entities: _Optional[_Iterable[_Union[_entity_type_pb2.EntityType.Entity, _Mapping]]]=...) -> None:
        ...

class ListSessionEntityTypesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListSessionEntityTypesResponse(_message.Message):
    __slots__ = ('session_entity_types', 'next_page_token')
    SESSION_ENTITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    session_entity_types: _containers.RepeatedCompositeFieldContainer[SessionEntityType]
    next_page_token: str

    def __init__(self, session_entity_types: _Optional[_Iterable[_Union[SessionEntityType, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetSessionEntityTypeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateSessionEntityTypeRequest(_message.Message):
    __slots__ = ('parent', 'session_entity_type')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SESSION_ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    session_entity_type: SessionEntityType

    def __init__(self, parent: _Optional[str]=..., session_entity_type: _Optional[_Union[SessionEntityType, _Mapping]]=...) -> None:
        ...

class UpdateSessionEntityTypeRequest(_message.Message):
    __slots__ = ('session_entity_type', 'update_mask')
    SESSION_ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    session_entity_type: SessionEntityType
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, session_entity_type: _Optional[_Union[SessionEntityType, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteSessionEntityTypeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...