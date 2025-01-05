from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import money_pb2 as _money_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Service(_message.Message):
    __slots__ = ('name', 'service_id', 'display_name', 'business_entity_name')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_ENTITY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    service_id: str
    display_name: str
    business_entity_name: str

    def __init__(self, name: _Optional[str]=..., service_id: _Optional[str]=..., display_name: _Optional[str]=..., business_entity_name: _Optional[str]=...) -> None:
        ...

class Sku(_message.Message):
    __slots__ = ('name', 'sku_id', 'description', 'category', 'service_regions', 'pricing_info', 'service_provider_name', 'geo_taxonomy')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SKU_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SERVICE_REGIONS_FIELD_NUMBER: _ClassVar[int]
    PRICING_INFO_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
    GEO_TAXONOMY_FIELD_NUMBER: _ClassVar[int]
    name: str
    sku_id: str
    description: str
    category: Category
    service_regions: _containers.RepeatedScalarFieldContainer[str]
    pricing_info: _containers.RepeatedCompositeFieldContainer[PricingInfo]
    service_provider_name: str
    geo_taxonomy: GeoTaxonomy

    def __init__(self, name: _Optional[str]=..., sku_id: _Optional[str]=..., description: _Optional[str]=..., category: _Optional[_Union[Category, _Mapping]]=..., service_regions: _Optional[_Iterable[str]]=..., pricing_info: _Optional[_Iterable[_Union[PricingInfo, _Mapping]]]=..., service_provider_name: _Optional[str]=..., geo_taxonomy: _Optional[_Union[GeoTaxonomy, _Mapping]]=...) -> None:
        ...

class Category(_message.Message):
    __slots__ = ('service_display_name', 'resource_family', 'resource_group', 'usage_type')
    SERVICE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FAMILY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    USAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    service_display_name: str
    resource_family: str
    resource_group: str
    usage_type: str

    def __init__(self, service_display_name: _Optional[str]=..., resource_family: _Optional[str]=..., resource_group: _Optional[str]=..., usage_type: _Optional[str]=...) -> None:
        ...

class PricingInfo(_message.Message):
    __slots__ = ('effective_time', 'summary', 'pricing_expression', 'aggregation_info', 'currency_conversion_rate')
    EFFECTIVE_TIME_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    PRICING_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_INFO_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CONVERSION_RATE_FIELD_NUMBER: _ClassVar[int]
    effective_time: _timestamp_pb2.Timestamp
    summary: str
    pricing_expression: PricingExpression
    aggregation_info: AggregationInfo
    currency_conversion_rate: float

    def __init__(self, effective_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., summary: _Optional[str]=..., pricing_expression: _Optional[_Union[PricingExpression, _Mapping]]=..., aggregation_info: _Optional[_Union[AggregationInfo, _Mapping]]=..., currency_conversion_rate: _Optional[float]=...) -> None:
        ...

class PricingExpression(_message.Message):
    __slots__ = ('usage_unit', 'display_quantity', 'tiered_rates', 'usage_unit_description', 'base_unit', 'base_unit_description', 'base_unit_conversion_factor')

    class TierRate(_message.Message):
        __slots__ = ('start_usage_amount', 'unit_price')
        START_USAGE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        UNIT_PRICE_FIELD_NUMBER: _ClassVar[int]
        start_usage_amount: float
        unit_price: _money_pb2.Money

        def __init__(self, start_usage_amount: _Optional[float]=..., unit_price: _Optional[_Union[_money_pb2.Money, _Mapping]]=...) -> None:
            ...
    USAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TIERED_RATES_FIELD_NUMBER: _ClassVar[int]
    USAGE_UNIT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BASE_UNIT_FIELD_NUMBER: _ClassVar[int]
    BASE_UNIT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BASE_UNIT_CONVERSION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    usage_unit: str
    display_quantity: float
    tiered_rates: _containers.RepeatedCompositeFieldContainer[PricingExpression.TierRate]
    usage_unit_description: str
    base_unit: str
    base_unit_description: str
    base_unit_conversion_factor: float

    def __init__(self, usage_unit: _Optional[str]=..., display_quantity: _Optional[float]=..., tiered_rates: _Optional[_Iterable[_Union[PricingExpression.TierRate, _Mapping]]]=..., usage_unit_description: _Optional[str]=..., base_unit: _Optional[str]=..., base_unit_description: _Optional[str]=..., base_unit_conversion_factor: _Optional[float]=...) -> None:
        ...

