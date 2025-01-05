from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class KeywordPlanKeywordAnnotationEnum(_message.Message):
    __slots__ = ()

    class KeywordPlanKeywordAnnotation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[KeywordPlanKeywordAnnotationEnum.KeywordPlanKeywordAnnotation]
        UNKNOWN: _ClassVar[KeywordPlanKeywordAnnotationEnum.KeywordPlanKeywordAnnotation]
        KEYWORD_CONCEPT: _ClassVar[KeywordPlanKeywordAnnotationEnum.KeywordPlanKeywordAnnotation]
    UNSPECIFIED: KeywordPlanKeywordAnnotationEnum.KeywordPlanKeywordAnnotation
    UNKNOWN: KeywordPlanKeywordAnnotationEnum.KeywordPlanKeywordAnnotation
    KEYWORD_CONCEPT: KeywordPlanKeywordAnnotationEnum.KeywordPlanKeywordAnnotation

    def __init__(self) -> None:
        ...