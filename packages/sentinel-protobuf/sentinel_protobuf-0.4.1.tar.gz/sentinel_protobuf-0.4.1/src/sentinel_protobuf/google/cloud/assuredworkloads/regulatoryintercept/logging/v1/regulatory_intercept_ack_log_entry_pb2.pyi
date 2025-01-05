from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class RegulatoryInterceptAckLogEntry(_message.Message):
    __slots__ = ('user_id', 'assured_workload_resource_id')
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ASSURED_WORKLOAD_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    assured_workload_resource_id: str

    def __init__(self, user_id: _Optional[str]=..., assured_workload_resource_id: _Optional[str]=...) -> None:
        ...