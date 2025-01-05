from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.shopping.merchant.accounts.v1beta import accessright_pb2 as _accessright_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ('name', 'state', 'access_rights')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[User.State]
        PENDING: _ClassVar[User.State]
        VERIFIED: _ClassVar[User.State]
    STATE_UNSPECIFIED: User.State
    PENDING: User.State
    VERIFIED: User.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_RIGHTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: User.State
    access_rights: _containers.RepeatedScalarFieldContainer[_accessright_pb2.AccessRight]

    def __init__(self, name: _Optional[str]=..., state: _Optional[_Union[User.State, str]]=..., access_rights: _Optional[_Iterable[_Union[_accessright_pb2.AccessRight, str]]]=...) -> None:
        ...

class GetUserRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateUserRequest(_message.Message):
    __slots__ = ('parent', 'user_id', 'user')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    user_id: str
    user: User

    def __init__(self, parent: _Optional[str]=..., user_id: _Optional[str]=..., user: _Optional[_Union[User, _Mapping]]=...) -> None:
        ...

class DeleteUserRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateUserRequest(_message.Message):
    __slots__ = ('user', 'update_mask')
    USER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    user: User
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, user: _Optional[_Union[User, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListUsersRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListUsersResponse(_message.Message):
    __slots__ = ('users', 'next_page_token')
    USERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[User]
    next_page_token: str

    def __init__(self, users: _Optional[_Iterable[_Union[User, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...