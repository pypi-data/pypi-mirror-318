from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class KeywordPlanCampaignKeywordErrorEnum(_message.Message):
    __slots__ = ()

    class KeywordPlanCampaignKeywordError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[KeywordPlanCampaignKeywordErrorEnum.KeywordPlanCampaignKeywordError]
        UNKNOWN: _ClassVar[KeywordPlanCampaignKeywordErrorEnum.KeywordPlanCampaignKeywordError]
        CAMPAIGN_KEYWORD_IS_POSITIVE: _ClassVar[KeywordPlanCampaignKeywordErrorEnum.KeywordPlanCampaignKeywordError]
    UNSPECIFIED: KeywordPlanCampaignKeywordErrorEnum.KeywordPlanCampaignKeywordError
    UNKNOWN: KeywordPlanCampaignKeywordErrorEnum.KeywordPlanCampaignKeywordError
    CAMPAIGN_KEYWORD_IS_POSITIVE: KeywordPlanCampaignKeywordErrorEnum.KeywordPlanCampaignKeywordError

    def __init__(self) -> None:
        ...