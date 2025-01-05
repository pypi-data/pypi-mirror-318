from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Connector(_message.Message):
    __slots__ = ('name', 'network', 'ip_cidr_range', 'state', 'min_throughput', 'max_throughput', 'connected_projects', 'subnet', 'machine_type', 'min_instances', 'max_instances')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Connector.State]
        READY: _ClassVar[Connector.State]
        CREATING: _ClassVar[Connector.State]
        DELETING: _ClassVar[Connector.State]
        ERROR: _ClassVar[Connector.State]
        UPDATING: _ClassVar[Connector.State]
    STATE_UNSPECIFIED: Connector.State
    READY: Connector.State
    CREATING: Connector.State
    DELETING: Connector.State
    ERROR: Connector.State
    UPDATING: Connector.State

    class Subnet(_message.Message):
        __slots__ = ('name', 'project_id')
        NAME_FIELD_NUMBER: _ClassVar[int]
        PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
        name: str
        project_id: str

        def __init__(self, name: _Optional[str]=..., project_id: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    IP_CIDR_RANGE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    MIN_THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
    MAX_THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_PROJECTS_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MIN_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    MAX_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    name: str
    network: str
    ip_cidr_range: str
    state: Connector.State
    min_throughput: int
    max_throughput: int
    connected_projects: _containers.RepeatedScalarFieldContainer[str]
    subnet: Connector.Subnet
    machine_type: str
    min_instances: int
    max_instances: int

    def __init__(self, name: _Optional[str]=..., network: _Optional[str]=..., ip_cidr_range: _Optional[str]=..., state: _Optional[_Union[Connector.State, str]]=..., min_throughput: _Optional[int]=..., max_throughput: _Optional[int]=..., connected_projects: _Optional[_Iterable[str]]=..., subnet: _Optional[_Union[Connector.Subnet, _Mapping]]=..., machine_type: _Optional[str]=..., min_instances: _Optional[int]=..., max_instances: _Optional[int]=...) -> None:
        ...

class CreateConnectorRequest(_message.Message):
    __slots__ = ('parent', 'connector_id', 'connector')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    parent: str
    connector_id: str
    connector: Connector

    def __init__(self, parent: _Optional[str]=..., connector_id: _Optional[str]=..., connector: _Optional[_Union[Connector, _Mapping]]=...) -> None:
        ...

class GetConnectorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListConnectorsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListConnectorsResponse(_message.Message):
    __slots__ = ('connectors', 'next_page_token')
    CONNECTORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    connectors: _containers.RepeatedCompositeFieldContainer[Connector]
    next_page_token: str

    def __init__(self, connectors: _Optional[_Iterable[_Union[Connector, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteConnectorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('method', 'create_time', 'end_time', 'target')
    METHOD_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    method: str
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str

    def __init__(self, method: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=...) -> None:
        ...