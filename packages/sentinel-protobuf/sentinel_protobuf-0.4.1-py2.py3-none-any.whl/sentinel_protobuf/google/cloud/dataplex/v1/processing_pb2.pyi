from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Trigger(_message.Message):
    __slots__ = ('on_demand', 'schedule')

    class OnDemand(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class Schedule(_message.Message):
        __slots__ = ('cron',)
        CRON_FIELD_NUMBER: _ClassVar[int]
        cron: str

        def __init__(self, cron: _Optional[str]=...) -> None:
            ...
    ON_DEMAND_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    on_demand: Trigger.OnDemand
    schedule: Trigger.Schedule

    def __init__(self, on_demand: _Optional[_Union[Trigger.OnDemand, _Mapping]]=..., schedule: _Optional[_Union[Trigger.Schedule, _Mapping]]=...) -> None:
        ...

class DataSource(_message.Message):
    __slots__ = ('entity', 'resource')
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    entity: str
    resource: str

    def __init__(self, entity: _Optional[str]=..., resource: _Optional[str]=...) -> None:
        ...

class ScannedData(_message.Message):
    __slots__ = ('incremental_field',)

    class IncrementalField(_message.Message):
        __slots__ = ('field', 'start', 'end')
        FIELD_FIELD_NUMBER: _ClassVar[int]
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        field: str
        start: str
        end: str

        def __init__(self, field: _Optional[str]=..., start: _Optional[str]=..., end: _Optional[str]=...) -> None:
            ...
    INCREMENTAL_FIELD_FIELD_NUMBER: _ClassVar[int]
    incremental_field: ScannedData.IncrementalField

    def __init__(self, incremental_field: _Optional[_Union[ScannedData.IncrementalField, _Mapping]]=...) -> None:
        ...