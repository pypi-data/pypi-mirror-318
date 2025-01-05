from google.actions.sdk.v2.conversation import intent_pb2 as _intent_pb2
from google.actions.sdk.v2.conversation.prompt.content import canvas_pb2 as _canvas_pb2
from google.actions.sdk.v2.conversation.prompt import prompt_pb2 as _prompt_pb2
from google.actions.sdk.v2 import event_logs_pb2 as _event_logs_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SendInteractionRequest(_message.Message):
    __slots__ = ('project', 'input', 'device_properties', 'conversation_token')
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project: str
    input: UserInput
    device_properties: DeviceProperties
    conversation_token: str

    def __init__(self, project: _Optional[str]=..., input: _Optional[_Union[UserInput, _Mapping]]=..., device_properties: _Optional[_Union[DeviceProperties, _Mapping]]=..., conversation_token: _Optional[str]=...) -> None:
        ...

class UserInput(_message.Message):
    __slots__ = ('query', 'type')

    class InputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INPUT_TYPE_UNSPECIFIED: _ClassVar[UserInput.InputType]
        TOUCH: _ClassVar[UserInput.InputType]
        VOICE: _ClassVar[UserInput.InputType]
        KEYBOARD: _ClassVar[UserInput.InputType]
        URL: _ClassVar[UserInput.InputType]
    INPUT_TYPE_UNSPECIFIED: UserInput.InputType
    TOUCH: UserInput.InputType
    VOICE: UserInput.InputType
    KEYBOARD: UserInput.InputType
    URL: UserInput.InputType
    QUERY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    query: str
    type: UserInput.InputType

    def __init__(self, query: _Optional[str]=..., type: _Optional[_Union[UserInput.InputType, str]]=...) -> None:
        ...

class DeviceProperties(_message.Message):
    __slots__ = ('surface', 'location', 'locale', 'time_zone')

    class Surface(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SURFACE_UNSPECIFIED: _ClassVar[DeviceProperties.Surface]
        SPEAKER: _ClassVar[DeviceProperties.Surface]
        PHONE: _ClassVar[DeviceProperties.Surface]
        ALLO: _ClassVar[DeviceProperties.Surface]
        SMART_DISPLAY: _ClassVar[DeviceProperties.Surface]
        KAI_OS: _ClassVar[DeviceProperties.Surface]
    SURFACE_UNSPECIFIED: DeviceProperties.Surface
    SPEAKER: DeviceProperties.Surface
    PHONE: DeviceProperties.Surface
    ALLO: DeviceProperties.Surface
    SMART_DISPLAY: DeviceProperties.Surface
    KAI_OS: DeviceProperties.Surface
    SURFACE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    surface: DeviceProperties.Surface
    location: Location
    locale: str
    time_zone: str

    def __init__(self, surface: _Optional[_Union[DeviceProperties.Surface, str]]=..., location: _Optional[_Union[Location, _Mapping]]=..., locale: _Optional[str]=..., time_zone: _Optional[str]=...) -> None:
        ...

class Location(_message.Message):
    __slots__ = ('coordinates', 'formatted_address', 'zip_code', 'city')
    COORDINATES_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ZIP_CODE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    coordinates: _latlng_pb2.LatLng
    formatted_address: str
    zip_code: str
    city: str

    def __init__(self, coordinates: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., formatted_address: _Optional[str]=..., zip_code: _Optional[str]=..., city: _Optional[str]=...) -> None:
        ...

class SendInteractionResponse(_message.Message):
    __slots__ = ('output', 'diagnostics', 'conversation_token')
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    output: Output
    diagnostics: Diagnostics
    conversation_token: str

    def __init__(self, output: _Optional[_Union[Output, _Mapping]]=..., diagnostics: _Optional[_Union[Diagnostics, _Mapping]]=..., conversation_token: _Optional[str]=...) -> None:
        ...

class Output(_message.Message):
    __slots__ = ('text', 'speech', 'canvas', 'actions_builder_prompt')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SPEECH_FIELD_NUMBER: _ClassVar[int]
    CANVAS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_BUILDER_PROMPT_FIELD_NUMBER: _ClassVar[int]
    text: str
    speech: _containers.RepeatedScalarFieldContainer[str]
    canvas: _canvas_pb2.Canvas
    actions_builder_prompt: _prompt_pb2.Prompt

    def __init__(self, text: _Optional[str]=..., speech: _Optional[_Iterable[str]]=..., canvas: _Optional[_Union[_canvas_pb2.Canvas, _Mapping]]=..., actions_builder_prompt: _Optional[_Union[_prompt_pb2.Prompt, _Mapping]]=...) -> None:
        ...

class Diagnostics(_message.Message):
    __slots__ = ('actions_builder_events',)
    ACTIONS_BUILDER_EVENTS_FIELD_NUMBER: _ClassVar[int]
    actions_builder_events: _containers.RepeatedCompositeFieldContainer[_event_logs_pb2.ExecutionEvent]

    def __init__(self, actions_builder_events: _Optional[_Iterable[_Union[_event_logs_pb2.ExecutionEvent, _Mapping]]]=...) -> None:
        ...

class MatchIntentsRequest(_message.Message):
    __slots__ = ('project', 'query', 'locale')
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    project: str
    query: str
    locale: str

    def __init__(self, project: _Optional[str]=..., query: _Optional[str]=..., locale: _Optional[str]=...) -> None:
        ...

class MatchIntentsResponse(_message.Message):
    __slots__ = ('matched_intents',)
    MATCHED_INTENTS_FIELD_NUMBER: _ClassVar[int]
    matched_intents: _containers.RepeatedCompositeFieldContainer[_intent_pb2.Intent]

    def __init__(self, matched_intents: _Optional[_Iterable[_Union[_intent_pb2.Intent, _Mapping]]]=...) -> None:
        ...

class SetWebAndAppActivityControlRequest(_message.Message):
    __slots__ = ('enabled',)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool

    def __init__(self, enabled: bool=...) -> None:
        ...