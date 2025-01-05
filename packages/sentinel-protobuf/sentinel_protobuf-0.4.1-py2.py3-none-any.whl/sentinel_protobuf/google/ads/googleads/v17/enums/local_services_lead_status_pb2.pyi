from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocalServicesLeadStatusEnum(_message.Message):
    __slots__ = ()

    class LeadStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocalServicesLeadStatusEnum.LeadStatus]
        UNKNOWN: _ClassVar[LocalServicesLeadStatusEnum.LeadStatus]
        NEW: _ClassVar[LocalServicesLeadStatusEnum.LeadStatus]
        ACTIVE: _ClassVar[LocalServicesLeadStatusEnum.LeadStatus]
        BOOKED: _ClassVar[LocalServicesLeadStatusEnum.LeadStatus]
        DECLINED: _ClassVar[LocalServicesLeadStatusEnum.LeadStatus]
        EXPIRED: _ClassVar[LocalServicesLeadStatusEnum.LeadStatus]
        DISABLED: _ClassVar[LocalServicesLeadStatusEnum.LeadStatus]
        CONSUMER_DECLINED: _ClassVar[LocalServicesLeadStatusEnum.LeadStatus]
        WIPED_OUT: _ClassVar[LocalServicesLeadStatusEnum.LeadStatus]
    UNSPECIFIED: LocalServicesLeadStatusEnum.LeadStatus
    UNKNOWN: LocalServicesLeadStatusEnum.LeadStatus
    NEW: LocalServicesLeadStatusEnum.LeadStatus
    ACTIVE: LocalServicesLeadStatusEnum.LeadStatus
    BOOKED: LocalServicesLeadStatusEnum.LeadStatus
    DECLINED: LocalServicesLeadStatusEnum.LeadStatus
    EXPIRED: LocalServicesLeadStatusEnum.LeadStatus
    DISABLED: LocalServicesLeadStatusEnum.LeadStatus
    CONSUMER_DECLINED: LocalServicesLeadStatusEnum.LeadStatus
    WIPED_OUT: LocalServicesLeadStatusEnum.LeadStatus

    def __init__(self) -> None:
        ...