class AggregationInfo(_message.Message):
    __slots__ = ('aggregation_level', 'aggregation_interval', 'aggregation_count')

    class AggregationLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AGGREGATION_LEVEL_UNSPECIFIED: _ClassVar[AggregationInfo.AggregationLevel]
        ACCOUNT: _ClassVar[AggregationInfo.AggregationLevel]
        PROJECT: _ClassVar[AggregationInfo.AggregationLevel]
    AGGREGATION_LEVEL_UNSPECIFIED: AggregationInfo.AggregationLevel
    ACCOUNT: AggregationInfo.AggregationLevel
    PROJECT: AggregationInfo.AggregationLevel

    class AggregationInterval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AGGREGATION_INTERVAL_UNSPECIFIED: _ClassVar[AggregationInfo.AggregationInterval]
        DAILY: _ClassVar[AggregationInfo.AggregationInterval]
        MONTHLY: _ClassVar[AggregationInfo.AggregationInterval]
    AGGREGATION_INTERVAL_UNSPECIFIED: AggregationInfo.AggregationInterval
    DAILY: AggregationInfo.AggregationInterval
    MONTHLY: AggregationInfo.AggregationInterval
    AGGREGATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    aggregation_level: AggregationInfo.AggregationLevel
    aggregation_interval: AggregationInfo.AggregationInterval
    aggregation_count: int

    def __init__(self, aggregation_level: _Optional[_Union[AggregationInfo.AggregationLevel, str]]=..., aggregation_interval: _Optional[_Union[AggregationInfo.AggregationInterval, str]]=..., aggregation_count: _Optional[int]=...) -> None:
        ...

class GeoTaxonomy(_message.Message):
    __slots__ = ('type', 'regions')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[GeoTaxonomy.Type]
        GLOBAL: _ClassVar[GeoTaxonomy.Type]
        REGIONAL: _ClassVar[GeoTaxonomy.Type]
        MULTI_REGIONAL: _ClassVar[GeoTaxonomy.Type]
    TYPE_UNSPECIFIED: GeoTaxonomy.Type
    GLOBAL: GeoTaxonomy.Type
    REGIONAL: GeoTaxonomy.Type
    MULTI_REGIONAL: GeoTaxonomy.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REGIONS_FIELD_NUMBER: _ClassVar[int]
    type: GeoTaxonomy.Type
    regions: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, type: _Optional[_Union[GeoTaxonomy.Type, str]]=..., regions: _Optional[_Iterable[str]]=...) -> None:
        ...

class ListServicesRequest(_message.Message):
    __slots__ = ('page_size', 'page_token')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListServicesResponse(_message.Message):
    __slots__ = ('services', 'next_page_token')
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    services: _containers.RepeatedCompositeFieldContainer[Service]
    next_page_token: str

    def __init__(self, services: _Optional[_Iterable[_Union[Service, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListSkusRequest(_message.Message):
    __slots__ = ('parent', 'start_time', 'end_time', 'currency_code', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    currency_code: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., currency_code: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListSkusResponse(_message.Message):
    __slots__ = ('skus', 'next_page_token')
    SKUS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    skus: _containers.RepeatedCompositeFieldContainer[Sku]
    next_page_token: str

    def __init__(self, skus: _Optional[_Iterable[_Union[Sku, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...