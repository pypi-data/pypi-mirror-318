from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AppCampaignAppStoreEnum(_message.Message):
    __slots__ = ()

    class AppCampaignAppStore(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AppCampaignAppStoreEnum.AppCampaignAppStore]
        UNKNOWN: _ClassVar[AppCampaignAppStoreEnum.AppCampaignAppStore]
        APPLE_APP_STORE: _ClassVar[AppCampaignAppStoreEnum.AppCampaignAppStore]
        GOOGLE_APP_STORE: _ClassVar[AppCampaignAppStoreEnum.AppCampaignAppStore]
    UNSPECIFIED: AppCampaignAppStoreEnum.AppCampaignAppStore
    UNKNOWN: AppCampaignAppStoreEnum.AppCampaignAppStore
    APPLE_APP_STORE: AppCampaignAppStoreEnum.AppCampaignAppStore
    GOOGLE_APP_STORE: AppCampaignAppStoreEnum.AppCampaignAppStore

    def __init__(self) -> None:
        ...