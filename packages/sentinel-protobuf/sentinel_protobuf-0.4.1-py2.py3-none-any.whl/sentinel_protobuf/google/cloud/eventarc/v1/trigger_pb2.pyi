from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.eventarc.v1 import network_config_pb2 as _network_config_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import code_pb2 as _code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Trigger(_message.Message):
    __slots__ = ('name', 'uid', 'create_time', 'update_time', 'event_filters', 'service_account', 'destination', 'transport', 'labels', 'channel', 'conditions', 'event_data_content_type', 'satisfies_pzs', 'etag')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class ConditionsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: StateCondition

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[StateCondition, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EVENT_FILTERS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    EVENT_DATA_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    event_filters: _containers.RepeatedCompositeFieldContainer[EventFilter]
    service_account: str
    destination: Destination
    transport: Transport
    labels: _containers.ScalarMap[str, str]
    channel: str
    conditions: _containers.MessageMap[str, StateCondition]
    event_data_content_type: str
    satisfies_pzs: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., event_filters: _Optional[_Iterable[_Union[EventFilter, _Mapping]]]=..., service_account: _Optional[str]=..., destination: _Optional[_Union[Destination, _Mapping]]=..., transport: _Optional[_Union[Transport, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., channel: _Optional[str]=..., conditions: _Optional[_Mapping[str, StateCondition]]=..., event_data_content_type: _Optional[str]=..., satisfies_pzs: bool=..., etag: _Optional[str]=...) -> None:
        ...

class EventFilter(_message.Message):
    __slots__ = ('attribute', 'value', 'operator')
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    attribute: str
    value: str
    operator: str

    def __init__(self, attribute: _Optional[str]=..., value: _Optional[str]=..., operator: _Optional[str]=...) -> None:
        ...

class StateCondition(_message.Message):
    __slots__ = ('code', 'message')
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: _code_pb2.Code
    message: str

    def __init__(self, code: _Optional[_Union[_code_pb2.Code, str]]=..., message: _Optional[str]=...) -> None:
        ...

class Destination(_message.Message):
    __slots__ = ('cloud_run', 'cloud_function', 'gke', 'workflow', 'http_endpoint', 'network_config')
    CLOUD_RUN_FIELD_NUMBER: _ClassVar[int]
    CLOUD_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    GKE_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_FIELD_NUMBER: _ClassVar[int]
    HTTP_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    cloud_run: CloudRun
    cloud_function: str
    gke: GKE
    workflow: str
    http_endpoint: HttpEndpoint
    network_config: _network_config_pb2.NetworkConfig

    def __init__(self, cloud_run: _Optional[_Union[CloudRun, _Mapping]]=..., cloud_function: _Optional[str]=..., gke: _Optional[_Union[GKE, _Mapping]]=..., workflow: _Optional[str]=..., http_endpoint: _Optional[_Union[HttpEndpoint, _Mapping]]=..., network_config: _Optional[_Union[_network_config_pb2.NetworkConfig, _Mapping]]=...) -> None:
        ...

class Transport(_message.Message):
    __slots__ = ('pubsub',)
    PUBSUB_FIELD_NUMBER: _ClassVar[int]
    pubsub: Pubsub

    def __init__(self, pubsub: _Optional[_Union[Pubsub, _Mapping]]=...) -> None:
        ...

class CloudRun(_message.Message):
    __slots__ = ('service', 'path', 'region')
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    service: str
    path: str
    region: str

    def __init__(self, service: _Optional[str]=..., path: _Optional[str]=..., region: _Optional[str]=...) -> None:
        ...

class GKE(_message.Message):
    __slots__ = ('cluster', 'location', 'namespace', 'service', 'path')
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    cluster: str
    location: str
    namespace: str
    service: str
    path: str

    def __init__(self, cluster: _Optional[str]=..., location: _Optional[str]=..., namespace: _Optional[str]=..., service: _Optional[str]=..., path: _Optional[str]=...) -> None:
        ...

class Pubsub(_message.Message):
    __slots__ = ('topic', 'subscription')
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    topic: str
    subscription: str

    def __init__(self, topic: _Optional[str]=..., subscription: _Optional[str]=...) -> None:
        ...

class HttpEndpoint(_message.Message):
    __slots__ = ('uri',)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str

    def __init__(self, uri: _Optional[str]=...) -> None:
        ...