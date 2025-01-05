from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class UserInterestTaxonomyTypeEnum(_message.Message):
    __slots__ = ()

    class UserInterestTaxonomyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType]
        UNKNOWN: _ClassVar[UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType]
        AFFINITY: _ClassVar[UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType]
        IN_MARKET: _ClassVar[UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType]
        MOBILE_APP_INSTALL_USER: _ClassVar[UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType]
        VERTICAL_GEO: _ClassVar[UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType]
        NEW_SMART_PHONE_USER: _ClassVar[UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType]
    UNSPECIFIED: UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType
    UNKNOWN: UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType
    AFFINITY: UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType
    IN_MARKET: UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType
    MOBILE_APP_INSTALL_USER: UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType
    VERTICAL_GEO: UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType
    NEW_SMART_PHONE_USER: UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType

    def __init__(self) -> None:
        ...