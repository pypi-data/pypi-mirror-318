from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

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
    __slots__ = ('stack_traces', 'error_message')
    STACK_TRACES_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    stack_traces: _containers.RepeatedScalarFieldContainer[str]
    error_message: str

    def __init__(self, stack_traces: _Optional[_Iterable[str]]=..., error_message: _Optional[str]=...) -> None:
        ...