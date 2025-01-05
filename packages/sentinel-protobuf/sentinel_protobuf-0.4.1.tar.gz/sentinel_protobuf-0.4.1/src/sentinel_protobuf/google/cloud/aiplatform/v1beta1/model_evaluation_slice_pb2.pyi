from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import explanation_pb2 as _explanation_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModelEvaluationSlice(_message.Message):
    __slots__ = ("name", "slice", "metrics_schema_uri", "metrics", "create_time", "model_explanation")
    class Slice(_message.Message):
        __slots__ = ("dimension", "value", "slice_spec")
        class SliceSpec(_message.Message):
            __slots__ = ("configs",)
            class SliceConfig(_message.Message):
                __slots__ = ("value", "range", "all_values")
                VALUE_FIELD_NUMBER: _ClassVar[int]
                RANGE_FIELD_NUMBER: _ClassVar[int]
                ALL_VALUES_FIELD_NUMBER: _ClassVar[int]
                value: ModelEvaluationSlice.Slice.SliceSpec.Value
                range: ModelEvaluationSlice.Slice.SliceSpec.Range
                all_values: _wrappers_pb2.BoolValue
                def __init__(self, value: _Optional[_Union[ModelEvaluationSlice.Slice.SliceSpec.Value, _Mapping]] = ..., range: _Optional[_Union[ModelEvaluationSlice.Slice.SliceSpec.Range, _Mapping]] = ..., all_values: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
            class Range(_message.Message):
                __slots__ = ("low", "high")
                LOW_FIELD_NUMBER: _ClassVar[int]
                HIGH_FIELD_NUMBER: _ClassVar[int]
                low: float
                high: float
                def __init__(self, low: _Optional[float] = ..., high: _Optional[float] = ...) -> None: ...
            class Value(_message.Message):
                __slots__ = ("string_value", "float_value")
                STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
                FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
                string_value: str
                float_value: float
                def __init__(self, string_value: _Optional[str] = ..., float_value: _Optional[float] = ...) -> None: ...
            class ConfigsEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: ModelEvaluationSlice.Slice.SliceSpec.SliceConfig
                def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig, _Mapping]] = ...) -> None: ...
            CONFIGS_FIELD_NUMBER: _ClassVar[int]
            configs: _containers.MessageMap[str, ModelEvaluationSlice.Slice.SliceSpec.SliceConfig]
            def __init__(self, configs: _Optional[_Mapping[str, ModelEvaluationSlice.Slice.SliceSpec.SliceConfig]] = ...) -> None: ...
        DIMENSION_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        SLICE_SPEC_FIELD_NUMBER: _ClassVar[int]
        dimension: str
        value: str
        slice_spec: ModelEvaluationSlice.Slice.SliceSpec
        def __init__(self, dimension: _Optional[str] = ..., value: _Optional[str] = ..., slice_spec: _Optional[_Union[ModelEvaluationSlice.Slice.SliceSpec, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLICE_FIELD_NUMBER: _ClassVar[int]
    METRICS_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    MODEL_EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    slice: ModelEvaluationSlice.Slice
    metrics_schema_uri: str
    metrics: _struct_pb2.Value
    create_time: _timestamp_pb2.Timestamp
    model_explanation: _explanation_pb2.ModelExplanation
    def __init__(self, name: _Optional[str] = ..., slice: _Optional[_Union[ModelEvaluationSlice.Slice, _Mapping]] = ..., metrics_schema_uri: _Optional[str] = ..., metrics: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., model_explanation: _Optional[_Union[_explanation_pb2.ModelExplanation, _Mapping]] = ...) -> None: ...
