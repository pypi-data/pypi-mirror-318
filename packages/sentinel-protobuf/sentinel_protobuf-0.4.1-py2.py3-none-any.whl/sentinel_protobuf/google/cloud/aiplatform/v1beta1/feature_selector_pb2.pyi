from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class IdMatcher(_message.Message):
    __slots__ = ('ids',)
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class FeatureSelector(_message.Message):
    __slots__ = ('id_matcher',)
    ID_MATCHER_FIELD_NUMBER: _ClassVar[int]
    id_matcher: IdMatcher

    def __init__(self, id_matcher: _Optional[_Union[IdMatcher, _Mapping]]=...) -> None:
        ...