from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionCustomVariableStatusEnum(_message.Message):
    __slots__ = ()

    class ConversionCustomVariableStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus]
        UNKNOWN: _ClassVar[ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus]
        ACTIVATION_NEEDED: _ClassVar[ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus]
        ENABLED: _ClassVar[ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus]
        PAUSED: _ClassVar[ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus]
    UNSPECIFIED: ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus
    UNKNOWN: ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus
    ACTIVATION_NEEDED: ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus
    ENABLED: ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus
    PAUSED: ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus

    def __init__(self) -> None:
        ...