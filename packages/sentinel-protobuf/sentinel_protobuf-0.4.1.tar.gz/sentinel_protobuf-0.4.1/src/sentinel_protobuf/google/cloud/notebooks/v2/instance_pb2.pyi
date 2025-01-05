from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.notebooks.v2 import gce_setup_pb2 as _gce_setup_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATE_UNSPECIFIED: _ClassVar[State]
    STARTING: _ClassVar[State]
    PROVISIONING: _ClassVar[State]
    ACTIVE: _ClassVar[State]
    STOPPING: _ClassVar[State]
    STOPPED: _ClassVar[State]
    DELETED: _ClassVar[State]
    UPGRADING: _ClassVar[State]
    INITIALIZING: _ClassVar[State]
    SUSPENDING: _ClassVar[State]
    SUSPENDED: _ClassVar[State]

class HealthState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HEALTH_STATE_UNSPECIFIED: _ClassVar[HealthState]
    HEALTHY: _ClassVar[HealthState]
    UNHEALTHY: _ClassVar[HealthState]
    AGENT_NOT_INSTALLED: _ClassVar[HealthState]
    AGENT_NOT_RUNNING: _ClassVar[HealthState]
STATE_UNSPECIFIED: State
STARTING: State
PROVISIONING: State
ACTIVE: State
STOPPING: State
STOPPED: State
DELETED: State
UPGRADING: State
INITIALIZING: State
SUSPENDING: State
SUSPENDED: State
HEALTH_STATE_UNSPECIFIED: HealthState
HEALTHY: HealthState
UNHEALTHY: HealthState
AGENT_NOT_INSTALLED: HealthState
AGENT_NOT_RUNNING: HealthState

class UpgradeHistoryEntry(_message.Message):
    __slots__ = ('snapshot', 'vm_image', 'container_image', 'framework', 'version', 'state', 'create_time', 'action', 'target_version')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[UpgradeHistoryEntry.State]
        STARTED: _ClassVar[UpgradeHistoryEntry.State]
        SUCCEEDED: _ClassVar[UpgradeHistoryEntry.State]
        FAILED: _ClassVar[UpgradeHistoryEntry.State]
    STATE_UNSPECIFIED: UpgradeHistoryEntry.State
    STARTED: UpgradeHistoryEntry.State
    SUCCEEDED: UpgradeHistoryEntry.State
    FAILED: UpgradeHistoryEntry.State

    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_UNSPECIFIED: _ClassVar[UpgradeHistoryEntry.Action]
        UPGRADE: _ClassVar[UpgradeHistoryEntry.Action]
        ROLLBACK: _ClassVar[UpgradeHistoryEntry.Action]
    ACTION_UNSPECIFIED: UpgradeHistoryEntry.Action
    UPGRADE: UpgradeHistoryEntry.Action
    ROLLBACK: UpgradeHistoryEntry.Action
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    VM_IMAGE_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_IMAGE_FIELD_NUMBER: _ClassVar[int]
    FRAMEWORK_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    TARGET_VERSION_FIELD_NUMBER: _ClassVar[int]
    snapshot: str
    vm_image: str
    container_image: str
    framework: str
    version: str
    state: UpgradeHistoryEntry.State
    create_time: _timestamp_pb2.Timestamp
    action: UpgradeHistoryEntry.Action
    target_version: str

    def __init__(self, snapshot: _Optional[str]=..., vm_image: _Optional[str]=..., container_image: _Optional[str]=..., framework: _Optional[str]=..., version: _Optional[str]=..., state: _Optional[_Union[UpgradeHistoryEntry.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., action: _Optional[_Union[UpgradeHistoryEntry.Action, str]]=..., target_version: _Optional[str]=...) -> None:
        ...

class Instance(_message.Message):
    __slots__ = ('name', 'gce_setup', 'proxy_uri', 'instance_owners', 'creator', 'state', 'upgrade_history', 'id', 'health_state', 'health_info', 'create_time', 'update_time', 'disable_proxy_access', 'labels')

    class HealthInfoEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    GCE_SETUP_FIELD_NUMBER: _ClassVar[int]
    PROXY_URI_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_OWNERS_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_HISTORY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    HEALTH_STATE_FIELD_NUMBER: _ClassVar[int]
    HEALTH_INFO_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISABLE_PROXY_ACCESS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    gce_setup: _gce_setup_pb2.GceSetup
    proxy_uri: str
    instance_owners: _containers.RepeatedScalarFieldContainer[str]
    creator: str
    state: State
    upgrade_history: _containers.RepeatedCompositeFieldContainer[UpgradeHistoryEntry]
    id: str
    health_state: HealthState
    health_info: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    disable_proxy_access: bool
    labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., gce_setup: _Optional[_Union[_gce_setup_pb2.GceSetup, _Mapping]]=..., proxy_uri: _Optional[str]=..., instance_owners: _Optional[_Iterable[str]]=..., creator: _Optional[str]=..., state: _Optional[_Union[State, str]]=..., upgrade_history: _Optional[_Iterable[_Union[UpgradeHistoryEntry, _Mapping]]]=..., id: _Optional[str]=..., health_state: _Optional[_Union[HealthState, str]]=..., health_info: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., disable_proxy_access: bool=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...