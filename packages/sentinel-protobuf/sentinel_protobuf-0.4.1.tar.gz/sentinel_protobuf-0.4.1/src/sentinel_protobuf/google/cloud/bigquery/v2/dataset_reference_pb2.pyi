from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class DatasetReference(_message.Message):
    __slots__ = ('dataset_id', 'project_id')
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    project_id: str

    def __init__(self, dataset_id: _Optional[str]=..., project_id: _Optional[str]=...) -> None:
        ...