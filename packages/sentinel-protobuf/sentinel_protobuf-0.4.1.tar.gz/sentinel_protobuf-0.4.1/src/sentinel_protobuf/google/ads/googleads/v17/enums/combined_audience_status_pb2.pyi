from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CombinedAudienceStatusEnum(_message.Message):
    __slots__ = ()

    class CombinedAudienceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CombinedAudienceStatusEnum.CombinedAudienceStatus]
        UNKNOWN: _ClassVar[CombinedAudienceStatusEnum.CombinedAudienceStatus]
        ENABLED: _ClassVar[CombinedAudienceStatusEnum.CombinedAudienceStatus]
        REMOVED: _ClassVar[CombinedAudienceStatusEnum.CombinedAudienceStatus]
    UNSPECIFIED: CombinedAudienceStatusEnum.CombinedAudienceStatus
    UNKNOWN: CombinedAudienceStatusEnum.CombinedAudienceStatus
    ENABLED: CombinedAudienceStatusEnum.CombinedAudienceStatus
    REMOVED: CombinedAudienceStatusEnum.CombinedAudienceStatus

    def __init__(self) -> None:
        ...