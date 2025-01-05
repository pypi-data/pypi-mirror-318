from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Api(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'display_name', 'managed_service', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Api.State]
        CREATING: _ClassVar[Api.State]
        ACTIVE: _ClassVar[Api.State]
        FAILED: _ClassVar[Api.State]
        DELETING: _ClassVar[Api.State]
        UPDATING: _ClassVar[Api.State]
    STATE_UNSPECIFIED: Api.State
    CREATING: Api.State
    ACTIVE: Api.State
    FAILED: Api.State
    DELETING: Api.State
    UPDATING: Api.State

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
    MANAGED_SERVICE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    display_name: str
    managed_service: str
    state: Api.State

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., display_name: _Optional[str]=..., managed_service: _Optional[str]=..., state: _Optional[_Union[Api.State, str]]=...) -> None:
        ...

class ApiConfig(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'display_name', 'gateway_service_account', 'service_config_id', 'state', 'openapi_documents', 'grpc_services', 'managed_service_configs')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ApiConfig.State]
        CREATING: _ClassVar[ApiConfig.State]
        ACTIVE: _ClassVar[ApiConfig.State]
        FAILED: _ClassVar[ApiConfig.State]
        DELETING: _ClassVar[ApiConfig.State]
        UPDATING: _ClassVar[ApiConfig.State]
        ACTIVATING: _ClassVar[ApiConfig.State]
    STATE_UNSPECIFIED: ApiConfig.State
    CREATING: ApiConfig.State
    ACTIVE: ApiConfig.State
    FAILED: ApiConfig.State
    DELETING: ApiConfig.State
    UPDATING: ApiConfig.State
    ACTIVATING: ApiConfig.State

    class File(_message.Message):
        __slots__ = ('path', 'contents')
        PATH_FIELD_NUMBER: _ClassVar[int]
        CONTENTS_FIELD_NUMBER: _ClassVar[int]
        path: str
        contents: bytes

        def __init__(self, path: _Optional[str]=..., contents: _Optional[bytes]=...) -> None:
            ...

    class OpenApiDocument(_message.Message):
        __slots__ = ('document',)
        DOCUMENT_FIELD_NUMBER: _ClassVar[int]
        document: ApiConfig.File

        def __init__(self, document: _Optional[_Union[ApiConfig.File, _Mapping]]=...) -> None:
            ...

    class GrpcServiceDefinition(_message.Message):
        __slots__ = ('file_descriptor_set', 'source')
        FILE_DESCRIPTOR_SET_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        file_descriptor_set: ApiConfig.File
        source: _containers.RepeatedCompositeFieldContainer[ApiConfig.File]

        def __init__(self, file_descriptor_set: _Optional[_Union[ApiConfig.File, _Mapping]]=..., source: _Optional[_Iterable[_Union[ApiConfig.File, _Mapping]]]=...) -> None:
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
    GATEWAY_SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    OPENAPI_DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    GRPC_SERVICES_FIELD_NUMBER: _ClassVar[int]
    MANAGED_SERVICE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    display_name: str
    gateway_service_account: str
    service_config_id: str
    state: ApiConfig.State
    openapi_documents: _containers.RepeatedCompositeFieldContainer[ApiConfig.OpenApiDocument]
    grpc_services: _containers.RepeatedCompositeFieldContainer[ApiConfig.GrpcServiceDefinition]
    managed_service_configs: _containers.RepeatedCompositeFieldContainer[ApiConfig.File]

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., display_name: _Optional[str]=..., gateway_service_account: _Optional[str]=..., service_config_id: _Optional[str]=..., state: _Optional[_Union[ApiConfig.State, str]]=..., openapi_documents: _Optional[_Iterable[_Union[ApiConfig.OpenApiDocument, _Mapping]]]=..., grpc_services: _Optional[_Iterable[_Union[ApiConfig.GrpcServiceDefinition, _Mapping]]]=..., managed_service_configs: _Optional[_Iterable[_Union[ApiConfig.File, _Mapping]]]=...) -> None:
        ...

class Gateway(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'display_name', 'api_config', 'state', 'default_hostname')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Gateway.State]
        CREATING: _ClassVar[Gateway.State]
        ACTIVE: _ClassVar[Gateway.State]
        FAILED: _ClassVar[Gateway.State]
        DELETING: _ClassVar[Gateway.State]
        UPDATING: _ClassVar[Gateway.State]
    STATE_UNSPECIFIED: Gateway.State
    CREATING: Gateway.State
    ACTIVE: Gateway.State
    FAILED: Gateway.State
    DELETING: Gateway.State
    UPDATING: Gateway.State

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
    API_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    display_name: str
    api_config: str
    state: Gateway.State
    default_hostname: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., display_name: _Optional[str]=..., api_config: _Optional[str]=..., state: _Optional[_Union[Gateway.State, str]]=..., default_hostname: _Optional[str]=...) -> None:
        ...

