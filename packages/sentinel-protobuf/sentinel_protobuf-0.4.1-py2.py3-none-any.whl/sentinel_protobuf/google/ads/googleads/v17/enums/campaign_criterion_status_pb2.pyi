from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CampaignCriterionStatusEnum(_message.Message):
    __slots__ = ()

    class CampaignCriterionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CampaignCriterionStatusEnum.CampaignCriterionStatus]
        UNKNOWN: _ClassVar[CampaignCriterionStatusEnum.CampaignCriterionStatus]
        ENABLED: _ClassVar[CampaignCriterionStatusEnum.CampaignCriterionStatus]
        PAUSED: _ClassVar[CampaignCriterionStatusEnum.CampaignCriterionStatus]
        REMOVED: _ClassVar[CampaignCriterionStatusEnum.CampaignCriterionStatus]
    UNSPECIFIED: CampaignCriterionStatusEnum.CampaignCriterionStatus
    UNKNOWN: CampaignCriterionStatusEnum.CampaignCriterionStatus
    ENABLED: CampaignCriterionStatusEnum.CampaignCriterionStatus
    PAUSED: CampaignCriterionStatusEnum.CampaignCriterionStatus
    REMOVED: CampaignCriterionStatusEnum.CampaignCriterionStatus

    def __init__(self) -> None:
        ...