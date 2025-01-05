from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class VanityPharmaDisplayUrlModeEnum(_message.Message):
    __slots__ = ()

    class VanityPharmaDisplayUrlMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[VanityPharmaDisplayUrlModeEnum.VanityPharmaDisplayUrlMode]
        UNKNOWN: _ClassVar[VanityPharmaDisplayUrlModeEnum.VanityPharmaDisplayUrlMode]
        MANUFACTURER_WEBSITE_URL: _ClassVar[VanityPharmaDisplayUrlModeEnum.VanityPharmaDisplayUrlMode]
        WEBSITE_DESCRIPTION: _ClassVar[VanityPharmaDisplayUrlModeEnum.VanityPharmaDisplayUrlMode]
    UNSPECIFIED: VanityPharmaDisplayUrlModeEnum.VanityPharmaDisplayUrlMode
    UNKNOWN: VanityPharmaDisplayUrlModeEnum.VanityPharmaDisplayUrlMode
    MANUFACTURER_WEBSITE_URL: VanityPharmaDisplayUrlModeEnum.VanityPharmaDisplayUrlMode
    WEBSITE_DESCRIPTION: VanityPharmaDisplayUrlModeEnum.VanityPharmaDisplayUrlMode

    def __init__(self) -> None:
        ...