from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupPolicy(_message.Message):
    __slots__ = ("name", "daily_backup_limit", "weekly_backup_limit", "monthly_backup_limit", "description", "enabled", "assigned_volume_count", "create_time", "labels", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[BackupPolicy.State]
        CREATING: _ClassVar[BackupPolicy.State]
        READY: _ClassVar[BackupPolicy.State]
        DELETING: _ClassVar[BackupPolicy.State]
        ERROR: _ClassVar[BackupPolicy.State]
        UPDATING: _ClassVar[BackupPolicy.State]
    STATE_UNSPECIFIED: BackupPolicy.State
    CREATING: BackupPolicy.State
    READY: BackupPolicy.State
    DELETING: BackupPolicy.State
    ERROR: BackupPolicy.State
    UPDATING: BackupPolicy.State
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DAILY_BACKUP_LIMIT_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_BACKUP_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_BACKUP_LIMIT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_VOLUME_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    daily_backup_limit: int
    weekly_backup_limit: int
    monthly_backup_limit: int
    description: str
    enabled: bool
    assigned_volume_count: int
    create_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    state: BackupPolicy.State
    def __init__(self, name: _Optional[str] = ..., daily_backup_limit: _Optional[int] = ..., weekly_backup_limit: _Optional[int] = ..., monthly_backup_limit: _Optional[int] = ..., description: _Optional[str] = ..., enabled: bool = ..., assigned_volume_count: _Optional[int] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., state: _Optional[_Union[BackupPolicy.State, str]] = ...) -> None: ...

class CreateBackupPolicyRequest(_message.Message):
    __slots__ = ("parent", "backup_policy", "backup_policy_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_POLICY_FIELD_NUMBER: _ClassVar[int]
    BACKUP_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    backup_policy: BackupPolicy
    backup_policy_id: str
    def __init__(self, parent: _Optional[str] = ..., backup_policy: _Optional[_Union[BackupPolicy, _Mapping]] = ..., backup_policy_id: _Optional[str] = ...) -> None: ...

class GetBackupPolicyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListBackupPoliciesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListBackupPoliciesResponse(_message.Message):
    __slots__ = ("backup_policies", "next_page_token", "unreachable")
    BACKUP_POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    backup_policies: _containers.RepeatedCompositeFieldContainer[BackupPolicy]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, backup_policies: _Optional[_Iterable[_Union[BackupPolicy, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateBackupPolicyRequest(_message.Message):
    __slots__ = ("update_mask", "backup_policy")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    BACKUP_POLICY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    backup_policy: BackupPolicy
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., backup_policy: _Optional[_Union[BackupPolicy, _Mapping]] = ...) -> None: ...

class DeleteBackupPolicyRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
