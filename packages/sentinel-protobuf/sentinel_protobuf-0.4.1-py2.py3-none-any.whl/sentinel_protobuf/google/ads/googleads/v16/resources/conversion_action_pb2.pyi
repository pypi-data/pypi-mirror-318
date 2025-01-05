from google.ads.googleads.v16.common import tag_snippet_pb2 as _tag_snippet_pb2
from google.ads.googleads.v16.enums import attribution_model_pb2 as _attribution_model_pb2
from google.ads.googleads.v16.enums import conversion_action_category_pb2 as _conversion_action_category_pb2
from google.ads.googleads.v16.enums import conversion_action_counting_type_pb2 as _conversion_action_counting_type_pb2
from google.ads.googleads.v16.enums import conversion_action_status_pb2 as _conversion_action_status_pb2
from google.ads.googleads.v16.enums import conversion_action_type_pb2 as _conversion_action_type_pb2
from google.ads.googleads.v16.enums import conversion_origin_pb2 as _conversion_origin_pb2
from google.ads.googleads.v16.enums import data_driven_model_status_pb2 as _data_driven_model_status_pb2
from google.ads.googleads.v16.enums import mobile_app_vendor_pb2 as _mobile_app_vendor_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConversionAction(_message.Message):
    __slots__ = ("resource_name", "id", "name", "status", "type", "origin", "primary_for_goal", "category", "owner_customer", "include_in_conversions_metric", "click_through_lookback_window_days", "view_through_lookback_window_days", "value_settings", "counting_type", "attribution_model_settings", "tag_snippets", "phone_call_duration_seconds", "app_id", "mobile_app_vendor", "firebase_settings", "third_party_app_analytics_settings", "google_analytics_4_settings")
    class AttributionModelSettings(_message.Message):
        __slots__ = ("attribution_model", "data_driven_model_status")
        ATTRIBUTION_MODEL_FIELD_NUMBER: _ClassVar[int]
        DATA_DRIVEN_MODEL_STATUS_FIELD_NUMBER: _ClassVar[int]
        attribution_model: _attribution_model_pb2.AttributionModelEnum.AttributionModel
        data_driven_model_status: _data_driven_model_status_pb2.DataDrivenModelStatusEnum.DataDrivenModelStatus
        def __init__(self, attribution_model: _Optional[_Union[_attribution_model_pb2.AttributionModelEnum.AttributionModel, str]] = ..., data_driven_model_status: _Optional[_Union[_data_driven_model_status_pb2.DataDrivenModelStatusEnum.DataDrivenModelStatus, str]] = ...) -> None: ...
    class ValueSettings(_message.Message):
        __slots__ = ("default_value", "default_currency_code", "always_use_default_value")
        DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
        ALWAYS_USE_DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        default_value: float
        default_currency_code: str
        always_use_default_value: bool
        def __init__(self, default_value: _Optional[float] = ..., default_currency_code: _Optional[str] = ..., always_use_default_value: bool = ...) -> None: ...
    class ThirdPartyAppAnalyticsSettings(_message.Message):
        __slots__ = ("event_name", "provider_name")
        EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
        PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
        event_name: str
        provider_name: str
        def __init__(self, event_name: _Optional[str] = ..., provider_name: _Optional[str] = ...) -> None: ...
    class FirebaseSettings(_message.Message):
        __slots__ = ("event_name", "project_id", "property_id", "property_name")
        EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
        PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
        PROPERTY_ID_FIELD_NUMBER: _ClassVar[int]
        PROPERTY_NAME_FIELD_NUMBER: _ClassVar[int]
        event_name: str
        project_id: str
        property_id: int
        property_name: str
        def __init__(self, event_name: _Optional[str] = ..., project_id: _Optional[str] = ..., property_id: _Optional[int] = ..., property_name: _Optional[str] = ...) -> None: ...
    class GoogleAnalytics4Settings(_message.Message):
        __slots__ = ("event_name", "property_name", "property_id")
        EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
        PROPERTY_NAME_FIELD_NUMBER: _ClassVar[int]
        PROPERTY_ID_FIELD_NUMBER: _ClassVar[int]
        event_name: str
        property_name: str
        property_id: int
        def __init__(self, event_name: _Optional[str] = ..., property_name: _Optional[str] = ..., property_id: _Optional[int] = ...) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_FOR_GOAL_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    OWNER_CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_IN_CONVERSIONS_METRIC_FIELD_NUMBER: _ClassVar[int]
    CLICK_THROUGH_LOOKBACK_WINDOW_DAYS_FIELD_NUMBER: _ClassVar[int]
    VIEW_THROUGH_LOOKBACK_WINDOW_DAYS_FIELD_NUMBER: _ClassVar[int]
    VALUE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    COUNTING_TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTION_MODEL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TAG_SNIPPETS_FIELD_NUMBER: _ClassVar[int]
    PHONE_CALL_DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    MOBILE_APP_VENDOR_FIELD_NUMBER: _ClassVar[int]
    FIREBASE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    THIRD_PARTY_APP_ANALYTICS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_ANALYTICS_4_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    status: _conversion_action_status_pb2.ConversionActionStatusEnum.ConversionActionStatus
    type: _conversion_action_type_pb2.ConversionActionTypeEnum.ConversionActionType
    origin: _conversion_origin_pb2.ConversionOriginEnum.ConversionOrigin
    primary_for_goal: bool
    category: _conversion_action_category_pb2.ConversionActionCategoryEnum.ConversionActionCategory
    owner_customer: str
    include_in_conversions_metric: bool
    click_through_lookback_window_days: int
    view_through_lookback_window_days: int
    value_settings: ConversionAction.ValueSettings
    counting_type: _conversion_action_counting_type_pb2.ConversionActionCountingTypeEnum.ConversionActionCountingType
    attribution_model_settings: ConversionAction.AttributionModelSettings
    tag_snippets: _containers.RepeatedCompositeFieldContainer[_tag_snippet_pb2.TagSnippet]
    phone_call_duration_seconds: int
    app_id: str
    mobile_app_vendor: _mobile_app_vendor_pb2.MobileAppVendorEnum.MobileAppVendor
    firebase_settings: ConversionAction.FirebaseSettings
    third_party_app_analytics_settings: ConversionAction.ThirdPartyAppAnalyticsSettings
    google_analytics_4_settings: ConversionAction.GoogleAnalytics4Settings
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., status: _Optional[_Union[_conversion_action_status_pb2.ConversionActionStatusEnum.ConversionActionStatus, str]] = ..., type: _Optional[_Union[_conversion_action_type_pb2.ConversionActionTypeEnum.ConversionActionType, str]] = ..., origin: _Optional[_Union[_conversion_origin_pb2.ConversionOriginEnum.ConversionOrigin, str]] = ..., primary_for_goal: bool = ..., category: _Optional[_Union[_conversion_action_category_pb2.ConversionActionCategoryEnum.ConversionActionCategory, str]] = ..., owner_customer: _Optional[str] = ..., include_in_conversions_metric: bool = ..., click_through_lookback_window_days: _Optional[int] = ..., view_through_lookback_window_days: _Optional[int] = ..., value_settings: _Optional[_Union[ConversionAction.ValueSettings, _Mapping]] = ..., counting_type: _Optional[_Union[_conversion_action_counting_type_pb2.ConversionActionCountingTypeEnum.ConversionActionCountingType, str]] = ..., attribution_model_settings: _Optional[_Union[ConversionAction.AttributionModelSettings, _Mapping]] = ..., tag_snippets: _Optional[_Iterable[_Union[_tag_snippet_pb2.TagSnippet, _Mapping]]] = ..., phone_call_duration_seconds: _Optional[int] = ..., app_id: _Optional[str] = ..., mobile_app_vendor: _Optional[_Union[_mobile_app_vendor_pb2.MobileAppVendorEnum.MobileAppVendor, str]] = ..., firebase_settings: _Optional[_Union[ConversionAction.FirebaseSettings, _Mapping]] = ..., third_party_app_analytics_settings: _Optional[_Union[ConversionAction.ThirdPartyAppAnalyticsSettings, _Mapping]] = ..., google_analytics_4_settings: _Optional[_Union[ConversionAction.GoogleAnalytics4Settings, _Mapping]] = ...) -> None: ...
