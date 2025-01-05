from google.cloud.dialogflow.v2beta1 import participant_pb2 as _participant_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class HumanAgentAssistantEvent(_message.Message):
    __slots__ = ('conversation', 'participant', 'suggestion_results')
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    conversation: str
    participant: str
    suggestion_results: _containers.RepeatedCompositeFieldContainer[_participant_pb2.SuggestionResult]

    def __init__(self, conversation: _Optional[str]=..., participant: _Optional[str]=..., suggestion_results: _Optional[_Iterable[_Union[_participant_pb2.SuggestionResult, _Mapping]]]=...) -> None:
        ...