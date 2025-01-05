from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class OperatingSystemVersionOperatorTypeEnum(_message.Message):
    __slots__ = ()

    class OperatingSystemVersionOperatorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorType]
        UNKNOWN: _ClassVar[OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorType]
        EQUALS_TO: _ClassVar[OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorType]
        GREATER_THAN_EQUALS_TO: _ClassVar[OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorType]
    UNSPECIFIED: OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorType
    UNKNOWN: OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorType
    EQUALS_TO: OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorType
    GREATER_THAN_EQUALS_TO: OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorType

    def __init__(self) -> None:
        ...