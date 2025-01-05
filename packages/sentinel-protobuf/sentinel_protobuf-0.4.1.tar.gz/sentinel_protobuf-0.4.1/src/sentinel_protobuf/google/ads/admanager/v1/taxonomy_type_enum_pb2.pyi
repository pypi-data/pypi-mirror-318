from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class TaxonomyTypeEnum(_message.Message):
    __slots__ = ()

    class TaxonomyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TAXONOMY_TYPE_UNSPECIFIED: _ClassVar[TaxonomyTypeEnum.TaxonomyType]
        TAXONOMY_IAB_AUDIENCE_1_1: _ClassVar[TaxonomyTypeEnum.TaxonomyType]
        TAXONOMY_IAB_CONTENT_2_1: _ClassVar[TaxonomyTypeEnum.TaxonomyType]
        TAXONOMY_IAB_CONTENT_2_2: _ClassVar[TaxonomyTypeEnum.TaxonomyType]
        TAXONOMY_IAB_CONTENT_3_0: _ClassVar[TaxonomyTypeEnum.TaxonomyType]
        TAXONOMY_GOOGLE_STRUCTURED_VIDEO_1_0: _ClassVar[TaxonomyTypeEnum.TaxonomyType]
    TAXONOMY_TYPE_UNSPECIFIED: TaxonomyTypeEnum.TaxonomyType
    TAXONOMY_IAB_AUDIENCE_1_1: TaxonomyTypeEnum.TaxonomyType
    TAXONOMY_IAB_CONTENT_2_1: TaxonomyTypeEnum.TaxonomyType
    TAXONOMY_IAB_CONTENT_2_2: TaxonomyTypeEnum.TaxonomyType
    TAXONOMY_IAB_CONTENT_3_0: TaxonomyTypeEnum.TaxonomyType
    TAXONOMY_GOOGLE_STRUCTURED_VIDEO_1_0: TaxonomyTypeEnum.TaxonomyType

    def __init__(self) -> None:
        ...