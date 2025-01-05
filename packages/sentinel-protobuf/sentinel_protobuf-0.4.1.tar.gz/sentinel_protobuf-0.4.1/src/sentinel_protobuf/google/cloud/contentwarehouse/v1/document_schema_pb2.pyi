from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DocumentSchema(_message.Message):
    __slots__ = ('name', 'display_name', 'property_definitions', 'document_is_folder', 'update_time', 'create_time', 'description')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_IS_FOLDER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    property_definitions: _containers.RepeatedCompositeFieldContainer[PropertyDefinition]
    document_is_folder: bool
    update_time: _timestamp_pb2.Timestamp
    create_time: _timestamp_pb2.Timestamp
    description: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., property_definitions: _Optional[_Iterable[_Union[PropertyDefinition, _Mapping]]]=..., document_is_folder: bool=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=...) -> None:
        ...

class PropertyDefinition(_message.Message):
    __slots__ = ('name', 'display_name', 'is_repeatable', 'is_filterable', 'is_searchable', 'is_metadata', 'is_required', 'retrieval_importance', 'integer_type_options', 'float_type_options', 'text_type_options', 'property_type_options', 'enum_type_options', 'date_time_type_options', 'map_type_options', 'timestamp_type_options', 'schema_sources')

    class RetrievalImportance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RETRIEVAL_IMPORTANCE_UNSPECIFIED: _ClassVar[PropertyDefinition.RetrievalImportance]
        HIGHEST: _ClassVar[PropertyDefinition.RetrievalImportance]
        HIGHER: _ClassVar[PropertyDefinition.RetrievalImportance]
        HIGH: _ClassVar[PropertyDefinition.RetrievalImportance]
        MEDIUM: _ClassVar[PropertyDefinition.RetrievalImportance]
        LOW: _ClassVar[PropertyDefinition.RetrievalImportance]
        LOWEST: _ClassVar[PropertyDefinition.RetrievalImportance]
    RETRIEVAL_IMPORTANCE_UNSPECIFIED: PropertyDefinition.RetrievalImportance
    HIGHEST: PropertyDefinition.RetrievalImportance
    HIGHER: PropertyDefinition.RetrievalImportance
    HIGH: PropertyDefinition.RetrievalImportance
    MEDIUM: PropertyDefinition.RetrievalImportance
    LOW: PropertyDefinition.RetrievalImportance
    LOWEST: PropertyDefinition.RetrievalImportance

    class SchemaSource(_message.Message):
        __slots__ = ('name', 'processor_type')
        NAME_FIELD_NUMBER: _ClassVar[int]
        PROCESSOR_TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        processor_type: str

        def __init__(self, name: _Optional[str]=..., processor_type: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_REPEATABLE_FIELD_NUMBER: _ClassVar[int]
    IS_FILTERABLE_FIELD_NUMBER: _ClassVar[int]
    IS_SEARCHABLE_FIELD_NUMBER: _ClassVar[int]
    IS_METADATA_FIELD_NUMBER: _ClassVar[int]
    IS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    RETRIEVAL_IMPORTANCE_FIELD_NUMBER: _ClassVar[int]
    INTEGER_TYPE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    FLOAT_TYPE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TEXT_TYPE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_TYPE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ENUM_TYPE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DATE_TIME_TYPE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    MAP_TYPE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_TYPE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    is_repeatable: bool
    is_filterable: bool
    is_searchable: bool
    is_metadata: bool
    is_required: bool
    retrieval_importance: PropertyDefinition.RetrievalImportance
    integer_type_options: IntegerTypeOptions
    float_type_options: FloatTypeOptions
    text_type_options: TextTypeOptions
    property_type_options: PropertyTypeOptions
    enum_type_options: EnumTypeOptions
    date_time_type_options: DateTimeTypeOptions
    map_type_options: MapTypeOptions
    timestamp_type_options: TimestampTypeOptions
    schema_sources: _containers.RepeatedCompositeFieldContainer[PropertyDefinition.SchemaSource]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., is_repeatable: bool=..., is_filterable: bool=..., is_searchable: bool=..., is_metadata: bool=..., is_required: bool=..., retrieval_importance: _Optional[_Union[PropertyDefinition.RetrievalImportance, str]]=..., integer_type_options: _Optional[_Union[IntegerTypeOptions, _Mapping]]=..., float_type_options: _Optional[_Union[FloatTypeOptions, _Mapping]]=..., text_type_options: _Optional[_Union[TextTypeOptions, _Mapping]]=..., property_type_options: _Optional[_Union[PropertyTypeOptions, _Mapping]]=..., enum_type_options: _Optional[_Union[EnumTypeOptions, _Mapping]]=..., date_time_type_options: _Optional[_Union[DateTimeTypeOptions, _Mapping]]=..., map_type_options: _Optional[_Union[MapTypeOptions, _Mapping]]=..., timestamp_type_options: _Optional[_Union[TimestampTypeOptions, _Mapping]]=..., schema_sources: _Optional[_Iterable[_Union[PropertyDefinition.SchemaSource, _Mapping]]]=...) -> None:
        ...

class IntegerTypeOptions(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class FloatTypeOptions(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TextTypeOptions(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DateTimeTypeOptions(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MapTypeOptions(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TimestampTypeOptions(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PropertyTypeOptions(_message.Message):
    __slots__ = ('property_definitions',)
    PROPERTY_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    property_definitions: _containers.RepeatedCompositeFieldContainer[PropertyDefinition]

    def __init__(self, property_definitions: _Optional[_Iterable[_Union[PropertyDefinition, _Mapping]]]=...) -> None:
        ...

class EnumTypeOptions(_message.Message):
    __slots__ = ('possible_values', 'validation_check_disabled')
    POSSIBLE_VALUES_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_CHECK_DISABLED_FIELD_NUMBER: _ClassVar[int]
    possible_values: _containers.RepeatedScalarFieldContainer[str]
    validation_check_disabled: bool

    def __init__(self, possible_values: _Optional[_Iterable[str]]=..., validation_check_disabled: bool=...) -> None:
        ...