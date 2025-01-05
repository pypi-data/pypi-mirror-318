from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SafetySettings(_message.Message):
    __slots__ = ('default_banned_phrase_match_strategy', 'banned_phrases')

    class PhraseMatchStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PHRASE_MATCH_STRATEGY_UNSPECIFIED: _ClassVar[SafetySettings.PhraseMatchStrategy]
        PARTIAL_MATCH: _ClassVar[SafetySettings.PhraseMatchStrategy]
        WORD_MATCH: _ClassVar[SafetySettings.PhraseMatchStrategy]
    PHRASE_MATCH_STRATEGY_UNSPECIFIED: SafetySettings.PhraseMatchStrategy
    PARTIAL_MATCH: SafetySettings.PhraseMatchStrategy
    WORD_MATCH: SafetySettings.PhraseMatchStrategy

    class Phrase(_message.Message):
        __slots__ = ('text', 'language_code')
        TEXT_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
        text: str
        language_code: str

        def __init__(self, text: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
            ...
    DEFAULT_BANNED_PHRASE_MATCH_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    BANNED_PHRASES_FIELD_NUMBER: _ClassVar[int]
    default_banned_phrase_match_strategy: SafetySettings.PhraseMatchStrategy
    banned_phrases: _containers.RepeatedCompositeFieldContainer[SafetySettings.Phrase]

    def __init__(self, default_banned_phrase_match_strategy: _Optional[_Union[SafetySettings.PhraseMatchStrategy, str]]=..., banned_phrases: _Optional[_Iterable[_Union[SafetySettings.Phrase, _Mapping]]]=...) -> None:
        ...