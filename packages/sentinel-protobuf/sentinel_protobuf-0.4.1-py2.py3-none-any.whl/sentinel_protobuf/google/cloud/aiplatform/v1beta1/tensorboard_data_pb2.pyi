from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.aiplatform.v1beta1 import tensorboard_time_series_pb2 as _tensorboard_time_series_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TimeSeriesData(_message.Message):
    __slots__ = ('tensorboard_time_series_id', 'value_type', 'values')
    TENSORBOARD_TIME_SERIES_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    tensorboard_time_series_id: str
    value_type: _tensorboard_time_series_pb2.TensorboardTimeSeries.ValueType
    values: _containers.RepeatedCompositeFieldContainer[TimeSeriesDataPoint]

    def __init__(self, tensorboard_time_series_id: _Optional[str]=..., value_type: _Optional[_Union[_tensorboard_time_series_pb2.TensorboardTimeSeries.ValueType, str]]=..., values: _Optional[_Iterable[_Union[TimeSeriesDataPoint, _Mapping]]]=...) -> None:
        ...

class TimeSeriesDataPoint(_message.Message):
    __slots__ = ('scalar', 'tensor', 'blobs', 'wall_time', 'step')
    SCALAR_FIELD_NUMBER: _ClassVar[int]
    TENSOR_FIELD_NUMBER: _ClassVar[int]
    BLOBS_FIELD_NUMBER: _ClassVar[int]
    WALL_TIME_FIELD_NUMBER: _ClassVar[int]
    STEP_FIELD_NUMBER: _ClassVar[int]
    scalar: Scalar
    tensor: TensorboardTensor
    blobs: TensorboardBlobSequence
    wall_time: _timestamp_pb2.Timestamp
    step: int

    def __init__(self, scalar: _Optional[_Union[Scalar, _Mapping]]=..., tensor: _Optional[_Union[TensorboardTensor, _Mapping]]=..., blobs: _Optional[_Union[TensorboardBlobSequence, _Mapping]]=..., wall_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., step: _Optional[int]=...) -> None:
        ...

class Scalar(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float

    def __init__(self, value: _Optional[float]=...) -> None:
        ...

class TensorboardTensor(_message.Message):
    __slots__ = ('value', 'version_number')
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    value: bytes
    version_number: int

    def __init__(self, value: _Optional[bytes]=..., version_number: _Optional[int]=...) -> None:
        ...

class TensorboardBlobSequence(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[TensorboardBlob]

    def __init__(self, values: _Optional[_Iterable[_Union[TensorboardBlob, _Mapping]]]=...) -> None:
        ...

class TensorboardBlob(_message.Message):
    __slots__ = ('id', 'data')
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    data: bytes

    def __init__(self, id: _Optional[str]=..., data: _Optional[bytes]=...) -> None:
        ...