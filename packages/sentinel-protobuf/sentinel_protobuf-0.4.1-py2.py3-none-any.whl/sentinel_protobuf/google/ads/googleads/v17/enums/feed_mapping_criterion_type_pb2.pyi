from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedMappingCriterionTypeEnum(_message.Message):
    __slots__ = ()

    class FeedMappingCriterionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedMappingCriterionTypeEnum.FeedMappingCriterionType]
        UNKNOWN: _ClassVar[FeedMappingCriterionTypeEnum.FeedMappingCriterionType]
        LOCATION_EXTENSION_TARGETING: _ClassVar[FeedMappingCriterionTypeEnum.FeedMappingCriterionType]
        DSA_PAGE_FEED: _ClassVar[FeedMappingCriterionTypeEnum.FeedMappingCriterionType]
    UNSPECIFIED: FeedMappingCriterionTypeEnum.FeedMappingCriterionType
    UNKNOWN: FeedMappingCriterionTypeEnum.FeedMappingCriterionType
    LOCATION_EXTENSION_TARGETING: FeedMappingCriterionTypeEnum.FeedMappingCriterionType
    DSA_PAGE_FEED: FeedMappingCriterionTypeEnum.FeedMappingCriterionType

    def __init__(self) -> None:
        ...