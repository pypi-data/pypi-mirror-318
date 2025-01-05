from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ValueRuleDeviceTypeEnum(_message.Message):
    __slots__ = ()

    class ValueRuleDeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ValueRuleDeviceTypeEnum.ValueRuleDeviceType]
        UNKNOWN: _ClassVar[ValueRuleDeviceTypeEnum.ValueRuleDeviceType]
        MOBILE: _ClassVar[ValueRuleDeviceTypeEnum.ValueRuleDeviceType]
        DESKTOP: _ClassVar[ValueRuleDeviceTypeEnum.ValueRuleDeviceType]
        TABLET: _ClassVar[ValueRuleDeviceTypeEnum.ValueRuleDeviceType]
    UNSPECIFIED: ValueRuleDeviceTypeEnum.ValueRuleDeviceType
    UNKNOWN: ValueRuleDeviceTypeEnum.ValueRuleDeviceType
    MOBILE: ValueRuleDeviceTypeEnum.ValueRuleDeviceType
    DESKTOP: ValueRuleDeviceTypeEnum.ValueRuleDeviceType
    TABLET: ValueRuleDeviceTypeEnum.ValueRuleDeviceType

    def __init__(self) -> None:
        ...