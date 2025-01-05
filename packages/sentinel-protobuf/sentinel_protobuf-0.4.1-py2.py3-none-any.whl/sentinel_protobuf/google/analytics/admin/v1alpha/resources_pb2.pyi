from google.analytics.admin.v1alpha import audience_pb2 as _audience_pb2
from google.analytics.admin.v1alpha import channel_group_pb2 as _channel_group_pb2
from google.analytics.admin.v1alpha import event_create_and_edit_pb2 as _event_create_and_edit_pb2
from google.analytics.admin.v1alpha import expanded_data_set_pb2 as _expanded_data_set_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IndustryCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INDUSTRY_CATEGORY_UNSPECIFIED: _ClassVar[IndustryCategory]
    AUTOMOTIVE: _ClassVar[IndustryCategory]
    BUSINESS_AND_INDUSTRIAL_MARKETS: _ClassVar[IndustryCategory]
    FINANCE: _ClassVar[IndustryCategory]
    HEALTHCARE: _ClassVar[IndustryCategory]
    TECHNOLOGY: _ClassVar[IndustryCategory]
    TRAVEL: _ClassVar[IndustryCategory]
    OTHER: _ClassVar[IndustryCategory]
    ARTS_AND_ENTERTAINMENT: _ClassVar[IndustryCategory]
    BEAUTY_AND_FITNESS: _ClassVar[IndustryCategory]
    BOOKS_AND_LITERATURE: _ClassVar[IndustryCategory]
    FOOD_AND_DRINK: _ClassVar[IndustryCategory]
    GAMES: _ClassVar[IndustryCategory]
    HOBBIES_AND_LEISURE: _ClassVar[IndustryCategory]
    HOME_AND_GARDEN: _ClassVar[IndustryCategory]
    INTERNET_AND_TELECOM: _ClassVar[IndustryCategory]
    LAW_AND_GOVERNMENT: _ClassVar[IndustryCategory]
    NEWS: _ClassVar[IndustryCategory]
    ONLINE_COMMUNITIES: _ClassVar[IndustryCategory]
    PEOPLE_AND_SOCIETY: _ClassVar[IndustryCategory]
    PETS_AND_ANIMALS: _ClassVar[IndustryCategory]
    REAL_ESTATE: _ClassVar[IndustryCategory]
    REFERENCE: _ClassVar[IndustryCategory]
    SCIENCE: _ClassVar[IndustryCategory]
    SPORTS: _ClassVar[IndustryCategory]
    JOBS_AND_EDUCATION: _ClassVar[IndustryCategory]
    SHOPPING: _ClassVar[IndustryCategory]

class ServiceLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVICE_LEVEL_UNSPECIFIED: _ClassVar[ServiceLevel]
    GOOGLE_ANALYTICS_STANDARD: _ClassVar[ServiceLevel]
    GOOGLE_ANALYTICS_360: _ClassVar[ServiceLevel]

class ActorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTOR_TYPE_UNSPECIFIED: _ClassVar[ActorType]
    USER: _ClassVar[ActorType]
    SYSTEM: _ClassVar[ActorType]
    SUPPORT: _ClassVar[ActorType]

class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTION_TYPE_UNSPECIFIED: _ClassVar[ActionType]
    CREATED: _ClassVar[ActionType]
    UPDATED: _ClassVar[ActionType]
    DELETED: _ClassVar[ActionType]

class ChangeHistoryResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHANGE_HISTORY_RESOURCE_TYPE_UNSPECIFIED: _ClassVar[ChangeHistoryResourceType]
    ACCOUNT: _ClassVar[ChangeHistoryResourceType]
    PROPERTY: _ClassVar[ChangeHistoryResourceType]
    FIREBASE_LINK: _ClassVar[ChangeHistoryResourceType]
    GOOGLE_ADS_LINK: _ClassVar[ChangeHistoryResourceType]
    GOOGLE_SIGNALS_SETTINGS: _ClassVar[ChangeHistoryResourceType]
    CONVERSION_EVENT: _ClassVar[ChangeHistoryResourceType]
    MEASUREMENT_PROTOCOL_SECRET: _ClassVar[ChangeHistoryResourceType]
    CUSTOM_DIMENSION: _ClassVar[ChangeHistoryResourceType]
    CUSTOM_METRIC: _ClassVar[ChangeHistoryResourceType]
    DATA_RETENTION_SETTINGS: _ClassVar[ChangeHistoryResourceType]
    DISPLAY_VIDEO_360_ADVERTISER_LINK: _ClassVar[ChangeHistoryResourceType]
    DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSAL: _ClassVar[ChangeHistoryResourceType]
    SEARCH_ADS_360_LINK: _ClassVar[ChangeHistoryResourceType]
    DATA_STREAM: _ClassVar[ChangeHistoryResourceType]
    ATTRIBUTION_SETTINGS: _ClassVar[ChangeHistoryResourceType]
    EXPANDED_DATA_SET: _ClassVar[ChangeHistoryResourceType]
    CHANNEL_GROUP: _ClassVar[ChangeHistoryResourceType]
    BIGQUERY_LINK: _ClassVar[ChangeHistoryResourceType]
    ENHANCED_MEASUREMENT_SETTINGS: _ClassVar[ChangeHistoryResourceType]
    DATA_REDACTION_SETTINGS: _ClassVar[ChangeHistoryResourceType]
    SKADNETWORK_CONVERSION_VALUE_SCHEMA: _ClassVar[ChangeHistoryResourceType]
    ADSENSE_LINK: _ClassVar[ChangeHistoryResourceType]
    AUDIENCE: _ClassVar[ChangeHistoryResourceType]
    EVENT_CREATE_RULE: _ClassVar[ChangeHistoryResourceType]
    CALCULATED_METRIC: _ClassVar[ChangeHistoryResourceType]

class GoogleSignalsState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GOOGLE_SIGNALS_STATE_UNSPECIFIED: _ClassVar[GoogleSignalsState]
    GOOGLE_SIGNALS_ENABLED: _ClassVar[GoogleSignalsState]
    GOOGLE_SIGNALS_DISABLED: _ClassVar[GoogleSignalsState]

class GoogleSignalsConsent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GOOGLE_SIGNALS_CONSENT_UNSPECIFIED: _ClassVar[GoogleSignalsConsent]
    GOOGLE_SIGNALS_CONSENT_CONSENTED: _ClassVar[GoogleSignalsConsent]
    GOOGLE_SIGNALS_CONSENT_NOT_CONSENTED: _ClassVar[GoogleSignalsConsent]

