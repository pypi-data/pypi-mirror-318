from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BackupDisasterRecovery(_message.Message):
    __slots__ = ('backup_template', 'policies', 'host', 'applications', 'storage_pool', 'policy_options', 'profile', 'appliance', 'backup_type', 'backup_create_time')
    BACKUP_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POOL_FIELD_NUMBER: _ClassVar[int]
    POLICY_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    APPLIANCE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    backup_template: str
    policies: _containers.RepeatedScalarFieldContainer[str]
    host: str
    applications: _containers.RepeatedScalarFieldContainer[str]
    storage_pool: str
    policy_options: _containers.RepeatedScalarFieldContainer[str]
    profile: str
    appliance: str
    backup_type: str
    backup_create_time: _timestamp_pb2.Timestamp

    def __init__(self, backup_template: _Optional[str]=..., policies: _Optional[_Iterable[str]]=..., host: _Optional[str]=..., applications: _Optional[_Iterable[str]]=..., storage_pool: _Optional[str]=..., policy_options: _Optional[_Iterable[str]]=..., profile: _Optional[str]=..., appliance: _Optional[str]=..., backup_type: _Optional[str]=..., backup_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...