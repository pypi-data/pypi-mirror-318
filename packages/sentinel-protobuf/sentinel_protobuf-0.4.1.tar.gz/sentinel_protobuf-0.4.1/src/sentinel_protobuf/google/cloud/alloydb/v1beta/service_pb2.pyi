from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.alloydb.v1beta import data_model_pb2 as _data_model_pb2
from google.cloud.alloydb.v1beta import resources_pb2 as _resources_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListClustersRequest(_message.Message):
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

class ListClustersResponse(_message.Message):
    __slots__ = ("clusters", "next_page_token", "unreachable")
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    clusters: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Cluster]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, clusters: _Optional[_Iterable[_Union[_resources_pb2.Cluster, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetClusterRequest(_message.Message):
    __slots__ = ("name", "view")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: _resources_pb2.ClusterView
    def __init__(self, name: _Optional[str] = ..., view: _Optional[_Union[_resources_pb2.ClusterView, str]] = ...) -> None: ...

class CreateSecondaryClusterRequest(_message.Message):
    __slots__ = ("parent", "cluster_id", "cluster", "request_id", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    cluster_id: str
    cluster: _resources_pb2.Cluster
    request_id: str
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., cluster_id: _Optional[str] = ..., cluster: _Optional[_Union[_resources_pb2.Cluster, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class CreateClusterRequest(_message.Message):
    __slots__ = ("parent", "cluster_id", "cluster", "request_id", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    cluster_id: str
    cluster: _resources_pb2.Cluster
    request_id: str
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., cluster_id: _Optional[str] = ..., cluster: _Optional[_Union[_resources_pb2.Cluster, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class UpdateClusterRequest(_message.Message):
    __slots__ = ("update_mask", "cluster", "request_id", "validate_only", "allow_missing")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    cluster: _resources_pb2.Cluster
    request_id: str
    validate_only: bool
    allow_missing: bool
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., cluster: _Optional[_Union[_resources_pb2.Cluster, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ..., allow_missing: bool = ...) -> None: ...

class UpgradeClusterRequest(_message.Message):
    __slots__ = ("name", "version", "request_id", "validate_only", "etag")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: _resources_pb2.DatabaseVersion
    request_id: str
    validate_only: bool
    etag: str
    def __init__(self, name: _Optional[str] = ..., version: _Optional[_Union[_resources_pb2.DatabaseVersion, str]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ..., etag: _Optional[str] = ...) -> None: ...

class UpgradeClusterResponse(_message.Message):
    __slots__ = ("status", "message", "cluster_upgrade_details")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[UpgradeClusterResponse.Status]
        NOT_STARTED: _ClassVar[UpgradeClusterResponse.Status]
        IN_PROGRESS: _ClassVar[UpgradeClusterResponse.Status]
        SUCCESS: _ClassVar[UpgradeClusterResponse.Status]
        FAILED: _ClassVar[UpgradeClusterResponse.Status]
        PARTIAL_SUCCESS: _ClassVar[UpgradeClusterResponse.Status]
        CANCEL_IN_PROGRESS: _ClassVar[UpgradeClusterResponse.Status]
        CANCELLED: _ClassVar[UpgradeClusterResponse.Status]
    STATUS_UNSPECIFIED: UpgradeClusterResponse.Status
    NOT_STARTED: UpgradeClusterResponse.Status
    IN_PROGRESS: UpgradeClusterResponse.Status
    SUCCESS: UpgradeClusterResponse.Status
    FAILED: UpgradeClusterResponse.Status
    PARTIAL_SUCCESS: UpgradeClusterResponse.Status
    CANCEL_IN_PROGRESS: UpgradeClusterResponse.Status
    CANCELLED: UpgradeClusterResponse.Status
    class Stage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STAGE_UNSPECIFIED: _ClassVar[UpgradeClusterResponse.Stage]
        ALLOYDB_PRECHECK: _ClassVar[UpgradeClusterResponse.Stage]
        PG_UPGRADE_CHECK: _ClassVar[UpgradeClusterResponse.Stage]
        PREPARE_FOR_UPGRADE: _ClassVar[UpgradeClusterResponse.Stage]
        PRIMARY_INSTANCE_UPGRADE: _ClassVar[UpgradeClusterResponse.Stage]
        READ_POOL_INSTANCES_UPGRADE: _ClassVar[UpgradeClusterResponse.Stage]
        ROLLBACK: _ClassVar[UpgradeClusterResponse.Stage]
        CLEANUP: _ClassVar[UpgradeClusterResponse.Stage]
    STAGE_UNSPECIFIED: UpgradeClusterResponse.Stage
    ALLOYDB_PRECHECK: UpgradeClusterResponse.Stage
    PG_UPGRADE_CHECK: UpgradeClusterResponse.Stage
    PREPARE_FOR_UPGRADE: UpgradeClusterResponse.Stage
    PRIMARY_INSTANCE_UPGRADE: UpgradeClusterResponse.Stage
    READ_POOL_INSTANCES_UPGRADE: UpgradeClusterResponse.Stage
    ROLLBACK: UpgradeClusterResponse.Stage
    CLEANUP: UpgradeClusterResponse.Stage
    class StageInfo(_message.Message):
        __slots__ = ("stage", "status", "logs_url")
        STAGE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        LOGS_URL_FIELD_NUMBER: _ClassVar[int]
        stage: UpgradeClusterResponse.Stage
        status: UpgradeClusterResponse.Status
        logs_url: str
        def __init__(self, stage: _Optional[_Union[UpgradeClusterResponse.Stage, str]] = ..., status: _Optional[_Union[UpgradeClusterResponse.Status, str]] = ..., logs_url: _Optional[str] = ...) -> None: ...
    class InstanceUpgradeDetails(_message.Message):
        __slots__ = ("name", "upgrade_status", "instance_type")
        NAME_FIELD_NUMBER: _ClassVar[int]
        UPGRADE_STATUS_FIELD_NUMBER: _ClassVar[int]
        INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        upgrade_status: UpgradeClusterResponse.Status
        instance_type: _resources_pb2.Instance.InstanceType
        def __init__(self, name: _Optional[str] = ..., upgrade_status: _Optional[_Union[UpgradeClusterResponse.Status, str]] = ..., instance_type: _Optional[_Union[_resources_pb2.Instance.InstanceType, str]] = ...) -> None: ...
    class ClusterUpgradeDetails(_message.Message):
        __slots__ = ("name", "upgrade_status", "cluster_type", "database_version", "stage_info", "instance_upgrade_details")
        NAME_FIELD_NUMBER: _ClassVar[int]
        UPGRADE_STATUS_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_TYPE_FIELD_NUMBER: _ClassVar[int]
        DATABASE_VERSION_FIELD_NUMBER: _ClassVar[int]
        STAGE_INFO_FIELD_NUMBER: _ClassVar[int]
        INSTANCE_UPGRADE_DETAILS_FIELD_NUMBER: _ClassVar[int]
        name: str
        upgrade_status: UpgradeClusterResponse.Status
        cluster_type: _resources_pb2.Cluster.ClusterType
        database_version: _resources_pb2.DatabaseVersion
        stage_info: _containers.RepeatedCompositeFieldContainer[UpgradeClusterResponse.StageInfo]
        instance_upgrade_details: _containers.RepeatedCompositeFieldContainer[UpgradeClusterResponse.InstanceUpgradeDetails]
        def __init__(self, name: _Optional[str] = ..., upgrade_status: _Optional[_Union[UpgradeClusterResponse.Status, str]] = ..., cluster_type: _Optional[_Union[_resources_pb2.Cluster.ClusterType, str]] = ..., database_version: _Optional[_Union[_resources_pb2.DatabaseVersion, str]] = ..., stage_info: _Optional[_Iterable[_Union[UpgradeClusterResponse.StageInfo, _Mapping]]] = ..., instance_upgrade_details: _Optional[_Iterable[_Union[UpgradeClusterResponse.InstanceUpgradeDetails, _Mapping]]] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_UPGRADE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    status: UpgradeClusterResponse.Status
    message: str
    cluster_upgrade_details: _containers.RepeatedCompositeFieldContainer[UpgradeClusterResponse.ClusterUpgradeDetails]
    def __init__(self, status: _Optional[_Union[UpgradeClusterResponse.Status, str]] = ..., message: _Optional[str] = ..., cluster_upgrade_details: _Optional[_Iterable[_Union[UpgradeClusterResponse.ClusterUpgradeDetails, _Mapping]]] = ...) -> None: ...

class DeleteClusterRequest(_message.Message):
    __slots__ = ("name", "request_id", "etag", "validate_only", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    etag: str
    validate_only: bool
    force: bool
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., etag: _Optional[str] = ..., validate_only: bool = ..., force: bool = ...) -> None: ...

class SwitchoverClusterRequest(_message.Message):
    __slots__ = ("name", "request_id", "validate_only")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    validate_only: bool
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class PromoteClusterRequest(_message.Message):
    __slots__ = ("name", "request_id", "etag", "validate_only")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    etag: str
    validate_only: bool
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., etag: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class RestoreClusterRequest(_message.Message):
    __slots__ = ("backup_source", "continuous_backup_source", "parent", "cluster_id", "cluster", "request_id", "validate_only")
    BACKUP_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CONTINUOUS_BACKUP_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    backup_source: _resources_pb2.BackupSource
    continuous_backup_source: _resources_pb2.ContinuousBackupSource
    parent: str
    cluster_id: str
    cluster: _resources_pb2.Cluster
    request_id: str
    validate_only: bool
    def __init__(self, backup_source: _Optional[_Union[_resources_pb2.BackupSource, _Mapping]] = ..., continuous_backup_source: _Optional[_Union[_resources_pb2.ContinuousBackupSource, _Mapping]] = ..., parent: _Optional[str] = ..., cluster_id: _Optional[str] = ..., cluster: _Optional[_Union[_resources_pb2.Cluster, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class ListInstancesRequest(_message.Message):
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

class ListInstancesResponse(_message.Message):
    __slots__ = ("instances", "next_page_token", "unreachable")
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Instance]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, instances: _Optional[_Iterable[_Union[_resources_pb2.Instance, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetInstanceRequest(_message.Message):
    __slots__ = ("name", "view")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: _resources_pb2.InstanceView
    def __init__(self, name: _Optional[str] = ..., view: _Optional[_Union[_resources_pb2.InstanceView, str]] = ...) -> None: ...

class CreateInstanceRequest(_message.Message):
    __slots__ = ("parent", "instance_id", "instance", "request_id", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    instance_id: str
    instance: _resources_pb2.Instance
    request_id: str
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., instance_id: _Optional[str] = ..., instance: _Optional[_Union[_resources_pb2.Instance, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class CreateSecondaryInstanceRequest(_message.Message):
    __slots__ = ("parent", "instance_id", "instance", "request_id", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    instance_id: str
    instance: _resources_pb2.Instance
    request_id: str
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., instance_id: _Optional[str] = ..., instance: _Optional[_Union[_resources_pb2.Instance, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class CreateInstanceRequests(_message.Message):
    __slots__ = ("create_instance_requests",)
    CREATE_INSTANCE_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    create_instance_requests: _containers.RepeatedCompositeFieldContainer[CreateInstanceRequest]
    def __init__(self, create_instance_requests: _Optional[_Iterable[_Union[CreateInstanceRequest, _Mapping]]] = ...) -> None: ...

class BatchCreateInstancesRequest(_message.Message):
    __slots__ = ("parent", "requests", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: CreateInstanceRequests
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., requests: _Optional[_Union[CreateInstanceRequests, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class BatchCreateInstancesResponse(_message.Message):
    __slots__ = ("instances",)
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Instance]
    def __init__(self, instances: _Optional[_Iterable[_Union[_resources_pb2.Instance, _Mapping]]] = ...) -> None: ...

class BatchCreateInstancesMetadata(_message.Message):
    __slots__ = ("instance_targets", "instance_statuses")
    class InstanceStatusesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: BatchCreateInstanceStatus
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[BatchCreateInstanceStatus, _Mapping]] = ...) -> None: ...
    INSTANCE_TARGETS_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_STATUSES_FIELD_NUMBER: _ClassVar[int]
    instance_targets: _containers.RepeatedScalarFieldContainer[str]
    instance_statuses: _containers.MessageMap[str, BatchCreateInstanceStatus]
    def __init__(self, instance_targets: _Optional[_Iterable[str]] = ..., instance_statuses: _Optional[_Mapping[str, BatchCreateInstanceStatus]] = ...) -> None: ...

class BatchCreateInstanceStatus(_message.Message):
    __slots__ = ("state", "error_msg", "error", "type")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[BatchCreateInstanceStatus.State]
        PENDING_CREATE: _ClassVar[BatchCreateInstanceStatus.State]
        READY: _ClassVar[BatchCreateInstanceStatus.State]
        CREATING: _ClassVar[BatchCreateInstanceStatus.State]
        DELETING: _ClassVar[BatchCreateInstanceStatus.State]
        FAILED: _ClassVar[BatchCreateInstanceStatus.State]
        ROLLED_BACK: _ClassVar[BatchCreateInstanceStatus.State]
    STATE_UNSPECIFIED: BatchCreateInstanceStatus.State
    PENDING_CREATE: BatchCreateInstanceStatus.State
    READY: BatchCreateInstanceStatus.State
    CREATING: BatchCreateInstanceStatus.State
    DELETING: BatchCreateInstanceStatus.State
    FAILED: BatchCreateInstanceStatus.State
    ROLLED_BACK: BatchCreateInstanceStatus.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    state: BatchCreateInstanceStatus.State
    error_msg: str
    error: _status_pb2.Status
    type: _resources_pb2.Instance.InstanceType
    def __init__(self, state: _Optional[_Union[BatchCreateInstanceStatus.State, str]] = ..., error_msg: _Optional[str] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., type: _Optional[_Union[_resources_pb2.Instance.InstanceType, str]] = ...) -> None: ...

class UpdateInstanceRequest(_message.Message):
    __slots__ = ("update_mask", "instance", "request_id", "validate_only", "allow_missing")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    instance: _resources_pb2.Instance
    request_id: str
    validate_only: bool
    allow_missing: bool
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., instance: _Optional[_Union[_resources_pb2.Instance, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ..., allow_missing: bool = ...) -> None: ...

class DeleteInstanceRequest(_message.Message):
    __slots__ = ("name", "request_id", "etag", "validate_only")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    etag: str
    validate_only: bool
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., etag: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class FailoverInstanceRequest(_message.Message):
    __slots__ = ("name", "request_id", "validate_only")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    validate_only: bool
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class InjectFaultRequest(_message.Message):
    __slots__ = ("fault_type", "name", "request_id", "validate_only")
    class FaultType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FAULT_TYPE_UNSPECIFIED: _ClassVar[InjectFaultRequest.FaultType]
        STOP_VM: _ClassVar[InjectFaultRequest.FaultType]
    FAULT_TYPE_UNSPECIFIED: InjectFaultRequest.FaultType
    STOP_VM: InjectFaultRequest.FaultType
    FAULT_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    fault_type: InjectFaultRequest.FaultType
    name: str
    request_id: str
    validate_only: bool
    def __init__(self, fault_type: _Optional[_Union[InjectFaultRequest.FaultType, str]] = ..., name: _Optional[str] = ..., request_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class RestartInstanceRequest(_message.Message):
    __slots__ = ("name", "request_id", "validate_only", "node_ids")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    validate_only: bool
    node_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., validate_only: bool = ..., node_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ExecuteSqlRequest(_message.Message):
    __slots__ = ("password", "instance", "database", "user", "sql_statement")
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    SQL_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    password: str
    instance: str
    database: str
    user: str
    sql_statement: str
    def __init__(self, password: _Optional[str] = ..., instance: _Optional[str] = ..., database: _Optional[str] = ..., user: _Optional[str] = ..., sql_statement: _Optional[str] = ...) -> None: ...

class ExecuteSqlResponse(_message.Message):
    __slots__ = ("sql_results", "metadata")
    SQL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    sql_results: _containers.RepeatedCompositeFieldContainer[_data_model_pb2.SqlResult]
    metadata: ExecuteSqlMetadata
    def __init__(self, sql_results: _Optional[_Iterable[_Union[_data_model_pb2.SqlResult, _Mapping]]] = ..., metadata: _Optional[_Union[ExecuteSqlMetadata, _Mapping]] = ...) -> None: ...

class ExecuteSqlMetadata(_message.Message):
    __slots__ = ("message", "partial_result", "sql_statement_execution_duration", "status")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[ExecuteSqlMetadata.Status]
        OK: _ClassVar[ExecuteSqlMetadata.Status]
        PARTIAL: _ClassVar[ExecuteSqlMetadata.Status]
        ERROR: _ClassVar[ExecuteSqlMetadata.Status]
    STATUS_UNSPECIFIED: ExecuteSqlMetadata.Status
    OK: ExecuteSqlMetadata.Status
    PARTIAL: ExecuteSqlMetadata.Status
    ERROR: ExecuteSqlMetadata.Status
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_RESULT_FIELD_NUMBER: _ClassVar[int]
    SQL_STATEMENT_EXECUTION_DURATION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    partial_result: bool
    sql_statement_execution_duration: _duration_pb2.Duration
    status: ExecuteSqlMetadata.Status
    def __init__(self, message: _Optional[str] = ..., partial_result: bool = ..., sql_statement_execution_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., status: _Optional[_Union[ExecuteSqlMetadata.Status, str]] = ...) -> None: ...

class ListBackupsRequest(_message.Message):
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

class ListBackupsResponse(_message.Message):
    __slots__ = ("backups", "next_page_token", "unreachable")
    BACKUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    backups: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Backup]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, backups: _Optional[_Iterable[_Union[_resources_pb2.Backup, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetBackupRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateBackupRequest(_message.Message):
    __slots__ = ("parent", "backup_id", "backup", "request_id", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    backup_id: str
    backup: _resources_pb2.Backup
    request_id: str
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., backup_id: _Optional[str] = ..., backup: _Optional[_Union[_resources_pb2.Backup, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class UpdateBackupRequest(_message.Message):
    __slots__ = ("update_mask", "backup", "request_id", "validate_only", "allow_missing")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    backup: _resources_pb2.Backup
    request_id: str
    validate_only: bool
    allow_missing: bool
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., backup: _Optional[_Union[_resources_pb2.Backup, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ..., allow_missing: bool = ...) -> None: ...

class DeleteBackupRequest(_message.Message):
    __slots__ = ("name", "request_id", "validate_only", "etag")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    validate_only: bool
    etag: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., validate_only: bool = ..., etag: _Optional[str] = ...) -> None: ...

class ListSupportedDatabaseFlagsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListSupportedDatabaseFlagsResponse(_message.Message):
    __slots__ = ("supported_database_flags", "next_page_token")
    SUPPORTED_DATABASE_FLAGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    supported_database_flags: _containers.RepeatedCompositeFieldContainer[_resources_pb2.SupportedDatabaseFlag]
    next_page_token: str
    def __init__(self, supported_database_flags: _Optional[_Iterable[_Union[_resources_pb2.SupportedDatabaseFlag, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GenerateClientCertificateRequest(_message.Message):
    __slots__ = ("parent", "request_id", "pem_csr", "cert_duration", "public_key", "use_metadata_exchange")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PEM_CSR_FIELD_NUMBER: _ClassVar[int]
    CERT_DURATION_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    USE_METADATA_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    request_id: str
    pem_csr: str
    cert_duration: _duration_pb2.Duration
    public_key: str
    use_metadata_exchange: bool
    def __init__(self, parent: _Optional[str] = ..., request_id: _Optional[str] = ..., pem_csr: _Optional[str] = ..., cert_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., public_key: _Optional[str] = ..., use_metadata_exchange: bool = ...) -> None: ...

class GenerateClientCertificateResponse(_message.Message):
    __slots__ = ("pem_certificate", "pem_certificate_chain", "ca_cert")
    PEM_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    PEM_CERTIFICATE_CHAIN_FIELD_NUMBER: _ClassVar[int]
    CA_CERT_FIELD_NUMBER: _ClassVar[int]
    pem_certificate: str
    pem_certificate_chain: _containers.RepeatedScalarFieldContainer[str]
    ca_cert: str
    def __init__(self, pem_certificate: _Optional[str] = ..., pem_certificate_chain: _Optional[_Iterable[str]] = ..., ca_cert: _Optional[str] = ...) -> None: ...

class GetConnectionInfoRequest(_message.Message):
    __slots__ = ("parent", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class OperationMetadata(_message.Message):
    __slots__ = ("batch_create_instances_metadata", "promote_cluster_status", "upgrade_cluster_status", "create_time", "end_time", "target", "verb", "status_message", "requested_cancellation", "api_version")
    BATCH_CREATE_INSTANCES_METADATA_FIELD_NUMBER: _ClassVar[int]
    PROMOTE_CLUSTER_STATUS_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_CLUSTER_STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    batch_create_instances_metadata: BatchCreateInstancesMetadata
    promote_cluster_status: PromoteClusterStatus
    upgrade_cluster_status: UpgradeClusterStatus
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str
    def __init__(self, batch_create_instances_metadata: _Optional[_Union[BatchCreateInstancesMetadata, _Mapping]] = ..., promote_cluster_status: _Optional[_Union[PromoteClusterStatus, _Mapping]] = ..., upgrade_cluster_status: _Optional[_Union[UpgradeClusterStatus, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., target: _Optional[str] = ..., verb: _Optional[str] = ..., status_message: _Optional[str] = ..., requested_cancellation: bool = ..., api_version: _Optional[str] = ...) -> None: ...

class PromoteClusterStatus(_message.Message):
    __slots__ = ("state",)
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PromoteClusterStatus.State]
        PROMOTE_CLUSTER_AVAILABLE_FOR_READ: _ClassVar[PromoteClusterStatus.State]
        PROMOTE_CLUSTER_AVAILABLE_FOR_WRITE: _ClassVar[PromoteClusterStatus.State]
        PROMOTE_CLUSTER_COMPLETED: _ClassVar[PromoteClusterStatus.State]
    STATE_UNSPECIFIED: PromoteClusterStatus.State
    PROMOTE_CLUSTER_AVAILABLE_FOR_READ: PromoteClusterStatus.State
    PROMOTE_CLUSTER_AVAILABLE_FOR_WRITE: PromoteClusterStatus.State
    PROMOTE_CLUSTER_COMPLETED: PromoteClusterStatus.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: PromoteClusterStatus.State
    def __init__(self, state: _Optional[_Union[PromoteClusterStatus.State, str]] = ...) -> None: ...

class UpgradeClusterStatus(_message.Message):
    __slots__ = ("state", "cancellable", "source_version", "target_version", "stages")
    class StageStatus(_message.Message):
        __slots__ = ("read_pool_instances_upgrade", "stage", "state")
        READ_POOL_INSTANCES_UPGRADE_FIELD_NUMBER: _ClassVar[int]
        STAGE_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        read_pool_instances_upgrade: UpgradeClusterStatus.ReadPoolInstancesUpgradeStageStatus
        stage: UpgradeClusterResponse.Stage
        state: UpgradeClusterResponse.Status
        def __init__(self, read_pool_instances_upgrade: _Optional[_Union[UpgradeClusterStatus.ReadPoolInstancesUpgradeStageStatus, _Mapping]] = ..., stage: _Optional[_Union[UpgradeClusterResponse.Stage, str]] = ..., state: _Optional[_Union[UpgradeClusterResponse.Status, str]] = ...) -> None: ...
    class ReadPoolInstancesUpgradeStageStatus(_message.Message):
        __slots__ = ("upgrade_stats",)
        class Stats(_message.Message):
            __slots__ = ("not_started", "ongoing", "success", "failed")
            NOT_STARTED_FIELD_NUMBER: _ClassVar[int]
            ONGOING_FIELD_NUMBER: _ClassVar[int]
            SUCCESS_FIELD_NUMBER: _ClassVar[int]
            FAILED_FIELD_NUMBER: _ClassVar[int]
            not_started: int
            ongoing: int
            success: int
            failed: int
            def __init__(self, not_started: _Optional[int] = ..., ongoing: _Optional[int] = ..., success: _Optional[int] = ..., failed: _Optional[int] = ...) -> None: ...
        UPGRADE_STATS_FIELD_NUMBER: _ClassVar[int]
        upgrade_stats: UpgradeClusterStatus.ReadPoolInstancesUpgradeStageStatus.Stats
        def __init__(self, upgrade_stats: _Optional[_Union[UpgradeClusterStatus.ReadPoolInstancesUpgradeStageStatus.Stats, _Mapping]] = ...) -> None: ...
    STATE_FIELD_NUMBER: _ClassVar[int]
    CANCELLABLE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    TARGET_VERSION_FIELD_NUMBER: _ClassVar[int]
    STAGES_FIELD_NUMBER: _ClassVar[int]
    state: UpgradeClusterResponse.Status
    cancellable: bool
    source_version: _resources_pb2.DatabaseVersion
    target_version: _resources_pb2.DatabaseVersion
    stages: _containers.RepeatedCompositeFieldContainer[UpgradeClusterStatus.StageStatus]
    def __init__(self, state: _Optional[_Union[UpgradeClusterResponse.Status, str]] = ..., cancellable: bool = ..., source_version: _Optional[_Union[_resources_pb2.DatabaseVersion, str]] = ..., target_version: _Optional[_Union[_resources_pb2.DatabaseVersion, str]] = ..., stages: _Optional[_Iterable[_Union[UpgradeClusterStatus.StageStatus, _Mapping]]] = ...) -> None: ...

class ListUsersRequest(_message.Message):
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

class ListUsersResponse(_message.Message):
    __slots__ = ("users", "next_page_token", "unreachable")
    USERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[_resources_pb2.User]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, users: _Optional[_Iterable[_Union[_resources_pb2.User, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ("parent", "user_id", "user", "request_id", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    user_id: str
    user: _resources_pb2.User
    request_id: str
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., user_id: _Optional[str] = ..., user: _Optional[_Union[_resources_pb2.User, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ("update_mask", "user", "request_id", "validate_only", "allow_missing")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    user: _resources_pb2.User
    request_id: str
    validate_only: bool
    allow_missing: bool
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., user: _Optional[_Union[_resources_pb2.User, _Mapping]] = ..., request_id: _Optional[str] = ..., validate_only: bool = ..., allow_missing: bool = ...) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = ("name", "request_id", "validate_only")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    validate_only: bool
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class ListDatabasesRequest(_message.Message):
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

class ListDatabasesResponse(_message.Message):
    __slots__ = ("databases", "next_page_token")
    DATABASES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    databases: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Database]
    next_page_token: str
    def __init__(self, databases: _Optional[_Iterable[_Union[_resources_pb2.Database, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
