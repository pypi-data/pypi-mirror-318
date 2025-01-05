from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.retail.v2 import common_pb2 as _common_pb2
from google.cloud.retail.v2 import import_config_pb2 as _import_config_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProductLevelConfig(_message.Message):
    __slots__ = ("ingestion_product_type", "merchant_center_product_id_field")
    INGESTION_PRODUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_CENTER_PRODUCT_ID_FIELD_FIELD_NUMBER: _ClassVar[int]
    ingestion_product_type: str
    merchant_center_product_id_field: str
    def __init__(self, ingestion_product_type: _Optional[str] = ..., merchant_center_product_id_field: _Optional[str] = ...) -> None: ...

class CatalogAttribute(_message.Message):
    __slots__ = ("key", "in_use", "type", "indexable_option", "dynamic_facetable_option", "searchable_option", "exact_searchable_option", "retrievable_option", "facet_config")
    class AttributeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[CatalogAttribute.AttributeType]
        TEXTUAL: _ClassVar[CatalogAttribute.AttributeType]
        NUMERICAL: _ClassVar[CatalogAttribute.AttributeType]
    UNKNOWN: CatalogAttribute.AttributeType
    TEXTUAL: CatalogAttribute.AttributeType
    NUMERICAL: CatalogAttribute.AttributeType
    class IndexableOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INDEXABLE_OPTION_UNSPECIFIED: _ClassVar[CatalogAttribute.IndexableOption]
        INDEXABLE_ENABLED: _ClassVar[CatalogAttribute.IndexableOption]
        INDEXABLE_DISABLED: _ClassVar[CatalogAttribute.IndexableOption]
    INDEXABLE_OPTION_UNSPECIFIED: CatalogAttribute.IndexableOption
    INDEXABLE_ENABLED: CatalogAttribute.IndexableOption
    INDEXABLE_DISABLED: CatalogAttribute.IndexableOption
    class DynamicFacetableOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DYNAMIC_FACETABLE_OPTION_UNSPECIFIED: _ClassVar[CatalogAttribute.DynamicFacetableOption]
        DYNAMIC_FACETABLE_ENABLED: _ClassVar[CatalogAttribute.DynamicFacetableOption]
        DYNAMIC_FACETABLE_DISABLED: _ClassVar[CatalogAttribute.DynamicFacetableOption]
    DYNAMIC_FACETABLE_OPTION_UNSPECIFIED: CatalogAttribute.DynamicFacetableOption
    DYNAMIC_FACETABLE_ENABLED: CatalogAttribute.DynamicFacetableOption
    DYNAMIC_FACETABLE_DISABLED: CatalogAttribute.DynamicFacetableOption
    class SearchableOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEARCHABLE_OPTION_UNSPECIFIED: _ClassVar[CatalogAttribute.SearchableOption]
        SEARCHABLE_ENABLED: _ClassVar[CatalogAttribute.SearchableOption]
        SEARCHABLE_DISABLED: _ClassVar[CatalogAttribute.SearchableOption]
    SEARCHABLE_OPTION_UNSPECIFIED: CatalogAttribute.SearchableOption
    SEARCHABLE_ENABLED: CatalogAttribute.SearchableOption
    SEARCHABLE_DISABLED: CatalogAttribute.SearchableOption
    class ExactSearchableOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXACT_SEARCHABLE_OPTION_UNSPECIFIED: _ClassVar[CatalogAttribute.ExactSearchableOption]
        EXACT_SEARCHABLE_ENABLED: _ClassVar[CatalogAttribute.ExactSearchableOption]
        EXACT_SEARCHABLE_DISABLED: _ClassVar[CatalogAttribute.ExactSearchableOption]
    EXACT_SEARCHABLE_OPTION_UNSPECIFIED: CatalogAttribute.ExactSearchableOption
    EXACT_SEARCHABLE_ENABLED: CatalogAttribute.ExactSearchableOption
    EXACT_SEARCHABLE_DISABLED: CatalogAttribute.ExactSearchableOption
    class RetrievableOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RETRIEVABLE_OPTION_UNSPECIFIED: _ClassVar[CatalogAttribute.RetrievableOption]
        RETRIEVABLE_ENABLED: _ClassVar[CatalogAttribute.RetrievableOption]
        RETRIEVABLE_DISABLED: _ClassVar[CatalogAttribute.RetrievableOption]
    RETRIEVABLE_OPTION_UNSPECIFIED: CatalogAttribute.RetrievableOption
    RETRIEVABLE_ENABLED: CatalogAttribute.RetrievableOption
    RETRIEVABLE_DISABLED: CatalogAttribute.RetrievableOption
    class FacetConfig(_message.Message):
        __slots__ = ("facet_intervals", "ignored_facet_values", "merged_facet_values", "merged_facet", "rerank_config")
        class IgnoredFacetValues(_message.Message):
            __slots__ = ("values", "start_time", "end_time")
            VALUES_FIELD_NUMBER: _ClassVar[int]
            START_TIME_FIELD_NUMBER: _ClassVar[int]
            END_TIME_FIELD_NUMBER: _ClassVar[int]
            values: _containers.RepeatedScalarFieldContainer[str]
            start_time: _timestamp_pb2.Timestamp
            end_time: _timestamp_pb2.Timestamp
            def __init__(self, values: _Optional[_Iterable[str]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
        class MergedFacetValue(_message.Message):
            __slots__ = ("values", "merged_value")
            VALUES_FIELD_NUMBER: _ClassVar[int]
            MERGED_VALUE_FIELD_NUMBER: _ClassVar[int]
            values: _containers.RepeatedScalarFieldContainer[str]
            merged_value: str
            def __init__(self, values: _Optional[_Iterable[str]] = ..., merged_value: _Optional[str] = ...) -> None: ...
        class MergedFacet(_message.Message):
            __slots__ = ("merged_facet_key",)
            MERGED_FACET_KEY_FIELD_NUMBER: _ClassVar[int]
            merged_facet_key: str
            def __init__(self, merged_facet_key: _Optional[str] = ...) -> None: ...
        class RerankConfig(_message.Message):
            __slots__ = ("rerank_facet", "facet_values")
            RERANK_FACET_FIELD_NUMBER: _ClassVar[int]
            FACET_VALUES_FIELD_NUMBER: _ClassVar[int]
            rerank_facet: bool
            facet_values: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, rerank_facet: bool = ..., facet_values: _Optional[_Iterable[str]] = ...) -> None: ...
        FACET_INTERVALS_FIELD_NUMBER: _ClassVar[int]
        IGNORED_FACET_VALUES_FIELD_NUMBER: _ClassVar[int]
        MERGED_FACET_VALUES_FIELD_NUMBER: _ClassVar[int]
        MERGED_FACET_FIELD_NUMBER: _ClassVar[int]
        RERANK_CONFIG_FIELD_NUMBER: _ClassVar[int]
        facet_intervals: _containers.RepeatedCompositeFieldContainer[_common_pb2.Interval]
        ignored_facet_values: _containers.RepeatedCompositeFieldContainer[CatalogAttribute.FacetConfig.IgnoredFacetValues]
        merged_facet_values: _containers.RepeatedCompositeFieldContainer[CatalogAttribute.FacetConfig.MergedFacetValue]
        merged_facet: CatalogAttribute.FacetConfig.MergedFacet
        rerank_config: CatalogAttribute.FacetConfig.RerankConfig
        def __init__(self, facet_intervals: _Optional[_Iterable[_Union[_common_pb2.Interval, _Mapping]]] = ..., ignored_facet_values: _Optional[_Iterable[_Union[CatalogAttribute.FacetConfig.IgnoredFacetValues, _Mapping]]] = ..., merged_facet_values: _Optional[_Iterable[_Union[CatalogAttribute.FacetConfig.MergedFacetValue, _Mapping]]] = ..., merged_facet: _Optional[_Union[CatalogAttribute.FacetConfig.MergedFacet, _Mapping]] = ..., rerank_config: _Optional[_Union[CatalogAttribute.FacetConfig.RerankConfig, _Mapping]] = ...) -> None: ...
    KEY_FIELD_NUMBER: _ClassVar[int]
    IN_USE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INDEXABLE_OPTION_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_FACETABLE_OPTION_FIELD_NUMBER: _ClassVar[int]
    SEARCHABLE_OPTION_FIELD_NUMBER: _ClassVar[int]
    EXACT_SEARCHABLE_OPTION_FIELD_NUMBER: _ClassVar[int]
    RETRIEVABLE_OPTION_FIELD_NUMBER: _ClassVar[int]
    FACET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    key: str
    in_use: bool
    type: CatalogAttribute.AttributeType
    indexable_option: CatalogAttribute.IndexableOption
    dynamic_facetable_option: CatalogAttribute.DynamicFacetableOption
    searchable_option: CatalogAttribute.SearchableOption
    exact_searchable_option: CatalogAttribute.ExactSearchableOption
    retrievable_option: CatalogAttribute.RetrievableOption
    facet_config: CatalogAttribute.FacetConfig
    def __init__(self, key: _Optional[str] = ..., in_use: bool = ..., type: _Optional[_Union[CatalogAttribute.AttributeType, str]] = ..., indexable_option: _Optional[_Union[CatalogAttribute.IndexableOption, str]] = ..., dynamic_facetable_option: _Optional[_Union[CatalogAttribute.DynamicFacetableOption, str]] = ..., searchable_option: _Optional[_Union[CatalogAttribute.SearchableOption, str]] = ..., exact_searchable_option: _Optional[_Union[CatalogAttribute.ExactSearchableOption, str]] = ..., retrievable_option: _Optional[_Union[CatalogAttribute.RetrievableOption, str]] = ..., facet_config: _Optional[_Union[CatalogAttribute.FacetConfig, _Mapping]] = ...) -> None: ...

class AttributesConfig(_message.Message):
    __slots__ = ("name", "catalog_attributes", "attribute_config_level")
    class CatalogAttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CatalogAttribute
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CatalogAttribute, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CATALOG_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_CONFIG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    name: str
    catalog_attributes: _containers.MessageMap[str, CatalogAttribute]
    attribute_config_level: _common_pb2.AttributeConfigLevel
    def __init__(self, name: _Optional[str] = ..., catalog_attributes: _Optional[_Mapping[str, CatalogAttribute]] = ..., attribute_config_level: _Optional[_Union[_common_pb2.AttributeConfigLevel, str]] = ...) -> None: ...

class CompletionConfig(_message.Message):
    __slots__ = ("name", "matching_order", "max_suggestions", "min_prefix_length", "auto_learning", "suggestions_input_config", "last_suggestions_import_operation", "denylist_input_config", "last_denylist_import_operation", "allowlist_input_config", "last_allowlist_import_operation")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MATCHING_ORDER_FIELD_NUMBER: _ClassVar[int]
    MAX_SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    MIN_PREFIX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    AUTO_LEARNING_FIELD_NUMBER: _ClassVar[int]
    SUGGESTIONS_INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LAST_SUGGESTIONS_IMPORT_OPERATION_FIELD_NUMBER: _ClassVar[int]
    DENYLIST_INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LAST_DENYLIST_IMPORT_OPERATION_FIELD_NUMBER: _ClassVar[int]
    ALLOWLIST_INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LAST_ALLOWLIST_IMPORT_OPERATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    matching_order: str
    max_suggestions: int
    min_prefix_length: int
    auto_learning: bool
    suggestions_input_config: _import_config_pb2.CompletionDataInputConfig
    last_suggestions_import_operation: str
    denylist_input_config: _import_config_pb2.CompletionDataInputConfig
    last_denylist_import_operation: str
    allowlist_input_config: _import_config_pb2.CompletionDataInputConfig
    last_allowlist_import_operation: str
    def __init__(self, name: _Optional[str] = ..., matching_order: _Optional[str] = ..., max_suggestions: _Optional[int] = ..., min_prefix_length: _Optional[int] = ..., auto_learning: bool = ..., suggestions_input_config: _Optional[_Union[_import_config_pb2.CompletionDataInputConfig, _Mapping]] = ..., last_suggestions_import_operation: _Optional[str] = ..., denylist_input_config: _Optional[_Union[_import_config_pb2.CompletionDataInputConfig, _Mapping]] = ..., last_denylist_import_operation: _Optional[str] = ..., allowlist_input_config: _Optional[_Union[_import_config_pb2.CompletionDataInputConfig, _Mapping]] = ..., last_allowlist_import_operation: _Optional[str] = ...) -> None: ...

class Catalog(_message.Message):
    __slots__ = ("name", "display_name", "product_level_config")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_LEVEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    product_level_config: ProductLevelConfig
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., product_level_config: _Optional[_Union[ProductLevelConfig, _Mapping]] = ...) -> None: ...
