from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AutoMlVideoActionRecognition(_message.Message):
    __slots__ = ('inputs',)
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    inputs: AutoMlVideoActionRecognitionInputs

    def __init__(self, inputs: _Optional[_Union[AutoMlVideoActionRecognitionInputs, _Mapping]]=...) -> None:
        ...

class AutoMlVideoActionRecognitionInputs(_message.Message):
    __slots__ = ('model_type',)

    class ModelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODEL_TYPE_UNSPECIFIED: _ClassVar[AutoMlVideoActionRecognitionInputs.ModelType]
        CLOUD: _ClassVar[AutoMlVideoActionRecognitionInputs.ModelType]
        MOBILE_VERSATILE_1: _ClassVar[AutoMlVideoActionRecognitionInputs.ModelType]
        MOBILE_JETSON_VERSATILE_1: _ClassVar[AutoMlVideoActionRecognitionInputs.ModelType]
        MOBILE_CORAL_VERSATILE_1: _ClassVar[AutoMlVideoActionRecognitionInputs.ModelType]
    MODEL_TYPE_UNSPECIFIED: AutoMlVideoActionRecognitionInputs.ModelType
    CLOUD: AutoMlVideoActionRecognitionInputs.ModelType
    MOBILE_VERSATILE_1: AutoMlVideoActionRecognitionInputs.ModelType
    MOBILE_JETSON_VERSATILE_1: AutoMlVideoActionRecognitionInputs.ModelType
    MOBILE_CORAL_VERSATILE_1: AutoMlVideoActionRecognitionInputs.ModelType
    MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    model_type: AutoMlVideoActionRecognitionInputs.ModelType

    def __init__(self, model_type: _Optional[_Union[AutoMlVideoActionRecognitionInputs.ModelType, str]]=...) -> None:
        ...