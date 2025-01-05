from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomInterestTypeEnum(_message.Message):
    __slots__ = ()

    class CustomInterestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomInterestTypeEnum.CustomInterestType]
        UNKNOWN: _ClassVar[CustomInterestTypeEnum.CustomInterestType]
        CUSTOM_AFFINITY: _ClassVar[CustomInterestTypeEnum.CustomInterestType]
        CUSTOM_INTENT: _ClassVar[CustomInterestTypeEnum.CustomInterestType]
    UNSPECIFIED: CustomInterestTypeEnum.CustomInterestType
    UNKNOWN: CustomInterestTypeEnum.CustomInterestType
    CUSTOM_AFFINITY: CustomInterestTypeEnum.CustomInterestType
    CUSTOM_INTENT: CustomInterestTypeEnum.CustomInterestType

    def __init__(self) -> None:
        ...