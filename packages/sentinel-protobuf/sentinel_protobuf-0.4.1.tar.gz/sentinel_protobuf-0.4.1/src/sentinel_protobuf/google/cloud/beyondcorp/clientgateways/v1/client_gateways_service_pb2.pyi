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

class ClientGateway(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'state', 'id', 'client_connector_service')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ClientGateway.State]
        CREATING: _ClassVar[ClientGateway.State]
        UPDATING: _ClassVar[ClientGateway.State]
        DELETING: _ClassVar[ClientGateway.State]
        RUNNING: _ClassVar[ClientGateway.State]
        DOWN: _ClassVar[ClientGateway.State]
        ERROR: _ClassVar[ClientGateway.State]
    STATE_UNSPECIFIED: ClientGateway.State
    CREATING: ClientGateway.State
    UPDATING: ClientGateway.State
    DELETING: ClientGateway.State
    RUNNING: ClientGateway.State
    DOWN: ClientGateway.State
    ERROR: ClientGateway.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CONNECTOR_SERVICE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    state: ClientGateway.State
    id: str
    client_connector_service: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[ClientGateway.State, str]]=..., id: _Optional[str]=..., client_connector_service: _Optional[str]=...) -> None:
        ...

class ListClientGatewaysRequest(_message.Message):
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

class ListClientGatewaysResponse(_message.Message):
    __slots__ = ('client_gateways', 'next_page_token', 'unreachable')
    CLIENT_GATEWAYS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    client_gateways: _containers.RepeatedCompositeFieldContainer[ClientGateway]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, client_gateways: _Optional[_Iterable[_Union[ClientGateway, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetClientGatewayRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateClientGatewayRequest(_message.Message):
    __slots__ = ('parent', 'client_gateway_id', 'client_gateway', 'request_id', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    client_gateway_id: str
    client_gateway: ClientGateway
    request_id: str
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., client_gateway_id: _Optional[str]=..., client_gateway: _Optional[_Union[ClientGateway, _Mapping]]=..., request_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class DeleteClientGatewayRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'validate_only')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    validate_only: bool

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class ClientGatewayOperationMetadata(_message.Message):
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