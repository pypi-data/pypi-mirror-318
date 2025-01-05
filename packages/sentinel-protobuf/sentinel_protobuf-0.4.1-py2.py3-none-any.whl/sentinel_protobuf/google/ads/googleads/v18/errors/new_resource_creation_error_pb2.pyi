from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class NewResourceCreationErrorEnum(_message.Message):
    __slots__ = ()

    class NewResourceCreationError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[NewResourceCreationErrorEnum.NewResourceCreationError]
        UNKNOWN: _ClassVar[NewResourceCreationErrorEnum.NewResourceCreationError]
        CANNOT_SET_ID_FOR_CREATE: _ClassVar[NewResourceCreationErrorEnum.NewResourceCreationError]
        DUPLICATE_TEMP_IDS: _ClassVar[NewResourceCreationErrorEnum.NewResourceCreationError]
        TEMP_ID_RESOURCE_HAD_ERRORS: _ClassVar[NewResourceCreationErrorEnum.NewResourceCreationError]
    UNSPECIFIED: NewResourceCreationErrorEnum.NewResourceCreationError
    UNKNOWN: NewResourceCreationErrorEnum.NewResourceCreationError
    CANNOT_SET_ID_FOR_CREATE: NewResourceCreationErrorEnum.NewResourceCreationError
    DUPLICATE_TEMP_IDS: NewResourceCreationErrorEnum.NewResourceCreationError
    TEMP_ID_RESOURCE_HAD_ERRORS: NewResourceCreationErrorEnum.NewResourceCreationError

    def __init__(self) -> None:
        ...