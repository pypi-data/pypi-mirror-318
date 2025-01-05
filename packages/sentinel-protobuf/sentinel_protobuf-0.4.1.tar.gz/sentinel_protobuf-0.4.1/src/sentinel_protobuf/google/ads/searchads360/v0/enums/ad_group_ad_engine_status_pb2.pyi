from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupAdEngineStatusEnum(_message.Message):
    __slots__ = ()

    class AdGroupAdEngineStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus]
        UNKNOWN: _ClassVar[AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus]
        AD_GROUP_AD_ELIGIBLE: _ClassVar[AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus]
        AD_GROUP_AD_INAPPROPRIATE_FOR_CAMPAIGN: _ClassVar[AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus]
        AD_GROUP_AD_MOBILE_URL_UNDER_REVIEW: _ClassVar[AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus]
        AD_GROUP_AD_PARTIALLY_INVALID: _ClassVar[AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus]
        AD_GROUP_AD_TO_BE_ACTIVATED: _ClassVar[AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus]
        AD_GROUP_AD_NOT_REVIEWED: _ClassVar[AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus]
        AD_GROUP_AD_ON_HOLD: _ClassVar[AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus]
        AD_GROUP_AD_PAUSED: _ClassVar[AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus]
        AD_GROUP_AD_REMOVED: _ClassVar[AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus]
        AD_GROUP_AD_PENDING_REVIEW: _ClassVar[AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus]
        AD_GROUP_AD_UNDER_REVIEW: _ClassVar[AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus]
        AD_GROUP_AD_APPROVED: _ClassVar[AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus]
        AD_GROUP_AD_DISAPPROVED: _ClassVar[AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus]
        AD_GROUP_AD_SERVING: _ClassVar[AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus]
        AD_GROUP_AD_ACCOUNT_PAUSED: _ClassVar[AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus]
        AD_GROUP_AD_CAMPAIGN_PAUSED: _ClassVar[AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus]
        AD_GROUP_AD_AD_GROUP_PAUSED: _ClassVar[AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus]
    UNSPECIFIED: AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus
    UNKNOWN: AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus
    AD_GROUP_AD_ELIGIBLE: AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus
    AD_GROUP_AD_INAPPROPRIATE_FOR_CAMPAIGN: AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus
    AD_GROUP_AD_MOBILE_URL_UNDER_REVIEW: AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus
    AD_GROUP_AD_PARTIALLY_INVALID: AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus
    AD_GROUP_AD_TO_BE_ACTIVATED: AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus
    AD_GROUP_AD_NOT_REVIEWED: AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus
    AD_GROUP_AD_ON_HOLD: AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus
    AD_GROUP_AD_PAUSED: AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus
    AD_GROUP_AD_REMOVED: AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus
    AD_GROUP_AD_PENDING_REVIEW: AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus
    AD_GROUP_AD_UNDER_REVIEW: AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus
    AD_GROUP_AD_APPROVED: AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus
    AD_GROUP_AD_DISAPPROVED: AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus
    AD_GROUP_AD_SERVING: AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus
    AD_GROUP_AD_ACCOUNT_PAUSED: AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus
    AD_GROUP_AD_CAMPAIGN_PAUSED: AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus
    AD_GROUP_AD_AD_GROUP_PAUSED: AdGroupAdEngineStatusEnum.AdGroupAdEngineStatus

    def __init__(self) -> None:
        ...