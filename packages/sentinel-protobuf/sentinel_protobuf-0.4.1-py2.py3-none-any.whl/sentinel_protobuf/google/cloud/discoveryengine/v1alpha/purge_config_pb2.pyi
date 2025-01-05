from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1alpha import import_config_pb2 as _import_config_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PurgeUserEventsRequest(_message.Message):
    __slots__ = ("parent", "filter", "force")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    force: bool
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., force: bool = ...) -> None: ...

class PurgeUserEventsResponse(_message.Message):
    __slots__ = ("purge_count",)
    PURGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    purge_count: int
    def __init__(self, purge_count: _Optional[int] = ...) -> None: ...

class PurgeUserEventsMetadata(_message.Message):
    __slots__ = ("create_time", "update_time", "success_count", "failure_count")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    success_count: int
    failure_count: int
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., success_count: _Optional[int] = ..., failure_count: _Optional[int] = ...) -> None: ...

class PurgeErrorConfig(_message.Message):
    __slots__ = ("gcs_prefix",)
    GCS_PREFIX_FIELD_NUMBER: _ClassVar[int]
    gcs_prefix: str
    def __init__(self, gcs_prefix: _Optional[str] = ...) -> None: ...

class PurgeDocumentsRequest(_message.Message):
    __slots__ = ("gcs_source", "inline_source", "parent", "filter", "error_config", "force")
    class InlineSource(_message.Message):
        __slots__ = ("documents",)
        DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
        documents: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, documents: _Optional[_Iterable[str]] = ...) -> None: ...
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    INLINE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ERROR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    gcs_source: _import_config_pb2.GcsSource
    inline_source: PurgeDocumentsRequest.InlineSource
    parent: str
    filter: str
    error_config: PurgeErrorConfig
    force: bool
    def __init__(self, gcs_source: _Optional[_Union[_import_config_pb2.GcsSource, _Mapping]] = ..., inline_source: _Optional[_Union[PurgeDocumentsRequest.InlineSource, _Mapping]] = ..., parent: _Optional[str] = ..., filter: _Optional[str] = ..., error_config: _Optional[_Union[PurgeErrorConfig, _Mapping]] = ..., force: bool = ...) -> None: ...

class PurgeDocumentsResponse(_message.Message):
    __slots__ = ("purge_count", "purge_sample")
    PURGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PURGE_SAMPLE_FIELD_NUMBER: _ClassVar[int]
    purge_count: int
    purge_sample: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, purge_count: _Optional[int] = ..., purge_sample: _Optional[_Iterable[str]] = ...) -> None: ...

class PurgeDocumentsMetadata(_message.Message):
    __slots__ = ("create_time", "update_time", "success_count", "failure_count", "ignored_count")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    IGNORED_COUNT_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    success_count: int
    failure_count: int
    ignored_count: int
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., success_count: _Optional[int] = ..., failure_count: _Optional[int] = ..., ignored_count: _Optional[int] = ...) -> None: ...

class PurgeSuggestionDenyListEntriesRequest(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...

class PurgeSuggestionDenyListEntriesResponse(_message.Message):
    __slots__ = ("purge_count", "error_samples")
    PURGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    purge_count: int
    error_samples: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    def __init__(self, purge_count: _Optional[int] = ..., error_samples: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ...) -> None: ...

class PurgeSuggestionDenyListEntriesMetadata(_message.Message):
    __slots__ = ("create_time", "update_time")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PurgeCompletionSuggestionsRequest(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...

class PurgeCompletionSuggestionsResponse(_message.Message):
    __slots__ = ("purge_succeeded", "error_samples")
    PURGE_SUCCEEDED_FIELD_NUMBER: _ClassVar[int]
    ERROR_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    purge_succeeded: bool
    error_samples: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    def __init__(self, purge_succeeded: bool = ..., error_samples: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ...) -> None: ...

class PurgeCompletionSuggestionsMetadata(_message.Message):
    __slots__ = ("create_time", "update_time")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
