from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BackupPlanAssociation(_message.Message):
    __slots__ = ('name', 'resource_type', 'resource', 'backup_plan', 'create_time', 'update_time', 'state', 'rules_config_info', 'data_source')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[BackupPlanAssociation.State]
        CREATING: _ClassVar[BackupPlanAssociation.State]
        ACTIVE: _ClassVar[BackupPlanAssociation.State]
        DELETING: _ClassVar[BackupPlanAssociation.State]
        INACTIVE: _ClassVar[BackupPlanAssociation.State]
    STATE_UNSPECIFIED: BackupPlanAssociation.State
    CREATING: BackupPlanAssociation.State
    ACTIVE: BackupPlanAssociation.State
    DELETING: BackupPlanAssociation.State
    INACTIVE: BackupPlanAssociation.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RULES_CONFIG_INFO_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    resource_type: str
    resource: str
    backup_plan: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    state: BackupPlanAssociation.State
    rules_config_info: _containers.RepeatedCompositeFieldContainer[RuleConfigInfo]
    data_source: str

    def __init__(self, name: _Optional[str]=..., resource_type: _Optional[str]=..., resource: _Optional[str]=..., backup_plan: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[BackupPlanAssociation.State, str]]=..., rules_config_info: _Optional[_Iterable[_Union[RuleConfigInfo, _Mapping]]]=..., data_source: _Optional[str]=...) -> None:
        ...

class RuleConfigInfo(_message.Message):
    __slots__ = ('rule_id', 'last_backup_state', 'last_backup_error', 'last_successful_backup_consistency_time')

    class LastBackupState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LAST_BACKUP_STATE_UNSPECIFIED: _ClassVar[RuleConfigInfo.LastBackupState]
        FIRST_BACKUP_PENDING: _ClassVar[RuleConfigInfo.LastBackupState]
        PERMISSION_DENIED: _ClassVar[RuleConfigInfo.LastBackupState]
        SUCCEEDED: _ClassVar[RuleConfigInfo.LastBackupState]
        FAILED: _ClassVar[RuleConfigInfo.LastBackupState]
    LAST_BACKUP_STATE_UNSPECIFIED: RuleConfigInfo.LastBackupState
    FIRST_BACKUP_PENDING: RuleConfigInfo.LastBackupState
    PERMISSION_DENIED: RuleConfigInfo.LastBackupState
    SUCCEEDED: RuleConfigInfo.LastBackupState
    FAILED: RuleConfigInfo.LastBackupState
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_BACKUP_STATE_FIELD_NUMBER: _ClassVar[int]
    LAST_BACKUP_ERROR_FIELD_NUMBER: _ClassVar[int]
    LAST_SUCCESSFUL_BACKUP_CONSISTENCY_TIME_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    last_backup_state: RuleConfigInfo.LastBackupState
    last_backup_error: _status_pb2.Status
    last_successful_backup_consistency_time: _timestamp_pb2.Timestamp

    def __init__(self, rule_id: _Optional[str]=..., last_backup_state: _Optional[_Union[RuleConfigInfo.LastBackupState, str]]=..., last_backup_error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., last_successful_backup_consistency_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CreateBackupPlanAssociationRequest(_message.Message):
    __slots__ = ('parent', 'backup_plan_association_id', 'backup_plan_association', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_ASSOCIATION_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_ASSOCIATION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    backup_plan_association_id: str
    backup_plan_association: BackupPlanAssociation
    request_id: str

    def __init__(self, parent: _Optional[str]=..., backup_plan_association_id: _Optional[str]=..., backup_plan_association: _Optional[_Union[BackupPlanAssociation, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListBackupPlanAssociationsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListBackupPlanAssociationsResponse(_message.Message):
    __slots__ = ('backup_plan_associations', 'next_page_token', 'unreachable')
    BACKUP_PLAN_ASSOCIATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    backup_plan_associations: _containers.RepeatedCompositeFieldContainer[BackupPlanAssociation]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, backup_plan_associations: _Optional[_Iterable[_Union[BackupPlanAssociation, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetBackupPlanAssociationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteBackupPlanAssociationRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class TriggerBackupRequest(_message.Message):
    __slots__ = ('name', 'rule_id', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    rule_id: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., rule_id: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...