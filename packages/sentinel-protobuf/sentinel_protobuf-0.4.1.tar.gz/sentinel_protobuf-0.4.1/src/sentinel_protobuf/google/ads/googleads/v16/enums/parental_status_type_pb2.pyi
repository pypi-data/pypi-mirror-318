from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ParentalStatusTypeEnum(_message.Message):
    __slots__ = ()

    class ParentalStatusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ParentalStatusTypeEnum.ParentalStatusType]
        UNKNOWN: _ClassVar[ParentalStatusTypeEnum.ParentalStatusType]
        PARENT: _ClassVar[ParentalStatusTypeEnum.ParentalStatusType]
        NOT_A_PARENT: _ClassVar[ParentalStatusTypeEnum.ParentalStatusType]
        UNDETERMINED: _ClassVar[ParentalStatusTypeEnum.ParentalStatusType]
    UNSPECIFIED: ParentalStatusTypeEnum.ParentalStatusType
    UNKNOWN: ParentalStatusTypeEnum.ParentalStatusType
    PARENT: ParentalStatusTypeEnum.ParentalStatusType
    NOT_A_PARENT: ParentalStatusTypeEnum.ParentalStatusType
    UNDETERMINED: ParentalStatusTypeEnum.ParentalStatusType

    def __init__(self) -> None:
        ...