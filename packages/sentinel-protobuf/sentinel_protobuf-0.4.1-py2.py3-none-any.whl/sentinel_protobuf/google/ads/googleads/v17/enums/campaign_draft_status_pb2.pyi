from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CampaignDraftStatusEnum(_message.Message):
    __slots__ = ()

    class CampaignDraftStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CampaignDraftStatusEnum.CampaignDraftStatus]
        UNKNOWN: _ClassVar[CampaignDraftStatusEnum.CampaignDraftStatus]
        PROPOSED: _ClassVar[CampaignDraftStatusEnum.CampaignDraftStatus]
        REMOVED: _ClassVar[CampaignDraftStatusEnum.CampaignDraftStatus]
        PROMOTING: _ClassVar[CampaignDraftStatusEnum.CampaignDraftStatus]
        PROMOTED: _ClassVar[CampaignDraftStatusEnum.CampaignDraftStatus]
        PROMOTE_FAILED: _ClassVar[CampaignDraftStatusEnum.CampaignDraftStatus]
    UNSPECIFIED: CampaignDraftStatusEnum.CampaignDraftStatus
    UNKNOWN: CampaignDraftStatusEnum.CampaignDraftStatus
    PROPOSED: CampaignDraftStatusEnum.CampaignDraftStatus
    REMOVED: CampaignDraftStatusEnum.CampaignDraftStatus
    PROMOTING: CampaignDraftStatusEnum.CampaignDraftStatus
    PROMOTED: CampaignDraftStatusEnum.CampaignDraftStatus
    PROMOTE_FAILED: CampaignDraftStatusEnum.CampaignDraftStatus

    def __init__(self) -> None:
        ...