from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import dayofweek_pb2 as _dayofweek_pb2
from google.type import timeofday_pb2 as _timeofday_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MemcacheVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEMCACHE_VERSION_UNSPECIFIED: _ClassVar[MemcacheVersion]
    MEMCACHE_1_5: _ClassVar[MemcacheVersion]
MEMCACHE_VERSION_UNSPECIFIED: MemcacheVersion
MEMCACHE_1_5: MemcacheVersion

class Instance(_message.Message):
    __slots__ = ('name', 'display_name', 'labels', 'authorized_network', 'zones', 'node_count', 'node_config', 'memcache_version', 'parameters', 'memcache_nodes', 'create_time', 'update_time', 'state', 'memcache_full_version', 'instance_messages', 'discovery_endpoint', 'update_available', 'maintenance_policy', 'maintenance_schedule')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Instance.State]
        CREATING: _ClassVar[Instance.State]
        READY: _ClassVar[Instance.State]
        UPDATING: _ClassVar[Instance.State]
        DELETING: _ClassVar[Instance.State]
        PERFORMING_MAINTENANCE: _ClassVar[Instance.State]
    STATE_UNSPECIFIED: Instance.State
    CREATING: Instance.State
    READY: Instance.State
    UPDATING: Instance.State
    DELETING: Instance.State
    PERFORMING_MAINTENANCE: Instance.State

    class NodeConfig(_message.Message):
        __slots__ = ('cpu_count', 'memory_size_mb')
        CPU_COUNT_FIELD_NUMBER: _ClassVar[int]
        MEMORY_SIZE_MB_FIELD_NUMBER: _ClassVar[int]
        cpu_count: int
        memory_size_mb: int

        def __init__(self, cpu_count: _Optional[int]=..., memory_size_mb: _Optional[int]=...) -> None:
            ...

    class Node(_message.Message):
        __slots__ = ('node_id', 'zone', 'state', 'host', 'port', 'parameters', 'update_available')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[Instance.Node.State]
            CREATING: _ClassVar[Instance.Node.State]
            READY: _ClassVar[Instance.Node.State]
            DELETING: _ClassVar[Instance.Node.State]
            UPDATING: _ClassVar[Instance.Node.State]
        STATE_UNSPECIFIED: Instance.Node.State
        CREATING: Instance.Node.State
        READY: Instance.Node.State
        DELETING: Instance.Node.State
        UPDATING: Instance.Node.State
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        ZONE_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        HOST_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        UPDATE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        node_id: str
        zone: str
        state: Instance.Node.State
        host: str
        port: int
        parameters: MemcacheParameters
        update_available: bool

        def __init__(self, node_id: _Optional[str]=..., zone: _Optional[str]=..., state: _Optional[_Union[Instance.Node.State, str]]=..., host: _Optional[str]=..., port: _Optional[int]=..., parameters: _Optional[_Union[MemcacheParameters, _Mapping]]=..., update_available: bool=...) -> None:
            ...

    class InstanceMessage(_message.Message):
        __slots__ = ('code', 'message')

        class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CODE_UNSPECIFIED: _ClassVar[Instance.InstanceMessage.Code]
            ZONE_DISTRIBUTION_UNBALANCED: _ClassVar[Instance.InstanceMessage.Code]
        CODE_UNSPECIFIED: Instance.InstanceMessage.Code
        ZONE_DISTRIBUTION_UNBALANCED: Instance.InstanceMessage.Code
        CODE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        code: Instance.InstanceMessage.Code
        message: str

        def __init__(self, code: _Optional[_Union[Instance.InstanceMessage.Code, str]]=..., message: _Optional[str]=...) -> None:
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
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_NETWORK_FIELD_NUMBER: _ClassVar[int]
    ZONES_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    NODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MEMCACHE_VERSION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    MEMCACHE_NODES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    MEMCACHE_FULL_VERSION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_POLICY_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    labels: _containers.ScalarMap[str, str]
    authorized_network: str
    zones: _containers.RepeatedScalarFieldContainer[str]
    node_count: int
    node_config: Instance.NodeConfig
    memcache_version: MemcacheVersion
    parameters: MemcacheParameters
    memcache_nodes: _containers.RepeatedCompositeFieldContainer[Instance.Node]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    state: Instance.State
    memcache_full_version: str
    instance_messages: _containers.RepeatedCompositeFieldContainer[Instance.InstanceMessage]
    discovery_endpoint: str
    update_available: bool
    maintenance_policy: MaintenancePolicy
    maintenance_schedule: MaintenanceSchedule

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., authorized_network: _Optional[str]=..., zones: _Optional[_Iterable[str]]=..., node_count: _Optional[int]=..., node_config: _Optional[_Union[Instance.NodeConfig, _Mapping]]=..., memcache_version: _Optional[_Union[MemcacheVersion, str]]=..., parameters: _Optional[_Union[MemcacheParameters, _Mapping]]=..., memcache_nodes: _Optional[_Iterable[_Union[Instance.Node, _Mapping]]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[Instance.State, str]]=..., memcache_full_version: _Optional[str]=..., instance_messages: _Optional[_Iterable[_Union[Instance.InstanceMessage, _Mapping]]]=..., discovery_endpoint: _Optional[str]=..., update_available: bool=..., maintenance_policy: _Optional[_Union[MaintenancePolicy, _Mapping]]=..., maintenance_schedule: _Optional[_Union[MaintenanceSchedule, _Mapping]]=...) -> None:
        ...

