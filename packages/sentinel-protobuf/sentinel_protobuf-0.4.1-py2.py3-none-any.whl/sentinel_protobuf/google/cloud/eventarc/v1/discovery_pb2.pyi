from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Provider(_message.Message):
    __slots__ = ('name', 'display_name', 'event_types')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    event_types: _containers.RepeatedCompositeFieldContainer[EventType]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., event_types: _Optional[_Iterable[_Union[EventType, _Mapping]]]=...) -> None:
        ...

class EventType(_message.Message):
    __slots__ = ('type', 'description', 'filtering_attributes', 'event_schema_uri')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FILTERING_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    EVENT_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    type: str
    description: str
    filtering_attributes: _containers.RepeatedCompositeFieldContainer[FilteringAttribute]
    event_schema_uri: str

    def __init__(self, type: _Optional[str]=..., description: _Optional[str]=..., filtering_attributes: _Optional[_Iterable[_Union[FilteringAttribute, _Mapping]]]=..., event_schema_uri: _Optional[str]=...) -> None:
        ...

class FilteringAttribute(_message.Message):
    __slots__ = ('attribute', 'description', 'required', 'path_pattern_supported')
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    PATH_PATTERN_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    attribute: str
    description: str
    required: bool
    path_pattern_supported: bool

    def __init__(self, attribute: _Optional[str]=..., description: _Optional[str]=..., required: bool=..., path_pattern_supported: bool=...) -> None:
        ...