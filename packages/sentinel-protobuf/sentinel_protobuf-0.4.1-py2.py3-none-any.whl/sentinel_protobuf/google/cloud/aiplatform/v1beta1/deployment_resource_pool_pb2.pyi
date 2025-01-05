from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1beta1 import machine_resources_pb2 as _machine_resources_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DeploymentResourcePool(_message.Message):
    __slots__ = ('name', 'dedicated_resources', 'encryption_spec', 'service_account', 'disable_container_logging', 'create_time', 'satisfies_pzs', 'satisfies_pzi')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEDICATED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    DISABLE_CONTAINER_LOGGING_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    name: str
    dedicated_resources: _machine_resources_pb2.DedicatedResources
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    service_account: str
    disable_container_logging: bool
    create_time: _timestamp_pb2.Timestamp
    satisfies_pzs: bool
    satisfies_pzi: bool

    def __init__(self, name: _Optional[str]=..., dedicated_resources: _Optional[_Union[_machine_resources_pb2.DedicatedResources, _Mapping]]=..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]]=..., service_account: _Optional[str]=..., disable_container_logging: bool=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., satisfies_pzs: bool=..., satisfies_pzi: bool=...) -> None:
        ...