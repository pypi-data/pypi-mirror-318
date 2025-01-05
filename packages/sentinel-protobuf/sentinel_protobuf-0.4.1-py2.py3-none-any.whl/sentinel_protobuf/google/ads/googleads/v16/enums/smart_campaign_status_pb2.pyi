from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SmartCampaignStatusEnum(_message.Message):
    __slots__ = ()

    class SmartCampaignStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SmartCampaignStatusEnum.SmartCampaignStatus]
        UNKNOWN: _ClassVar[SmartCampaignStatusEnum.SmartCampaignStatus]
        PAUSED: _ClassVar[SmartCampaignStatusEnum.SmartCampaignStatus]
        NOT_ELIGIBLE: _ClassVar[SmartCampaignStatusEnum.SmartCampaignStatus]
        PENDING: _ClassVar[SmartCampaignStatusEnum.SmartCampaignStatus]
        ELIGIBLE: _ClassVar[SmartCampaignStatusEnum.SmartCampaignStatus]
        REMOVED: _ClassVar[SmartCampaignStatusEnum.SmartCampaignStatus]
        ENDED: _ClassVar[SmartCampaignStatusEnum.SmartCampaignStatus]
    UNSPECIFIED: SmartCampaignStatusEnum.SmartCampaignStatus
    UNKNOWN: SmartCampaignStatusEnum.SmartCampaignStatus
    PAUSED: SmartCampaignStatusEnum.SmartCampaignStatus
    NOT_ELIGIBLE: SmartCampaignStatusEnum.SmartCampaignStatus
    PENDING: SmartCampaignStatusEnum.SmartCampaignStatus
    ELIGIBLE: SmartCampaignStatusEnum.SmartCampaignStatus
    REMOVED: SmartCampaignStatusEnum.SmartCampaignStatus
    ENDED: SmartCampaignStatusEnum.SmartCampaignStatus

    def __init__(self) -> None:
        ...