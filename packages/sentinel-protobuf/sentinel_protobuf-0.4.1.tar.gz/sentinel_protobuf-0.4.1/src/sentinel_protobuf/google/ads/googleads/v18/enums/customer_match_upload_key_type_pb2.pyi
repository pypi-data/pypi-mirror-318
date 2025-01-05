from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomerMatchUploadKeyTypeEnum(_message.Message):
    __slots__ = ()

    class CustomerMatchUploadKeyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType]
        UNKNOWN: _ClassVar[CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType]
        CONTACT_INFO: _ClassVar[CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType]
        CRM_ID: _ClassVar[CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType]
        MOBILE_ADVERTISING_ID: _ClassVar[CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType]
    UNSPECIFIED: CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType
    UNKNOWN: CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType
    CONTACT_INFO: CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType
    CRM_ID: CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType
    MOBILE_ADVERTISING_ID: CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType

    def __init__(self) -> None:
        ...