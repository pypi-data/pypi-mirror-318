from google.ads.googleads.v17.enums import product_availability_pb2 as _product_availability_pb2
from google.ads.googleads.v17.enums import product_channel_pb2 as _product_channel_pb2
from google.ads.googleads.v17.enums import product_channel_exclusivity_pb2 as _product_channel_exclusivity_pb2
from google.ads.googleads.v17.enums import product_condition_pb2 as _product_condition_pb2
from google.ads.googleads.v17.enums import product_issue_severity_pb2 as _product_issue_severity_pb2
from google.ads.googleads.v17.enums import product_status_pb2 as _product_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShoppingProduct(_message.Message):
    __slots__ = ("resource_name", "merchant_center_id", "channel", "language_code", "feed_label", "item_id", "multi_client_account_id", "title", "brand", "price_micros", "currency_code", "channel_exclusivity", "condition", "availability", "target_countries", "custom_attribute0", "custom_attribute1", "custom_attribute2", "custom_attribute3", "custom_attribute4", "category_level1", "category_level2", "category_level3", "category_level4", "category_level5", "product_type_level1", "product_type_level2", "product_type_level3", "product_type_level4", "product_type_level5", "effective_max_cpc_micros", "status", "issues", "campaign", "ad_group")
    class ProductIssue(_message.Message):
        __slots__ = ("error_code", "ads_severity", "attribute_name", "description", "detail", "documentation", "affected_regions")
        ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
        ADS_SEVERITY_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTE_NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DETAIL_FIELD_NUMBER: _ClassVar[int]
        DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
        AFFECTED_REGIONS_FIELD_NUMBER: _ClassVar[int]
        error_code: str
        ads_severity: _product_issue_severity_pb2.ProductIssueSeverityEnum.ProductIssueSeverity
        attribute_name: str
        description: str
        detail: str
        documentation: str
        affected_regions: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, error_code: _Optional[str] = ..., ads_severity: _Optional[_Union[_product_issue_severity_pb2.ProductIssueSeverityEnum.ProductIssueSeverity, str]] = ..., attribute_name: _Optional[str] = ..., description: _Optional[str] = ..., detail: _Optional[str] = ..., documentation: _Optional[str] = ..., affected_regions: _Optional[_Iterable[str]] = ...) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_CENTER_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    MULTI_CLIENT_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    PRICE_MICROS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_EXCLUSIVITY_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    TARGET_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTE0_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTE1_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTE2_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTE3_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTE4_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_LEVEL1_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_LEVEL2_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_LEVEL3_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_LEVEL4_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_LEVEL5_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_LEVEL1_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_LEVEL2_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_LEVEL3_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_LEVEL4_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_LEVEL5_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_MAX_CPC_MICROS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    merchant_center_id: int
    channel: _product_channel_pb2.ProductChannelEnum.ProductChannel
    language_code: str
    feed_label: str
    item_id: str
    multi_client_account_id: int
    title: str
    brand: str
    price_micros: int
    currency_code: str
    channel_exclusivity: _product_channel_exclusivity_pb2.ProductChannelExclusivityEnum.ProductChannelExclusivity
    condition: _product_condition_pb2.ProductConditionEnum.ProductCondition
    availability: _product_availability_pb2.ProductAvailabilityEnum.ProductAvailability
    target_countries: _containers.RepeatedScalarFieldContainer[str]
    custom_attribute0: str
    custom_attribute1: str
    custom_attribute2: str
    custom_attribute3: str
    custom_attribute4: str
    category_level1: str
    category_level2: str
    category_level3: str
    category_level4: str
    category_level5: str
    product_type_level1: str
    product_type_level2: str
    product_type_level3: str
    product_type_level4: str
    product_type_level5: str
    effective_max_cpc_micros: int
    status: _product_status_pb2.ProductStatusEnum.ProductStatus
    issues: _containers.RepeatedCompositeFieldContainer[ShoppingProduct.ProductIssue]
    campaign: str
    ad_group: str
    def __init__(self, resource_name: _Optional[str] = ..., merchant_center_id: _Optional[int] = ..., channel: _Optional[_Union[_product_channel_pb2.ProductChannelEnum.ProductChannel, str]] = ..., language_code: _Optional[str] = ..., feed_label: _Optional[str] = ..., item_id: _Optional[str] = ..., multi_client_account_id: _Optional[int] = ..., title: _Optional[str] = ..., brand: _Optional[str] = ..., price_micros: _Optional[int] = ..., currency_code: _Optional[str] = ..., channel_exclusivity: _Optional[_Union[_product_channel_exclusivity_pb2.ProductChannelExclusivityEnum.ProductChannelExclusivity, str]] = ..., condition: _Optional[_Union[_product_condition_pb2.ProductConditionEnum.ProductCondition, str]] = ..., availability: _Optional[_Union[_product_availability_pb2.ProductAvailabilityEnum.ProductAvailability, str]] = ..., target_countries: _Optional[_Iterable[str]] = ..., custom_attribute0: _Optional[str] = ..., custom_attribute1: _Optional[str] = ..., custom_attribute2: _Optional[str] = ..., custom_attribute3: _Optional[str] = ..., custom_attribute4: _Optional[str] = ..., category_level1: _Optional[str] = ..., category_level2: _Optional[str] = ..., category_level3: _Optional[str] = ..., category_level4: _Optional[str] = ..., category_level5: _Optional[str] = ..., product_type_level1: _Optional[str] = ..., product_type_level2: _Optional[str] = ..., product_type_level3: _Optional[str] = ..., product_type_level4: _Optional[str] = ..., product_type_level5: _Optional[str] = ..., effective_max_cpc_micros: _Optional[int] = ..., status: _Optional[_Union[_product_status_pb2.ProductStatusEnum.ProductStatus, str]] = ..., issues: _Optional[_Iterable[_Union[ShoppingProduct.ProductIssue, _Mapping]]] = ..., campaign: _Optional[str] = ..., ad_group: _Optional[str] = ...) -> None: ...
