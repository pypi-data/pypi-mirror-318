from google.analytics.admin.v1alpha import access_report_pb2 as _access_report_pb2
from google.analytics.admin.v1alpha import audience_pb2 as _audience_pb2
from google.analytics.admin.v1alpha import channel_group_pb2 as _channel_group_pb2
from google.analytics.admin.v1alpha import event_create_and_edit_pb2 as _event_create_and_edit_pb2
from google.analytics.admin.v1alpha import expanded_data_set_pb2 as _expanded_data_set_pb2
from google.analytics.admin.v1alpha import resources_pb2 as _resources_pb2
from google.analytics.admin.v1alpha import subproperty_event_filter_pb2 as _subproperty_event_filter_pb2
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

class GetGlobalSiteTagRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

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

class GetSKAdNetworkConversionValueSchemaRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateSKAdNetworkConversionValueSchemaRequest(_message.Message):
    __slots__ = ("parent", "skadnetwork_conversion_value_schema")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SKADNETWORK_CONVERSION_VALUE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    parent: str
    skadnetwork_conversion_value_schema: _resources_pb2.SKAdNetworkConversionValueSchema
    def __init__(self, parent: _Optional[str] = ..., skadnetwork_conversion_value_schema: _Optional[_Union[_resources_pb2.SKAdNetworkConversionValueSchema, _Mapping]] = ...) -> None: ...

