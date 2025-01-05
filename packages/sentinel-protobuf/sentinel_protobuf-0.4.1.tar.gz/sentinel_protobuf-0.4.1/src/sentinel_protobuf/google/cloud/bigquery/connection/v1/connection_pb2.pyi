from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateConnectionRequest(_message.Message):
    __slots__ = ('parent', 'connection_id', 'connection')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    connection_id: str
    connection: Connection

    def __init__(self, parent: _Optional[str]=..., connection_id: _Optional[str]=..., connection: _Optional[_Union[Connection, _Mapping]]=...) -> None:
        ...

class GetConnectionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListConnectionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListConnectionsResponse(_message.Message):
    __slots__ = ('next_page_token', 'connections')
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    next_page_token: str
    connections: _containers.RepeatedCompositeFieldContainer[Connection]

    def __init__(self, next_page_token: _Optional[str]=..., connections: _Optional[_Iterable[_Union[Connection, _Mapping]]]=...) -> None:
        ...

class UpdateConnectionRequest(_message.Message):
    __slots__ = ('name', 'connection', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    connection: Connection
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., connection: _Optional[_Union[Connection, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteConnectionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class Connection(_message.Message):
    __slots__ = ('name', 'friendly_name', 'description', 'cloud_sql', 'aws', 'azure', 'cloud_spanner', 'cloud_resource', 'spark', 'salesforce_data_cloud', 'creation_time', 'last_modified_time', 'has_credential')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SQL_FIELD_NUMBER: _ClassVar[int]
    AWS_FIELD_NUMBER: _ClassVar[int]
    AZURE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SPANNER_FIELD_NUMBER: _ClassVar[int]
    CLOUD_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    SPARK_FIELD_NUMBER: _ClassVar[int]
    SALESFORCE_DATA_CLOUD_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    HAS_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    friendly_name: str
    description: str
    cloud_sql: CloudSqlProperties
    aws: AwsProperties
    azure: AzureProperties
    cloud_spanner: CloudSpannerProperties
    cloud_resource: CloudResourceProperties
    spark: SparkProperties
    salesforce_data_cloud: SalesforceDataCloudProperties
    creation_time: int
    last_modified_time: int
    has_credential: bool

    def __init__(self, name: _Optional[str]=..., friendly_name: _Optional[str]=..., description: _Optional[str]=..., cloud_sql: _Optional[_Union[CloudSqlProperties, _Mapping]]=..., aws: _Optional[_Union[AwsProperties, _Mapping]]=..., azure: _Optional[_Union[AzureProperties, _Mapping]]=..., cloud_spanner: _Optional[_Union[CloudSpannerProperties, _Mapping]]=..., cloud_resource: _Optional[_Union[CloudResourceProperties, _Mapping]]=..., spark: _Optional[_Union[SparkProperties, _Mapping]]=..., salesforce_data_cloud: _Optional[_Union[SalesforceDataCloudProperties, _Mapping]]=..., creation_time: _Optional[int]=..., last_modified_time: _Optional[int]=..., has_credential: bool=...) -> None:
        ...

class CloudSqlProperties(_message.Message):
    __slots__ = ('instance_id', 'database', 'type', 'credential', 'service_account_id')

    class DatabaseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATABASE_TYPE_UNSPECIFIED: _ClassVar[CloudSqlProperties.DatabaseType]
        POSTGRES: _ClassVar[CloudSqlProperties.DatabaseType]
        MYSQL: _ClassVar[CloudSqlProperties.DatabaseType]
    DATABASE_TYPE_UNSPECIFIED: CloudSqlProperties.DatabaseType
    POSTGRES: CloudSqlProperties.DatabaseType
    MYSQL: CloudSqlProperties.DatabaseType
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    database: str
    type: CloudSqlProperties.DatabaseType
    credential: CloudSqlCredential
    service_account_id: str

    def __init__(self, instance_id: _Optional[str]=..., database: _Optional[str]=..., type: _Optional[_Union[CloudSqlProperties.DatabaseType, str]]=..., credential: _Optional[_Union[CloudSqlCredential, _Mapping]]=..., service_account_id: _Optional[str]=...) -> None:
        ...

class CloudSqlCredential(_message.Message):
    __slots__ = ('username', 'password')
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str

    def __init__(self, username: _Optional[str]=..., password: _Optional[str]=...) -> None:
        ...

class CloudSpannerProperties(_message.Message):
    __slots__ = ('database', 'use_parallelism', 'max_parallelism', 'use_serverless_analytics', 'use_data_boost', 'database_role')
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    USE_PARALLELISM_FIELD_NUMBER: _ClassVar[int]
    MAX_PARALLELISM_FIELD_NUMBER: _ClassVar[int]
    USE_SERVERLESS_ANALYTICS_FIELD_NUMBER: _ClassVar[int]
    USE_DATA_BOOST_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ROLE_FIELD_NUMBER: _ClassVar[int]
    database: str
    use_parallelism: bool
    max_parallelism: int
    use_serverless_analytics: bool
    use_data_boost: bool
    database_role: str

    def __init__(self, database: _Optional[str]=..., use_parallelism: bool=..., max_parallelism: _Optional[int]=..., use_serverless_analytics: bool=..., use_data_boost: bool=..., database_role: _Optional[str]=...) -> None:
        ...

class AwsProperties(_message.Message):
    __slots__ = ('cross_account_role', 'access_role')
    CROSS_ACCOUNT_ROLE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_ROLE_FIELD_NUMBER: _ClassVar[int]
    cross_account_role: AwsCrossAccountRole
    access_role: AwsAccessRole

    def __init__(self, cross_account_role: _Optional[_Union[AwsCrossAccountRole, _Mapping]]=..., access_role: _Optional[_Union[AwsAccessRole, _Mapping]]=...) -> None:
        ...

class AwsCrossAccountRole(_message.Message):
    __slots__ = ('iam_role_id', 'iam_user_id', 'external_id')
    IAM_ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    IAM_USER_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    iam_role_id: str
    iam_user_id: str
    external_id: str

    def __init__(self, iam_role_id: _Optional[str]=..., iam_user_id: _Optional[str]=..., external_id: _Optional[str]=...) -> None:
        ...

class AwsAccessRole(_message.Message):
    __slots__ = ('iam_role_id', 'identity')
    IAM_ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    iam_role_id: str
    identity: str

    def __init__(self, iam_role_id: _Optional[str]=..., identity: _Optional[str]=...) -> None:
        ...

class AzureProperties(_message.Message):
    __slots__ = ('application', 'client_id', 'object_id', 'customer_tenant_id', 'redirect_uri', 'federated_application_client_id', 'identity')
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    FEDERATED_APPLICATION_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    application: str
    client_id: str
    object_id: str
    customer_tenant_id: str
    redirect_uri: str
    federated_application_client_id: str
    identity: str

    def __init__(self, application: _Optional[str]=..., client_id: _Optional[str]=..., object_id: _Optional[str]=..., customer_tenant_id: _Optional[str]=..., redirect_uri: _Optional[str]=..., federated_application_client_id: _Optional[str]=..., identity: _Optional[str]=...) -> None:
        ...

class CloudResourceProperties(_message.Message):
    __slots__ = ('service_account_id',)
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    service_account_id: str

    def __init__(self, service_account_id: _Optional[str]=...) -> None:
        ...

class MetastoreServiceConfig(_message.Message):
    __slots__ = ('metastore_service',)
    METASTORE_SERVICE_FIELD_NUMBER: _ClassVar[int]
    metastore_service: str

    def __init__(self, metastore_service: _Optional[str]=...) -> None:
        ...

class SparkHistoryServerConfig(_message.Message):
    __slots__ = ('dataproc_cluster',)
    DATAPROC_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    dataproc_cluster: str

    def __init__(self, dataproc_cluster: _Optional[str]=...) -> None:
        ...

class SparkProperties(_message.Message):
    __slots__ = ('service_account_id', 'metastore_service_config', 'spark_history_server_config')
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    METASTORE_SERVICE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SPARK_HISTORY_SERVER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    service_account_id: str
    metastore_service_config: MetastoreServiceConfig
    spark_history_server_config: SparkHistoryServerConfig

    def __init__(self, service_account_id: _Optional[str]=..., metastore_service_config: _Optional[_Union[MetastoreServiceConfig, _Mapping]]=..., spark_history_server_config: _Optional[_Union[SparkHistoryServerConfig, _Mapping]]=...) -> None:
        ...

class SalesforceDataCloudProperties(_message.Message):
    __slots__ = ('instance_uri', 'identity', 'tenant_id')
    INSTANCE_URI_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    instance_uri: str
    identity: str
    tenant_id: str

    def __init__(self, instance_uri: _Optional[str]=..., identity: _Optional[str]=..., tenant_id: _Optional[str]=...) -> None:
        ...