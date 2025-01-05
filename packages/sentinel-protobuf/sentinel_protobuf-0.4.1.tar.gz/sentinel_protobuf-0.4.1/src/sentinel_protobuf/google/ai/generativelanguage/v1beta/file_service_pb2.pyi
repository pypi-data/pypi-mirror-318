from google.ai.generativelanguage.v1beta import file_pb2 as _file_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileRequest(_message.Message):
    __slots__ = ('file',)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: _file_pb2.File

    def __init__(self, file: _Optional[_Union[_file_pb2.File, _Mapping]]=...) -> None:
        ...

class CreateFileResponse(_message.Message):
    __slots__ = ('file',)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: _file_pb2.File

    def __init__(self, file: _Optional[_Union[_file_pb2.File, _Mapping]]=...) -> None:
        ...

class ListFilesRequest(_message.Message):
    __slots__ = ('page_size', 'page_token')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListFilesResponse(_message.Message):
    __slots__ = ('files', 'next_page_token')
    FILES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    next_page_token: str

    def __init__(self, files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetFileRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteFileRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...