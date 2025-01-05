from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class UserListSizeRangeEnum(_message.Message):
    __slots__ = ()

    class UserListSizeRange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[UserListSizeRangeEnum.UserListSizeRange]
        UNKNOWN: _ClassVar[UserListSizeRangeEnum.UserListSizeRange]
        LESS_THAN_FIVE_HUNDRED: _ClassVar[UserListSizeRangeEnum.UserListSizeRange]
        LESS_THAN_ONE_THOUSAND: _ClassVar[UserListSizeRangeEnum.UserListSizeRange]
        ONE_THOUSAND_TO_TEN_THOUSAND: _ClassVar[UserListSizeRangeEnum.UserListSizeRange]
        TEN_THOUSAND_TO_FIFTY_THOUSAND: _ClassVar[UserListSizeRangeEnum.UserListSizeRange]
        FIFTY_THOUSAND_TO_ONE_HUNDRED_THOUSAND: _ClassVar[UserListSizeRangeEnum.UserListSizeRange]
        ONE_HUNDRED_THOUSAND_TO_THREE_HUNDRED_THOUSAND: _ClassVar[UserListSizeRangeEnum.UserListSizeRange]
        THREE_HUNDRED_THOUSAND_TO_FIVE_HUNDRED_THOUSAND: _ClassVar[UserListSizeRangeEnum.UserListSizeRange]
        FIVE_HUNDRED_THOUSAND_TO_ONE_MILLION: _ClassVar[UserListSizeRangeEnum.UserListSizeRange]
        ONE_MILLION_TO_TWO_MILLION: _ClassVar[UserListSizeRangeEnum.UserListSizeRange]
        TWO_MILLION_TO_THREE_MILLION: _ClassVar[UserListSizeRangeEnum.UserListSizeRange]
        THREE_MILLION_TO_FIVE_MILLION: _ClassVar[UserListSizeRangeEnum.UserListSizeRange]
        FIVE_MILLION_TO_TEN_MILLION: _ClassVar[UserListSizeRangeEnum.UserListSizeRange]
        TEN_MILLION_TO_TWENTY_MILLION: _ClassVar[UserListSizeRangeEnum.UserListSizeRange]
        TWENTY_MILLION_TO_THIRTY_MILLION: _ClassVar[UserListSizeRangeEnum.UserListSizeRange]
        THIRTY_MILLION_TO_FIFTY_MILLION: _ClassVar[UserListSizeRangeEnum.UserListSizeRange]
        OVER_FIFTY_MILLION: _ClassVar[UserListSizeRangeEnum.UserListSizeRange]
    UNSPECIFIED: UserListSizeRangeEnum.UserListSizeRange
    UNKNOWN: UserListSizeRangeEnum.UserListSizeRange
    LESS_THAN_FIVE_HUNDRED: UserListSizeRangeEnum.UserListSizeRange
    LESS_THAN_ONE_THOUSAND: UserListSizeRangeEnum.UserListSizeRange
    ONE_THOUSAND_TO_TEN_THOUSAND: UserListSizeRangeEnum.UserListSizeRange
    TEN_THOUSAND_TO_FIFTY_THOUSAND: UserListSizeRangeEnum.UserListSizeRange
    FIFTY_THOUSAND_TO_ONE_HUNDRED_THOUSAND: UserListSizeRangeEnum.UserListSizeRange
    ONE_HUNDRED_THOUSAND_TO_THREE_HUNDRED_THOUSAND: UserListSizeRangeEnum.UserListSizeRange
    THREE_HUNDRED_THOUSAND_TO_FIVE_HUNDRED_THOUSAND: UserListSizeRangeEnum.UserListSizeRange
    FIVE_HUNDRED_THOUSAND_TO_ONE_MILLION: UserListSizeRangeEnum.UserListSizeRange
    ONE_MILLION_TO_TWO_MILLION: UserListSizeRangeEnum.UserListSizeRange
    TWO_MILLION_TO_THREE_MILLION: UserListSizeRangeEnum.UserListSizeRange
    THREE_MILLION_TO_FIVE_MILLION: UserListSizeRangeEnum.UserListSizeRange
    FIVE_MILLION_TO_TEN_MILLION: UserListSizeRangeEnum.UserListSizeRange
    TEN_MILLION_TO_TWENTY_MILLION: UserListSizeRangeEnum.UserListSizeRange
    TWENTY_MILLION_TO_THIRTY_MILLION: UserListSizeRangeEnum.UserListSizeRange
    THIRTY_MILLION_TO_FIFTY_MILLION: UserListSizeRangeEnum.UserListSizeRange
    OVER_FIFTY_MILLION: UserListSizeRangeEnum.UserListSizeRange

    def __init__(self) -> None:
        ...