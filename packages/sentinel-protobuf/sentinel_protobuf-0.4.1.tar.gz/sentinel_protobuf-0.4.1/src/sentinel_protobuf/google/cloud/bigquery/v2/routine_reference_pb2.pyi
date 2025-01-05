from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class RoutineReference(_message.Message):
    __slots__ = ('project_id', 'dataset_id', 'routine_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTINE_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    routine_id: str

    def __init__(self, project_id: _Optional[str]=..., dataset_id: _Optional[str]=..., routine_id: _Optional[str]=...) -> None:
        ...