from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AffiliateLocationFeedRelationshipTypeEnum(_message.Message):
    __slots__ = ()

    class AffiliateLocationFeedRelationshipType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AffiliateLocationFeedRelationshipTypeEnum.AffiliateLocationFeedRelationshipType]
        UNKNOWN: _ClassVar[AffiliateLocationFeedRelationshipTypeEnum.AffiliateLocationFeedRelationshipType]
        GENERAL_RETAILER: _ClassVar[AffiliateLocationFeedRelationshipTypeEnum.AffiliateLocationFeedRelationshipType]
    UNSPECIFIED: AffiliateLocationFeedRelationshipTypeEnum.AffiliateLocationFeedRelationshipType
    UNKNOWN: AffiliateLocationFeedRelationshipTypeEnum.AffiliateLocationFeedRelationshipType
    GENERAL_RETAILER: AffiliateLocationFeedRelationshipTypeEnum.AffiliateLocationFeedRelationshipType

    def __init__(self) -> None:
        ...