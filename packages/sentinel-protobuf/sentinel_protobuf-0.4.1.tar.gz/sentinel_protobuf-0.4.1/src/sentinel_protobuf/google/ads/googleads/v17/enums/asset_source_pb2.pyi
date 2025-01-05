from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetSourceEnum(_message.Message):
    __slots__ = ()

    class AssetSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetSourceEnum.AssetSource]
        UNKNOWN: _ClassVar[AssetSourceEnum.AssetSource]
        ADVERTISER: _ClassVar[AssetSourceEnum.AssetSource]
        AUTOMATICALLY_CREATED: _ClassVar[AssetSourceEnum.AssetSource]
    UNSPECIFIED: AssetSourceEnum.AssetSource
    UNKNOWN: AssetSourceEnum.AssetSource
    ADVERTISER: AssetSourceEnum.AssetSource
    AUTOMATICALLY_CREATED: AssetSourceEnum.AssetSource

    def __init__(self) -> None:
        ...