from google.cloud.automl.v1beta1 import annotation_spec_pb2 as _annotation_spec_pb2
from google.cloud.automl.v1beta1 import classification_pb2 as _classification_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ImageClassificationDatasetMetadata(_message.Message):
    __slots__ = ('classification_type',)
    CLASSIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    classification_type: _classification_pb2.ClassificationType

    def __init__(self, classification_type: _Optional[_Union[_classification_pb2.ClassificationType, str]]=...) -> None:
        ...

class ImageObjectDetectionDatasetMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ImageClassificationModelMetadata(_message.Message):
    __slots__ = ('base_model_id', 'train_budget', 'train_cost', 'stop_reason', 'model_type', 'node_qps', 'node_count')
    BASE_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    TRAIN_BUDGET_FIELD_NUMBER: _ClassVar[int]
    TRAIN_COST_FIELD_NUMBER: _ClassVar[int]
    STOP_REASON_FIELD_NUMBER: _ClassVar[int]
    MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    NODE_QPS_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    base_model_id: str
    train_budget: int
    train_cost: int
    stop_reason: str
    model_type: str
    node_qps: float
    node_count: int

    def __init__(self, base_model_id: _Optional[str]=..., train_budget: _Optional[int]=..., train_cost: _Optional[int]=..., stop_reason: _Optional[str]=..., model_type: _Optional[str]=..., node_qps: _Optional[float]=..., node_count: _Optional[int]=...) -> None:
        ...

class ImageObjectDetectionModelMetadata(_message.Message):
    __slots__ = ('model_type', 'node_count', 'node_qps', 'stop_reason', 'train_budget_milli_node_hours', 'train_cost_milli_node_hours')
    MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    NODE_QPS_FIELD_NUMBER: _ClassVar[int]
    STOP_REASON_FIELD_NUMBER: _ClassVar[int]
    TRAIN_BUDGET_MILLI_NODE_HOURS_FIELD_NUMBER: _ClassVar[int]
    TRAIN_COST_MILLI_NODE_HOURS_FIELD_NUMBER: _ClassVar[int]
    model_type: str
    node_count: int
    node_qps: float
    stop_reason: str
    train_budget_milli_node_hours: int
    train_cost_milli_node_hours: int

    def __init__(self, model_type: _Optional[str]=..., node_count: _Optional[int]=..., node_qps: _Optional[float]=..., stop_reason: _Optional[str]=..., train_budget_milli_node_hours: _Optional[int]=..., train_cost_milli_node_hours: _Optional[int]=...) -> None:
        ...

class ImageClassificationModelDeploymentMetadata(_message.Message):
    __slots__ = ('node_count',)
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    node_count: int

    def __init__(self, node_count: _Optional[int]=...) -> None:
        ...

class ImageObjectDetectionModelDeploymentMetadata(_message.Message):
    __slots__ = ('node_count',)
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    node_count: int

    def __init__(self, node_count: _Optional[int]=...) -> None:
        ...