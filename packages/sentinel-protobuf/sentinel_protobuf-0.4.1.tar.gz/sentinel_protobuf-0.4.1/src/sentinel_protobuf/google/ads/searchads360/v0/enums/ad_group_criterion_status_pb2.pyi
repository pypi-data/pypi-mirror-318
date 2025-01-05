from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupCriterionStatusEnum(_message.Message):
    __slots__ = ()

    class AdGroupCriterionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdGroupCriterionStatusEnum.AdGroupCriterionStatus]
        UNKNOWN: _ClassVar[AdGroupCriterionStatusEnum.AdGroupCriterionStatus]
        ENABLED: _ClassVar[AdGroupCriterionStatusEnum.AdGroupCriterionStatus]
        PAUSED: _ClassVar[AdGroupCriterionStatusEnum.AdGroupCriterionStatus]
        REMOVED: _ClassVar[AdGroupCriterionStatusEnum.AdGroupCriterionStatus]
    UNSPECIFIED: AdGroupCriterionStatusEnum.AdGroupCriterionStatus
    UNKNOWN: AdGroupCriterionStatusEnum.AdGroupCriterionStatus
    ENABLED: AdGroupCriterionStatusEnum.AdGroupCriterionStatus
    PAUSED: AdGroupCriterionStatusEnum.AdGroupCriterionStatus
    REMOVED: AdGroupCriterionStatusEnum.AdGroupCriterionStatus

    def __init__(self) -> None:
        ...