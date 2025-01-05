from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class DeployedModelRef(_message.Message):
    __slots__ = ('endpoint', 'deployed_model_id')
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    deployed_model_id: str

    def __init__(self, endpoint: _Optional[str]=..., deployed_model_id: _Optional[str]=...) -> None:
        ...