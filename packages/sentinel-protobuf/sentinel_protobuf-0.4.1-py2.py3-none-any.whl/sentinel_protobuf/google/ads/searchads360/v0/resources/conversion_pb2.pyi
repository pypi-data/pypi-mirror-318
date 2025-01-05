from google.ads.searchads360.v0.enums import asset_field_type_pb2 as _asset_field_type_pb2
from google.ads.searchads360.v0.enums import attribution_type_pb2 as _attribution_type_pb2
from google.ads.searchads360.v0.enums import conversion_status_pb2 as _conversion_status_pb2
from google.ads.searchads360.v0.enums import product_channel_pb2 as _product_channel_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Conversion(_message.Message):
    __slots__ = ("resource_name", "id", "criterion_id", "merchant_id", "ad_id", "click_id", "visit_id", "advertiser_conversion_id", "product_id", "product_channel", "product_language_code", "product_store_id", "product_country_code", "attribution_type", "conversion_date_time", "conversion_last_modified_date_time", "conversion_visit_date_time", "conversion_quantity", "conversion_revenue_micros", "floodlight_original_revenue", "floodlight_order_id", "status", "asset_id", "asset_field_type")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CRITERION_ID_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    AD_ID_FIELD_NUMBER: _ClassVar[int]
    CLICK_ID_FIELD_NUMBER: _ClassVar[int]
    VISIT_ID_FIELD_NUMBER: _ClassVar[int]
    ADVERTISER_CONVERSION_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_STORE_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_LAST_MODIFIED_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_VISIT_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_REVENUE_MICROS_FIELD_NUMBER: _ClassVar[int]
    FLOODLIGHT_ORIGINAL_REVENUE_FIELD_NUMBER: _ClassVar[int]
    FLOODLIGHT_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    criterion_id: int
    merchant_id: int
    ad_id: int
    click_id: str
    visit_id: int
    advertiser_conversion_id: str
    product_id: str
    product_channel: _product_channel_pb2.ProductChannelEnum.ProductChannel
    product_language_code: str
    product_store_id: str
    product_country_code: str
    attribution_type: _attribution_type_pb2.AttributionTypeEnum.AttributionType
    conversion_date_time: str
    conversion_last_modified_date_time: str
    conversion_visit_date_time: str
    conversion_quantity: int
    conversion_revenue_micros: int
    floodlight_original_revenue: int
    floodlight_order_id: str
    status: _conversion_status_pb2.ConversionStatusEnum.ConversionStatus
    asset_id: int
    asset_field_type: _asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., criterion_id: _Optional[int] = ..., merchant_id: _Optional[int] = ..., ad_id: _Optional[int] = ..., click_id: _Optional[str] = ..., visit_id: _Optional[int] = ..., advertiser_conversion_id: _Optional[str] = ..., product_id: _Optional[str] = ..., product_channel: _Optional[_Union[_product_channel_pb2.ProductChannelEnum.ProductChannel, str]] = ..., product_language_code: _Optional[str] = ..., product_store_id: _Optional[str] = ..., product_country_code: _Optional[str] = ..., attribution_type: _Optional[_Union[_attribution_type_pb2.AttributionTypeEnum.AttributionType, str]] = ..., conversion_date_time: _Optional[str] = ..., conversion_last_modified_date_time: _Optional[str] = ..., conversion_visit_date_time: _Optional[str] = ..., conversion_quantity: _Optional[int] = ..., conversion_revenue_micros: _Optional[int] = ..., floodlight_original_revenue: _Optional[int] = ..., floodlight_order_id: _Optional[str] = ..., status: _Optional[_Union[_conversion_status_pb2.ConversionStatusEnum.ConversionStatus, str]] = ..., asset_id: _Optional[int] = ..., asset_field_type: _Optional[_Union[_asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType, str]] = ...) -> None: ...
