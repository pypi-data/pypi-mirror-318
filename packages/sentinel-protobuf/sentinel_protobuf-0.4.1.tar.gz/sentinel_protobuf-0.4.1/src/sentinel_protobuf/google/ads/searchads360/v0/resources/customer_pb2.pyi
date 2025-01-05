from google.ads.searchads360.v0.enums import account_status_pb2 as _account_status_pb2
from google.ads.searchads360.v0.enums import account_type_pb2 as _account_type_pb2
from google.ads.searchads360.v0.enums import conversion_tracking_status_enum_pb2 as _conversion_tracking_status_enum_pb2
from google.ads.searchads360.v0.enums import customer_status_pb2 as _customer_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Customer(_message.Message):
    __slots__ = ("resource_name", "id", "descriptive_name", "currency_code", "time_zone", "tracking_url_template", "final_url_suffix", "auto_tagging_enabled", "manager", "conversion_tracking_setting", "account_type", "double_click_campaign_manager_setting", "account_status", "last_modified_time", "engine_id", "status", "creation_time")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    FINAL_URL_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    AUTO_TAGGING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MANAGER_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_TRACKING_SETTING_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_CLICK_CAMPAIGN_MANAGER_SETTING_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    ENGINE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    descriptive_name: str
    currency_code: str
    time_zone: str
    tracking_url_template: str
    final_url_suffix: str
    auto_tagging_enabled: bool
    manager: bool
    conversion_tracking_setting: ConversionTrackingSetting
    account_type: _account_type_pb2.AccountTypeEnum.AccountType
    double_click_campaign_manager_setting: DoubleClickCampaignManagerSetting
    account_status: _account_status_pb2.AccountStatusEnum.AccountStatus
    last_modified_time: str
    engine_id: str
    status: _customer_status_pb2.CustomerStatusEnum.CustomerStatus
    creation_time: str
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., descriptive_name: _Optional[str] = ..., currency_code: _Optional[str] = ..., time_zone: _Optional[str] = ..., tracking_url_template: _Optional[str] = ..., final_url_suffix: _Optional[str] = ..., auto_tagging_enabled: bool = ..., manager: bool = ..., conversion_tracking_setting: _Optional[_Union[ConversionTrackingSetting, _Mapping]] = ..., account_type: _Optional[_Union[_account_type_pb2.AccountTypeEnum.AccountType, str]] = ..., double_click_campaign_manager_setting: _Optional[_Union[DoubleClickCampaignManagerSetting, _Mapping]] = ..., account_status: _Optional[_Union[_account_status_pb2.AccountStatusEnum.AccountStatus, str]] = ..., last_modified_time: _Optional[str] = ..., engine_id: _Optional[str] = ..., status: _Optional[_Union[_customer_status_pb2.CustomerStatusEnum.CustomerStatus, str]] = ..., creation_time: _Optional[str] = ...) -> None: ...

class ConversionTrackingSetting(_message.Message):
    __slots__ = ("conversion_tracking_id", "google_ads_cross_account_conversion_tracking_id", "cross_account_conversion_tracking_id", "accepted_customer_data_terms", "conversion_tracking_status", "enhanced_conversions_for_leads_enabled", "google_ads_conversion_customer")
    CONVERSION_TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_ADS_CROSS_ACCOUNT_CONVERSION_TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    CROSS_ACCOUNT_CONVERSION_TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_CUSTOMER_DATA_TERMS_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_TRACKING_STATUS_FIELD_NUMBER: _ClassVar[int]
    ENHANCED_CONVERSIONS_FOR_LEADS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_ADS_CONVERSION_CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    conversion_tracking_id: int
    google_ads_cross_account_conversion_tracking_id: int
    cross_account_conversion_tracking_id: int
    accepted_customer_data_terms: bool
    conversion_tracking_status: _conversion_tracking_status_enum_pb2.ConversionTrackingStatusEnum.ConversionTrackingStatus
    enhanced_conversions_for_leads_enabled: bool
    google_ads_conversion_customer: str
    def __init__(self, conversion_tracking_id: _Optional[int] = ..., google_ads_cross_account_conversion_tracking_id: _Optional[int] = ..., cross_account_conversion_tracking_id: _Optional[int] = ..., accepted_customer_data_terms: bool = ..., conversion_tracking_status: _Optional[_Union[_conversion_tracking_status_enum_pb2.ConversionTrackingStatusEnum.ConversionTrackingStatus, str]] = ..., enhanced_conversions_for_leads_enabled: bool = ..., google_ads_conversion_customer: _Optional[str] = ...) -> None: ...

class DoubleClickCampaignManagerSetting(_message.Message):
    __slots__ = ("advertiser_id", "network_id", "time_zone")
    ADVERTISER_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    advertiser_id: int
    network_id: int
    time_zone: str
    def __init__(self, advertiser_id: _Optional[int] = ..., network_id: _Optional[int] = ..., time_zone: _Optional[str] = ...) -> None: ...
