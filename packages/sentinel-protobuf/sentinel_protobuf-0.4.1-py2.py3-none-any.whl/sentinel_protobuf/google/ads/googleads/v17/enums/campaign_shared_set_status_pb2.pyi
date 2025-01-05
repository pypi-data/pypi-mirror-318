from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CampaignSharedSetStatusEnum(_message.Message):
    __slots__ = ()

    class CampaignSharedSetStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CampaignSharedSetStatusEnum.CampaignSharedSetStatus]
        UNKNOWN: _ClassVar[CampaignSharedSetStatusEnum.CampaignSharedSetStatus]
        ENABLED: _ClassVar[CampaignSharedSetStatusEnum.CampaignSharedSetStatus]
        REMOVED: _ClassVar[CampaignSharedSetStatusEnum.CampaignSharedSetStatus]
    UNSPECIFIED: CampaignSharedSetStatusEnum.CampaignSharedSetStatus
    UNKNOWN: CampaignSharedSetStatusEnum.CampaignSharedSetStatus
    ENABLED: CampaignSharedSetStatusEnum.CampaignSharedSetStatus
    REMOVED: CampaignSharedSetStatusEnum.CampaignSharedSetStatus

    def __init__(self) -> None:
        ...