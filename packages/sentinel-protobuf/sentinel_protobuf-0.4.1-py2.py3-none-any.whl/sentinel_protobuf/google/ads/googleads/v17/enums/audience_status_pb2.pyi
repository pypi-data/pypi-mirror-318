from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AudienceStatusEnum(_message.Message):
    __slots__ = ()

    class AudienceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AudienceStatusEnum.AudienceStatus]
        UNKNOWN: _ClassVar[AudienceStatusEnum.AudienceStatus]
        ENABLED: _ClassVar[AudienceStatusEnum.AudienceStatus]
        REMOVED: _ClassVar[AudienceStatusEnum.AudienceStatus]
    UNSPECIFIED: AudienceStatusEnum.AudienceStatus
    UNKNOWN: AudienceStatusEnum.AudienceStatus
    ENABLED: AudienceStatusEnum.AudienceStatus
    REMOVED: AudienceStatusEnum.AudienceStatus

    def __init__(self) -> None:
        ...