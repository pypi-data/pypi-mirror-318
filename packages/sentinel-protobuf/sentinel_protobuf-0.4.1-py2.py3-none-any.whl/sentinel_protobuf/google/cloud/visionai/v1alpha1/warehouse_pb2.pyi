from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.type import datetime_pb2 as _datetime_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FacetBucketType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FACET_BUCKET_TYPE_UNSPECIFIED: _ClassVar[FacetBucketType]
    FACET_BUCKET_TYPE_VALUE: _ClassVar[FacetBucketType]
    FACET_BUCKET_TYPE_DATETIME: _ClassVar[FacetBucketType]
    FACET_BUCKET_TYPE_FIXED_RANGE: _ClassVar[FacetBucketType]
    FACET_BUCKET_TYPE_CUSTOM_RANGE: _ClassVar[FacetBucketType]
FACET_BUCKET_TYPE_UNSPECIFIED: FacetBucketType
FACET_BUCKET_TYPE_VALUE: FacetBucketType
FACET_BUCKET_TYPE_DATETIME: FacetBucketType
FACET_BUCKET_TYPE_FIXED_RANGE: FacetBucketType
FACET_BUCKET_TYPE_CUSTOM_RANGE: FacetBucketType

class CreateAssetRequest(_message.Message):
    __slots__ = ("parent", "asset", "asset_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    asset: Asset
    asset_id: str
    def __init__(self, parent: _Optional[str] = ..., asset: _Optional[_Union[Asset, _Mapping]] = ..., asset_id: _Optional[str] = ...) -> None: ...

class GetAssetRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAssetsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAssetsResponse(_message.Message):
    __slots__ = ("assets", "next_page_token")
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    assets: _containers.RepeatedCompositeFieldContainer[Asset]
    next_page_token: str
    def __init__(self, assets: _Optional[_Iterable[_Union[Asset, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateAssetRequest(_message.Message):
    __slots__ = ("asset", "update_mask")
    ASSET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    asset: Asset
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, asset: _Optional[_Union[Asset, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteAssetRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class Asset(_message.Message):
    __slots__ = ("name", "ttl")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    name: str
    ttl: _duration_pb2.Duration
    def __init__(self, name: _Optional[str] = ..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class CreateCorpusRequest(_message.Message):
    __slots__ = ("parent", "corpus")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CORPUS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    corpus: Corpus
    def __init__(self, parent: _Optional[str] = ..., corpus: _Optional[_Union[Corpus, _Mapping]] = ...) -> None: ...

class CreateCorpusMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Corpus(_message.Message):
    __slots__ = ("name", "display_name", "description", "default_ttl")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TTL_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    default_ttl: _duration_pb2.Duration
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., default_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class GetCorpusRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateCorpusRequest(_message.Message):
    __slots__ = ("corpus", "update_mask")
    CORPUS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    corpus: Corpus
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, corpus: _Optional[_Union[Corpus, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListCorporaRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListCorporaResponse(_message.Message):
    __slots__ = ("corpora", "next_page_token")
    CORPORA_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    corpora: _containers.RepeatedCompositeFieldContainer[Corpus]
    next_page_token: str
    def __init__(self, corpora: _Optional[_Iterable[_Union[Corpus, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteCorpusRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateDataSchemaRequest(_message.Message):
    __slots__ = ("parent", "data_schema")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATA_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    parent: str
    data_schema: DataSchema
    def __init__(self, parent: _Optional[str] = ..., data_schema: _Optional[_Union[DataSchema, _Mapping]] = ...) -> None: ...

class DataSchema(_message.Message):
    __slots__ = ("name", "key", "schema_details")
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_DETAILS_FIELD_NUMBER: _ClassVar[int]
    name: str
    key: str
    schema_details: DataSchemaDetails
    def __init__(self, name: _Optional[str] = ..., key: _Optional[str] = ..., schema_details: _Optional[_Union[DataSchemaDetails, _Mapping]] = ...) -> None: ...

class DataSchemaDetails(_message.Message):
    __slots__ = ("type", "proto_any_config", "granularity", "search_strategy")
    class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_TYPE_UNSPECIFIED: _ClassVar[DataSchemaDetails.DataType]
        INTEGER: _ClassVar[DataSchemaDetails.DataType]
        FLOAT: _ClassVar[DataSchemaDetails.DataType]
        STRING: _ClassVar[DataSchemaDetails.DataType]
        DATETIME: _ClassVar[DataSchemaDetails.DataType]
        GEO_COORDINATE: _ClassVar[DataSchemaDetails.DataType]
        PROTO_ANY: _ClassVar[DataSchemaDetails.DataType]
        BOOLEAN: _ClassVar[DataSchemaDetails.DataType]
    DATA_TYPE_UNSPECIFIED: DataSchemaDetails.DataType
    INTEGER: DataSchemaDetails.DataType
    FLOAT: DataSchemaDetails.DataType
    STRING: DataSchemaDetails.DataType
    DATETIME: DataSchemaDetails.DataType
    GEO_COORDINATE: DataSchemaDetails.DataType
    PROTO_ANY: DataSchemaDetails.DataType
    BOOLEAN: DataSchemaDetails.DataType
    class Granularity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GRANULARITY_UNSPECIFIED: _ClassVar[DataSchemaDetails.Granularity]
        GRANULARITY_ASSET_LEVEL: _ClassVar[DataSchemaDetails.Granularity]
        GRANULARITY_PARTITION_LEVEL: _ClassVar[DataSchemaDetails.Granularity]
    GRANULARITY_UNSPECIFIED: DataSchemaDetails.Granularity
    GRANULARITY_ASSET_LEVEL: DataSchemaDetails.Granularity
    GRANULARITY_PARTITION_LEVEL: DataSchemaDetails.Granularity
    class ProtoAnyConfig(_message.Message):
        __slots__ = ("type_uri",)
        TYPE_URI_FIELD_NUMBER: _ClassVar[int]
        type_uri: str
        def __init__(self, type_uri: _Optional[str] = ...) -> None: ...
    class SearchStrategy(_message.Message):
        __slots__ = ("search_strategy_type",)
        class SearchStrategyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_SEARCH: _ClassVar[DataSchemaDetails.SearchStrategy.SearchStrategyType]
            EXACT_SEARCH: _ClassVar[DataSchemaDetails.SearchStrategy.SearchStrategyType]
            SMART_SEARCH: _ClassVar[DataSchemaDetails.SearchStrategy.SearchStrategyType]
        NO_SEARCH: DataSchemaDetails.SearchStrategy.SearchStrategyType
        EXACT_SEARCH: DataSchemaDetails.SearchStrategy.SearchStrategyType
        SMART_SEARCH: DataSchemaDetails.SearchStrategy.SearchStrategyType
        SEARCH_STRATEGY_TYPE_FIELD_NUMBER: _ClassVar[int]
        search_strategy_type: DataSchemaDetails.SearchStrategy.SearchStrategyType
        def __init__(self, search_strategy_type: _Optional[_Union[DataSchemaDetails.SearchStrategy.SearchStrategyType, str]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROTO_ANY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    type: DataSchemaDetails.DataType
    proto_any_config: DataSchemaDetails.ProtoAnyConfig
    granularity: DataSchemaDetails.Granularity
    search_strategy: DataSchemaDetails.SearchStrategy
    def __init__(self, type: _Optional[_Union[DataSchemaDetails.DataType, str]] = ..., proto_any_config: _Optional[_Union[DataSchemaDetails.ProtoAnyConfig, _Mapping]] = ..., granularity: _Optional[_Union[DataSchemaDetails.Granularity, str]] = ..., search_strategy: _Optional[_Union[DataSchemaDetails.SearchStrategy, _Mapping]] = ...) -> None: ...

class UpdateDataSchemaRequest(_message.Message):
    __slots__ = ("data_schema", "update_mask")
    DATA_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    data_schema: DataSchema
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, data_schema: _Optional[_Union[DataSchema, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetDataSchemaRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteDataSchemaRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListDataSchemasRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListDataSchemasResponse(_message.Message):
    __slots__ = ("data_schemas", "next_page_token")
    DATA_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    data_schemas: _containers.RepeatedCompositeFieldContainer[DataSchema]
    next_page_token: str
    def __init__(self, data_schemas: _Optional[_Iterable[_Union[DataSchema, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateAnnotationRequest(_message.Message):
    __slots__ = ("parent", "annotation", "annotation_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    annotation: Annotation
    annotation_id: str
    def __init__(self, parent: _Optional[str] = ..., annotation: _Optional[_Union[Annotation, _Mapping]] = ..., annotation_id: _Optional[str] = ...) -> None: ...

class Annotation(_message.Message):
    __slots__ = ("name", "user_specified_annotation")
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_SPECIFIED_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    user_specified_annotation: UserSpecifiedAnnotation
    def __init__(self, name: _Optional[str] = ..., user_specified_annotation: _Optional[_Union[UserSpecifiedAnnotation, _Mapping]] = ...) -> None: ...

class UserSpecifiedAnnotation(_message.Message):
    __slots__ = ("key", "value", "partition")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: AnnotationValue
    partition: Partition
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AnnotationValue, _Mapping]] = ..., partition: _Optional[_Union[Partition, _Mapping]] = ...) -> None: ...

class GeoCoordinate(_message.Message):
    __slots__ = ("latitude", "longitude")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ...) -> None: ...

class AnnotationValue(_message.Message):
    __slots__ = ("int_value", "float_value", "str_value", "datetime_value", "geo_coordinate", "proto_any_value", "bool_value", "customized_struct_data_value")
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    STR_VALUE_FIELD_NUMBER: _ClassVar[int]
    DATETIME_VALUE_FIELD_NUMBER: _ClassVar[int]
    GEO_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    PROTO_ANY_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMIZED_STRUCT_DATA_VALUE_FIELD_NUMBER: _ClassVar[int]
    int_value: int
    float_value: float
    str_value: str
    datetime_value: str
    geo_coordinate: GeoCoordinate
    proto_any_value: _any_pb2.Any
    bool_value: bool
    customized_struct_data_value: _struct_pb2.Struct
    def __init__(self, int_value: _Optional[int] = ..., float_value: _Optional[float] = ..., str_value: _Optional[str] = ..., datetime_value: _Optional[str] = ..., geo_coordinate: _Optional[_Union[GeoCoordinate, _Mapping]] = ..., proto_any_value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., bool_value: bool = ..., customized_struct_data_value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ListAnnotationsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListAnnotationsResponse(_message.Message):
    __slots__ = ("annotations", "next_page_token")
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    annotations: _containers.RepeatedCompositeFieldContainer[Annotation]
    next_page_token: str
    def __init__(self, annotations: _Optional[_Iterable[_Union[Annotation, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetAnnotationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateAnnotationRequest(_message.Message):
    __slots__ = ("annotation", "update_mask")
    ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    annotation: Annotation
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, annotation: _Optional[_Union[Annotation, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteAnnotationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateSearchConfigRequest(_message.Message):
    __slots__ = ("parent", "search_config", "search_config_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SEARCH_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    search_config: SearchConfig
    search_config_id: str
    def __init__(self, parent: _Optional[str] = ..., search_config: _Optional[_Union[SearchConfig, _Mapping]] = ..., search_config_id: _Optional[str] = ...) -> None: ...

class UpdateSearchConfigRequest(_message.Message):
    __slots__ = ("search_config", "update_mask")
    SEARCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    search_config: SearchConfig
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, search_config: _Optional[_Union[SearchConfig, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetSearchConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteSearchConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListSearchConfigsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListSearchConfigsResponse(_message.Message):
    __slots__ = ("search_configs", "next_page_token")
    SEARCH_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    search_configs: _containers.RepeatedCompositeFieldContainer[SearchConfig]
    next_page_token: str
    def __init__(self, search_configs: _Optional[_Iterable[_Union[SearchConfig, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class SearchConfig(_message.Message):
    __slots__ = ("name", "facet_property", "search_criteria_property")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FACET_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_CRITERIA_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    name: str
    facet_property: FacetProperty
    search_criteria_property: SearchCriteriaProperty
    def __init__(self, name: _Optional[str] = ..., facet_property: _Optional[_Union[FacetProperty, _Mapping]] = ..., search_criteria_property: _Optional[_Union[SearchCriteriaProperty, _Mapping]] = ...) -> None: ...

class FacetProperty(_message.Message):
    __slots__ = ("fixed_range_bucket_spec", "custom_range_bucket_spec", "datetime_bucket_spec", "mapped_fields", "display_name", "result_size", "bucket_type")
    class FixedRangeBucketSpec(_message.Message):
        __slots__ = ("bucket_start", "bucket_granularity", "bucket_count")
        BUCKET_START_FIELD_NUMBER: _ClassVar[int]
        BUCKET_GRANULARITY_FIELD_NUMBER: _ClassVar[int]
        BUCKET_COUNT_FIELD_NUMBER: _ClassVar[int]
        bucket_start: FacetValue
        bucket_granularity: FacetValue
        bucket_count: int
        def __init__(self, bucket_start: _Optional[_Union[FacetValue, _Mapping]] = ..., bucket_granularity: _Optional[_Union[FacetValue, _Mapping]] = ..., bucket_count: _Optional[int] = ...) -> None: ...
    class CustomRangeBucketSpec(_message.Message):
        __slots__ = ("endpoints",)
        ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
        endpoints: _containers.RepeatedCompositeFieldContainer[FacetValue]
        def __init__(self, endpoints: _Optional[_Iterable[_Union[FacetValue, _Mapping]]] = ...) -> None: ...
    class DateTimeBucketSpec(_message.Message):
        __slots__ = ("granularity",)
        class Granularity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            GRANULARITY_UNSPECIFIED: _ClassVar[FacetProperty.DateTimeBucketSpec.Granularity]
            YEAR: _ClassVar[FacetProperty.DateTimeBucketSpec.Granularity]
            MONTH: _ClassVar[FacetProperty.DateTimeBucketSpec.Granularity]
            DAY: _ClassVar[FacetProperty.DateTimeBucketSpec.Granularity]
        GRANULARITY_UNSPECIFIED: FacetProperty.DateTimeBucketSpec.Granularity
        YEAR: FacetProperty.DateTimeBucketSpec.Granularity
        MONTH: FacetProperty.DateTimeBucketSpec.Granularity
        DAY: FacetProperty.DateTimeBucketSpec.Granularity
        GRANULARITY_FIELD_NUMBER: _ClassVar[int]
        granularity: FacetProperty.DateTimeBucketSpec.Granularity
        def __init__(self, granularity: _Optional[_Union[FacetProperty.DateTimeBucketSpec.Granularity, str]] = ...) -> None: ...
    FIXED_RANGE_BUCKET_SPEC_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_RANGE_BUCKET_SPEC_FIELD_NUMBER: _ClassVar[int]
    DATETIME_BUCKET_SPEC_FIELD_NUMBER: _ClassVar[int]
    MAPPED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    RESULT_SIZE_FIELD_NUMBER: _ClassVar[int]
    BUCKET_TYPE_FIELD_NUMBER: _ClassVar[int]
    fixed_range_bucket_spec: FacetProperty.FixedRangeBucketSpec
    custom_range_bucket_spec: FacetProperty.CustomRangeBucketSpec
    datetime_bucket_spec: FacetProperty.DateTimeBucketSpec
    mapped_fields: _containers.RepeatedScalarFieldContainer[str]
    display_name: str
    result_size: int
    bucket_type: FacetBucketType
    def __init__(self, fixed_range_bucket_spec: _Optional[_Union[FacetProperty.FixedRangeBucketSpec, _Mapping]] = ..., custom_range_bucket_spec: _Optional[_Union[FacetProperty.CustomRangeBucketSpec, _Mapping]] = ..., datetime_bucket_spec: _Optional[_Union[FacetProperty.DateTimeBucketSpec, _Mapping]] = ..., mapped_fields: _Optional[_Iterable[str]] = ..., display_name: _Optional[str] = ..., result_size: _Optional[int] = ..., bucket_type: _Optional[_Union[FacetBucketType, str]] = ...) -> None: ...

class SearchCriteriaProperty(_message.Message):
    __slots__ = ("mapped_fields",)
    MAPPED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    mapped_fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, mapped_fields: _Optional[_Iterable[str]] = ...) -> None: ...

class FacetValue(_message.Message):
    __slots__ = ("string_value", "integer_value", "datetime_value")
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    INTEGER_VALUE_FIELD_NUMBER: _ClassVar[int]
    DATETIME_VALUE_FIELD_NUMBER: _ClassVar[int]
    string_value: str
    integer_value: int
    datetime_value: _datetime_pb2.DateTime
    def __init__(self, string_value: _Optional[str] = ..., integer_value: _Optional[int] = ..., datetime_value: _Optional[_Union[_datetime_pb2.DateTime, _Mapping]] = ...) -> None: ...

class FacetBucket(_message.Message):
    __slots__ = ("value", "range", "selected")
    class Range(_message.Message):
        __slots__ = ("start", "end")
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        start: FacetValue
        end: FacetValue
        def __init__(self, start: _Optional[_Union[FacetValue, _Mapping]] = ..., end: _Optional[_Union[FacetValue, _Mapping]] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    SELECTED_FIELD_NUMBER: _ClassVar[int]
    value: FacetValue
    range: FacetBucket.Range
    selected: bool
    def __init__(self, value: _Optional[_Union[FacetValue, _Mapping]] = ..., range: _Optional[_Union[FacetBucket.Range, _Mapping]] = ..., selected: bool = ...) -> None: ...

class FacetGroup(_message.Message):
    __slots__ = ("facet_id", "display_name", "buckets", "bucket_type", "fetch_matched_annotations")
    FACET_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    BUCKET_TYPE_FIELD_NUMBER: _ClassVar[int]
    FETCH_MATCHED_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    facet_id: str
    display_name: str
    buckets: _containers.RepeatedCompositeFieldContainer[FacetBucket]
    bucket_type: FacetBucketType
    fetch_matched_annotations: bool
    def __init__(self, facet_id: _Optional[str] = ..., display_name: _Optional[str] = ..., buckets: _Optional[_Iterable[_Union[FacetBucket, _Mapping]]] = ..., bucket_type: _Optional[_Union[FacetBucketType, str]] = ..., fetch_matched_annotations: bool = ...) -> None: ...

class IngestAssetRequest(_message.Message):
    __slots__ = ("config", "time_indexed_data")
    class Config(_message.Message):
        __slots__ = ("video_type", "asset")
        class VideoType(_message.Message):
            __slots__ = ("container_format",)
            class ContainerFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                CONTAINER_FORMAT_UNSPECIFIED: _ClassVar[IngestAssetRequest.Config.VideoType.ContainerFormat]
                CONTAINER_FORMAT_MP4: _ClassVar[IngestAssetRequest.Config.VideoType.ContainerFormat]
            CONTAINER_FORMAT_UNSPECIFIED: IngestAssetRequest.Config.VideoType.ContainerFormat
            CONTAINER_FORMAT_MP4: IngestAssetRequest.Config.VideoType.ContainerFormat
            CONTAINER_FORMAT_FIELD_NUMBER: _ClassVar[int]
            container_format: IngestAssetRequest.Config.VideoType.ContainerFormat
            def __init__(self, container_format: _Optional[_Union[IngestAssetRequest.Config.VideoType.ContainerFormat, str]] = ...) -> None: ...
        VIDEO_TYPE_FIELD_NUMBER: _ClassVar[int]
        ASSET_FIELD_NUMBER: _ClassVar[int]
        video_type: IngestAssetRequest.Config.VideoType
        asset: str
        def __init__(self, video_type: _Optional[_Union[IngestAssetRequest.Config.VideoType, _Mapping]] = ..., asset: _Optional[str] = ...) -> None: ...
    class TimeIndexedData(_message.Message):
        __slots__ = ("data", "temporal_partition")
        DATA_FIELD_NUMBER: _ClassVar[int]
        TEMPORAL_PARTITION_FIELD_NUMBER: _ClassVar[int]
        data: bytes
        temporal_partition: Partition.TemporalPartition
        def __init__(self, data: _Optional[bytes] = ..., temporal_partition: _Optional[_Union[Partition.TemporalPartition, _Mapping]] = ...) -> None: ...
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    TIME_INDEXED_DATA_FIELD_NUMBER: _ClassVar[int]
    config: IngestAssetRequest.Config
    time_indexed_data: IngestAssetRequest.TimeIndexedData
    def __init__(self, config: _Optional[_Union[IngestAssetRequest.Config, _Mapping]] = ..., time_indexed_data: _Optional[_Union[IngestAssetRequest.TimeIndexedData, _Mapping]] = ...) -> None: ...

class IngestAssetResponse(_message.Message):
    __slots__ = ("successfully_ingested_partition",)
    SUCCESSFULLY_INGESTED_PARTITION_FIELD_NUMBER: _ClassVar[int]
    successfully_ingested_partition: Partition.TemporalPartition
    def __init__(self, successfully_ingested_partition: _Optional[_Union[Partition.TemporalPartition, _Mapping]] = ...) -> None: ...

class ClipAssetRequest(_message.Message):
    __slots__ = ("name", "temporal_partition")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPORAL_PARTITION_FIELD_NUMBER: _ClassVar[int]
    name: str
    temporal_partition: Partition.TemporalPartition
    def __init__(self, name: _Optional[str] = ..., temporal_partition: _Optional[_Union[Partition.TemporalPartition, _Mapping]] = ...) -> None: ...

class ClipAssetResponse(_message.Message):
    __slots__ = ("time_indexed_uris",)
    class TimeIndexedUri(_message.Message):
        __slots__ = ("temporal_partition", "uri")
        TEMPORAL_PARTITION_FIELD_NUMBER: _ClassVar[int]
        URI_FIELD_NUMBER: _ClassVar[int]
        temporal_partition: Partition.TemporalPartition
        uri: str
        def __init__(self, temporal_partition: _Optional[_Union[Partition.TemporalPartition, _Mapping]] = ..., uri: _Optional[str] = ...) -> None: ...
    TIME_INDEXED_URIS_FIELD_NUMBER: _ClassVar[int]
    time_indexed_uris: _containers.RepeatedCompositeFieldContainer[ClipAssetResponse.TimeIndexedUri]
    def __init__(self, time_indexed_uris: _Optional[_Iterable[_Union[ClipAssetResponse.TimeIndexedUri, _Mapping]]] = ...) -> None: ...

class GenerateHlsUriRequest(_message.Message):
    __slots__ = ("name", "temporal_partitions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPORAL_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    temporal_partitions: _containers.RepeatedCompositeFieldContainer[Partition.TemporalPartition]
    def __init__(self, name: _Optional[str] = ..., temporal_partitions: _Optional[_Iterable[_Union[Partition.TemporalPartition, _Mapping]]] = ...) -> None: ...

class GenerateHlsUriResponse(_message.Message):
    __slots__ = ("uri", "temporal_partitions")
    URI_FIELD_NUMBER: _ClassVar[int]
    TEMPORAL_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    uri: str
    temporal_partitions: _containers.RepeatedCompositeFieldContainer[Partition.TemporalPartition]
    def __init__(self, uri: _Optional[str] = ..., temporal_partitions: _Optional[_Iterable[_Union[Partition.TemporalPartition, _Mapping]]] = ...) -> None: ...

class SearchAssetsRequest(_message.Message):
    __slots__ = ("corpus", "page_size", "page_token", "content_time_ranges", "criteria", "facet_selections", "result_annotation_keys")
    CORPUS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TIME_RANGES_FIELD_NUMBER: _ClassVar[int]
    CRITERIA_FIELD_NUMBER: _ClassVar[int]
    FACET_SELECTIONS_FIELD_NUMBER: _ClassVar[int]
    RESULT_ANNOTATION_KEYS_FIELD_NUMBER: _ClassVar[int]
    corpus: str
    page_size: int
    page_token: str
    content_time_ranges: DateTimeRangeArray
    criteria: _containers.RepeatedCompositeFieldContainer[Criteria]
    facet_selections: _containers.RepeatedCompositeFieldContainer[FacetGroup]
    result_annotation_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, corpus: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., content_time_ranges: _Optional[_Union[DateTimeRangeArray, _Mapping]] = ..., criteria: _Optional[_Iterable[_Union[Criteria, _Mapping]]] = ..., facet_selections: _Optional[_Iterable[_Union[FacetGroup, _Mapping]]] = ..., result_annotation_keys: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteAssetMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AnnotationMatchingResult(_message.Message):
    __slots__ = ("criteria", "matched_annotations", "status")
    CRITERIA_FIELD_NUMBER: _ClassVar[int]
    MATCHED_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    criteria: Criteria
    matched_annotations: _containers.RepeatedCompositeFieldContainer[Annotation]
    status: _status_pb2.Status
    def __init__(self, criteria: _Optional[_Union[Criteria, _Mapping]] = ..., matched_annotations: _Optional[_Iterable[_Union[Annotation, _Mapping]]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...

class SearchResultItem(_message.Message):
    __slots__ = ("asset", "segments", "segment", "requested_annotations", "annotation_matching_results")
    ASSET_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_MATCHING_RESULTS_FIELD_NUMBER: _ClassVar[int]
    asset: str
    segments: _containers.RepeatedCompositeFieldContainer[Partition.TemporalPartition]
    segment: Partition.TemporalPartition
    requested_annotations: _containers.RepeatedCompositeFieldContainer[Annotation]
    annotation_matching_results: _containers.RepeatedCompositeFieldContainer[AnnotationMatchingResult]
    def __init__(self, asset: _Optional[str] = ..., segments: _Optional[_Iterable[_Union[Partition.TemporalPartition, _Mapping]]] = ..., segment: _Optional[_Union[Partition.TemporalPartition, _Mapping]] = ..., requested_annotations: _Optional[_Iterable[_Union[Annotation, _Mapping]]] = ..., annotation_matching_results: _Optional[_Iterable[_Union[AnnotationMatchingResult, _Mapping]]] = ...) -> None: ...

class SearchAssetsResponse(_message.Message):
    __slots__ = ("search_result_items", "next_page_token", "facet_results")
    SEARCH_RESULT_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FACET_RESULTS_FIELD_NUMBER: _ClassVar[int]
    search_result_items: _containers.RepeatedCompositeFieldContainer[SearchResultItem]
    next_page_token: str
    facet_results: _containers.RepeatedCompositeFieldContainer[FacetGroup]
    def __init__(self, search_result_items: _Optional[_Iterable[_Union[SearchResultItem, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., facet_results: _Optional[_Iterable[_Union[FacetGroup, _Mapping]]] = ...) -> None: ...

class IntRange(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: int
    end: int
    def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...

class FloatRange(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: float
    end: float
    def __init__(self, start: _Optional[float] = ..., end: _Optional[float] = ...) -> None: ...

class StringArray(_message.Message):
    __slots__ = ("txt_values",)
    TXT_VALUES_FIELD_NUMBER: _ClassVar[int]
    txt_values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, txt_values: _Optional[_Iterable[str]] = ...) -> None: ...

class IntRangeArray(_message.Message):
    __slots__ = ("int_ranges",)
    INT_RANGES_FIELD_NUMBER: _ClassVar[int]
    int_ranges: _containers.RepeatedCompositeFieldContainer[IntRange]
    def __init__(self, int_ranges: _Optional[_Iterable[_Union[IntRange, _Mapping]]] = ...) -> None: ...

class FloatRangeArray(_message.Message):
    __slots__ = ("float_ranges",)
    FLOAT_RANGES_FIELD_NUMBER: _ClassVar[int]
    float_ranges: _containers.RepeatedCompositeFieldContainer[FloatRange]
    def __init__(self, float_ranges: _Optional[_Iterable[_Union[FloatRange, _Mapping]]] = ...) -> None: ...

class DateTimeRange(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: _datetime_pb2.DateTime
    end: _datetime_pb2.DateTime
    def __init__(self, start: _Optional[_Union[_datetime_pb2.DateTime, _Mapping]] = ..., end: _Optional[_Union[_datetime_pb2.DateTime, _Mapping]] = ...) -> None: ...

class DateTimeRangeArray(_message.Message):
    __slots__ = ("date_time_ranges",)
    DATE_TIME_RANGES_FIELD_NUMBER: _ClassVar[int]
    date_time_ranges: _containers.RepeatedCompositeFieldContainer[DateTimeRange]
    def __init__(self, date_time_ranges: _Optional[_Iterable[_Union[DateTimeRange, _Mapping]]] = ...) -> None: ...

class CircleArea(_message.Message):
    __slots__ = ("latitude", "longitude", "radius_meter")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    RADIUS_METER_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    radius_meter: float
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., radius_meter: _Optional[float] = ...) -> None: ...

class GeoLocationArray(_message.Message):
    __slots__ = ("circle_areas",)
    CIRCLE_AREAS_FIELD_NUMBER: _ClassVar[int]
    circle_areas: _containers.RepeatedCompositeFieldContainer[CircleArea]
    def __init__(self, circle_areas: _Optional[_Iterable[_Union[CircleArea, _Mapping]]] = ...) -> None: ...

class BoolValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class Criteria(_message.Message):
    __slots__ = ("text_array", "int_range_array", "float_range_array", "date_time_range_array", "geo_location_array", "bool_value", "field", "fetch_matched_annotations")
    TEXT_ARRAY_FIELD_NUMBER: _ClassVar[int]
    INT_RANGE_ARRAY_FIELD_NUMBER: _ClassVar[int]
    FLOAT_RANGE_ARRAY_FIELD_NUMBER: _ClassVar[int]
    DATE_TIME_RANGE_ARRAY_FIELD_NUMBER: _ClassVar[int]
    GEO_LOCATION_ARRAY_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    FETCH_MATCHED_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    text_array: StringArray
    int_range_array: IntRangeArray
    float_range_array: FloatRangeArray
    date_time_range_array: DateTimeRangeArray
    geo_location_array: GeoLocationArray
    bool_value: BoolValue
    field: str
    fetch_matched_annotations: bool
    def __init__(self, text_array: _Optional[_Union[StringArray, _Mapping]] = ..., int_range_array: _Optional[_Union[IntRangeArray, _Mapping]] = ..., float_range_array: _Optional[_Union[FloatRangeArray, _Mapping]] = ..., date_time_range_array: _Optional[_Union[DateTimeRangeArray, _Mapping]] = ..., geo_location_array: _Optional[_Union[GeoLocationArray, _Mapping]] = ..., bool_value: _Optional[_Union[BoolValue, _Mapping]] = ..., field: _Optional[str] = ..., fetch_matched_annotations: bool = ...) -> None: ...

class Partition(_message.Message):
    __slots__ = ("temporal_partition", "spatial_partition")
    class TemporalPartition(_message.Message):
        __slots__ = ("start_time", "end_time")
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        start_time: _timestamp_pb2.Timestamp
        end_time: _timestamp_pb2.Timestamp
        def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class SpatialPartition(_message.Message):
        __slots__ = ("x_min", "y_min", "x_max", "y_max")
        X_MIN_FIELD_NUMBER: _ClassVar[int]
        Y_MIN_FIELD_NUMBER: _ClassVar[int]
        X_MAX_FIELD_NUMBER: _ClassVar[int]
        Y_MAX_FIELD_NUMBER: _ClassVar[int]
        x_min: int
        y_min: int
        x_max: int
        y_max: int
        def __init__(self, x_min: _Optional[int] = ..., y_min: _Optional[int] = ..., x_max: _Optional[int] = ..., y_max: _Optional[int] = ...) -> None: ...
    TEMPORAL_PARTITION_FIELD_NUMBER: _ClassVar[int]
    SPATIAL_PARTITION_FIELD_NUMBER: _ClassVar[int]
    temporal_partition: Partition.TemporalPartition
    spatial_partition: Partition.SpatialPartition
    def __init__(self, temporal_partition: _Optional[_Union[Partition.TemporalPartition, _Mapping]] = ..., spatial_partition: _Optional[_Union[Partition.SpatialPartition, _Mapping]] = ...) -> None: ...
