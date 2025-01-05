from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class OperatorErrorEnum(_message.Message):
    __slots__ = ()

    class OperatorError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[OperatorErrorEnum.OperatorError]
        UNKNOWN: _ClassVar[OperatorErrorEnum.OperatorError]
        OPERATOR_NOT_SUPPORTED: _ClassVar[OperatorErrorEnum.OperatorError]
    UNSPECIFIED: OperatorErrorEnum.OperatorError
    UNKNOWN: OperatorErrorEnum.OperatorError
    OPERATOR_NOT_SUPPORTED: OperatorErrorEnum.OperatorError

    def __init__(self) -> None:
        ...