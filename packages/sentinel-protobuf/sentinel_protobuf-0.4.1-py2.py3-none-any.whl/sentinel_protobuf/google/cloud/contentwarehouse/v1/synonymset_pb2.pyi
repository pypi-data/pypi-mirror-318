from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SynonymSet(_message.Message):
    __slots__ = ('name', 'context', 'synonyms')

    class Synonym(_message.Message):
        __slots__ = ('words',)
        WORDS_FIELD_NUMBER: _ClassVar[int]
        words: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, words: _Optional[_Iterable[str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SYNONYMS_FIELD_NUMBER: _ClassVar[int]
    name: str
    context: str
    synonyms: _containers.RepeatedCompositeFieldContainer[SynonymSet.Synonym]

    def __init__(self, name: _Optional[str]=..., context: _Optional[str]=..., synonyms: _Optional[_Iterable[_Union[SynonymSet.Synonym, _Mapping]]]=...) -> None:
        ...