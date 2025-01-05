from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.backupdr.v1 import backupplan_pb2 as _backupplan_pb2
from google.cloud.backupdr.v1 import backupplanassociation_pb2 as _backupplanassociation_pb2
from google.cloud.backupdr.v1 import backupvault_pb2 as _backupvault_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NetworkConfig(_message.Message):
    __slots__ = ("network", "peering_mode")
    class PeeringMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PEERING_MODE_UNSPECIFIED: _ClassVar[NetworkConfig.PeeringMode]
        PRIVATE_SERVICE_ACCESS: _ClassVar[NetworkConfig.PeeringMode]
    PEERING_MODE_UNSPECIFIED: NetworkConfig.PeeringMode
    PRIVATE_SERVICE_ACCESS: NetworkConfig.PeeringMode
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    PEERING_MODE_FIELD_NUMBER: _ClassVar[int]
    network: str
    peering_mode: NetworkConfig.PeeringMode
    def __init__(self, network: _Optional[str] = ..., peering_mode: _Optional[_Union[NetworkConfig.PeeringMode, str]] = ...) -> None: ...

class ManagementURI(_message.Message):
    __slots__ = ("web_ui", "api")
    WEB_UI_FIELD_NUMBER: _ClassVar[int]
    API_FIELD_NUMBER: _ClassVar[int]
    web_ui: str
    api: str
    def __init__(self, web_ui: _Optional[str] = ..., api: _Optional[str] = ...) -> None: ...

class WorkforceIdentityBasedManagementURI(_message.Message):
    __slots__ = ("first_party_management_uri", "third_party_management_uri")
    FIRST_PARTY_MANAGEMENT_URI_FIELD_NUMBER: _ClassVar[int]
    THIRD_PARTY_MANAGEMENT_URI_FIELD_NUMBER: _ClassVar[int]
    first_party_management_uri: str
    third_party_management_uri: str
    def __init__(self, first_party_management_uri: _Optional[str] = ..., third_party_management_uri: _Optional[str] = ...) -> None: ...

class WorkforceIdentityBasedOAuth2ClientID(_message.Message):
    __slots__ = ("first_party_oauth2_client_id", "third_party_oauth2_client_id")
    FIRST_PARTY_OAUTH2_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    THIRD_PARTY_OAUTH2_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    first_party_oauth2_client_id: str
    third_party_oauth2_client_id: str
    def __init__(self, first_party_oauth2_client_id: _Optional[str] = ..., third_party_oauth2_client_id: _Optional[str] = ...) -> None: ...

class ManagementServer(_message.Message):
    __slots__ = ("name", "description", "labels", "create_time", "update_time", "type", "management_uri", "workforce_identity_based_management_uri", "state", "networks", "etag", "oauth2_client_id", "workforce_identity_based_oauth2_client_id", "ba_proxy_uri", "satisfies_pzs", "satisfies_pzi")
    class InstanceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INSTANCE_TYPE_UNSPECIFIED: _ClassVar[ManagementServer.InstanceType]
        BACKUP_RESTORE: _ClassVar[ManagementServer.InstanceType]
    INSTANCE_TYPE_UNSPECIFIED: ManagementServer.InstanceType
    BACKUP_RESTORE: ManagementServer.InstanceType
    class InstanceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INSTANCE_STATE_UNSPECIFIED: _ClassVar[ManagementServer.InstanceState]
        CREATING: _ClassVar[ManagementServer.InstanceState]
        READY: _ClassVar[ManagementServer.InstanceState]
        UPDATING: _ClassVar[ManagementServer.InstanceState]
        DELETING: _ClassVar[ManagementServer.InstanceState]
        REPAIRING: _ClassVar[ManagementServer.InstanceState]
        MAINTENANCE: _ClassVar[ManagementServer.InstanceState]
        ERROR: _ClassVar[ManagementServer.InstanceState]
    INSTANCE_STATE_UNSPECIFIED: ManagementServer.InstanceState
    CREATING: ManagementServer.InstanceState
    READY: ManagementServer.InstanceState
    UPDATING: ManagementServer.InstanceState
    DELETING: ManagementServer.InstanceState
    REPAIRING: ManagementServer.InstanceState
    MAINTENANCE: ManagementServer.InstanceState
    ERROR: ManagementServer.InstanceState
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_URI_FIELD_NUMBER: _ClassVar[int]
    WORKFORCE_IDENTITY_BASED_MANAGEMENT_URI_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    NETWORKS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    OAUTH2_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFORCE_IDENTITY_BASED_OAUTH2_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    BA_PROXY_URI_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    type: ManagementServer.InstanceType
    management_uri: ManagementURI
    workforce_identity_based_management_uri: WorkforceIdentityBasedManagementURI
    state: ManagementServer.InstanceState
    networks: _containers.RepeatedCompositeFieldContainer[NetworkConfig]
    etag: str
    oauth2_client_id: str
    workforce_identity_based_oauth2_client_id: WorkforceIdentityBasedOAuth2ClientID
    ba_proxy_uri: _containers.RepeatedScalarFieldContainer[str]
    satisfies_pzs: _wrappers_pb2.BoolValue
    satisfies_pzi: bool
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., type: _Optional[_Union[ManagementServer.InstanceType, str]] = ..., management_uri: _Optional[_Union[ManagementURI, _Mapping]] = ..., workforce_identity_based_management_uri: _Optional[_Union[WorkforceIdentityBasedManagementURI, _Mapping]] = ..., state: _Optional[_Union[ManagementServer.InstanceState, str]] = ..., networks: _Optional[_Iterable[_Union[NetworkConfig, _Mapping]]] = ..., etag: _Optional[str] = ..., oauth2_client_id: _Optional[str] = ..., workforce_identity_based_oauth2_client_id: _Optional[_Union[WorkforceIdentityBasedOAuth2ClientID, _Mapping]] = ..., ba_proxy_uri: _Optional[_Iterable[str]] = ..., satisfies_pzs: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., satisfies_pzi: bool = ...) -> None: ...

class ListManagementServersRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListManagementServersResponse(_message.Message):
    __slots__ = ("management_servers", "next_page_token", "unreachable")
    MANAGEMENT_SERVERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    management_servers: _containers.RepeatedCompositeFieldContainer[ManagementServer]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, management_servers: _Optional[_Iterable[_Union[ManagementServer, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetManagementServerRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateManagementServerRequest(_message.Message):
    __slots__ = ("parent", "management_server_id", "management_server", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_SERVER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    management_server_id: str
    management_server: ManagementServer
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., management_server_id: _Optional[str] = ..., management_server: _Optional[_Union[ManagementServer, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteManagementServerRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class OperationMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "target", "verb", "status_message", "requested_cancellation", "api_version", "additional_info")
    class AdditionalInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_INFO_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str
    additional_info: _containers.ScalarMap[str, str]
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., target: _Optional[str] = ..., verb: _Optional[str] = ..., status_message: _Optional[str] = ..., requested_cancellation: bool = ..., api_version: _Optional[str] = ..., additional_info: _Optional[_Mapping[str, str]] = ...) -> None: ...
