from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.retail.v2 import product_pb2 as _product_pb2
from google.cloud.retail.v2 import user_event_pb2 as _user_event_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GcsSource(_message.Message):
    __slots__ = ("input_uris", "data_schema")
    INPUT_URIS_FIELD_NUMBER: _ClassVar[int]
    DATA_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    input_uris: _containers.RepeatedScalarFieldContainer[str]
    data_schema: str
    def __init__(self, input_uris: _Optional[_Iterable[str]] = ..., data_schema: _Optional[str] = ...) -> None: ...

class BigQuerySource(_message.Message):
    __slots__ = ("partition_date", "project_id", "dataset_id", "table_id", "gcs_staging_dir", "data_schema")
    PARTITION_DATE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    GCS_STAGING_DIR_FIELD_NUMBER: _ClassVar[int]
    DATA_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    partition_date: _date_pb2.Date
    project_id: str
    dataset_id: str
    table_id: str
    gcs_staging_dir: str
    data_schema: str
    def __init__(self, partition_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., project_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., table_id: _Optional[str] = ..., gcs_staging_dir: _Optional[str] = ..., data_schema: _Optional[str] = ...) -> None: ...

class ProductInlineSource(_message.Message):
    __slots__ = ("products",)
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    products: _containers.RepeatedCompositeFieldContainer[_product_pb2.Product]
    def __init__(self, products: _Optional[_Iterable[_Union[_product_pb2.Product, _Mapping]]] = ...) -> None: ...

class UserEventInlineSource(_message.Message):
    __slots__ = ("user_events",)
    USER_EVENTS_FIELD_NUMBER: _ClassVar[int]
    user_events: _containers.RepeatedCompositeFieldContainer[_user_event_pb2.UserEvent]
    def __init__(self, user_events: _Optional[_Iterable[_Union[_user_event_pb2.UserEvent, _Mapping]]] = ...) -> None: ...

class ImportErrorsConfig(_message.Message):
    __slots__ = ("gcs_prefix",)
    GCS_PREFIX_FIELD_NUMBER: _ClassVar[int]
    gcs_prefix: str
    def __init__(self, gcs_prefix: _Optional[str] = ...) -> None: ...

