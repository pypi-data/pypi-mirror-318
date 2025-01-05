from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GroupMembership(_message.Message):
    __slots__ = ('group_type', 'group_id')

    class GroupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GROUP_TYPE_UNSPECIFIED: _ClassVar[GroupMembership.GroupType]
        GROUP_TYPE_TOXIC_COMBINATION: _ClassVar[GroupMembership.GroupType]
    GROUP_TYPE_UNSPECIFIED: GroupMembership.GroupType
    GROUP_TYPE_TOXIC_COMBINATION: GroupMembership.GroupType
    GROUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_type: GroupMembership.GroupType
    group_id: str

    def __init__(self, group_type: _Optional[_Union[GroupMembership.GroupType, str]]=..., group_id: _Optional[str]=...) -> None:
        ...