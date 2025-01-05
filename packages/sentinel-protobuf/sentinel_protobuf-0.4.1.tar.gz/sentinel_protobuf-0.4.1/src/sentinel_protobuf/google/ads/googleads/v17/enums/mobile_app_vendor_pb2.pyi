from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class MobileAppVendorEnum(_message.Message):
    __slots__ = ()

    class MobileAppVendor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[MobileAppVendorEnum.MobileAppVendor]
        UNKNOWN: _ClassVar[MobileAppVendorEnum.MobileAppVendor]
        APPLE_APP_STORE: _ClassVar[MobileAppVendorEnum.MobileAppVendor]
        GOOGLE_APP_STORE: _ClassVar[MobileAppVendorEnum.MobileAppVendor]
    UNSPECIFIED: MobileAppVendorEnum.MobileAppVendor
    UNKNOWN: MobileAppVendorEnum.MobileAppVendor
    APPLE_APP_STORE: MobileAppVendorEnum.MobileAppVendor
    GOOGLE_APP_STORE: MobileAppVendorEnum.MobileAppVendor

    def __init__(self) -> None:
        ...