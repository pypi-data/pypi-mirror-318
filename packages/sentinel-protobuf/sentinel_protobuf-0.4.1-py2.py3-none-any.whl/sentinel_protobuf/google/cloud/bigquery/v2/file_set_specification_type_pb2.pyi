from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FileSetSpecType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FILE_SET_SPEC_TYPE_FILE_SYSTEM_MATCH: _ClassVar[FileSetSpecType]
    FILE_SET_SPEC_TYPE_NEW_LINE_DELIMITED_MANIFEST: _ClassVar[FileSetSpecType]
FILE_SET_SPEC_TYPE_FILE_SYSTEM_MATCH: FileSetSpecType
FILE_SET_SPEC_TYPE_NEW_LINE_DELIMITED_MANIFEST: FileSetSpecType