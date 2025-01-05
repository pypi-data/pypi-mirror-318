from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class KeywordPlanAdGroupKeywordErrorEnum(_message.Message):
    __slots__ = ()

    class KeywordPlanAdGroupKeywordError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError]
        UNKNOWN: _ClassVar[KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError]
        INVALID_KEYWORD_MATCH_TYPE: _ClassVar[KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError]
        DUPLICATE_KEYWORD: _ClassVar[KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError]
        KEYWORD_TEXT_TOO_LONG: _ClassVar[KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError]
        KEYWORD_HAS_INVALID_CHARS: _ClassVar[KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError]
        KEYWORD_HAS_TOO_MANY_WORDS: _ClassVar[KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError]
        INVALID_KEYWORD_TEXT: _ClassVar[KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError]
        NEGATIVE_KEYWORD_HAS_CPC_BID: _ClassVar[KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError]
        NEW_BMM_KEYWORDS_NOT_ALLOWED: _ClassVar[KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError]
    UNSPECIFIED: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError
    UNKNOWN: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError
    INVALID_KEYWORD_MATCH_TYPE: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError
    DUPLICATE_KEYWORD: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError
    KEYWORD_TEXT_TOO_LONG: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError
    KEYWORD_HAS_INVALID_CHARS: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError
    KEYWORD_HAS_TOO_MANY_WORDS: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError
    INVALID_KEYWORD_TEXT: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError
    NEGATIVE_KEYWORD_HAS_CPC_BID: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError
    NEW_BMM_KEYWORDS_NOT_ALLOWED: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError

    def __init__(self) -> None:
        ...