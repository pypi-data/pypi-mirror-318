from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class DataDrivenModelStatusEnum(_message.Message):
    __slots__ = ()

    class DataDrivenModelStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[DataDrivenModelStatusEnum.DataDrivenModelStatus]
        UNKNOWN: _ClassVar[DataDrivenModelStatusEnum.DataDrivenModelStatus]
        AVAILABLE: _ClassVar[DataDrivenModelStatusEnum.DataDrivenModelStatus]
        STALE: _ClassVar[DataDrivenModelStatusEnum.DataDrivenModelStatus]
        EXPIRED: _ClassVar[DataDrivenModelStatusEnum.DataDrivenModelStatus]
        NEVER_GENERATED: _ClassVar[DataDrivenModelStatusEnum.DataDrivenModelStatus]
    UNSPECIFIED: DataDrivenModelStatusEnum.DataDrivenModelStatus
    UNKNOWN: DataDrivenModelStatusEnum.DataDrivenModelStatus
    AVAILABLE: DataDrivenModelStatusEnum.DataDrivenModelStatus
    STALE: DataDrivenModelStatusEnum.DataDrivenModelStatus
    EXPIRED: DataDrivenModelStatusEnum.DataDrivenModelStatus
    NEVER_GENERATED: DataDrivenModelStatusEnum.DataDrivenModelStatus

    def __init__(self) -> None:
        ...