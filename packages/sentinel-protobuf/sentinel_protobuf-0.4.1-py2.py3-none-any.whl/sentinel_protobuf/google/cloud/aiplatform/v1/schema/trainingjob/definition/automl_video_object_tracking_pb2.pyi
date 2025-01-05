from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AutoMlVideoObjectTracking(_message.Message):
    __slots__ = ('inputs',)
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    inputs: AutoMlVideoObjectTrackingInputs

    def __init__(self, inputs: _Optional[_Union[AutoMlVideoObjectTrackingInputs, _Mapping]]=...) -> None:
        ...

class AutoMlVideoObjectTrackingInputs(_message.Message):
    __slots__ = ('model_type',)

    class ModelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODEL_TYPE_UNSPECIFIED: _ClassVar[AutoMlVideoObjectTrackingInputs.ModelType]
        CLOUD: _ClassVar[AutoMlVideoObjectTrackingInputs.ModelType]
        MOBILE_VERSATILE_1: _ClassVar[AutoMlVideoObjectTrackingInputs.ModelType]
        MOBILE_CORAL_VERSATILE_1: _ClassVar[AutoMlVideoObjectTrackingInputs.ModelType]
        MOBILE_CORAL_LOW_LATENCY_1: _ClassVar[AutoMlVideoObjectTrackingInputs.ModelType]
        MOBILE_JETSON_VERSATILE_1: _ClassVar[AutoMlVideoObjectTrackingInputs.ModelType]
        MOBILE_JETSON_LOW_LATENCY_1: _ClassVar[AutoMlVideoObjectTrackingInputs.ModelType]
    MODEL_TYPE_UNSPECIFIED: AutoMlVideoObjectTrackingInputs.ModelType
    CLOUD: AutoMlVideoObjectTrackingInputs.ModelType
    MOBILE_VERSATILE_1: AutoMlVideoObjectTrackingInputs.ModelType
    MOBILE_CORAL_VERSATILE_1: AutoMlVideoObjectTrackingInputs.ModelType
    MOBILE_CORAL_LOW_LATENCY_1: AutoMlVideoObjectTrackingInputs.ModelType
    MOBILE_JETSON_VERSATILE_1: AutoMlVideoObjectTrackingInputs.ModelType
    MOBILE_JETSON_LOW_LATENCY_1: AutoMlVideoObjectTrackingInputs.ModelType
    MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    model_type: AutoMlVideoObjectTrackingInputs.ModelType

    def __init__(self, model_type: _Optional[_Union[AutoMlVideoObjectTrackingInputs.ModelType, str]]=...) -> None:
        ...