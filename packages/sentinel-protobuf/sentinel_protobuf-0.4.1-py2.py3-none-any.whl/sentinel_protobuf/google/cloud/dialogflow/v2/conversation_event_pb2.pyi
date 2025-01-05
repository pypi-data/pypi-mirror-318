from google.cloud.dialogflow.v2 import participant_pb2 as _participant_pb2
from google.cloud.dialogflow.v2 import session_pb2 as _session_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ConversationEvent(_message.Message):
    __slots__ = ('conversation', 'type', 'error_status', 'new_message_payload', 'new_recognition_result_payload')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[ConversationEvent.Type]
        CONVERSATION_STARTED: _ClassVar[ConversationEvent.Type]
        CONVERSATION_FINISHED: _ClassVar[ConversationEvent.Type]
        HUMAN_INTERVENTION_NEEDED: _ClassVar[ConversationEvent.Type]
        NEW_MESSAGE: _ClassVar[ConversationEvent.Type]
        NEW_RECOGNITION_RESULT: _ClassVar[ConversationEvent.Type]
        UNRECOVERABLE_ERROR: _ClassVar[ConversationEvent.Type]
    TYPE_UNSPECIFIED: ConversationEvent.Type
    CONVERSATION_STARTED: ConversationEvent.Type
    CONVERSATION_FINISHED: ConversationEvent.Type
    HUMAN_INTERVENTION_NEEDED: ConversationEvent.Type
    NEW_MESSAGE: ConversationEvent.Type
    NEW_RECOGNITION_RESULT: ConversationEvent.Type
    UNRECOVERABLE_ERROR: ConversationEvent.Type
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_STATUS_FIELD_NUMBER: _ClassVar[int]
    NEW_MESSAGE_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    NEW_RECOGNITION_RESULT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    conversation: str
    type: ConversationEvent.Type
    error_status: _status_pb2.Status
    new_message_payload: _participant_pb2.Message
    new_recognition_result_payload: _session_pb2.StreamingRecognitionResult

    def __init__(self, conversation: _Optional[str]=..., type: _Optional[_Union[ConversationEvent.Type, str]]=..., error_status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., new_message_payload: _Optional[_Union[_participant_pb2.Message, _Mapping]]=..., new_recognition_result_payload: _Optional[_Union[_session_pb2.StreamingRecognitionResult, _Mapping]]=...) -> None:
        ...