class ListGatewaysRequest(_message.Message):
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

class ListGatewaysResponse(_message.Message):
    __slots__ = ('gateways', 'next_page_token', 'unreachable_locations')
    GATEWAYS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    gateways: _containers.RepeatedCompositeFieldContainer[Gateway]
    next_page_token: str
    unreachable_locations: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, gateways: _Optional[_Iterable[_Union[Gateway, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable_locations: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetGatewayRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateGatewayRequest(_message.Message):
    __slots__ = ('parent', 'gateway_id', 'gateway')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    gateway_id: str
    gateway: Gateway

    def __init__(self, parent: _Optional[str]=..., gateway_id: _Optional[str]=..., gateway: _Optional[_Union[Gateway, _Mapping]]=...) -> None:
        ...

class UpdateGatewayRequest(_message.Message):
    __slots__ = ('update_mask', 'gateway')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    gateway: Gateway

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., gateway: _Optional[_Union[Gateway, _Mapping]]=...) -> None:
        ...

class DeleteGatewayRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListApisRequest(_message.Message):
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

class ListApisResponse(_message.Message):
    __slots__ = ('apis', 'next_page_token', 'unreachable_locations')
    APIS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    apis: _containers.RepeatedCompositeFieldContainer[Api]
    next_page_token: str
    unreachable_locations: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, apis: _Optional[_Iterable[_Union[Api, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable_locations: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetApiRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateApiRequest(_message.Message):
    __slots__ = ('parent', 'api_id', 'api')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    API_ID_FIELD_NUMBER: _ClassVar[int]
    API_FIELD_NUMBER: _ClassVar[int]
    parent: str
    api_id: str
    api: Api

    def __init__(self, parent: _Optional[str]=..., api_id: _Optional[str]=..., api: _Optional[_Union[Api, _Mapping]]=...) -> None:
        ...

class UpdateApiRequest(_message.Message):
    __slots__ = ('update_mask', 'api')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    API_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    api: Api

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., api: _Optional[_Union[Api, _Mapping]]=...) -> None:
        ...

class DeleteApiRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListApiConfigsRequest(_message.Message):
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

class ListApiConfigsResponse(_message.Message):
    __slots__ = ('api_configs', 'next_page_token', 'unreachable_locations')
    API_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    api_configs: _containers.RepeatedCompositeFieldContainer[ApiConfig]
    next_page_token: str
    unreachable_locations: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, api_configs: _Optional[_Iterable[_Union[ApiConfig, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable_locations: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetApiConfigRequest(_message.Message):
    __slots__ = ('name', 'view')

    class ConfigView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONFIG_VIEW_UNSPECIFIED: _ClassVar[GetApiConfigRequest.ConfigView]
        BASIC: _ClassVar[GetApiConfigRequest.ConfigView]
        FULL: _ClassVar[GetApiConfigRequest.ConfigView]
    CONFIG_VIEW_UNSPECIFIED: GetApiConfigRequest.ConfigView
    BASIC: GetApiConfigRequest.ConfigView
    FULL: GetApiConfigRequest.ConfigView
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: GetApiConfigRequest.ConfigView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[GetApiConfigRequest.ConfigView, str]]=...) -> None:
        ...

class CreateApiConfigRequest(_message.Message):
    __slots__ = ('parent', 'api_config_id', 'api_config')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    API_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    API_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    api_config_id: str
    api_config: ApiConfig

    def __init__(self, parent: _Optional[str]=..., api_config_id: _Optional[str]=..., api_config: _Optional[_Union[ApiConfig, _Mapping]]=...) -> None:
        ...

class UpdateApiConfigRequest(_message.Message):
    __slots__ = ('update_mask', 'api_config')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    API_CONFIG_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    api_config: ApiConfig

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., api_config: _Optional[_Union[ApiConfig, _Mapping]]=...) -> None:
        ...

class DeleteApiConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version', 'diagnostics')

    class Diagnostic(_message.Message):
        __slots__ = ('location', 'message')
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        location: str
        message: str

        def __init__(self, location: _Optional[str]=..., message: _Optional[str]=...) -> None:
            ...
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str
    diagnostics: _containers.RepeatedCompositeFieldContainer[OperationMetadata.Diagnostic]

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=..., diagnostics: _Optional[_Iterable[_Union[OperationMetadata.Diagnostic, _Mapping]]]=...) -> None:
        ...