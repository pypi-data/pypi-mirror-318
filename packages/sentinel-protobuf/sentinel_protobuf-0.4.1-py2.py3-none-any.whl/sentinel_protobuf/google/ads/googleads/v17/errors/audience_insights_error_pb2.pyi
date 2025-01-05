from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AudienceInsightsErrorEnum(_message.Message):
    __slots__ = ()

    class AudienceInsightsError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AudienceInsightsErrorEnum.AudienceInsightsError]
        UNKNOWN: _ClassVar[AudienceInsightsErrorEnum.AudienceInsightsError]
        DIMENSION_INCOMPATIBLE_WITH_TOPIC_AUDIENCE_COMBINATIONS: _ClassVar[AudienceInsightsErrorEnum.AudienceInsightsError]
    UNSPECIFIED: AudienceInsightsErrorEnum.AudienceInsightsError
    UNKNOWN: AudienceInsightsErrorEnum.AudienceInsightsError
    DIMENSION_INCOMPATIBLE_WITH_TOPIC_AUDIENCE_COMBINATIONS: AudienceInsightsErrorEnum.AudienceInsightsError

    def __init__(self) -> None:
        ...