from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomClass(_message.Message):
    __slots__ = ('name', 'custom_class_id', 'items')

    class ClassItem(_message.Message):
        __slots__ = ('value',)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str

        def __init__(self, value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    name: str
    custom_class_id: str
    items: _containers.RepeatedCompositeFieldContainer[CustomClass.ClassItem]

    def __init__(self, name: _Optional[str]=..., custom_class_id: _Optional[str]=..., items: _Optional[_Iterable[_Union[CustomClass.ClassItem, _Mapping]]]=...) -> None:
        ...

class PhraseSet(_message.Message):
    __slots__ = ('name', 'phrases', 'boost')

    class Phrase(_message.Message):
        __slots__ = ('value', 'boost')
        VALUE_FIELD_NUMBER: _ClassVar[int]
        BOOST_FIELD_NUMBER: _ClassVar[int]
        value: str
        boost: float

        def __init__(self, value: _Optional[str]=..., boost: _Optional[float]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHRASES_FIELD_NUMBER: _ClassVar[int]
    BOOST_FIELD_NUMBER: _ClassVar[int]
    name: str
    phrases: _containers.RepeatedCompositeFieldContainer[PhraseSet.Phrase]
    boost: float

    def __init__(self, name: _Optional[str]=..., phrases: _Optional[_Iterable[_Union[PhraseSet.Phrase, _Mapping]]]=..., boost: _Optional[float]=...) -> None:
        ...

class SpeechAdaptation(_message.Message):
    __slots__ = ('phrase_sets', 'phrase_set_references', 'custom_classes', 'abnf_grammar')

    class ABNFGrammar(_message.Message):
        __slots__ = ('abnf_strings',)
        ABNF_STRINGS_FIELD_NUMBER: _ClassVar[int]
        abnf_strings: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, abnf_strings: _Optional[_Iterable[str]]=...) -> None:
            ...
    PHRASE_SETS_FIELD_NUMBER: _ClassVar[int]
    PHRASE_SET_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CLASSES_FIELD_NUMBER: _ClassVar[int]
    ABNF_GRAMMAR_FIELD_NUMBER: _ClassVar[int]
    phrase_sets: _containers.RepeatedCompositeFieldContainer[PhraseSet]
    phrase_set_references: _containers.RepeatedScalarFieldContainer[str]
    custom_classes: _containers.RepeatedCompositeFieldContainer[CustomClass]
    abnf_grammar: SpeechAdaptation.ABNFGrammar

    def __init__(self, phrase_sets: _Optional[_Iterable[_Union[PhraseSet, _Mapping]]]=..., phrase_set_references: _Optional[_Iterable[str]]=..., custom_classes: _Optional[_Iterable[_Union[CustomClass, _Mapping]]]=..., abnf_grammar: _Optional[_Union[SpeechAdaptation.ABNFGrammar, _Mapping]]=...) -> None:
        ...

class TranscriptNormalization(_message.Message):
    __slots__ = ('entries',)

    class Entry(_message.Message):
        __slots__ = ('search', 'replace', 'case_sensitive')
        SEARCH_FIELD_NUMBER: _ClassVar[int]
        REPLACE_FIELD_NUMBER: _ClassVar[int]
        CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
        search: str
        replace: str
        case_sensitive: bool

        def __init__(self, search: _Optional[str]=..., replace: _Optional[str]=..., case_sensitive: bool=...) -> None:
            ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[TranscriptNormalization.Entry]

    def __init__(self, entries: _Optional[_Iterable[_Union[TranscriptNormalization.Entry, _Mapping]]]=...) -> None:
        ...