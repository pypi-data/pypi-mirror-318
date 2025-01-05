from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomConversionGoalStatusEnum(_message.Message):
    __slots__ = ()

    class CustomConversionGoalStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomConversionGoalStatusEnum.CustomConversionGoalStatus]
        UNKNOWN: _ClassVar[CustomConversionGoalStatusEnum.CustomConversionGoalStatus]
        ENABLED: _ClassVar[CustomConversionGoalStatusEnum.CustomConversionGoalStatus]
        REMOVED: _ClassVar[CustomConversionGoalStatusEnum.CustomConversionGoalStatus]
    UNSPECIFIED: CustomConversionGoalStatusEnum.CustomConversionGoalStatus
    UNKNOWN: CustomConversionGoalStatusEnum.CustomConversionGoalStatus
    ENABLED: CustomConversionGoalStatusEnum.CustomConversionGoalStatus
    REMOVED: CustomConversionGoalStatusEnum.CustomConversionGoalStatus

    def __init__(self) -> None:
        ...