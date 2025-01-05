from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocalServicesLeadTypeEnum(_message.Message):
    __slots__ = ()

    class LeadType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocalServicesLeadTypeEnum.LeadType]
        UNKNOWN: _ClassVar[LocalServicesLeadTypeEnum.LeadType]
        MESSAGE: _ClassVar[LocalServicesLeadTypeEnum.LeadType]
        PHONE_CALL: _ClassVar[LocalServicesLeadTypeEnum.LeadType]
        BOOKING: _ClassVar[LocalServicesLeadTypeEnum.LeadType]
    UNSPECIFIED: LocalServicesLeadTypeEnum.LeadType
    UNKNOWN: LocalServicesLeadTypeEnum.LeadType
    MESSAGE: LocalServicesLeadTypeEnum.LeadType
    PHONE_CALL: LocalServicesLeadTypeEnum.LeadType
    BOOKING: LocalServicesLeadTypeEnum.LeadType

    def __init__(self) -> None:
        ...