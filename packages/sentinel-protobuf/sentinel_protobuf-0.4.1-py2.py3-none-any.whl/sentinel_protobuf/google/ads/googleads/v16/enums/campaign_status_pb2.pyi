from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CampaignStatusEnum(_message.Message):
    __slots__ = ()

    class CampaignStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CampaignStatusEnum.CampaignStatus]
        UNKNOWN: _ClassVar[CampaignStatusEnum.CampaignStatus]
        ENABLED: _ClassVar[CampaignStatusEnum.CampaignStatus]
        PAUSED: _ClassVar[CampaignStatusEnum.CampaignStatus]
        REMOVED: _ClassVar[CampaignStatusEnum.CampaignStatus]
    UNSPECIFIED: CampaignStatusEnum.CampaignStatus
    UNKNOWN: CampaignStatusEnum.CampaignStatus
    ENABLED: CampaignStatusEnum.CampaignStatus
    PAUSED: CampaignStatusEnum.CampaignStatus
    REMOVED: CampaignStatusEnum.CampaignStatus

    def __init__(self) -> None:
        ...