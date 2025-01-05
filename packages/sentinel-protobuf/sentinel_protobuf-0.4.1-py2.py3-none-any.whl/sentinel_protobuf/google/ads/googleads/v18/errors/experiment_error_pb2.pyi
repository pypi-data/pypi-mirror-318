from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ExperimentErrorEnum(_message.Message):
    __slots__ = ()

    class ExperimentError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ExperimentErrorEnum.ExperimentError]
        UNKNOWN: _ClassVar[ExperimentErrorEnum.ExperimentError]
        CANNOT_SET_START_DATE_IN_PAST: _ClassVar[ExperimentErrorEnum.ExperimentError]
        END_DATE_BEFORE_START_DATE: _ClassVar[ExperimentErrorEnum.ExperimentError]
        START_DATE_TOO_FAR_IN_FUTURE: _ClassVar[ExperimentErrorEnum.ExperimentError]
        DUPLICATE_EXPERIMENT_NAME: _ClassVar[ExperimentErrorEnum.ExperimentError]
        CANNOT_MODIFY_REMOVED_EXPERIMENT: _ClassVar[ExperimentErrorEnum.ExperimentError]
        START_DATE_ALREADY_PASSED: _ClassVar[ExperimentErrorEnum.ExperimentError]
        CANNOT_SET_END_DATE_IN_PAST: _ClassVar[ExperimentErrorEnum.ExperimentError]
        CANNOT_SET_STATUS_TO_REMOVED: _ClassVar[ExperimentErrorEnum.ExperimentError]
        CANNOT_MODIFY_PAST_END_DATE: _ClassVar[ExperimentErrorEnum.ExperimentError]
        INVALID_STATUS: _ClassVar[ExperimentErrorEnum.ExperimentError]
        INVALID_CAMPAIGN_CHANNEL_TYPE: _ClassVar[ExperimentErrorEnum.ExperimentError]
        OVERLAPPING_MEMBERS_AND_DATE_RANGE: _ClassVar[ExperimentErrorEnum.ExperimentError]
        INVALID_TRIAL_ARM_TRAFFIC_SPLIT: _ClassVar[ExperimentErrorEnum.ExperimentError]
        TRAFFIC_SPLIT_OVERLAPPING: _ClassVar[ExperimentErrorEnum.ExperimentError]
        SUM_TRIAL_ARM_TRAFFIC_UNEQUALS_TO_TRIAL_TRAFFIC_SPLIT_DENOMINATOR: _ClassVar[ExperimentErrorEnum.ExperimentError]
        CANNOT_MODIFY_TRAFFIC_SPLIT_AFTER_START: _ClassVar[ExperimentErrorEnum.ExperimentError]
        EXPERIMENT_NOT_FOUND: _ClassVar[ExperimentErrorEnum.ExperimentError]
        EXPERIMENT_NOT_YET_STARTED: _ClassVar[ExperimentErrorEnum.ExperimentError]
        CANNOT_HAVE_MULTIPLE_CONTROL_ARMS: _ClassVar[ExperimentErrorEnum.ExperimentError]
        IN_DESIGN_CAMPAIGNS_NOT_SET: _ClassVar[ExperimentErrorEnum.ExperimentError]
        CANNOT_SET_STATUS_TO_GRADUATED: _ClassVar[ExperimentErrorEnum.ExperimentError]
        CANNOT_CREATE_EXPERIMENT_CAMPAIGN_WITH_SHARED_BUDGET: _ClassVar[ExperimentErrorEnum.ExperimentError]
        CANNOT_CREATE_EXPERIMENT_CAMPAIGN_WITH_CUSTOM_BUDGET: _ClassVar[ExperimentErrorEnum.ExperimentError]
        STATUS_TRANSITION_INVALID: _ClassVar[ExperimentErrorEnum.ExperimentError]
        DUPLICATE_EXPERIMENT_CAMPAIGN_NAME: _ClassVar[ExperimentErrorEnum.ExperimentError]
        CANNOT_REMOVE_IN_CREATION_EXPERIMENT: _ClassVar[ExperimentErrorEnum.ExperimentError]
        CANNOT_ADD_CAMPAIGN_WITH_DEPRECATED_AD_TYPES: _ClassVar[ExperimentErrorEnum.ExperimentError]
        CANNOT_ENABLE_SYNC_FOR_UNSUPPORTED_EXPERIMENT_TYPE: _ClassVar[ExperimentErrorEnum.ExperimentError]
        INVALID_DURATION_FOR_AN_EXPERIMENT: _ClassVar[ExperimentErrorEnum.ExperimentError]
    UNSPECIFIED: ExperimentErrorEnum.ExperimentError
    UNKNOWN: ExperimentErrorEnum.ExperimentError
    CANNOT_SET_START_DATE_IN_PAST: ExperimentErrorEnum.ExperimentError
    END_DATE_BEFORE_START_DATE: ExperimentErrorEnum.ExperimentError
    START_DATE_TOO_FAR_IN_FUTURE: ExperimentErrorEnum.ExperimentError
    DUPLICATE_EXPERIMENT_NAME: ExperimentErrorEnum.ExperimentError
    CANNOT_MODIFY_REMOVED_EXPERIMENT: ExperimentErrorEnum.ExperimentError
    START_DATE_ALREADY_PASSED: ExperimentErrorEnum.ExperimentError
    CANNOT_SET_END_DATE_IN_PAST: ExperimentErrorEnum.ExperimentError
    CANNOT_SET_STATUS_TO_REMOVED: ExperimentErrorEnum.ExperimentError
    CANNOT_MODIFY_PAST_END_DATE: ExperimentErrorEnum.ExperimentError
    INVALID_STATUS: ExperimentErrorEnum.ExperimentError
    INVALID_CAMPAIGN_CHANNEL_TYPE: ExperimentErrorEnum.ExperimentError
    OVERLAPPING_MEMBERS_AND_DATE_RANGE: ExperimentErrorEnum.ExperimentError
    INVALID_TRIAL_ARM_TRAFFIC_SPLIT: ExperimentErrorEnum.ExperimentError
    TRAFFIC_SPLIT_OVERLAPPING: ExperimentErrorEnum.ExperimentError
    SUM_TRIAL_ARM_TRAFFIC_UNEQUALS_TO_TRIAL_TRAFFIC_SPLIT_DENOMINATOR: ExperimentErrorEnum.ExperimentError
    CANNOT_MODIFY_TRAFFIC_SPLIT_AFTER_START: ExperimentErrorEnum.ExperimentError
    EXPERIMENT_NOT_FOUND: ExperimentErrorEnum.ExperimentError
    EXPERIMENT_NOT_YET_STARTED: ExperimentErrorEnum.ExperimentError
    CANNOT_HAVE_MULTIPLE_CONTROL_ARMS: ExperimentErrorEnum.ExperimentError
    IN_DESIGN_CAMPAIGNS_NOT_SET: ExperimentErrorEnum.ExperimentError
    CANNOT_SET_STATUS_TO_GRADUATED: ExperimentErrorEnum.ExperimentError
    CANNOT_CREATE_EXPERIMENT_CAMPAIGN_WITH_SHARED_BUDGET: ExperimentErrorEnum.ExperimentError
    CANNOT_CREATE_EXPERIMENT_CAMPAIGN_WITH_CUSTOM_BUDGET: ExperimentErrorEnum.ExperimentError
    STATUS_TRANSITION_INVALID: ExperimentErrorEnum.ExperimentError
    DUPLICATE_EXPERIMENT_CAMPAIGN_NAME: ExperimentErrorEnum.ExperimentError
    CANNOT_REMOVE_IN_CREATION_EXPERIMENT: ExperimentErrorEnum.ExperimentError
    CANNOT_ADD_CAMPAIGN_WITH_DEPRECATED_AD_TYPES: ExperimentErrorEnum.ExperimentError
    CANNOT_ENABLE_SYNC_FOR_UNSUPPORTED_EXPERIMENT_TYPE: ExperimentErrorEnum.ExperimentError
    INVALID_DURATION_FOR_AN_EXPERIMENT: ExperimentErrorEnum.ExperimentError

    def __init__(self) -> None:
        ...