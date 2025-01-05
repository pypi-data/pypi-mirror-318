from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class DistinctErrorEnum(_message.Message):
    __slots__ = ()

    class DistinctError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[DistinctErrorEnum.DistinctError]
        UNKNOWN: _ClassVar[DistinctErrorEnum.DistinctError]
        DUPLICATE_ELEMENT: _ClassVar[DistinctErrorEnum.DistinctError]
        DUPLICATE_TYPE: _ClassVar[DistinctErrorEnum.DistinctError]
    UNSPECIFIED: DistinctErrorEnum.DistinctError
    UNKNOWN: DistinctErrorEnum.DistinctError
    DUPLICATE_ELEMENT: DistinctErrorEnum.DistinctError
    DUPLICATE_TYPE: DistinctErrorEnum.DistinctError

    def __init__(self) -> None:
        ...