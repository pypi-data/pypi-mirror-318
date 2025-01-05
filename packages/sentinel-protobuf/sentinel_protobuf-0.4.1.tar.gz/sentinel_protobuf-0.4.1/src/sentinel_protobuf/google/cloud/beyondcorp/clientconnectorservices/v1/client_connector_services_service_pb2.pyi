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

class ClientConnectorService(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'display_name', 'ingress', 'egress', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ClientConnectorService.State]
        CREATING: _ClassVar[ClientConnectorService.State]
        UPDATING: _ClassVar[ClientConnectorService.State]
        DELETING: _ClassVar[ClientConnectorService.State]
        RUNNING: _ClassVar[ClientConnectorService.State]
        DOWN: _ClassVar[ClientConnectorService.State]
        ERROR: _ClassVar[ClientConnectorService.State]
    STATE_UNSPECIFIED: ClientConnectorService.State
    CREATING: ClientConnectorService.State
    UPDATING: ClientConnectorService.State
    DELETING: ClientConnectorService.State
    RUNNING: ClientConnectorService.State
    DOWN: ClientConnectorService.State
    ERROR: ClientConnectorService.State

    class Ingress(_message.Message):
        __slots__ = ('config',)

        class Config(_message.Message):
            __slots__ = ('transport_protocol', 'destination_routes')

            class TransportProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                TRANSPORT_PROTOCOL_UNSPECIFIED: _ClassVar[ClientConnectorService.Ingress.Config.TransportProtocol]
                TCP: _ClassVar[ClientConnectorService.Ingress.Config.TransportProtocol]
            TRANSPORT_PROTOCOL_UNSPECIFIED: ClientConnectorService.Ingress.Config.TransportProtocol
            TCP: ClientConnectorService.Ingress.Config.TransportProtocol

            class DestinationRoute(_message.Message):
                __slots__ = ('address', 'netmask')
                ADDRESS_FIELD_NUMBER: _ClassVar[int]
                NETMASK_FIELD_NUMBER: _ClassVar[int]
                address: str
                netmask: str

                def __init__(self, address: _Optional[str]=..., netmask: _Optional[str]=...) -> None:
                    ...
            TRANSPORT_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
            DESTINATION_ROUTES_FIELD_NUMBER: _ClassVar[int]
            transport_protocol: ClientConnectorService.Ingress.Config.TransportProtocol
            destination_routes: _containers.RepeatedCompositeFieldContainer[ClientConnectorService.Ingress.Config.DestinationRoute]

            def __init__(self, transport_protocol: _Optional[_Union[ClientConnectorService.Ingress.Config.TransportProtocol, str]]=..., destination_routes: _Optional[_Iterable[_Union[ClientConnectorService.Ingress.Config.DestinationRoute, _Mapping]]]=...) -> None:
                ...
        CONFIG_FIELD_NUMBER: _ClassVar[int]
        config: ClientConnectorService.Ingress.Config

        def __init__(self, config: _Optional[_Union[ClientConnectorService.Ingress.Config, _Mapping]]=...) -> None:
            ...

    class Egress(_message.Message):
        __slots__ = ('peered_vpc',)

        class PeeredVpc(_message.Message):
            __slots__ = ('network_vpc',)
            NETWORK_VPC_FIELD_NUMBER: _ClassVar[int]
            network_vpc: str

            def __init__(self, network_vpc: _Optional[str]=...) -> None:
                ...
        PEERED_VPC_FIELD_NUMBER: _ClassVar[int]
        peered_vpc: ClientConnectorService.Egress.PeeredVpc

        def __init__(self, peered_vpc: _Optional[_Union[ClientConnectorService.Egress.PeeredVpc, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    INGRESS_FIELD_NUMBER: _ClassVar[int]
    EGRESS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    display_name: str
    ingress: ClientConnectorService.Ingress
    egress: ClientConnectorService.Egress
    state: ClientConnectorService.State

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., display_name: _Optional[str]=..., ingress: _Optional[_Union[ClientConnectorService.Ingress, _Mapping]]=..., egress: _Optional[_Union[ClientConnectorService.Egress, _Mapping]]=..., state: _Optional[_Union[ClientConnectorService.State, str]]=...) -> None:
        ...

class ListClientConnectorServicesRequest(_message.Message):
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

class ListClientConnectorServicesResponse(_message.Message):
    __slots__ = ('client_connector_services', 'next_page_token', 'unreachable')
    CLIENT_CONNECTOR_SERVICES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    client_connector_services: _containers.RepeatedCompositeFieldContainer[ClientConnectorService]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, client_connector_services: _Optional[_Iterable[_Union[ClientConnectorService, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetClientConnectorServiceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateClientConnectorServiceRequest(_message.Message):
    __slots__ = ('parent', 'client_connector_service_id', 'client_connector_service', 'request_id', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CONNECTOR_SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CONNECTOR_SERVICE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    client_connector_service_id: str
    client_connector_service: ClientConnectorService
    request_id: str
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., client_connector_service_id: _Optional[str]=..., client_connector_service: _Optional[_Union[ClientConnectorService, _Mapping]]=..., request_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class UpdateClientConnectorServiceRequest(_message.Message):
    __slots__ = ('update_mask', 'client_connector_service', 'request_id', 'validate_only', 'allow_missing')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CONNECTOR_SERVICE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    client_connector_service: ClientConnectorService
    request_id: str
    validate_only: bool
    allow_missing: bool

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., client_connector_service: _Optional[_Union[ClientConnectorService, _Mapping]]=..., request_id: _Optional[str]=..., validate_only: bool=..., allow_missing: bool=...) -> None:
        ...

class DeleteClientConnectorServiceRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'validate_only')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    validate_only: bool

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class ClientConnectorServiceOperationMetadata(_message.Message):
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