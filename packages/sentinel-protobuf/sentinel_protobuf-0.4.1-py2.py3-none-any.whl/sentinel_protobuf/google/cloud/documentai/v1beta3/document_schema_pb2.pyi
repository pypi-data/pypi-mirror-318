from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SummaryOptions(_message.Message):
    __slots__ = ('length', 'format')

    class Length(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LENGTH_UNSPECIFIED: _ClassVar[SummaryOptions.Length]
        BRIEF: _ClassVar[SummaryOptions.Length]
        MODERATE: _ClassVar[SummaryOptions.Length]
        COMPREHENSIVE: _ClassVar[SummaryOptions.Length]
    LENGTH_UNSPECIFIED: SummaryOptions.Length
    BRIEF: SummaryOptions.Length
    MODERATE: SummaryOptions.Length
    COMPREHENSIVE: SummaryOptions.Length

    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FORMAT_UNSPECIFIED: _ClassVar[SummaryOptions.Format]
        PARAGRAPH: _ClassVar[SummaryOptions.Format]
        BULLETS: _ClassVar[SummaryOptions.Format]
    FORMAT_UNSPECIFIED: SummaryOptions.Format
    PARAGRAPH: SummaryOptions.Format
    BULLETS: SummaryOptions.Format
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    length: SummaryOptions.Length
    format: SummaryOptions.Format

    def __init__(self, length: _Optional[_Union[SummaryOptions.Length, str]]=..., format: _Optional[_Union[SummaryOptions.Format, str]]=...) -> None:
        ...

class FieldExtractionMetadata(_message.Message):
    __slots__ = ('summary_options',)
    SUMMARY_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    summary_options: SummaryOptions

    def __init__(self, summary_options: _Optional[_Union[SummaryOptions, _Mapping]]=...) -> None:
        ...

class PropertyMetadata(_message.Message):
    __slots__ = ('inactive', 'field_extraction_metadata')
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    FIELD_EXTRACTION_METADATA_FIELD_NUMBER: _ClassVar[int]
    inactive: bool
    field_extraction_metadata: FieldExtractionMetadata

    def __init__(self, inactive: bool=..., field_extraction_metadata: _Optional[_Union[FieldExtractionMetadata, _Mapping]]=...) -> None:
        ...

class EntityTypeMetadata(_message.Message):
    __slots__ = ('inactive',)
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    inactive: bool

    def __init__(self, inactive: bool=...) -> None:
        ...

class DocumentSchema(_message.Message):
    __slots__ = ('display_name', 'description', 'entity_types', 'metadata')

    class EntityType(_message.Message):
        __slots__ = ('enum_values', 'display_name', 'name', 'description', 'base_types', 'properties', 'entity_type_metadata')

        class EnumValues(_message.Message):
            __slots__ = ('values',)
            VALUES_FIELD_NUMBER: _ClassVar[int]
            values: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, values: _Optional[_Iterable[str]]=...) -> None:
                ...

        class Property(_message.Message):
            __slots__ = ('name', 'description', 'display_name', 'value_type', 'occurrence_type', 'property_metadata')

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
            DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
            OCCURRENCE_TYPE_FIELD_NUMBER: _ClassVar[int]
            PROPERTY_METADATA_FIELD_NUMBER: _ClassVar[int]
            name: str
            description: str
            display_name: str
            value_type: str
            occurrence_type: DocumentSchema.EntityType.Property.OccurrenceType
            property_metadata: PropertyMetadata

            def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., display_name: _Optional[str]=..., value_type: _Optional[str]=..., occurrence_type: _Optional[_Union[DocumentSchema.EntityType.Property.OccurrenceType, str]]=..., property_metadata: _Optional[_Union[PropertyMetadata, _Mapping]]=...) -> None:
                ...
        ENUM_VALUES_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        BASE_TYPES_FIELD_NUMBER: _ClassVar[int]
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        ENTITY_TYPE_METADATA_FIELD_NUMBER: _ClassVar[int]
        enum_values: DocumentSchema.EntityType.EnumValues
        display_name: str
        name: str
        description: str
        base_types: _containers.RepeatedScalarFieldContainer[str]
        properties: _containers.RepeatedCompositeFieldContainer[DocumentSchema.EntityType.Property]
        entity_type_metadata: EntityTypeMetadata

        def __init__(self, enum_values: _Optional[_Union[DocumentSchema.EntityType.EnumValues, _Mapping]]=..., display_name: _Optional[str]=..., name: _Optional[str]=..., description: _Optional[str]=..., base_types: _Optional[_Iterable[str]]=..., properties: _Optional[_Iterable[_Union[DocumentSchema.EntityType.Property, _Mapping]]]=..., entity_type_metadata: _Optional[_Union[EntityTypeMetadata, _Mapping]]=...) -> None:
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