from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OutputConfig(_message.Message):
    __slots__ = ('gcs_destination', 'bigquery_destination')

    class GcsDestination(_message.Message):
        __slots__ = ('output_uri_prefix',)
        OUTPUT_URI_PREFIX_FIELD_NUMBER: _ClassVar[int]
        output_uri_prefix: str

        def __init__(self, output_uri_prefix: _Optional[str]=...) -> None:
            ...

    class BigQueryDestination(_message.Message):
        __slots__ = ('dataset_id', 'table_id_prefix', 'table_type')
        DATASET_ID_FIELD_NUMBER: _ClassVar[int]
        TABLE_ID_PREFIX_FIELD_NUMBER: _ClassVar[int]
        TABLE_TYPE_FIELD_NUMBER: _ClassVar[int]
        dataset_id: str
        table_id_prefix: str
        table_type: str

        def __init__(self, dataset_id: _Optional[str]=..., table_id_prefix: _Optional[str]=..., table_type: _Optional[str]=...) -> None:
            ...
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: OutputConfig.GcsDestination
    bigquery_destination: OutputConfig.BigQueryDestination

    def __init__(self, gcs_destination: _Optional[_Union[OutputConfig.GcsDestination, _Mapping]]=..., bigquery_destination: _Optional[_Union[OutputConfig.BigQueryDestination, _Mapping]]=...) -> None:
        ...

class ExportErrorsConfig(_message.Message):
    __slots__ = ('gcs_prefix',)
    GCS_PREFIX_FIELD_NUMBER: _ClassVar[int]
    gcs_prefix: str

    def __init__(self, gcs_prefix: _Optional[str]=...) -> None:
        ...

class ExportAnalyticsMetricsRequest(_message.Message):
    __slots__ = ('catalog', 'output_config', 'filter')
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    catalog: str
    output_config: OutputConfig
    filter: str

    def __init__(self, catalog: _Optional[str]=..., output_config: _Optional[_Union[OutputConfig, _Mapping]]=..., filter: _Optional[str]=...) -> None:
        ...

class ExportMetadata(_message.Message):
    __slots__ = ('create_time', 'update_time')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ExportAnalyticsMetricsResponse(_message.Message):
    __slots__ = ('error_samples', 'errors_config', 'output_result')
    ERROR_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    ERRORS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_RESULT_FIELD_NUMBER: _ClassVar[int]
    error_samples: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    errors_config: ExportErrorsConfig
    output_result: OutputResult

    def __init__(self, error_samples: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=..., errors_config: _Optional[_Union[ExportErrorsConfig, _Mapping]]=..., output_result: _Optional[_Union[OutputResult, _Mapping]]=...) -> None:
        ...

class OutputResult(_message.Message):
    __slots__ = ('bigquery_result', 'gcs_result')
    BIGQUERY_RESULT_FIELD_NUMBER: _ClassVar[int]
    GCS_RESULT_FIELD_NUMBER: _ClassVar[int]
    bigquery_result: _containers.RepeatedCompositeFieldContainer[BigQueryOutputResult]
    gcs_result: _containers.RepeatedCompositeFieldContainer[GcsOutputResult]

    def __init__(self, bigquery_result: _Optional[_Iterable[_Union[BigQueryOutputResult, _Mapping]]]=..., gcs_result: _Optional[_Iterable[_Union[GcsOutputResult, _Mapping]]]=...) -> None:
        ...

class BigQueryOutputResult(_message.Message):
    __slots__ = ('dataset_id', 'table_id')
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    table_id: str

    def __init__(self, dataset_id: _Optional[str]=..., table_id: _Optional[str]=...) -> None:
        ...

class GcsOutputResult(_message.Message):
    __slots__ = ('output_uri',)
    OUTPUT_URI_FIELD_NUMBER: _ClassVar[int]
    output_uri: str

    def __init__(self, output_uri: _Optional[str]=...) -> None:
        ...