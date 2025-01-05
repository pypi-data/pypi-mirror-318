from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.monitoring.metricsscope.v1 import metrics_scope_pb2 as _metrics_scope_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetMetricsScopeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListMetricsScopesByMonitoredProjectRequest(_message.Message):
    __slots__ = ('monitored_resource_container',)
    MONITORED_RESOURCE_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    monitored_resource_container: str

    def __init__(self, monitored_resource_container: _Optional[str]=...) -> None:
        ...

class ListMetricsScopesByMonitoredProjectResponse(_message.Message):
    __slots__ = ('metrics_scopes',)
    METRICS_SCOPES_FIELD_NUMBER: _ClassVar[int]
    metrics_scopes: _containers.RepeatedCompositeFieldContainer[_metrics_scope_pb2.MetricsScope]

    def __init__(self, metrics_scopes: _Optional[_Iterable[_Union[_metrics_scope_pb2.MetricsScope, _Mapping]]]=...) -> None:
        ...

class CreateMonitoredProjectRequest(_message.Message):
    __slots__ = ('parent', 'monitored_project')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MONITORED_PROJECT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    monitored_project: _metrics_scope_pb2.MonitoredProject

    def __init__(self, parent: _Optional[str]=..., monitored_project: _Optional[_Union[_metrics_scope_pb2.MonitoredProject, _Mapping]]=...) -> None:
        ...

class DeleteMonitoredProjectRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('state', 'create_time', 'update_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[OperationMetadata.State]
        CREATED: _ClassVar[OperationMetadata.State]
        RUNNING: _ClassVar[OperationMetadata.State]
        DONE: _ClassVar[OperationMetadata.State]
        CANCELLED: _ClassVar[OperationMetadata.State]
    STATE_UNSPECIFIED: OperationMetadata.State
    CREATED: OperationMetadata.State
    RUNNING: OperationMetadata.State
    DONE: OperationMetadata.State
    CANCELLED: OperationMetadata.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    state: OperationMetadata.State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, state: _Optional[_Union[OperationMetadata.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...