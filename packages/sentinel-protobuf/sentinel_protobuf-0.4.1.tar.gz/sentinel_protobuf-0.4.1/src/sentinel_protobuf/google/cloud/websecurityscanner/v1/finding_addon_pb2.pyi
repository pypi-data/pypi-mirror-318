from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Form(_message.Message):
    __slots__ = ('action_uri', 'fields')
    ACTION_URI_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    action_uri: str
    fields: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, action_uri: _Optional[str]=..., fields: _Optional[_Iterable[str]]=...) -> None:
        ...

class OutdatedLibrary(_message.Message):
    __slots__ = ('library_name', 'version', 'learn_more_urls')
    LIBRARY_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    LEARN_MORE_URLS_FIELD_NUMBER: _ClassVar[int]
    library_name: str
    version: str
    learn_more_urls: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, library_name: _Optional[str]=..., version: _Optional[str]=..., learn_more_urls: _Optional[_Iterable[str]]=...) -> None:
        ...

class ViolatingResource(_message.Message):
    __slots__ = ('content_type', 'resource_url')
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    content_type: str
    resource_url: str

    def __init__(self, content_type: _Optional[str]=..., resource_url: _Optional[str]=...) -> None:
        ...

class VulnerableParameters(_message.Message):
    __slots__ = ('parameter_names',)
    PARAMETER_NAMES_FIELD_NUMBER: _ClassVar[int]
    parameter_names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, parameter_names: _Optional[_Iterable[str]]=...) -> None:
        ...

class VulnerableHeaders(_message.Message):
    __slots__ = ('headers', 'missing_headers')

    class Header(_message.Message):
        __slots__ = ('name', 'value')
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str

        def __init__(self, name: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    MISSING_HEADERS_FIELD_NUMBER: _ClassVar[int]
    headers: _containers.RepeatedCompositeFieldContainer[VulnerableHeaders.Header]
    missing_headers: _containers.RepeatedCompositeFieldContainer[VulnerableHeaders.Header]

    def __init__(self, headers: _Optional[_Iterable[_Union[VulnerableHeaders.Header, _Mapping]]]=..., missing_headers: _Optional[_Iterable[_Union[VulnerableHeaders.Header, _Mapping]]]=...) -> None:
        ...

class Xss(_message.Message):
    __slots__ = ('stack_traces', 'error_message', 'attack_vector', 'stored_xss_seeding_url')

    class AttackVector(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ATTACK_VECTOR_UNSPECIFIED: _ClassVar[Xss.AttackVector]
        LOCAL_STORAGE: _ClassVar[Xss.AttackVector]
        SESSION_STORAGE: _ClassVar[Xss.AttackVector]
        WINDOW_NAME: _ClassVar[Xss.AttackVector]
        REFERRER: _ClassVar[Xss.AttackVector]
        FORM_INPUT: _ClassVar[Xss.AttackVector]
        COOKIE: _ClassVar[Xss.AttackVector]
        POST_MESSAGE: _ClassVar[Xss.AttackVector]
        GET_PARAMETERS: _ClassVar[Xss.AttackVector]
        URL_FRAGMENT: _ClassVar[Xss.AttackVector]
        HTML_COMMENT: _ClassVar[Xss.AttackVector]
        POST_PARAMETERS: _ClassVar[Xss.AttackVector]
        PROTOCOL: _ClassVar[Xss.AttackVector]
        STORED_XSS: _ClassVar[Xss.AttackVector]
        SAME_ORIGIN: _ClassVar[Xss.AttackVector]
        USER_CONTROLLABLE_URL: _ClassVar[Xss.AttackVector]
    ATTACK_VECTOR_UNSPECIFIED: Xss.AttackVector
    LOCAL_STORAGE: Xss.AttackVector
    SESSION_STORAGE: Xss.AttackVector
    WINDOW_NAME: Xss.AttackVector
    REFERRER: Xss.AttackVector
    FORM_INPUT: Xss.AttackVector
    COOKIE: Xss.AttackVector
    POST_MESSAGE: Xss.AttackVector
    GET_PARAMETERS: Xss.AttackVector
    URL_FRAGMENT: Xss.AttackVector
    HTML_COMMENT: Xss.AttackVector
    POST_PARAMETERS: Xss.AttackVector
    PROTOCOL: Xss.AttackVector
    STORED_XSS: Xss.AttackVector
    SAME_ORIGIN: Xss.AttackVector
    USER_CONTROLLABLE_URL: Xss.AttackVector
    STACK_TRACES_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ATTACK_VECTOR_FIELD_NUMBER: _ClassVar[int]
    STORED_XSS_SEEDING_URL_FIELD_NUMBER: _ClassVar[int]
    stack_traces: _containers.RepeatedScalarFieldContainer[str]
    error_message: str
    attack_vector: Xss.AttackVector
    stored_xss_seeding_url: str

    def __init__(self, stack_traces: _Optional[_Iterable[str]]=..., error_message: _Optional[str]=..., attack_vector: _Optional[_Union[Xss.AttackVector, str]]=..., stored_xss_seeding_url: _Optional[str]=...) -> None:
        ...

class Xxe(_message.Message):
    __slots__ = ('payload_value', 'payload_location')

    class Location(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOCATION_UNSPECIFIED: _ClassVar[Xxe.Location]
        COMPLETE_REQUEST_BODY: _ClassVar[Xxe.Location]
    LOCATION_UNSPECIFIED: Xxe.Location
    COMPLETE_REQUEST_BODY: Xxe.Location
    PAYLOAD_VALUE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_LOCATION_FIELD_NUMBER: _ClassVar[int]
    payload_value: str
    payload_location: Xxe.Location

    def __init__(self, payload_value: _Optional[str]=..., payload_location: _Optional[_Union[Xxe.Location, str]]=...) -> None:
        ...