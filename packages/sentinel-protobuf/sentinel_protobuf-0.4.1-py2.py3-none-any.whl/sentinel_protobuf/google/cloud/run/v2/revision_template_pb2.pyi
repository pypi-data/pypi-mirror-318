from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.run.v2.k8s import min_pb2 as _min_pb2
from google.cloud.run.v2 import vendor_settings_pb2 as _vendor_settings_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RevisionTemplate(_message.Message):
    __slots__ = ("revision", "labels", "annotations", "scaling", "vpc_access", "timeout", "service_account", "containers", "volumes", "execution_environment", "encryption_key", "max_instance_request_concurrency", "service_mesh", "encryption_key_revocation_action", "encryption_key_shutdown_duration", "session_affinity", "health_check_disabled", "node_selector")
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
    REVISION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    SCALING_FIELD_NUMBER: _ClassVar[int]
    VPC_ACCESS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CONTAINERS_FIELD_NUMBER: _ClassVar[int]
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    MAX_INSTANCE_REQUEST_CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    SERVICE_MESH_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_REVOCATION_ACTION_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_SHUTDOWN_DURATION_FIELD_NUMBER: _ClassVar[int]
    SESSION_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    HEALTH_CHECK_DISABLED_FIELD_NUMBER: _ClassVar[int]
    NODE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    revision: str
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    scaling: _vendor_settings_pb2.RevisionScaling
    vpc_access: _vendor_settings_pb2.VpcAccess
    timeout: _duration_pb2.Duration
    service_account: str
    containers: _containers.RepeatedCompositeFieldContainer[_min_pb2.Container]
    volumes: _containers.RepeatedCompositeFieldContainer[_min_pb2.Volume]
    execution_environment: _vendor_settings_pb2.ExecutionEnvironment
    encryption_key: str
    max_instance_request_concurrency: int
    service_mesh: _vendor_settings_pb2.ServiceMesh
    encryption_key_revocation_action: _vendor_settings_pb2.EncryptionKeyRevocationAction
    encryption_key_shutdown_duration: _duration_pb2.Duration
    session_affinity: bool
    health_check_disabled: bool
    node_selector: _vendor_settings_pb2.NodeSelector
    def __init__(self, revision: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., annotations: _Optional[_Mapping[str, str]] = ..., scaling: _Optional[_Union[_vendor_settings_pb2.RevisionScaling, _Mapping]] = ..., vpc_access: _Optional[_Union[_vendor_settings_pb2.VpcAccess, _Mapping]] = ..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., service_account: _Optional[str] = ..., containers: _Optional[_Iterable[_Union[_min_pb2.Container, _Mapping]]] = ..., volumes: _Optional[_Iterable[_Union[_min_pb2.Volume, _Mapping]]] = ..., execution_environment: _Optional[_Union[_vendor_settings_pb2.ExecutionEnvironment, str]] = ..., encryption_key: _Optional[str] = ..., max_instance_request_concurrency: _Optional[int] = ..., service_mesh: _Optional[_Union[_vendor_settings_pb2.ServiceMesh, _Mapping]] = ..., encryption_key_revocation_action: _Optional[_Union[_vendor_settings_pb2.EncryptionKeyRevocationAction, str]] = ..., encryption_key_shutdown_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., session_affinity: bool = ..., health_check_disabled: bool = ..., node_selector: _Optional[_Union[_vendor_settings_pb2.NodeSelector, _Mapping]] = ...) -> None: ...
