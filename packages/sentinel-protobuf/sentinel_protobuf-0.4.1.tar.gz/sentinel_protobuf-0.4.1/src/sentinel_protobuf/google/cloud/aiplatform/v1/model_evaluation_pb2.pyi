from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import explanation_pb2 as _explanation_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModelEvaluation(_message.Message):
    __slots__ = ("name", "display_name", "metrics_schema_uri", "metrics", "create_time", "slice_dimensions", "data_item_schema_uri", "annotation_schema_uri", "model_explanation", "explanation_specs", "metadata")
    class ModelEvaluationExplanationSpec(_message.Message):
        __slots__ = ("explanation_type", "explanation_spec")
        EXPLANATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        EXPLANATION_SPEC_FIELD_NUMBER: _ClassVar[int]
        explanation_type: str
        explanation_spec: _explanation_pb2.ExplanationSpec
        def __init__(self, explanation_type: _Optional[str] = ..., explanation_spec: _Optional[_Union[_explanation_pb2.ExplanationSpec, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    METRICS_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SLICE_DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    DATA_ITEM_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    MODEL_EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_SPECS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    metrics_schema_uri: str
    metrics: _struct_pb2.Value
    create_time: _timestamp_pb2.Timestamp
    slice_dimensions: _containers.RepeatedScalarFieldContainer[str]
    data_item_schema_uri: str
    annotation_schema_uri: str
    model_explanation: _explanation_pb2.ModelExplanation
    explanation_specs: _containers.RepeatedCompositeFieldContainer[ModelEvaluation.ModelEvaluationExplanationSpec]
    metadata: _struct_pb2.Value
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., metrics_schema_uri: _Optional[str] = ..., metrics: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., slice_dimensions: _Optional[_Iterable[str]] = ..., data_item_schema_uri: _Optional[str] = ..., annotation_schema_uri: _Optional[str] = ..., model_explanation: _Optional[_Union[_explanation_pb2.ModelExplanation, _Mapping]] = ..., explanation_specs: _Optional[_Iterable[_Union[ModelEvaluation.ModelEvaluationExplanationSpec, _Mapping]]] = ..., metadata: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
