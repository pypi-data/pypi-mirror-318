from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CampaignPrimaryStatusEnum(_message.Message):
    __slots__ = ()

    class CampaignPrimaryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CampaignPrimaryStatusEnum.CampaignPrimaryStatus]
        UNKNOWN: _ClassVar[CampaignPrimaryStatusEnum.CampaignPrimaryStatus]
        ELIGIBLE: _ClassVar[CampaignPrimaryStatusEnum.CampaignPrimaryStatus]
        PAUSED: _ClassVar[CampaignPrimaryStatusEnum.CampaignPrimaryStatus]
        REMOVED: _ClassVar[CampaignPrimaryStatusEnum.CampaignPrimaryStatus]
        ENDED: _ClassVar[CampaignPrimaryStatusEnum.CampaignPrimaryStatus]
        PENDING: _ClassVar[CampaignPrimaryStatusEnum.CampaignPrimaryStatus]
        MISCONFIGURED: _ClassVar[CampaignPrimaryStatusEnum.CampaignPrimaryStatus]
        LIMITED: _ClassVar[CampaignPrimaryStatusEnum.CampaignPrimaryStatus]
        LEARNING: _ClassVar[CampaignPrimaryStatusEnum.CampaignPrimaryStatus]
        NOT_ELIGIBLE: _ClassVar[CampaignPrimaryStatusEnum.CampaignPrimaryStatus]
    UNSPECIFIED: CampaignPrimaryStatusEnum.CampaignPrimaryStatus
    UNKNOWN: CampaignPrimaryStatusEnum.CampaignPrimaryStatus
    ELIGIBLE: CampaignPrimaryStatusEnum.CampaignPrimaryStatus
    PAUSED: CampaignPrimaryStatusEnum.CampaignPrimaryStatus
    REMOVED: CampaignPrimaryStatusEnum.CampaignPrimaryStatus
    ENDED: CampaignPrimaryStatusEnum.CampaignPrimaryStatus
    PENDING: CampaignPrimaryStatusEnum.CampaignPrimaryStatus
    MISCONFIGURED: CampaignPrimaryStatusEnum.CampaignPrimaryStatus
    LIMITED: CampaignPrimaryStatusEnum.CampaignPrimaryStatus
    LEARNING: CampaignPrimaryStatusEnum.CampaignPrimaryStatus
    NOT_ELIGIBLE: CampaignPrimaryStatusEnum.CampaignPrimaryStatus

    def __init__(self) -> None:
        ...