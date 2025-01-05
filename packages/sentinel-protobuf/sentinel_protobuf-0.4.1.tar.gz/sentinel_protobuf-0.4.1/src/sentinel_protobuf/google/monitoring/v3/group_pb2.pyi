from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Group(_message.Message):
    __slots__ = ('name', 'display_name', 'parent_name', 'filter', 'is_cluster')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    IS_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    parent_name: str
    filter: str
    is_cluster: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., parent_name: _Optional[str]=..., filter: _Optional[str]=..., is_cluster: bool=...) -> None:
        ...