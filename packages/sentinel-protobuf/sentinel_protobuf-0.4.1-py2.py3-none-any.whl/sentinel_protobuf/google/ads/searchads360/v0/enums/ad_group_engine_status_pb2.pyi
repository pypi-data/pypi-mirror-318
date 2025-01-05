from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupEngineStatusEnum(_message.Message):
    __slots__ = ()

    class AdGroupEngineStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdGroupEngineStatusEnum.AdGroupEngineStatus]
        UNKNOWN: _ClassVar[AdGroupEngineStatusEnum.AdGroupEngineStatus]
        AD_GROUP_ELIGIBLE: _ClassVar[AdGroupEngineStatusEnum.AdGroupEngineStatus]
        AD_GROUP_EXPIRED: _ClassVar[AdGroupEngineStatusEnum.AdGroupEngineStatus]
        AD_GROUP_REMOVED: _ClassVar[AdGroupEngineStatusEnum.AdGroupEngineStatus]
        AD_GROUP_DRAFT: _ClassVar[AdGroupEngineStatusEnum.AdGroupEngineStatus]
        AD_GROUP_PAUSED: _ClassVar[AdGroupEngineStatusEnum.AdGroupEngineStatus]
        AD_GROUP_SERVING: _ClassVar[AdGroupEngineStatusEnum.AdGroupEngineStatus]
        AD_GROUP_SUBMITTED: _ClassVar[AdGroupEngineStatusEnum.AdGroupEngineStatus]
        CAMPAIGN_PAUSED: _ClassVar[AdGroupEngineStatusEnum.AdGroupEngineStatus]
        ACCOUNT_PAUSED: _ClassVar[AdGroupEngineStatusEnum.AdGroupEngineStatus]
    UNSPECIFIED: AdGroupEngineStatusEnum.AdGroupEngineStatus
    UNKNOWN: AdGroupEngineStatusEnum.AdGroupEngineStatus
    AD_GROUP_ELIGIBLE: AdGroupEngineStatusEnum.AdGroupEngineStatus
    AD_GROUP_EXPIRED: AdGroupEngineStatusEnum.AdGroupEngineStatus
    AD_GROUP_REMOVED: AdGroupEngineStatusEnum.AdGroupEngineStatus
    AD_GROUP_DRAFT: AdGroupEngineStatusEnum.AdGroupEngineStatus
    AD_GROUP_PAUSED: AdGroupEngineStatusEnum.AdGroupEngineStatus
    AD_GROUP_SERVING: AdGroupEngineStatusEnum.AdGroupEngineStatus
    AD_GROUP_SUBMITTED: AdGroupEngineStatusEnum.AdGroupEngineStatus
    CAMPAIGN_PAUSED: AdGroupEngineStatusEnum.AdGroupEngineStatus
    ACCOUNT_PAUSED: AdGroupEngineStatusEnum.AdGroupEngineStatus

    def __init__(self) -> None:
        ...