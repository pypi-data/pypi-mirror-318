from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocalServicesLeadConversationTypeEnum(_message.Message):
    __slots__ = ()

    class ConversationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocalServicesLeadConversationTypeEnum.ConversationType]
        UNKNOWN: _ClassVar[LocalServicesLeadConversationTypeEnum.ConversationType]
        EMAIL: _ClassVar[LocalServicesLeadConversationTypeEnum.ConversationType]
        MESSAGE: _ClassVar[LocalServicesLeadConversationTypeEnum.ConversationType]
        PHONE_CALL: _ClassVar[LocalServicesLeadConversationTypeEnum.ConversationType]
        SMS: _ClassVar[LocalServicesLeadConversationTypeEnum.ConversationType]
        BOOKING: _ClassVar[LocalServicesLeadConversationTypeEnum.ConversationType]
        WHATSAPP: _ClassVar[LocalServicesLeadConversationTypeEnum.ConversationType]
        ADS_API: _ClassVar[LocalServicesLeadConversationTypeEnum.ConversationType]
    UNSPECIFIED: LocalServicesLeadConversationTypeEnum.ConversationType
    UNKNOWN: LocalServicesLeadConversationTypeEnum.ConversationType
    EMAIL: LocalServicesLeadConversationTypeEnum.ConversationType
    MESSAGE: LocalServicesLeadConversationTypeEnum.ConversationType
    PHONE_CALL: LocalServicesLeadConversationTypeEnum.ConversationType
    SMS: LocalServicesLeadConversationTypeEnum.ConversationType
    BOOKING: LocalServicesLeadConversationTypeEnum.ConversationType
    WHATSAPP: LocalServicesLeadConversationTypeEnum.ConversationType
    ADS_API: LocalServicesLeadConversationTypeEnum.ConversationType

    def __init__(self) -> None:
        ...