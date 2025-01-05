from google.maps.routes.v1 import fallback_info_pb2 as _fallback_info_pb2
from google.maps.routes.v1 import route_pb2 as _route_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ComputeRoutesResponse(_message.Message):
    __slots__ = ('routes', 'fallback_info')
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_INFO_FIELD_NUMBER: _ClassVar[int]
    routes: _containers.RepeatedCompositeFieldContainer[_route_pb2.Route]
    fallback_info: _fallback_info_pb2.FallbackInfo

    def __init__(self, routes: _Optional[_Iterable[_Union[_route_pb2.Route, _Mapping]]]=..., fallback_info: _Optional[_Union[_fallback_info_pb2.FallbackInfo, _Mapping]]=...) -> None:
        ...