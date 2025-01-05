from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DocumentSchema(_message.Message):
    __slots__ = ('display_name', 'description', 'entity_types', 'metadata')

    class EntityType(_message.Message):
        __slots__ = ('enum_values', 'display_name', 'name', 'base_types', 'properties')

        class EnumValues(_message.Message):
            __slots__ = ('values',)
            VALUES_FIELD_NUMBER: _ClassVar[int]
            values: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, values: _Optional[_Iterable[str]]=...) -> None:
                ...

        class Property(_message.Message):
            __slots__ = ('name', 'display_name', 'value_type', 'occurrence_type')

            class OccurrenceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                OCCURRENCE_TYPE_UNSPECIFIED: _ClassVar[DocumentSchema.EntityType.Property.OccurrenceType]
                OPTIONAL_ONCE: _ClassVar[DocumentSchema.EntityType.Property.OccurrenceType]
                OPTIONAL_MULTIPLE: _ClassVar[DocumentSchema.EntityType.Property.OccurrenceType]
                REQUIRED_ONCE: _ClassVar[DocumentSchema.EntityType.Property.OccurrenceType]
                REQUIRED_MULTIPLE: _ClassVar[DocumentSchema.EntityType.Property.OccurrenceType]
            OCCURRENCE_TYPE_UNSPECIFIED: DocumentSchema.EntityType.Property.OccurrenceType
            OPTIONAL_ONCE: DocumentSchema.EntityType.Property.OccurrenceType
            OPTIONAL_MULTIPLE: DocumentSchema.EntityType.Property.OccurrenceType
            REQUIRED_ONCE: DocumentSchema.EntityType.Property.OccurrenceType
            REQUIRED_MULTIPLE: DocumentSchema.EntityType.Property.OccurrenceType
            NAME_FIELD_NUMBER: _ClassVar[int]
            DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
            OCCURRENCE_TYPE_FIELD_NUMBER: _ClassVar[int]
            name: str
            display_name: str
            value_type: str
            occurrence_type: DocumentSchema.EntityType.Property.OccurrenceType

            def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., value_type: _Optional[str]=..., occurrence_type: _Optional[_Union[DocumentSchema.EntityType.Property.OccurrenceType, str]]=...) -> None:
                ...
        ENUM_VALUES_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        BASE_TYPES_FIELD_NUMBER: _ClassVar[int]
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        enum_values: DocumentSchema.EntityType.EnumValues
        display_name: str
        name: str
        base_types: _containers.RepeatedScalarFieldContainer[str]
        properties: _containers.RepeatedCompositeFieldContainer[DocumentSchema.EntityType.Property]

        def __init__(self, enum_values: _Optional[_Union[DocumentSchema.EntityType.EnumValues, _Mapping]]=..., display_name: _Optional[str]=..., name: _Optional[str]=..., base_types: _Optional[_Iterable[str]]=..., properties: _Optional[_Iterable[_Union[DocumentSchema.EntityType.Property, _Mapping]]]=...) -> None:
            ...

    class Metadata(_message.Message):
        __slots__ = ('document_splitter', 'document_allow_multiple_labels', 'prefixed_naming_on_properties', 'skip_naming_validation')
        DOCUMENT_SPLITTER_FIELD_NUMBER: _ClassVar[int]
        DOCUMENT_ALLOW_MULTIPLE_LABELS_FIELD_NUMBER: _ClassVar[int]
        PREFIXED_NAMING_ON_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        SKIP_NAMING_VALIDATION_FIELD_NUMBER: _ClassVar[int]
        document_splitter: bool
        document_allow_multiple_labels: bool
        prefixed_naming_on_properties: bool
        skip_naming_validation: bool

        def __init__(self, document_splitter: bool=..., document_allow_multiple_labels: bool=..., prefixed_naming_on_properties: bool=..., skip_naming_validation: bool=...) -> None:
            ...
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    description: str
    entity_types: _containers.RepeatedCompositeFieldContainer[DocumentSchema.EntityType]
    metadata: DocumentSchema.Metadata

    def __init__(self, display_name: _Optional[str]=..., description: _Optional[str]=..., entity_types: _Optional[_Iterable[_Union[DocumentSchema.EntityType, _Mapping]]]=..., metadata: _Optional[_Union[DocumentSchema.Metadata, _Mapping]]=...) -> None:
        ...