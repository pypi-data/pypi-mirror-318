from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SmartCampaignSetting(_message.Message):
    __slots__ = ("resource_name", "campaign", "phone_number", "advertising_language_code", "final_url", "ad_optimized_business_profile_setting", "business_name", "business_profile_location")
    class PhoneNumber(_message.Message):
        __slots__ = ("phone_number", "country_code")
        PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
        phone_number: str
        country_code: str
        def __init__(self, phone_number: _Optional[str] = ..., country_code: _Optional[str] = ...) -> None: ...
    class AdOptimizedBusinessProfileSetting(_message.Message):
        __slots__ = ("include_lead_form",)
        INCLUDE_LEAD_FORM_FIELD_NUMBER: _ClassVar[int]
        include_lead_form: bool
        def __init__(self, include_lead_form: bool = ...) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ADVERTISING_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    FINAL_URL_FIELD_NUMBER: _ClassVar[int]
    AD_OPTIMIZED_BUSINESS_PROFILE_SETTING_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_PROFILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    campaign: str
    phone_number: SmartCampaignSetting.PhoneNumber
    advertising_language_code: str
    final_url: str
    ad_optimized_business_profile_setting: SmartCampaignSetting.AdOptimizedBusinessProfileSetting
    business_name: str
    business_profile_location: str
    def __init__(self, resource_name: _Optional[str] = ..., campaign: _Optional[str] = ..., phone_number: _Optional[_Union[SmartCampaignSetting.PhoneNumber, _Mapping]] = ..., advertising_language_code: _Optional[str] = ..., final_url: _Optional[str] = ..., ad_optimized_business_profile_setting: _Optional[_Union[SmartCampaignSetting.AdOptimizedBusinessProfileSetting, _Mapping]] = ..., business_name: _Optional[str] = ..., business_profile_location: _Optional[str] = ...) -> None: ...
