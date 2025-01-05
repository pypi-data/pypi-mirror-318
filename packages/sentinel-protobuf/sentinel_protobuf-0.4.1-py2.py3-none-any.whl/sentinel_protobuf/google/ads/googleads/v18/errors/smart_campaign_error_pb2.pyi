from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SmartCampaignErrorEnum(_message.Message):
    __slots__ = ()

    class SmartCampaignError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SmartCampaignErrorEnum.SmartCampaignError]
        UNKNOWN: _ClassVar[SmartCampaignErrorEnum.SmartCampaignError]
        INVALID_BUSINESS_LOCATION_ID: _ClassVar[SmartCampaignErrorEnum.SmartCampaignError]
        INVALID_CAMPAIGN: _ClassVar[SmartCampaignErrorEnum.SmartCampaignError]
        BUSINESS_NAME_OR_BUSINESS_LOCATION_ID_MISSING: _ClassVar[SmartCampaignErrorEnum.SmartCampaignError]
        REQUIRED_SUGGESTION_FIELD_MISSING: _ClassVar[SmartCampaignErrorEnum.SmartCampaignError]
        GEO_TARGETS_REQUIRED: _ClassVar[SmartCampaignErrorEnum.SmartCampaignError]
        CANNOT_DETERMINE_SUGGESTION_LOCALE: _ClassVar[SmartCampaignErrorEnum.SmartCampaignError]
        FINAL_URL_NOT_CRAWLABLE: _ClassVar[SmartCampaignErrorEnum.SmartCampaignError]
    UNSPECIFIED: SmartCampaignErrorEnum.SmartCampaignError
    UNKNOWN: SmartCampaignErrorEnum.SmartCampaignError
    INVALID_BUSINESS_LOCATION_ID: SmartCampaignErrorEnum.SmartCampaignError
    INVALID_CAMPAIGN: SmartCampaignErrorEnum.SmartCampaignError
    BUSINESS_NAME_OR_BUSINESS_LOCATION_ID_MISSING: SmartCampaignErrorEnum.SmartCampaignError
    REQUIRED_SUGGESTION_FIELD_MISSING: SmartCampaignErrorEnum.SmartCampaignError
    GEO_TARGETS_REQUIRED: SmartCampaignErrorEnum.SmartCampaignError
    CANNOT_DETERMINE_SUGGESTION_LOCALE: SmartCampaignErrorEnum.SmartCampaignError
    FINAL_URL_NOT_CRAWLABLE: SmartCampaignErrorEnum.SmartCampaignError

    def __init__(self) -> None:
        ...