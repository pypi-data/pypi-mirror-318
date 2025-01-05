from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedItemQualityDisapprovalReasonEnum(_message.Message):
    __slots__ = ()

    class FeedItemQualityDisapprovalReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
        UNKNOWN: _ClassVar[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
        PRICE_TABLE_REPETITIVE_HEADERS: _ClassVar[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
        PRICE_TABLE_REPETITIVE_DESCRIPTION: _ClassVar[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
        PRICE_TABLE_INCONSISTENT_ROWS: _ClassVar[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
        PRICE_DESCRIPTION_HAS_PRICE_QUALIFIERS: _ClassVar[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
        PRICE_UNSUPPORTED_LANGUAGE: _ClassVar[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
        PRICE_TABLE_ROW_HEADER_TABLE_TYPE_MISMATCH: _ClassVar[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
        PRICE_TABLE_ROW_HEADER_HAS_PROMOTIONAL_TEXT: _ClassVar[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
        PRICE_TABLE_ROW_DESCRIPTION_NOT_RELEVANT: _ClassVar[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
        PRICE_TABLE_ROW_DESCRIPTION_HAS_PROMOTIONAL_TEXT: _ClassVar[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
        PRICE_TABLE_ROW_HEADER_DESCRIPTION_REPETITIVE: _ClassVar[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
        PRICE_TABLE_ROW_UNRATEABLE: _ClassVar[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
        PRICE_TABLE_ROW_PRICE_INVALID: _ClassVar[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
        PRICE_TABLE_ROW_URL_INVALID: _ClassVar[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
        PRICE_HEADER_OR_DESCRIPTION_HAS_PRICE: _ClassVar[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
        STRUCTURED_SNIPPETS_HEADER_POLICY_VIOLATED: _ClassVar[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
        STRUCTURED_SNIPPETS_REPEATED_VALUES: _ClassVar[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
        STRUCTURED_SNIPPETS_EDITORIAL_GUIDELINES: _ClassVar[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
        STRUCTURED_SNIPPETS_HAS_PROMOTIONAL_TEXT: _ClassVar[FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
    UNSPECIFIED: FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    UNKNOWN: FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    PRICE_TABLE_REPETITIVE_HEADERS: FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    PRICE_TABLE_REPETITIVE_DESCRIPTION: FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    PRICE_TABLE_INCONSISTENT_ROWS: FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    PRICE_DESCRIPTION_HAS_PRICE_QUALIFIERS: FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    PRICE_UNSUPPORTED_LANGUAGE: FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    PRICE_TABLE_ROW_HEADER_TABLE_TYPE_MISMATCH: FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    PRICE_TABLE_ROW_HEADER_HAS_PROMOTIONAL_TEXT: FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    PRICE_TABLE_ROW_DESCRIPTION_NOT_RELEVANT: FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    PRICE_TABLE_ROW_DESCRIPTION_HAS_PROMOTIONAL_TEXT: FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    PRICE_TABLE_ROW_HEADER_DESCRIPTION_REPETITIVE: FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    PRICE_TABLE_ROW_UNRATEABLE: FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    PRICE_TABLE_ROW_PRICE_INVALID: FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    PRICE_TABLE_ROW_URL_INVALID: FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    PRICE_HEADER_OR_DESCRIPTION_HAS_PRICE: FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    STRUCTURED_SNIPPETS_HEADER_POLICY_VIOLATED: FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    STRUCTURED_SNIPPETS_REPEATED_VALUES: FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    STRUCTURED_SNIPPETS_EDITORIAL_GUIDELINES: FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    STRUCTURED_SNIPPETS_HAS_PROMOTIONAL_TEXT: FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason

    def __init__(self) -> None:
        ...