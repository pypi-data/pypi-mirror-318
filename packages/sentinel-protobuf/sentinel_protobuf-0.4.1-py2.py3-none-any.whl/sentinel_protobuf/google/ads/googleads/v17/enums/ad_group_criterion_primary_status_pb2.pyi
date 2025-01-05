from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupCriterionPrimaryStatusEnum(_message.Message):
    __slots__ = ()

    class AdGroupCriterionPrimaryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdGroupCriterionPrimaryStatusEnum.AdGroupCriterionPrimaryStatus]
        UNKNOWN: _ClassVar[AdGroupCriterionPrimaryStatusEnum.AdGroupCriterionPrimaryStatus]
        ELIGIBLE: _ClassVar[AdGroupCriterionPrimaryStatusEnum.AdGroupCriterionPrimaryStatus]
        PAUSED: _ClassVar[AdGroupCriterionPrimaryStatusEnum.AdGroupCriterionPrimaryStatus]
        REMOVED: _ClassVar[AdGroupCriterionPrimaryStatusEnum.AdGroupCriterionPrimaryStatus]
        PENDING: _ClassVar[AdGroupCriterionPrimaryStatusEnum.AdGroupCriterionPrimaryStatus]
        NOT_ELIGIBLE: _ClassVar[AdGroupCriterionPrimaryStatusEnum.AdGroupCriterionPrimaryStatus]
    UNSPECIFIED: AdGroupCriterionPrimaryStatusEnum.AdGroupCriterionPrimaryStatus
    UNKNOWN: AdGroupCriterionPrimaryStatusEnum.AdGroupCriterionPrimaryStatus
    ELIGIBLE: AdGroupCriterionPrimaryStatusEnum.AdGroupCriterionPrimaryStatus
    PAUSED: AdGroupCriterionPrimaryStatusEnum.AdGroupCriterionPrimaryStatus
    REMOVED: AdGroupCriterionPrimaryStatusEnum.AdGroupCriterionPrimaryStatus
    PENDING: AdGroupCriterionPrimaryStatusEnum.AdGroupCriterionPrimaryStatus
    NOT_ELIGIBLE: AdGroupCriterionPrimaryStatusEnum.AdGroupCriterionPrimaryStatus

    def __init__(self) -> None:
        ...