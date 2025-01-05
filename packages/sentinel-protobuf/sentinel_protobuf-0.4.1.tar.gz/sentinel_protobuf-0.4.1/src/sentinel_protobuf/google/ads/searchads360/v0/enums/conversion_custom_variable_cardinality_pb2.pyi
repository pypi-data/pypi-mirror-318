from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionCustomVariableCardinalityEnum(_message.Message):
    __slots__ = ()

    class ConversionCustomVariableCardinality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionCustomVariableCardinalityEnum.ConversionCustomVariableCardinality]
        UNKNOWN: _ClassVar[ConversionCustomVariableCardinalityEnum.ConversionCustomVariableCardinality]
        BELOW_ALL_LIMITS: _ClassVar[ConversionCustomVariableCardinalityEnum.ConversionCustomVariableCardinality]
        EXCEEDS_SEGMENTATION_LIMIT_BUT_NOT_STATS_LIMIT: _ClassVar[ConversionCustomVariableCardinalityEnum.ConversionCustomVariableCardinality]
        APPROACHES_STATS_LIMIT: _ClassVar[ConversionCustomVariableCardinalityEnum.ConversionCustomVariableCardinality]
        EXCEEDS_STATS_LIMIT: _ClassVar[ConversionCustomVariableCardinalityEnum.ConversionCustomVariableCardinality]
    UNSPECIFIED: ConversionCustomVariableCardinalityEnum.ConversionCustomVariableCardinality
    UNKNOWN: ConversionCustomVariableCardinalityEnum.ConversionCustomVariableCardinality
    BELOW_ALL_LIMITS: ConversionCustomVariableCardinalityEnum.ConversionCustomVariableCardinality
    EXCEEDS_SEGMENTATION_LIMIT_BUT_NOT_STATS_LIMIT: ConversionCustomVariableCardinalityEnum.ConversionCustomVariableCardinality
    APPROACHES_STATS_LIMIT: ConversionCustomVariableCardinalityEnum.ConversionCustomVariableCardinality
    EXCEEDS_STATS_LIMIT: ConversionCustomVariableCardinalityEnum.ConversionCustomVariableCardinality

    def __init__(self) -> None:
        ...