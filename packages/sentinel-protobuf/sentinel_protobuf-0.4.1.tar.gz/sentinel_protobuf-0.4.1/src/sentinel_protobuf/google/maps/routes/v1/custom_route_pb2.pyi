from google.maps.routes.v1 import route_pb2 as _route_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomRoute(_message.Message):
    __slots__ = ('route', 'token')
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    route: _route_pb2.Route
    token: str

    def __init__(self, route: _Optional[_Union[_route_pb2.Route, _Mapping]]=..., token: _Optional[str]=...) -> None:
        ...