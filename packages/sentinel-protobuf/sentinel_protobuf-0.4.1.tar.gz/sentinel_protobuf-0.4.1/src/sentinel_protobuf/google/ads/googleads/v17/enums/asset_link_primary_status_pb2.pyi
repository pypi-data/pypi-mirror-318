from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetLinkPrimaryStatusEnum(_message.Message):
    __slots__ = ()

    class AssetLinkPrimaryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus]
        UNKNOWN: _ClassVar[AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus]
        ELIGIBLE: _ClassVar[AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus]
        PAUSED: _ClassVar[AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus]
        REMOVED: _ClassVar[AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus]
        PENDING: _ClassVar[AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus]
        LIMITED: _ClassVar[AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus]
        NOT_ELIGIBLE: _ClassVar[AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus]
    UNSPECIFIED: AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus
    UNKNOWN: AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus
    ELIGIBLE: AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus
    PAUSED: AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus
    REMOVED: AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus
    PENDING: AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus
    LIMITED: AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus
    NOT_ELIGIBLE: AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus

    def __init__(self) -> None:
        ...