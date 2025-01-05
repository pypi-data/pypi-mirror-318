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

class Endpoint(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'network', 'endpoint_forwarding_rule', 'endpoint_ip', 'description', 'severity', 'state', 'traffic_logs')

    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[Endpoint.Severity]
        INFORMATIONAL: _ClassVar[Endpoint.Severity]
        LOW: _ClassVar[Endpoint.Severity]
        MEDIUM: _ClassVar[Endpoint.Severity]
        HIGH: _ClassVar[Endpoint.Severity]
        CRITICAL: _ClassVar[Endpoint.Severity]
    SEVERITY_UNSPECIFIED: Endpoint.Severity
    INFORMATIONAL: Endpoint.Severity
    LOW: Endpoint.Severity
    MEDIUM: Endpoint.Severity
    HIGH: Endpoint.Severity
    CRITICAL: Endpoint.Severity

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Endpoint.State]
        CREATING: _ClassVar[Endpoint.State]
        READY: _ClassVar[Endpoint.State]
        DELETING: _ClassVar[Endpoint.State]
    STATE_UNSPECIFIED: Endpoint.State
    CREATING: Endpoint.State
    READY: Endpoint.State
    DELETING: Endpoint.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FORWARDING_RULE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_IP_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_LOGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    network: str
    endpoint_forwarding_rule: str
    endpoint_ip: str
    description: str
    severity: Endpoint.Severity
    state: Endpoint.State
    traffic_logs: bool

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., network: _Optional[str]=..., endpoint_forwarding_rule: _Optional[str]=..., endpoint_ip: _Optional[str]=..., description: _Optional[str]=..., severity: _Optional[_Union[Endpoint.Severity, str]]=..., state: _Optional[_Union[Endpoint.State, str]]=..., traffic_logs: bool=...) -> None:
        ...

class ListEndpointsRequest(_message.Message):
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

class ListEndpointsResponse(_message.Message):
    __slots__ = ('endpoints', 'next_page_token', 'unreachable')
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    endpoints: _containers.RepeatedCompositeFieldContainer[Endpoint]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, endpoints: _Optional[_Iterable[_Union[Endpoint, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetEndpointRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateEndpointRequest(_message.Message):
    __slots__ = ('parent', 'endpoint_id', 'endpoint', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    endpoint_id: str
    endpoint: Endpoint
    request_id: str

    def __init__(self, parent: _Optional[str]=..., endpoint_id: _Optional[str]=..., endpoint: _Optional[_Union[Endpoint, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteEndpointRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...