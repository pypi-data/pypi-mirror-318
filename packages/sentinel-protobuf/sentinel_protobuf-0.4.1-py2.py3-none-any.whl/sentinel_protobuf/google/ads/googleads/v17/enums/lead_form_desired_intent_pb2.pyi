from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LeadFormDesiredIntentEnum(_message.Message):
    __slots__ = ()

    class LeadFormDesiredIntent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LeadFormDesiredIntentEnum.LeadFormDesiredIntent]
        UNKNOWN: _ClassVar[LeadFormDesiredIntentEnum.LeadFormDesiredIntent]
        LOW_INTENT: _ClassVar[LeadFormDesiredIntentEnum.LeadFormDesiredIntent]
        HIGH_INTENT: _ClassVar[LeadFormDesiredIntentEnum.LeadFormDesiredIntent]
    UNSPECIFIED: LeadFormDesiredIntentEnum.LeadFormDesiredIntent
    UNKNOWN: LeadFormDesiredIntentEnum.LeadFormDesiredIntent
    LOW_INTENT: LeadFormDesiredIntentEnum.LeadFormDesiredIntent
    HIGH_INTENT: LeadFormDesiredIntentEnum.LeadFormDesiredIntent

    def __init__(self) -> None:
        ...