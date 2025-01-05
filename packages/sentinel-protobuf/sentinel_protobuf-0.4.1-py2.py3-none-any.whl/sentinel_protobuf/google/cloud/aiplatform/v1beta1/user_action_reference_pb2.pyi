from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class UserActionReference(_message.Message):
    __slots__ = ('operation', 'data_labeling_job', 'method')
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    DATA_LABELING_JOB_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    operation: str
    data_labeling_job: str
    method: str

    def __init__(self, operation: _Optional[str]=..., data_labeling_job: _Optional[str]=..., method: _Optional[str]=...) -> None:
        ...