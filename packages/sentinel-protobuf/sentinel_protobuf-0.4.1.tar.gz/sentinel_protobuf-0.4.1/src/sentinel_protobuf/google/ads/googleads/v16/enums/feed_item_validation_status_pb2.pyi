from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FeedItemValidationStatusEnum(_message.Message):
    __slots__ = ()

    class FeedItemValidationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FeedItemValidationStatusEnum.FeedItemValidationStatus]
        UNKNOWN: _ClassVar[FeedItemValidationStatusEnum.FeedItemValidationStatus]
        PENDING: _ClassVar[FeedItemValidationStatusEnum.FeedItemValidationStatus]
        INVALID: _ClassVar[FeedItemValidationStatusEnum.FeedItemValidationStatus]
        VALID: _ClassVar[FeedItemValidationStatusEnum.FeedItemValidationStatus]
    UNSPECIFIED: FeedItemValidationStatusEnum.FeedItemValidationStatus
    UNKNOWN: FeedItemValidationStatusEnum.FeedItemValidationStatus
    PENDING: FeedItemValidationStatusEnum.FeedItemValidationStatus
    INVALID: FeedItemValidationStatusEnum.FeedItemValidationStatus
    VALID: FeedItemValidationStatusEnum.FeedItemValidationStatus

    def __init__(self) -> None:
        ...