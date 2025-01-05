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
    DATA_RETENTION_SETTINGS: _ClassVar[ChangeHistoryResourceType]
    DISPLAY_VIDEO_360_ADVERTISER_LINK: _ClassVar[ChangeHistoryResourceType]
    DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSAL: _ClassVar[ChangeHistoryResourceType]
    DATA_STREAM: _ClassVar[ChangeHistoryResourceType]
    ATTRIBUTION_SETTINGS: _ClassVar[ChangeHistoryResourceType]

class PropertyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROPERTY_TYPE_UNSPECIFIED: _ClassVar[PropertyType]
    PROPERTY_TYPE_ORDINARY: _ClassVar[PropertyType]
    PROPERTY_TYPE_SUBPROPERTY: _ClassVar[PropertyType]
    PROPERTY_TYPE_ROLLUP: _ClassVar[PropertyType]
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
DATA_RETENTION_SETTINGS: ChangeHistoryResourceType
DISPLAY_VIDEO_360_ADVERTISER_LINK: ChangeHistoryResourceType
DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSAL: ChangeHistoryResourceType
DATA_STREAM: ChangeHistoryResourceType
ATTRIBUTION_SETTINGS: ChangeHistoryResourceType
PROPERTY_TYPE_UNSPECIFIED: PropertyType
PROPERTY_TYPE_ORDINARY: PropertyType
PROPERTY_TYPE_SUBPROPERTY: PropertyType
PROPERTY_TYPE_ROLLUP: PropertyType

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
        __slots__ = ("account", "property", "firebase_link", "google_ads_link", "conversion_event", "measurement_protocol_secret", "data_retention_settings", "data_stream")
        ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        PROPERTY_FIELD_NUMBER: _ClassVar[int]
        FIREBASE_LINK_FIELD_NUMBER: _ClassVar[int]
        GOOGLE_ADS_LINK_FIELD_NUMBER: _ClassVar[int]
        CONVERSION_EVENT_FIELD_NUMBER: _ClassVar[int]
        MEASUREMENT_PROTOCOL_SECRET_FIELD_NUMBER: _ClassVar[int]
        DATA_RETENTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        DATA_STREAM_FIELD_NUMBER: _ClassVar[int]
        account: Account
        property: Property
        firebase_link: FirebaseLink
        google_ads_link: GoogleAdsLink
        conversion_event: ConversionEvent
        measurement_protocol_secret: MeasurementProtocolSecret
        data_retention_settings: DataRetentionSettings
        data_stream: DataStream
        def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ..., property: _Optional[_Union[Property, _Mapping]] = ..., firebase_link: _Optional[_Union[FirebaseLink, _Mapping]] = ..., google_ads_link: _Optional[_Union[GoogleAdsLink, _Mapping]] = ..., conversion_event: _Optional[_Union[ConversionEvent, _Mapping]] = ..., measurement_protocol_secret: _Optional[_Union[MeasurementProtocolSecret, _Mapping]] = ..., data_retention_settings: _Optional[_Union[DataRetentionSettings, _Mapping]] = ..., data_stream: _Optional[_Union[DataStream, _Mapping]] = ...) -> None: ...
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_BEFORE_CHANGE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_AFTER_CHANGE_FIELD_NUMBER: _ClassVar[int]
    resource: str
    action: ActionType
    resource_before_change: ChangeHistoryChange.ChangeHistoryResource
    resource_after_change: ChangeHistoryChange.ChangeHistoryResource
    def __init__(self, resource: _Optional[str] = ..., action: _Optional[_Union[ActionType, str]] = ..., resource_before_change: _Optional[_Union[ChangeHistoryChange.ChangeHistoryResource, _Mapping]] = ..., resource_after_change: _Optional[_Union[ChangeHistoryChange.ChangeHistoryResource, _Mapping]] = ...) -> None: ...

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
