from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ContentLabelTypeEnum(_message.Message):
    __slots__ = ()

    class ContentLabelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        UNKNOWN: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        SEXUALLY_SUGGESTIVE: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        BELOW_THE_FOLD: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        PARKED_DOMAIN: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        JUVENILE: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        PROFANITY: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        TRAGEDY: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        VIDEO: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        VIDEO_RATING_DV_G: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        VIDEO_RATING_DV_PG: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        VIDEO_RATING_DV_T: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        VIDEO_RATING_DV_MA: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        VIDEO_NOT_YET_RATED: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        EMBEDDED_VIDEO: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        LIVE_STREAMING_VIDEO: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        SOCIAL_ISSUES: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        BRAND_SUITABILITY_CONTENT_FOR_FAMILIES: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        BRAND_SUITABILITY_GAMES_FIGHTING: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        BRAND_SUITABILITY_GAMES_MATURE: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        BRAND_SUITABILITY_HEALTH_SENSITIVE: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        BRAND_SUITABILITY_HEALTH_SOURCE_UNDETERMINED: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        BRAND_SUITABILITY_NEWS_RECENT: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        BRAND_SUITABILITY_NEWS_SENSITIVE: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        BRAND_SUITABILITY_NEWS_SOURCE_NOT_FEATURED: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        BRAND_SUITABILITY_POLITICS: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
        BRAND_SUITABILITY_RELIGION: _ClassVar[ContentLabelTypeEnum.ContentLabelType]
    UNSPECIFIED: ContentLabelTypeEnum.ContentLabelType
    UNKNOWN: ContentLabelTypeEnum.ContentLabelType
    SEXUALLY_SUGGESTIVE: ContentLabelTypeEnum.ContentLabelType
    BELOW_THE_FOLD: ContentLabelTypeEnum.ContentLabelType
    PARKED_DOMAIN: ContentLabelTypeEnum.ContentLabelType
    JUVENILE: ContentLabelTypeEnum.ContentLabelType
    PROFANITY: ContentLabelTypeEnum.ContentLabelType
    TRAGEDY: ContentLabelTypeEnum.ContentLabelType
    VIDEO: ContentLabelTypeEnum.ContentLabelType
    VIDEO_RATING_DV_G: ContentLabelTypeEnum.ContentLabelType
    VIDEO_RATING_DV_PG: ContentLabelTypeEnum.ContentLabelType
    VIDEO_RATING_DV_T: ContentLabelTypeEnum.ContentLabelType
    VIDEO_RATING_DV_MA: ContentLabelTypeEnum.ContentLabelType
    VIDEO_NOT_YET_RATED: ContentLabelTypeEnum.ContentLabelType
    EMBEDDED_VIDEO: ContentLabelTypeEnum.ContentLabelType
    LIVE_STREAMING_VIDEO: ContentLabelTypeEnum.ContentLabelType
    SOCIAL_ISSUES: ContentLabelTypeEnum.ContentLabelType
    BRAND_SUITABILITY_CONTENT_FOR_FAMILIES: ContentLabelTypeEnum.ContentLabelType
    BRAND_SUITABILITY_GAMES_FIGHTING: ContentLabelTypeEnum.ContentLabelType
    BRAND_SUITABILITY_GAMES_MATURE: ContentLabelTypeEnum.ContentLabelType
    BRAND_SUITABILITY_HEALTH_SENSITIVE: ContentLabelTypeEnum.ContentLabelType
    BRAND_SUITABILITY_HEALTH_SOURCE_UNDETERMINED: ContentLabelTypeEnum.ContentLabelType
    BRAND_SUITABILITY_NEWS_RECENT: ContentLabelTypeEnum.ContentLabelType
    BRAND_SUITABILITY_NEWS_SENSITIVE: ContentLabelTypeEnum.ContentLabelType
    BRAND_SUITABILITY_NEWS_SOURCE_NOT_FEATURED: ContentLabelTypeEnum.ContentLabelType
    BRAND_SUITABILITY_POLITICS: ContentLabelTypeEnum.ContentLabelType
    BRAND_SUITABILITY_RELIGION: ContentLabelTypeEnum.ContentLabelType

    def __init__(self) -> None:
        ...