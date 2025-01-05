from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.bigquery.datatransfer.v1 import transfer_pb2 as _transfer_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataSourceParameter(_message.Message):
    __slots__ = ("param_id", "display_name", "description", "type", "required", "repeated", "validation_regex", "allowed_values", "min_value", "max_value", "fields", "validation_description", "validation_help_url", "immutable", "recurse", "deprecated")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[DataSourceParameter.Type]
        STRING: _ClassVar[DataSourceParameter.Type]
        INTEGER: _ClassVar[DataSourceParameter.Type]
        DOUBLE: _ClassVar[DataSourceParameter.Type]
        BOOLEAN: _ClassVar[DataSourceParameter.Type]
        RECORD: _ClassVar[DataSourceParameter.Type]
        PLUS_PAGE: _ClassVar[DataSourceParameter.Type]
        LIST: _ClassVar[DataSourceParameter.Type]
    TYPE_UNSPECIFIED: DataSourceParameter.Type
    STRING: DataSourceParameter.Type
    INTEGER: DataSourceParameter.Type
    DOUBLE: DataSourceParameter.Type
    BOOLEAN: DataSourceParameter.Type
    RECORD: DataSourceParameter.Type
    PLUS_PAGE: DataSourceParameter.Type
    LIST: DataSourceParameter.Type
    PARAM_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    REPEATED_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_REGEX_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_VALUES_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_HELP_URL_FIELD_NUMBER: _ClassVar[int]
    IMMUTABLE_FIELD_NUMBER: _ClassVar[int]
    RECURSE_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    param_id: str
    display_name: str
    description: str
    type: DataSourceParameter.Type
    required: bool
    repeated: bool
    validation_regex: str
    allowed_values: _containers.RepeatedScalarFieldContainer[str]
    min_value: _wrappers_pb2.DoubleValue
    max_value: _wrappers_pb2.DoubleValue
    fields: _containers.RepeatedCompositeFieldContainer[DataSourceParameter]
    validation_description: str
    validation_help_url: str
    immutable: bool
    recurse: bool
    deprecated: bool
    def __init__(self, param_id: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[DataSourceParameter.Type, str]] = ..., required: bool = ..., repeated: bool = ..., validation_regex: _Optional[str] = ..., allowed_values: _Optional[_Iterable[str]] = ..., min_value: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., max_value: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., fields: _Optional[_Iterable[_Union[DataSourceParameter, _Mapping]]] = ..., validation_description: _Optional[str] = ..., validation_help_url: _Optional[str] = ..., immutable: bool = ..., recurse: bool = ..., deprecated: bool = ...) -> None: ...

