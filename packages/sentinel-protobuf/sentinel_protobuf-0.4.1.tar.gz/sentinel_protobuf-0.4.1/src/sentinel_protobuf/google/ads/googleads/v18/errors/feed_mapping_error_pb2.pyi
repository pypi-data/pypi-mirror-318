from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedMappingErrorEnum(_message.Message):
    __slots__ = ()

    class FeedMappingError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedMappingErrorEnum.FeedMappingError]
        UNKNOWN: _ClassVar[FeedMappingErrorEnum.FeedMappingError]
        INVALID_PLACEHOLDER_FIELD: _ClassVar[FeedMappingErrorEnum.FeedMappingError]
        INVALID_CRITERION_FIELD: _ClassVar[FeedMappingErrorEnum.FeedMappingError]
        INVALID_PLACEHOLDER_TYPE: _ClassVar[FeedMappingErrorEnum.FeedMappingError]
        INVALID_CRITERION_TYPE: _ClassVar[FeedMappingErrorEnum.FeedMappingError]
        NO_ATTRIBUTE_FIELD_MAPPINGS: _ClassVar[FeedMappingErrorEnum.FeedMappingError]
        FEED_ATTRIBUTE_TYPE_MISMATCH: _ClassVar[FeedMappingErrorEnum.FeedMappingError]
        CANNOT_OPERATE_ON_MAPPINGS_FOR_SYSTEM_GENERATED_FEED: _ClassVar[FeedMappingErrorEnum.FeedMappingError]
        MULTIPLE_MAPPINGS_FOR_PLACEHOLDER_TYPE: _ClassVar[FeedMappingErrorEnum.FeedMappingError]
        MULTIPLE_MAPPINGS_FOR_CRITERION_TYPE: _ClassVar[FeedMappingErrorEnum.FeedMappingError]
        MULTIPLE_MAPPINGS_FOR_PLACEHOLDER_FIELD: _ClassVar[FeedMappingErrorEnum.FeedMappingError]
        MULTIPLE_MAPPINGS_FOR_CRITERION_FIELD: _ClassVar[FeedMappingErrorEnum.FeedMappingError]
        UNEXPECTED_ATTRIBUTE_FIELD_MAPPINGS: _ClassVar[FeedMappingErrorEnum.FeedMappingError]
        LOCATION_PLACEHOLDER_ONLY_FOR_PLACES_FEEDS: _ClassVar[FeedMappingErrorEnum.FeedMappingError]
        CANNOT_MODIFY_MAPPINGS_FOR_TYPED_FEED: _ClassVar[FeedMappingErrorEnum.FeedMappingError]
        INVALID_PLACEHOLDER_TYPE_FOR_NON_SYSTEM_GENERATED_FEED: _ClassVar[FeedMappingErrorEnum.FeedMappingError]
        INVALID_PLACEHOLDER_TYPE_FOR_SYSTEM_GENERATED_FEED_TYPE: _ClassVar[FeedMappingErrorEnum.FeedMappingError]
        ATTRIBUTE_FIELD_MAPPING_MISSING_FIELD: _ClassVar[FeedMappingErrorEnum.FeedMappingError]
        LEGACY_FEED_TYPE_READ_ONLY: _ClassVar[FeedMappingErrorEnum.FeedMappingError]
    UNSPECIFIED: FeedMappingErrorEnum.FeedMappingError
    UNKNOWN: FeedMappingErrorEnum.FeedMappingError
    INVALID_PLACEHOLDER_FIELD: FeedMappingErrorEnum.FeedMappingError
    INVALID_CRITERION_FIELD: FeedMappingErrorEnum.FeedMappingError
    INVALID_PLACEHOLDER_TYPE: FeedMappingErrorEnum.FeedMappingError
    INVALID_CRITERION_TYPE: FeedMappingErrorEnum.FeedMappingError
    NO_ATTRIBUTE_FIELD_MAPPINGS: FeedMappingErrorEnum.FeedMappingError
    FEED_ATTRIBUTE_TYPE_MISMATCH: FeedMappingErrorEnum.FeedMappingError
    CANNOT_OPERATE_ON_MAPPINGS_FOR_SYSTEM_GENERATED_FEED: FeedMappingErrorEnum.FeedMappingError
    MULTIPLE_MAPPINGS_FOR_PLACEHOLDER_TYPE: FeedMappingErrorEnum.FeedMappingError
    MULTIPLE_MAPPINGS_FOR_CRITERION_TYPE: FeedMappingErrorEnum.FeedMappingError
    MULTIPLE_MAPPINGS_FOR_PLACEHOLDER_FIELD: FeedMappingErrorEnum.FeedMappingError
    MULTIPLE_MAPPINGS_FOR_CRITERION_FIELD: FeedMappingErrorEnum.FeedMappingError
    UNEXPECTED_ATTRIBUTE_FIELD_MAPPINGS: FeedMappingErrorEnum.FeedMappingError
    LOCATION_PLACEHOLDER_ONLY_FOR_PLACES_FEEDS: FeedMappingErrorEnum.FeedMappingError
    CANNOT_MODIFY_MAPPINGS_FOR_TYPED_FEED: FeedMappingErrorEnum.FeedMappingError
    INVALID_PLACEHOLDER_TYPE_FOR_NON_SYSTEM_GENERATED_FEED: FeedMappingErrorEnum.FeedMappingError
    INVALID_PLACEHOLDER_TYPE_FOR_SYSTEM_GENERATED_FEED_TYPE: FeedMappingErrorEnum.FeedMappingError
    ATTRIBUTE_FIELD_MAPPING_MISSING_FIELD: FeedMappingErrorEnum.FeedMappingError
    LEGACY_FEED_TYPE_READ_ONLY: FeedMappingErrorEnum.FeedMappingError

    def __init__(self) -> None:
        ...