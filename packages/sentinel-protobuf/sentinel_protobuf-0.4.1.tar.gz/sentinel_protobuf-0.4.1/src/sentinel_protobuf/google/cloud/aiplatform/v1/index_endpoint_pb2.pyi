from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1 import machine_resources_pb2 as _machine_resources_pb2
from google.cloud.aiplatform.v1 import service_networking_pb2 as _service_networking_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class IndexEndpoint(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'deployed_indexes', 'etag', 'labels', 'create_time', 'update_time', 'network', 'enable_private_service_connect', 'private_service_connect_config', 'public_endpoint_enabled', 'public_endpoint_domain_name', 'encryption_spec', 'satisfies_pzs', 'satisfies_pzi')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_INDEXES_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PRIVATE_SERVICE_CONNECT_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_SERVICE_CONNECT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_ENDPOINT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_ENDPOINT_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    deployed_indexes: _containers.RepeatedCompositeFieldContainer[DeployedIndex]
    etag: str
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    network: str
    enable_private_service_connect: bool
    private_service_connect_config: _service_networking_pb2.PrivateServiceConnectConfig
    public_endpoint_enabled: bool
    public_endpoint_domain_name: str
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    satisfies_pzs: bool
    satisfies_pzi: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., deployed_indexes: _Optional[_Iterable[_Union[DeployedIndex, _Mapping]]]=..., etag: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., network: _Optional[str]=..., enable_private_service_connect: bool=..., private_service_connect_config: _Optional[_Union[_service_networking_pb2.PrivateServiceConnectConfig, _Mapping]]=..., public_endpoint_enabled: bool=..., public_endpoint_domain_name: _Optional[str]=..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]]=..., satisfies_pzs: bool=..., satisfies_pzi: bool=...) -> None:
        ...

class DeployedIndex(_message.Message):
    __slots__ = ('id', 'index', 'display_name', 'create_time', 'private_endpoints', 'index_sync_time', 'automatic_resources', 'dedicated_resources', 'enable_access_logging', 'deployed_index_auth_config', 'reserved_ip_ranges', 'deployment_group', 'psc_automation_configs')
    ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    INDEX_SYNC_TIME_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    DEDICATED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ACCESS_LOGGING_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_INDEX_AUTH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESERVED_IP_RANGES_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_GROUP_FIELD_NUMBER: _ClassVar[int]
    PSC_AUTOMATION_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    index: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    private_endpoints: IndexPrivateEndpoints
    index_sync_time: _timestamp_pb2.Timestamp
    automatic_resources: _machine_resources_pb2.AutomaticResources
    dedicated_resources: _machine_resources_pb2.DedicatedResources
    enable_access_logging: bool
    deployed_index_auth_config: DeployedIndexAuthConfig
    reserved_ip_ranges: _containers.RepeatedScalarFieldContainer[str]
    deployment_group: str
    psc_automation_configs: _containers.RepeatedCompositeFieldContainer[_service_networking_pb2.PSCAutomationConfig]

    def __init__(self, id: _Optional[str]=..., index: _Optional[str]=..., display_name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., private_endpoints: _Optional[_Union[IndexPrivateEndpoints, _Mapping]]=..., index_sync_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., automatic_resources: _Optional[_Union[_machine_resources_pb2.AutomaticResources, _Mapping]]=..., dedicated_resources: _Optional[_Union[_machine_resources_pb2.DedicatedResources, _Mapping]]=..., enable_access_logging: bool=..., deployed_index_auth_config: _Optional[_Union[DeployedIndexAuthConfig, _Mapping]]=..., reserved_ip_ranges: _Optional[_Iterable[str]]=..., deployment_group: _Optional[str]=..., psc_automation_configs: _Optional[_Iterable[_Union[_service_networking_pb2.PSCAutomationConfig, _Mapping]]]=...) -> None:
        ...

class DeployedIndexAuthConfig(_message.Message):
    __slots__ = ('auth_provider',)

    class AuthProvider(_message.Message):
        __slots__ = ('audiences', 'allowed_issuers')
        AUDIENCES_FIELD_NUMBER: _ClassVar[int]
        ALLOWED_ISSUERS_FIELD_NUMBER: _ClassVar[int]
        audiences: _containers.RepeatedScalarFieldContainer[str]
        allowed_issuers: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, audiences: _Optional[_Iterable[str]]=..., allowed_issuers: _Optional[_Iterable[str]]=...) -> None:
            ...
    AUTH_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    auth_provider: DeployedIndexAuthConfig.AuthProvider

    def __init__(self, auth_provider: _Optional[_Union[DeployedIndexAuthConfig.AuthProvider, _Mapping]]=...) -> None:
        ...

class IndexPrivateEndpoints(_message.Message):
    __slots__ = ('match_grpc_address', 'service_attachment', 'psc_automated_endpoints')
    MATCH_GRPC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    PSC_AUTOMATED_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    match_grpc_address: str
    service_attachment: str
    psc_automated_endpoints: _containers.RepeatedCompositeFieldContainer[_service_networking_pb2.PscAutomatedEndpoints]

    def __init__(self, match_grpc_address: _Optional[str]=..., service_attachment: _Optional[str]=..., psc_automated_endpoints: _Optional[_Iterable[_Union[_service_networking_pb2.PscAutomatedEndpoints, _Mapping]]]=...) -> None:
        ...