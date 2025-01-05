from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class IngestDetailsLog(_message.Message):
    __slots__ = ('ingestion_tracking_id', 'content')
    INGESTION_TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ingestion_tracking_id: str
    content: str

    def __init__(self, ingestion_tracking_id: _Optional[str]=..., content: _Optional[str]=...) -> None:
        ...