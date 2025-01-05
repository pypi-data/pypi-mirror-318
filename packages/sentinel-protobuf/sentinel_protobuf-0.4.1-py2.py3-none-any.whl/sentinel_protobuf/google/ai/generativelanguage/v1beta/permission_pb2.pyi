from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Permission(_message.Message):
    __slots__ = ("name", "grantee_type", "email_address", "role")
    class GranteeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GRANTEE_TYPE_UNSPECIFIED: _ClassVar[Permission.GranteeType]
        USER: _ClassVar[Permission.GranteeType]
        GROUP: _ClassVar[Permission.GranteeType]
        EVERYONE: _ClassVar[Permission.GranteeType]
    GRANTEE_TYPE_UNSPECIFIED: Permission.GranteeType
    USER: Permission.GranteeType
    GROUP: Permission.GranteeType
    EVERYONE: Permission.GranteeType
    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROLE_UNSPECIFIED: _ClassVar[Permission.Role]
        OWNER: _ClassVar[Permission.Role]
        WRITER: _ClassVar[Permission.Role]
        READER: _ClassVar[Permission.Role]
    ROLE_UNSPECIFIED: Permission.Role
    OWNER: Permission.Role
    WRITER: Permission.Role
    READER: Permission.Role
    NAME_FIELD_NUMBER: _ClassVar[int]
    GRANTEE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    grantee_type: Permission.GranteeType
    email_address: str
    role: Permission.Role
    def __init__(self, name: _Optional[str] = ..., grantee_type: _Optional[_Union[Permission.GranteeType, str]] = ..., email_address: _Optional[str] = ..., role: _Optional[_Union[Permission.Role, str]] = ...) -> None: ...
