from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupCustomizerErrorEnum(_message.Message):
    __slots__ = ()

    class AdGroupCustomizerError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdGroupCustomizerErrorEnum.AdGroupCustomizerError]
        UNKNOWN: _ClassVar[AdGroupCustomizerErrorEnum.AdGroupCustomizerError]
    UNSPECIFIED: AdGroupCustomizerErrorEnum.AdGroupCustomizerError
    UNKNOWN: AdGroupCustomizerErrorEnum.AdGroupCustomizerError

    def __init__(self) -> None:
        ...