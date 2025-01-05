from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class KeywordPlanCompetitionLevelEnum(_message.Message):
    __slots__ = ()

    class KeywordPlanCompetitionLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel]
        UNKNOWN: _ClassVar[KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel]
        LOW: _ClassVar[KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel]
        MEDIUM: _ClassVar[KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel]
        HIGH: _ClassVar[KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel]
    UNSPECIFIED: KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel
    UNKNOWN: KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel
    LOW: KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel
    MEDIUM: KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel
    HIGH: KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel

    def __init__(self) -> None:
        ...