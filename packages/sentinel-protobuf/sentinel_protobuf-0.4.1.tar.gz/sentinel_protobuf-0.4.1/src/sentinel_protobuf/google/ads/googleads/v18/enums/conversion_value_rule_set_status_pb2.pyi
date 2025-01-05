from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionValueRuleSetStatusEnum(_message.Message):
    __slots__ = ()

    class ConversionValueRuleSetStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionValueRuleSetStatusEnum.ConversionValueRuleSetStatus]
        UNKNOWN: _ClassVar[ConversionValueRuleSetStatusEnum.ConversionValueRuleSetStatus]
        ENABLED: _ClassVar[ConversionValueRuleSetStatusEnum.ConversionValueRuleSetStatus]
        REMOVED: _ClassVar[ConversionValueRuleSetStatusEnum.ConversionValueRuleSetStatus]
        PAUSED: _ClassVar[ConversionValueRuleSetStatusEnum.ConversionValueRuleSetStatus]
    UNSPECIFIED: ConversionValueRuleSetStatusEnum.ConversionValueRuleSetStatus
    UNKNOWN: ConversionValueRuleSetStatusEnum.ConversionValueRuleSetStatus
    ENABLED: ConversionValueRuleSetStatusEnum.ConversionValueRuleSetStatus
    REMOVED: ConversionValueRuleSetStatusEnum.ConversionValueRuleSetStatus
    PAUSED: ConversionValueRuleSetStatusEnum.ConversionValueRuleSetStatus

    def __init__(self) -> None:
        ...