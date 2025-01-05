from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.recommendationengine.v1beta1 import catalog_pb2 as _catalog_pb2
from google.cloud.recommendationengine.v1beta1 import user_event_pb2 as _user_event_pb2
from google.cloud.recommendationengine.v1beta1 import recommendationengine_resources_pb2 as _recommendationengine_resources_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GcsSource(_message.Message):
    __slots__ = ('input_uris',)
    INPUT_URIS_FIELD_NUMBER: _ClassVar[int]
    input_uris: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, input_uris: _Optional[_Iterable[str]]=...) -> None:
        ...

class CatalogInlineSource(_message.Message):
    __slots__ = ('catalog_items',)
    CATALOG_ITEMS_FIELD_NUMBER: _ClassVar[int]
    catalog_items: _containers.RepeatedCompositeFieldContainer[_catalog_pb2.CatalogItem]

    def __init__(self, catalog_items: _Optional[_Iterable[_Union[_catalog_pb2.CatalogItem, _Mapping]]]=...) -> None:
        ...

class UserEventInlineSource(_message.Message):
    __slots__ = ('user_events',)
    USER_EVENTS_FIELD_NUMBER: _ClassVar[int]
    user_events: _containers.RepeatedCompositeFieldContainer[_user_event_pb2.UserEvent]

    def __init__(self, user_events: _Optional[_Iterable[_Union[_user_event_pb2.UserEvent, _Mapping]]]=...) -> None:
        ...

class ImportErrorsConfig(_message.Message):
    __slots__ = ('gcs_prefix',)
    GCS_PREFIX_FIELD_NUMBER: _ClassVar[int]
    gcs_prefix: str

    def __init__(self, gcs_prefix: _Optional[str]=...) -> None:
        ...

class ImportCatalogItemsRequest(_message.Message):
    __slots__ = ('parent', 'request_id', 'input_config', 'errors_config')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ERRORS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    request_id: str
    input_config: InputConfig
    errors_config: ImportErrorsConfig

    def __init__(self, parent: _Optional[str]=..., request_id: _Optional[str]=..., input_config: _Optional[_Union[InputConfig, _Mapping]]=..., errors_config: _Optional[_Union[ImportErrorsConfig, _Mapping]]=...) -> None:
        ...

class ImportUserEventsRequest(_message.Message):
    __slots__ = ('parent', 'request_id', 'input_config', 'errors_config')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ERRORS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    request_id: str
    input_config: InputConfig
    errors_config: ImportErrorsConfig

    def __init__(self, parent: _Optional[str]=..., request_id: _Optional[str]=..., input_config: _Optional[_Union[InputConfig, _Mapping]]=..., errors_config: _Optional[_Union[ImportErrorsConfig, _Mapping]]=...) -> None:
        ...

class InputConfig(_message.Message):
    __slots__ = ('catalog_inline_source', 'gcs_source', 'user_event_inline_source')
    CATALOG_INLINE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    USER_EVENT_INLINE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    catalog_inline_source: CatalogInlineSource
    gcs_source: GcsSource
    user_event_inline_source: UserEventInlineSource

    def __init__(self, catalog_inline_source: _Optional[_Union[CatalogInlineSource, _Mapping]]=..., gcs_source: _Optional[_Union[GcsSource, _Mapping]]=..., user_event_inline_source: _Optional[_Union[UserEventInlineSource, _Mapping]]=...) -> None:
        ...

class ImportMetadata(_message.Message):
    __slots__ = ('operation_name', 'request_id', 'create_time', 'success_count', 'failure_count', 'update_time')
    OPERATION_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    operation_name: str
    request_id: str
    create_time: _timestamp_pb2.Timestamp
    success_count: int
    failure_count: int
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, operation_name: _Optional[str]=..., request_id: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., success_count: _Optional[int]=..., failure_count: _Optional[int]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ImportCatalogItemsResponse(_message.Message):
    __slots__ = ('error_samples', 'errors_config')
    ERROR_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    ERRORS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    error_samples: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    errors_config: ImportErrorsConfig

    def __init__(self, error_samples: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=..., errors_config: _Optional[_Union[ImportErrorsConfig, _Mapping]]=...) -> None:
        ...

class ImportUserEventsResponse(_message.Message):
    __slots__ = ('error_samples', 'errors_config', 'import_summary')
    ERROR_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    ERRORS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IMPORT_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    error_samples: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    errors_config: ImportErrorsConfig
    import_summary: UserEventImportSummary

    def __init__(self, error_samples: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=..., errors_config: _Optional[_Union[ImportErrorsConfig, _Mapping]]=..., import_summary: _Optional[_Union[UserEventImportSummary, _Mapping]]=...) -> None:
        ...

class UserEventImportSummary(_message.Message):
    __slots__ = ('joined_events_count', 'unjoined_events_count')
    JOINED_EVENTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNJOINED_EVENTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    joined_events_count: int
    unjoined_events_count: int

    def __init__(self, joined_events_count: _Optional[int]=..., unjoined_events_count: _Optional[int]=...) -> None:
        ...