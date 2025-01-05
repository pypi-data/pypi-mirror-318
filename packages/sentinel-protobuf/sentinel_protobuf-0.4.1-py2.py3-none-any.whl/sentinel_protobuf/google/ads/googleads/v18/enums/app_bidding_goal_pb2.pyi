from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AppBiddingGoalEnum(_message.Message):
    __slots__ = ()

    class AppBiddingGoal(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AppBiddingGoalEnum.AppBiddingGoal]
        UNKNOWN: _ClassVar[AppBiddingGoalEnum.AppBiddingGoal]
        OPTIMIZE_FOR_INSTALL_CONVERSION_VOLUME: _ClassVar[AppBiddingGoalEnum.AppBiddingGoal]
        OPTIMIZE_FOR_IN_APP_CONVERSION_VOLUME: _ClassVar[AppBiddingGoalEnum.AppBiddingGoal]
        OPTIMIZE_FOR_TOTAL_CONVERSION_VALUE: _ClassVar[AppBiddingGoalEnum.AppBiddingGoal]
        OPTIMIZE_FOR_TARGET_IN_APP_CONVERSION: _ClassVar[AppBiddingGoalEnum.AppBiddingGoal]
        OPTIMIZE_FOR_RETURN_ON_ADVERTISING_SPEND: _ClassVar[AppBiddingGoalEnum.AppBiddingGoal]
        OPTIMIZE_FOR_INSTALL_CONVERSION_VOLUME_WITHOUT_TARGET_CPI: _ClassVar[AppBiddingGoalEnum.AppBiddingGoal]
        OPTIMIZE_FOR_PRE_REGISTRATION_CONVERSION_VOLUME: _ClassVar[AppBiddingGoalEnum.AppBiddingGoal]
    UNSPECIFIED: AppBiddingGoalEnum.AppBiddingGoal
    UNKNOWN: AppBiddingGoalEnum.AppBiddingGoal
    OPTIMIZE_FOR_INSTALL_CONVERSION_VOLUME: AppBiddingGoalEnum.AppBiddingGoal
    OPTIMIZE_FOR_IN_APP_CONVERSION_VOLUME: AppBiddingGoalEnum.AppBiddingGoal
    OPTIMIZE_FOR_TOTAL_CONVERSION_VALUE: AppBiddingGoalEnum.AppBiddingGoal
    OPTIMIZE_FOR_TARGET_IN_APP_CONVERSION: AppBiddingGoalEnum.AppBiddingGoal
    OPTIMIZE_FOR_RETURN_ON_ADVERTISING_SPEND: AppBiddingGoalEnum.AppBiddingGoal
    OPTIMIZE_FOR_INSTALL_CONVERSION_VOLUME_WITHOUT_TARGET_CPI: AppBiddingGoalEnum.AppBiddingGoal
    OPTIMIZE_FOR_PRE_REGISTRATION_CONVERSION_VOLUME: AppBiddingGoalEnum.AppBiddingGoal

    def __init__(self) -> None:
        ...