from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AdParameter(_message.Message):
    __slots__ = ("resource_name", "ad_group_criterion", "parameter_index", "insertion_text")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_CRITERION_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_INDEX_FIELD_NUMBER: _ClassVar[int]
    INSERTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    ad_group_criterion: str
    parameter_index: int
    insertion_text: str
    def __init__(self, resource_name: _Optional[str] = ..., ad_group_criterion: _Optional[str] = ..., parameter_index: _Optional[int] = ..., insertion_text: _Optional[str] = ...) -> None: ...
