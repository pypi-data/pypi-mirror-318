from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class KeywordPlanCampaignErrorEnum(_message.Message):
    __slots__ = ()

    class KeywordPlanCampaignError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError]
        UNKNOWN: _ClassVar[KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError]
        INVALID_NAME: _ClassVar[KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError]
        INVALID_LANGUAGES: _ClassVar[KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError]
        INVALID_GEOS: _ClassVar[KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError]
        DUPLICATE_NAME: _ClassVar[KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError]
        MAX_GEOS_EXCEEDED: _ClassVar[KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError]
        MAX_LANGUAGES_EXCEEDED: _ClassVar[KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError]
    UNSPECIFIED: KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError
    UNKNOWN: KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError
    INVALID_NAME: KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError
    INVALID_LANGUAGES: KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError
    INVALID_GEOS: KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError
    DUPLICATE_NAME: KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError
    MAX_GEOS_EXCEEDED: KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError
    MAX_LANGUAGES_EXCEEDED: KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError

    def __init__(self) -> None:
        ...