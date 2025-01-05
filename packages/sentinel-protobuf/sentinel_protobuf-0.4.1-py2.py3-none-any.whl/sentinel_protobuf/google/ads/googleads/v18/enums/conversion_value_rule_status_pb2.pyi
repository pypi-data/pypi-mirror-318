from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionValueRuleStatusEnum(_message.Message):
    __slots__ = ()

    class ConversionValueRuleStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionValueRuleStatusEnum.ConversionValueRuleStatus]
        UNKNOWN: _ClassVar[ConversionValueRuleStatusEnum.ConversionValueRuleStatus]
        ENABLED: _ClassVar[ConversionValueRuleStatusEnum.ConversionValueRuleStatus]
        REMOVED: _ClassVar[ConversionValueRuleStatusEnum.ConversionValueRuleStatus]
        PAUSED: _ClassVar[ConversionValueRuleStatusEnum.ConversionValueRuleStatus]
    UNSPECIFIED: ConversionValueRuleStatusEnum.ConversionValueRuleStatus
    UNKNOWN: ConversionValueRuleStatusEnum.ConversionValueRuleStatus
    ENABLED: ConversionValueRuleStatusEnum.ConversionValueRuleStatus
    REMOVED: ConversionValueRuleStatusEnum.ConversionValueRuleStatus
    PAUSED: ConversionValueRuleStatusEnum.ConversionValueRuleStatus

    def __init__(self) -> None:
        ...