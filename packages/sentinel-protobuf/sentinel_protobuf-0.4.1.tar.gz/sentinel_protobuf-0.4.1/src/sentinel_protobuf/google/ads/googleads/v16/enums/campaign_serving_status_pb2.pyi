from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CampaignServingStatusEnum(_message.Message):
    __slots__ = ()

    class CampaignServingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CampaignServingStatusEnum.CampaignServingStatus]
        UNKNOWN: _ClassVar[CampaignServingStatusEnum.CampaignServingStatus]
        SERVING: _ClassVar[CampaignServingStatusEnum.CampaignServingStatus]
        NONE: _ClassVar[CampaignServingStatusEnum.CampaignServingStatus]
        ENDED: _ClassVar[CampaignServingStatusEnum.CampaignServingStatus]
        PENDING: _ClassVar[CampaignServingStatusEnum.CampaignServingStatus]
        SUSPENDED: _ClassVar[CampaignServingStatusEnum.CampaignServingStatus]
    UNSPECIFIED: CampaignServingStatusEnum.CampaignServingStatus
    UNKNOWN: CampaignServingStatusEnum.CampaignServingStatus
    SERVING: CampaignServingStatusEnum.CampaignServingStatus
    NONE: CampaignServingStatusEnum.CampaignServingStatus
    ENDED: CampaignServingStatusEnum.CampaignServingStatus
    PENDING: CampaignServingStatusEnum.CampaignServingStatus
    SUSPENDED: CampaignServingStatusEnum.CampaignServingStatus

    def __init__(self) -> None:
        ...