from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class DatabaseErrorEnum(_message.Message):
    __slots__ = ()

    class DatabaseError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[DatabaseErrorEnum.DatabaseError]
        UNKNOWN: _ClassVar[DatabaseErrorEnum.DatabaseError]
        CONCURRENT_MODIFICATION: _ClassVar[DatabaseErrorEnum.DatabaseError]
        DATA_CONSTRAINT_VIOLATION: _ClassVar[DatabaseErrorEnum.DatabaseError]
        REQUEST_TOO_LARGE: _ClassVar[DatabaseErrorEnum.DatabaseError]
    UNSPECIFIED: DatabaseErrorEnum.DatabaseError
    UNKNOWN: DatabaseErrorEnum.DatabaseError
    CONCURRENT_MODIFICATION: DatabaseErrorEnum.DatabaseError
    DATA_CONSTRAINT_VIOLATION: DatabaseErrorEnum.DatabaseError
    REQUEST_TOO_LARGE: DatabaseErrorEnum.DatabaseError

    def __init__(self) -> None:
        ...