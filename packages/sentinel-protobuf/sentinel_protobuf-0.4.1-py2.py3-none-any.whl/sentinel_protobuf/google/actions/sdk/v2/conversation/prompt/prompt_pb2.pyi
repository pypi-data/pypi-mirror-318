from google.actions.sdk.v2.conversation.prompt.content import canvas_pb2 as _canvas_pb2
from google.actions.sdk.v2.conversation.prompt.content import content_pb2 as _content_pb2
from google.actions.sdk.v2.conversation.prompt.content import link_pb2 as _link_pb2
from google.actions.sdk.v2.conversation.prompt import simple_pb2 as _simple_pb2
from google.actions.sdk.v2.conversation.prompt import suggestion_pb2 as _suggestion_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Prompt(_message.Message):
    __slots__ = ('append', 'override', 'first_simple', 'content', 'last_simple', 'suggestions', 'link', 'canvas')
    APPEND_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    FIRST_SIMPLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    LAST_SIMPLE_FIELD_NUMBER: _ClassVar[int]
    SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    CANVAS_FIELD_NUMBER: _ClassVar[int]
    append: bool
    override: bool
    first_simple: _simple_pb2.Simple
    content: _content_pb2.Content
    last_simple: _simple_pb2.Simple
    suggestions: _containers.RepeatedCompositeFieldContainer[_suggestion_pb2.Suggestion]
    link: _link_pb2.Link
    canvas: _canvas_pb2.Canvas

    def __init__(self, append: bool=..., override: bool=..., first_simple: _Optional[_Union[_simple_pb2.Simple, _Mapping]]=..., content: _Optional[_Union[_content_pb2.Content, _Mapping]]=..., last_simple: _Optional[_Union[_simple_pb2.Simple, _Mapping]]=..., suggestions: _Optional[_Iterable[_Union[_suggestion_pb2.Suggestion, _Mapping]]]=..., link: _Optional[_Union[_link_pb2.Link, _Mapping]]=..., canvas: _Optional[_Union[_canvas_pb2.Canvas, _Mapping]]=...) -> None:
        ...