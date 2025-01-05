from google.api import resource_pb2 as _resource_pb2
from google.maps.places.v1 import review_pb2 as _review_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class References(_message.Message):
    __slots__ = ('reviews', 'places')
    REVIEWS_FIELD_NUMBER: _ClassVar[int]
    PLACES_FIELD_NUMBER: _ClassVar[int]
    reviews: _containers.RepeatedCompositeFieldContainer[_review_pb2.Review]
    places: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, reviews: _Optional[_Iterable[_Union[_review_pb2.Review, _Mapping]]]=..., places: _Optional[_Iterable[str]]=...) -> None:
        ...