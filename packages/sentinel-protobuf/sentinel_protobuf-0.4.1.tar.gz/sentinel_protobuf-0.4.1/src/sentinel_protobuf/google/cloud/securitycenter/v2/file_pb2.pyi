from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class File(_message.Message):
    __slots__ = ('path', 'size', 'sha256', 'hashed_size', 'partially_hashed', 'contents', 'disk_path')

    class DiskPath(_message.Message):
        __slots__ = ('partition_uuid', 'relative_path')
        PARTITION_UUID_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
        partition_uuid: str
        relative_path: str

        def __init__(self, partition_uuid: _Optional[str]=..., relative_path: _Optional[str]=...) -> None:
            ...
    PATH_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    HASHED_SIZE_FIELD_NUMBER: _ClassVar[int]
    PARTIALLY_HASHED_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    DISK_PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    size: int
    sha256: str
    hashed_size: int
    partially_hashed: bool
    contents: str
    disk_path: File.DiskPath

    def __init__(self, path: _Optional[str]=..., size: _Optional[int]=..., sha256: _Optional[str]=..., hashed_size: _Optional[int]=..., partially_hashed: bool=..., contents: _Optional[str]=..., disk_path: _Optional[_Union[File.DiskPath, _Mapping]]=...) -> None:
        ...