class LinkProposalInitiatingProduct(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LINK_PROPOSAL_INITIATING_PRODUCT_UNSPECIFIED: _ClassVar[LinkProposalInitiatingProduct]
    GOOGLE_ANALYTICS: _ClassVar[LinkProposalInitiatingProduct]
    LINKED_PRODUCT: _ClassVar[LinkProposalInitiatingProduct]

class LinkProposalState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LINK_PROPOSAL_STATE_UNSPECIFIED: _ClassVar[LinkProposalState]
    AWAITING_REVIEW_FROM_GOOGLE_ANALYTICS: _ClassVar[LinkProposalState]
    AWAITING_REVIEW_FROM_LINKED_PRODUCT: _ClassVar[LinkProposalState]
    WITHDRAWN: _ClassVar[LinkProposalState]
    DECLINED: _ClassVar[LinkProposalState]
    EXPIRED: _ClassVar[LinkProposalState]
    OBSOLETE: _ClassVar[LinkProposalState]

class PropertyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROPERTY_TYPE_UNSPECIFIED: _ClassVar[PropertyType]
    PROPERTY_TYPE_ORDINARY: _ClassVar[PropertyType]
    PROPERTY_TYPE_SUBPROPERTY: _ClassVar[PropertyType]
    PROPERTY_TYPE_ROLLUP: _ClassVar[PropertyType]

class CoarseValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COARSE_VALUE_UNSPECIFIED: _ClassVar[CoarseValue]
    COARSE_VALUE_LOW: _ClassVar[CoarseValue]
    COARSE_VALUE_MEDIUM: _ClassVar[CoarseValue]
    COARSE_VALUE_HIGH: _ClassVar[CoarseValue]
INDUSTRY_CATEGORY_UNSPECIFIED: IndustryCategory
AUTOMOTIVE: IndustryCategory
BUSINESS_AND_INDUSTRIAL_MARKETS: IndustryCategory
FINANCE: IndustryCategory
HEALTHCARE: IndustryCategory
TECHNOLOGY: IndustryCategory
TRAVEL: IndustryCategory
OTHER: IndustryCategory
ARTS_AND_ENTERTAINMENT: IndustryCategory
BEAUTY_AND_FITNESS: IndustryCategory
BOOKS_AND_LITERATURE: IndustryCategory
FOOD_AND_DRINK: IndustryCategory
GAMES: IndustryCategory
HOBBIES_AND_LEISURE: IndustryCategory
HOME_AND_GARDEN: IndustryCategory
INTERNET_AND_TELECOM: IndustryCategory
LAW_AND_GOVERNMENT: IndustryCategory
NEWS: IndustryCategory
ONLINE_COMMUNITIES: IndustryCategory
PEOPLE_AND_SOCIETY: IndustryCategory
PETS_AND_ANIMALS: IndustryCategory
REAL_ESTATE: IndustryCategory
REFERENCE: IndustryCategory
SCIENCE: IndustryCategory
SPORTS: IndustryCategory
JOBS_AND_EDUCATION: IndustryCategory
SHOPPING: IndustryCategory
SERVICE_LEVEL_UNSPECIFIED: ServiceLevel
GOOGLE_ANALYTICS_STANDARD: ServiceLevel
GOOGLE_ANALYTICS_360: ServiceLevel
ACTOR_TYPE_UNSPECIFIED: ActorType
USER: ActorType
SYSTEM: ActorType
SUPPORT: ActorType
ACTION_TYPE_UNSPECIFIED: ActionType
CREATED: ActionType
UPDATED: ActionType
DELETED: ActionType
CHANGE_HISTORY_RESOURCE_TYPE_UNSPECIFIED: ChangeHistoryResourceType
ACCOUNT: ChangeHistoryResourceType
PROPERTY: ChangeHistoryResourceType
FIREBASE_LINK: ChangeHistoryResourceType
GOOGLE_ADS_LINK: ChangeHistoryResourceType
GOOGLE_SIGNALS_SETTINGS: ChangeHistoryResourceType
CONVERSION_EVENT: ChangeHistoryResourceType
MEASUREMENT_PROTOCOL_SECRET: ChangeHistoryResourceType
CUSTOM_DIMENSION: ChangeHistoryResourceType
CUSTOM_METRIC: ChangeHistoryResourceType
DATA_RETENTION_SETTINGS: ChangeHistoryResourceType
DISPLAY_VIDEO_360_ADVERTISER_LINK: ChangeHistoryResourceType
DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSAL: ChangeHistoryResourceType
SEARCH_ADS_360_LINK: ChangeHistoryResourceType
DATA_STREAM: ChangeHistoryResourceType
ATTRIBUTION_SETTINGS: ChangeHistoryResourceType
EXPANDED_DATA_SET: ChangeHistoryResourceType
CHANNEL_GROUP: ChangeHistoryResourceType
BIGQUERY_LINK: ChangeHistoryResourceType
ENHANCED_MEASUREMENT_SETTINGS: ChangeHistoryResourceType
DATA_REDACTION_SETTINGS: ChangeHistoryResourceType
SKADNETWORK_CONVERSION_VALUE_SCHEMA: ChangeHistoryResourceType
ADSENSE_LINK: ChangeHistoryResourceType
AUDIENCE: ChangeHistoryResourceType
EVENT_CREATE_RULE: ChangeHistoryResourceType
CALCULATED_METRIC: ChangeHistoryResourceType
GOOGLE_SIGNALS_STATE_UNSPECIFIED: GoogleSignalsState
GOOGLE_SIGNALS_ENABLED: GoogleSignalsState
GOOGLE_SIGNALS_DISABLED: GoogleSignalsState
GOOGLE_SIGNALS_CONSENT_UNSPECIFIED: GoogleSignalsConsent
GOOGLE_SIGNALS_CONSENT_CONSENTED: GoogleSignalsConsent
GOOGLE_SIGNALS_CONSENT_NOT_CONSENTED: GoogleSignalsConsent
LINK_PROPOSAL_INITIATING_PRODUCT_UNSPECIFIED: LinkProposalInitiatingProduct
GOOGLE_ANALYTICS: LinkProposalInitiatingProduct
LINKED_PRODUCT: LinkProposalInitiatingProduct
LINK_PROPOSAL_STATE_UNSPECIFIED: LinkProposalState
AWAITING_REVIEW_FROM_GOOGLE_ANALYTICS: LinkProposalState
AWAITING_REVIEW_FROM_LINKED_PRODUCT: LinkProposalState
WITHDRAWN: LinkProposalState
DECLINED: LinkProposalState
EXPIRED: LinkProposalState
OBSOLETE: LinkProposalState
PROPERTY_TYPE_UNSPECIFIED: PropertyType
PROPERTY_TYPE_ORDINARY: PropertyType
PROPERTY_TYPE_SUBPROPERTY: PropertyType
PROPERTY_TYPE_ROLLUP: PropertyType
COARSE_VALUE_UNSPECIFIED: CoarseValue
COARSE_VALUE_LOW: CoarseValue
COARSE_VALUE_MEDIUM: CoarseValue
COARSE_VALUE_HIGH: CoarseValue

class Account(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "display_name", "region_code", "deleted", "gmp_organization")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    GMP_ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    display_name: str
    region_code: str
    deleted: bool
    gmp_organization: str
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., display_name: _Optional[str] = ..., region_code: _Optional[str] = ..., deleted: bool = ..., gmp_organization: _Optional[str] = ...) -> None: ...

