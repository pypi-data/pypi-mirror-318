from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionAdjustmentTypeEnum(_message.Message):
    __slots__ = ()

    class ConversionAdjustmentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionAdjustmentTypeEnum.ConversionAdjustmentType]
        UNKNOWN: _ClassVar[ConversionAdjustmentTypeEnum.ConversionAdjustmentType]
        RETRACTION: _ClassVar[ConversionAdjustmentTypeEnum.ConversionAdjustmentType]
        RESTATEMENT: _ClassVar[ConversionAdjustmentTypeEnum.ConversionAdjustmentType]
        ENHANCEMENT: _ClassVar[ConversionAdjustmentTypeEnum.ConversionAdjustmentType]
    UNSPECIFIED: ConversionAdjustmentTypeEnum.ConversionAdjustmentType
    UNKNOWN: ConversionAdjustmentTypeEnum.ConversionAdjustmentType
    RETRACTION: ConversionAdjustmentTypeEnum.ConversionAdjustmentType
    RESTATEMENT: ConversionAdjustmentTypeEnum.ConversionAdjustmentType
    ENHANCEMENT: ConversionAdjustmentTypeEnum.ConversionAdjustmentType

    def __init__(self) -> None:
        ...