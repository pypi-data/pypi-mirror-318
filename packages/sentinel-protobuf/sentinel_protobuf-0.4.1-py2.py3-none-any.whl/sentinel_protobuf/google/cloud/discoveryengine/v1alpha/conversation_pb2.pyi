from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1alpha import search_service_pb2 as _search_service_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Conversation(_message.Message):
    __slots__ = ("name", "state", "user_pseudo_id", "messages", "start_time", "end_time")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Conversation.State]
        IN_PROGRESS: _ClassVar[Conversation.State]
        COMPLETED: _ClassVar[Conversation.State]
    STATE_UNSPECIFIED: Conversation.State
    IN_PROGRESS: Conversation.State
    COMPLETED: Conversation.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    USER_PSEUDO_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: Conversation.State
    user_pseudo_id: str
    messages: _containers.RepeatedCompositeFieldContainer[ConversationMessage]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[Conversation.State, str]] = ..., user_pseudo_id: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[ConversationMessage, _Mapping]]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Reply(_message.Message):
    __slots__ = ("reply", "references", "summary")
    class Reference(_message.Message):
        __slots__ = ("uri", "anchor_text", "start", "end")
        URI_FIELD_NUMBER: _ClassVar[int]
        ANCHOR_TEXT_FIELD_NUMBER: _ClassVar[int]
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        uri: str
        anchor_text: str
        start: int
        end: int
        def __init__(self, uri: _Optional[str] = ..., anchor_text: _Optional[str] = ..., start: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...
    REPLY_FIELD_NUMBER: _ClassVar[int]
    REFERENCES_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    reply: str
    references: _containers.RepeatedCompositeFieldContainer[Reply.Reference]
    summary: _search_service_pb2.SearchResponse.Summary
    def __init__(self, reply: _Optional[str] = ..., references: _Optional[_Iterable[_Union[Reply.Reference, _Mapping]]] = ..., summary: _Optional[_Union[_search_service_pb2.SearchResponse.Summary, _Mapping]] = ...) -> None: ...

class ConversationContext(_message.Message):
    __slots__ = ("context_documents", "active_document")
    CONTEXT_DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    context_documents: _containers.RepeatedScalarFieldContainer[str]
    active_document: str
    def __init__(self, context_documents: _Optional[_Iterable[str]] = ..., active_document: _Optional[str] = ...) -> None: ...

class TextInput(_message.Message):
    __slots__ = ("input", "context")
    INPUT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    input: str
    context: ConversationContext
    def __init__(self, input: _Optional[str] = ..., context: _Optional[_Union[ConversationContext, _Mapping]] = ...) -> None: ...

class ConversationMessage(_message.Message):
    __slots__ = ("user_input", "reply", "create_time")
    USER_INPUT_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    user_input: TextInput
    reply: Reply
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, user_input: _Optional[_Union[TextInput, _Mapping]] = ..., reply: _Optional[_Union[Reply, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
