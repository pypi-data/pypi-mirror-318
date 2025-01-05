from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.beyondcorp.appconnectors.v1 import app_connector_instance_config_pb2 as _app_connector_instance_config_pb2
from google.cloud.beyondcorp.appconnectors.v1 import resource_info_pb2 as _resource_info_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListAppConnectorsRequest(_message.Message):
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

class ListAppConnectorsResponse(_message.Message):
    __slots__ = ('app_connectors', 'next_page_token', 'unreachable')
    APP_CONNECTORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    app_connectors: _containers.RepeatedCompositeFieldContainer[AppConnector]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, app_connectors: _Optional[_Iterable[_Union[AppConnector, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetAppConnectorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateAppConnectorRequest(_message.Message):
    __slots__ = ('parent', 'app_connector_id', 'app_connector', 'request_id', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    APP_CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    APP_CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    app_connector_id: str
    app_connector: AppConnector
    request_id: str
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., app_connector_id: _Optional[str]=..., app_connector: _Optional[_Union[AppConnector, _Mapping]]=..., request_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class UpdateAppConnectorRequest(_message.Message):
    __slots__ = ('update_mask', 'app_connector', 'request_id', 'validate_only')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    APP_CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    app_connector: AppConnector
    request_id: str
    validate_only: bool

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., app_connector: _Optional[_Union[AppConnector, _Mapping]]=..., request_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class DeleteAppConnectorRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'validate_only')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    validate_only: bool

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class ReportStatusRequest(_message.Message):
    __slots__ = ('app_connector', 'resource_info', 'request_id', 'validate_only')
    APP_CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    app_connector: str
    resource_info: _resource_info_pb2.ResourceInfo
    request_id: str
    validate_only: bool

    def __init__(self, app_connector: _Optional[str]=..., resource_info: _Optional[_Union[_resource_info_pb2.ResourceInfo, _Mapping]]=..., request_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class AppConnector(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'display_name', 'uid', 'state', 'principal_info', 'resource_info')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AppConnector.State]
        CREATING: _ClassVar[AppConnector.State]
        CREATED: _ClassVar[AppConnector.State]
        UPDATING: _ClassVar[AppConnector.State]
        DELETING: _ClassVar[AppConnector.State]
        DOWN: _ClassVar[AppConnector.State]
    STATE_UNSPECIFIED: AppConnector.State
    CREATING: AppConnector.State
    CREATED: AppConnector.State
    UPDATING: AppConnector.State
    DELETING: AppConnector.State
    DOWN: AppConnector.State

    class PrincipalInfo(_message.Message):
        __slots__ = ('service_account',)

        class ServiceAccount(_message.Message):
            __slots__ = ('email',)
            EMAIL_FIELD_NUMBER: _ClassVar[int]
            email: str

            def __init__(self, email: _Optional[str]=...) -> None:
                ...
        SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        service_account: AppConnector.PrincipalInfo.ServiceAccount

        def __init__(self, service_account: _Optional[_Union[AppConnector.PrincipalInfo.ServiceAccount, _Mapping]]=...) -> None:
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
    STATE_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_INFO_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    display_name: str
    uid: str
    state: AppConnector.State
    principal_info: AppConnector.PrincipalInfo
    resource_info: _resource_info_pb2.ResourceInfo

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., display_name: _Optional[str]=..., uid: _Optional[str]=..., state: _Optional[_Union[AppConnector.State, str]]=..., principal_info: _Optional[_Union[AppConnector.PrincipalInfo, _Mapping]]=..., resource_info: _Optional[_Union[_resource_info_pb2.ResourceInfo, _Mapping]]=...) -> None:
        ...

class AppConnectorOperationMetadata(_message.Message):
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