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

class Service(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'service_reference', 'service_properties', 'attributes', 'discovered_service', 'create_time', 'update_time', 'uid', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Service.State]
        CREATING: _ClassVar[Service.State]
        ACTIVE: _ClassVar[Service.State]
        DELETING: _ClassVar[Service.State]
        DETACHED: _ClassVar[Service.State]
    STATE_UNSPECIFIED: Service.State
    CREATING: Service.State
    ACTIVE: Service.State
    DELETING: Service.State
    DETACHED: Service.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SERVICE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    DISCOVERED_SERVICE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    service_reference: ServiceReference
    service_properties: ServiceProperties
    attributes: _attributes_pb2.Attributes
    discovered_service: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    uid: str
    state: Service.State

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., service_reference: _Optional[_Union[ServiceReference, _Mapping]]=..., service_properties: _Optional[_Union[ServiceProperties, _Mapping]]=..., attributes: _Optional[_Union[_attributes_pb2.Attributes, _Mapping]]=..., discovered_service: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., uid: _Optional[str]=..., state: _Optional[_Union[Service.State, str]]=...) -> None:
        ...

class ServiceReference(_message.Message):
    __slots__ = ('uri',)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str

    def __init__(self, uri: _Optional[str]=...) -> None:
        ...

class ServiceProperties(_message.Message):
    __slots__ = ('gcp_project', 'location', 'zone')
    GCP_PROJECT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    gcp_project: str
    location: str
    zone: str

    def __init__(self, gcp_project: _Optional[str]=..., location: _Optional[str]=..., zone: _Optional[str]=...) -> None:
        ...

class DiscoveredService(_message.Message):
    __slots__ = ('name', 'service_reference', 'service_properties')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    service_reference: ServiceReference
    service_properties: ServiceProperties

    def __init__(self, name: _Optional[str]=..., service_reference: _Optional[_Union[ServiceReference, _Mapping]]=..., service_properties: _Optional[_Union[ServiceProperties, _Mapping]]=...) -> None:
        ...