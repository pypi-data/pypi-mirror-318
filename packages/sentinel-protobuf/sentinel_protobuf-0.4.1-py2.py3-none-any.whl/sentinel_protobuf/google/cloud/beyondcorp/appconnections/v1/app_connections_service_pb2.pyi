from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListAppConnectionsRequest(_message.Message):
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

class ListAppConnectionsResponse(_message.Message):
    __slots__ = ('app_connections', 'next_page_token', 'unreachable')
    APP_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    app_connections: _containers.RepeatedCompositeFieldContainer[AppConnection]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, app_connections: _Optional[_Iterable[_Union[AppConnection, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetAppConnectionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateAppConnectionRequest(_message.Message):
    __slots__ = ('parent', 'app_connection_id', 'app_connection', 'request_id', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    APP_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    APP_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    app_connection_id: str
    app_connection: AppConnection
    request_id: str
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., app_connection_id: _Optional[str]=..., app_connection: _Optional[_Union[AppConnection, _Mapping]]=..., request_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class UpdateAppConnectionRequest(_message.Message):
    __slots__ = ('update_mask', 'app_connection', 'request_id', 'validate_only', 'allow_missing')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    APP_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    app_connection: AppConnection
    request_id: str
    validate_only: bool
    allow_missing: bool

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., app_connection: _Optional[_Union[AppConnection, _Mapping]]=..., request_id: _Optional[str]=..., validate_only: bool=..., allow_missing: bool=...) -> None:
        ...

class DeleteAppConnectionRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'validate_only')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    validate_only: bool

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class ResolveAppConnectionsRequest(_message.Message):
    __slots__ = ('parent', 'app_connector_id', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    APP_CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    app_connector_id: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., app_connector_id: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ResolveAppConnectionsResponse(_message.Message):
    __slots__ = ('app_connection_details', 'next_page_token', 'unreachable')

    class AppConnectionDetails(_message.Message):
        __slots__ = ('app_connection', 'recent_mig_vms')
        APP_CONNECTION_FIELD_NUMBER: _ClassVar[int]
        RECENT_MIG_VMS_FIELD_NUMBER: _ClassVar[int]
        app_connection: AppConnection
        recent_mig_vms: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, app_connection: _Optional[_Union[AppConnection, _Mapping]]=..., recent_mig_vms: _Optional[_Iterable[str]]=...) -> None:
            ...
    APP_CONNECTION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    app_connection_details: _containers.RepeatedCompositeFieldContainer[ResolveAppConnectionsResponse.AppConnectionDetails]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, app_connection_details: _Optional[_Iterable[_Union[ResolveAppConnectionsResponse.AppConnectionDetails, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class AppConnection(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'display_name', 'uid', 'type', 'application_endpoint', 'connectors', 'state', 'gateway')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[AppConnection.Type]
        TCP_PROXY: _ClassVar[AppConnection.Type]
    TYPE_UNSPECIFIED: AppConnection.Type
    TCP_PROXY: AppConnection.Type

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AppConnection.State]
        CREATING: _ClassVar[AppConnection.State]
        CREATED: _ClassVar[AppConnection.State]
        UPDATING: _ClassVar[AppConnection.State]
        DELETING: _ClassVar[AppConnection.State]
        DOWN: _ClassVar[AppConnection.State]
    STATE_UNSPECIFIED: AppConnection.State
    CREATING: AppConnection.State
    CREATED: AppConnection.State
    UPDATING: AppConnection.State
    DELETING: AppConnection.State
    DOWN: AppConnection.State

    class ApplicationEndpoint(_message.Message):
        __slots__ = ('host', 'port')
        HOST_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        host: str
        port: int

        def __init__(self, host: _Optional[str]=..., port: _Optional[int]=...) -> None:
            ...

    class Gateway(_message.Message):
        __slots__ = ('type', 'uri', 'ingress_port', 'app_gateway')

        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[AppConnection.Gateway.Type]
            GCP_REGIONAL_MIG: _ClassVar[AppConnection.Gateway.Type]
        TYPE_UNSPECIFIED: AppConnection.Gateway.Type
        GCP_REGIONAL_MIG: AppConnection.Gateway.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        URI_FIELD_NUMBER: _ClassVar[int]
        INGRESS_PORT_FIELD_NUMBER: _ClassVar[int]
        APP_GATEWAY_FIELD_NUMBER: _ClassVar[int]
        type: AppConnection.Gateway.Type
        uri: str
        ingress_port: int
        app_gateway: str

        def __init__(self, type: _Optional[_Union[AppConnection.Gateway.Type, str]]=..., uri: _Optional[str]=..., ingress_port: _Optional[int]=..., app_gateway: _Optional[str]=...) -> None:
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
    APPLICATION_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    CONNECTORS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    display_name: str
    uid: str
    type: AppConnection.Type
    application_endpoint: AppConnection.ApplicationEndpoint
    connectors: _containers.RepeatedScalarFieldContainer[str]
    state: AppConnection.State
    gateway: AppConnection.Gateway

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., display_name: _Optional[str]=..., uid: _Optional[str]=..., type: _Optional[_Union[AppConnection.Type, str]]=..., application_endpoint: _Optional[_Union[AppConnection.ApplicationEndpoint, _Mapping]]=..., connectors: _Optional[_Iterable[str]]=..., state: _Optional[_Union[AppConnection.State, str]]=..., gateway: _Optional[_Union[AppConnection.Gateway, _Mapping]]=...) -> None:
        ...

class AppConnectionOperationMetadata(_message.Message):
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