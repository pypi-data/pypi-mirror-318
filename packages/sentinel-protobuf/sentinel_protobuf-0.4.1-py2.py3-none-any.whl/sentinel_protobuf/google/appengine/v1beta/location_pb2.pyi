from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class LocationMetadata(_message.Message):
    __slots__ = ('standard_environment_available', 'flexible_environment_available', 'search_api_available')
    STANDARD_ENVIRONMENT_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    FLEXIBLE_ENVIRONMENT_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_API_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    standard_environment_available: bool
    flexible_environment_available: bool
    search_api_available: bool

    def __init__(self, standard_environment_available: bool=..., flexible_environment_available: bool=..., search_api_available: bool=...) -> None:
        ...