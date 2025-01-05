from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import operation_pb2 as _operation_pb2
from google.cloud.aiplatform.v1beta1 import tensorboard_pb2 as _tensorboard_pb2
from google.cloud.aiplatform.v1beta1 import tensorboard_data_pb2 as _tensorboard_data_pb2
from google.cloud.aiplatform.v1beta1 import tensorboard_experiment_pb2 as _tensorboard_experiment_pb2
from google.cloud.aiplatform.v1beta1 import tensorboard_run_pb2 as _tensorboard_run_pb2
from google.cloud.aiplatform.v1beta1 import tensorboard_time_series_pb2 as _tensorboard_time_series_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateTensorboardRequest(_message.Message):
    __slots__ = ('parent', 'tensorboard')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TENSORBOARD_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tensorboard: _tensorboard_pb2.Tensorboard

    def __init__(self, parent: _Optional[str]=..., tensorboard: _Optional[_Union[_tensorboard_pb2.Tensorboard, _Mapping]]=...) -> None:
        ...

class GetTensorboardRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListTensorboardsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'order_by', 'read_mask')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    order_by: str
    read_mask: _field_mask_pb2.FieldMask

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListTensorboardsResponse(_message.Message):
    __slots__ = ('tensorboards', 'next_page_token')
    TENSORBOARDS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tensorboards: _containers.RepeatedCompositeFieldContainer[_tensorboard_pb2.Tensorboard]
    next_page_token: str

    def __init__(self, tensorboards: _Optional[_Iterable[_Union[_tensorboard_pb2.Tensorboard, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateTensorboardRequest(_message.Message):
    __slots__ = ('update_mask', 'tensorboard')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    TENSORBOARD_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    tensorboard: _tensorboard_pb2.Tensorboard

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., tensorboard: _Optional[_Union[_tensorboard_pb2.Tensorboard, _Mapping]]=...) -> None:
        ...

class DeleteTensorboardRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ReadTensorboardUsageRequest(_message.Message):
    __slots__ = ('tensorboard',)
    TENSORBOARD_FIELD_NUMBER: _ClassVar[int]
    tensorboard: str

    def __init__(self, tensorboard: _Optional[str]=...) -> None:
        ...

class ReadTensorboardUsageResponse(_message.Message):
    __slots__ = ('monthly_usage_data',)

    class PerUserUsageData(_message.Message):
        __slots__ = ('username', 'view_count')
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        VIEW_COUNT_FIELD_NUMBER: _ClassVar[int]
        username: str
        view_count: int

        def __init__(self, username: _Optional[str]=..., view_count: _Optional[int]=...) -> None:
            ...

    class PerMonthUsageData(_message.Message):
        __slots__ = ('user_usage_data',)
        USER_USAGE_DATA_FIELD_NUMBER: _ClassVar[int]
        user_usage_data: _containers.RepeatedCompositeFieldContainer[ReadTensorboardUsageResponse.PerUserUsageData]

        def __init__(self, user_usage_data: _Optional[_Iterable[_Union[ReadTensorboardUsageResponse.PerUserUsageData, _Mapping]]]=...) -> None:
            ...

    class MonthlyUsageDataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ReadTensorboardUsageResponse.PerMonthUsageData

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ReadTensorboardUsageResponse.PerMonthUsageData, _Mapping]]=...) -> None:
            ...
    MONTHLY_USAGE_DATA_FIELD_NUMBER: _ClassVar[int]
    monthly_usage_data: _containers.MessageMap[str, ReadTensorboardUsageResponse.PerMonthUsageData]

    def __init__(self, monthly_usage_data: _Optional[_Mapping[str, ReadTensorboardUsageResponse.PerMonthUsageData]]=...) -> None:
        ...

class ReadTensorboardSizeRequest(_message.Message):
    __slots__ = ('tensorboard',)
    TENSORBOARD_FIELD_NUMBER: _ClassVar[int]
    tensorboard: str

    def __init__(self, tensorboard: _Optional[str]=...) -> None:
        ...

