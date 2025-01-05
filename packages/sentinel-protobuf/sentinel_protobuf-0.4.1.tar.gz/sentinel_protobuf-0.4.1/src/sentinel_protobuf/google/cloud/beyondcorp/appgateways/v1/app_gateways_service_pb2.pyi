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

class ListAppGatewaysRequest(_message.Message):
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

class ListAppGatewaysResponse(_message.Message):
    __slots__ = ('app_gateways', 'next_page_token', 'unreachable')
    APP_GATEWAYS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    app_gateways: _containers.RepeatedCompositeFieldContainer[AppGateway]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, app_gateways: _Optional[_Iterable[_Union[AppGateway, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetAppGatewayRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateAppGatewayRequest(_message.Message):
    __slots__ = ('parent', 'app_gateway_id', 'app_gateway', 'request_id', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    APP_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    APP_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    app_gateway_id: str
    app_gateway: AppGateway
    request_id: str
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., app_gateway_id: _Optional[str]=..., app_gateway: _Optional[_Union[AppGateway, _Mapping]]=..., request_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class DeleteAppGatewayRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'validate_only')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    validate_only: bool

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class AppGateway(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'display_name', 'uid', 'type', 'state', 'uri', 'allocated_connections', 'host_type')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[AppGateway.Type]
        TCP_PROXY: _ClassVar[AppGateway.Type]
    TYPE_UNSPECIFIED: AppGateway.Type
    TCP_PROXY: AppGateway.Type

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AppGateway.State]
        CREATING: _ClassVar[AppGateway.State]
        CREATED: _ClassVar[AppGateway.State]
        UPDATING: _ClassVar[AppGateway.State]
        DELETING: _ClassVar[AppGateway.State]
        DOWN: _ClassVar[AppGateway.State]
    STATE_UNSPECIFIED: AppGateway.State
    CREATING: AppGateway.State
    CREATED: AppGateway.State
    UPDATING: AppGateway.State
    DELETING: AppGateway.State
    DOWN: AppGateway.State

    class HostType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HOST_TYPE_UNSPECIFIED: _ClassVar[AppGateway.HostType]
        GCP_REGIONAL_MIG: _ClassVar[AppGateway.HostType]
    HOST_TYPE_UNSPECIFIED: AppGateway.HostType
    GCP_REGIONAL_MIG: AppGateway.HostType

    class AllocatedConnection(_message.Message):
        __slots__ = ('psc_uri', 'ingress_port')
        PSC_URI_FIELD_NUMBER: _ClassVar[int]
        INGRESS_PORT_FIELD_NUMBER: _ClassVar[int]
        psc_uri: str
        ingress_port: int

        def __init__(self, psc_uri: _Optional[str]=..., ingress_port: _Optional[int]=...) -> None:
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
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    ALLOCATED_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    HOST_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    display_name: str
    uid: str
    type: AppGateway.Type
    state: AppGateway.State
    uri: str
    allocated_connections: _containers.RepeatedCompositeFieldContainer[AppGateway.AllocatedConnection]
    host_type: AppGateway.HostType

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., display_name: _Optional[str]=..., uid: _Optional[str]=..., type: _Optional[_Union[AppGateway.Type, str]]=..., state: _Optional[_Union[AppGateway.State, str]]=..., uri: _Optional[str]=..., allocated_connections: _Optional[_Iterable[_Union[AppGateway.AllocatedConnection, _Mapping]]]=..., host_type: _Optional[_Union[AppGateway.HostType, str]]=...) -> None:
        ...

class AppGatewayOperationMetadata(_message.Message):
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