from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.chat.v1 import group_pb2 as _group_pb2
from google.chat.v1 import user_pb2 as _user_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Membership(_message.Message):
    __slots__ = ('name', 'state', 'role', 'member', 'group_member', 'create_time', 'delete_time')

    class MembershipState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MEMBERSHIP_STATE_UNSPECIFIED: _ClassVar[Membership.MembershipState]
        JOINED: _ClassVar[Membership.MembershipState]
        INVITED: _ClassVar[Membership.MembershipState]
        NOT_A_MEMBER: _ClassVar[Membership.MembershipState]
    MEMBERSHIP_STATE_UNSPECIFIED: Membership.MembershipState
    JOINED: Membership.MembershipState
    INVITED: Membership.MembershipState
    NOT_A_MEMBER: Membership.MembershipState

    class MembershipRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MEMBERSHIP_ROLE_UNSPECIFIED: _ClassVar[Membership.MembershipRole]
        ROLE_MEMBER: _ClassVar[Membership.MembershipRole]
        ROLE_MANAGER: _ClassVar[Membership.MembershipRole]
    MEMBERSHIP_ROLE_UNSPECIFIED: Membership.MembershipRole
    ROLE_MEMBER: Membership.MembershipRole
    ROLE_MANAGER: Membership.MembershipRole
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    GROUP_MEMBER_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: Membership.MembershipState
    role: Membership.MembershipRole
    member: _user_pb2.User
    group_member: _group_pb2.Group
    create_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., state: _Optional[_Union[Membership.MembershipState, str]]=..., role: _Optional[_Union[Membership.MembershipRole, str]]=..., member: _Optional[_Union[_user_pb2.User, _Mapping]]=..., group_member: _Optional[_Union[_group_pb2.Group, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CreateMembershipRequest(_message.Message):
    __slots__ = ('parent', 'membership', 'use_admin_access')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    membership: Membership
    use_admin_access: bool

    def __init__(self, parent: _Optional[str]=..., membership: _Optional[_Union[Membership, _Mapping]]=..., use_admin_access: bool=...) -> None:
        ...

class UpdateMembershipRequest(_message.Message):
    __slots__ = ('membership', 'update_mask', 'use_admin_access')
    MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    membership: Membership
    update_mask: _field_mask_pb2.FieldMask
    use_admin_access: bool

    def __init__(self, membership: _Optional[_Union[Membership, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., use_admin_access: bool=...) -> None:
        ...

class ListMembershipsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'show_groups', 'show_invited', 'use_admin_access')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    SHOW_GROUPS_FIELD_NUMBER: _ClassVar[int]
    SHOW_INVITED_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    show_groups: bool
    show_invited: bool
    use_admin_access: bool

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., show_groups: bool=..., show_invited: bool=..., use_admin_access: bool=...) -> None:
        ...

class ListMembershipsResponse(_message.Message):
    __slots__ = ('memberships', 'next_page_token')
    MEMBERSHIPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    memberships: _containers.RepeatedCompositeFieldContainer[Membership]
    next_page_token: str

    def __init__(self, memberships: _Optional[_Iterable[_Union[Membership, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetMembershipRequest(_message.Message):
    __slots__ = ('name', 'use_admin_access')
    NAME_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    use_admin_access: bool

    def __init__(self, name: _Optional[str]=..., use_admin_access: bool=...) -> None:
        ...

class DeleteMembershipRequest(_message.Message):
    __slots__ = ('name', 'use_admin_access')
    NAME_FIELD_NUMBER: _ClassVar[int]
    USE_ADMIN_ACCESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    use_admin_access: bool

    def __init__(self, name: _Optional[str]=..., use_admin_access: bool=...) -> None:
        ...