from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AppendLeadConversationRequest(_message.Message):
    __slots__ = ('customer_id', 'conversations')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    conversations: _containers.RepeatedCompositeFieldContainer[Conversation]

    def __init__(self, customer_id: _Optional[str]=..., conversations: _Optional[_Iterable[_Union[Conversation, _Mapping]]]=...) -> None:
        ...

class AppendLeadConversationResponse(_message.Message):
    __slots__ = ('responses',)
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    responses: _containers.RepeatedCompositeFieldContainer[ConversationOrError]

    def __init__(self, responses: _Optional[_Iterable[_Union[ConversationOrError, _Mapping]]]=...) -> None:
        ...

class Conversation(_message.Message):
    __slots__ = ('local_services_lead', 'text')
    LOCAL_SERVICES_LEAD_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    local_services_lead: str
    text: str

    def __init__(self, local_services_lead: _Optional[str]=..., text: _Optional[str]=...) -> None:
        ...

class ConversationOrError(_message.Message):
    __slots__ = ('local_services_lead_conversation', 'partial_failure_error')
    LOCAL_SERVICES_LEAD_CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    local_services_lead_conversation: str
    partial_failure_error: _status_pb2.Status

    def __init__(self, local_services_lead_conversation: _Optional[str]=..., partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...