class Property(_message.Message):
    __slots__ = ("name", "property_type", "create_time", "update_time", "parent", "display_name", "industry_category", "time_zone", "currency_code", "service_level", "delete_time", "expire_time", "account")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    INDUSTRY_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    property_type: PropertyType
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    parent: str
    display_name: str
    industry_category: IndustryCategory
    time_zone: str
    currency_code: str
    service_level: ServiceLevel
    delete_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    account: str
    def __init__(self, name: _Optional[str] = ..., property_type: _Optional[_Union[PropertyType, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., parent: _Optional[str] = ..., display_name: _Optional[str] = ..., industry_category: _Optional[_Union[IndustryCategory, str]] = ..., time_zone: _Optional[str] = ..., currency_code: _Optional[str] = ..., service_level: _Optional[_Union[ServiceLevel, str]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., account: _Optional[str] = ...) -> None: ...

class DataStream(_message.Message):
    __slots__ = ("web_stream_data", "android_app_stream_data", "ios_app_stream_data", "name", "type", "display_name", "create_time", "update_time")
    class DataStreamType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_STREAM_TYPE_UNSPECIFIED: _ClassVar[DataStream.DataStreamType]
        WEB_DATA_STREAM: _ClassVar[DataStream.DataStreamType]
        ANDROID_APP_DATA_STREAM: _ClassVar[DataStream.DataStreamType]
        IOS_APP_DATA_STREAM: _ClassVar[DataStream.DataStreamType]
    DATA_STREAM_TYPE_UNSPECIFIED: DataStream.DataStreamType
    WEB_DATA_STREAM: DataStream.DataStreamType
    ANDROID_APP_DATA_STREAM: DataStream.DataStreamType
    IOS_APP_DATA_STREAM: DataStream.DataStreamType
    class WebStreamData(_message.Message):
        __slots__ = ("measurement_id", "firebase_app_id", "default_uri")
        MEASUREMENT_ID_FIELD_NUMBER: _ClassVar[int]
        FIREBASE_APP_ID_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_URI_FIELD_NUMBER: _ClassVar[int]
        measurement_id: str
        firebase_app_id: str
        default_uri: str
        def __init__(self, measurement_id: _Optional[str] = ..., firebase_app_id: _Optional[str] = ..., default_uri: _Optional[str] = ...) -> None: ...
    class AndroidAppStreamData(_message.Message):
        __slots__ = ("firebase_app_id", "package_name")
        FIREBASE_APP_ID_FIELD_NUMBER: _ClassVar[int]
        PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
        firebase_app_id: str
        package_name: str
        def __init__(self, firebase_app_id: _Optional[str] = ..., package_name: _Optional[str] = ...) -> None: ...
    class IosAppStreamData(_message.Message):
        __slots__ = ("firebase_app_id", "bundle_id")
        FIREBASE_APP_ID_FIELD_NUMBER: _ClassVar[int]
        BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
        firebase_app_id: str
        bundle_id: str
        def __init__(self, firebase_app_id: _Optional[str] = ..., bundle_id: _Optional[str] = ...) -> None: ...
    WEB_STREAM_DATA_FIELD_NUMBER: _ClassVar[int]
    ANDROID_APP_STREAM_DATA_FIELD_NUMBER: _ClassVar[int]
    IOS_APP_STREAM_DATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    web_stream_data: DataStream.WebStreamData
    android_app_stream_data: DataStream.AndroidAppStreamData
    ios_app_stream_data: DataStream.IosAppStreamData
    name: str
    type: DataStream.DataStreamType
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, web_stream_data: _Optional[_Union[DataStream.WebStreamData, _Mapping]] = ..., android_app_stream_data: _Optional[_Union[DataStream.AndroidAppStreamData, _Mapping]] = ..., ios_app_stream_data: _Optional[_Union[DataStream.IosAppStreamData, _Mapping]] = ..., name: _Optional[str] = ..., type: _Optional[_Union[DataStream.DataStreamType, str]] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class FirebaseLink(_message.Message):
    __slots__ = ("name", "project", "create_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    project: str
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., project: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GlobalSiteTag(_message.Message):
    __slots__ = ("name", "snippet")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SNIPPET_FIELD_NUMBER: _ClassVar[int]
    name: str
    snippet: str
    def __init__(self, name: _Optional[str] = ..., snippet: _Optional[str] = ...) -> None: ...

class GoogleAdsLink(_message.Message):
    __slots__ = ("name", "customer_id", "can_manage_clients", "ads_personalization_enabled", "create_time", "update_time", "creator_email_address")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CAN_MANAGE_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    ADS_PERSONALIZATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATOR_EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    customer_id: str
    can_manage_clients: bool
    ads_personalization_enabled: _wrappers_pb2.BoolValue
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    creator_email_address: str
    def __init__(self, name: _Optional[str] = ..., customer_id: _Optional[str] = ..., can_manage_clients: bool = ..., ads_personalization_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., creator_email_address: _Optional[str] = ...) -> None: ...

class DataSharingSettings(_message.Message):
    __slots__ = ("name", "sharing_with_google_support_enabled", "sharing_with_google_assigned_sales_enabled", "sharing_with_google_any_sales_enabled", "sharing_with_google_products_enabled", "sharing_with_others_enabled")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SHARING_WITH_GOOGLE_SUPPORT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SHARING_WITH_GOOGLE_ASSIGNED_SALES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SHARING_WITH_GOOGLE_ANY_SALES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SHARING_WITH_GOOGLE_PRODUCTS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SHARING_WITH_OTHERS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    sharing_with_google_support_enabled: bool
    sharing_with_google_assigned_sales_enabled: bool
    sharing_with_google_any_sales_enabled: bool
    sharing_with_google_products_enabled: bool
    sharing_with_others_enabled: bool
    def __init__(self, name: _Optional[str] = ..., sharing_with_google_support_enabled: bool = ..., sharing_with_google_assigned_sales_enabled: bool = ..., sharing_with_google_any_sales_enabled: bool = ..., sharing_with_google_products_enabled: bool = ..., sharing_with_others_enabled: bool = ...) -> None: ...

class AccountSummary(_message.Message):
    __slots__ = ("name", "account", "display_name", "property_summaries")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    account: str
    display_name: str
    property_summaries: _containers.RepeatedCompositeFieldContainer[PropertySummary]
    def __init__(self, name: _Optional[str] = ..., account: _Optional[str] = ..., display_name: _Optional[str] = ..., property_summaries: _Optional[_Iterable[_Union[PropertySummary, _Mapping]]] = ...) -> None: ...

class PropertySummary(_message.Message):
    __slots__ = ("property", "display_name", "property_type", "parent")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    property: str
    display_name: str
    property_type: PropertyType
    parent: str
    def __init__(self, property: _Optional[str] = ..., display_name: _Optional[str] = ..., property_type: _Optional[_Union[PropertyType, str]] = ..., parent: _Optional[str] = ...) -> None: ...

class MeasurementProtocolSecret(_message.Message):
    __slots__ = ("name", "display_name", "secret_value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SECRET_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    secret_value: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., secret_value: _Optional[str] = ...) -> None: ...

class SKAdNetworkConversionValueSchema(_message.Message):
    __slots__ = ("name", "postback_window_one", "postback_window_two", "postback_window_three", "apply_conversion_values")
    NAME_FIELD_NUMBER: _ClassVar[int]
    POSTBACK_WINDOW_ONE_FIELD_NUMBER: _ClassVar[int]
    POSTBACK_WINDOW_TWO_FIELD_NUMBER: _ClassVar[int]
    POSTBACK_WINDOW_THREE_FIELD_NUMBER: _ClassVar[int]
    APPLY_CONVERSION_VALUES_FIELD_NUMBER: _ClassVar[int]
    name: str
    postback_window_one: PostbackWindow
    postback_window_two: PostbackWindow
    postback_window_three: PostbackWindow
    apply_conversion_values: bool
    def __init__(self, name: _Optional[str] = ..., postback_window_one: _Optional[_Union[PostbackWindow, _Mapping]] = ..., postback_window_two: _Optional[_Union[PostbackWindow, _Mapping]] = ..., postback_window_three: _Optional[_Union[PostbackWindow, _Mapping]] = ..., apply_conversion_values: bool = ...) -> None: ...

class PostbackWindow(_message.Message):
    __slots__ = ("conversion_values", "postback_window_settings_enabled")
    CONVERSION_VALUES_FIELD_NUMBER: _ClassVar[int]
    POSTBACK_WINDOW_SETTINGS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    conversion_values: _containers.RepeatedCompositeFieldContainer[ConversionValues]
    postback_window_settings_enabled: bool
    def __init__(self, conversion_values: _Optional[_Iterable[_Union[ConversionValues, _Mapping]]] = ..., postback_window_settings_enabled: bool = ...) -> None: ...

class ConversionValues(_message.Message):
    __slots__ = ("display_name", "fine_value", "coarse_value", "event_mappings", "lock_enabled")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    FINE_VALUE_FIELD_NUMBER: _ClassVar[int]
    COARSE_VALUE_FIELD_NUMBER: _ClassVar[int]
    EVENT_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    LOCK_ENABLED_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    fine_value: int
    coarse_value: CoarseValue
    event_mappings: _containers.RepeatedCompositeFieldContainer[EventMapping]
    lock_enabled: bool
    def __init__(self, display_name: _Optional[str] = ..., fine_value: _Optional[int] = ..., coarse_value: _Optional[_Union[CoarseValue, str]] = ..., event_mappings: _Optional[_Iterable[_Union[EventMapping, _Mapping]]] = ..., lock_enabled: bool = ...) -> None: ...

class EventMapping(_message.Message):
    __slots__ = ("event_name", "min_event_count", "max_event_count", "min_event_value", "max_event_value")
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    MIN_EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    MIN_EVENT_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_EVENT_VALUE_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    min_event_count: int
    max_event_count: int
    min_event_value: float
    max_event_value: float
    def __init__(self, event_name: _Optional[str] = ..., min_event_count: _Optional[int] = ..., max_event_count: _Optional[int] = ..., min_event_value: _Optional[float] = ..., max_event_value: _Optional[float] = ...) -> None: ...

class ChangeHistoryEvent(_message.Message):
    __slots__ = ("id", "change_time", "actor_type", "user_actor_email", "changes_filtered", "changes")
    ID_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TIME_FIELD_NUMBER: _ClassVar[int]
    ACTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ACTOR_EMAIL_FIELD_NUMBER: _ClassVar[int]
    CHANGES_FILTERED_FIELD_NUMBER: _ClassVar[int]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    id: str
    change_time: _timestamp_pb2.Timestamp
    actor_type: ActorType
    user_actor_email: str
    changes_filtered: bool
    changes: _containers.RepeatedCompositeFieldContainer[ChangeHistoryChange]
    def __init__(self, id: _Optional[str] = ..., change_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., actor_type: _Optional[_Union[ActorType, str]] = ..., user_actor_email: _Optional[str] = ..., changes_filtered: bool = ..., changes: _Optional[_Iterable[_Union[ChangeHistoryChange, _Mapping]]] = ...) -> None: ...

class ChangeHistoryChange(_message.Message):
    __slots__ = ("resource", "action", "resource_before_change", "resource_after_change")
    class ChangeHistoryResource(_message.Message):
        __slots__ = ("account", "property", "firebase_link", "google_ads_link", "google_signals_settings", "display_video_360_advertiser_link", "display_video_360_advertiser_link_proposal", "conversion_event", "measurement_protocol_secret", "custom_dimension", "custom_metric", "data_retention_settings", "search_ads_360_link", "data_stream", "attribution_settings", "expanded_data_set", "channel_group", "bigquery_link", "enhanced_measurement_settings", "data_redaction_settings", "skadnetwork_conversion_value_schema", "adsense_link", "audience", "event_create_rule", "calculated_metric")
        ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        PROPERTY_FIELD_NUMBER: _ClassVar[int]
        FIREBASE_LINK_FIELD_NUMBER: _ClassVar[int]
        GOOGLE_ADS_LINK_FIELD_NUMBER: _ClassVar[int]
        GOOGLE_SIGNALS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_VIDEO_360_ADVERTISER_LINK_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
        CONVERSION_EVENT_FIELD_NUMBER: _ClassVar[int]
        MEASUREMENT_PROTOCOL_SECRET_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_DIMENSION_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_METRIC_FIELD_NUMBER: _ClassVar[int]
        DATA_RETENTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        SEARCH_ADS_360_LINK_FIELD_NUMBER: _ClassVar[int]
        DATA_STREAM_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        EXPANDED_DATA_SET_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_GROUP_FIELD_NUMBER: _ClassVar[int]
        BIGQUERY_LINK_FIELD_NUMBER: _ClassVar[int]
        ENHANCED_MEASUREMENT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        DATA_REDACTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        SKADNETWORK_CONVERSION_VALUE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        ADSENSE_LINK_FIELD_NUMBER: _ClassVar[int]
        AUDIENCE_FIELD_NUMBER: _ClassVar[int]
        EVENT_CREATE_RULE_FIELD_NUMBER: _ClassVar[int]
        CALCULATED_METRIC_FIELD_NUMBER: _ClassVar[int]
        account: Account
        property: Property
        firebase_link: FirebaseLink
        google_ads_link: GoogleAdsLink
        google_signals_settings: GoogleSignalsSettings
        display_video_360_advertiser_link: DisplayVideo360AdvertiserLink
        display_video_360_advertiser_link_proposal: DisplayVideo360AdvertiserLinkProposal
        conversion_event: ConversionEvent
        measurement_protocol_secret: MeasurementProtocolSecret
        custom_dimension: CustomDimension
        custom_metric: CustomMetric
        data_retention_settings: DataRetentionSettings
        search_ads_360_link: SearchAds360Link
        data_stream: DataStream
        attribution_settings: AttributionSettings
        expanded_data_set: _expanded_data_set_pb2.ExpandedDataSet
        channel_group: _channel_group_pb2.ChannelGroup
        bigquery_link: BigQueryLink
        enhanced_measurement_settings: EnhancedMeasurementSettings
        data_redaction_settings: DataRedactionSettings
        skadnetwork_conversion_value_schema: SKAdNetworkConversionValueSchema
        adsense_link: AdSenseLink
        audience: _audience_pb2.Audience
        event_create_rule: _event_create_and_edit_pb2.EventCreateRule
        calculated_metric: CalculatedMetric
        def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ..., property: _Optional[_Union[Property, _Mapping]] = ..., firebase_link: _Optional[_Union[FirebaseLink, _Mapping]] = ..., google_ads_link: _Optional[_Union[GoogleAdsLink, _Mapping]] = ..., google_signals_settings: _Optional[_Union[GoogleSignalsSettings, _Mapping]] = ..., display_video_360_advertiser_link: _Optional[_Union[DisplayVideo360AdvertiserLink, _Mapping]] = ..., display_video_360_advertiser_link_proposal: _Optional[_Union[DisplayVideo360AdvertiserLinkProposal, _Mapping]] = ..., conversion_event: _Optional[_Union[ConversionEvent, _Mapping]] = ..., measurement_protocol_secret: _Optional[_Union[MeasurementProtocolSecret, _Mapping]] = ..., custom_dimension: _Optional[_Union[CustomDimension, _Mapping]] = ..., custom_metric: _Optional[_Union[CustomMetric, _Mapping]] = ..., data_retention_settings: _Optional[_Union[DataRetentionSettings, _Mapping]] = ..., search_ads_360_link: _Optional[_Union[SearchAds360Link, _Mapping]] = ..., data_stream: _Optional[_Union[DataStream, _Mapping]] = ..., attribution_settings: _Optional[_Union[AttributionSettings, _Mapping]] = ..., expanded_data_set: _Optional[_Union[_expanded_data_set_pb2.ExpandedDataSet, _Mapping]] = ..., channel_group: _Optional[_Union[_channel_group_pb2.ChannelGroup, _Mapping]] = ..., bigquery_link: _Optional[_Union[BigQueryLink, _Mapping]] = ..., enhanced_measurement_settings: _Optional[_Union[EnhancedMeasurementSettings, _Mapping]] = ..., data_redaction_settings: _Optional[_Union[DataRedactionSettings, _Mapping]] = ..., skadnetwork_conversion_value_schema: _Optional[_Union[SKAdNetworkConversionValueSchema, _Mapping]] = ..., adsense_link: _Optional[_Union[AdSenseLink, _Mapping]] = ..., audience: _Optional[_Union[_audience_pb2.Audience, _Mapping]] = ..., event_create_rule: _Optional[_Union[_event_create_and_edit_pb2.EventCreateRule, _Mapping]] = ..., calculated_metric: _Optional[_Union[CalculatedMetric, _Mapping]] = ...) -> None: ...
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_BEFORE_CHANGE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_AFTER_CHANGE_FIELD_NUMBER: _ClassVar[int]
    resource: str
    action: ActionType
    resource_before_change: ChangeHistoryChange.ChangeHistoryResource
    resource_after_change: ChangeHistoryChange.ChangeHistoryResource
    def __init__(self, resource: _Optional[str] = ..., action: _Optional[_Union[ActionType, str]] = ..., resource_before_change: _Optional[_Union[ChangeHistoryChange.ChangeHistoryResource, _Mapping]] = ..., resource_after_change: _Optional[_Union[ChangeHistoryChange.ChangeHistoryResource, _Mapping]] = ...) -> None: ...

class DisplayVideo360AdvertiserLink(_message.Message):
    __slots__ = ("name", "advertiser_id", "advertiser_display_name", "ads_personalization_enabled", "campaign_data_sharing_enabled", "cost_data_sharing_enabled")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADVERTISER_ID_FIELD_NUMBER: _ClassVar[int]
    ADVERTISER_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ADS_PERSONALIZATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_DATA_SHARING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    COST_DATA_SHARING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    advertiser_id: str
    advertiser_display_name: str
    ads_personalization_enabled: _wrappers_pb2.BoolValue
    campaign_data_sharing_enabled: _wrappers_pb2.BoolValue
    cost_data_sharing_enabled: _wrappers_pb2.BoolValue
    def __init__(self, name: _Optional[str] = ..., advertiser_id: _Optional[str] = ..., advertiser_display_name: _Optional[str] = ..., ads_personalization_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., campaign_data_sharing_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., cost_data_sharing_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class DisplayVideo360AdvertiserLinkProposal(_message.Message):
    __slots__ = ("name", "advertiser_id", "link_proposal_status_details", "advertiser_display_name", "validation_email", "ads_personalization_enabled", "campaign_data_sharing_enabled", "cost_data_sharing_enabled")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADVERTISER_ID_FIELD_NUMBER: _ClassVar[int]
    LINK_PROPOSAL_STATUS_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ADVERTISER_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_EMAIL_FIELD_NUMBER: _ClassVar[int]
    ADS_PERSONALIZATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_DATA_SHARING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    COST_DATA_SHARING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    advertiser_id: str
    link_proposal_status_details: LinkProposalStatusDetails
    advertiser_display_name: str
    validation_email: str
    ads_personalization_enabled: _wrappers_pb2.BoolValue
    campaign_data_sharing_enabled: _wrappers_pb2.BoolValue
    cost_data_sharing_enabled: _wrappers_pb2.BoolValue
    def __init__(self, name: _Optional[str] = ..., advertiser_id: _Optional[str] = ..., link_proposal_status_details: _Optional[_Union[LinkProposalStatusDetails, _Mapping]] = ..., advertiser_display_name: _Optional[str] = ..., validation_email: _Optional[str] = ..., ads_personalization_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., campaign_data_sharing_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., cost_data_sharing_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class SearchAds360Link(_message.Message):
    __slots__ = ("name", "advertiser_id", "campaign_data_sharing_enabled", "cost_data_sharing_enabled", "advertiser_display_name", "ads_personalization_enabled", "site_stats_sharing_enabled")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADVERTISER_ID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_DATA_SHARING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    COST_DATA_SHARING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ADVERTISER_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ADS_PERSONALIZATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SITE_STATS_SHARING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    advertiser_id: str
    campaign_data_sharing_enabled: _wrappers_pb2.BoolValue
    cost_data_sharing_enabled: _wrappers_pb2.BoolValue
    advertiser_display_name: str
    ads_personalization_enabled: _wrappers_pb2.BoolValue
    site_stats_sharing_enabled: _wrappers_pb2.BoolValue
    def __init__(self, name: _Optional[str] = ..., advertiser_id: _Optional[str] = ..., campaign_data_sharing_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., cost_data_sharing_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., advertiser_display_name: _Optional[str] = ..., ads_personalization_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., site_stats_sharing_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class LinkProposalStatusDetails(_message.Message):
    __slots__ = ("link_proposal_initiating_product", "requestor_email", "link_proposal_state")
    LINK_PROPOSAL_INITIATING_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    REQUESTOR_EMAIL_FIELD_NUMBER: _ClassVar[int]
    LINK_PROPOSAL_STATE_FIELD_NUMBER: _ClassVar[int]
    link_proposal_initiating_product: LinkProposalInitiatingProduct
    requestor_email: str
    link_proposal_state: LinkProposalState
    def __init__(self, link_proposal_initiating_product: _Optional[_Union[LinkProposalInitiatingProduct, str]] = ..., requestor_email: _Optional[str] = ..., link_proposal_state: _Optional[_Union[LinkProposalState, str]] = ...) -> None: ...

class ConversionEvent(_message.Message):
    __slots__ = ("name", "event_name", "create_time", "deletable", "custom", "counting_method", "default_conversion_value")
    class ConversionCountingMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONVERSION_COUNTING_METHOD_UNSPECIFIED: _ClassVar[ConversionEvent.ConversionCountingMethod]
        ONCE_PER_EVENT: _ClassVar[ConversionEvent.ConversionCountingMethod]
        ONCE_PER_SESSION: _ClassVar[ConversionEvent.ConversionCountingMethod]
    CONVERSION_COUNTING_METHOD_UNSPECIFIED: ConversionEvent.ConversionCountingMethod
    ONCE_PER_EVENT: ConversionEvent.ConversionCountingMethod
    ONCE_PER_SESSION: ConversionEvent.ConversionCountingMethod
    class DefaultConversionValue(_message.Message):
        __slots__ = ("value", "currency_code")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
        value: float
        currency_code: str
        def __init__(self, value: _Optional[float] = ..., currency_code: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETABLE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    COUNTING_METHOD_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CONVERSION_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    event_name: str
    create_time: _timestamp_pb2.Timestamp
    deletable: bool
    custom: bool
    counting_method: ConversionEvent.ConversionCountingMethod
    default_conversion_value: ConversionEvent.DefaultConversionValue
    def __init__(self, name: _Optional[str] = ..., event_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deletable: bool = ..., custom: bool = ..., counting_method: _Optional[_Union[ConversionEvent.ConversionCountingMethod, str]] = ..., default_conversion_value: _Optional[_Union[ConversionEvent.DefaultConversionValue, _Mapping]] = ...) -> None: ...

class KeyEvent(_message.Message):
    __slots__ = ("name", "event_name", "create_time", "deletable", "custom", "counting_method", "default_value")
    class CountingMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COUNTING_METHOD_UNSPECIFIED: _ClassVar[KeyEvent.CountingMethod]
        ONCE_PER_EVENT: _ClassVar[KeyEvent.CountingMethod]
        ONCE_PER_SESSION: _ClassVar[KeyEvent.CountingMethod]
    COUNTING_METHOD_UNSPECIFIED: KeyEvent.CountingMethod
    ONCE_PER_EVENT: KeyEvent.CountingMethod
    ONCE_PER_SESSION: KeyEvent.CountingMethod
    class DefaultValue(_message.Message):
        __slots__ = ("numeric_value", "currency_code")
        NUMERIC_VALUE_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
        numeric_value: float
        currency_code: str
        def __init__(self, numeric_value: _Optional[float] = ..., currency_code: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETABLE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    COUNTING_METHOD_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    event_name: str
    create_time: _timestamp_pb2.Timestamp
    deletable: bool
    custom: bool
    counting_method: KeyEvent.CountingMethod
    default_value: KeyEvent.DefaultValue
    def __init__(self, name: _Optional[str] = ..., event_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deletable: bool = ..., custom: bool = ..., counting_method: _Optional[_Union[KeyEvent.CountingMethod, str]] = ..., default_value: _Optional[_Union[KeyEvent.DefaultValue, _Mapping]] = ...) -> None: ...

class GoogleSignalsSettings(_message.Message):
    __slots__ = ("name", "state", "consent")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONSENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: GoogleSignalsState
    consent: GoogleSignalsConsent
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[GoogleSignalsState, str]] = ..., consent: _Optional[_Union[GoogleSignalsConsent, str]] = ...) -> None: ...

class CustomDimension(_message.Message):
    __slots__ = ("name", "parameter_name", "display_name", "description", "scope", "disallow_ads_personalization")
    class DimensionScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DIMENSION_SCOPE_UNSPECIFIED: _ClassVar[CustomDimension.DimensionScope]
        EVENT: _ClassVar[CustomDimension.DimensionScope]
        USER: _ClassVar[CustomDimension.DimensionScope]
        ITEM: _ClassVar[CustomDimension.DimensionScope]
    DIMENSION_SCOPE_UNSPECIFIED: CustomDimension.DimensionScope
    EVENT: CustomDimension.DimensionScope
    USER: CustomDimension.DimensionScope
    ITEM: CustomDimension.DimensionScope
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    DISALLOW_ADS_PERSONALIZATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    parameter_name: str
    display_name: str
    description: str
    scope: CustomDimension.DimensionScope
    disallow_ads_personalization: bool
    def __init__(self, name: _Optional[str] = ..., parameter_name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., scope: _Optional[_Union[CustomDimension.DimensionScope, str]] = ..., disallow_ads_personalization: bool = ...) -> None: ...

class CustomMetric(_message.Message):
    __slots__ = ("name", "parameter_name", "display_name", "description", "measurement_unit", "scope", "restricted_metric_type")
    class MeasurementUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MEASUREMENT_UNIT_UNSPECIFIED: _ClassVar[CustomMetric.MeasurementUnit]
        STANDARD: _ClassVar[CustomMetric.MeasurementUnit]
        CURRENCY: _ClassVar[CustomMetric.MeasurementUnit]
        FEET: _ClassVar[CustomMetric.MeasurementUnit]
        METERS: _ClassVar[CustomMetric.MeasurementUnit]
        KILOMETERS: _ClassVar[CustomMetric.MeasurementUnit]
        MILES: _ClassVar[CustomMetric.MeasurementUnit]
        MILLISECONDS: _ClassVar[CustomMetric.MeasurementUnit]
        SECONDS: _ClassVar[CustomMetric.MeasurementUnit]
        MINUTES: _ClassVar[CustomMetric.MeasurementUnit]
        HOURS: _ClassVar[CustomMetric.MeasurementUnit]
    MEASUREMENT_UNIT_UNSPECIFIED: CustomMetric.MeasurementUnit
    STANDARD: CustomMetric.MeasurementUnit
    CURRENCY: CustomMetric.MeasurementUnit
    FEET: CustomMetric.MeasurementUnit
    METERS: CustomMetric.MeasurementUnit
    KILOMETERS: CustomMetric.MeasurementUnit
    MILES: CustomMetric.MeasurementUnit
    MILLISECONDS: CustomMetric.MeasurementUnit
    SECONDS: CustomMetric.MeasurementUnit
    MINUTES: CustomMetric.MeasurementUnit
    HOURS: CustomMetric.MeasurementUnit
    class MetricScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        METRIC_SCOPE_UNSPECIFIED: _ClassVar[CustomMetric.MetricScope]
        EVENT: _ClassVar[CustomMetric.MetricScope]
    METRIC_SCOPE_UNSPECIFIED: CustomMetric.MetricScope
    EVENT: CustomMetric.MetricScope
    class RestrictedMetricType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESTRICTED_METRIC_TYPE_UNSPECIFIED: _ClassVar[CustomMetric.RestrictedMetricType]
        COST_DATA: _ClassVar[CustomMetric.RestrictedMetricType]
        REVENUE_DATA: _ClassVar[CustomMetric.RestrictedMetricType]
    RESTRICTED_METRIC_TYPE_UNSPECIFIED: CustomMetric.RestrictedMetricType
    COST_DATA: CustomMetric.RestrictedMetricType
    REVENUE_DATA: CustomMetric.RestrictedMetricType
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_UNIT_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    RESTRICTED_METRIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    parameter_name: str
    display_name: str
    description: str
    measurement_unit: CustomMetric.MeasurementUnit
    scope: CustomMetric.MetricScope
    restricted_metric_type: _containers.RepeatedScalarFieldContainer[CustomMetric.RestrictedMetricType]
    def __init__(self, name: _Optional[str] = ..., parameter_name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., measurement_unit: _Optional[_Union[CustomMetric.MeasurementUnit, str]] = ..., scope: _Optional[_Union[CustomMetric.MetricScope, str]] = ..., restricted_metric_type: _Optional[_Iterable[_Union[CustomMetric.RestrictedMetricType, str]]] = ...) -> None: ...

class CalculatedMetric(_message.Message):
    __slots__ = ("name", "description", "display_name", "calculated_metric_id", "metric_unit", "restricted_metric_type", "formula", "invalid_metric_reference")
    class MetricUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        METRIC_UNIT_UNSPECIFIED: _ClassVar[CalculatedMetric.MetricUnit]
        STANDARD: _ClassVar[CalculatedMetric.MetricUnit]
        CURRENCY: _ClassVar[CalculatedMetric.MetricUnit]
        FEET: _ClassVar[CalculatedMetric.MetricUnit]
        MILES: _ClassVar[CalculatedMetric.MetricUnit]
        METERS: _ClassVar[CalculatedMetric.MetricUnit]
        KILOMETERS: _ClassVar[CalculatedMetric.MetricUnit]
        MILLISECONDS: _ClassVar[CalculatedMetric.MetricUnit]
        SECONDS: _ClassVar[CalculatedMetric.MetricUnit]
        MINUTES: _ClassVar[CalculatedMetric.MetricUnit]
        HOURS: _ClassVar[CalculatedMetric.MetricUnit]
    METRIC_UNIT_UNSPECIFIED: CalculatedMetric.MetricUnit
    STANDARD: CalculatedMetric.MetricUnit
    CURRENCY: CalculatedMetric.MetricUnit
    FEET: CalculatedMetric.MetricUnit
    MILES: CalculatedMetric.MetricUnit
    METERS: CalculatedMetric.MetricUnit
    KILOMETERS: CalculatedMetric.MetricUnit
    MILLISECONDS: CalculatedMetric.MetricUnit
    SECONDS: CalculatedMetric.MetricUnit
    MINUTES: CalculatedMetric.MetricUnit
    HOURS: CalculatedMetric.MetricUnit
    class RestrictedMetricType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESTRICTED_METRIC_TYPE_UNSPECIFIED: _ClassVar[CalculatedMetric.RestrictedMetricType]
        COST_DATA: _ClassVar[CalculatedMetric.RestrictedMetricType]
        REVENUE_DATA: _ClassVar[CalculatedMetric.RestrictedMetricType]
    RESTRICTED_METRIC_TYPE_UNSPECIFIED: CalculatedMetric.RestrictedMetricType
    COST_DATA: CalculatedMetric.RestrictedMetricType
    REVENUE_DATA: CalculatedMetric.RestrictedMetricType
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CALCULATED_METRIC_ID_FIELD_NUMBER: _ClassVar[int]
    METRIC_UNIT_FIELD_NUMBER: _ClassVar[int]
    RESTRICTED_METRIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    FORMULA_FIELD_NUMBER: _ClassVar[int]
    INVALID_METRIC_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    display_name: str
    calculated_metric_id: str
    metric_unit: CalculatedMetric.MetricUnit
    restricted_metric_type: _containers.RepeatedScalarFieldContainer[CalculatedMetric.RestrictedMetricType]
    formula: str
    invalid_metric_reference: bool
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., display_name: _Optional[str] = ..., calculated_metric_id: _Optional[str] = ..., metric_unit: _Optional[_Union[CalculatedMetric.MetricUnit, str]] = ..., restricted_metric_type: _Optional[_Iterable[_Union[CalculatedMetric.RestrictedMetricType, str]]] = ..., formula: _Optional[str] = ..., invalid_metric_reference: bool = ...) -> None: ...

class DataRetentionSettings(_message.Message):
    __slots__ = ("name", "event_data_retention", "reset_user_data_on_new_activity")
    class RetentionDuration(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RETENTION_DURATION_UNSPECIFIED: _ClassVar[DataRetentionSettings.RetentionDuration]
        TWO_MONTHS: _ClassVar[DataRetentionSettings.RetentionDuration]
        FOURTEEN_MONTHS: _ClassVar[DataRetentionSettings.RetentionDuration]
        TWENTY_SIX_MONTHS: _ClassVar[DataRetentionSettings.RetentionDuration]
        THIRTY_EIGHT_MONTHS: _ClassVar[DataRetentionSettings.RetentionDuration]
        FIFTY_MONTHS: _ClassVar[DataRetentionSettings.RetentionDuration]
    RETENTION_DURATION_UNSPECIFIED: DataRetentionSettings.RetentionDuration
    TWO_MONTHS: DataRetentionSettings.RetentionDuration
    FOURTEEN_MONTHS: DataRetentionSettings.RetentionDuration
    TWENTY_SIX_MONTHS: DataRetentionSettings.RetentionDuration
    THIRTY_EIGHT_MONTHS: DataRetentionSettings.RetentionDuration
    FIFTY_MONTHS: DataRetentionSettings.RetentionDuration
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_DATA_RETENTION_FIELD_NUMBER: _ClassVar[int]
    RESET_USER_DATA_ON_NEW_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    event_data_retention: DataRetentionSettings.RetentionDuration
    reset_user_data_on_new_activity: bool
    def __init__(self, name: _Optional[str] = ..., event_data_retention: _Optional[_Union[DataRetentionSettings.RetentionDuration, str]] = ..., reset_user_data_on_new_activity: bool = ...) -> None: ...

class AttributionSettings(_message.Message):
    __slots__ = ("name", "acquisition_conversion_event_lookback_window", "other_conversion_event_lookback_window", "reporting_attribution_model", "ads_web_conversion_data_export_scope")
    class AcquisitionConversionEventLookbackWindow(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_UNSPECIFIED: _ClassVar[AttributionSettings.AcquisitionConversionEventLookbackWindow]
        ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_7_DAYS: _ClassVar[AttributionSettings.AcquisitionConversionEventLookbackWindow]
        ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_30_DAYS: _ClassVar[AttributionSettings.AcquisitionConversionEventLookbackWindow]
    ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_UNSPECIFIED: AttributionSettings.AcquisitionConversionEventLookbackWindow
    ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_7_DAYS: AttributionSettings.AcquisitionConversionEventLookbackWindow
    ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_30_DAYS: AttributionSettings.AcquisitionConversionEventLookbackWindow
    class OtherConversionEventLookbackWindow(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_UNSPECIFIED: _ClassVar[AttributionSettings.OtherConversionEventLookbackWindow]
        OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_30_DAYS: _ClassVar[AttributionSettings.OtherConversionEventLookbackWindow]
        OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_60_DAYS: _ClassVar[AttributionSettings.OtherConversionEventLookbackWindow]
        OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_90_DAYS: _ClassVar[AttributionSettings.OtherConversionEventLookbackWindow]
    OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_UNSPECIFIED: AttributionSettings.OtherConversionEventLookbackWindow
    OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_30_DAYS: AttributionSettings.OtherConversionEventLookbackWindow
    OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_60_DAYS: AttributionSettings.OtherConversionEventLookbackWindow
    OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_90_DAYS: AttributionSettings.OtherConversionEventLookbackWindow
    class ReportingAttributionModel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REPORTING_ATTRIBUTION_MODEL_UNSPECIFIED: _ClassVar[AttributionSettings.ReportingAttributionModel]
        PAID_AND_ORGANIC_CHANNELS_DATA_DRIVEN: _ClassVar[AttributionSettings.ReportingAttributionModel]
        PAID_AND_ORGANIC_CHANNELS_LAST_CLICK: _ClassVar[AttributionSettings.ReportingAttributionModel]
        GOOGLE_PAID_CHANNELS_LAST_CLICK: _ClassVar[AttributionSettings.ReportingAttributionModel]
    REPORTING_ATTRIBUTION_MODEL_UNSPECIFIED: AttributionSettings.ReportingAttributionModel
    PAID_AND_ORGANIC_CHANNELS_DATA_DRIVEN: AttributionSettings.ReportingAttributionModel
    PAID_AND_ORGANIC_CHANNELS_LAST_CLICK: AttributionSettings.ReportingAttributionModel
    GOOGLE_PAID_CHANNELS_LAST_CLICK: AttributionSettings.ReportingAttributionModel
    class AdsWebConversionDataExportScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ADS_WEB_CONVERSION_DATA_EXPORT_SCOPE_UNSPECIFIED: _ClassVar[AttributionSettings.AdsWebConversionDataExportScope]
        NOT_SELECTED_YET: _ClassVar[AttributionSettings.AdsWebConversionDataExportScope]
        PAID_AND_ORGANIC_CHANNELS: _ClassVar[AttributionSettings.AdsWebConversionDataExportScope]
        GOOGLE_PAID_CHANNELS: _ClassVar[AttributionSettings.AdsWebConversionDataExportScope]
    ADS_WEB_CONVERSION_DATA_EXPORT_SCOPE_UNSPECIFIED: AttributionSettings.AdsWebConversionDataExportScope
    NOT_SELECTED_YET: AttributionSettings.AdsWebConversionDataExportScope
    PAID_AND_ORGANIC_CHANNELS: AttributionSettings.AdsWebConversionDataExportScope
    GOOGLE_PAID_CHANNELS: AttributionSettings.AdsWebConversionDataExportScope
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_FIELD_NUMBER: _ClassVar[int]
    OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_FIELD_NUMBER: _ClassVar[int]
    REPORTING_ATTRIBUTION_MODEL_FIELD_NUMBER: _ClassVar[int]
    ADS_WEB_CONVERSION_DATA_EXPORT_SCOPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    acquisition_conversion_event_lookback_window: AttributionSettings.AcquisitionConversionEventLookbackWindow
    other_conversion_event_lookback_window: AttributionSettings.OtherConversionEventLookbackWindow
    reporting_attribution_model: AttributionSettings.ReportingAttributionModel
    ads_web_conversion_data_export_scope: AttributionSettings.AdsWebConversionDataExportScope
    def __init__(self, name: _Optional[str] = ..., acquisition_conversion_event_lookback_window: _Optional[_Union[AttributionSettings.AcquisitionConversionEventLookbackWindow, str]] = ..., other_conversion_event_lookback_window: _Optional[_Union[AttributionSettings.OtherConversionEventLookbackWindow, str]] = ..., reporting_attribution_model: _Optional[_Union[AttributionSettings.ReportingAttributionModel, str]] = ..., ads_web_conversion_data_export_scope: _Optional[_Union[AttributionSettings.AdsWebConversionDataExportScope, str]] = ...) -> None: ...

class AccessBinding(_message.Message):
    __slots__ = ("user", "name", "roles")
    USER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    user: str
    name: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user: _Optional[str] = ..., name: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ...) -> None: ...

class BigQueryLink(_message.Message):
    __slots__ = ("name", "project", "create_time", "daily_export_enabled", "streaming_export_enabled", "fresh_daily_export_enabled", "include_advertising_id", "export_streams", "excluded_events", "dataset_location")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DAILY_EXPORT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    STREAMING_EXPORT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FRESH_DAILY_EXPORT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ADVERTISING_ID_FIELD_NUMBER: _ClassVar[int]
    EXPORT_STREAMS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_EVENTS_FIELD_NUMBER: _ClassVar[int]
    DATASET_LOCATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    project: str
    create_time: _timestamp_pb2.Timestamp
    daily_export_enabled: bool
    streaming_export_enabled: bool
    fresh_daily_export_enabled: bool
    include_advertising_id: bool
    export_streams: _containers.RepeatedScalarFieldContainer[str]
    excluded_events: _containers.RepeatedScalarFieldContainer[str]
    dataset_location: str
    def __init__(self, name: _Optional[str] = ..., project: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., daily_export_enabled: bool = ..., streaming_export_enabled: bool = ..., fresh_daily_export_enabled: bool = ..., include_advertising_id: bool = ..., export_streams: _Optional[_Iterable[str]] = ..., excluded_events: _Optional[_Iterable[str]] = ..., dataset_location: _Optional[str] = ...) -> None: ...

class EnhancedMeasurementSettings(_message.Message):
    __slots__ = ("name", "stream_enabled", "scrolls_enabled", "outbound_clicks_enabled", "site_search_enabled", "video_engagement_enabled", "file_downloads_enabled", "page_changes_enabled", "form_interactions_enabled", "search_query_parameter", "uri_query_parameter")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STREAM_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SCROLLS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_CLICKS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SITE_SEARCH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ENGAGEMENT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FILE_DOWNLOADS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PAGE_CHANGES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FORM_INTERACTIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SEARCH_QUERY_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    URI_QUERY_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    name: str
    stream_enabled: bool
    scrolls_enabled: bool
    outbound_clicks_enabled: bool
    site_search_enabled: bool
    video_engagement_enabled: bool
    file_downloads_enabled: bool
    page_changes_enabled: bool
    form_interactions_enabled: bool
    search_query_parameter: str
    uri_query_parameter: str
    def __init__(self, name: _Optional[str] = ..., stream_enabled: bool = ..., scrolls_enabled: bool = ..., outbound_clicks_enabled: bool = ..., site_search_enabled: bool = ..., video_engagement_enabled: bool = ..., file_downloads_enabled: bool = ..., page_changes_enabled: bool = ..., form_interactions_enabled: bool = ..., search_query_parameter: _Optional[str] = ..., uri_query_parameter: _Optional[str] = ...) -> None: ...

class ConnectedSiteTag(_message.Message):
    __slots__ = ("display_name", "tag_id")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_ID_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    tag_id: str
    def __init__(self, display_name: _Optional[str] = ..., tag_id: _Optional[str] = ...) -> None: ...

class DataRedactionSettings(_message.Message):
    __slots__ = ("name", "email_redaction_enabled", "query_parameter_redaction_enabled", "query_parameter_keys")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_REDACTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    QUERY_PARAMETER_REDACTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    QUERY_PARAMETER_KEYS_FIELD_NUMBER: _ClassVar[int]
    name: str
    email_redaction_enabled: bool
    query_parameter_redaction_enabled: bool
    query_parameter_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., email_redaction_enabled: bool = ..., query_parameter_redaction_enabled: bool = ..., query_parameter_keys: _Optional[_Iterable[str]] = ...) -> None: ...

class AdSenseLink(_message.Message):
    __slots__ = ("name", "ad_client_code")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AD_CLIENT_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    ad_client_code: str
    def __init__(self, name: _Optional[str] = ..., ad_client_code: _Optional[str] = ...) -> None: ...

class RollupPropertySourceLink(_message.Message):
    __slots__ = ("name", "source_property")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    name: str
    source_property: str
    def __init__(self, name: _Optional[str] = ..., source_property: _Optional[str] = ...) -> None: ...
