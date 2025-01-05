from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomAudienceMemberTypeEnum(_message.Message):
    __slots__ = ()

    class CustomAudienceMemberType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomAudienceMemberTypeEnum.CustomAudienceMemberType]
        UNKNOWN: _ClassVar[CustomAudienceMemberTypeEnum.CustomAudienceMemberType]
        KEYWORD: _ClassVar[CustomAudienceMemberTypeEnum.CustomAudienceMemberType]
        URL: _ClassVar[CustomAudienceMemberTypeEnum.CustomAudienceMemberType]
        PLACE_CATEGORY: _ClassVar[CustomAudienceMemberTypeEnum.CustomAudienceMemberType]
        APP: _ClassVar[CustomAudienceMemberTypeEnum.CustomAudienceMemberType]
    UNSPECIFIED: CustomAudienceMemberTypeEnum.CustomAudienceMemberType
    UNKNOWN: CustomAudienceMemberTypeEnum.CustomAudienceMemberType
    KEYWORD: CustomAudienceMemberTypeEnum.CustomAudienceMemberType
    URL: CustomAudienceMemberTypeEnum.CustomAudienceMemberType
    PLACE_CATEGORY: CustomAudienceMemberTypeEnum.CustomAudienceMemberType
    APP: CustomAudienceMemberTypeEnum.CustomAudienceMemberType

    def __init__(self) -> None:
        ...