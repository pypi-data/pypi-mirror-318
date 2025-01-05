from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.chat.v1 import membership_pb2 as _membership_pb2
from google.chat.v1 import space_pb2 as _space_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetUpSpaceRequest(_message.Message):
    __slots__ = ("space", "request_id", "memberships")
    SPACE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIPS_FIELD_NUMBER: _ClassVar[int]
    space: _space_pb2.Space
    request_id: str
    memberships: _containers.RepeatedCompositeFieldContainer[_membership_pb2.Membership]
    def __init__(self, space: _Optional[_Union[_space_pb2.Space, _Mapping]] = ..., request_id: _Optional[str] = ..., memberships: _Optional[_Iterable[_Union[_membership_pb2.Membership, _Mapping]]] = ...) -> None: ...
