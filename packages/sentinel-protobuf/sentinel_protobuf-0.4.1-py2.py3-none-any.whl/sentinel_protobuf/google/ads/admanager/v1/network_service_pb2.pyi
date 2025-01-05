from google.ads.admanager.v1 import network_messages_pb2 as _network_messages_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetNetworkRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListNetworksRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListNetworksResponse(_message.Message):
    __slots__ = ('networks',)
    NETWORKS_FIELD_NUMBER: _ClassVar[int]
    networks: _containers.RepeatedCompositeFieldContainer[_network_messages_pb2.Network]

    def __init__(self, networks: _Optional[_Iterable[_Union[_network_messages_pb2.Network, _Mapping]]]=...) -> None:
        ...