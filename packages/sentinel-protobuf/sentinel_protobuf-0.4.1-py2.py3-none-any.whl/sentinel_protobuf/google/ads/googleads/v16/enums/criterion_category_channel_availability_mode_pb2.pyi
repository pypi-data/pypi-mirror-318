from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CriterionCategoryChannelAvailabilityModeEnum(_message.Message):
    __slots__ = ()

    class CriterionCategoryChannelAvailabilityMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode]
        UNKNOWN: _ClassVar[CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode]
        ALL_CHANNELS: _ClassVar[CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode]
        CHANNEL_TYPE_AND_ALL_SUBTYPES: _ClassVar[CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode]
        CHANNEL_TYPE_AND_SUBSET_SUBTYPES: _ClassVar[CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode]
    UNSPECIFIED: CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode
    UNKNOWN: CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode
    ALL_CHANNELS: CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode
    CHANNEL_TYPE_AND_ALL_SUBTYPES: CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode
    CHANNEL_TYPE_AND_SUBSET_SUBTYPES: CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode

    def __init__(self) -> None:
        ...