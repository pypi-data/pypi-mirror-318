from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UserLocationView(_message.Message):
    __slots__ = ("resource_name", "country_criterion_id", "targeting_location")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CRITERION_ID_FIELD_NUMBER: _ClassVar[int]
    TARGETING_LOCATION_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    country_criterion_id: int
    targeting_location: bool
    def __init__(self, resource_name: _Optional[str] = ..., country_criterion_id: _Optional[int] = ..., targeting_location: bool = ...) -> None: ...
