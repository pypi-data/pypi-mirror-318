from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomInterestMemberTypeEnum(_message.Message):
    __slots__ = ()

    class CustomInterestMemberType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomInterestMemberTypeEnum.CustomInterestMemberType]
        UNKNOWN: _ClassVar[CustomInterestMemberTypeEnum.CustomInterestMemberType]
        KEYWORD: _ClassVar[CustomInterestMemberTypeEnum.CustomInterestMemberType]
        URL: _ClassVar[CustomInterestMemberTypeEnum.CustomInterestMemberType]
    UNSPECIFIED: CustomInterestMemberTypeEnum.CustomInterestMemberType
    UNKNOWN: CustomInterestMemberTypeEnum.CustomInterestMemberType
    KEYWORD: CustomInterestMemberTypeEnum.CustomInterestMemberType
    URL: CustomInterestMemberTypeEnum.CustomInterestMemberType

    def __init__(self) -> None:
        ...