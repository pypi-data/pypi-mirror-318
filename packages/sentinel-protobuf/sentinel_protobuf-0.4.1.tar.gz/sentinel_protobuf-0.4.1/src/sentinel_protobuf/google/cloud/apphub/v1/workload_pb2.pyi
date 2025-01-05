from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.apphub.v1 import attributes_pb2 as _attributes_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Workload(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'workload_reference', 'workload_properties', 'discovered_workload', 'attributes', 'create_time', 'update_time', 'uid', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Workload.State]
        CREATING: _ClassVar[Workload.State]
        ACTIVE: _ClassVar[Workload.State]
        DELETING: _ClassVar[Workload.State]
        DETACHED: _ClassVar[Workload.State]
    STATE_UNSPECIFIED: Workload.State
    CREATING: Workload.State
    ACTIVE: Workload.State
    DELETING: Workload.State
    DETACHED: Workload.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    DISCOVERED_WORKLOAD_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    workload_reference: WorkloadReference
    workload_properties: WorkloadProperties
    discovered_workload: str
    attributes: _attributes_pb2.Attributes
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    uid: str
    state: Workload.State

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., workload_reference: _Optional[_Union[WorkloadReference, _Mapping]]=..., workload_properties: _Optional[_Union[WorkloadProperties, _Mapping]]=..., discovered_workload: _Optional[str]=..., attributes: _Optional[_Union[_attributes_pb2.Attributes, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., uid: _Optional[str]=..., state: _Optional[_Union[Workload.State, str]]=...) -> None:
        ...

class WorkloadReference(_message.Message):
    __slots__ = ('uri',)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str

    def __init__(self, uri: _Optional[str]=...) -> None:
        ...

class WorkloadProperties(_message.Message):
    __slots__ = ('gcp_project', 'location', 'zone')
    GCP_PROJECT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    gcp_project: str
    location: str
    zone: str

    def __init__(self, gcp_project: _Optional[str]=..., location: _Optional[str]=..., zone: _Optional[str]=...) -> None:
        ...

class DiscoveredWorkload(_message.Message):
    __slots__ = ('name', 'workload_reference', 'workload_properties')
    NAME_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    workload_reference: WorkloadReference
    workload_properties: WorkloadProperties

    def __init__(self, name: _Optional[str]=..., workload_reference: _Optional[_Union[WorkloadReference, _Mapping]]=..., workload_properties: _Optional[_Union[WorkloadProperties, _Mapping]]=...) -> None:
        ...