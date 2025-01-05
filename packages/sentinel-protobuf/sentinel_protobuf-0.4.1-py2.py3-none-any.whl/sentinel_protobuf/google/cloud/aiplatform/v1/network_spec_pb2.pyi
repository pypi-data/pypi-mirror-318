from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class NetworkSpec(_message.Message):
    __slots__ = ('enable_internet_access', 'network', 'subnetwork')
    ENABLE_INTERNET_ACCESS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    enable_internet_access: bool
    network: str
    subnetwork: str

    def __init__(self, enable_internet_access: bool=..., network: _Optional[str]=..., subnetwork: _Optional[str]=...) -> None:
        ...