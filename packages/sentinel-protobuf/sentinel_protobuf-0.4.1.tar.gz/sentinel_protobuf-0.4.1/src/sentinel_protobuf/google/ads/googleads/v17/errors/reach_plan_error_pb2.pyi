from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ReachPlanErrorEnum(_message.Message):
    __slots__ = ()

    class ReachPlanError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ReachPlanErrorEnum.ReachPlanError]
        UNKNOWN: _ClassVar[ReachPlanErrorEnum.ReachPlanError]
        NOT_FORECASTABLE_MISSING_RATE: _ClassVar[ReachPlanErrorEnum.ReachPlanError]
        NOT_FORECASTABLE_NOT_ENOUGH_INVENTORY: _ClassVar[ReachPlanErrorEnum.ReachPlanError]
        NOT_FORECASTABLE_ACCOUNT_NOT_ENABLED: _ClassVar[ReachPlanErrorEnum.ReachPlanError]
    UNSPECIFIED: ReachPlanErrorEnum.ReachPlanError
    UNKNOWN: ReachPlanErrorEnum.ReachPlanError
    NOT_FORECASTABLE_MISSING_RATE: ReachPlanErrorEnum.ReachPlanError
    NOT_FORECASTABLE_NOT_ENOUGH_INVENTORY: ReachPlanErrorEnum.ReachPlanError
    NOT_FORECASTABLE_ACCOUNT_NOT_ENABLED: ReachPlanErrorEnum.ReachPlanError

    def __init__(self) -> None:
        ...