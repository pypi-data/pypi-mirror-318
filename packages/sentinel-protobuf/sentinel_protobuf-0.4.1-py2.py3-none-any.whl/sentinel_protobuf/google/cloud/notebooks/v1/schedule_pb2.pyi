from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.notebooks.v1 import execution_pb2 as _execution_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Schedule(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'state', 'cron_schedule', 'time_zone', 'create_time', 'update_time', 'execution_template', 'recent_executions')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Schedule.State]
        ENABLED: _ClassVar[Schedule.State]
        PAUSED: _ClassVar[Schedule.State]
        DISABLED: _ClassVar[Schedule.State]
        UPDATE_FAILED: _ClassVar[Schedule.State]
        INITIALIZING: _ClassVar[Schedule.State]
        DELETING: _ClassVar[Schedule.State]
    STATE_UNSPECIFIED: Schedule.State
    ENABLED: Schedule.State
    PAUSED: Schedule.State
    DISABLED: Schedule.State
    UPDATE_FAILED: Schedule.State
    INITIALIZING: Schedule.State
    DELETING: Schedule.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CRON_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    RECENT_EXECUTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    state: Schedule.State
    cron_schedule: str
    time_zone: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    execution_template: _execution_pb2.ExecutionTemplate
    recent_executions: _containers.RepeatedCompositeFieldContainer[_execution_pb2.Execution]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., state: _Optional[_Union[Schedule.State, str]]=..., cron_schedule: _Optional[str]=..., time_zone: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., execution_template: _Optional[_Union[_execution_pb2.ExecutionTemplate, _Mapping]]=..., recent_executions: _Optional[_Iterable[_Union[_execution_pb2.Execution, _Mapping]]]=...) -> None:
        ...