from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class GoogleAdsFieldCategoryEnum(_message.Message):
    __slots__ = ()

    class GoogleAdsFieldCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory]
        UNKNOWN: _ClassVar[GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory]
        RESOURCE: _ClassVar[GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory]
        ATTRIBUTE: _ClassVar[GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory]
        SEGMENT: _ClassVar[GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory]
        METRIC: _ClassVar[GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory]
    UNSPECIFIED: GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory
    UNKNOWN: GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory
    RESOURCE: GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory
    ATTRIBUTE: GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory
    SEGMENT: GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory
    METRIC: GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory

    def __init__(self) -> None:
        ...