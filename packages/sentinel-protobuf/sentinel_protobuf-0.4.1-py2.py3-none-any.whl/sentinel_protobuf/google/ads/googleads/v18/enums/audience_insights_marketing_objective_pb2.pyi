from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AudienceInsightsMarketingObjectiveEnum(_message.Message):
    __slots__ = ()

    class AudienceInsightsMarketingObjective(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AudienceInsightsMarketingObjectiveEnum.AudienceInsightsMarketingObjective]
        UNKNOWN: _ClassVar[AudienceInsightsMarketingObjectiveEnum.AudienceInsightsMarketingObjective]
        AWARENESS: _ClassVar[AudienceInsightsMarketingObjectiveEnum.AudienceInsightsMarketingObjective]
        CONSIDERATION: _ClassVar[AudienceInsightsMarketingObjectiveEnum.AudienceInsightsMarketingObjective]
    UNSPECIFIED: AudienceInsightsMarketingObjectiveEnum.AudienceInsightsMarketingObjective
    UNKNOWN: AudienceInsightsMarketingObjectiveEnum.AudienceInsightsMarketingObjective
    AWARENESS: AudienceInsightsMarketingObjectiveEnum.AudienceInsightsMarketingObjective
    CONSIDERATION: AudienceInsightsMarketingObjectiveEnum.AudienceInsightsMarketingObjective

    def __init__(self) -> None:
        ...