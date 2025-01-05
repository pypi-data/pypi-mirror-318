from google.api import resource_pb2 as _resource_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DocumentQuery(_message.Message):
    __slots__ = ('query', 'is_nl_query', 'custom_property_filter', 'time_filters', 'document_schema_names', 'property_filter', 'file_type_filter', 'folder_name_filter', 'document_name_filter', 'query_context', 'document_creator_filter', 'custom_weights_metadata')
    QUERY_FIELD_NUMBER: _ClassVar[int]
    IS_NL_QUERY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_PROPERTY_FILTER_FIELD_NUMBER: _ClassVar[int]
    TIME_FILTERS_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_SCHEMA_NAMES_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_FILTER_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FILTER_FIELD_NUMBER: _ClassVar[int]
    FOLDER_NAME_FILTER_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_NAME_FILTER_FIELD_NUMBER: _ClassVar[int]
    QUERY_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_CREATOR_FILTER_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_WEIGHTS_METADATA_FIELD_NUMBER: _ClassVar[int]
    query: str
    is_nl_query: bool
    custom_property_filter: str
    time_filters: _containers.RepeatedCompositeFieldContainer[TimeFilter]
    document_schema_names: _containers.RepeatedScalarFieldContainer[str]
    property_filter: _containers.RepeatedCompositeFieldContainer[PropertyFilter]
    file_type_filter: FileTypeFilter
    folder_name_filter: str
    document_name_filter: _containers.RepeatedScalarFieldContainer[str]
    query_context: _containers.RepeatedScalarFieldContainer[str]
    document_creator_filter: _containers.RepeatedScalarFieldContainer[str]
    custom_weights_metadata: CustomWeightsMetadata

    def __init__(self, query: _Optional[str]=..., is_nl_query: bool=..., custom_property_filter: _Optional[str]=..., time_filters: _Optional[_Iterable[_Union[TimeFilter, _Mapping]]]=..., document_schema_names: _Optional[_Iterable[str]]=..., property_filter: _Optional[_Iterable[_Union[PropertyFilter, _Mapping]]]=..., file_type_filter: _Optional[_Union[FileTypeFilter, _Mapping]]=..., folder_name_filter: _Optional[str]=..., document_name_filter: _Optional[_Iterable[str]]=..., query_context: _Optional[_Iterable[str]]=..., document_creator_filter: _Optional[_Iterable[str]]=..., custom_weights_metadata: _Optional[_Union[CustomWeightsMetadata, _Mapping]]=...) -> None:
        ...

class TimeFilter(_message.Message):
    __slots__ = ('time_range', 'time_field')

    class TimeField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIME_FIELD_UNSPECIFIED: _ClassVar[TimeFilter.TimeField]
        CREATE_TIME: _ClassVar[TimeFilter.TimeField]
        UPDATE_TIME: _ClassVar[TimeFilter.TimeField]
        DISPOSITION_TIME: _ClassVar[TimeFilter.TimeField]
    TIME_FIELD_UNSPECIFIED: TimeFilter.TimeField
    CREATE_TIME: TimeFilter.TimeField
    UPDATE_TIME: TimeFilter.TimeField
    DISPOSITION_TIME: TimeFilter.TimeField
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_FIELD_NUMBER: _ClassVar[int]
    time_range: _interval_pb2.Interval
    time_field: TimeFilter.TimeField

    def __init__(self, time_range: _Optional[_Union[_interval_pb2.Interval, _Mapping]]=..., time_field: _Optional[_Union[TimeFilter.TimeField, str]]=...) -> None:
        ...

class PropertyFilter(_message.Message):
    __slots__ = ('document_schema_name', 'condition')
    DOCUMENT_SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    document_schema_name: str
    condition: str

    def __init__(self, document_schema_name: _Optional[str]=..., condition: _Optional[str]=...) -> None:
        ...

class FileTypeFilter(_message.Message):
    __slots__ = ('file_type',)

    class FileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FILE_TYPE_UNSPECIFIED: _ClassVar[FileTypeFilter.FileType]
        ALL: _ClassVar[FileTypeFilter.FileType]
        FOLDER: _ClassVar[FileTypeFilter.FileType]
        DOCUMENT: _ClassVar[FileTypeFilter.FileType]
        ROOT_FOLDER: _ClassVar[FileTypeFilter.FileType]
    FILE_TYPE_UNSPECIFIED: FileTypeFilter.FileType
    ALL: FileTypeFilter.FileType
    FOLDER: FileTypeFilter.FileType
    DOCUMENT: FileTypeFilter.FileType
    ROOT_FOLDER: FileTypeFilter.FileType
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    file_type: FileTypeFilter.FileType

    def __init__(self, file_type: _Optional[_Union[FileTypeFilter.FileType, str]]=...) -> None:
        ...

class CustomWeightsMetadata(_message.Message):
    __slots__ = ('weighted_schema_properties',)
    WEIGHTED_SCHEMA_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    weighted_schema_properties: _containers.RepeatedCompositeFieldContainer[WeightedSchemaProperty]

    def __init__(self, weighted_schema_properties: _Optional[_Iterable[_Union[WeightedSchemaProperty, _Mapping]]]=...) -> None:
        ...

class WeightedSchemaProperty(_message.Message):
    __slots__ = ('document_schema_name', 'property_names')
    DOCUMENT_SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_NAMES_FIELD_NUMBER: _ClassVar[int]
    document_schema_name: str
    property_names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, document_schema_name: _Optional[str]=..., property_names: _Optional[_Iterable[str]]=...) -> None:
        ...