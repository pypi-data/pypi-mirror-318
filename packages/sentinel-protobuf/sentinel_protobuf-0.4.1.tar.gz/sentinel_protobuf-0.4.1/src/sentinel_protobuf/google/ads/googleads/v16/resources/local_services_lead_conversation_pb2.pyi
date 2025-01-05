from google.ads.googleads.v16.enums import local_services_conversation_type_pb2 as _local_services_conversation_type_pb2
from google.ads.googleads.v16.enums import local_services_participant_type_pb2 as _local_services_participant_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocalServicesLeadConversation(_message.Message):
    __slots__ = ("resource_name", "id", "conversation_channel", "participant_type", "lead", "event_date_time", "phone_call_details", "message_details")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_TYPE_FIELD_NUMBER: _ClassVar[int]
    LEAD_FIELD_NUMBER: _ClassVar[int]
    EVENT_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PHONE_CALL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    conversation_channel: _local_services_conversation_type_pb2.LocalServicesLeadConversationTypeEnum.ConversationType
    participant_type: _local_services_participant_type_pb2.LocalServicesParticipantTypeEnum.ParticipantType
    lead: str
    event_date_time: str
    phone_call_details: PhoneCallDetails
    message_details: MessageDetails
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., conversation_channel: _Optional[_Union[_local_services_conversation_type_pb2.LocalServicesLeadConversationTypeEnum.ConversationType, str]] = ..., participant_type: _Optional[_Union[_local_services_participant_type_pb2.LocalServicesParticipantTypeEnum.ParticipantType, str]] = ..., lead: _Optional[str] = ..., event_date_time: _Optional[str] = ..., phone_call_details: _Optional[_Union[PhoneCallDetails, _Mapping]] = ..., message_details: _Optional[_Union[MessageDetails, _Mapping]] = ...) -> None: ...

class PhoneCallDetails(_message.Message):
    __slots__ = ("call_duration_millis", "call_recording_url")
    CALL_DURATION_MILLIS_FIELD_NUMBER: _ClassVar[int]
    CALL_RECORDING_URL_FIELD_NUMBER: _ClassVar[int]
    call_duration_millis: int
    call_recording_url: str
    def __init__(self, call_duration_millis: _Optional[int] = ..., call_recording_url: _Optional[str] = ...) -> None: ...

class MessageDetails(_message.Message):
    __slots__ = ("text", "attachment_urls")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_URLS_FIELD_NUMBER: _ClassVar[int]
    text: str
    attachment_urls: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, text: _Optional[str] = ..., attachment_urls: _Optional[_Iterable[str]] = ...) -> None: ...
