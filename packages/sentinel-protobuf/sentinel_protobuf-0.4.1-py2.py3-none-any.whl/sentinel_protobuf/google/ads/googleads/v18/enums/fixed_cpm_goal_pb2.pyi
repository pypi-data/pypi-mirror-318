from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FixedCpmGoalEnum(_message.Message):
    __slots__ = ()

    class FixedCpmGoal(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FixedCpmGoalEnum.FixedCpmGoal]
        UNKNOWN: _ClassVar[FixedCpmGoalEnum.FixedCpmGoal]
        REACH: _ClassVar[FixedCpmGoalEnum.FixedCpmGoal]
        TARGET_FREQUENCY: _ClassVar[FixedCpmGoalEnum.FixedCpmGoal]
    UNSPECIFIED: FixedCpmGoalEnum.FixedCpmGoal
    UNKNOWN: FixedCpmGoalEnum.FixedCpmGoal
    REACH: FixedCpmGoalEnum.FixedCpmGoal
    TARGET_FREQUENCY: FixedCpmGoalEnum.FixedCpmGoal

    def __init__(self) -> None:
        ...