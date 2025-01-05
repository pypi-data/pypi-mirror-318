from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class File(_message.Message):
    __slots__ = ('uid', 'uri', 'length', 'content_type', 'archive_entry', 'content_viewer', 'hidden', 'description', 'digest', 'hash_type')

    class HashType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HASH_TYPE_UNSPECIFIED: _ClassVar[File.HashType]
        MD5: _ClassVar[File.HashType]
        SHA1: _ClassVar[File.HashType]
        SHA256: _ClassVar[File.HashType]
    HASH_TYPE_UNSPECIFIED: File.HashType
    MD5: File.HashType
    SHA1: File.HashType
    SHA256: File.HashType
    UID_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_ENTRY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_VIEWER_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    HASH_TYPE_FIELD_NUMBER: _ClassVar[int]
    uid: str
    uri: str
    length: _wrappers_pb2.Int64Value
    content_type: str
    archive_entry: ArchiveEntry
    content_viewer: str
    hidden: bool
    description: str
    digest: str
    hash_type: File.HashType

    def __init__(self, uid: _Optional[str]=..., uri: _Optional[str]=..., length: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., content_type: _Optional[str]=..., archive_entry: _Optional[_Union[ArchiveEntry, _Mapping]]=..., content_viewer: _Optional[str]=..., hidden: bool=..., description: _Optional[str]=..., digest: _Optional[str]=..., hash_type: _Optional[_Union[File.HashType, str]]=...) -> None:
        ...

class ArchiveEntry(_message.Message):
    __slots__ = ('path', 'length', 'content_type')
    PATH_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    path: str
    length: _wrappers_pb2.Int64Value
    content_type: str

    def __init__(self, path: _Optional[str]=..., length: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., content_type: _Optional[str]=...) -> None:
        ...