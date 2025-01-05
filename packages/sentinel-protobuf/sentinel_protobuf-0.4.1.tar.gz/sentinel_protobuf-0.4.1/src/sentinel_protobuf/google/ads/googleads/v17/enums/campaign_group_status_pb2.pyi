from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CampaignGroupStatusEnum(_message.Message):
    __slots__ = ()

    class CampaignGroupStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CampaignGroupStatusEnum.CampaignGroupStatus]
        UNKNOWN: _ClassVar[CampaignGroupStatusEnum.CampaignGroupStatus]
        ENABLED: _ClassVar[CampaignGroupStatusEnum.CampaignGroupStatus]
        REMOVED: _ClassVar[CampaignGroupStatusEnum.CampaignGroupStatus]
    UNSPECIFIED: CampaignGroupStatusEnum.CampaignGroupStatus
    UNKNOWN: CampaignGroupStatusEnum.CampaignGroupStatus
    ENABLED: CampaignGroupStatusEnum.CampaignGroupStatus
    REMOVED: CampaignGroupStatusEnum.CampaignGroupStatus

    def __init__(self) -> None:
        ...