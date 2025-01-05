from google.cloud.dialogflow.v2 import context_pb2 as _context_pb2
from google.cloud.dialogflow.v2 import intent_pb2 as _intent_pb2
from google.cloud.dialogflow.v2 import session_pb2 as _session_pb2
from google.cloud.dialogflow.v2 import session_entity_type_pb2 as _session_entity_type_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class WebhookRequest(_message.Message):
    __slots__ = ('session', 'response_id', 'query_result', 'original_detect_intent_request')
    SESSION_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_RESULT_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_DETECT_INTENT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    session: str
    response_id: str
    query_result: _session_pb2.QueryResult
    original_detect_intent_request: OriginalDetectIntentRequest

    def __init__(self, session: _Optional[str]=..., response_id: _Optional[str]=..., query_result: _Optional[_Union[_session_pb2.QueryResult, _Mapping]]=..., original_detect_intent_request: _Optional[_Union[OriginalDetectIntentRequest, _Mapping]]=...) -> None:
        ...

class WebhookResponse(_message.Message):
    __slots__ = ('fulfillment_text', 'fulfillment_messages', 'source', 'payload', 'output_contexts', 'followup_event_input', 'session_entity_types')
    FULFILLMENT_TEXT_FIELD_NUMBER: _ClassVar[int]
    FULFILLMENT_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    FOLLOWUP_EVENT_INPUT_FIELD_NUMBER: _ClassVar[int]
    SESSION_ENTITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    fulfillment_text: str
    fulfillment_messages: _containers.RepeatedCompositeFieldContainer[_intent_pb2.Intent.Message]
    source: str
    payload: _struct_pb2.Struct
    output_contexts: _containers.RepeatedCompositeFieldContainer[_context_pb2.Context]
    followup_event_input: _session_pb2.EventInput
    session_entity_types: _containers.RepeatedCompositeFieldContainer[_session_entity_type_pb2.SessionEntityType]

    def __init__(self, fulfillment_text: _Optional[str]=..., fulfillment_messages: _Optional[_Iterable[_Union[_intent_pb2.Intent.Message, _Mapping]]]=..., source: _Optional[str]=..., payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., output_contexts: _Optional[_Iterable[_Union[_context_pb2.Context, _Mapping]]]=..., followup_event_input: _Optional[_Union[_session_pb2.EventInput, _Mapping]]=..., session_entity_types: _Optional[_Iterable[_Union[_session_entity_type_pb2.SessionEntityType, _Mapping]]]=...) -> None:
        ...

class OriginalDetectIntentRequest(_message.Message):
    __slots__ = ('source', 'version', 'payload')
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    source: str
    version: str
    payload: _struct_pb2.Struct

    def __init__(self, source: _Optional[str]=..., version: _Optional[str]=..., payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...