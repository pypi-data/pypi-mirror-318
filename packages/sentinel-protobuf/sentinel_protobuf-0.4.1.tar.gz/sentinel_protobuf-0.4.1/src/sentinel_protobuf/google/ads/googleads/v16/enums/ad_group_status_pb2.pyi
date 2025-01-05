from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupStatusEnum(_message.Message):
    __slots__ = ()

    class AdGroupStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdGroupStatusEnum.AdGroupStatus]
        UNKNOWN: _ClassVar[AdGroupStatusEnum.AdGroupStatus]
        ENABLED: _ClassVar[AdGroupStatusEnum.AdGroupStatus]
        PAUSED: _ClassVar[AdGroupStatusEnum.AdGroupStatus]
        REMOVED: _ClassVar[AdGroupStatusEnum.AdGroupStatus]
    UNSPECIFIED: AdGroupStatusEnum.AdGroupStatus
    UNKNOWN: AdGroupStatusEnum.AdGroupStatus
    ENABLED: AdGroupStatusEnum.AdGroupStatus
    PAUSED: AdGroupStatusEnum.AdGroupStatus
    REMOVED: AdGroupStatusEnum.AdGroupStatus

    def __init__(self) -> None:
        ...