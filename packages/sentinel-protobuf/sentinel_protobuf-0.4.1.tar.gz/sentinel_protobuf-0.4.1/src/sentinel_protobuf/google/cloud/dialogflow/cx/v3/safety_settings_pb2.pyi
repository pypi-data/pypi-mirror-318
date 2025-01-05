from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SafetySettings(_message.Message):
    __slots__ = ('banned_phrases',)

    class Phrase(_message.Message):
        __slots__ = ('text', 'language_code')
        TEXT_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
        text: str
        language_code: str

        def __init__(self, text: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
            ...
    BANNED_PHRASES_FIELD_NUMBER: _ClassVar[int]
    banned_phrases: _containers.RepeatedCompositeFieldContainer[SafetySettings.Phrase]

    def __init__(self, banned_phrases: _Optional[_Iterable[_Union[SafetySettings.Phrase, _Mapping]]]=...) -> None:
        ...