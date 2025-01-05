from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CollectionSizeErrorEnum(_message.Message):
    __slots__ = ()

    class CollectionSizeError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CollectionSizeErrorEnum.CollectionSizeError]
        UNKNOWN: _ClassVar[CollectionSizeErrorEnum.CollectionSizeError]
        TOO_FEW: _ClassVar[CollectionSizeErrorEnum.CollectionSizeError]
        TOO_MANY: _ClassVar[CollectionSizeErrorEnum.CollectionSizeError]
    UNSPECIFIED: CollectionSizeErrorEnum.CollectionSizeError
    UNKNOWN: CollectionSizeErrorEnum.CollectionSizeError
    TOO_FEW: CollectionSizeErrorEnum.CollectionSizeError
    TOO_MANY: CollectionSizeErrorEnum.CollectionSizeError

    def __init__(self) -> None:
        ...