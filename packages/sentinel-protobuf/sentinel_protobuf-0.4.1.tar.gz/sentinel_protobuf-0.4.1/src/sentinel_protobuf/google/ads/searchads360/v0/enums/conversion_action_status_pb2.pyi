from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionActionStatusEnum(_message.Message):
    __slots__ = ()

    class ConversionActionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionActionStatusEnum.ConversionActionStatus]
        UNKNOWN: _ClassVar[ConversionActionStatusEnum.ConversionActionStatus]
        ENABLED: _ClassVar[ConversionActionStatusEnum.ConversionActionStatus]
        REMOVED: _ClassVar[ConversionActionStatusEnum.ConversionActionStatus]
        HIDDEN: _ClassVar[ConversionActionStatusEnum.ConversionActionStatus]
    UNSPECIFIED: ConversionActionStatusEnum.ConversionActionStatus
    UNKNOWN: ConversionActionStatusEnum.ConversionActionStatus
    ENABLED: ConversionActionStatusEnum.ConversionActionStatus
    REMOVED: ConversionActionStatusEnum.ConversionActionStatus
    HIDDEN: ConversionActionStatusEnum.ConversionActionStatus

    def __init__(self) -> None:
        ...