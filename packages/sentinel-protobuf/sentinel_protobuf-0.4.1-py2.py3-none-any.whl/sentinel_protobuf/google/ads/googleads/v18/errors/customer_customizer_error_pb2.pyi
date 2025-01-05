from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomerCustomizerErrorEnum(_message.Message):
    __slots__ = ()

    class CustomerCustomizerError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomerCustomizerErrorEnum.CustomerCustomizerError]
        UNKNOWN: _ClassVar[CustomerCustomizerErrorEnum.CustomerCustomizerError]
    UNSPECIFIED: CustomerCustomizerErrorEnum.CustomerCustomizerError
    UNKNOWN: CustomerCustomizerErrorEnum.CustomerCustomizerError

    def __init__(self) -> None:
        ...