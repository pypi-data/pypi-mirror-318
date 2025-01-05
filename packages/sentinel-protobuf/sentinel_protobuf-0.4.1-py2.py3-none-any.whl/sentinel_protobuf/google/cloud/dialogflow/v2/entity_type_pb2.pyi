from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EntityType(_message.Message):
    __slots__ = ('name', 'display_name', 'kind', 'auto_expansion_mode', 'entities', 'enable_fuzzy_extraction')

    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KIND_UNSPECIFIED: _ClassVar[EntityType.Kind]
        KIND_MAP: _ClassVar[EntityType.Kind]
        KIND_LIST: _ClassVar[EntityType.Kind]
        KIND_REGEXP: _ClassVar[EntityType.Kind]
    KIND_UNSPECIFIED: EntityType.Kind
    KIND_MAP: EntityType.Kind
    KIND_LIST: EntityType.Kind
    KIND_REGEXP: EntityType.Kind

    class AutoExpansionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AUTO_EXPANSION_MODE_UNSPECIFIED: _ClassVar[EntityType.AutoExpansionMode]
        AUTO_EXPANSION_MODE_DEFAULT: _ClassVar[EntityType.AutoExpansionMode]
    AUTO_EXPANSION_MODE_UNSPECIFIED: EntityType.AutoExpansionMode
    AUTO_EXPANSION_MODE_DEFAULT: EntityType.AutoExpansionMode

    class Entity(_message.Message):
        __slots__ = ('value', 'synonyms')
        VALUE_FIELD_NUMBER: _ClassVar[int]
        SYNONYMS_FIELD_NUMBER: _ClassVar[int]
        value: str
        synonyms: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, value: _Optional[str]=..., synonyms: _Optional[_Iterable[str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    AUTO_EXPANSION_MODE_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FUZZY_EXTRACTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    kind: EntityType.Kind
    auto_expansion_mode: EntityType.AutoExpansionMode
    entities: _containers.RepeatedCompositeFieldContainer[EntityType.Entity]
    enable_fuzzy_extraction: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., kind: _Optional[_Union[EntityType.Kind, str]]=..., auto_expansion_mode: _Optional[_Union[EntityType.AutoExpansionMode, str]]=..., entities: _Optional[_Iterable[_Union[EntityType.Entity, _Mapping]]]=..., enable_fuzzy_extraction: bool=...) -> None:
        ...

class ListEntityTypesRequest(_message.Message):
    __slots__ = ('parent', 'language_code', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    language_code: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., language_code: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListEntityTypesResponse(_message.Message):
    __slots__ = ('entity_types', 'next_page_token')
    ENTITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    entity_types: _containers.RepeatedCompositeFieldContainer[EntityType]
    next_page_token: str

    def __init__(self, entity_types: _Optional[_Iterable[_Union[EntityType, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetEntityTypeRequest(_message.Message):
    __slots__ = ('name', 'language_code')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    language_code: str

    def __init__(self, name: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class CreateEntityTypeRequest(_message.Message):
    __slots__ = ('parent', 'entity_type', 'language_code')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entity_type: EntityType
    language_code: str

    def __init__(self, parent: _Optional[str]=..., entity_type: _Optional[_Union[EntityType, _Mapping]]=..., language_code: _Optional[str]=...) -> None:
        ...

class UpdateEntityTypeRequest(_message.Message):
    __slots__ = ('entity_type', 'language_code', 'update_mask')
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    entity_type: EntityType
    language_code: str
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, entity_type: _Optional[_Union[EntityType, _Mapping]]=..., language_code: _Optional[str]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteEntityTypeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class BatchUpdateEntityTypesRequest(_message.Message):
    __slots__ = ('parent', 'entity_type_batch_uri', 'entity_type_batch_inline', 'language_code', 'update_mask')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_BATCH_URI_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_BATCH_INLINE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entity_type_batch_uri: str
    entity_type_batch_inline: EntityTypeBatch
    language_code: str
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, parent: _Optional[str]=..., entity_type_batch_uri: _Optional[str]=..., entity_type_batch_inline: _Optional[_Union[EntityTypeBatch, _Mapping]]=..., language_code: _Optional[str]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class BatchUpdateEntityTypesResponse(_message.Message):
    __slots__ = ('entity_types',)
    ENTITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    entity_types: _containers.RepeatedCompositeFieldContainer[EntityType]

    def __init__(self, entity_types: _Optional[_Iterable[_Union[EntityType, _Mapping]]]=...) -> None:
        ...

class BatchDeleteEntityTypesRequest(_message.Message):
    __slots__ = ('parent', 'entity_type_names')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_NAMES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entity_type_names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, parent: _Optional[str]=..., entity_type_names: _Optional[_Iterable[str]]=...) -> None:
        ...

class BatchCreateEntitiesRequest(_message.Message):
    __slots__ = ('parent', 'entities', 'language_code')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entities: _containers.RepeatedCompositeFieldContainer[EntityType.Entity]
    language_code: str

    def __init__(self, parent: _Optional[str]=..., entities: _Optional[_Iterable[_Union[EntityType.Entity, _Mapping]]]=..., language_code: _Optional[str]=...) -> None:
        ...

class BatchUpdateEntitiesRequest(_message.Message):
    __slots__ = ('parent', 'entities', 'language_code', 'update_mask')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entities: _containers.RepeatedCompositeFieldContainer[EntityType.Entity]
    language_code: str
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, parent: _Optional[str]=..., entities: _Optional[_Iterable[_Union[EntityType.Entity, _Mapping]]]=..., language_code: _Optional[str]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class BatchDeleteEntitiesRequest(_message.Message):
    __slots__ = ('parent', 'entity_values', 'language_code')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_VALUES_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entity_values: _containers.RepeatedScalarFieldContainer[str]
    language_code: str

    def __init__(self, parent: _Optional[str]=..., entity_values: _Optional[_Iterable[str]]=..., language_code: _Optional[str]=...) -> None:
        ...

class EntityTypeBatch(_message.Message):
    __slots__ = ('entity_types',)
    ENTITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    entity_types: _containers.RepeatedCompositeFieldContainer[EntityType]

    def __init__(self, entity_types: _Optional[_Iterable[_Union[EntityType, _Mapping]]]=...) -> None:
        ...