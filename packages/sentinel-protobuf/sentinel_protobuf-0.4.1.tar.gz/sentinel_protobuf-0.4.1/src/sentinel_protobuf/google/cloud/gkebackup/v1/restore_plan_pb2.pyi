from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.gkebackup.v1 import restore_pb2 as _restore_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RestorePlan(_message.Message):
    __slots__ = ('name', 'uid', 'create_time', 'update_time', 'description', 'backup_plan', 'cluster', 'restore_config', 'labels', 'etag', 'state', 'state_reason')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[RestorePlan.State]
        CLUSTER_PENDING: _ClassVar[RestorePlan.State]
        READY: _ClassVar[RestorePlan.State]
        FAILED: _ClassVar[RestorePlan.State]
        DELETING: _ClassVar[RestorePlan.State]
    STATE_UNSPECIFIED: RestorePlan.State
    CLUSTER_PENDING: RestorePlan.State
    READY: RestorePlan.State
    FAILED: RestorePlan.State
    DELETING: RestorePlan.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    RESTORE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_REASON_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    backup_plan: str
    cluster: str
    restore_config: _restore_pb2.RestoreConfig
    labels: _containers.ScalarMap[str, str]
    etag: str
    state: RestorePlan.State
    state_reason: str

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., backup_plan: _Optional[str]=..., cluster: _Optional[str]=..., restore_config: _Optional[_Union[_restore_pb2.RestoreConfig, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=..., state: _Optional[_Union[RestorePlan.State, str]]=..., state_reason: _Optional[str]=...) -> None:
        ...