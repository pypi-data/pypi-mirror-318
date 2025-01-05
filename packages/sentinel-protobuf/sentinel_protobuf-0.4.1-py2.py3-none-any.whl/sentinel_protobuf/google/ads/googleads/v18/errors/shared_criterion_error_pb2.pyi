from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SharedCriterionErrorEnum(_message.Message):
    __slots__ = ()

    class SharedCriterionError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SharedCriterionErrorEnum.SharedCriterionError]
        UNKNOWN: _ClassVar[SharedCriterionErrorEnum.SharedCriterionError]
        CRITERION_TYPE_NOT_ALLOWED_FOR_SHARED_SET_TYPE: _ClassVar[SharedCriterionErrorEnum.SharedCriterionError]
    UNSPECIFIED: SharedCriterionErrorEnum.SharedCriterionError
    UNKNOWN: SharedCriterionErrorEnum.SharedCriterionError
    CRITERION_TYPE_NOT_ALLOWED_FOR_SHARED_SET_TYPE: SharedCriterionErrorEnum.SharedCriterionError

    def __init__(self) -> None:
        ...