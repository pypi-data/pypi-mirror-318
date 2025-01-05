from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1beta import project_pb2 as _project_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ProvisionProjectRequest(_message.Message):
    __slots__ = ('name', 'accept_data_use_terms', 'data_use_terms_version')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_DATA_USE_TERMS_FIELD_NUMBER: _ClassVar[int]
    DATA_USE_TERMS_VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    accept_data_use_terms: bool
    data_use_terms_version: str

    def __init__(self, name: _Optional[str]=..., accept_data_use_terms: bool=..., data_use_terms_version: _Optional[str]=...) -> None:
        ...

class ProvisionProjectMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...