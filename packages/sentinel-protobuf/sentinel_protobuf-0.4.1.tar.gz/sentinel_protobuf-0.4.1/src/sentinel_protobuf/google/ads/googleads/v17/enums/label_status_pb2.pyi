from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LabelStatusEnum(_message.Message):
    __slots__ = ()

    class LabelStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LabelStatusEnum.LabelStatus]
        UNKNOWN: _ClassVar[LabelStatusEnum.LabelStatus]
        ENABLED: _ClassVar[LabelStatusEnum.LabelStatus]
        REMOVED: _ClassVar[LabelStatusEnum.LabelStatus]
    UNSPECIFIED: LabelStatusEnum.LabelStatus
    UNKNOWN: LabelStatusEnum.LabelStatus
    ENABLED: LabelStatusEnum.LabelStatus
    REMOVED: LabelStatusEnum.LabelStatus

    def __init__(self) -> None:
        ...