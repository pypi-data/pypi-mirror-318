from google.analytics.admin.v1beta import access_report_pb2 as _access_report_pb2
from google.analytics.admin.v1beta import resources_pb2 as _resources_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RunAccessReportRequest(_message.Message):
    __slots__ = ("entity", "dimensions", "metrics", "date_ranges", "dimension_filter", "metric_filter", "offset", "limit", "time_zone", "order_bys", "return_entity_quota", "include_all_users", "expand_groups")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    DATE_RANGES_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FILTER_FIELD_NUMBER: _ClassVar[int]
    METRIC_FILTER_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    ORDER_BYS_FIELD_NUMBER: _ClassVar[int]
    RETURN_ENTITY_QUOTA_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ALL_USERS_FIELD_NUMBER: _ClassVar[int]
    EXPAND_GROUPS_FIELD_NUMBER: _ClassVar[int]
    entity: str
    dimensions: _containers.RepeatedCompositeFieldContainer[_access_report_pb2.AccessDimension]
    metrics: _containers.RepeatedCompositeFieldContainer[_access_report_pb2.AccessMetric]
    date_ranges: _containers.RepeatedCompositeFieldContainer[_access_report_pb2.AccessDateRange]
    dimension_filter: _access_report_pb2.AccessFilterExpression
    metric_filter: _access_report_pb2.AccessFilterExpression
    offset: int
    limit: int
    time_zone: str
    order_bys: _containers.RepeatedCompositeFieldContainer[_access_report_pb2.AccessOrderBy]
    return_entity_quota: bool
    include_all_users: bool
    expand_groups: bool
    def __init__(self, entity: _Optional[str] = ..., dimensions: _Optional[_Iterable[_Union[_access_report_pb2.AccessDimension, _Mapping]]] = ..., metrics: _Optional[_Iterable[_Union[_access_report_pb2.AccessMetric, _Mapping]]] = ..., date_ranges: _Optional[_Iterable[_Union[_access_report_pb2.AccessDateRange, _Mapping]]] = ..., dimension_filter: _Optional[_Union[_access_report_pb2.AccessFilterExpression, _Mapping]] = ..., metric_filter: _Optional[_Union[_access_report_pb2.AccessFilterExpression, _Mapping]] = ..., offset: _Optional[int] = ..., limit: _Optional[int] = ..., time_zone: _Optional[str] = ..., order_bys: _Optional[_Iterable[_Union[_access_report_pb2.AccessOrderBy, _Mapping]]] = ..., return_entity_quota: bool = ..., include_all_users: bool = ..., expand_groups: bool = ...) -> None: ...

class RunAccessReportResponse(_message.Message):
    __slots__ = ("dimension_headers", "metric_headers", "rows", "row_count", "quota")
    DIMENSION_HEADERS_FIELD_NUMBER: _ClassVar[int]
    METRIC_HEADERS_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    QUOTA_FIELD_NUMBER: _ClassVar[int]
    dimension_headers: _containers.RepeatedCompositeFieldContainer[_access_report_pb2.AccessDimensionHeader]
    metric_headers: _containers.RepeatedCompositeFieldContainer[_access_report_pb2.AccessMetricHeader]
    rows: _containers.RepeatedCompositeFieldContainer[_access_report_pb2.AccessRow]
    row_count: int
    quota: _access_report_pb2.AccessQuota
    def __init__(self, dimension_headers: _Optional[_Iterable[_Union[_access_report_pb2.AccessDimensionHeader, _Mapping]]] = ..., metric_headers: _Optional[_Iterable[_Union[_access_report_pb2.AccessMetricHeader, _Mapping]]] = ..., rows: _Optional[_Iterable[_Union[_access_report_pb2.AccessRow, _Mapping]]] = ..., row_count: _Optional[int] = ..., quota: _Optional[_Union[_access_report_pb2.AccessQuota, _Mapping]] = ...) -> None: ...

class GetAccountRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAccountsRequest(_message.Message):
    __slots__ = ("page_size", "page_token", "show_deleted")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    show_deleted: bool
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., show_deleted: bool = ...) -> None: ...

