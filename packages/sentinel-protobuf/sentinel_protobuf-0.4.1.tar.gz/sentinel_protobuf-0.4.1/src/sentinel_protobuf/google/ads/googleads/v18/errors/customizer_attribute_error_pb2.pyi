from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomizerAttributeErrorEnum(_message.Message):
    __slots__ = ()

    class CustomizerAttributeError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomizerAttributeErrorEnum.CustomizerAttributeError]
        UNKNOWN: _ClassVar[CustomizerAttributeErrorEnum.CustomizerAttributeError]
        DUPLICATE_CUSTOMIZER_ATTRIBUTE_NAME: _ClassVar[CustomizerAttributeErrorEnum.CustomizerAttributeError]
    UNSPECIFIED: CustomizerAttributeErrorEnum.CustomizerAttributeError
    UNKNOWN: CustomizerAttributeErrorEnum.CustomizerAttributeError
    DUPLICATE_CUSTOMIZER_ATTRIBUTE_NAME: CustomizerAttributeErrorEnum.CustomizerAttributeError

    def __init__(self) -> None:
        ...