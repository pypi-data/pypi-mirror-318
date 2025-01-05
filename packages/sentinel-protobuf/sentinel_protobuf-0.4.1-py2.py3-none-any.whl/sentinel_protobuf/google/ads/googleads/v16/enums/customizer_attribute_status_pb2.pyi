from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomizerAttributeStatusEnum(_message.Message):
    __slots__ = ()

    class CustomizerAttributeStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomizerAttributeStatusEnum.CustomizerAttributeStatus]
        UNKNOWN: _ClassVar[CustomizerAttributeStatusEnum.CustomizerAttributeStatus]
        ENABLED: _ClassVar[CustomizerAttributeStatusEnum.CustomizerAttributeStatus]
        REMOVED: _ClassVar[CustomizerAttributeStatusEnum.CustomizerAttributeStatus]
    UNSPECIFIED: CustomizerAttributeStatusEnum.CustomizerAttributeStatus
    UNKNOWN: CustomizerAttributeStatusEnum.CustomizerAttributeStatus
    ENABLED: CustomizerAttributeStatusEnum.CustomizerAttributeStatus
    REMOVED: CustomizerAttributeStatusEnum.CustomizerAttributeStatus

    def __init__(self) -> None:
        ...