from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CampaignExperimentTypeEnum(_message.Message):
    __slots__ = ()

    class CampaignExperimentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CampaignExperimentTypeEnum.CampaignExperimentType]
        UNKNOWN: _ClassVar[CampaignExperimentTypeEnum.CampaignExperimentType]
        BASE: _ClassVar[CampaignExperimentTypeEnum.CampaignExperimentType]
        DRAFT: _ClassVar[CampaignExperimentTypeEnum.CampaignExperimentType]
        EXPERIMENT: _ClassVar[CampaignExperimentTypeEnum.CampaignExperimentType]
    UNSPECIFIED: CampaignExperimentTypeEnum.CampaignExperimentType
    UNKNOWN: CampaignExperimentTypeEnum.CampaignExperimentType
    BASE: CampaignExperimentTypeEnum.CampaignExperimentType
    DRAFT: CampaignExperimentTypeEnum.CampaignExperimentType
    EXPERIMENT: CampaignExperimentTypeEnum.CampaignExperimentType

    def __init__(self) -> None:
        ...