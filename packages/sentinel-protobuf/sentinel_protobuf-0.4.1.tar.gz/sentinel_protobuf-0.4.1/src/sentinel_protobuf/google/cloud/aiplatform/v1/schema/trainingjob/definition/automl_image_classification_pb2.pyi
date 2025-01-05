from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AutoMlImageClassification(_message.Message):
    __slots__ = ('inputs', 'metadata')
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    inputs: AutoMlImageClassificationInputs
    metadata: AutoMlImageClassificationMetadata

    def __init__(self, inputs: _Optional[_Union[AutoMlImageClassificationInputs, _Mapping]]=..., metadata: _Optional[_Union[AutoMlImageClassificationMetadata, _Mapping]]=...) -> None:
        ...

class AutoMlImageClassificationInputs(_message.Message):
    __slots__ = ('model_type', 'base_model_id', 'budget_milli_node_hours', 'disable_early_stopping', 'multi_label')

    class ModelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODEL_TYPE_UNSPECIFIED: _ClassVar[AutoMlImageClassificationInputs.ModelType]
        CLOUD: _ClassVar[AutoMlImageClassificationInputs.ModelType]
        MOBILE_TF_LOW_LATENCY_1: _ClassVar[AutoMlImageClassificationInputs.ModelType]
        MOBILE_TF_VERSATILE_1: _ClassVar[AutoMlImageClassificationInputs.ModelType]
        MOBILE_TF_HIGH_ACCURACY_1: _ClassVar[AutoMlImageClassificationInputs.ModelType]
    MODEL_TYPE_UNSPECIFIED: AutoMlImageClassificationInputs.ModelType
    CLOUD: AutoMlImageClassificationInputs.ModelType
    MOBILE_TF_LOW_LATENCY_1: AutoMlImageClassificationInputs.ModelType
    MOBILE_TF_VERSATILE_1: AutoMlImageClassificationInputs.ModelType
    MOBILE_TF_HIGH_ACCURACY_1: AutoMlImageClassificationInputs.ModelType
    MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    BUDGET_MILLI_NODE_HOURS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_EARLY_STOPPING_FIELD_NUMBER: _ClassVar[int]
    MULTI_LABEL_FIELD_NUMBER: _ClassVar[int]
    model_type: AutoMlImageClassificationInputs.ModelType
    base_model_id: str
    budget_milli_node_hours: int
    disable_early_stopping: bool
    multi_label: bool

    def __init__(self, model_type: _Optional[_Union[AutoMlImageClassificationInputs.ModelType, str]]=..., base_model_id: _Optional[str]=..., budget_milli_node_hours: _Optional[int]=..., disable_early_stopping: bool=..., multi_label: bool=...) -> None:
        ...

class AutoMlImageClassificationMetadata(_message.Message):
    __slots__ = ('cost_milli_node_hours', 'successful_stop_reason')

    class SuccessfulStopReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESSFUL_STOP_REASON_UNSPECIFIED: _ClassVar[AutoMlImageClassificationMetadata.SuccessfulStopReason]
        BUDGET_REACHED: _ClassVar[AutoMlImageClassificationMetadata.SuccessfulStopReason]
        MODEL_CONVERGED: _ClassVar[AutoMlImageClassificationMetadata.SuccessfulStopReason]
    SUCCESSFUL_STOP_REASON_UNSPECIFIED: AutoMlImageClassificationMetadata.SuccessfulStopReason
    BUDGET_REACHED: AutoMlImageClassificationMetadata.SuccessfulStopReason
    MODEL_CONVERGED: AutoMlImageClassificationMetadata.SuccessfulStopReason
    COST_MILLI_NODE_HOURS_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFUL_STOP_REASON_FIELD_NUMBER: _ClassVar[int]
    cost_milli_node_hours: int
    successful_stop_reason: AutoMlImageClassificationMetadata.SuccessfulStopReason

    def __init__(self, cost_milli_node_hours: _Optional[int]=..., successful_stop_reason: _Optional[_Union[AutoMlImageClassificationMetadata.SuccessfulStopReason, str]]=...) -> None:
        ...