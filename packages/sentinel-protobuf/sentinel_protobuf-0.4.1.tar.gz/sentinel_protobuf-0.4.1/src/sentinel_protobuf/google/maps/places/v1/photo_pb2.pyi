from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.maps.places.v1 import attribution_pb2 as _attribution_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Photo(_message.Message):
    __slots__ = ('name', 'width_px', 'height_px', 'author_attributions')
    NAME_FIELD_NUMBER: _ClassVar[int]
    WIDTH_PX_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_PX_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ATTRIBUTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    width_px: int
    height_px: int
    author_attributions: _containers.RepeatedCompositeFieldContainer[_attribution_pb2.AuthorAttribution]

    def __init__(self, name: _Optional[str]=..., width_px: _Optional[int]=..., height_px: _Optional[int]=..., author_attributions: _Optional[_Iterable[_Union[_attribution_pb2.AuthorAttribution, _Mapping]]]=...) -> None:
        ...