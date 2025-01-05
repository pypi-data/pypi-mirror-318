from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataFiles(_message.Message):
    __slots__ = ('data_files',)
    DATA_FILES_FIELD_NUMBER: _ClassVar[int]
    data_files: _containers.RepeatedCompositeFieldContainer[DataFile]

    def __init__(self, data_files: _Optional[_Iterable[_Union[DataFile, _Mapping]]]=...) -> None:
        ...

class DataFile(_message.Message):
    __slots__ = ('file_path', 'content_type', 'payload')
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    content_type: str
    payload: bytes

    def __init__(self, file_path: _Optional[str]=..., content_type: _Optional[str]=..., payload: _Optional[bytes]=...) -> None:
        ...