from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AssignmentProtocol(_message.Message):
    __slots__ = ('manual_assignment_type', 'auto_assignment_type')

    class ManualAssignmentType(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class AutoAssignmentType(_message.Message):
        __slots__ = ('inactive_license_ttl',)
        INACTIVE_LICENSE_TTL_FIELD_NUMBER: _ClassVar[int]
        inactive_license_ttl: _duration_pb2.Duration

        def __init__(self, inactive_license_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...
    MANUAL_ASSIGNMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUTO_ASSIGNMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    manual_assignment_type: AssignmentProtocol.ManualAssignmentType
    auto_assignment_type: AssignmentProtocol.AutoAssignmentType

    def __init__(self, manual_assignment_type: _Optional[_Union[AssignmentProtocol.ManualAssignmentType, _Mapping]]=..., auto_assignment_type: _Optional[_Union[AssignmentProtocol.AutoAssignmentType, _Mapping]]=...) -> None:
        ...

class LicensePool(_message.Message):
    __slots__ = ('name', 'license_assignment_protocol', 'available_license_count', 'total_license_count')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LICENSE_ASSIGNMENT_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_LICENSE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LICENSE_COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    license_assignment_protocol: AssignmentProtocol
    available_license_count: int
    total_license_count: int

    def __init__(self, name: _Optional[str]=..., license_assignment_protocol: _Optional[_Union[AssignmentProtocol, _Mapping]]=..., available_license_count: _Optional[int]=..., total_license_count: _Optional[int]=...) -> None:
        ...

class GetLicensePoolRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateLicensePoolRequest(_message.Message):
    __slots__ = ('license_pool', 'update_mask')
    LICENSE_POOL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    license_pool: LicensePool
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, license_pool: _Optional[_Union[LicensePool, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class AssignRequest(_message.Message):
    __slots__ = ('parent', 'usernames')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    USERNAMES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    usernames: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, parent: _Optional[str]=..., usernames: _Optional[_Iterable[str]]=...) -> None:
        ...

class AssignResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class UnassignRequest(_message.Message):
    __slots__ = ('parent', 'usernames')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    USERNAMES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    usernames: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, parent: _Optional[str]=..., usernames: _Optional[_Iterable[str]]=...) -> None:
        ...

class UnassignResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class EnumerateLicensedUsersRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class LicensedUser(_message.Message):
    __slots__ = ('username', 'assign_time', 'recent_usage_time')
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_TIME_FIELD_NUMBER: _ClassVar[int]
    RECENT_USAGE_TIME_FIELD_NUMBER: _ClassVar[int]
    username: str
    assign_time: _timestamp_pb2.Timestamp
    recent_usage_time: _timestamp_pb2.Timestamp

    def __init__(self, username: _Optional[str]=..., assign_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., recent_usage_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class EnumerateLicensedUsersResponse(_message.Message):
    __slots__ = ('licensed_users', 'next_page_token')
    LICENSED_USERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    licensed_users: _containers.RepeatedCompositeFieldContainer[LicensedUser]
    next_page_token: str

    def __init__(self, licensed_users: _Optional[_Iterable[_Union[LicensedUser, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...