class MaintenancePolicy(_message.Message):
    __slots__ = ('create_time', 'update_time', 'description', 'weekly_maintenance_window')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_MAINTENANCE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    weekly_maintenance_window: _containers.RepeatedCompositeFieldContainer[WeeklyMaintenanceWindow]

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., weekly_maintenance_window: _Optional[_Iterable[_Union[WeeklyMaintenanceWindow, _Mapping]]]=...) -> None:
        ...

class WeeklyMaintenanceWindow(_message.Message):
    __slots__ = ('day', 'start_time', 'duration')
    DAY_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    day: _dayofweek_pb2.DayOfWeek
    start_time: _timeofday_pb2.TimeOfDay
    duration: _duration_pb2.Duration

    def __init__(self, day: _Optional[_Union[_dayofweek_pb2.DayOfWeek, str]]=..., start_time: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class MaintenanceSchedule(_message.Message):
    __slots__ = ('start_time', 'end_time', 'schedule_deadline_time')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_DEADLINE_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    schedule_deadline_time: _timestamp_pb2.Timestamp

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., schedule_deadline_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListInstancesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
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

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListInstancesResponse(_message.Message):
    __slots__ = ('resources', 'next_page_token', 'unreachable')
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    resources: _containers.RepeatedCompositeFieldContainer[Instance]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, resources: _Optional[_Iterable[_Union[Instance, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateInstanceRequest(_message.Message):
    __slots__ = ('parent', 'instance_id', 'resource')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    instance_id: str
    resource: Instance

    def __init__(self, parent: _Optional[str]=..., instance_id: _Optional[str]=..., resource: _Optional[_Union[Instance, _Mapping]]=...) -> None:
        ...

class UpdateInstanceRequest(_message.Message):
    __slots__ = ('update_mask', 'resource')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    resource: Instance

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., resource: _Optional[_Union[Instance, _Mapping]]=...) -> None:
        ...

class DeleteInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RescheduleMaintenanceRequest(_message.Message):
    __slots__ = ('instance', 'reschedule_type', 'schedule_time')

    class RescheduleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESCHEDULE_TYPE_UNSPECIFIED: _ClassVar[RescheduleMaintenanceRequest.RescheduleType]
        IMMEDIATE: _ClassVar[RescheduleMaintenanceRequest.RescheduleType]
        NEXT_AVAILABLE_WINDOW: _ClassVar[RescheduleMaintenanceRequest.RescheduleType]
        SPECIFIC_TIME: _ClassVar[RescheduleMaintenanceRequest.RescheduleType]
    RESCHEDULE_TYPE_UNSPECIFIED: RescheduleMaintenanceRequest.RescheduleType
    IMMEDIATE: RescheduleMaintenanceRequest.RescheduleType
    NEXT_AVAILABLE_WINDOW: RescheduleMaintenanceRequest.RescheduleType
    SPECIFIC_TIME: RescheduleMaintenanceRequest.RescheduleType
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    RESCHEDULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TIME_FIELD_NUMBER: _ClassVar[int]
    instance: str
    reschedule_type: RescheduleMaintenanceRequest.RescheduleType
    schedule_time: _timestamp_pb2.Timestamp

    def __init__(self, instance: _Optional[str]=..., reschedule_type: _Optional[_Union[RescheduleMaintenanceRequest.RescheduleType, str]]=..., schedule_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ApplyParametersRequest(_message.Message):
    __slots__ = ('name', 'node_ids', 'apply_all')
    NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    APPLY_ALL_FIELD_NUMBER: _ClassVar[int]
    name: str
    node_ids: _containers.RepeatedScalarFieldContainer[str]
    apply_all: bool

    def __init__(self, name: _Optional[str]=..., node_ids: _Optional[_Iterable[str]]=..., apply_all: bool=...) -> None:
        ...

class UpdateParametersRequest(_message.Message):
    __slots__ = ('name', 'update_mask', 'parameters')
    NAME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    update_mask: _field_mask_pb2.FieldMask
    parameters: MemcacheParameters

    def __init__(self, name: _Optional[str]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., parameters: _Optional[_Union[MemcacheParameters, _Mapping]]=...) -> None:
        ...

class ApplySoftwareUpdateRequest(_message.Message):
    __slots__ = ('instance', 'node_ids', 'apply_all')
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    APPLY_ALL_FIELD_NUMBER: _ClassVar[int]
    instance: str
    node_ids: _containers.RepeatedScalarFieldContainer[str]
    apply_all: bool

    def __init__(self, instance: _Optional[str]=..., node_ids: _Optional[_Iterable[str]]=..., apply_all: bool=...) -> None:
        ...

class MemcacheParameters(_message.Message):
    __slots__ = ('id', 'params')

    class ParamsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    id: str
    params: _containers.ScalarMap[str, str]

    def __init__(self, id: _Optional[str]=..., params: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_detail', 'cancel_requested', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_DETAIL_FIELD_NUMBER: _ClassVar[int]
    CANCEL_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_detail: str
    cancel_requested: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_detail: _Optional[str]=..., cancel_requested: bool=..., api_version: _Optional[str]=...) -> None:
        ...

class LocationMetadata(_message.Message):
    __slots__ = ('available_zones',)

    class AvailableZonesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ZoneMetadata

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ZoneMetadata, _Mapping]]=...) -> None:
            ...
    AVAILABLE_ZONES_FIELD_NUMBER: _ClassVar[int]
    available_zones: _containers.MessageMap[str, ZoneMetadata]

    def __init__(self, available_zones: _Optional[_Mapping[str, ZoneMetadata]]=...) -> None:
        ...

class ZoneMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...