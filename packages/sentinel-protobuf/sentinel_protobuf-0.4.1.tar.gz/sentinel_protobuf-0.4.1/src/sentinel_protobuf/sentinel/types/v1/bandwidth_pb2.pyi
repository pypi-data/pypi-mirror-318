from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Bandwidth(_message.Message):
    __slots__ = ('upload', 'download')
    UPLOAD_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    upload: str
    download: str

    def __init__(self, upload: _Optional[str]=..., download: _Optional[str]=...) -> None:
        ...