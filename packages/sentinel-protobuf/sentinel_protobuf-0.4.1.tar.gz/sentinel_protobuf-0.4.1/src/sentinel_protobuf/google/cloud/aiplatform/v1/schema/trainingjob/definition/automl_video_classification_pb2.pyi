from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AutoMlVideoClassification(_message.Message):
    __slots__ = ('inputs',)
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    inputs: AutoMlVideoClassificationInputs

    def __init__(self, inputs: _Optional[_Union[AutoMlVideoClassificationInputs, _Mapping]]=...) -> None:
        ...

class AutoMlVideoClassificationInputs(_message.Message):
    __slots__ = ('model_type',)

    class ModelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODEL_TYPE_UNSPECIFIED: _ClassVar[AutoMlVideoClassificationInputs.ModelType]
        CLOUD: _ClassVar[AutoMlVideoClassificationInputs.ModelType]
        MOBILE_VERSATILE_1: _ClassVar[AutoMlVideoClassificationInputs.ModelType]
        MOBILE_JETSON_VERSATILE_1: _ClassVar[AutoMlVideoClassificationInputs.ModelType]
    MODEL_TYPE_UNSPECIFIED: AutoMlVideoClassificationInputs.ModelType
    CLOUD: AutoMlVideoClassificationInputs.ModelType
    MOBILE_VERSATILE_1: AutoMlVideoClassificationInputs.ModelType
    MOBILE_JETSON_VERSATILE_1: AutoMlVideoClassificationInputs.ModelType
    MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    model_type: AutoMlVideoClassificationInputs.ModelType

    def __init__(self, model_type: _Optional[_Union[AutoMlVideoClassificationInputs.ModelType, str]]=...) -> None:
        ...