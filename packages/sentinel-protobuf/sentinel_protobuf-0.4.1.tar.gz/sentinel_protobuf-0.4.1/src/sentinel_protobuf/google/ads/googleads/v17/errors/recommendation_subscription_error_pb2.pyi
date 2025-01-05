from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class RecommendationSubscriptionErrorEnum(_message.Message):
    __slots__ = ()

    class RecommendationSubscriptionError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[RecommendationSubscriptionErrorEnum.RecommendationSubscriptionError]
        UNKNOWN: _ClassVar[RecommendationSubscriptionErrorEnum.RecommendationSubscriptionError]
    UNSPECIFIED: RecommendationSubscriptionErrorEnum.RecommendationSubscriptionError
    UNKNOWN: RecommendationSubscriptionErrorEnum.RecommendationSubscriptionError

    def __init__(self) -> None:
        ...