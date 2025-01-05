from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetGroupPrimaryStatusEnum(_message.Message):
    __slots__ = ()

    class AssetGroupPrimaryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus]
        UNKNOWN: _ClassVar[AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus]
        ELIGIBLE: _ClassVar[AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus]
        PAUSED: _ClassVar[AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus]
        REMOVED: _ClassVar[AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus]
        NOT_ELIGIBLE: _ClassVar[AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus]
        LIMITED: _ClassVar[AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus]
        PENDING: _ClassVar[AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus]
    UNSPECIFIED: AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus
    UNKNOWN: AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus
    ELIGIBLE: AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus
    PAUSED: AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus
    REMOVED: AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus
    NOT_ELIGIBLE: AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus
    LIMITED: AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus
    PENDING: AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus

    def __init__(self) -> None:
        ...