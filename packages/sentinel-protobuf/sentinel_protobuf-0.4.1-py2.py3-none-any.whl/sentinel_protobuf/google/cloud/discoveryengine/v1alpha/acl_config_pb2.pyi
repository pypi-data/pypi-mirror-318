from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1alpha import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AclConfig(_message.Message):
    __slots__ = ('name', 'idp_config')
    NAME_FIELD_NUMBER: _ClassVar[int]
    IDP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    idp_config: _common_pb2.IdpConfig

    def __init__(self, name: _Optional[str]=..., idp_config: _Optional[_Union[_common_pb2.IdpConfig, _Mapping]]=...) -> None:
        ...