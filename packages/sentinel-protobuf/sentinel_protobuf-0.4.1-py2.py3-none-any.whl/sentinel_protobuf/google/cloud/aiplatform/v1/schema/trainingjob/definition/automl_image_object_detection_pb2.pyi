from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AutoMlImageObjectDetection(_message.Message):
    __slots__ = ('inputs', 'metadata')
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    inputs: AutoMlImageObjectDetectionInputs
    metadata: AutoMlImageObjectDetectionMetadata

    def __init__(self, inputs: _Optional[_Union[AutoMlImageObjectDetectionInputs, _Mapping]]=..., metadata: _Optional[_Union[AutoMlImageObjectDetectionMetadata, _Mapping]]=...) -> None:
        ...

class AutoMlImageObjectDetectionInputs(_message.Message):
    __slots__ = ('model_type', 'budget_milli_node_hours', 'disable_early_stopping')

    class ModelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODEL_TYPE_UNSPECIFIED: _ClassVar[AutoMlImageObjectDetectionInputs.ModelType]
        CLOUD_HIGH_ACCURACY_1: _ClassVar[AutoMlImageObjectDetectionInputs.ModelType]
        CLOUD_LOW_LATENCY_1: _ClassVar[AutoMlImageObjectDetectionInputs.ModelType]
        MOBILE_TF_LOW_LATENCY_1: _ClassVar[AutoMlImageObjectDetectionInputs.ModelType]
        MOBILE_TF_VERSATILE_1: _ClassVar[AutoMlImageObjectDetectionInputs.ModelType]
        MOBILE_TF_HIGH_ACCURACY_1: _ClassVar[AutoMlImageObjectDetectionInputs.ModelType]
    MODEL_TYPE_UNSPECIFIED: AutoMlImageObjectDetectionInputs.ModelType
    CLOUD_HIGH_ACCURACY_1: AutoMlImageObjectDetectionInputs.ModelType
    CLOUD_LOW_LATENCY_1: AutoMlImageObjectDetectionInputs.ModelType
    MOBILE_TF_LOW_LATENCY_1: AutoMlImageObjectDetectionInputs.ModelType
    MOBILE_TF_VERSATILE_1: AutoMlImageObjectDetectionInputs.ModelType
    MOBILE_TF_HIGH_ACCURACY_1: AutoMlImageObjectDetectionInputs.ModelType
    MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    BUDGET_MILLI_NODE_HOURS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_EARLY_STOPPING_FIELD_NUMBER: _ClassVar[int]
    model_type: AutoMlImageObjectDetectionInputs.ModelType
    budget_milli_node_hours: int
    disable_early_stopping: bool

    def __init__(self, model_type: _Optional[_Union[AutoMlImageObjectDetectionInputs.ModelType, str]]=..., budget_milli_node_hours: _Optional[int]=..., disable_early_stopping: bool=...) -> None:
        ...

class AutoMlImageObjectDetectionMetadata(_message.Message):
    __slots__ = ('cost_milli_node_hours', 'successful_stop_reason')

    class SuccessfulStopReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESSFUL_STOP_REASON_UNSPECIFIED: _ClassVar[AutoMlImageObjectDetectionMetadata.SuccessfulStopReason]
        BUDGET_REACHED: _ClassVar[AutoMlImageObjectDetectionMetadata.SuccessfulStopReason]
        MODEL_CONVERGED: _ClassVar[AutoMlImageObjectDetectionMetadata.SuccessfulStopReason]
    SUCCESSFUL_STOP_REASON_UNSPECIFIED: AutoMlImageObjectDetectionMetadata.SuccessfulStopReason
    BUDGET_REACHED: AutoMlImageObjectDetectionMetadata.SuccessfulStopReason
    MODEL_CONVERGED: AutoMlImageObjectDetectionMetadata.SuccessfulStopReason
    COST_MILLI_NODE_HOURS_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFUL_STOP_REASON_FIELD_NUMBER: _ClassVar[int]
    cost_milli_node_hours: int
    successful_stop_reason: AutoMlImageObjectDetectionMetadata.SuccessfulStopReason

    def __init__(self, cost_milli_node_hours: _Optional[int]=..., successful_stop_reason: _Optional[_Union[AutoMlImageObjectDetectionMetadata.SuccessfulStopReason, str]]=...) -> None:
        ...