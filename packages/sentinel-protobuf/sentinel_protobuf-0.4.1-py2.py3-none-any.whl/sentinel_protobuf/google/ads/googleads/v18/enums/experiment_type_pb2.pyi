from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ExperimentTypeEnum(_message.Message):
    __slots__ = ()

    class ExperimentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ExperimentTypeEnum.ExperimentType]
        UNKNOWN: _ClassVar[ExperimentTypeEnum.ExperimentType]
        DISPLAY_AND_VIDEO_360: _ClassVar[ExperimentTypeEnum.ExperimentType]
        AD_VARIATION: _ClassVar[ExperimentTypeEnum.ExperimentType]
        YOUTUBE_CUSTOM: _ClassVar[ExperimentTypeEnum.ExperimentType]
        DISPLAY_CUSTOM: _ClassVar[ExperimentTypeEnum.ExperimentType]
        SEARCH_CUSTOM: _ClassVar[ExperimentTypeEnum.ExperimentType]
        DISPLAY_AUTOMATED_BIDDING_STRATEGY: _ClassVar[ExperimentTypeEnum.ExperimentType]
        SEARCH_AUTOMATED_BIDDING_STRATEGY: _ClassVar[ExperimentTypeEnum.ExperimentType]
        SHOPPING_AUTOMATED_BIDDING_STRATEGY: _ClassVar[ExperimentTypeEnum.ExperimentType]
        SMART_MATCHING: _ClassVar[ExperimentTypeEnum.ExperimentType]
        HOTEL_CUSTOM: _ClassVar[ExperimentTypeEnum.ExperimentType]
    UNSPECIFIED: ExperimentTypeEnum.ExperimentType
    UNKNOWN: ExperimentTypeEnum.ExperimentType
    DISPLAY_AND_VIDEO_360: ExperimentTypeEnum.ExperimentType
    AD_VARIATION: ExperimentTypeEnum.ExperimentType
    YOUTUBE_CUSTOM: ExperimentTypeEnum.ExperimentType
    DISPLAY_CUSTOM: ExperimentTypeEnum.ExperimentType
    SEARCH_CUSTOM: ExperimentTypeEnum.ExperimentType
    DISPLAY_AUTOMATED_BIDDING_STRATEGY: ExperimentTypeEnum.ExperimentType
    SEARCH_AUTOMATED_BIDDING_STRATEGY: ExperimentTypeEnum.ExperimentType
    SHOPPING_AUTOMATED_BIDDING_STRATEGY: ExperimentTypeEnum.ExperimentType
    SMART_MATCHING: ExperimentTypeEnum.ExperimentType
    HOTEL_CUSTOM: ExperimentTypeEnum.ExperimentType

    def __init__(self) -> None:
        ...