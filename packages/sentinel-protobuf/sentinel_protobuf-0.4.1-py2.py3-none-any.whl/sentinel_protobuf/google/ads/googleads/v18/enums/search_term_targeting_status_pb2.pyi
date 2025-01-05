from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SearchTermTargetingStatusEnum(_message.Message):
    __slots__ = ()

    class SearchTermTargetingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SearchTermTargetingStatusEnum.SearchTermTargetingStatus]
        UNKNOWN: _ClassVar[SearchTermTargetingStatusEnum.SearchTermTargetingStatus]
        ADDED: _ClassVar[SearchTermTargetingStatusEnum.SearchTermTargetingStatus]
        EXCLUDED: _ClassVar[SearchTermTargetingStatusEnum.SearchTermTargetingStatus]
        ADDED_EXCLUDED: _ClassVar[SearchTermTargetingStatusEnum.SearchTermTargetingStatus]
        NONE: _ClassVar[SearchTermTargetingStatusEnum.SearchTermTargetingStatus]
    UNSPECIFIED: SearchTermTargetingStatusEnum.SearchTermTargetingStatus
    UNKNOWN: SearchTermTargetingStatusEnum.SearchTermTargetingStatus
    ADDED: SearchTermTargetingStatusEnum.SearchTermTargetingStatus
    EXCLUDED: SearchTermTargetingStatusEnum.SearchTermTargetingStatus
    ADDED_EXCLUDED: SearchTermTargetingStatusEnum.SearchTermTargetingStatus
    NONE: SearchTermTargetingStatusEnum.SearchTermTargetingStatus

    def __init__(self) -> None:
        ...