class DeleteSKAdNetworkConversionValueSchemaRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateSKAdNetworkConversionValueSchemaRequest(_message.Message):
    __slots__ = ("skadnetwork_conversion_value_schema", "update_mask")
    SKADNETWORK_CONVERSION_VALUE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    skadnetwork_conversion_value_schema: _resources_pb2.SKAdNetworkConversionValueSchema
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, skadnetwork_conversion_value_schema: _Optional[_Union[_resources_pb2.SKAdNetworkConversionValueSchema, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListSKAdNetworkConversionValueSchemasRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListSKAdNetworkConversionValueSchemasResponse(_message.Message):
    __slots__ = ("skadnetwork_conversion_value_schemas", "next_page_token")
    SKADNETWORK_CONVERSION_VALUE_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    skadnetwork_conversion_value_schemas: _containers.RepeatedCompositeFieldContainer[_resources_pb2.SKAdNetworkConversionValueSchema]
    next_page_token: str
    def __init__(self, skadnetwork_conversion_value_schemas: _Optional[_Iterable[_Union[_resources_pb2.SKAdNetworkConversionValueSchema, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetGoogleSignalsSettingsRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateGoogleSignalsSettingsRequest(_message.Message):
    __slots__ = ("google_signals_settings", "update_mask")
    GOOGLE_SIGNALS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    google_signals_settings: _resources_pb2.GoogleSignalsSettings
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, google_signals_settings: _Optional[_Union[_resources_pb2.GoogleSignalsSettings, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

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

class GetDisplayVideo360AdvertiserLinkRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListDisplayVideo360AdvertiserLinksRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListDisplayVideo360AdvertiserLinksResponse(_message.Message):
    __slots__ = ("display_video_360_advertiser_links", "next_page_token")
    DISPLAY_VIDEO_360_ADVERTISER_LINKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    display_video_360_advertiser_links: _containers.RepeatedCompositeFieldContainer[_resources_pb2.DisplayVideo360AdvertiserLink]
    next_page_token: str
    def __init__(self, display_video_360_advertiser_links: _Optional[_Iterable[_Union[_resources_pb2.DisplayVideo360AdvertiserLink, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateDisplayVideo360AdvertiserLinkRequest(_message.Message):
    __slots__ = ("parent", "display_video_360_advertiser_link")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_VIDEO_360_ADVERTISER_LINK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    display_video_360_advertiser_link: _resources_pb2.DisplayVideo360AdvertiserLink
    def __init__(self, parent: _Optional[str] = ..., display_video_360_advertiser_link: _Optional[_Union[_resources_pb2.DisplayVideo360AdvertiserLink, _Mapping]] = ...) -> None: ...

class DeleteDisplayVideo360AdvertiserLinkRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateDisplayVideo360AdvertiserLinkRequest(_message.Message):
    __slots__ = ("display_video_360_advertiser_link", "update_mask")
    DISPLAY_VIDEO_360_ADVERTISER_LINK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    display_video_360_advertiser_link: _resources_pb2.DisplayVideo360AdvertiserLink
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, display_video_360_advertiser_link: _Optional[_Union[_resources_pb2.DisplayVideo360AdvertiserLink, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetDisplayVideo360AdvertiserLinkProposalRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListDisplayVideo360AdvertiserLinkProposalsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListDisplayVideo360AdvertiserLinkProposalsResponse(_message.Message):
    __slots__ = ("display_video_360_advertiser_link_proposals", "next_page_token")
    DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSALS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    display_video_360_advertiser_link_proposals: _containers.RepeatedCompositeFieldContainer[_resources_pb2.DisplayVideo360AdvertiserLinkProposal]
    next_page_token: str
    def __init__(self, display_video_360_advertiser_link_proposals: _Optional[_Iterable[_Union[_resources_pb2.DisplayVideo360AdvertiserLinkProposal, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateDisplayVideo360AdvertiserLinkProposalRequest(_message.Message):
    __slots__ = ("parent", "display_video_360_advertiser_link_proposal")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    display_video_360_advertiser_link_proposal: _resources_pb2.DisplayVideo360AdvertiserLinkProposal
    def __init__(self, parent: _Optional[str] = ..., display_video_360_advertiser_link_proposal: _Optional[_Union[_resources_pb2.DisplayVideo360AdvertiserLinkProposal, _Mapping]] = ...) -> None: ...

class DeleteDisplayVideo360AdvertiserLinkProposalRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ApproveDisplayVideo360AdvertiserLinkProposalRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ApproveDisplayVideo360AdvertiserLinkProposalResponse(_message.Message):
    __slots__ = ("display_video_360_advertiser_link",)
    DISPLAY_VIDEO_360_ADVERTISER_LINK_FIELD_NUMBER: _ClassVar[int]
    display_video_360_advertiser_link: _resources_pb2.DisplayVideo360AdvertiserLink
    def __init__(self, display_video_360_advertiser_link: _Optional[_Union[_resources_pb2.DisplayVideo360AdvertiserLink, _Mapping]] = ...) -> None: ...

class CancelDisplayVideo360AdvertiserLinkProposalRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetSearchAds360LinkRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListSearchAds360LinksRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListSearchAds360LinksResponse(_message.Message):
    __slots__ = ("search_ads_360_links", "next_page_token")
    SEARCH_ADS_360_LINKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    search_ads_360_links: _containers.RepeatedCompositeFieldContainer[_resources_pb2.SearchAds360Link]
    next_page_token: str
    def __init__(self, search_ads_360_links: _Optional[_Iterable[_Union[_resources_pb2.SearchAds360Link, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateSearchAds360LinkRequest(_message.Message):
    __slots__ = ("parent", "search_ads_360_link")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ADS_360_LINK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    search_ads_360_link: _resources_pb2.SearchAds360Link
    def __init__(self, parent: _Optional[str] = ..., search_ads_360_link: _Optional[_Union[_resources_pb2.SearchAds360Link, _Mapping]] = ...) -> None: ...

class DeleteSearchAds360LinkRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateSearchAds360LinkRequest(_message.Message):
    __slots__ = ("search_ads_360_link", "update_mask")
    SEARCH_ADS_360_LINK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    search_ads_360_link: _resources_pb2.SearchAds360Link
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, search_ads_360_link: _Optional[_Union[_resources_pb2.SearchAds360Link, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

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

class CreateCalculatedMetricRequest(_message.Message):
    __slots__ = ("parent", "calculated_metric_id", "calculated_metric")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CALCULATED_METRIC_ID_FIELD_NUMBER: _ClassVar[int]
    CALCULATED_METRIC_FIELD_NUMBER: _ClassVar[int]
    parent: str
    calculated_metric_id: str
    calculated_metric: _resources_pb2.CalculatedMetric
    def __init__(self, parent: _Optional[str] = ..., calculated_metric_id: _Optional[str] = ..., calculated_metric: _Optional[_Union[_resources_pb2.CalculatedMetric, _Mapping]] = ...) -> None: ...

class UpdateCalculatedMetricRequest(_message.Message):
    __slots__ = ("calculated_metric", "update_mask")
    CALCULATED_METRIC_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    calculated_metric: _resources_pb2.CalculatedMetric
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, calculated_metric: _Optional[_Union[_resources_pb2.CalculatedMetric, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteCalculatedMetricRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListCalculatedMetricsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListCalculatedMetricsResponse(_message.Message):
    __slots__ = ("calculated_metrics", "next_page_token")
    CALCULATED_METRICS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    calculated_metrics: _containers.RepeatedCompositeFieldContainer[_resources_pb2.CalculatedMetric]
    next_page_token: str
    def __init__(self, calculated_metrics: _Optional[_Iterable[_Union[_resources_pb2.CalculatedMetric, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetCalculatedMetricRequest(_message.Message):
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

class GetAudienceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAudiencesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAudiencesResponse(_message.Message):
    __slots__ = ("audiences", "next_page_token")
    AUDIENCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    audiences: _containers.RepeatedCompositeFieldContainer[_audience_pb2.Audience]
    next_page_token: str
    def __init__(self, audiences: _Optional[_Iterable[_Union[_audience_pb2.Audience, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateAudienceRequest(_message.Message):
    __slots__ = ("parent", "audience")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    audience: _audience_pb2.Audience
    def __init__(self, parent: _Optional[str] = ..., audience: _Optional[_Union[_audience_pb2.Audience, _Mapping]] = ...) -> None: ...

class UpdateAudienceRequest(_message.Message):
    __slots__ = ("audience", "update_mask")
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    audience: _audience_pb2.Audience
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, audience: _Optional[_Union[_audience_pb2.Audience, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ArchiveAudienceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetAttributionSettingsRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateAttributionSettingsRequest(_message.Message):
    __slots__ = ("attribution_settings", "update_mask")
    ATTRIBUTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    attribution_settings: _resources_pb2.AttributionSettings
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, attribution_settings: _Optional[_Union[_resources_pb2.AttributionSettings, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetAccessBindingRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BatchGetAccessBindingsRequest(_message.Message):
    __slots__ = ("parent", "names")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[str] = ..., names: _Optional[_Iterable[str]] = ...) -> None: ...

class BatchGetAccessBindingsResponse(_message.Message):
    __slots__ = ("access_bindings",)
    ACCESS_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    access_bindings: _containers.RepeatedCompositeFieldContainer[_resources_pb2.AccessBinding]
    def __init__(self, access_bindings: _Optional[_Iterable[_Union[_resources_pb2.AccessBinding, _Mapping]]] = ...) -> None: ...

class ListAccessBindingsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAccessBindingsResponse(_message.Message):
    __slots__ = ("access_bindings", "next_page_token")
    ACCESS_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_bindings: _containers.RepeatedCompositeFieldContainer[_resources_pb2.AccessBinding]
    next_page_token: str
    def __init__(self, access_bindings: _Optional[_Iterable[_Union[_resources_pb2.AccessBinding, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateAccessBindingRequest(_message.Message):
    __slots__ = ("parent", "access_binding")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_BINDING_FIELD_NUMBER: _ClassVar[int]
    parent: str
    access_binding: _resources_pb2.AccessBinding
    def __init__(self, parent: _Optional[str] = ..., access_binding: _Optional[_Union[_resources_pb2.AccessBinding, _Mapping]] = ...) -> None: ...

class BatchCreateAccessBindingsRequest(_message.Message):
    __slots__ = ("parent", "requests")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[CreateAccessBindingRequest]
    def __init__(self, parent: _Optional[str] = ..., requests: _Optional[_Iterable[_Union[CreateAccessBindingRequest, _Mapping]]] = ...) -> None: ...

class BatchCreateAccessBindingsResponse(_message.Message):
    __slots__ = ("access_bindings",)
    ACCESS_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    access_bindings: _containers.RepeatedCompositeFieldContainer[_resources_pb2.AccessBinding]
    def __init__(self, access_bindings: _Optional[_Iterable[_Union[_resources_pb2.AccessBinding, _Mapping]]] = ...) -> None: ...

class UpdateAccessBindingRequest(_message.Message):
    __slots__ = ("access_binding",)
    ACCESS_BINDING_FIELD_NUMBER: _ClassVar[int]
    access_binding: _resources_pb2.AccessBinding
    def __init__(self, access_binding: _Optional[_Union[_resources_pb2.AccessBinding, _Mapping]] = ...) -> None: ...

class BatchUpdateAccessBindingsRequest(_message.Message):
    __slots__ = ("parent", "requests")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[UpdateAccessBindingRequest]
    def __init__(self, parent: _Optional[str] = ..., requests: _Optional[_Iterable[_Union[UpdateAccessBindingRequest, _Mapping]]] = ...) -> None: ...

class BatchUpdateAccessBindingsResponse(_message.Message):
    __slots__ = ("access_bindings",)
    ACCESS_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    access_bindings: _containers.RepeatedCompositeFieldContainer[_resources_pb2.AccessBinding]
    def __init__(self, access_bindings: _Optional[_Iterable[_Union[_resources_pb2.AccessBinding, _Mapping]]] = ...) -> None: ...

class DeleteAccessBindingRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BatchDeleteAccessBindingsRequest(_message.Message):
    __slots__ = ("parent", "requests")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[DeleteAccessBindingRequest]
    def __init__(self, parent: _Optional[str] = ..., requests: _Optional[_Iterable[_Union[DeleteAccessBindingRequest, _Mapping]]] = ...) -> None: ...

class CreateExpandedDataSetRequest(_message.Message):
    __slots__ = ("parent", "expanded_data_set")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXPANDED_DATA_SET_FIELD_NUMBER: _ClassVar[int]
    parent: str
    expanded_data_set: _expanded_data_set_pb2.ExpandedDataSet
    def __init__(self, parent: _Optional[str] = ..., expanded_data_set: _Optional[_Union[_expanded_data_set_pb2.ExpandedDataSet, _Mapping]] = ...) -> None: ...

class UpdateExpandedDataSetRequest(_message.Message):
    __slots__ = ("expanded_data_set", "update_mask")
    EXPANDED_DATA_SET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    expanded_data_set: _expanded_data_set_pb2.ExpandedDataSet
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, expanded_data_set: _Optional[_Union[_expanded_data_set_pb2.ExpandedDataSet, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteExpandedDataSetRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetExpandedDataSetRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListExpandedDataSetsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListExpandedDataSetsResponse(_message.Message):
    __slots__ = ("expanded_data_sets", "next_page_token")
    EXPANDED_DATA_SETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    expanded_data_sets: _containers.RepeatedCompositeFieldContainer[_expanded_data_set_pb2.ExpandedDataSet]
    next_page_token: str
    def __init__(self, expanded_data_sets: _Optional[_Iterable[_Union[_expanded_data_set_pb2.ExpandedDataSet, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateChannelGroupRequest(_message.Message):
    __slots__ = ("parent", "channel_group")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_GROUP_FIELD_NUMBER: _ClassVar[int]
    parent: str
    channel_group: _channel_group_pb2.ChannelGroup
    def __init__(self, parent: _Optional[str] = ..., channel_group: _Optional[_Union[_channel_group_pb2.ChannelGroup, _Mapping]] = ...) -> None: ...

class UpdateChannelGroupRequest(_message.Message):
    __slots__ = ("channel_group", "update_mask")
    CHANNEL_GROUP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    channel_group: _channel_group_pb2.ChannelGroup
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, channel_group: _Optional[_Union[_channel_group_pb2.ChannelGroup, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteChannelGroupRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetChannelGroupRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListChannelGroupsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListChannelGroupsResponse(_message.Message):
    __slots__ = ("channel_groups", "next_page_token")
    CHANNEL_GROUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    channel_groups: _containers.RepeatedCompositeFieldContainer[_channel_group_pb2.ChannelGroup]
    next_page_token: str
    def __init__(self, channel_groups: _Optional[_Iterable[_Union[_channel_group_pb2.ChannelGroup, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class SetAutomatedGa4ConfigurationOptOutRequest(_message.Message):
    __slots__ = ("property", "opt_out")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    OPT_OUT_FIELD_NUMBER: _ClassVar[int]
    property: str
    opt_out: bool
    def __init__(self, property: _Optional[str] = ..., opt_out: bool = ...) -> None: ...

class SetAutomatedGa4ConfigurationOptOutResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FetchAutomatedGa4ConfigurationOptOutRequest(_message.Message):
    __slots__ = ("property",)
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    property: str
    def __init__(self, property: _Optional[str] = ...) -> None: ...

class FetchAutomatedGa4ConfigurationOptOutResponse(_message.Message):
    __slots__ = ("opt_out",)
    OPT_OUT_FIELD_NUMBER: _ClassVar[int]
    opt_out: bool
    def __init__(self, opt_out: bool = ...) -> None: ...

class CreateBigQueryLinkRequest(_message.Message):
    __slots__ = ("parent", "bigquery_link")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_LINK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    bigquery_link: _resources_pb2.BigQueryLink
    def __init__(self, parent: _Optional[str] = ..., bigquery_link: _Optional[_Union[_resources_pb2.BigQueryLink, _Mapping]] = ...) -> None: ...

class GetBigQueryLinkRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListBigQueryLinksRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListBigQueryLinksResponse(_message.Message):
    __slots__ = ("bigquery_links", "next_page_token")
    BIGQUERY_LINKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    bigquery_links: _containers.RepeatedCompositeFieldContainer[_resources_pb2.BigQueryLink]
    next_page_token: str
    def __init__(self, bigquery_links: _Optional[_Iterable[_Union[_resources_pb2.BigQueryLink, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateBigQueryLinkRequest(_message.Message):
    __slots__ = ("bigquery_link", "update_mask")
    BIGQUERY_LINK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    bigquery_link: _resources_pb2.BigQueryLink
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, bigquery_link: _Optional[_Union[_resources_pb2.BigQueryLink, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteBigQueryLinkRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetEnhancedMeasurementSettingsRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateEnhancedMeasurementSettingsRequest(_message.Message):
    __slots__ = ("enhanced_measurement_settings", "update_mask")
    ENHANCED_MEASUREMENT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    enhanced_measurement_settings: _resources_pb2.EnhancedMeasurementSettings
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, enhanced_measurement_settings: _Optional[_Union[_resources_pb2.EnhancedMeasurementSettings, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetDataRedactionSettingsRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateDataRedactionSettingsRequest(_message.Message):
    __slots__ = ("data_redaction_settings", "update_mask")
    DATA_REDACTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    data_redaction_settings: _resources_pb2.DataRedactionSettings
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, data_redaction_settings: _Optional[_Union[_resources_pb2.DataRedactionSettings, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateConnectedSiteTagRequest(_message.Message):
    __slots__ = ("property", "connected_site_tag")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_SITE_TAG_FIELD_NUMBER: _ClassVar[int]
    property: str
    connected_site_tag: _resources_pb2.ConnectedSiteTag
    def __init__(self, property: _Optional[str] = ..., connected_site_tag: _Optional[_Union[_resources_pb2.ConnectedSiteTag, _Mapping]] = ...) -> None: ...

class CreateConnectedSiteTagResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteConnectedSiteTagRequest(_message.Message):
    __slots__ = ("property", "tag_id")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    TAG_ID_FIELD_NUMBER: _ClassVar[int]
    property: str
    tag_id: str
    def __init__(self, property: _Optional[str] = ..., tag_id: _Optional[str] = ...) -> None: ...

class ListConnectedSiteTagsRequest(_message.Message):
    __slots__ = ("property",)
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    property: str
    def __init__(self, property: _Optional[str] = ...) -> None: ...

class ListConnectedSiteTagsResponse(_message.Message):
    __slots__ = ("connected_site_tags",)
    CONNECTED_SITE_TAGS_FIELD_NUMBER: _ClassVar[int]
    connected_site_tags: _containers.RepeatedCompositeFieldContainer[_resources_pb2.ConnectedSiteTag]
    def __init__(self, connected_site_tags: _Optional[_Iterable[_Union[_resources_pb2.ConnectedSiteTag, _Mapping]]] = ...) -> None: ...

class CreateAdSenseLinkRequest(_message.Message):
    __slots__ = ("parent", "adsense_link")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ADSENSE_LINK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    adsense_link: _resources_pb2.AdSenseLink
    def __init__(self, parent: _Optional[str] = ..., adsense_link: _Optional[_Union[_resources_pb2.AdSenseLink, _Mapping]] = ...) -> None: ...

class GetAdSenseLinkRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteAdSenseLinkRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAdSenseLinksRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAdSenseLinksResponse(_message.Message):
    __slots__ = ("adsense_links", "next_page_token")
    ADSENSE_LINKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    adsense_links: _containers.RepeatedCompositeFieldContainer[_resources_pb2.AdSenseLink]
    next_page_token: str
    def __init__(self, adsense_links: _Optional[_Iterable[_Union[_resources_pb2.AdSenseLink, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class FetchConnectedGa4PropertyRequest(_message.Message):
    __slots__ = ("property",)
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    property: str
    def __init__(self, property: _Optional[str] = ...) -> None: ...

class FetchConnectedGa4PropertyResponse(_message.Message):
    __slots__ = ("property",)
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    property: str
    def __init__(self, property: _Optional[str] = ...) -> None: ...

class CreateEventCreateRuleRequest(_message.Message):
    __slots__ = ("parent", "event_create_rule")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EVENT_CREATE_RULE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    event_create_rule: _event_create_and_edit_pb2.EventCreateRule
    def __init__(self, parent: _Optional[str] = ..., event_create_rule: _Optional[_Union[_event_create_and_edit_pb2.EventCreateRule, _Mapping]] = ...) -> None: ...

class UpdateEventCreateRuleRequest(_message.Message):
    __slots__ = ("event_create_rule", "update_mask")
    EVENT_CREATE_RULE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    event_create_rule: _event_create_and_edit_pb2.EventCreateRule
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, event_create_rule: _Optional[_Union[_event_create_and_edit_pb2.EventCreateRule, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteEventCreateRuleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetEventCreateRuleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListEventCreateRulesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListEventCreateRulesResponse(_message.Message):
    __slots__ = ("event_create_rules", "next_page_token")
    EVENT_CREATE_RULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    event_create_rules: _containers.RepeatedCompositeFieldContainer[_event_create_and_edit_pb2.EventCreateRule]
    next_page_token: str
    def __init__(self, event_create_rules: _Optional[_Iterable[_Union[_event_create_and_edit_pb2.EventCreateRule, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateEventEditRuleRequest(_message.Message):
    __slots__ = ("parent", "event_edit_rule")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EVENT_EDIT_RULE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    event_edit_rule: _event_create_and_edit_pb2.EventEditRule
    def __init__(self, parent: _Optional[str] = ..., event_edit_rule: _Optional[_Union[_event_create_and_edit_pb2.EventEditRule, _Mapping]] = ...) -> None: ...

class UpdateEventEditRuleRequest(_message.Message):
    __slots__ = ("event_edit_rule", "update_mask")
    EVENT_EDIT_RULE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    event_edit_rule: _event_create_and_edit_pb2.EventEditRule
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, event_edit_rule: _Optional[_Union[_event_create_and_edit_pb2.EventEditRule, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteEventEditRuleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetEventEditRuleRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListEventEditRulesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListEventEditRulesResponse(_message.Message):
    __slots__ = ("event_edit_rules", "next_page_token")
    EVENT_EDIT_RULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    event_edit_rules: _containers.RepeatedCompositeFieldContainer[_event_create_and_edit_pb2.EventEditRule]
    next_page_token: str
    def __init__(self, event_edit_rules: _Optional[_Iterable[_Union[_event_create_and_edit_pb2.EventEditRule, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ReorderEventEditRulesRequest(_message.Message):
    __slots__ = ("parent", "event_edit_rules")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EVENT_EDIT_RULES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    event_edit_rules: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[str] = ..., event_edit_rules: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateRollupPropertyRequest(_message.Message):
    __slots__ = ("rollup_property", "source_properties")
    ROLLUP_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    rollup_property: _resources_pb2.Property
    source_properties: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, rollup_property: _Optional[_Union[_resources_pb2.Property, _Mapping]] = ..., source_properties: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateRollupPropertyResponse(_message.Message):
    __slots__ = ("rollup_property", "rollup_property_source_links")
    ROLLUP_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    ROLLUP_PROPERTY_SOURCE_LINKS_FIELD_NUMBER: _ClassVar[int]
    rollup_property: _resources_pb2.Property
    rollup_property_source_links: _containers.RepeatedCompositeFieldContainer[_resources_pb2.RollupPropertySourceLink]
    def __init__(self, rollup_property: _Optional[_Union[_resources_pb2.Property, _Mapping]] = ..., rollup_property_source_links: _Optional[_Iterable[_Union[_resources_pb2.RollupPropertySourceLink, _Mapping]]] = ...) -> None: ...

class GetRollupPropertySourceLinkRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListRollupPropertySourceLinksRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListRollupPropertySourceLinksResponse(_message.Message):
    __slots__ = ("rollup_property_source_links", "next_page_token")
    ROLLUP_PROPERTY_SOURCE_LINKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    rollup_property_source_links: _containers.RepeatedCompositeFieldContainer[_resources_pb2.RollupPropertySourceLink]
    next_page_token: str
    def __init__(self, rollup_property_source_links: _Optional[_Iterable[_Union[_resources_pb2.RollupPropertySourceLink, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateRollupPropertySourceLinkRequest(_message.Message):
    __slots__ = ("parent", "rollup_property_source_link")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ROLLUP_PROPERTY_SOURCE_LINK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    rollup_property_source_link: _resources_pb2.RollupPropertySourceLink
    def __init__(self, parent: _Optional[str] = ..., rollup_property_source_link: _Optional[_Union[_resources_pb2.RollupPropertySourceLink, _Mapping]] = ...) -> None: ...

class DeleteRollupPropertySourceLinkRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ProvisionSubpropertyRequest(_message.Message):
    __slots__ = ("subproperty", "subproperty_event_filter")
    SUBPROPERTY_FIELD_NUMBER: _ClassVar[int]
    SUBPROPERTY_EVENT_FILTER_FIELD_NUMBER: _ClassVar[int]
    subproperty: _resources_pb2.Property
    subproperty_event_filter: _subproperty_event_filter_pb2.SubpropertyEventFilter
    def __init__(self, subproperty: _Optional[_Union[_resources_pb2.Property, _Mapping]] = ..., subproperty_event_filter: _Optional[_Union[_subproperty_event_filter_pb2.SubpropertyEventFilter, _Mapping]] = ...) -> None: ...

class ProvisionSubpropertyResponse(_message.Message):
    __slots__ = ("subproperty", "subproperty_event_filter")
    SUBPROPERTY_FIELD_NUMBER: _ClassVar[int]
    SUBPROPERTY_EVENT_FILTER_FIELD_NUMBER: _ClassVar[int]
    subproperty: _resources_pb2.Property
    subproperty_event_filter: _subproperty_event_filter_pb2.SubpropertyEventFilter
    def __init__(self, subproperty: _Optional[_Union[_resources_pb2.Property, _Mapping]] = ..., subproperty_event_filter: _Optional[_Union[_subproperty_event_filter_pb2.SubpropertyEventFilter, _Mapping]] = ...) -> None: ...

class CreateSubpropertyEventFilterRequest(_message.Message):
    __slots__ = ("parent", "subproperty_event_filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SUBPROPERTY_EVENT_FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    subproperty_event_filter: _subproperty_event_filter_pb2.SubpropertyEventFilter
    def __init__(self, parent: _Optional[str] = ..., subproperty_event_filter: _Optional[_Union[_subproperty_event_filter_pb2.SubpropertyEventFilter, _Mapping]] = ...) -> None: ...

class GetSubpropertyEventFilterRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListSubpropertyEventFiltersRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListSubpropertyEventFiltersResponse(_message.Message):
    __slots__ = ("subproperty_event_filters", "next_page_token")
    SUBPROPERTY_EVENT_FILTERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    subproperty_event_filters: _containers.RepeatedCompositeFieldContainer[_subproperty_event_filter_pb2.SubpropertyEventFilter]
    next_page_token: str
    def __init__(self, subproperty_event_filters: _Optional[_Iterable[_Union[_subproperty_event_filter_pb2.SubpropertyEventFilter, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateSubpropertyEventFilterRequest(_message.Message):
    __slots__ = ("subproperty_event_filter", "update_mask")
    SUBPROPERTY_EVENT_FILTER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    subproperty_event_filter: _subproperty_event_filter_pb2.SubpropertyEventFilter
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, subproperty_event_filter: _Optional[_Union[_subproperty_event_filter_pb2.SubpropertyEventFilter, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteSubpropertyEventFilterRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
