from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class RecommendationSubscriptionStatusEnum(_message.Message):
    __slots__ = ()

    class RecommendationSubscriptionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[RecommendationSubscriptionStatusEnum.RecommendationSubscriptionStatus]
        UNKNOWN: _ClassVar[RecommendationSubscriptionStatusEnum.RecommendationSubscriptionStatus]
        ENABLED: _ClassVar[RecommendationSubscriptionStatusEnum.RecommendationSubscriptionStatus]
        PAUSED: _ClassVar[RecommendationSubscriptionStatusEnum.RecommendationSubscriptionStatus]
    UNSPECIFIED: RecommendationSubscriptionStatusEnum.RecommendationSubscriptionStatus
    UNKNOWN: RecommendationSubscriptionStatusEnum.RecommendationSubscriptionStatus
    ENABLED: RecommendationSubscriptionStatusEnum.RecommendationSubscriptionStatus
    PAUSED: RecommendationSubscriptionStatusEnum.RecommendationSubscriptionStatus

    def __init__(self) -> None:
        ...