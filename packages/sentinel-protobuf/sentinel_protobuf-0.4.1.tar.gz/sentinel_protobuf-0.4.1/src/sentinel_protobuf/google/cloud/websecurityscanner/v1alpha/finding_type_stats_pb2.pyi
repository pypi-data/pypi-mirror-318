from google.cloud.websecurityscanner.v1alpha import finding_pb2 as _finding_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FindingTypeStats(_message.Message):
    __slots__ = ('finding_type', 'finding_count')
    FINDING_TYPE_FIELD_NUMBER: _ClassVar[int]
    FINDING_COUNT_FIELD_NUMBER: _ClassVar[int]
    finding_type: _finding_pb2.Finding.FindingType
    finding_count: int

    def __init__(self, finding_type: _Optional[_Union[_finding_pb2.Finding.FindingType, str]]=..., finding_count: _Optional[int]=...) -> None:
        ...