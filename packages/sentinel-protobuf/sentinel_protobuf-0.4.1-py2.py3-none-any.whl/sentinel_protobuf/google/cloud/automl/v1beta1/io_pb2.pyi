from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class InputConfig(_message.Message):
    __slots__ = ('gcs_source', 'bigquery_source', 'params')

    class ParamsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    gcs_source: GcsSource
    bigquery_source: BigQuerySource
    params: _containers.ScalarMap[str, str]

    def __init__(self, gcs_source: _Optional[_Union[GcsSource, _Mapping]]=..., bigquery_source: _Optional[_Union[BigQuerySource, _Mapping]]=..., params: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class BatchPredictInputConfig(_message.Message):
    __slots__ = ('gcs_source', 'bigquery_source')
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    gcs_source: GcsSource
    bigquery_source: BigQuerySource

    def __init__(self, gcs_source: _Optional[_Union[GcsSource, _Mapping]]=..., bigquery_source: _Optional[_Union[BigQuerySource, _Mapping]]=...) -> None:
        ...

class DocumentInputConfig(_message.Message):
    __slots__ = ('gcs_source',)
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    gcs_source: GcsSource

    def __init__(self, gcs_source: _Optional[_Union[GcsSource, _Mapping]]=...) -> None:
        ...

class OutputConfig(_message.Message):
    __slots__ = ('gcs_destination', 'bigquery_destination')
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: GcsDestination
    bigquery_destination: BigQueryDestination

    def __init__(self, gcs_destination: _Optional[_Union[GcsDestination, _Mapping]]=..., bigquery_destination: _Optional[_Union[BigQueryDestination, _Mapping]]=...) -> None:
        ...

class BatchPredictOutputConfig(_message.Message):
    __slots__ = ('gcs_destination', 'bigquery_destination')
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: GcsDestination
    bigquery_destination: BigQueryDestination

    def __init__(self, gcs_destination: _Optional[_Union[GcsDestination, _Mapping]]=..., bigquery_destination: _Optional[_Union[BigQueryDestination, _Mapping]]=...) -> None:
        ...

class ModelExportOutputConfig(_message.Message):
    __slots__ = ('gcs_destination', 'gcr_destination', 'model_format', 'params')

    class ParamsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    GCR_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    MODEL_FORMAT_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: GcsDestination
    gcr_destination: GcrDestination
    model_format: str
    params: _containers.ScalarMap[str, str]

    def __init__(self, gcs_destination: _Optional[_Union[GcsDestination, _Mapping]]=..., gcr_destination: _Optional[_Union[GcrDestination, _Mapping]]=..., model_format: _Optional[str]=..., params: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ExportEvaluatedExamplesOutputConfig(_message.Message):
    __slots__ = ('bigquery_destination',)
    BIGQUERY_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    bigquery_destination: BigQueryDestination

    def __init__(self, bigquery_destination: _Optional[_Union[BigQueryDestination, _Mapping]]=...) -> None:
        ...

class GcsSource(_message.Message):
    __slots__ = ('input_uris',)
    INPUT_URIS_FIELD_NUMBER: _ClassVar[int]
    input_uris: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, input_uris: _Optional[_Iterable[str]]=...) -> None:
        ...

class BigQuerySource(_message.Message):
    __slots__ = ('input_uri',)
    INPUT_URI_FIELD_NUMBER: _ClassVar[int]
    input_uri: str

    def __init__(self, input_uri: _Optional[str]=...) -> None:
        ...

class GcsDestination(_message.Message):
    __slots__ = ('output_uri_prefix',)
    OUTPUT_URI_PREFIX_FIELD_NUMBER: _ClassVar[int]
    output_uri_prefix: str

    def __init__(self, output_uri_prefix: _Optional[str]=...) -> None:
        ...

class BigQueryDestination(_message.Message):
    __slots__ = ('output_uri',)
    OUTPUT_URI_FIELD_NUMBER: _ClassVar[int]
    output_uri: str

    def __init__(self, output_uri: _Optional[str]=...) -> None:
        ...

class GcrDestination(_message.Message):
    __slots__ = ('output_uri',)
    OUTPUT_URI_FIELD_NUMBER: _ClassVar[int]
    output_uri: str

    def __init__(self, output_uri: _Optional[str]=...) -> None:
        ...