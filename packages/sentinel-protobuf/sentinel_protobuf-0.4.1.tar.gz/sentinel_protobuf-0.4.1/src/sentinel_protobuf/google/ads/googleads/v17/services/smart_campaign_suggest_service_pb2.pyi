from google.ads.googleads.v17.common import ad_type_infos_pb2 as _ad_type_infos_pb2
from google.ads.googleads.v17.common import criteria_pb2 as _criteria_pb2
from google.ads.googleads.v17.resources import keyword_theme_constant_pb2 as _keyword_theme_constant_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SuggestSmartCampaignBudgetOptionsRequest(_message.Message):
    __slots__ = ("customer_id", "campaign", "suggestion_info")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_INFO_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    campaign: str
    suggestion_info: SmartCampaignSuggestionInfo
    def __init__(self, customer_id: _Optional[str] = ..., campaign: _Optional[str] = ..., suggestion_info: _Optional[_Union[SmartCampaignSuggestionInfo, _Mapping]] = ...) -> None: ...

class SmartCampaignSuggestionInfo(_message.Message):
    __slots__ = ("final_url", "language_code", "ad_schedules", "keyword_themes", "business_context", "business_profile_location", "location_list", "proximity")
    class LocationList(_message.Message):
        __slots__ = ("locations",)
        LOCATIONS_FIELD_NUMBER: _ClassVar[int]
        locations: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.LocationInfo]
        def __init__(self, locations: _Optional[_Iterable[_Union[_criteria_pb2.LocationInfo, _Mapping]]] = ...) -> None: ...
    class BusinessContext(_message.Message):
        __slots__ = ("business_name",)
        BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
        business_name: str
        def __init__(self, business_name: _Optional[str] = ...) -> None: ...
    FINAL_URL_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    AD_SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_THEMES_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_PROFILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_LIST_FIELD_NUMBER: _ClassVar[int]
    PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    final_url: str
    language_code: str
    ad_schedules: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.AdScheduleInfo]
    keyword_themes: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.KeywordThemeInfo]
    business_context: SmartCampaignSuggestionInfo.BusinessContext
    business_profile_location: str
    location_list: SmartCampaignSuggestionInfo.LocationList
    proximity: _criteria_pb2.ProximityInfo
    def __init__(self, final_url: _Optional[str] = ..., language_code: _Optional[str] = ..., ad_schedules: _Optional[_Iterable[_Union[_criteria_pb2.AdScheduleInfo, _Mapping]]] = ..., keyword_themes: _Optional[_Iterable[_Union[_criteria_pb2.KeywordThemeInfo, _Mapping]]] = ..., business_context: _Optional[_Union[SmartCampaignSuggestionInfo.BusinessContext, _Mapping]] = ..., business_profile_location: _Optional[str] = ..., location_list: _Optional[_Union[SmartCampaignSuggestionInfo.LocationList, _Mapping]] = ..., proximity: _Optional[_Union[_criteria_pb2.ProximityInfo, _Mapping]] = ...) -> None: ...

class SuggestSmartCampaignBudgetOptionsResponse(_message.Message):
    __slots__ = ("low", "recommended", "high")
    class Metrics(_message.Message):
        __slots__ = ("min_daily_clicks", "max_daily_clicks")
        MIN_DAILY_CLICKS_FIELD_NUMBER: _ClassVar[int]
        MAX_DAILY_CLICKS_FIELD_NUMBER: _ClassVar[int]
        min_daily_clicks: int
        max_daily_clicks: int
        def __init__(self, min_daily_clicks: _Optional[int] = ..., max_daily_clicks: _Optional[int] = ...) -> None: ...
    class BudgetOption(_message.Message):
        __slots__ = ("daily_amount_micros", "metrics")
        DAILY_AMOUNT_MICROS_FIELD_NUMBER: _ClassVar[int]
        METRICS_FIELD_NUMBER: _ClassVar[int]
        daily_amount_micros: int
        metrics: SuggestSmartCampaignBudgetOptionsResponse.Metrics
        def __init__(self, daily_amount_micros: _Optional[int] = ..., metrics: _Optional[_Union[SuggestSmartCampaignBudgetOptionsResponse.Metrics, _Mapping]] = ...) -> None: ...
    LOW_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    low: SuggestSmartCampaignBudgetOptionsResponse.BudgetOption
    recommended: SuggestSmartCampaignBudgetOptionsResponse.BudgetOption
    high: SuggestSmartCampaignBudgetOptionsResponse.BudgetOption
    def __init__(self, low: _Optional[_Union[SuggestSmartCampaignBudgetOptionsResponse.BudgetOption, _Mapping]] = ..., recommended: _Optional[_Union[SuggestSmartCampaignBudgetOptionsResponse.BudgetOption, _Mapping]] = ..., high: _Optional[_Union[SuggestSmartCampaignBudgetOptionsResponse.BudgetOption, _Mapping]] = ...) -> None: ...

class SuggestSmartCampaignAdRequest(_message.Message):
    __slots__ = ("customer_id", "suggestion_info")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_INFO_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    suggestion_info: SmartCampaignSuggestionInfo
    def __init__(self, customer_id: _Optional[str] = ..., suggestion_info: _Optional[_Union[SmartCampaignSuggestionInfo, _Mapping]] = ...) -> None: ...

class SuggestSmartCampaignAdResponse(_message.Message):
    __slots__ = ("ad_info",)
    AD_INFO_FIELD_NUMBER: _ClassVar[int]
    ad_info: _ad_type_infos_pb2.SmartCampaignAdInfo
    def __init__(self, ad_info: _Optional[_Union[_ad_type_infos_pb2.SmartCampaignAdInfo, _Mapping]] = ...) -> None: ...

class SuggestKeywordThemesRequest(_message.Message):
    __slots__ = ("customer_id", "suggestion_info")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_INFO_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    suggestion_info: SmartCampaignSuggestionInfo
    def __init__(self, customer_id: _Optional[str] = ..., suggestion_info: _Optional[_Union[SmartCampaignSuggestionInfo, _Mapping]] = ...) -> None: ...

class SuggestKeywordThemesResponse(_message.Message):
    __slots__ = ("keyword_themes",)
    class KeywordTheme(_message.Message):
        __slots__ = ("keyword_theme_constant", "free_form_keyword_theme")
        KEYWORD_THEME_CONSTANT_FIELD_NUMBER: _ClassVar[int]
        FREE_FORM_KEYWORD_THEME_FIELD_NUMBER: _ClassVar[int]
        keyword_theme_constant: _keyword_theme_constant_pb2.KeywordThemeConstant
        free_form_keyword_theme: str
        def __init__(self, keyword_theme_constant: _Optional[_Union[_keyword_theme_constant_pb2.KeywordThemeConstant, _Mapping]] = ..., free_form_keyword_theme: _Optional[str] = ...) -> None: ...
    KEYWORD_THEMES_FIELD_NUMBER: _ClassVar[int]
    keyword_themes: _containers.RepeatedCompositeFieldContainer[SuggestKeywordThemesResponse.KeywordTheme]
    def __init__(self, keyword_themes: _Optional[_Iterable[_Union[SuggestKeywordThemesResponse.KeywordTheme, _Mapping]]] = ...) -> None: ...
