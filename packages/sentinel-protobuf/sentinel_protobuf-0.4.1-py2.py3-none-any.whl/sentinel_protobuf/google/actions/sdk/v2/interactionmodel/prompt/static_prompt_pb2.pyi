from google.actions.sdk.v2.interactionmodel.prompt.content import static_canvas_prompt_pb2 as _static_canvas_prompt_pb2
from google.actions.sdk.v2.interactionmodel.prompt.content import static_content_prompt_pb2 as _static_content_prompt_pb2
from google.actions.sdk.v2.interactionmodel.prompt.content import static_link_prompt_pb2 as _static_link_prompt_pb2
from google.actions.sdk.v2.interactionmodel.prompt import static_simple_prompt_pb2 as _static_simple_prompt_pb2
from google.actions.sdk.v2.interactionmodel.prompt import suggestion_pb2 as _suggestion_pb2
from google.actions.sdk.v2.interactionmodel.prompt import surface_capabilities_pb2 as _surface_capabilities_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class StaticPrompt(_message.Message):
    __slots__ = ('candidates',)

    class StaticPromptCandidate(_message.Message):
        __slots__ = ('selector', 'prompt_response')

        class StaticPromptResponse(_message.Message):
            __slots__ = ('first_simple', 'content', 'last_simple', 'suggestions', 'link', 'override', 'canvas')
            FIRST_SIMPLE_FIELD_NUMBER: _ClassVar[int]
            CONTENT_FIELD_NUMBER: _ClassVar[int]
            LAST_SIMPLE_FIELD_NUMBER: _ClassVar[int]
            SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
            LINK_FIELD_NUMBER: _ClassVar[int]
            OVERRIDE_FIELD_NUMBER: _ClassVar[int]
            CANVAS_FIELD_NUMBER: _ClassVar[int]
            first_simple: _static_simple_prompt_pb2.StaticSimplePrompt
            content: _static_content_prompt_pb2.StaticContentPrompt
            last_simple: _static_simple_prompt_pb2.StaticSimplePrompt
            suggestions: _containers.RepeatedCompositeFieldContainer[_suggestion_pb2.Suggestion]
            link: _static_link_prompt_pb2.StaticLinkPrompt
            override: bool
            canvas: _static_canvas_prompt_pb2.StaticCanvasPrompt

            def __init__(self, first_simple: _Optional[_Union[_static_simple_prompt_pb2.StaticSimplePrompt, _Mapping]]=..., content: _Optional[_Union[_static_content_prompt_pb2.StaticContentPrompt, _Mapping]]=..., last_simple: _Optional[_Union[_static_simple_prompt_pb2.StaticSimplePrompt, _Mapping]]=..., suggestions: _Optional[_Iterable[_Union[_suggestion_pb2.Suggestion, _Mapping]]]=..., link: _Optional[_Union[_static_link_prompt_pb2.StaticLinkPrompt, _Mapping]]=..., override: bool=..., canvas: _Optional[_Union[_static_canvas_prompt_pb2.StaticCanvasPrompt, _Mapping]]=...) -> None:
                ...
        SELECTOR_FIELD_NUMBER: _ClassVar[int]
        PROMPT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        selector: StaticPrompt.Selector
        prompt_response: StaticPrompt.StaticPromptCandidate.StaticPromptResponse

        def __init__(self, selector: _Optional[_Union[StaticPrompt.Selector, _Mapping]]=..., prompt_response: _Optional[_Union[StaticPrompt.StaticPromptCandidate.StaticPromptResponse, _Mapping]]=...) -> None:
            ...

    class Selector(_message.Message):
        __slots__ = ('surface_capabilities',)
        SURFACE_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
        surface_capabilities: _surface_capabilities_pb2.SurfaceCapabilities

        def __init__(self, surface_capabilities: _Optional[_Union[_surface_capabilities_pb2.SurfaceCapabilities, _Mapping]]=...) -> None:
            ...
    CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    candidates: _containers.RepeatedCompositeFieldContainer[StaticPrompt.StaticPromptCandidate]

    def __init__(self, candidates: _Optional[_Iterable[_Union[StaticPrompt.StaticPromptCandidate, _Mapping]]]=...) -> None:
        ...