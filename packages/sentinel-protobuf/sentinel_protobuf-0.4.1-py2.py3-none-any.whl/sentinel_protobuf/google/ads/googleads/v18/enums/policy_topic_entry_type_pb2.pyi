from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PolicyTopicEntryTypeEnum(_message.Message):
    __slots__ = ()

    class PolicyTopicEntryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PolicyTopicEntryTypeEnum.PolicyTopicEntryType]
        UNKNOWN: _ClassVar[PolicyTopicEntryTypeEnum.PolicyTopicEntryType]
        PROHIBITED: _ClassVar[PolicyTopicEntryTypeEnum.PolicyTopicEntryType]
        LIMITED: _ClassVar[PolicyTopicEntryTypeEnum.PolicyTopicEntryType]
        FULLY_LIMITED: _ClassVar[PolicyTopicEntryTypeEnum.PolicyTopicEntryType]
        DESCRIPTIVE: _ClassVar[PolicyTopicEntryTypeEnum.PolicyTopicEntryType]
        BROADENING: _ClassVar[PolicyTopicEntryTypeEnum.PolicyTopicEntryType]
        AREA_OF_INTEREST_ONLY: _ClassVar[PolicyTopicEntryTypeEnum.PolicyTopicEntryType]
    UNSPECIFIED: PolicyTopicEntryTypeEnum.PolicyTopicEntryType
    UNKNOWN: PolicyTopicEntryTypeEnum.PolicyTopicEntryType
    PROHIBITED: PolicyTopicEntryTypeEnum.PolicyTopicEntryType
    LIMITED: PolicyTopicEntryTypeEnum.PolicyTopicEntryType
    FULLY_LIMITED: PolicyTopicEntryTypeEnum.PolicyTopicEntryType
    DESCRIPTIVE: PolicyTopicEntryTypeEnum.PolicyTopicEntryType
    BROADENING: PolicyTopicEntryTypeEnum.PolicyTopicEntryType
    AREA_OF_INTEREST_ONLY: PolicyTopicEntryTypeEnum.PolicyTopicEntryType

    def __init__(self) -> None:
        ...