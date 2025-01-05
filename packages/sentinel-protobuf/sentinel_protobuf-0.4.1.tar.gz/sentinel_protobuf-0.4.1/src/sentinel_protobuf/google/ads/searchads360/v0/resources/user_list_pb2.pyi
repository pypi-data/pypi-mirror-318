from google.ads.searchads360.v0.enums import user_list_type_pb2 as _user_list_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserList(_message.Message):
    __slots__ = ("resource_name", "id", "name", "type")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    type: _user_list_type_pb2.UserListTypeEnum.UserListType
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., type: _Optional[_Union[_user_list_type_pb2.UserListTypeEnum.UserListType, str]] = ...) -> None: ...