class ListAccountsResponse(_message.Message):
    __slots__ = ("accounts", "next_page_token")
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Account]
    next_page_token: str
    def __init__(self, accounts: _Optional[_Iterable[_Union[_resources_pb2.Account, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteAccountRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateAccountRequest(_message.Message):
    __slots__ = ("account", "update_mask")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    account: _resources_pb2.Account
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, account: _Optional[_Union[_resources_pb2.Account, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ProvisionAccountTicketRequest(_message.Message):
    __slots__ = ("account", "redirect_uri")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    account: _resources_pb2.Account
    redirect_uri: str
    def __init__(self, account: _Optional[_Union[_resources_pb2.Account, _Mapping]] = ..., redirect_uri: _Optional[str] = ...) -> None: ...

class ProvisionAccountTicketResponse(_message.Message):
    __slots__ = ("account_ticket_id",)
    ACCOUNT_TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    account_ticket_id: str
    def __init__(self, account_ticket_id: _Optional[str] = ...) -> None: ...

class GetPropertyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListPropertiesRequest(_message.Message):
    __slots__ = ("filter", "page_size", "page_token", "show_deleted")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    filter: str
    page_size: int
    page_token: str
    show_deleted: bool
    def __init__(self, filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., show_deleted: bool = ...) -> None: ...

class ListPropertiesResponse(_message.Message):
    __slots__ = ("properties", "next_page_token")
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    properties: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Property]
    next_page_token: str
    def __init__(self, properties: _Optional[_Iterable[_Union[_resources_pb2.Property, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdatePropertyRequest(_message.Message):
    __slots__ = ("property", "update_mask")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    property: _resources_pb2.Property
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, property: _Optional[_Union[_resources_pb2.Property, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreatePropertyRequest(_message.Message):
    __slots__ = ("property",)
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    property: _resources_pb2.Property
    def __init__(self, property: _Optional[_Union[_resources_pb2.Property, _Mapping]] = ...) -> None: ...

class DeletePropertyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateFirebaseLinkRequest(_message.Message):
    __slots__ = ("parent", "firebase_link")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FIREBASE_LINK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    firebase_link: _resources_pb2.FirebaseLink
    def __init__(self, parent: _Optional[str] = ..., firebase_link: _Optional[_Union[_resources_pb2.FirebaseLink, _Mapping]] = ...) -> None: ...

class DeleteFirebaseLinkRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListFirebaseLinksRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListFirebaseLinksResponse(_message.Message):
    __slots__ = ("firebase_links", "next_page_token")
    FIREBASE_LINKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    firebase_links: _containers.RepeatedCompositeFieldContainer[_resources_pb2.FirebaseLink]
    next_page_token: str
    def __init__(self, firebase_links: _Optional[_Iterable[_Union[_resources_pb2.FirebaseLink, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateGoogleAdsLinkRequest(_message.Message):
    __slots__ = ("parent", "google_ads_link")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_ADS_LINK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    google_ads_link: _resources_pb2.GoogleAdsLink
    def __init__(self, parent: _Optional[str] = ..., google_ads_link: _Optional[_Union[_resources_pb2.GoogleAdsLink, _Mapping]] = ...) -> None: ...

class UpdateGoogleAdsLinkRequest(_message.Message):
    __slots__ = ("google_ads_link", "update_mask")
    GOOGLE_ADS_LINK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    google_ads_link: _resources_pb2.GoogleAdsLink
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, google_ads_link: _Optional[_Union[_resources_pb2.GoogleAdsLink, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteGoogleAdsLinkRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListGoogleAdsLinksRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListGoogleAdsLinksResponse(_message.Message):
    __slots__ = ("google_ads_links", "next_page_token")
    GOOGLE_ADS_LINKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    google_ads_links: _containers.RepeatedCompositeFieldContainer[_resources_pb2.GoogleAdsLink]
    next_page_token: str
    def __init__(self, google_ads_links: _Optional[_Iterable[_Union[_resources_pb2.GoogleAdsLink, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetDataSharingSettingsRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAccountSummariesRequest(_message.Message):
    __slots__ = ("page_size", "page_token")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAccountSummariesResponse(_message.Message):
    __slots__ = ("account_summaries", "next_page_token")
    ACCOUNT_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    account_summaries: _containers.RepeatedCompositeFieldContainer[_resources_pb2.AccountSummary]
    next_page_token: str
    def __init__(self, account_summaries: _Optional[_Iterable[_Union[_resources_pb2.AccountSummary, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class AcknowledgeUserDataCollectionRequest(_message.Message):
    __slots__ = ("property", "acknowledgement")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGEMENT_FIELD_NUMBER: _ClassVar[int]
    property: str
    acknowledgement: str
    def __init__(self, property: _Optional[str] = ..., acknowledgement: _Optional[str] = ...) -> None: ...

class AcknowledgeUserDataCollectionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SearchChangeHistoryEventsRequest(_message.Message):
    __slots__ = ("account", "property", "resource_type", "action", "actor_email", "earliest_change_time", "latest_change_time", "page_size", "page_token")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ACTOR_EMAIL_FIELD_NUMBER: _ClassVar[int]
    EARLIEST_CHANGE_TIME_FIELD_NUMBER: _ClassVar[int]
    LATEST_CHANGE_TIME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    account: str
    property: str
    resource_type: _containers.RepeatedScalarFieldContainer[_resources_pb2.ChangeHistoryResourceType]
    action: _containers.RepeatedScalarFieldContainer[_resources_pb2.ActionType]
    actor_email: _containers.RepeatedScalarFieldContainer[str]
    earliest_change_time: _timestamp_pb2.Timestamp
    latest_change_time: _timestamp_pb2.Timestamp
    page_size: int
    page_token: str
    def __init__(self, account: _Optional[str] = ..., property: _Optional[str] = ..., resource_type: _Optional[_Iterable[_Union[_resources_pb2.ChangeHistoryResourceType, str]]] = ..., action: _Optional[_Iterable[_Union[_resources_pb2.ActionType, str]]] = ..., actor_email: _Optional[_Iterable[str]] = ..., earliest_change_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., latest_change_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class SearchChangeHistoryEventsResponse(_message.Message):
    __slots__ = ("change_history_events", "next_page_token")
    CHANGE_HISTORY_EVENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    change_history_events: _containers.RepeatedCompositeFieldContainer[_resources_pb2.ChangeHistoryEvent]
    next_page_token: str
    def __init__(self, change_history_events: _Optional[_Iterable[_Union[_resources_pb2.ChangeHistoryEvent, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetMeasurementProtocolSecretRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateMeasurementProtocolSecretRequest(_message.Message):
    __slots__ = ("parent", "measurement_protocol_secret")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_PROTOCOL_SECRET_FIELD_NUMBER: _ClassVar[int]
    parent: str
    measurement_protocol_secret: _resources_pb2.MeasurementProtocolSecret
    def __init__(self, parent: _Optional[str] = ..., measurement_protocol_secret: _Optional[_Union[_resources_pb2.MeasurementProtocolSecret, _Mapping]] = ...) -> None: ...

class DeleteMeasurementProtocolSecretRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateMeasurementProtocolSecretRequest(_message.Message):
    __slots__ = ("measurement_protocol_secret", "update_mask")
    MEASUREMENT_PROTOCOL_SECRET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    measurement_protocol_secret: _resources_pb2.MeasurementProtocolSecret
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, measurement_protocol_secret: _Optional[_Union[_resources_pb2.MeasurementProtocolSecret, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListMeasurementProtocolSecretsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListMeasurementProtocolSecretsResponse(_message.Message):
    __slots__ = ("measurement_protocol_secrets", "next_page_token")
    MEASUREMENT_PROTOCOL_SECRETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    measurement_protocol_secrets: _containers.RepeatedCompositeFieldContainer[_resources_pb2.MeasurementProtocolSecret]
    next_page_token: str
    def __init__(self, measurement_protocol_secrets: _Optional[_Iterable[_Union[_resources_pb2.MeasurementProtocolSecret, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateConversionEventRequest(_message.Message):
    __slots__ = ("conversion_event", "parent")
    CONVERSION_EVENT_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    conversion_event: _resources_pb2.ConversionEvent
    parent: str
    def __init__(self, conversion_event: _Optional[_Union[_resources_pb2.ConversionEvent, _Mapping]] = ..., parent: _Optional[str] = ...) -> None: ...

class UpdateConversionEventRequest(_message.Message):
    __slots__ = ("conversion_event", "update_mask")
    CONVERSION_EVENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    conversion_event: _resources_pb2.ConversionEvent
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, conversion_event: _Optional[_Union[_resources_pb2.ConversionEvent, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetConversionEventRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteConversionEventRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListConversionEventsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListConversionEventsResponse(_message.Message):
    __slots__ = ("conversion_events", "next_page_token")
    CONVERSION_EVENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    conversion_events: _containers.RepeatedCompositeFieldContainer[_resources_pb2.ConversionEvent]
    next_page_token: str
    def __init__(self, conversion_events: _Optional[_Iterable[_Union[_resources_pb2.ConversionEvent, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateKeyEventRequest(_message.Message):
    __slots__ = ("key_event", "parent")
    KEY_EVENT_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    key_event: _resources_pb2.KeyEvent
    parent: str
    def __init__(self, key_event: _Optional[_Union[_resources_pb2.KeyEvent, _Mapping]] = ..., parent: _Optional[str] = ...) -> None: ...

class UpdateKeyEventRequest(_message.Message):
    __slots__ = ("key_event", "update_mask")
    KEY_EVENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    key_event: _resources_pb2.KeyEvent
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, key_event: _Optional[_Union[_resources_pb2.KeyEvent, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetKeyEventRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteKeyEventRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListKeyEventsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListKeyEventsResponse(_message.Message):
    __slots__ = ("key_events", "next_page_token")
    KEY_EVENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    key_events: _containers.RepeatedCompositeFieldContainer[_resources_pb2.KeyEvent]
    next_page_token: str
    def __init__(self, key_events: _Optional[_Iterable[_Union[_resources_pb2.KeyEvent, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateCustomDimensionRequest(_message.Message):
    __slots__ = ("parent", "custom_dimension")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    custom_dimension: _resources_pb2.CustomDimension
    def __init__(self, parent: _Optional[str] = ..., custom_dimension: _Optional[_Union[_resources_pb2.CustomDimension, _Mapping]] = ...) -> None: ...

class UpdateCustomDimensionRequest(_message.Message):
    __slots__ = ("custom_dimension", "update_mask")
    CUSTOM_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    custom_dimension: _resources_pb2.CustomDimension
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, custom_dimension: _Optional[_Union[_resources_pb2.CustomDimension, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListCustomDimensionsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListCustomDimensionsResponse(_message.Message):
    __slots__ = ("custom_dimensions", "next_page_token")
    CUSTOM_DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    custom_dimensions: _containers.RepeatedCompositeFieldContainer[_resources_pb2.CustomDimension]
    next_page_token: str
    def __init__(self, custom_dimensions: _Optional[_Iterable[_Union[_resources_pb2.CustomDimension, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ArchiveCustomDimensionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetCustomDimensionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateCustomMetricRequest(_message.Message):
    __slots__ = ("parent", "custom_metric")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_METRIC_FIELD_NUMBER: _ClassVar[int]
    parent: str
    custom_metric: _resources_pb2.CustomMetric
    def __init__(self, parent: _Optional[str] = ..., custom_metric: _Optional[_Union[_resources_pb2.CustomMetric, _Mapping]] = ...) -> None: ...

class UpdateCustomMetricRequest(_message.Message):
    __slots__ = ("custom_metric", "update_mask")
    CUSTOM_METRIC_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    custom_metric: _resources_pb2.CustomMetric
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, custom_metric: _Optional[_Union[_resources_pb2.CustomMetric, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListCustomMetricsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListCustomMetricsResponse(_message.Message):
    __slots__ = ("custom_metrics", "next_page_token")
    CUSTOM_METRICS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    custom_metrics: _containers.RepeatedCompositeFieldContainer[_resources_pb2.CustomMetric]
    next_page_token: str
    def __init__(self, custom_metrics: _Optional[_Iterable[_Union[_resources_pb2.CustomMetric, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ArchiveCustomMetricRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetCustomMetricRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetDataRetentionSettingsRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateDataRetentionSettingsRequest(_message.Message):
    __slots__ = ("data_retention_settings", "update_mask")
    DATA_RETENTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    data_retention_settings: _resources_pb2.DataRetentionSettings
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, data_retention_settings: _Optional[_Union[_resources_pb2.DataRetentionSettings, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateDataStreamRequest(_message.Message):
    __slots__ = ("parent", "data_stream")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATA_STREAM_FIELD_NUMBER: _ClassVar[int]
    parent: str
    data_stream: _resources_pb2.DataStream
    def __init__(self, parent: _Optional[str] = ..., data_stream: _Optional[_Union[_resources_pb2.DataStream, _Mapping]] = ...) -> None: ...

class DeleteDataStreamRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateDataStreamRequest(_message.Message):
    __slots__ = ("data_stream", "update_mask")
    DATA_STREAM_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    data_stream: _resources_pb2.DataStream
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, data_stream: _Optional[_Union[_resources_pb2.DataStream, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListDataStreamsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListDataStreamsResponse(_message.Message):
    __slots__ = ("data_streams", "next_page_token")
    DATA_STREAMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    data_streams: _containers.RepeatedCompositeFieldContainer[_resources_pb2.DataStream]
    next_page_token: str
    def __init__(self, data_streams: _Optional[_Iterable[_Union[_resources_pb2.DataStream, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetDataStreamRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
