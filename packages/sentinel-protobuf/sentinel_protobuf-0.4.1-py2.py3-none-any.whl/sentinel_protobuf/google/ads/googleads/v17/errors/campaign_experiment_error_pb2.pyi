from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CampaignExperimentErrorEnum(_message.Message):
    __slots__ = ()

    class CampaignExperimentError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CampaignExperimentErrorEnum.CampaignExperimentError]
        UNKNOWN: _ClassVar[CampaignExperimentErrorEnum.CampaignExperimentError]
        DUPLICATE_NAME: _ClassVar[CampaignExperimentErrorEnum.CampaignExperimentError]
        INVALID_TRANSITION: _ClassVar[CampaignExperimentErrorEnum.CampaignExperimentError]
        CANNOT_CREATE_EXPERIMENT_WITH_SHARED_BUDGET: _ClassVar[CampaignExperimentErrorEnum.CampaignExperimentError]
        CANNOT_CREATE_EXPERIMENT_FOR_REMOVED_BASE_CAMPAIGN: _ClassVar[CampaignExperimentErrorEnum.CampaignExperimentError]
        CANNOT_CREATE_EXPERIMENT_FOR_NON_PROPOSED_DRAFT: _ClassVar[CampaignExperimentErrorEnum.CampaignExperimentError]
        CUSTOMER_CANNOT_CREATE_EXPERIMENT: _ClassVar[CampaignExperimentErrorEnum.CampaignExperimentError]
        CAMPAIGN_CANNOT_CREATE_EXPERIMENT: _ClassVar[CampaignExperimentErrorEnum.CampaignExperimentError]
        EXPERIMENT_DURATIONS_MUST_NOT_OVERLAP: _ClassVar[CampaignExperimentErrorEnum.CampaignExperimentError]
        EXPERIMENT_DURATION_MUST_BE_WITHIN_CAMPAIGN_DURATION: _ClassVar[CampaignExperimentErrorEnum.CampaignExperimentError]
        CANNOT_MUTATE_EXPERIMENT_DUE_TO_STATUS: _ClassVar[CampaignExperimentErrorEnum.CampaignExperimentError]
    UNSPECIFIED: CampaignExperimentErrorEnum.CampaignExperimentError
    UNKNOWN: CampaignExperimentErrorEnum.CampaignExperimentError
    DUPLICATE_NAME: CampaignExperimentErrorEnum.CampaignExperimentError
    INVALID_TRANSITION: CampaignExperimentErrorEnum.CampaignExperimentError
    CANNOT_CREATE_EXPERIMENT_WITH_SHARED_BUDGET: CampaignExperimentErrorEnum.CampaignExperimentError
    CANNOT_CREATE_EXPERIMENT_FOR_REMOVED_BASE_CAMPAIGN: CampaignExperimentErrorEnum.CampaignExperimentError
    CANNOT_CREATE_EXPERIMENT_FOR_NON_PROPOSED_DRAFT: CampaignExperimentErrorEnum.CampaignExperimentError
    CUSTOMER_CANNOT_CREATE_EXPERIMENT: CampaignExperimentErrorEnum.CampaignExperimentError
    CAMPAIGN_CANNOT_CREATE_EXPERIMENT: CampaignExperimentErrorEnum.CampaignExperimentError
    EXPERIMENT_DURATIONS_MUST_NOT_OVERLAP: CampaignExperimentErrorEnum.CampaignExperimentError
    EXPERIMENT_DURATION_MUST_BE_WITHIN_CAMPAIGN_DURATION: CampaignExperimentErrorEnum.CampaignExperimentError
    CANNOT_MUTATE_EXPERIMENT_DUE_TO_STATUS: CampaignExperimentErrorEnum.CampaignExperimentError

    def __init__(self) -> None:
        ...