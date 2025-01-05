from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomerFeedErrorEnum(_message.Message):
    __slots__ = ()

    class CustomerFeedError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomerFeedErrorEnum.CustomerFeedError]
        UNKNOWN: _ClassVar[CustomerFeedErrorEnum.CustomerFeedError]
        FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE: _ClassVar[CustomerFeedErrorEnum.CustomerFeedError]
        CANNOT_CREATE_FOR_REMOVED_FEED: _ClassVar[CustomerFeedErrorEnum.CustomerFeedError]
        CANNOT_CREATE_ALREADY_EXISTING_CUSTOMER_FEED: _ClassVar[CustomerFeedErrorEnum.CustomerFeedError]
        CANNOT_MODIFY_REMOVED_CUSTOMER_FEED: _ClassVar[CustomerFeedErrorEnum.CustomerFeedError]
        INVALID_PLACEHOLDER_TYPE: _ClassVar[CustomerFeedErrorEnum.CustomerFeedError]
        MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE: _ClassVar[CustomerFeedErrorEnum.CustomerFeedError]
        PLACEHOLDER_TYPE_NOT_ALLOWED_ON_CUSTOMER_FEED: _ClassVar[CustomerFeedErrorEnum.CustomerFeedError]
    UNSPECIFIED: CustomerFeedErrorEnum.CustomerFeedError
    UNKNOWN: CustomerFeedErrorEnum.CustomerFeedError
    FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE: CustomerFeedErrorEnum.CustomerFeedError
    CANNOT_CREATE_FOR_REMOVED_FEED: CustomerFeedErrorEnum.CustomerFeedError
    CANNOT_CREATE_ALREADY_EXISTING_CUSTOMER_FEED: CustomerFeedErrorEnum.CustomerFeedError
    CANNOT_MODIFY_REMOVED_CUSTOMER_FEED: CustomerFeedErrorEnum.CustomerFeedError
    INVALID_PLACEHOLDER_TYPE: CustomerFeedErrorEnum.CustomerFeedError
    MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE: CustomerFeedErrorEnum.CustomerFeedError
    PLACEHOLDER_TYPE_NOT_ALLOWED_ON_CUSTOMER_FEED: CustomerFeedErrorEnum.CustomerFeedError

    def __init__(self) -> None:
        ...