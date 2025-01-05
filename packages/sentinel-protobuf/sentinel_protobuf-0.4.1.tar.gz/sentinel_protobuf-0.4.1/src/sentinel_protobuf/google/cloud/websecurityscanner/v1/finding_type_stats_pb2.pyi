from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class FindingTypeStats(_message.Message):
    __slots__ = ('finding_type', 'finding_count')
    FINDING_TYPE_FIELD_NUMBER: _ClassVar[int]
    FINDING_COUNT_FIELD_NUMBER: _ClassVar[int]
    finding_type: str
    finding_count: int

    def __init__(self, finding_type: _Optional[str]=..., finding_count: _Optional[int]=...) -> None:
        ...