from google.ads.admanager.v1 import role_enums_pb2 as _role_enums_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Role(_message.Message):
    __slots__ = ('name', 'role_id', 'display_name', 'description', 'built_in', 'status')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BUILT_IN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    role_id: int
    display_name: str
    description: str
    built_in: bool
    status: _role_enums_pb2.RoleStatusEnum.RoleStatus

    def __init__(self, name: _Optional[str]=..., role_id: _Optional[int]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., built_in: bool=..., status: _Optional[_Union[_role_enums_pb2.RoleStatusEnum.RoleStatus, str]]=...) -> None:
        ...