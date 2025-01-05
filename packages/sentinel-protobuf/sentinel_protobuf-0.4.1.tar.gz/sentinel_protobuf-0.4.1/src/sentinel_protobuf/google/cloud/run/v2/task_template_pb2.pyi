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

class TaskTemplate(_message.Message):
    __slots__ = ("containers", "volumes", "max_retries", "timeout", "service_account", "execution_environment", "encryption_key", "vpc_access")
    CONTAINERS_FIELD_NUMBER: _ClassVar[int]
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    VPC_ACCESS_FIELD_NUMBER: _ClassVar[int]
    containers: _containers.RepeatedCompositeFieldContainer[_min_pb2.Container]
    volumes: _containers.RepeatedCompositeFieldContainer[_min_pb2.Volume]
    max_retries: int
    timeout: _duration_pb2.Duration
    service_account: str
    execution_environment: _vendor_settings_pb2.ExecutionEnvironment
    encryption_key: str
    vpc_access: _vendor_settings_pb2.VpcAccess
    def __init__(self, containers: _Optional[_Iterable[_Union[_min_pb2.Container, _Mapping]]] = ..., volumes: _Optional[_Iterable[_Union[_min_pb2.Volume, _Mapping]]] = ..., max_retries: _Optional[int] = ..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., service_account: _Optional[str] = ..., execution_environment: _Optional[_Union[_vendor_settings_pb2.ExecutionEnvironment, str]] = ..., encryption_key: _Optional[str] = ..., vpc_access: _Optional[_Union[_vendor_settings_pb2.VpcAccess, _Mapping]] = ...) -> None: ...
