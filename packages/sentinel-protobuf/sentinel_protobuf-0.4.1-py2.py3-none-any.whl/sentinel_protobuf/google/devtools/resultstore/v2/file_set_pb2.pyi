from google.api import resource_pb2 as _resource_pb2
from google.devtools.resultstore.v2 import file_pb2 as _file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FileSet(_message.Message):
    __slots__ = ('name', 'id', 'file_sets', 'files')

    class Id(_message.Message):
        __slots__ = ('invocation_id', 'file_set_id')
        INVOCATION_ID_FIELD_NUMBER: _ClassVar[int]
        FILE_SET_ID_FIELD_NUMBER: _ClassVar[int]
        invocation_id: str
        file_set_id: str

        def __init__(self, invocation_id: _Optional[str]=..., file_set_id: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FILE_SETS_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: FileSet.Id
    file_sets: _containers.RepeatedScalarFieldContainer[str]
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]

    def __init__(self, name: _Optional[str]=..., id: _Optional[_Union[FileSet.Id, _Mapping]]=..., file_sets: _Optional[_Iterable[str]]=..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]]=...) -> None:
        ...