class ImportProductsRequest(_message.Message):
    __slots__ = ("parent", "request_id", "input_config", "errors_config", "update_mask", "reconciliation_mode", "notification_pubsub_topic")
    class ReconciliationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RECONCILIATION_MODE_UNSPECIFIED: _ClassVar[ImportProductsRequest.ReconciliationMode]
        INCREMENTAL: _ClassVar[ImportProductsRequest.ReconciliationMode]
        FULL: _ClassVar[ImportProductsRequest.ReconciliationMode]
    RECONCILIATION_MODE_UNSPECIFIED: ImportProductsRequest.ReconciliationMode
    INCREMENTAL: ImportProductsRequest.ReconciliationMode
    FULL: ImportProductsRequest.ReconciliationMode
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ERRORS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    RECONCILIATION_MODE_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_PUBSUB_TOPIC_FIELD_NUMBER: _ClassVar[int]
    parent: str
    request_id: str
    input_config: ProductInputConfig
    errors_config: ImportErrorsConfig
    update_mask: _field_mask_pb2.FieldMask
    reconciliation_mode: ImportProductsRequest.ReconciliationMode
    notification_pubsub_topic: str
    def __init__(self, parent: _Optional[str] = ..., request_id: _Optional[str] = ..., input_config: _Optional[_Union[ProductInputConfig, _Mapping]] = ..., errors_config: _Optional[_Union[ImportErrorsConfig, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., reconciliation_mode: _Optional[_Union[ImportProductsRequest.ReconciliationMode, str]] = ..., notification_pubsub_topic: _Optional[str] = ...) -> None: ...

class ImportUserEventsRequest(_message.Message):
    __slots__ = ("parent", "input_config", "errors_config")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ERRORS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    input_config: UserEventInputConfig
    errors_config: ImportErrorsConfig
    def __init__(self, parent: _Optional[str] = ..., input_config: _Optional[_Union[UserEventInputConfig, _Mapping]] = ..., errors_config: _Optional[_Union[ImportErrorsConfig, _Mapping]] = ...) -> None: ...

class ImportCompletionDataRequest(_message.Message):
    __slots__ = ("parent", "input_config", "notification_pubsub_topic")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_PUBSUB_TOPIC_FIELD_NUMBER: _ClassVar[int]
    parent: str
    input_config: CompletionDataInputConfig
    notification_pubsub_topic: str
    def __init__(self, parent: _Optional[str] = ..., input_config: _Optional[_Union[CompletionDataInputConfig, _Mapping]] = ..., notification_pubsub_topic: _Optional[str] = ...) -> None: ...

class ProductInputConfig(_message.Message):
    __slots__ = ("product_inline_source", "gcs_source", "big_query_source")
    PRODUCT_INLINE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    BIG_QUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    product_inline_source: ProductInlineSource
    gcs_source: GcsSource
    big_query_source: BigQuerySource
    def __init__(self, product_inline_source: _Optional[_Union[ProductInlineSource, _Mapping]] = ..., gcs_source: _Optional[_Union[GcsSource, _Mapping]] = ..., big_query_source: _Optional[_Union[BigQuerySource, _Mapping]] = ...) -> None: ...

class UserEventInputConfig(_message.Message):
    __slots__ = ("user_event_inline_source", "gcs_source", "big_query_source")
    USER_EVENT_INLINE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    BIG_QUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    user_event_inline_source: UserEventInlineSource
    gcs_source: GcsSource
    big_query_source: BigQuerySource
    def __init__(self, user_event_inline_source: _Optional[_Union[UserEventInlineSource, _Mapping]] = ..., gcs_source: _Optional[_Union[GcsSource, _Mapping]] = ..., big_query_source: _Optional[_Union[BigQuerySource, _Mapping]] = ...) -> None: ...

class CompletionDataInputConfig(_message.Message):
    __slots__ = ("big_query_source",)
    BIG_QUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    big_query_source: BigQuerySource
    def __init__(self, big_query_source: _Optional[_Union[BigQuerySource, _Mapping]] = ...) -> None: ...

class ImportMetadata(_message.Message):
    __slots__ = ("create_time", "update_time", "success_count", "failure_count", "request_id", "notification_pubsub_topic")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_PUBSUB_TOPIC_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    success_count: int
    failure_count: int
    request_id: str
    notification_pubsub_topic: str
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., success_count: _Optional[int] = ..., failure_count: _Optional[int] = ..., request_id: _Optional[str] = ..., notification_pubsub_topic: _Optional[str] = ...) -> None: ...

class ImportProductsResponse(_message.Message):
    __slots__ = ("error_samples", "errors_config")
    ERROR_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    ERRORS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    error_samples: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    errors_config: ImportErrorsConfig
    def __init__(self, error_samples: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ..., errors_config: _Optional[_Union[ImportErrorsConfig, _Mapping]] = ...) -> None: ...

class ImportUserEventsResponse(_message.Message):
    __slots__ = ("error_samples", "errors_config", "import_summary")
    ERROR_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    ERRORS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IMPORT_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    error_samples: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    errors_config: ImportErrorsConfig
    import_summary: UserEventImportSummary
    def __init__(self, error_samples: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ..., errors_config: _Optional[_Union[ImportErrorsConfig, _Mapping]] = ..., import_summary: _Optional[_Union[UserEventImportSummary, _Mapping]] = ...) -> None: ...

class UserEventImportSummary(_message.Message):
    __slots__ = ("joined_events_count", "unjoined_events_count")
    JOINED_EVENTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNJOINED_EVENTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    joined_events_count: int
    unjoined_events_count: int
    def __init__(self, joined_events_count: _Optional[int] = ..., unjoined_events_count: _Optional[int] = ...) -> None: ...

class ImportCompletionDataResponse(_message.Message):
    __slots__ = ("error_samples",)
    ERROR_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    error_samples: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    def __init__(self, error_samples: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ...) -> None: ...
