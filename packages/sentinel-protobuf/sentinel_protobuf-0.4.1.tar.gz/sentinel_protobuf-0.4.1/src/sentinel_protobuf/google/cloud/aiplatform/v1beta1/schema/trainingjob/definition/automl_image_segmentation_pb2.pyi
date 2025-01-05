from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AutoMlImageSegmentation(_message.Message):
    __slots__ = ('inputs', 'metadata')
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    inputs: AutoMlImageSegmentationInputs
    metadata: AutoMlImageSegmentationMetadata

    def __init__(self, inputs: _Optional[_Union[AutoMlImageSegmentationInputs, _Mapping]]=..., metadata: _Optional[_Union[AutoMlImageSegmentationMetadata, _Mapping]]=...) -> None:
        ...

class AutoMlImageSegmentationInputs(_message.Message):
    __slots__ = ('model_type', 'budget_milli_node_hours', 'base_model_id')

    class ModelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODEL_TYPE_UNSPECIFIED: _ClassVar[AutoMlImageSegmentationInputs.ModelType]
        CLOUD_HIGH_ACCURACY_1: _ClassVar[AutoMlImageSegmentationInputs.ModelType]
        CLOUD_LOW_ACCURACY_1: _ClassVar[AutoMlImageSegmentationInputs.ModelType]
        MOBILE_TF_LOW_LATENCY_1: _ClassVar[AutoMlImageSegmentationInputs.ModelType]
    MODEL_TYPE_UNSPECIFIED: AutoMlImageSegmentationInputs.ModelType
    CLOUD_HIGH_ACCURACY_1: AutoMlImageSegmentationInputs.ModelType
    CLOUD_LOW_ACCURACY_1: AutoMlImageSegmentationInputs.ModelType
    MOBILE_TF_LOW_LATENCY_1: AutoMlImageSegmentationInputs.ModelType
    MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    BUDGET_MILLI_NODE_HOURS_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    model_type: AutoMlImageSegmentationInputs.ModelType
    budget_milli_node_hours: int
    base_model_id: str

    def __init__(self, model_type: _Optional[_Union[AutoMlImageSegmentationInputs.ModelType, str]]=..., budget_milli_node_hours: _Optional[int]=..., base_model_id: _Optional[str]=...) -> None:
        ...

class AutoMlImageSegmentationMetadata(_message.Message):
    __slots__ = ('cost_milli_node_hours', 'successful_stop_reason')

    class SuccessfulStopReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESSFUL_STOP_REASON_UNSPECIFIED: _ClassVar[AutoMlImageSegmentationMetadata.SuccessfulStopReason]
        BUDGET_REACHED: _ClassVar[AutoMlImageSegmentationMetadata.SuccessfulStopReason]
        MODEL_CONVERGED: _ClassVar[AutoMlImageSegmentationMetadata.SuccessfulStopReason]
    SUCCESSFUL_STOP_REASON_UNSPECIFIED: AutoMlImageSegmentationMetadata.SuccessfulStopReason
    BUDGET_REACHED: AutoMlImageSegmentationMetadata.SuccessfulStopReason
    MODEL_CONVERGED: AutoMlImageSegmentationMetadata.SuccessfulStopReason
    COST_MILLI_NODE_HOURS_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFUL_STOP_REASON_FIELD_NUMBER: _ClassVar[int]
    cost_milli_node_hours: int
    successful_stop_reason: AutoMlImageSegmentationMetadata.SuccessfulStopReason

    def __init__(self, cost_milli_node_hours: _Optional[int]=..., successful_stop_reason: _Optional[_Union[AutoMlImageSegmentationMetadata.SuccessfulStopReason, str]]=...) -> None:
        ...