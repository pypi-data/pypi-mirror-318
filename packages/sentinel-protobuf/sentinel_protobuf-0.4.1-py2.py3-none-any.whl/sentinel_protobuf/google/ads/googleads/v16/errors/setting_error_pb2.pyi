from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SettingErrorEnum(_message.Message):
    __slots__ = ()

    class SettingError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SettingErrorEnum.SettingError]
        UNKNOWN: _ClassVar[SettingErrorEnum.SettingError]
        SETTING_TYPE_IS_NOT_AVAILABLE: _ClassVar[SettingErrorEnum.SettingError]
        SETTING_TYPE_IS_NOT_COMPATIBLE_WITH_CAMPAIGN: _ClassVar[SettingErrorEnum.SettingError]
        TARGETING_SETTING_CONTAINS_INVALID_CRITERION_TYPE_GROUP: _ClassVar[SettingErrorEnum.SettingError]
        TARGETING_SETTING_DEMOGRAPHIC_CRITERION_TYPE_GROUPS_MUST_BE_SET_TO_TARGET_ALL: _ClassVar[SettingErrorEnum.SettingError]
        TARGETING_SETTING_CANNOT_CHANGE_TARGET_ALL_TO_FALSE_FOR_DEMOGRAPHIC_CRITERION_TYPE_GROUP: _ClassVar[SettingErrorEnum.SettingError]
        DYNAMIC_SEARCH_ADS_SETTING_AT_LEAST_ONE_FEED_ID_MUST_BE_PRESENT: _ClassVar[SettingErrorEnum.SettingError]
        DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_INVALID_DOMAIN_NAME: _ClassVar[SettingErrorEnum.SettingError]
        DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_SUBDOMAIN_NAME: _ClassVar[SettingErrorEnum.SettingError]
        DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_INVALID_LANGUAGE_CODE: _ClassVar[SettingErrorEnum.SettingError]
        TARGET_ALL_IS_NOT_ALLOWED_FOR_PLACEMENT_IN_SEARCH_CAMPAIGN: _ClassVar[SettingErrorEnum.SettingError]
        SETTING_VALUE_NOT_COMPATIBLE_WITH_CAMPAIGN: _ClassVar[SettingErrorEnum.SettingError]
        BID_ONLY_IS_NOT_ALLOWED_TO_BE_MODIFIED_WITH_CUSTOMER_MATCH_TARGETING: _ClassVar[SettingErrorEnum.SettingError]
    UNSPECIFIED: SettingErrorEnum.SettingError
    UNKNOWN: SettingErrorEnum.SettingError
    SETTING_TYPE_IS_NOT_AVAILABLE: SettingErrorEnum.SettingError
    SETTING_TYPE_IS_NOT_COMPATIBLE_WITH_CAMPAIGN: SettingErrorEnum.SettingError
    TARGETING_SETTING_CONTAINS_INVALID_CRITERION_TYPE_GROUP: SettingErrorEnum.SettingError
    TARGETING_SETTING_DEMOGRAPHIC_CRITERION_TYPE_GROUPS_MUST_BE_SET_TO_TARGET_ALL: SettingErrorEnum.SettingError
    TARGETING_SETTING_CANNOT_CHANGE_TARGET_ALL_TO_FALSE_FOR_DEMOGRAPHIC_CRITERION_TYPE_GROUP: SettingErrorEnum.SettingError
    DYNAMIC_SEARCH_ADS_SETTING_AT_LEAST_ONE_FEED_ID_MUST_BE_PRESENT: SettingErrorEnum.SettingError
    DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_INVALID_DOMAIN_NAME: SettingErrorEnum.SettingError
    DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_SUBDOMAIN_NAME: SettingErrorEnum.SettingError
    DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_INVALID_LANGUAGE_CODE: SettingErrorEnum.SettingError
    TARGET_ALL_IS_NOT_ALLOWED_FOR_PLACEMENT_IN_SEARCH_CAMPAIGN: SettingErrorEnum.SettingError
    SETTING_VALUE_NOT_COMPATIBLE_WITH_CAMPAIGN: SettingErrorEnum.SettingError
    BID_ONLY_IS_NOT_ALLOWED_TO_BE_MODIFIED_WITH_CUSTOMER_MATCH_TARGETING: SettingErrorEnum.SettingError

    def __init__(self) -> None:
        ...