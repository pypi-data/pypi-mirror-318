from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.securitycenter.v2 import resource_pb2 as _resource_pb2_1
from google.cloud.securitycenter.v2 import valued_resource_pb2 as _valued_resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Simulation(_message.Message):
    __slots__ = ('name', 'create_time', 'resource_value_configs_metadata', 'cloud_provider')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VALUE_CONFIGS_METADATA_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    resource_value_configs_metadata: _containers.RepeatedCompositeFieldContainer[_valued_resource_pb2.ResourceValueConfigMetadata]
    cloud_provider: _resource_pb2_1.CloudProvider

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., resource_value_configs_metadata: _Optional[_Iterable[_Union[_valued_resource_pb2.ResourceValueConfigMetadata, _Mapping]]]=..., cloud_provider: _Optional[_Union[_resource_pb2_1.CloudProvider, str]]=...) -> None:
        ...