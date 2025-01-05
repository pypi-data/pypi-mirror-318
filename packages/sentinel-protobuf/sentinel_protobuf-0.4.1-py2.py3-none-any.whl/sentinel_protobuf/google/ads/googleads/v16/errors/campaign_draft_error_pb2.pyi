from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CampaignDraftErrorEnum(_message.Message):
    __slots__ = ()

    class CampaignDraftError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CampaignDraftErrorEnum.CampaignDraftError]
        UNKNOWN: _ClassVar[CampaignDraftErrorEnum.CampaignDraftError]
        DUPLICATE_DRAFT_NAME: _ClassVar[CampaignDraftErrorEnum.CampaignDraftError]
        INVALID_STATUS_TRANSITION_FROM_REMOVED: _ClassVar[CampaignDraftErrorEnum.CampaignDraftError]
        INVALID_STATUS_TRANSITION_FROM_PROMOTED: _ClassVar[CampaignDraftErrorEnum.CampaignDraftError]
        INVALID_STATUS_TRANSITION_FROM_PROMOTE_FAILED: _ClassVar[CampaignDraftErrorEnum.CampaignDraftError]
        CUSTOMER_CANNOT_CREATE_DRAFT: _ClassVar[CampaignDraftErrorEnum.CampaignDraftError]
        CAMPAIGN_CANNOT_CREATE_DRAFT: _ClassVar[CampaignDraftErrorEnum.CampaignDraftError]
        INVALID_DRAFT_CHANGE: _ClassVar[CampaignDraftErrorEnum.CampaignDraftError]
        INVALID_STATUS_TRANSITION: _ClassVar[CampaignDraftErrorEnum.CampaignDraftError]
        MAX_NUMBER_OF_DRAFTS_PER_CAMPAIGN_REACHED: _ClassVar[CampaignDraftErrorEnum.CampaignDraftError]
        LIST_ERRORS_FOR_PROMOTED_DRAFT_ONLY: _ClassVar[CampaignDraftErrorEnum.CampaignDraftError]
    UNSPECIFIED: CampaignDraftErrorEnum.CampaignDraftError
    UNKNOWN: CampaignDraftErrorEnum.CampaignDraftError
    DUPLICATE_DRAFT_NAME: CampaignDraftErrorEnum.CampaignDraftError
    INVALID_STATUS_TRANSITION_FROM_REMOVED: CampaignDraftErrorEnum.CampaignDraftError
    INVALID_STATUS_TRANSITION_FROM_PROMOTED: CampaignDraftErrorEnum.CampaignDraftError
    INVALID_STATUS_TRANSITION_FROM_PROMOTE_FAILED: CampaignDraftErrorEnum.CampaignDraftError
    CUSTOMER_CANNOT_CREATE_DRAFT: CampaignDraftErrorEnum.CampaignDraftError
    CAMPAIGN_CANNOT_CREATE_DRAFT: CampaignDraftErrorEnum.CampaignDraftError
    INVALID_DRAFT_CHANGE: CampaignDraftErrorEnum.CampaignDraftError
    INVALID_STATUS_TRANSITION: CampaignDraftErrorEnum.CampaignDraftError
    MAX_NUMBER_OF_DRAFTS_PER_CAMPAIGN_REACHED: CampaignDraftErrorEnum.CampaignDraftError
    LIST_ERRORS_FOR_PROMOTED_DRAFT_ONLY: CampaignDraftErrorEnum.CampaignDraftError

    def __init__(self) -> None:
        ...