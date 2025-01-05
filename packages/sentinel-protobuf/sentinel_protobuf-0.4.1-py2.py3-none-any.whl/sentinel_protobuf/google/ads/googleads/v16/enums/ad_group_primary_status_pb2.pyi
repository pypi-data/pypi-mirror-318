from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupPrimaryStatusEnum(_message.Message):
    __slots__ = ()

    class AdGroupPrimaryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus]
        UNKNOWN: _ClassVar[AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus]
        ELIGIBLE: _ClassVar[AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus]
        PAUSED: _ClassVar[AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus]
        REMOVED: _ClassVar[AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus]
        PENDING: _ClassVar[AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus]
        NOT_ELIGIBLE: _ClassVar[AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus]
        LIMITED: _ClassVar[AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus]
    UNSPECIFIED: AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus
    UNKNOWN: AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus
    ELIGIBLE: AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus
    PAUSED: AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus
    REMOVED: AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus
    PENDING: AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus
    NOT_ELIGIBLE: AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus
    LIMITED: AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus

    def __init__(self) -> None:
        ...