class DataSource(_message.Message):
    __slots__ = ("name", "data_source_id", "display_name", "description", "client_id", "scopes", "transfer_type", "supports_multiple_transfers", "update_deadline_seconds", "default_schedule", "supports_custom_schedule", "parameters", "help_url", "authorization_type", "data_refresh_type", "default_data_refresh_window_days", "manual_runs_disabled", "minimum_schedule_interval")
    class AuthorizationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AUTHORIZATION_TYPE_UNSPECIFIED: _ClassVar[DataSource.AuthorizationType]
        AUTHORIZATION_CODE: _ClassVar[DataSource.AuthorizationType]
        GOOGLE_PLUS_AUTHORIZATION_CODE: _ClassVar[DataSource.AuthorizationType]
        FIRST_PARTY_OAUTH: _ClassVar[DataSource.AuthorizationType]
    AUTHORIZATION_TYPE_UNSPECIFIED: DataSource.AuthorizationType
    AUTHORIZATION_CODE: DataSource.AuthorizationType
    GOOGLE_PLUS_AUTHORIZATION_CODE: DataSource.AuthorizationType
    FIRST_PARTY_OAUTH: DataSource.AuthorizationType
    class DataRefreshType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_REFRESH_TYPE_UNSPECIFIED: _ClassVar[DataSource.DataRefreshType]
        SLIDING_WINDOW: _ClassVar[DataSource.DataRefreshType]
        CUSTOM_SLIDING_WINDOW: _ClassVar[DataSource.DataRefreshType]
    DATA_REFRESH_TYPE_UNSPECIFIED: DataSource.DataRefreshType
    SLIDING_WINDOW: DataSource.DataRefreshType
    CUSTOM_SLIDING_WINDOW: DataSource.DataRefreshType
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_MULTIPLE_TRANSFERS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_DEADLINE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_CUSTOM_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    HELP_URL_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_REFRESH_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DATA_REFRESH_WINDOW_DAYS_FIELD_NUMBER: _ClassVar[int]
    MANUAL_RUNS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_SCHEDULE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    data_source_id: str
    display_name: str
    description: str
    client_id: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    transfer_type: _transfer_pb2.TransferType
    supports_multiple_transfers: bool
    update_deadline_seconds: int
    default_schedule: str
    supports_custom_schedule: bool
    parameters: _containers.RepeatedCompositeFieldContainer[DataSourceParameter]
    help_url: str
    authorization_type: DataSource.AuthorizationType
    data_refresh_type: DataSource.DataRefreshType
    default_data_refresh_window_days: int
    manual_runs_disabled: bool
    minimum_schedule_interval: _duration_pb2.Duration
    def __init__(self, name: _Optional[str] = ..., data_source_id: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., client_id: _Optional[str] = ..., scopes: _Optional[_Iterable[str]] = ..., transfer_type: _Optional[_Union[_transfer_pb2.TransferType, str]] = ..., supports_multiple_transfers: bool = ..., update_deadline_seconds: _Optional[int] = ..., default_schedule: _Optional[str] = ..., supports_custom_schedule: bool = ..., parameters: _Optional[_Iterable[_Union[DataSourceParameter, _Mapping]]] = ..., help_url: _Optional[str] = ..., authorization_type: _Optional[_Union[DataSource.AuthorizationType, str]] = ..., data_refresh_type: _Optional[_Union[DataSource.DataRefreshType, str]] = ..., default_data_refresh_window_days: _Optional[int] = ..., manual_runs_disabled: bool = ..., minimum_schedule_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class GetDataSourceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListDataSourcesRequest(_message.Message):
    __slots__ = ("parent", "page_token", "page_size")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int
    def __init__(self, parent: _Optional[str] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListDataSourcesResponse(_message.Message):
    __slots__ = ("data_sources", "next_page_token")
    DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    data_sources: _containers.RepeatedCompositeFieldContainer[DataSource]
    next_page_token: str
    def __init__(self, data_sources: _Optional[_Iterable[_Union[DataSource, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateTransferConfigRequest(_message.Message):
    __slots__ = ("parent", "transfer_config", "authorization_code", "version_info", "service_account_name")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_CODE_FIELD_NUMBER: _ClassVar[int]
    VERSION_INFO_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    parent: str
    transfer_config: _transfer_pb2.TransferConfig
    authorization_code: str
    version_info: str
    service_account_name: str
    def __init__(self, parent: _Optional[str] = ..., transfer_config: _Optional[_Union[_transfer_pb2.TransferConfig, _Mapping]] = ..., authorization_code: _Optional[str] = ..., version_info: _Optional[str] = ..., service_account_name: _Optional[str] = ...) -> None: ...

class UpdateTransferConfigRequest(_message.Message):
    __slots__ = ("transfer_config", "authorization_code", "update_mask", "version_info", "service_account_name")
    TRANSFER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_CODE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VERSION_INFO_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    transfer_config: _transfer_pb2.TransferConfig
    authorization_code: str
    update_mask: _field_mask_pb2.FieldMask
    version_info: str
    service_account_name: str
    def __init__(self, transfer_config: _Optional[_Union[_transfer_pb2.TransferConfig, _Mapping]] = ..., authorization_code: _Optional[str] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., version_info: _Optional[str] = ..., service_account_name: _Optional[str] = ...) -> None: ...

class GetTransferConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteTransferConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetTransferRunRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteTransferRunRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListTransferConfigsRequest(_message.Message):
    __slots__ = ("parent", "data_source_ids", "page_token", "page_size")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_IDS_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    data_source_ids: _containers.RepeatedScalarFieldContainer[str]
    page_token: str
    page_size: int
    def __init__(self, parent: _Optional[str] = ..., data_source_ids: _Optional[_Iterable[str]] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListTransferConfigsResponse(_message.Message):
    __slots__ = ("transfer_configs", "next_page_token")
    TRANSFER_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    transfer_configs: _containers.RepeatedCompositeFieldContainer[_transfer_pb2.TransferConfig]
    next_page_token: str
    def __init__(self, transfer_configs: _Optional[_Iterable[_Union[_transfer_pb2.TransferConfig, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListTransferRunsRequest(_message.Message):
    __slots__ = ("parent", "states", "page_token", "page_size", "run_attempt")
    class RunAttempt(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RUN_ATTEMPT_UNSPECIFIED: _ClassVar[ListTransferRunsRequest.RunAttempt]
        LATEST: _ClassVar[ListTransferRunsRequest.RunAttempt]
    RUN_ATTEMPT_UNSPECIFIED: ListTransferRunsRequest.RunAttempt
    LATEST: ListTransferRunsRequest.RunAttempt
    PARENT_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    RUN_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    states: _containers.RepeatedScalarFieldContainer[_transfer_pb2.TransferState]
    page_token: str
    page_size: int
    run_attempt: ListTransferRunsRequest.RunAttempt
    def __init__(self, parent: _Optional[str] = ..., states: _Optional[_Iterable[_Union[_transfer_pb2.TransferState, str]]] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ..., run_attempt: _Optional[_Union[ListTransferRunsRequest.RunAttempt, str]] = ...) -> None: ...

class ListTransferRunsResponse(_message.Message):
    __slots__ = ("transfer_runs", "next_page_token")
    TRANSFER_RUNS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    transfer_runs: _containers.RepeatedCompositeFieldContainer[_transfer_pb2.TransferRun]
    next_page_token: str
    def __init__(self, transfer_runs: _Optional[_Iterable[_Union[_transfer_pb2.TransferRun, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListTransferLogsRequest(_message.Message):
    __slots__ = ("parent", "page_token", "page_size", "message_types")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int
    message_types: _containers.RepeatedScalarFieldContainer[_transfer_pb2.TransferMessage.MessageSeverity]
    def __init__(self, parent: _Optional[str] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ..., message_types: _Optional[_Iterable[_Union[_transfer_pb2.TransferMessage.MessageSeverity, str]]] = ...) -> None: ...

class ListTransferLogsResponse(_message.Message):
    __slots__ = ("transfer_messages", "next_page_token")
    TRANSFER_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    transfer_messages: _containers.RepeatedCompositeFieldContainer[_transfer_pb2.TransferMessage]
    next_page_token: str
    def __init__(self, transfer_messages: _Optional[_Iterable[_Union[_transfer_pb2.TransferMessage, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CheckValidCredsRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CheckValidCredsResponse(_message.Message):
    __slots__ = ("has_valid_creds",)
    HAS_VALID_CREDS_FIELD_NUMBER: _ClassVar[int]
    has_valid_creds: bool
    def __init__(self, has_valid_creds: bool = ...) -> None: ...

class ScheduleTransferRunsRequest(_message.Message):
    __slots__ = ("parent", "start_time", "end_time")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    parent: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, parent: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ScheduleTransferRunsResponse(_message.Message):
    __slots__ = ("runs",)
    RUNS_FIELD_NUMBER: _ClassVar[int]
    runs: _containers.RepeatedCompositeFieldContainer[_transfer_pb2.TransferRun]
    def __init__(self, runs: _Optional[_Iterable[_Union[_transfer_pb2.TransferRun, _Mapping]]] = ...) -> None: ...

class StartManualTransferRunsRequest(_message.Message):
    __slots__ = ("parent", "requested_time_range", "requested_run_time")
    class TimeRange(_message.Message):
        __slots__ = ("start_time", "end_time")
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        start_time: _timestamp_pb2.Timestamp
        end_time: _timestamp_pb2.Timestamp
        def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_RUN_TIME_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requested_time_range: StartManualTransferRunsRequest.TimeRange
    requested_run_time: _timestamp_pb2.Timestamp
    def __init__(self, parent: _Optional[str] = ..., requested_time_range: _Optional[_Union[StartManualTransferRunsRequest.TimeRange, _Mapping]] = ..., requested_run_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StartManualTransferRunsResponse(_message.Message):
    __slots__ = ("runs",)
    RUNS_FIELD_NUMBER: _ClassVar[int]
    runs: _containers.RepeatedCompositeFieldContainer[_transfer_pb2.TransferRun]
    def __init__(self, runs: _Optional[_Iterable[_Union[_transfer_pb2.TransferRun, _Mapping]]] = ...) -> None: ...

class EnrollDataSourcesRequest(_message.Message):
    __slots__ = ("name", "data_source_ids")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_IDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    data_source_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., data_source_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class UnenrollDataSourcesRequest(_message.Message):
    __slots__ = ("name", "data_source_ids")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_IDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    data_source_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., data_source_ids: _Optional[_Iterable[str]] = ...) -> None: ...
