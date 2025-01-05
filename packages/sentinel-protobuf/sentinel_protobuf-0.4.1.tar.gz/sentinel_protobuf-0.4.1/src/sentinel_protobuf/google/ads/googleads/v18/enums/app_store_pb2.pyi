from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AppStoreEnum(_message.Message):
    __slots__ = ()

    class AppStore(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AppStoreEnum.AppStore]
        UNKNOWN: _ClassVar[AppStoreEnum.AppStore]
        APPLE_ITUNES: _ClassVar[AppStoreEnum.AppStore]
        GOOGLE_PLAY: _ClassVar[AppStoreEnum.AppStore]
    UNSPECIFIED: AppStoreEnum.AppStore
    UNKNOWN: AppStoreEnum.AppStore
    APPLE_ITUNES: AppStoreEnum.AppStore
    GOOGLE_PLAY: AppStoreEnum.AppStore

    def __init__(self) -> None:
        ...