from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomAudienceStatusEnum(_message.Message):
    __slots__ = ()

    class CustomAudienceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomAudienceStatusEnum.CustomAudienceStatus]
        UNKNOWN: _ClassVar[CustomAudienceStatusEnum.CustomAudienceStatus]
        ENABLED: _ClassVar[CustomAudienceStatusEnum.CustomAudienceStatus]
        REMOVED: _ClassVar[CustomAudienceStatusEnum.CustomAudienceStatus]
    UNSPECIFIED: CustomAudienceStatusEnum.CustomAudienceStatus
    UNKNOWN: CustomAudienceStatusEnum.CustomAudienceStatus
    ENABLED: CustomAudienceStatusEnum.CustomAudienceStatus
    REMOVED: CustomAudienceStatusEnum.CustomAudienceStatus

    def __init__(self) -> None:
        ...