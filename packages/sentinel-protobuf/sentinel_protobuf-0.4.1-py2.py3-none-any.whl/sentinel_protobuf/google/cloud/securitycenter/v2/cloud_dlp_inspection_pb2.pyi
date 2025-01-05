from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class CloudDlpInspection(_message.Message):
    __slots__ = ('inspect_job', 'info_type', 'info_type_count', 'full_scan')
    INSPECT_JOB_FIELD_NUMBER: _ClassVar[int]
    INFO_TYPE_FIELD_NUMBER: _ClassVar[int]
    INFO_TYPE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FULL_SCAN_FIELD_NUMBER: _ClassVar[int]
    inspect_job: str
    info_type: str
    info_type_count: int
    full_scan: bool

    def __init__(self, inspect_job: _Optional[str]=..., info_type: _Optional[str]=..., info_type_count: _Optional[int]=..., full_scan: bool=...) -> None:
        ...