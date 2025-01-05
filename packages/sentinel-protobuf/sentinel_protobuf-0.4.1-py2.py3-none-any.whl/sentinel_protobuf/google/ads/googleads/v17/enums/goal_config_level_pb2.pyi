from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class GoalConfigLevelEnum(_message.Message):
    __slots__ = ()

    class GoalConfigLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[GoalConfigLevelEnum.GoalConfigLevel]
        UNKNOWN: _ClassVar[GoalConfigLevelEnum.GoalConfigLevel]
        CUSTOMER: _ClassVar[GoalConfigLevelEnum.GoalConfigLevel]
        CAMPAIGN: _ClassVar[GoalConfigLevelEnum.GoalConfigLevel]
    UNSPECIFIED: GoalConfigLevelEnum.GoalConfigLevel
    UNKNOWN: GoalConfigLevelEnum.GoalConfigLevel
    CUSTOMER: GoalConfigLevelEnum.GoalConfigLevel
    CAMPAIGN: GoalConfigLevelEnum.GoalConfigLevel

    def __init__(self) -> None:
        ...