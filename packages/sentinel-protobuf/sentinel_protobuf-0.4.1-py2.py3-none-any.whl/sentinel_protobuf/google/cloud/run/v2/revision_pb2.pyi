from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import launch_stage_pb2 as _launch_stage_pb2
from google.api import resource_pb2 as _resource_pb2
from google.api import routing_pb2 as _routing_pb2
from google.cloud.run.v2 import condition_pb2 as _condition_pb2
from google.cloud.run.v2.k8s import min_pb2 as _min_pb2
from google.cloud.run.v2 import status_pb2 as _status_pb2
from google.cloud.run.v2 import vendor_settings_pb2 as _vendor_settings_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetRevisionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListRevisionsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "show_deleted")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    show_deleted: bool
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., show_deleted: bool = ...) -> None: ...

class ListRevisionsResponse(_message.Message):
    __slots__ = ("revisions", "next_page_token")
    REVISIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    revisions: _containers.RepeatedCompositeFieldContainer[Revision]
    next_page_token: str
    def __init__(self, revisions: _Optional[_Iterable[_Union[Revision, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteRevisionRequest(_message.Message):
    __slots__ = ("name", "validate_only", "etag")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    etag: str
    def __init__(self, name: _Optional[str] = ..., validate_only: bool = ..., etag: _Optional[str] = ...) -> None: ...

class Revision(_message.Message):
    __slots__ = ("name", "uid", "generation", "labels", "annotations", "create_time", "update_time", "delete_time", "expire_time", "launch_stage", "service", "scaling", "vpc_access", "max_instance_request_concurrency", "timeout", "service_account", "containers", "volumes", "execution_environment", "encryption_key", "service_mesh", "encryption_key_revocation_action", "encryption_key_shutdown_duration", "reconciling", "conditions", "observed_generation", "log_uri", "satisfies_pzs", "session_affinity", "scaling_status", "node_selector", "etag")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_STAGE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SCALING_FIELD_NUMBER: _ClassVar[int]
    VPC_ACCESS_FIELD_NUMBER: _ClassVar[int]
    MAX_INSTANCE_REQUEST_CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CONTAINERS_FIELD_NUMBER: _ClassVar[int]
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    SERVICE_MESH_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_REVOCATION_ACTION_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_SHUTDOWN_DURATION_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_GENERATION_FIELD_NUMBER: _ClassVar[int]
    LOG_URI_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SESSION_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    SCALING_STATUS_FIELD_NUMBER: _ClassVar[int]
    NODE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    generation: int
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    launch_stage: _launch_stage_pb2.LaunchStage
    service: str
    scaling: _vendor_settings_pb2.RevisionScaling
    vpc_access: _vendor_settings_pb2.VpcAccess
    max_instance_request_concurrency: int
    timeout: _duration_pb2.Duration
    service_account: str
    containers: _containers.RepeatedCompositeFieldContainer[_min_pb2.Container]
    volumes: _containers.RepeatedCompositeFieldContainer[_min_pb2.Volume]
    execution_environment: _vendor_settings_pb2.ExecutionEnvironment
    encryption_key: str
    service_mesh: _vendor_settings_pb2.ServiceMesh
    encryption_key_revocation_action: _vendor_settings_pb2.EncryptionKeyRevocationAction
    encryption_key_shutdown_duration: _duration_pb2.Duration
    reconciling: bool
    conditions: _containers.RepeatedCompositeFieldContainer[_condition_pb2.Condition]
    observed_generation: int
    log_uri: str
    satisfies_pzs: bool
    session_affinity: bool
    scaling_status: _status_pb2.RevisionScalingStatus
    node_selector: _vendor_settings_pb2.NodeSelector
    etag: str
    def __init__(self, name: _Optional[str] = ..., uid: _Optional[str] = ..., generation: _Optional[int] = ..., labels: _Optional[_Mapping[str, str]] = ..., annotations: _Optional[_Mapping[str, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., launch_stage: _Optional[_Union[_launch_stage_pb2.LaunchStage, str]] = ..., service: _Optional[str] = ..., scaling: _Optional[_Union[_vendor_settings_pb2.RevisionScaling, _Mapping]] = ..., vpc_access: _Optional[_Union[_vendor_settings_pb2.VpcAccess, _Mapping]] = ..., max_instance_request_concurrency: _Optional[int] = ..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., service_account: _Optional[str] = ..., containers: _Optional[_Iterable[_Union[_min_pb2.Container, _Mapping]]] = ..., volumes: _Optional[_Iterable[_Union[_min_pb2.Volume, _Mapping]]] = ..., execution_environment: _Optional[_Union[_vendor_settings_pb2.ExecutionEnvironment, str]] = ..., encryption_key: _Optional[str] = ..., service_mesh: _Optional[_Union[_vendor_settings_pb2.ServiceMesh, _Mapping]] = ..., encryption_key_revocation_action: _Optional[_Union[_vendor_settings_pb2.EncryptionKeyRevocationAction, str]] = ..., encryption_key_shutdown_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., reconciling: bool = ..., conditions: _Optional[_Iterable[_Union[_condition_pb2.Condition, _Mapping]]] = ..., observed_generation: _Optional[int] = ..., log_uri: _Optional[str] = ..., satisfies_pzs: bool = ..., session_affinity: bool = ..., scaling_status: _Optional[_Union[_status_pb2.RevisionScalingStatus, _Mapping]] = ..., node_selector: _Optional[_Union[_vendor_settings_pb2.NodeSelector, _Mapping]] = ..., etag: _Optional[str] = ...) -> None: ...
