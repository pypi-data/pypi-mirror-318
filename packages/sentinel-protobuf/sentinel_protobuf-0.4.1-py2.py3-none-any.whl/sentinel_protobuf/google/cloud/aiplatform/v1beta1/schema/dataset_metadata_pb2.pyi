from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ImageDatasetMetadata(_message.Message):
    __slots__ = ('data_item_schema_uri', 'gcs_bucket')
    DATA_ITEM_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    GCS_BUCKET_FIELD_NUMBER: _ClassVar[int]
    data_item_schema_uri: str
    gcs_bucket: str

    def __init__(self, data_item_schema_uri: _Optional[str]=..., gcs_bucket: _Optional[str]=...) -> None:
        ...

class TextDatasetMetadata(_message.Message):
    __slots__ = ('data_item_schema_uri', 'gcs_bucket')
    DATA_ITEM_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    GCS_BUCKET_FIELD_NUMBER: _ClassVar[int]
    data_item_schema_uri: str
    gcs_bucket: str

    def __init__(self, data_item_schema_uri: _Optional[str]=..., gcs_bucket: _Optional[str]=...) -> None:
        ...

class VideoDatasetMetadata(_message.Message):
    __slots__ = ('data_item_schema_uri', 'gcs_bucket')
    DATA_ITEM_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    GCS_BUCKET_FIELD_NUMBER: _ClassVar[int]
    data_item_schema_uri: str
    gcs_bucket: str

    def __init__(self, data_item_schema_uri: _Optional[str]=..., gcs_bucket: _Optional[str]=...) -> None:
        ...

class TablesDatasetMetadata(_message.Message):
    __slots__ = ('input_config',)

    class InputConfig(_message.Message):
        __slots__ = ('gcs_source', 'bigquery_source')
        GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
        BIGQUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
        gcs_source: TablesDatasetMetadata.GcsSource
        bigquery_source: TablesDatasetMetadata.BigQuerySource

        def __init__(self, gcs_source: _Optional[_Union[TablesDatasetMetadata.GcsSource, _Mapping]]=..., bigquery_source: _Optional[_Union[TablesDatasetMetadata.BigQuerySource, _Mapping]]=...) -> None:
            ...

    class GcsSource(_message.Message):
        __slots__ = ('uri',)
        URI_FIELD_NUMBER: _ClassVar[int]
        uri: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, uri: _Optional[_Iterable[str]]=...) -> None:
            ...

    class BigQuerySource(_message.Message):
        __slots__ = ('uri',)
        URI_FIELD_NUMBER: _ClassVar[int]
        uri: str

        def __init__(self, uri: _Optional[str]=...) -> None:
            ...
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    input_config: TablesDatasetMetadata.InputConfig

    def __init__(self, input_config: _Optional[_Union[TablesDatasetMetadata.InputConfig, _Mapping]]=...) -> None:
        ...

class TimeSeriesDatasetMetadata(_message.Message):
    __slots__ = ('input_config', 'time_series_identifier_column', 'time_column')

    class InputConfig(_message.Message):
        __slots__ = ('gcs_source', 'bigquery_source')
        GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
        BIGQUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
        gcs_source: TimeSeriesDatasetMetadata.GcsSource
        bigquery_source: TimeSeriesDatasetMetadata.BigQuerySource

        def __init__(self, gcs_source: _Optional[_Union[TimeSeriesDatasetMetadata.GcsSource, _Mapping]]=..., bigquery_source: _Optional[_Union[TimeSeriesDatasetMetadata.BigQuerySource, _Mapping]]=...) -> None:
            ...

    class GcsSource(_message.Message):
        __slots__ = ('uri',)
        URI_FIELD_NUMBER: _ClassVar[int]
        uri: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, uri: _Optional[_Iterable[str]]=...) -> None:
            ...

    class BigQuerySource(_message.Message):
        __slots__ = ('uri',)
        URI_FIELD_NUMBER: _ClassVar[int]
        uri: str

        def __init__(self, uri: _Optional[str]=...) -> None:
            ...
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TIME_SERIES_IDENTIFIER_COLUMN_FIELD_NUMBER: _ClassVar[int]
    TIME_COLUMN_FIELD_NUMBER: _ClassVar[int]
    input_config: TimeSeriesDatasetMetadata.InputConfig
    time_series_identifier_column: str
    time_column: str

    def __init__(self, input_config: _Optional[_Union[TimeSeriesDatasetMetadata.InputConfig, _Mapping]]=..., time_series_identifier_column: _Optional[str]=..., time_column: _Optional[str]=...) -> None:
        ...