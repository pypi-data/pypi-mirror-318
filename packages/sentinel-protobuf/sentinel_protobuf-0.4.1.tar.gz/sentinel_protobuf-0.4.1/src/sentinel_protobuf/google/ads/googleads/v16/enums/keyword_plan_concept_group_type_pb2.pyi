from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class KeywordPlanConceptGroupTypeEnum(_message.Message):
    __slots__ = ()

    class KeywordPlanConceptGroupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType]
        UNKNOWN: _ClassVar[KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType]
        BRAND: _ClassVar[KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType]
        OTHER_BRANDS: _ClassVar[KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType]
        NON_BRAND: _ClassVar[KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType]
    UNSPECIFIED: KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType
    UNKNOWN: KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType
    BRAND: KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType
    OTHER_BRANDS: KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType
    NON_BRAND: KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType

    def __init__(self) -> None:
        ...