class ReadTensorboardSizeResponse(_message.Message):
    __slots__ = ('storage_size_byte',)
    STORAGE_SIZE_BYTE_FIELD_NUMBER: _ClassVar[int]
    storage_size_byte: int

    def __init__(self, storage_size_byte: _Optional[int]=...) -> None:
        ...

class CreateTensorboardExperimentRequest(_message.Message):
    __slots__ = ('parent', 'tensorboard_experiment', 'tensorboard_experiment_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TENSORBOARD_EXPERIMENT_FIELD_NUMBER: _ClassVar[int]
    TENSORBOARD_EXPERIMENT_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tensorboard_experiment: _tensorboard_experiment_pb2.TensorboardExperiment
    tensorboard_experiment_id: str

    def __init__(self, parent: _Optional[str]=..., tensorboard_experiment: _Optional[_Union[_tensorboard_experiment_pb2.TensorboardExperiment, _Mapping]]=..., tensorboard_experiment_id: _Optional[str]=...) -> None:
        ...

class GetTensorboardExperimentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListTensorboardExperimentsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'order_by', 'read_mask')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    order_by: str
    read_mask: _field_mask_pb2.FieldMask

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListTensorboardExperimentsResponse(_message.Message):
    __slots__ = ('tensorboard_experiments', 'next_page_token')
    TENSORBOARD_EXPERIMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tensorboard_experiments: _containers.RepeatedCompositeFieldContainer[_tensorboard_experiment_pb2.TensorboardExperiment]
    next_page_token: str

    def __init__(self, tensorboard_experiments: _Optional[_Iterable[_Union[_tensorboard_experiment_pb2.TensorboardExperiment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateTensorboardExperimentRequest(_message.Message):
    __slots__ = ('update_mask', 'tensorboard_experiment')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    TENSORBOARD_EXPERIMENT_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    tensorboard_experiment: _tensorboard_experiment_pb2.TensorboardExperiment

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., tensorboard_experiment: _Optional[_Union[_tensorboard_experiment_pb2.TensorboardExperiment, _Mapping]]=...) -> None:
        ...

class DeleteTensorboardExperimentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class BatchCreateTensorboardRunsRequest(_message.Message):
    __slots__ = ('parent', 'requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[CreateTensorboardRunRequest]

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[CreateTensorboardRunRequest, _Mapping]]]=...) -> None:
        ...

class BatchCreateTensorboardRunsResponse(_message.Message):
    __slots__ = ('tensorboard_runs',)
    TENSORBOARD_RUNS_FIELD_NUMBER: _ClassVar[int]
    tensorboard_runs: _containers.RepeatedCompositeFieldContainer[_tensorboard_run_pb2.TensorboardRun]

    def __init__(self, tensorboard_runs: _Optional[_Iterable[_Union[_tensorboard_run_pb2.TensorboardRun, _Mapping]]]=...) -> None:
        ...

class CreateTensorboardRunRequest(_message.Message):
    __slots__ = ('parent', 'tensorboard_run', 'tensorboard_run_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TENSORBOARD_RUN_FIELD_NUMBER: _ClassVar[int]
    TENSORBOARD_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tensorboard_run: _tensorboard_run_pb2.TensorboardRun
    tensorboard_run_id: str

    def __init__(self, parent: _Optional[str]=..., tensorboard_run: _Optional[_Union[_tensorboard_run_pb2.TensorboardRun, _Mapping]]=..., tensorboard_run_id: _Optional[str]=...) -> None:
        ...

class GetTensorboardRunRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ReadTensorboardBlobDataRequest(_message.Message):
    __slots__ = ('time_series', 'blob_ids')
    TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    BLOB_IDS_FIELD_NUMBER: _ClassVar[int]
    time_series: str
    blob_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, time_series: _Optional[str]=..., blob_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class ReadTensorboardBlobDataResponse(_message.Message):
    __slots__ = ('blobs',)
    BLOBS_FIELD_NUMBER: _ClassVar[int]
    blobs: _containers.RepeatedCompositeFieldContainer[_tensorboard_data_pb2.TensorboardBlob]

    def __init__(self, blobs: _Optional[_Iterable[_Union[_tensorboard_data_pb2.TensorboardBlob, _Mapping]]]=...) -> None:
        ...

class ListTensorboardRunsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'order_by', 'read_mask')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    order_by: str
    read_mask: _field_mask_pb2.FieldMask

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListTensorboardRunsResponse(_message.Message):
    __slots__ = ('tensorboard_runs', 'next_page_token')
    TENSORBOARD_RUNS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tensorboard_runs: _containers.RepeatedCompositeFieldContainer[_tensorboard_run_pb2.TensorboardRun]
    next_page_token: str

    def __init__(self, tensorboard_runs: _Optional[_Iterable[_Union[_tensorboard_run_pb2.TensorboardRun, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateTensorboardRunRequest(_message.Message):
    __slots__ = ('update_mask', 'tensorboard_run')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    TENSORBOARD_RUN_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    tensorboard_run: _tensorboard_run_pb2.TensorboardRun

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., tensorboard_run: _Optional[_Union[_tensorboard_run_pb2.TensorboardRun, _Mapping]]=...) -> None:
        ...

class DeleteTensorboardRunRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class BatchCreateTensorboardTimeSeriesRequest(_message.Message):
    __slots__ = ('parent', 'requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[CreateTensorboardTimeSeriesRequest]

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[CreateTensorboardTimeSeriesRequest, _Mapping]]]=...) -> None:
        ...

class BatchCreateTensorboardTimeSeriesResponse(_message.Message):
    __slots__ = ('tensorboard_time_series',)
    TENSORBOARD_TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    tensorboard_time_series: _containers.RepeatedCompositeFieldContainer[_tensorboard_time_series_pb2.TensorboardTimeSeries]

    def __init__(self, tensorboard_time_series: _Optional[_Iterable[_Union[_tensorboard_time_series_pb2.TensorboardTimeSeries, _Mapping]]]=...) -> None:
        ...

class CreateTensorboardTimeSeriesRequest(_message.Message):
    __slots__ = ('parent', 'tensorboard_time_series_id', 'tensorboard_time_series')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TENSORBOARD_TIME_SERIES_ID_FIELD_NUMBER: _ClassVar[int]
    TENSORBOARD_TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tensorboard_time_series_id: str
    tensorboard_time_series: _tensorboard_time_series_pb2.TensorboardTimeSeries

    def __init__(self, parent: _Optional[str]=..., tensorboard_time_series_id: _Optional[str]=..., tensorboard_time_series: _Optional[_Union[_tensorboard_time_series_pb2.TensorboardTimeSeries, _Mapping]]=...) -> None:
        ...

class GetTensorboardTimeSeriesRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListTensorboardTimeSeriesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'order_by', 'read_mask')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    order_by: str
    read_mask: _field_mask_pb2.FieldMask

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListTensorboardTimeSeriesResponse(_message.Message):
    __slots__ = ('tensorboard_time_series', 'next_page_token')
    TENSORBOARD_TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tensorboard_time_series: _containers.RepeatedCompositeFieldContainer[_tensorboard_time_series_pb2.TensorboardTimeSeries]
    next_page_token: str

    def __init__(self, tensorboard_time_series: _Optional[_Iterable[_Union[_tensorboard_time_series_pb2.TensorboardTimeSeries, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateTensorboardTimeSeriesRequest(_message.Message):
    __slots__ = ('update_mask', 'tensorboard_time_series')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    TENSORBOARD_TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    tensorboard_time_series: _tensorboard_time_series_pb2.TensorboardTimeSeries

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., tensorboard_time_series: _Optional[_Union[_tensorboard_time_series_pb2.TensorboardTimeSeries, _Mapping]]=...) -> None:
        ...

class DeleteTensorboardTimeSeriesRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class BatchReadTensorboardTimeSeriesDataRequest(_message.Message):
    __slots__ = ('tensorboard', 'time_series')
    TENSORBOARD_FIELD_NUMBER: _ClassVar[int]
    TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    tensorboard: str
    time_series: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, tensorboard: _Optional[str]=..., time_series: _Optional[_Iterable[str]]=...) -> None:
        ...

class BatchReadTensorboardTimeSeriesDataResponse(_message.Message):
    __slots__ = ('time_series_data',)
    TIME_SERIES_DATA_FIELD_NUMBER: _ClassVar[int]
    time_series_data: _containers.RepeatedCompositeFieldContainer[_tensorboard_data_pb2.TimeSeriesData]

    def __init__(self, time_series_data: _Optional[_Iterable[_Union[_tensorboard_data_pb2.TimeSeriesData, _Mapping]]]=...) -> None:
        ...

class ReadTensorboardTimeSeriesDataRequest(_message.Message):
    __slots__ = ('tensorboard_time_series', 'max_data_points', 'filter')
    TENSORBOARD_TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    MAX_DATA_POINTS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    tensorboard_time_series: str
    max_data_points: int
    filter: str

    def __init__(self, tensorboard_time_series: _Optional[str]=..., max_data_points: _Optional[int]=..., filter: _Optional[str]=...) -> None:
        ...

class ReadTensorboardTimeSeriesDataResponse(_message.Message):
    __slots__ = ('time_series_data',)
    TIME_SERIES_DATA_FIELD_NUMBER: _ClassVar[int]
    time_series_data: _tensorboard_data_pb2.TimeSeriesData

    def __init__(self, time_series_data: _Optional[_Union[_tensorboard_data_pb2.TimeSeriesData, _Mapping]]=...) -> None:
        ...

class WriteTensorboardExperimentDataRequest(_message.Message):
    __slots__ = ('tensorboard_experiment', 'write_run_data_requests')
    TENSORBOARD_EXPERIMENT_FIELD_NUMBER: _ClassVar[int]
    WRITE_RUN_DATA_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    tensorboard_experiment: str
    write_run_data_requests: _containers.RepeatedCompositeFieldContainer[WriteTensorboardRunDataRequest]

    def __init__(self, tensorboard_experiment: _Optional[str]=..., write_run_data_requests: _Optional[_Iterable[_Union[WriteTensorboardRunDataRequest, _Mapping]]]=...) -> None:
        ...

class WriteTensorboardExperimentDataResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WriteTensorboardRunDataRequest(_message.Message):
    __slots__ = ('tensorboard_run', 'time_series_data')
    TENSORBOARD_RUN_FIELD_NUMBER: _ClassVar[int]
    TIME_SERIES_DATA_FIELD_NUMBER: _ClassVar[int]
    tensorboard_run: str
    time_series_data: _containers.RepeatedCompositeFieldContainer[_tensorboard_data_pb2.TimeSeriesData]

    def __init__(self, tensorboard_run: _Optional[str]=..., time_series_data: _Optional[_Iterable[_Union[_tensorboard_data_pb2.TimeSeriesData, _Mapping]]]=...) -> None:
        ...

class WriteTensorboardRunDataResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ExportTensorboardTimeSeriesDataRequest(_message.Message):
    __slots__ = ('tensorboard_time_series', 'filter', 'page_size', 'page_token', 'order_by')
    TENSORBOARD_TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    tensorboard_time_series: str
    filter: str
    page_size: int
    page_token: str
    order_by: str

    def __init__(self, tensorboard_time_series: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ExportTensorboardTimeSeriesDataResponse(_message.Message):
    __slots__ = ('time_series_data_points', 'next_page_token')
    TIME_SERIES_DATA_POINTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    time_series_data_points: _containers.RepeatedCompositeFieldContainer[_tensorboard_data_pb2.TimeSeriesDataPoint]
    next_page_token: str

    def __init__(self, time_series_data_points: _Optional[_Iterable[_Union[_tensorboard_data_pb2.TimeSeriesDataPoint, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateTensorboardOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class UpdateTensorboardOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...