from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionValueRulePrimaryDimensionEnum(_message.Message):
    __slots__ = ()

    class ConversionValueRulePrimaryDimension(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension]
        UNKNOWN: _ClassVar[ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension]
        NO_RULE_APPLIED: _ClassVar[ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension]
        ORIGINAL: _ClassVar[ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension]
        NEW_VS_RETURNING_USER: _ClassVar[ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension]
        GEO_LOCATION: _ClassVar[ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension]
        DEVICE: _ClassVar[ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension]
        AUDIENCE: _ClassVar[ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension]
        MULTIPLE: _ClassVar[ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension]
        ITINERARY: _ClassVar[ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension]
    UNSPECIFIED: ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension
    UNKNOWN: ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension
    NO_RULE_APPLIED: ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension
    ORIGINAL: ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension
    NEW_VS_RETURNING_USER: ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension
    GEO_LOCATION: ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension
    DEVICE: ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension
    AUDIENCE: ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension
    MULTIPLE: ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension
    ITINERARY: ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension

    def __init__(self) -> None:
        ...