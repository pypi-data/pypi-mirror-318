from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ExperimentArmErrorEnum(_message.Message):
    __slots__ = ()

    class ExperimentArmError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ExperimentArmErrorEnum.ExperimentArmError]
        UNKNOWN: _ClassVar[ExperimentArmErrorEnum.ExperimentArmError]
        EXPERIMENT_ARM_COUNT_LIMIT_EXCEEDED: _ClassVar[ExperimentArmErrorEnum.ExperimentArmError]
        INVALID_CAMPAIGN_STATUS: _ClassVar[ExperimentArmErrorEnum.ExperimentArmError]
        DUPLICATE_EXPERIMENT_ARM_NAME: _ClassVar[ExperimentArmErrorEnum.ExperimentArmError]
        CANNOT_SET_TREATMENT_ARM_CAMPAIGN: _ClassVar[ExperimentArmErrorEnum.ExperimentArmError]
        CANNOT_MODIFY_CAMPAIGN_IDS: _ClassVar[ExperimentArmErrorEnum.ExperimentArmError]
        CANNOT_MODIFY_CAMPAIGN_WITHOUT_SUFFIX_SET: _ClassVar[ExperimentArmErrorEnum.ExperimentArmError]
        CANNOT_MUTATE_TRAFFIC_SPLIT_AFTER_START: _ClassVar[ExperimentArmErrorEnum.ExperimentArmError]
        CANNOT_ADD_CAMPAIGN_WITH_SHARED_BUDGET: _ClassVar[ExperimentArmErrorEnum.ExperimentArmError]
        CANNOT_ADD_CAMPAIGN_WITH_CUSTOM_BUDGET: _ClassVar[ExperimentArmErrorEnum.ExperimentArmError]
        CANNOT_ADD_CAMPAIGNS_WITH_DYNAMIC_ASSETS_ENABLED: _ClassVar[ExperimentArmErrorEnum.ExperimentArmError]
        UNSUPPORTED_CAMPAIGN_ADVERTISING_CHANNEL_SUB_TYPE: _ClassVar[ExperimentArmErrorEnum.ExperimentArmError]
        CANNOT_ADD_BASE_CAMPAIGN_WITH_DATE_RANGE: _ClassVar[ExperimentArmErrorEnum.ExperimentArmError]
        BIDDING_STRATEGY_NOT_SUPPORTED_IN_EXPERIMENTS: _ClassVar[ExperimentArmErrorEnum.ExperimentArmError]
        TRAFFIC_SPLIT_NOT_SUPPORTED_FOR_CHANNEL_TYPE: _ClassVar[ExperimentArmErrorEnum.ExperimentArmError]
    UNSPECIFIED: ExperimentArmErrorEnum.ExperimentArmError
    UNKNOWN: ExperimentArmErrorEnum.ExperimentArmError
    EXPERIMENT_ARM_COUNT_LIMIT_EXCEEDED: ExperimentArmErrorEnum.ExperimentArmError
    INVALID_CAMPAIGN_STATUS: ExperimentArmErrorEnum.ExperimentArmError
    DUPLICATE_EXPERIMENT_ARM_NAME: ExperimentArmErrorEnum.ExperimentArmError
    CANNOT_SET_TREATMENT_ARM_CAMPAIGN: ExperimentArmErrorEnum.ExperimentArmError
    CANNOT_MODIFY_CAMPAIGN_IDS: ExperimentArmErrorEnum.ExperimentArmError
    CANNOT_MODIFY_CAMPAIGN_WITHOUT_SUFFIX_SET: ExperimentArmErrorEnum.ExperimentArmError
    CANNOT_MUTATE_TRAFFIC_SPLIT_AFTER_START: ExperimentArmErrorEnum.ExperimentArmError
    CANNOT_ADD_CAMPAIGN_WITH_SHARED_BUDGET: ExperimentArmErrorEnum.ExperimentArmError
    CANNOT_ADD_CAMPAIGN_WITH_CUSTOM_BUDGET: ExperimentArmErrorEnum.ExperimentArmError
    CANNOT_ADD_CAMPAIGNS_WITH_DYNAMIC_ASSETS_ENABLED: ExperimentArmErrorEnum.ExperimentArmError
    UNSUPPORTED_CAMPAIGN_ADVERTISING_CHANNEL_SUB_TYPE: ExperimentArmErrorEnum.ExperimentArmError
    CANNOT_ADD_BASE_CAMPAIGN_WITH_DATE_RANGE: ExperimentArmErrorEnum.ExperimentArmError
    BIDDING_STRATEGY_NOT_SUPPORTED_IN_EXPERIMENTS: ExperimentArmErrorEnum.ExperimentArmError
    TRAFFIC_SPLIT_NOT_SUPPORTED_FOR_CHANNEL_TYPE: ExperimentArmErrorEnum.ExperimentArmError

    def __init__(self) -> None:
        ...