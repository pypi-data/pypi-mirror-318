from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.security.publicca.v1beta1 import resources_pb2 as _resources_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateExternalAccountKeyRequest(_message.Message):
    __slots__ = ('parent', 'external_account_key')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACCOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    external_account_key: _resources_pb2.ExternalAccountKey

    def __init__(self, parent: _Optional[str]=..., external_account_key: _Optional[_Union[_resources_pb2.ExternalAccountKey, _Mapping]]=...) -> None:
        ...