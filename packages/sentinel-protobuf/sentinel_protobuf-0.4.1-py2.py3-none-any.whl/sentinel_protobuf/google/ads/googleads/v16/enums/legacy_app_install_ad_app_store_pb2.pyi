from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LegacyAppInstallAdAppStoreEnum(_message.Message):
    __slots__ = ()

    class LegacyAppInstallAdAppStore(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore]
        UNKNOWN: _ClassVar[LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore]
        APPLE_APP_STORE: _ClassVar[LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore]
        GOOGLE_PLAY: _ClassVar[LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore]
        WINDOWS_STORE: _ClassVar[LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore]
        WINDOWS_PHONE_STORE: _ClassVar[LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore]
        CN_APP_STORE: _ClassVar[LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore]
    UNSPECIFIED: LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore
    UNKNOWN: LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore
    APPLE_APP_STORE: LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore
    GOOGLE_PLAY: LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore
    WINDOWS_STORE: LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore
    WINDOWS_PHONE_STORE: LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore
    CN_APP_STORE: LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore

    def __init__(self) -> None:
        ...