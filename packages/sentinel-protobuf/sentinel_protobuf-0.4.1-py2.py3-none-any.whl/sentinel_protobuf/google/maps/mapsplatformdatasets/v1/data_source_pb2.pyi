from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FileFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FILE_FORMAT_UNSPECIFIED: _ClassVar[FileFormat]
    FILE_FORMAT_GEOJSON: _ClassVar[FileFormat]
    FILE_FORMAT_KML: _ClassVar[FileFormat]
    FILE_FORMAT_CSV: _ClassVar[FileFormat]
FILE_FORMAT_UNSPECIFIED: FileFormat
FILE_FORMAT_GEOJSON: FileFormat
FILE_FORMAT_KML: FileFormat
FILE_FORMAT_CSV: FileFormat

class LocalFileSource(_message.Message):
    __slots__ = ('filename', 'file_format')
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    filename: str
    file_format: FileFormat

    def __init__(self, filename: _Optional[str]=..., file_format: _Optional[_Union[FileFormat, str]]=...) -> None:
        ...

class GcsSource(_message.Message):
    __slots__ = ('input_uri', 'file_format')
    INPUT_URI_FIELD_NUMBER: _ClassVar[int]
    FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    input_uri: str
    file_format: FileFormat

    def __init__(self, input_uri: _Optional[str]=..., file_format: _Optional[_Union[FileFormat, str]]=...) -> None:
        ...