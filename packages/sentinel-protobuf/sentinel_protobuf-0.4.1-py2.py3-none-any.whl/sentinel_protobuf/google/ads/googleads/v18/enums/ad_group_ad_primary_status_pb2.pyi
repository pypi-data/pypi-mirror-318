from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupAdPrimaryStatusEnum(_message.Message):
    __slots__ = ()

    class AdGroupAdPrimaryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus]
        UNKNOWN: _ClassVar[AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus]
        ELIGIBLE: _ClassVar[AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus]
        PAUSED: _ClassVar[AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus]
        REMOVED: _ClassVar[AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus]
        PENDING: _ClassVar[AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus]
        LIMITED: _ClassVar[AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus]
        NOT_ELIGIBLE: _ClassVar[AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus]
    UNSPECIFIED: AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus
    UNKNOWN: AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus
    ELIGIBLE: AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus
    PAUSED: AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus
    REMOVED: AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus
    PENDING: AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus
    LIMITED: AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus
    NOT_ELIGIBLE: AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus

    def __init__(self) -> None:
        ...