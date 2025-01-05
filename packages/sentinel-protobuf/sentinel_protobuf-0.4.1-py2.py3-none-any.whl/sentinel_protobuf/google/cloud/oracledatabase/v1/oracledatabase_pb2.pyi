from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.oracledatabase.v1 import autonomous_database_pb2 as _autonomous_database_pb2
from google.cloud.oracledatabase.v1 import autonomous_database_character_set_pb2 as _autonomous_database_character_set_pb2
from google.cloud.oracledatabase.v1 import autonomous_db_backup_pb2 as _autonomous_db_backup_pb2
from google.cloud.oracledatabase.v1 import autonomous_db_version_pb2 as _autonomous_db_version_pb2
from google.cloud.oracledatabase.v1 import db_node_pb2 as _db_node_pb2
from google.cloud.oracledatabase.v1 import db_server_pb2 as _db_server_pb2
from google.cloud.oracledatabase.v1 import db_system_shape_pb2 as _db_system_shape_pb2
from google.cloud.oracledatabase.v1 import entitlement_pb2 as _entitlement_pb2
from google.cloud.oracledatabase.v1 import exadata_infra_pb2 as _exadata_infra_pb2
from google.cloud.oracledatabase.v1 import gi_version_pb2 as _gi_version_pb2
from google.cloud.oracledatabase.v1 import vm_cluster_pb2 as _vm_cluster_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListCloudExadataInfrastructuresRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListCloudExadataInfrastructuresResponse(_message.Message):
    __slots__ = ("cloud_exadata_infrastructures", "next_page_token")
    CLOUD_EXADATA_INFRASTRUCTURES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    cloud_exadata_infrastructures: _containers.RepeatedCompositeFieldContainer[_exadata_infra_pb2.CloudExadataInfrastructure]
    next_page_token: str
    def __init__(self, cloud_exadata_infrastructures: _Optional[_Iterable[_Union[_exadata_infra_pb2.CloudExadataInfrastructure, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetCloudExadataInfrastructureRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateCloudExadataInfrastructureRequest(_message.Message):
    __slots__ = ("parent", "cloud_exadata_infrastructure_id", "cloud_exadata_infrastructure", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_EXADATA_INFRASTRUCTURE_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_EXADATA_INFRASTRUCTURE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    cloud_exadata_infrastructure_id: str
    cloud_exadata_infrastructure: _exadata_infra_pb2.CloudExadataInfrastructure
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., cloud_exadata_infrastructure_id: _Optional[str] = ..., cloud_exadata_infrastructure: _Optional[_Union[_exadata_infra_pb2.CloudExadataInfrastructure, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteCloudExadataInfrastructureRequest(_message.Message):
    __slots__ = ("name", "request_id", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., force: bool = ...) -> None: ...

class ListCloudVmClustersRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListCloudVmClustersResponse(_message.Message):
    __slots__ = ("cloud_vm_clusters", "next_page_token")
    CLOUD_VM_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    cloud_vm_clusters: _containers.RepeatedCompositeFieldContainer[_vm_cluster_pb2.CloudVmCluster]
    next_page_token: str
    def __init__(self, cloud_vm_clusters: _Optional[_Iterable[_Union[_vm_cluster_pb2.CloudVmCluster, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetCloudVmClusterRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateCloudVmClusterRequest(_message.Message):
    __slots__ = ("parent", "cloud_vm_cluster_id", "cloud_vm_cluster", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_VM_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_VM_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    cloud_vm_cluster_id: str
    cloud_vm_cluster: _vm_cluster_pb2.CloudVmCluster
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., cloud_vm_cluster_id: _Optional[str] = ..., cloud_vm_cluster: _Optional[_Union[_vm_cluster_pb2.CloudVmCluster, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteCloudVmClusterRequest(_message.Message):
    __slots__ = ("name", "request_id", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., force: bool = ...) -> None: ...

class ListEntitlementsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListEntitlementsResponse(_message.Message):
    __slots__ = ("entitlements", "next_page_token")
    ENTITLEMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    entitlements: _containers.RepeatedCompositeFieldContainer[_entitlement_pb2.Entitlement]
    next_page_token: str
    def __init__(self, entitlements: _Optional[_Iterable[_Union[_entitlement_pb2.Entitlement, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListDbServersRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListDbServersResponse(_message.Message):
    __slots__ = ("db_servers", "next_page_token")
    DB_SERVERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    db_servers: _containers.RepeatedCompositeFieldContainer[_db_server_pb2.DbServer]
    next_page_token: str
    def __init__(self, db_servers: _Optional[_Iterable[_Union[_db_server_pb2.DbServer, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListDbNodesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListDbNodesResponse(_message.Message):
    __slots__ = ("db_nodes", "next_page_token")
    DB_NODES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    db_nodes: _containers.RepeatedCompositeFieldContainer[_db_node_pb2.DbNode]
    next_page_token: str
    def __init__(self, db_nodes: _Optional[_Iterable[_Union[_db_node_pb2.DbNode, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListGiVersionsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListGiVersionsResponse(_message.Message):
    __slots__ = ("gi_versions", "next_page_token")
    GI_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    gi_versions: _containers.RepeatedCompositeFieldContainer[_gi_version_pb2.GiVersion]
    next_page_token: str
    def __init__(self, gi_versions: _Optional[_Iterable[_Union[_gi_version_pb2.GiVersion, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListDbSystemShapesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListDbSystemShapesResponse(_message.Message):
    __slots__ = ("db_system_shapes", "next_page_token")
    DB_SYSTEM_SHAPES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    db_system_shapes: _containers.RepeatedCompositeFieldContainer[_db_system_shape_pb2.DbSystemShape]
    next_page_token: str
    def __init__(self, db_system_shapes: _Optional[_Iterable[_Union[_db_system_shape_pb2.DbSystemShape, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class OperationMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "target", "verb", "status_message", "requested_cancellation", "api_version", "percent_complete")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    PERCENT_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str
    percent_complete: float
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., target: _Optional[str] = ..., verb: _Optional[str] = ..., status_message: _Optional[str] = ..., requested_cancellation: bool = ..., api_version: _Optional[str] = ..., percent_complete: _Optional[float] = ...) -> None: ...

class ListAutonomousDatabasesRequest(_message.Message):
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

class ListAutonomousDatabasesResponse(_message.Message):
    __slots__ = ("autonomous_databases", "next_page_token")
    AUTONOMOUS_DATABASES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    autonomous_databases: _containers.RepeatedCompositeFieldContainer[_autonomous_database_pb2.AutonomousDatabase]
    next_page_token: str
    def __init__(self, autonomous_databases: _Optional[_Iterable[_Union[_autonomous_database_pb2.AutonomousDatabase, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetAutonomousDatabaseRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateAutonomousDatabaseRequest(_message.Message):
    __slots__ = ("parent", "autonomous_database_id", "autonomous_database", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    AUTONOMOUS_DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    AUTONOMOUS_DATABASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    autonomous_database_id: str
    autonomous_database: _autonomous_database_pb2.AutonomousDatabase
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., autonomous_database_id: _Optional[str] = ..., autonomous_database: _Optional[_Union[_autonomous_database_pb2.AutonomousDatabase, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteAutonomousDatabaseRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class RestoreAutonomousDatabaseRequest(_message.Message):
    __slots__ = ("name", "restore_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESTORE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    restore_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., restore_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GenerateAutonomousDatabaseWalletRequest(_message.Message):
    __slots__ = ("name", "type", "is_regional", "password")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_REGIONAL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _autonomous_database_pb2.GenerateType
    is_regional: bool
    password: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_autonomous_database_pb2.GenerateType, str]] = ..., is_regional: bool = ..., password: _Optional[str] = ...) -> None: ...

class GenerateAutonomousDatabaseWalletResponse(_message.Message):
    __slots__ = ("archive_content",)
    ARCHIVE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    archive_content: bytes
    def __init__(self, archive_content: _Optional[bytes] = ...) -> None: ...

class ListAutonomousDbVersionsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAutonomousDbVersionsResponse(_message.Message):
    __slots__ = ("autonomous_db_versions", "next_page_token")
    AUTONOMOUS_DB_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    autonomous_db_versions: _containers.RepeatedCompositeFieldContainer[_autonomous_db_version_pb2.AutonomousDbVersion]
    next_page_token: str
    def __init__(self, autonomous_db_versions: _Optional[_Iterable[_Union[_autonomous_db_version_pb2.AutonomousDbVersion, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListAutonomousDatabaseCharacterSetsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListAutonomousDatabaseCharacterSetsResponse(_message.Message):
    __slots__ = ("autonomous_database_character_sets", "next_page_token")
    AUTONOMOUS_DATABASE_CHARACTER_SETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    autonomous_database_character_sets: _containers.RepeatedCompositeFieldContainer[_autonomous_database_character_set_pb2.AutonomousDatabaseCharacterSet]
    next_page_token: str
    def __init__(self, autonomous_database_character_sets: _Optional[_Iterable[_Union[_autonomous_database_character_set_pb2.AutonomousDatabaseCharacterSet, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListAutonomousDatabaseBackupsRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAutonomousDatabaseBackupsResponse(_message.Message):
    __slots__ = ("autonomous_database_backups", "next_page_token")
    AUTONOMOUS_DATABASE_BACKUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    autonomous_database_backups: _containers.RepeatedCompositeFieldContainer[_autonomous_db_backup_pb2.AutonomousDatabaseBackup]
    next_page_token: str
    def __init__(self, autonomous_database_backups: _Optional[_Iterable[_Union[_autonomous_db_backup_pb2.AutonomousDatabaseBackup, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
