from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class OptimizationGoalTypeEnum(_message.Message):
    __slots__ = ()

    class OptimizationGoalType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[OptimizationGoalTypeEnum.OptimizationGoalType]
        UNKNOWN: _ClassVar[OptimizationGoalTypeEnum.OptimizationGoalType]
        CALL_CLICKS: _ClassVar[OptimizationGoalTypeEnum.OptimizationGoalType]
        DRIVING_DIRECTIONS: _ClassVar[OptimizationGoalTypeEnum.OptimizationGoalType]
        APP_PRE_REGISTRATION: _ClassVar[OptimizationGoalTypeEnum.OptimizationGoalType]
    UNSPECIFIED: OptimizationGoalTypeEnum.OptimizationGoalType
    UNKNOWN: OptimizationGoalTypeEnum.OptimizationGoalType
    CALL_CLICKS: OptimizationGoalTypeEnum.OptimizationGoalType
    DRIVING_DIRECTIONS: OptimizationGoalTypeEnum.OptimizationGoalType
    APP_PRE_REGISTRATION: OptimizationGoalTypeEnum.OptimizationGoalType

    def __init__(self) -> None:
        ...