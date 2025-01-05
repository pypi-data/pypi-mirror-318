from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ValueRuleSetDimensionEnum(_message.Message):
    __slots__ = ()

    class ValueRuleSetDimension(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ValueRuleSetDimensionEnum.ValueRuleSetDimension]
        UNKNOWN: _ClassVar[ValueRuleSetDimensionEnum.ValueRuleSetDimension]
        GEO_LOCATION: _ClassVar[ValueRuleSetDimensionEnum.ValueRuleSetDimension]
        DEVICE: _ClassVar[ValueRuleSetDimensionEnum.ValueRuleSetDimension]
        AUDIENCE: _ClassVar[ValueRuleSetDimensionEnum.ValueRuleSetDimension]
        NO_CONDITION: _ClassVar[ValueRuleSetDimensionEnum.ValueRuleSetDimension]
        ITINERARY: _ClassVar[ValueRuleSetDimensionEnum.ValueRuleSetDimension]
    UNSPECIFIED: ValueRuleSetDimensionEnum.ValueRuleSetDimension
    UNKNOWN: ValueRuleSetDimensionEnum.ValueRuleSetDimension
    GEO_LOCATION: ValueRuleSetDimensionEnum.ValueRuleSetDimension
    DEVICE: ValueRuleSetDimensionEnum.ValueRuleSetDimension
    AUDIENCE: ValueRuleSetDimensionEnum.ValueRuleSetDimension
    NO_CONDITION: ValueRuleSetDimensionEnum.ValueRuleSetDimension
    ITINERARY: ValueRuleSetDimensionEnum.ValueRuleSetDimension

    def __init__(self) -> None:
        ...