from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.cx.v3 import inline_pb2 as _inline_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EntityType(_message.Message):
    __slots__ = ('name', 'display_name', 'kind', 'auto_expansion_mode', 'entities', 'excluded_phrases', 'enable_fuzzy_extraction', 'redact')

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

    class ExcludedPhrase(_message.Message):
        __slots__ = ('value',)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str

        def __init__(self, value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    AUTO_EXPANSION_MODE_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_PHRASES_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FUZZY_EXTRACTION_FIELD_NUMBER: _ClassVar[int]
    REDACT_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    kind: EntityType.Kind
    auto_expansion_mode: EntityType.AutoExpansionMode
    entities: _containers.RepeatedCompositeFieldContainer[EntityType.Entity]
    excluded_phrases: _containers.RepeatedCompositeFieldContainer[EntityType.ExcludedPhrase]
    enable_fuzzy_extraction: bool
    redact: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., kind: _Optional[_Union[EntityType.Kind, str]]=..., auto_expansion_mode: _Optional[_Union[EntityType.AutoExpansionMode, str]]=..., entities: _Optional[_Iterable[_Union[EntityType.Entity, _Mapping]]]=..., excluded_phrases: _Optional[_Iterable[_Union[EntityType.ExcludedPhrase, _Mapping]]]=..., enable_fuzzy_extraction: bool=..., redact: bool=...) -> None:
        ...

class ExportEntityTypesRequest(_message.Message):
    __slots__ = ('parent', 'entity_types', 'entity_types_uri', 'entity_types_content_inline', 'data_format', 'language_code')

    class DataFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_FORMAT_UNSPECIFIED: _ClassVar[ExportEntityTypesRequest.DataFormat]
        BLOB: _ClassVar[ExportEntityTypesRequest.DataFormat]
        JSON_PACKAGE: _ClassVar[ExportEntityTypesRequest.DataFormat]
    DATA_FORMAT_UNSPECIFIED: ExportEntityTypesRequest.DataFormat
    BLOB: ExportEntityTypesRequest.DataFormat
    JSON_PACKAGE: ExportEntityTypesRequest.DataFormat
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPES_URI_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPES_CONTENT_INLINE_FIELD_NUMBER: _ClassVar[int]
    DATA_FORMAT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entity_types: _containers.RepeatedScalarFieldContainer[str]
    entity_types_uri: str
    entity_types_content_inline: bool
    data_format: ExportEntityTypesRequest.DataFormat
    language_code: str

    def __init__(self, parent: _Optional[str]=..., entity_types: _Optional[_Iterable[str]]=..., entity_types_uri: _Optional[str]=..., entity_types_content_inline: bool=..., data_format: _Optional[_Union[ExportEntityTypesRequest.DataFormat, str]]=..., language_code: _Optional[str]=...) -> None:
        ...

class ExportEntityTypesResponse(_message.Message):
    __slots__ = ('entity_types_uri', 'entity_types_content')
    ENTITY_TYPES_URI_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPES_CONTENT_FIELD_NUMBER: _ClassVar[int]
    entity_types_uri: str
    entity_types_content: _inline_pb2.InlineDestination

    def __init__(self, entity_types_uri: _Optional[str]=..., entity_types_content: _Optional[_Union[_inline_pb2.InlineDestination, _Mapping]]=...) -> None:
        ...

class ExportEntityTypesMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ImportEntityTypesRequest(_message.Message):
    __slots__ = ('parent', 'entity_types_uri', 'entity_types_content', 'merge_option', 'target_entity_type')

    class MergeOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MERGE_OPTION_UNSPECIFIED: _ClassVar[ImportEntityTypesRequest.MergeOption]
        REPLACE: _ClassVar[ImportEntityTypesRequest.MergeOption]
        MERGE: _ClassVar[ImportEntityTypesRequest.MergeOption]
        RENAME: _ClassVar[ImportEntityTypesRequest.MergeOption]
        REPORT_CONFLICT: _ClassVar[ImportEntityTypesRequest.MergeOption]
        KEEP: _ClassVar[ImportEntityTypesRequest.MergeOption]
    MERGE_OPTION_UNSPECIFIED: ImportEntityTypesRequest.MergeOption
    REPLACE: ImportEntityTypesRequest.MergeOption
    MERGE: ImportEntityTypesRequest.MergeOption
    RENAME: ImportEntityTypesRequest.MergeOption
    REPORT_CONFLICT: ImportEntityTypesRequest.MergeOption
    KEEP: ImportEntityTypesRequest.MergeOption
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPES_URI_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPES_CONTENT_FIELD_NUMBER: _ClassVar[int]
    MERGE_OPTION_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entity_types_uri: str
    entity_types_content: _inline_pb2.InlineSource
    merge_option: ImportEntityTypesRequest.MergeOption
    target_entity_type: str

    def __init__(self, parent: _Optional[str]=..., entity_types_uri: _Optional[str]=..., entity_types_content: _Optional[_Union[_inline_pb2.InlineSource, _Mapping]]=..., merge_option: _Optional[_Union[ImportEntityTypesRequest.MergeOption, str]]=..., target_entity_type: _Optional[str]=...) -> None:
        ...

class ImportEntityTypesResponse(_message.Message):
    __slots__ = ('entity_types', 'conflicting_resources')

    class ConflictingResources(_message.Message):
        __slots__ = ('entity_type_display_names', 'entity_display_names')
        ENTITY_TYPE_DISPLAY_NAMES_FIELD_NUMBER: _ClassVar[int]
        ENTITY_DISPLAY_NAMES_FIELD_NUMBER: _ClassVar[int]
        entity_type_display_names: _containers.RepeatedScalarFieldContainer[str]
        entity_display_names: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, entity_type_display_names: _Optional[_Iterable[str]]=..., entity_display_names: _Optional[_Iterable[str]]=...) -> None:
            ...
    ENTITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    CONFLICTING_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    entity_types: _containers.RepeatedScalarFieldContainer[str]
    conflicting_resources: ImportEntityTypesResponse.ConflictingResources

    def __init__(self, entity_types: _Optional[_Iterable[str]]=..., conflicting_resources: _Optional[_Union[ImportEntityTypesResponse.ConflictingResources, _Mapping]]=...) -> None:
        ...

class ImportEntityTypesMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
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
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...