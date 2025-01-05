from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocalServicesBusinessRegistrationTypeEnum(_message.Message):
    __slots__ = ()

    class LocalServicesBusinessRegistrationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocalServicesBusinessRegistrationTypeEnum.LocalServicesBusinessRegistrationType]
        UNKNOWN: _ClassVar[LocalServicesBusinessRegistrationTypeEnum.LocalServicesBusinessRegistrationType]
        NUMBER: _ClassVar[LocalServicesBusinessRegistrationTypeEnum.LocalServicesBusinessRegistrationType]
        DOCUMENT: _ClassVar[LocalServicesBusinessRegistrationTypeEnum.LocalServicesBusinessRegistrationType]
    UNSPECIFIED: LocalServicesBusinessRegistrationTypeEnum.LocalServicesBusinessRegistrationType
    UNKNOWN: LocalServicesBusinessRegistrationTypeEnum.LocalServicesBusinessRegistrationType
    NUMBER: LocalServicesBusinessRegistrationTypeEnum.LocalServicesBusinessRegistrationType
    DOCUMENT: LocalServicesBusinessRegistrationTypeEnum.LocalServicesBusinessRegistrationType

    def __init__(self) -> None:
        ...