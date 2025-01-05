from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Program(_message.Message):
    __slots__ = ('name', 'documentation_uri', 'state', 'active_region_codes', 'unmet_requirements')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Program.State]
        NOT_ELIGIBLE: _ClassVar[Program.State]
        ELIGIBLE: _ClassVar[Program.State]
        ENABLED: _ClassVar[Program.State]
    STATE_UNSPECIFIED: Program.State
    NOT_ELIGIBLE: Program.State
    ELIGIBLE: Program.State
    ENABLED: Program.State

    class Requirement(_message.Message):
        __slots__ = ('title', 'documentation_uri', 'affected_region_codes')
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DOCUMENTATION_URI_FIELD_NUMBER: _ClassVar[int]
        AFFECTED_REGION_CODES_FIELD_NUMBER: _ClassVar[int]
        title: str
        documentation_uri: str
        affected_region_codes: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, title: _Optional[str]=..., documentation_uri: _Optional[str]=..., affected_region_codes: _Optional[_Iterable[str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_URI_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_REGION_CODES_FIELD_NUMBER: _ClassVar[int]
    UNMET_REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    documentation_uri: str
    state: Program.State
    active_region_codes: _containers.RepeatedScalarFieldContainer[str]
    unmet_requirements: _containers.RepeatedCompositeFieldContainer[Program.Requirement]

    def __init__(self, name: _Optional[str]=..., documentation_uri: _Optional[str]=..., state: _Optional[_Union[Program.State, str]]=..., active_region_codes: _Optional[_Iterable[str]]=..., unmet_requirements: _Optional[_Iterable[_Union[Program.Requirement, _Mapping]]]=...) -> None:
        ...

class GetProgramRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListProgramsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListProgramsResponse(_message.Message):
    __slots__ = ('programs', 'next_page_token')
    PROGRAMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    programs: _containers.RepeatedCompositeFieldContainer[Program]
    next_page_token: str

    def __init__(self, programs: _Optional[_Iterable[_Union[Program, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class EnableProgramRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DisableProgramRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...