from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class TargetCpaOptInRecommendationGoalEnum(_message.Message):
    __slots__ = ()

    class TargetCpaOptInRecommendationGoal(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoal]
        UNKNOWN: _ClassVar[TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoal]
        SAME_COST: _ClassVar[TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoal]
        SAME_CONVERSIONS: _ClassVar[TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoal]
        SAME_CPA: _ClassVar[TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoal]
        CLOSEST_CPA: _ClassVar[TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoal]
    UNSPECIFIED: TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoal
    UNKNOWN: TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoal
    SAME_COST: TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoal
    SAME_CONVERSIONS: TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoal
    SAME_CPA: TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoal
    CLOSEST_CPA: TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoal

    def __init__(self) -> None:
        ...