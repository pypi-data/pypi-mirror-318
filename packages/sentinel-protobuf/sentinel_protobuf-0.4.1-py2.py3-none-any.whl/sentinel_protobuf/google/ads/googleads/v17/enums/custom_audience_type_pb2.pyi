from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomAudienceTypeEnum(_message.Message):
    __slots__ = ()

    class CustomAudienceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomAudienceTypeEnum.CustomAudienceType]
        UNKNOWN: _ClassVar[CustomAudienceTypeEnum.CustomAudienceType]
        AUTO: _ClassVar[CustomAudienceTypeEnum.CustomAudienceType]
        INTEREST: _ClassVar[CustomAudienceTypeEnum.CustomAudienceType]
        PURCHASE_INTENT: _ClassVar[CustomAudienceTypeEnum.CustomAudienceType]
        SEARCH: _ClassVar[CustomAudienceTypeEnum.CustomAudienceType]
    UNSPECIFIED: CustomAudienceTypeEnum.CustomAudienceType
    UNKNOWN: CustomAudienceTypeEnum.CustomAudienceType
    AUTO: CustomAudienceTypeEnum.CustomAudienceType
    INTEREST: CustomAudienceTypeEnum.CustomAudienceType
    PURCHASE_INTENT: CustomAudienceTypeEnum.CustomAudienceType
    SEARCH: CustomAudienceTypeEnum.CustomAudienceType

    def __init__(self) -> None:
        ...