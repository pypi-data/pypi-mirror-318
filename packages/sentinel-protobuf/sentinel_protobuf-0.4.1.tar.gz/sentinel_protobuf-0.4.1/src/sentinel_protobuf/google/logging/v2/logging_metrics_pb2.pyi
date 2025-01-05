from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import distribution_pb2 as _distribution_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import metric_pb2 as _metric_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LogMetric(_message.Message):
    __slots__ = ('name', 'description', 'filter', 'bucket_name', 'disabled', 'metric_descriptor', 'value_extractor', 'label_extractors', 'bucket_options', 'create_time', 'update_time', 'version')

    class ApiVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        V2: _ClassVar[LogMetric.ApiVersion]
        V1: _ClassVar[LogMetric.ApiVersion]
    V2: LogMetric.ApiVersion
    V1: LogMetric.ApiVersion

    class LabelExtractorsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    METRIC_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    VALUE_EXTRACTOR_FIELD_NUMBER: _ClassVar[int]
    LABEL_EXTRACTORS_FIELD_NUMBER: _ClassVar[int]
    BUCKET_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    filter: str
    bucket_name: str
    disabled: bool
    metric_descriptor: _metric_pb2.MetricDescriptor
    value_extractor: str
    label_extractors: _containers.ScalarMap[str, str]
    bucket_options: _distribution_pb2.Distribution.BucketOptions
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    version: LogMetric.ApiVersion

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., filter: _Optional[str]=..., bucket_name: _Optional[str]=..., disabled: bool=..., metric_descriptor: _Optional[_Union[_metric_pb2.MetricDescriptor, _Mapping]]=..., value_extractor: _Optional[str]=..., label_extractors: _Optional[_Mapping[str, str]]=..., bucket_options: _Optional[_Union[_distribution_pb2.Distribution.BucketOptions, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., version: _Optional[_Union[LogMetric.ApiVersion, str]]=...) -> None:
        ...

class ListLogMetricsRequest(_message.Message):
    __slots__ = ('parent', 'page_token', 'page_size')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int

    def __init__(self, parent: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class ListLogMetricsResponse(_message.Message):
    __slots__ = ('metrics', 'next_page_token')
    METRICS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    metrics: _containers.RepeatedCompositeFieldContainer[LogMetric]
    next_page_token: str

    def __init__(self, metrics: _Optional[_Iterable[_Union[LogMetric, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetLogMetricRequest(_message.Message):
    __slots__ = ('metric_name',)
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    metric_name: str

    def __init__(self, metric_name: _Optional[str]=...) -> None:
        ...

class CreateLogMetricRequest(_message.Message):
    __slots__ = ('parent', 'metric')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    parent: str
    metric: LogMetric

    def __init__(self, parent: _Optional[str]=..., metric: _Optional[_Union[LogMetric, _Mapping]]=...) -> None:
        ...

class UpdateLogMetricRequest(_message.Message):
    __slots__ = ('metric_name', 'metric')
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    metric_name: str
    metric: LogMetric

    def __init__(self, metric_name: _Optional[str]=..., metric: _Optional[_Union[LogMetric, _Mapping]]=...) -> None:
        ...

class DeleteLogMetricRequest(_message.Message):
    __slots__ = ('metric_name',)
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    metric_name: str

    def __init__(self, metric_name: _Optional[str]=...) -> None:
        ...