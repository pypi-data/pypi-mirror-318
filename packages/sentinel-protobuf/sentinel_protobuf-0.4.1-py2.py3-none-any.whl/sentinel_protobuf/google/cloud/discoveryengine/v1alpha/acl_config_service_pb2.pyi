from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1alpha import acl_config_pb2 as _acl_config_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetAclConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateAclConfigRequest(_message.Message):
    __slots__ = ('acl_config',)
    ACL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    acl_config: _acl_config_pb2.AclConfig

    def __init__(self, acl_config: _Optional[_Union[_acl_config_pb2.AclConfig, _Mapping]]=...) -> None:
        ...