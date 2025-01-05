from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SearchAds360FieldCategoryEnum(_message.Message):
    __slots__ = ()

    class SearchAds360FieldCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SearchAds360FieldCategoryEnum.SearchAds360FieldCategory]
        UNKNOWN: _ClassVar[SearchAds360FieldCategoryEnum.SearchAds360FieldCategory]
        RESOURCE: _ClassVar[SearchAds360FieldCategoryEnum.SearchAds360FieldCategory]
        ATTRIBUTE: _ClassVar[SearchAds360FieldCategoryEnum.SearchAds360FieldCategory]
        SEGMENT: _ClassVar[SearchAds360FieldCategoryEnum.SearchAds360FieldCategory]
        METRIC: _ClassVar[SearchAds360FieldCategoryEnum.SearchAds360FieldCategory]
    UNSPECIFIED: SearchAds360FieldCategoryEnum.SearchAds360FieldCategory
    UNKNOWN: SearchAds360FieldCategoryEnum.SearchAds360FieldCategory
    RESOURCE: SearchAds360FieldCategoryEnum.SearchAds360FieldCategory
    ATTRIBUTE: SearchAds360FieldCategoryEnum.SearchAds360FieldCategory
    SEGMENT: SearchAds360FieldCategoryEnum.SearchAds360FieldCategory
    METRIC: SearchAds360FieldCategoryEnum.SearchAds360FieldCategory

    def __init__(self) -> None:
        ...