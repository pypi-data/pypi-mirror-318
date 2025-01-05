from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1alpha import import_config_pb2 as _import_config_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EstimateDataSizeRequest(_message.Message):
    __slots__ = ("website_data_source", "file_data_source", "location")
    class WebsiteDataSource(_message.Message):
        __slots__ = ("estimator_uri_patterns",)
        class EstimatorUriPattern(_message.Message):
            __slots__ = ("provided_uri_pattern", "exact_match", "exclusive")
            PROVIDED_URI_PATTERN_FIELD_NUMBER: _ClassVar[int]
            EXACT_MATCH_FIELD_NUMBER: _ClassVar[int]
            EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
            provided_uri_pattern: str
            exact_match: bool
            exclusive: bool
            def __init__(self, provided_uri_pattern: _Optional[str] = ..., exact_match: bool = ..., exclusive: bool = ...) -> None: ...
        ESTIMATOR_URI_PATTERNS_FIELD_NUMBER: _ClassVar[int]
        estimator_uri_patterns: _containers.RepeatedCompositeFieldContainer[EstimateDataSizeRequest.WebsiteDataSource.EstimatorUriPattern]
        def __init__(self, estimator_uri_patterns: _Optional[_Iterable[_Union[EstimateDataSizeRequest.WebsiteDataSource.EstimatorUriPattern, _Mapping]]] = ...) -> None: ...
    class FileDataSource(_message.Message):
        __slots__ = ("gcs_source", "bigquery_source")
        GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
        BIGQUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
        gcs_source: _import_config_pb2.GcsSource
        bigquery_source: _import_config_pb2.BigQuerySource
        def __init__(self, gcs_source: _Optional[_Union[_import_config_pb2.GcsSource, _Mapping]] = ..., bigquery_source: _Optional[_Union[_import_config_pb2.BigQuerySource, _Mapping]] = ...) -> None: ...
    WEBSITE_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    FILE_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    website_data_source: EstimateDataSizeRequest.WebsiteDataSource
    file_data_source: EstimateDataSizeRequest.FileDataSource
    location: str
    def __init__(self, website_data_source: _Optional[_Union[EstimateDataSizeRequest.WebsiteDataSource, _Mapping]] = ..., file_data_source: _Optional[_Union[EstimateDataSizeRequest.FileDataSource, _Mapping]] = ..., location: _Optional[str] = ...) -> None: ...

class EstimateDataSizeResponse(_message.Message):
    __slots__ = ("data_size_bytes", "document_count")
    DATA_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    data_size_bytes: int
    document_count: int
    def __init__(self, data_size_bytes: _Optional[int] = ..., document_count: _Optional[int] = ...) -> None: ...

class EstimateDataSizeMetadata(_message.Message):
    __slots__ = ("create_time",)
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
