from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import monitored_resource_pb2 as _monitored_resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class IncidentList(_message.Message):
    __slots__ = ('monitored_resources', 'policy_names')
    MONITORED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    POLICY_NAMES_FIELD_NUMBER: _ClassVar[int]
    monitored_resources: _containers.RepeatedCompositeFieldContainer[_monitored_resource_pb2.MonitoredResource]
    policy_names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, monitored_resources: _Optional[_Iterable[_Union[_monitored_resource_pb2.MonitoredResource, _Mapping]]]=..., policy_names: _Optional[_Iterable[str]]=...) -> None:
        ...