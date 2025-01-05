from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomInterestStatusEnum(_message.Message):
    __slots__ = ()

    class CustomInterestStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomInterestStatusEnum.CustomInterestStatus]
        UNKNOWN: _ClassVar[CustomInterestStatusEnum.CustomInterestStatus]
        ENABLED: _ClassVar[CustomInterestStatusEnum.CustomInterestStatus]
        REMOVED: _ClassVar[CustomInterestStatusEnum.CustomInterestStatus]
    UNSPECIFIED: CustomInterestStatusEnum.CustomInterestStatus
    UNKNOWN: CustomInterestStatusEnum.CustomInterestStatus
    ENABLED: CustomInterestStatusEnum.CustomInterestStatus
    REMOVED: CustomInterestStatusEnum.CustomInterestStatus

    def __init__(self) -> None:
        ...