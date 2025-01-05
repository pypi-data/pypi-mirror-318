from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Schema(_message.Message):
    __slots__ = ('struct_schema', 'json_schema', 'name', 'field_configs')
    STRUCT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    JSON_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    struct_schema: _struct_pb2.Struct
    json_schema: str
    name: str
    field_configs: _containers.RepeatedCompositeFieldContainer[FieldConfig]

    def __init__(self, struct_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., json_schema: _Optional[str]=..., name: _Optional[str]=..., field_configs: _Optional[_Iterable[_Union[FieldConfig, _Mapping]]]=...) -> None:
        ...

class FieldConfig(_message.Message):
    __slots__ = ('field_path', 'field_type', 'indexable_option', 'dynamic_facetable_option', 'searchable_option', 'retrievable_option', 'completable_option', 'recs_filterable_option', 'key_property_type', 'advanced_site_search_data_sources', 'schema_org_paths')

    class FieldType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FIELD_TYPE_UNSPECIFIED: _ClassVar[FieldConfig.FieldType]
        OBJECT: _ClassVar[FieldConfig.FieldType]
        STRING: _ClassVar[FieldConfig.FieldType]
        NUMBER: _ClassVar[FieldConfig.FieldType]
        INTEGER: _ClassVar[FieldConfig.FieldType]
        BOOLEAN: _ClassVar[FieldConfig.FieldType]
        GEOLOCATION: _ClassVar[FieldConfig.FieldType]
        DATETIME: _ClassVar[FieldConfig.FieldType]
    FIELD_TYPE_UNSPECIFIED: FieldConfig.FieldType
    OBJECT: FieldConfig.FieldType
    STRING: FieldConfig.FieldType
    NUMBER: FieldConfig.FieldType
    INTEGER: FieldConfig.FieldType
    BOOLEAN: FieldConfig.FieldType
    GEOLOCATION: FieldConfig.FieldType
    DATETIME: FieldConfig.FieldType

    class IndexableOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INDEXABLE_OPTION_UNSPECIFIED: _ClassVar[FieldConfig.IndexableOption]
        INDEXABLE_ENABLED: _ClassVar[FieldConfig.IndexableOption]
        INDEXABLE_DISABLED: _ClassVar[FieldConfig.IndexableOption]
    INDEXABLE_OPTION_UNSPECIFIED: FieldConfig.IndexableOption
    INDEXABLE_ENABLED: FieldConfig.IndexableOption
    INDEXABLE_DISABLED: FieldConfig.IndexableOption

    class DynamicFacetableOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DYNAMIC_FACETABLE_OPTION_UNSPECIFIED: _ClassVar[FieldConfig.DynamicFacetableOption]
        DYNAMIC_FACETABLE_ENABLED: _ClassVar[FieldConfig.DynamicFacetableOption]
        DYNAMIC_FACETABLE_DISABLED: _ClassVar[FieldConfig.DynamicFacetableOption]
    DYNAMIC_FACETABLE_OPTION_UNSPECIFIED: FieldConfig.DynamicFacetableOption
    DYNAMIC_FACETABLE_ENABLED: FieldConfig.DynamicFacetableOption
    DYNAMIC_FACETABLE_DISABLED: FieldConfig.DynamicFacetableOption

    class SearchableOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEARCHABLE_OPTION_UNSPECIFIED: _ClassVar[FieldConfig.SearchableOption]
        SEARCHABLE_ENABLED: _ClassVar[FieldConfig.SearchableOption]
        SEARCHABLE_DISABLED: _ClassVar[FieldConfig.SearchableOption]
    SEARCHABLE_OPTION_UNSPECIFIED: FieldConfig.SearchableOption
    SEARCHABLE_ENABLED: FieldConfig.SearchableOption
    SEARCHABLE_DISABLED: FieldConfig.SearchableOption

    class RetrievableOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RETRIEVABLE_OPTION_UNSPECIFIED: _ClassVar[FieldConfig.RetrievableOption]
        RETRIEVABLE_ENABLED: _ClassVar[FieldConfig.RetrievableOption]
        RETRIEVABLE_DISABLED: _ClassVar[FieldConfig.RetrievableOption]
    RETRIEVABLE_OPTION_UNSPECIFIED: FieldConfig.RetrievableOption
    RETRIEVABLE_ENABLED: FieldConfig.RetrievableOption
    RETRIEVABLE_DISABLED: FieldConfig.RetrievableOption

    class CompletableOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPLETABLE_OPTION_UNSPECIFIED: _ClassVar[FieldConfig.CompletableOption]
        COMPLETABLE_ENABLED: _ClassVar[FieldConfig.CompletableOption]
        COMPLETABLE_DISABLED: _ClassVar[FieldConfig.CompletableOption]
    COMPLETABLE_OPTION_UNSPECIFIED: FieldConfig.CompletableOption
    COMPLETABLE_ENABLED: FieldConfig.CompletableOption
    COMPLETABLE_DISABLED: FieldConfig.CompletableOption

    class FilterableOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FILTERABLE_OPTION_UNSPECIFIED: _ClassVar[FieldConfig.FilterableOption]
        FILTERABLE_ENABLED: _ClassVar[FieldConfig.FilterableOption]
        FILTERABLE_DISABLED: _ClassVar[FieldConfig.FilterableOption]
    FILTERABLE_OPTION_UNSPECIFIED: FieldConfig.FilterableOption
    FILTERABLE_ENABLED: FieldConfig.FilterableOption
    FILTERABLE_DISABLED: FieldConfig.FilterableOption

    class AdvancedSiteSearchDataSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ADVANCED_SITE_SEARCH_DATA_SOURCE_UNSPECIFIED: _ClassVar[FieldConfig.AdvancedSiteSearchDataSource]
        METATAGS: _ClassVar[FieldConfig.AdvancedSiteSearchDataSource]
        PAGEMAP: _ClassVar[FieldConfig.AdvancedSiteSearchDataSource]
        URI_PATTERN_MAPPING: _ClassVar[FieldConfig.AdvancedSiteSearchDataSource]
        SCHEMA_ORG: _ClassVar[FieldConfig.AdvancedSiteSearchDataSource]
    ADVANCED_SITE_SEARCH_DATA_SOURCE_UNSPECIFIED: FieldConfig.AdvancedSiteSearchDataSource
    METATAGS: FieldConfig.AdvancedSiteSearchDataSource
    PAGEMAP: FieldConfig.AdvancedSiteSearchDataSource
    URI_PATTERN_MAPPING: FieldConfig.AdvancedSiteSearchDataSource
    SCHEMA_ORG: FieldConfig.AdvancedSiteSearchDataSource
    FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    INDEXABLE_OPTION_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_FACETABLE_OPTION_FIELD_NUMBER: _ClassVar[int]
    SEARCHABLE_OPTION_FIELD_NUMBER: _ClassVar[int]
    RETRIEVABLE_OPTION_FIELD_NUMBER: _ClassVar[int]
    COMPLETABLE_OPTION_FIELD_NUMBER: _ClassVar[int]
    RECS_FILTERABLE_OPTION_FIELD_NUMBER: _ClassVar[int]
    KEY_PROPERTY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_SITE_SEARCH_DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_ORG_PATHS_FIELD_NUMBER: _ClassVar[int]
    field_path: str
    field_type: FieldConfig.FieldType
    indexable_option: FieldConfig.IndexableOption
    dynamic_facetable_option: FieldConfig.DynamicFacetableOption
    searchable_option: FieldConfig.SearchableOption
    retrievable_option: FieldConfig.RetrievableOption
    completable_option: FieldConfig.CompletableOption
    recs_filterable_option: FieldConfig.FilterableOption
    key_property_type: str
    advanced_site_search_data_sources: _containers.RepeatedScalarFieldContainer[FieldConfig.AdvancedSiteSearchDataSource]
    schema_org_paths: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, field_path: _Optional[str]=..., field_type: _Optional[_Union[FieldConfig.FieldType, str]]=..., indexable_option: _Optional[_Union[FieldConfig.IndexableOption, str]]=..., dynamic_facetable_option: _Optional[_Union[FieldConfig.DynamicFacetableOption, str]]=..., searchable_option: _Optional[_Union[FieldConfig.SearchableOption, str]]=..., retrievable_option: _Optional[_Union[FieldConfig.RetrievableOption, str]]=..., completable_option: _Optional[_Union[FieldConfig.CompletableOption, str]]=..., recs_filterable_option: _Optional[_Union[FieldConfig.FilterableOption, str]]=..., key_property_type: _Optional[str]=..., advanced_site_search_data_sources: _Optional[_Iterable[_Union[FieldConfig.AdvancedSiteSearchDataSource, str]]]=..., schema_org_paths: _Optional[_Iterable[str]]=...) -> None:
        ...