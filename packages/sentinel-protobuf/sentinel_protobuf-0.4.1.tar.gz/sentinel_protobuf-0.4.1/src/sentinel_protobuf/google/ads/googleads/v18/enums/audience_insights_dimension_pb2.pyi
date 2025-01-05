from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AudienceInsightsDimensionEnum(_message.Message):
    __slots__ = ()

    class AudienceInsightsDimension(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
        UNKNOWN: _ClassVar[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
        CATEGORY: _ClassVar[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
        KNOWLEDGE_GRAPH: _ClassVar[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
        GEO_TARGET_COUNTRY: _ClassVar[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
        SUB_COUNTRY_LOCATION: _ClassVar[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
        YOUTUBE_CHANNEL: _ClassVar[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
        YOUTUBE_DYNAMIC_LINEUP: _ClassVar[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
        AFFINITY_USER_INTEREST: _ClassVar[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
        IN_MARKET_USER_INTEREST: _ClassVar[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
        PARENTAL_STATUS: _ClassVar[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
        INCOME_RANGE: _ClassVar[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
        AGE_RANGE: _ClassVar[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
        GENDER: _ClassVar[AudienceInsightsDimensionEnum.AudienceInsightsDimension]
    UNSPECIFIED: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    UNKNOWN: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    CATEGORY: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    KNOWLEDGE_GRAPH: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    GEO_TARGET_COUNTRY: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    SUB_COUNTRY_LOCATION: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    YOUTUBE_CHANNEL: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    YOUTUBE_DYNAMIC_LINEUP: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    AFFINITY_USER_INTEREST: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    IN_MARKET_USER_INTEREST: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    PARENTAL_STATUS: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    INCOME_RANGE: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    AGE_RANGE: AudienceInsightsDimensionEnum.AudienceInsightsDimension
    GENDER: AudienceInsightsDimensionEnum.AudienceInsightsDimension

    def __init__(self) -> None:
        ...