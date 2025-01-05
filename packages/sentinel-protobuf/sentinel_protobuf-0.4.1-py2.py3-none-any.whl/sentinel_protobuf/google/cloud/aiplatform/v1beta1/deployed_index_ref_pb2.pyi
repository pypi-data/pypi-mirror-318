from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class DeployedIndexRef(_message.Message):
    __slots__ = ('index_endpoint', 'deployed_index_id', 'display_name')
    INDEX_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_INDEX_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    index_endpoint: str
    deployed_index_id: str
    display_name: str

    def __init__(self, index_endpoint: _Optional[str]=..., deployed_index_id: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...