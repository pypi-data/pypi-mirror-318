from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class StaticSimplePrompt(_message.Message):
    __slots__ = ('variants',)

    class Variant(_message.Message):
        __slots__ = ('speech', 'text')
        SPEECH_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        speech: str
        text: str

        def __init__(self, speech: _Optional[str]=..., text: _Optional[str]=...) -> None:
            ...
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    variants: _containers.RepeatedCompositeFieldContainer[StaticSimplePrompt.Variant]

    def __init__(self, variants: _Optional[_Iterable[_Union[StaticSimplePrompt.Variant, _Mapping]]]=...) -> None:
        ...