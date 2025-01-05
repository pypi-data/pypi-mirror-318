from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class UserListErrorEnum(_message.Message):
    __slots__ = ()

    class UserListError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[UserListErrorEnum.UserListError]
        UNKNOWN: _ClassVar[UserListErrorEnum.UserListError]
        EXTERNAL_REMARKETING_USER_LIST_MUTATE_NOT_SUPPORTED: _ClassVar[UserListErrorEnum.UserListError]
        CONCRETE_TYPE_REQUIRED: _ClassVar[UserListErrorEnum.UserListError]
        CONVERSION_TYPE_ID_REQUIRED: _ClassVar[UserListErrorEnum.UserListError]
        DUPLICATE_CONVERSION_TYPES: _ClassVar[UserListErrorEnum.UserListError]
        INVALID_CONVERSION_TYPE: _ClassVar[UserListErrorEnum.UserListError]
        INVALID_DESCRIPTION: _ClassVar[UserListErrorEnum.UserListError]
        INVALID_NAME: _ClassVar[UserListErrorEnum.UserListError]
        INVALID_TYPE: _ClassVar[UserListErrorEnum.UserListError]
        CAN_NOT_ADD_LOGICAL_LIST_AS_LOGICAL_LIST_OPERAND: _ClassVar[UserListErrorEnum.UserListError]
        INVALID_USER_LIST_LOGICAL_RULE_OPERAND: _ClassVar[UserListErrorEnum.UserListError]
        NAME_ALREADY_USED: _ClassVar[UserListErrorEnum.UserListError]
        NEW_CONVERSION_TYPE_NAME_REQUIRED: _ClassVar[UserListErrorEnum.UserListError]
        CONVERSION_TYPE_NAME_ALREADY_USED: _ClassVar[UserListErrorEnum.UserListError]
        OWNERSHIP_REQUIRED_FOR_SET: _ClassVar[UserListErrorEnum.UserListError]
        USER_LIST_MUTATE_NOT_SUPPORTED: _ClassVar[UserListErrorEnum.UserListError]
        INVALID_RULE: _ClassVar[UserListErrorEnum.UserListError]
        INVALID_DATE_RANGE: _ClassVar[UserListErrorEnum.UserListError]
        CAN_NOT_MUTATE_SENSITIVE_USERLIST: _ClassVar[UserListErrorEnum.UserListError]
        MAX_NUM_RULEBASED_USERLISTS: _ClassVar[UserListErrorEnum.UserListError]
        CANNOT_MODIFY_BILLABLE_RECORD_COUNT: _ClassVar[UserListErrorEnum.UserListError]
        APP_ID_NOT_SET: _ClassVar[UserListErrorEnum.UserListError]
        USERLIST_NAME_IS_RESERVED_FOR_SYSTEM_LIST: _ClassVar[UserListErrorEnum.UserListError]
        ADVERTISER_NOT_ON_ALLOWLIST_FOR_USING_UPLOADED_DATA: _ClassVar[UserListErrorEnum.UserListError]
        RULE_TYPE_IS_NOT_SUPPORTED: _ClassVar[UserListErrorEnum.UserListError]
        CAN_NOT_ADD_A_SIMILAR_USERLIST_AS_LOGICAL_LIST_OPERAND: _ClassVar[UserListErrorEnum.UserListError]
        CAN_NOT_MIX_CRM_BASED_IN_LOGICAL_LIST_WITH_OTHER_LISTS: _ClassVar[UserListErrorEnum.UserListError]
        APP_ID_NOT_ALLOWED: _ClassVar[UserListErrorEnum.UserListError]
        CANNOT_MUTATE_SYSTEM_LIST: _ClassVar[UserListErrorEnum.UserListError]
        MOBILE_APP_IS_SENSITIVE: _ClassVar[UserListErrorEnum.UserListError]
        SEED_LIST_DOES_NOT_EXIST: _ClassVar[UserListErrorEnum.UserListError]
        INVALID_SEED_LIST_ACCESS_REASON: _ClassVar[UserListErrorEnum.UserListError]
        INVALID_SEED_LIST_TYPE: _ClassVar[UserListErrorEnum.UserListError]
        INVALID_COUNTRY_CODES: _ClassVar[UserListErrorEnum.UserListError]
    UNSPECIFIED: UserListErrorEnum.UserListError
    UNKNOWN: UserListErrorEnum.UserListError
    EXTERNAL_REMARKETING_USER_LIST_MUTATE_NOT_SUPPORTED: UserListErrorEnum.UserListError
    CONCRETE_TYPE_REQUIRED: UserListErrorEnum.UserListError
    CONVERSION_TYPE_ID_REQUIRED: UserListErrorEnum.UserListError
    DUPLICATE_CONVERSION_TYPES: UserListErrorEnum.UserListError
    INVALID_CONVERSION_TYPE: UserListErrorEnum.UserListError
    INVALID_DESCRIPTION: UserListErrorEnum.UserListError
    INVALID_NAME: UserListErrorEnum.UserListError
    INVALID_TYPE: UserListErrorEnum.UserListError
    CAN_NOT_ADD_LOGICAL_LIST_AS_LOGICAL_LIST_OPERAND: UserListErrorEnum.UserListError
    INVALID_USER_LIST_LOGICAL_RULE_OPERAND: UserListErrorEnum.UserListError
    NAME_ALREADY_USED: UserListErrorEnum.UserListError
    NEW_CONVERSION_TYPE_NAME_REQUIRED: UserListErrorEnum.UserListError
    CONVERSION_TYPE_NAME_ALREADY_USED: UserListErrorEnum.UserListError
    OWNERSHIP_REQUIRED_FOR_SET: UserListErrorEnum.UserListError
    USER_LIST_MUTATE_NOT_SUPPORTED: UserListErrorEnum.UserListError
    INVALID_RULE: UserListErrorEnum.UserListError
    INVALID_DATE_RANGE: UserListErrorEnum.UserListError
    CAN_NOT_MUTATE_SENSITIVE_USERLIST: UserListErrorEnum.UserListError
    MAX_NUM_RULEBASED_USERLISTS: UserListErrorEnum.UserListError
    CANNOT_MODIFY_BILLABLE_RECORD_COUNT: UserListErrorEnum.UserListError
    APP_ID_NOT_SET: UserListErrorEnum.UserListError
    USERLIST_NAME_IS_RESERVED_FOR_SYSTEM_LIST: UserListErrorEnum.UserListError
    ADVERTISER_NOT_ON_ALLOWLIST_FOR_USING_UPLOADED_DATA: UserListErrorEnum.UserListError
    RULE_TYPE_IS_NOT_SUPPORTED: UserListErrorEnum.UserListError
    CAN_NOT_ADD_A_SIMILAR_USERLIST_AS_LOGICAL_LIST_OPERAND: UserListErrorEnum.UserListError
    CAN_NOT_MIX_CRM_BASED_IN_LOGICAL_LIST_WITH_OTHER_LISTS: UserListErrorEnum.UserListError
    APP_ID_NOT_ALLOWED: UserListErrorEnum.UserListError
    CANNOT_MUTATE_SYSTEM_LIST: UserListErrorEnum.UserListError
    MOBILE_APP_IS_SENSITIVE: UserListErrorEnum.UserListError
    SEED_LIST_DOES_NOT_EXIST: UserListErrorEnum.UserListError
    INVALID_SEED_LIST_ACCESS_REASON: UserListErrorEnum.UserListError
    INVALID_SEED_LIST_TYPE: UserListErrorEnum.UserListError
    INVALID_COUNTRY_CODES: UserListErrorEnum.UserListError

    def __init__(self) -> None:
        ...