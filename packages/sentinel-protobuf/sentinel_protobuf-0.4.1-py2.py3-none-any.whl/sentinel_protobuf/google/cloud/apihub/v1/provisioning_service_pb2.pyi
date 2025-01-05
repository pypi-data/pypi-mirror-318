from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.apihub.v1 import common_fields_pb2 as _common_fields_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateApiHubInstanceRequest(_message.Message):
    __slots__ = ('parent', 'api_hub_instance_id', 'api_hub_instance')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    API_HUB_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    API_HUB_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    api_hub_instance_id: str
    api_hub_instance: _common_fields_pb2.ApiHubInstance

    def __init__(self, parent: _Optional[str]=..., api_hub_instance_id: _Optional[str]=..., api_hub_instance: _Optional[_Union[_common_fields_pb2.ApiHubInstance, _Mapping]]=...) -> None:
        ...

class GetApiHubInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class LookupApiHubInstanceRequest(_message.Message):
    __slots__ = ('parent',)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str

    def __init__(self, parent: _Optional[str]=...) -> None:
        ...

class LookupApiHubInstanceResponse(_message.Message):
    __slots__ = ('api_hub_instance',)
    API_HUB_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    api_hub_instance: _common_fields_pb2.ApiHubInstance

    def __init__(self, api_hub_instance: _Optional[_Union[_common_fields_pb2.ApiHubInstance, _Mapping]]=...) -> None:
        ...