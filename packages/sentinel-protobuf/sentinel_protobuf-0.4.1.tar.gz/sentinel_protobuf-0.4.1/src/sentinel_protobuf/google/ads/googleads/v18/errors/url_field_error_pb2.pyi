from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class UrlFieldErrorEnum(_message.Message):
    __slots__ = ()

    class UrlFieldError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        UNKNOWN: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_TRACKING_URL_TEMPLATE: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_TAG_IN_TRACKING_URL_TEMPLATE: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        MISSING_TRACKING_URL_TEMPLATE_TAG: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        MISSING_PROTOCOL_IN_TRACKING_URL_TEMPLATE: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_PROTOCOL_IN_TRACKING_URL_TEMPLATE: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        MALFORMED_TRACKING_URL_TEMPLATE: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        MISSING_HOST_IN_TRACKING_URL_TEMPLATE: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_TLD_IN_TRACKING_URL_TEMPLATE: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        REDUNDANT_NESTED_TRACKING_URL_TEMPLATE_TAG: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_FINAL_URL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_TAG_IN_FINAL_URL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        REDUNDANT_NESTED_FINAL_URL_TAG: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        MISSING_PROTOCOL_IN_FINAL_URL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_PROTOCOL_IN_FINAL_URL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        MALFORMED_FINAL_URL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        MISSING_HOST_IN_FINAL_URL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_TLD_IN_FINAL_URL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_FINAL_MOBILE_URL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_TAG_IN_FINAL_MOBILE_URL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        REDUNDANT_NESTED_FINAL_MOBILE_URL_TAG: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        MISSING_PROTOCOL_IN_FINAL_MOBILE_URL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_PROTOCOL_IN_FINAL_MOBILE_URL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        MALFORMED_FINAL_MOBILE_URL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        MISSING_HOST_IN_FINAL_MOBILE_URL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_TLD_IN_FINAL_MOBILE_URL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_FINAL_APP_URL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_TAG_IN_FINAL_APP_URL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        REDUNDANT_NESTED_FINAL_APP_URL_TAG: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        MULTIPLE_APP_URLS_FOR_OSTYPE: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_OSTYPE: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_PROTOCOL_FOR_APP_URL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_PACKAGE_ID_FOR_APP_URL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        URL_CUSTOM_PARAMETERS_COUNT_EXCEEDS_LIMIT: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_CHARACTERS_IN_URL_CUSTOM_PARAMETER_KEY: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_CHARACTERS_IN_URL_CUSTOM_PARAMETER_VALUE: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_TAG_IN_URL_CUSTOM_PARAMETER_VALUE: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        REDUNDANT_NESTED_URL_CUSTOM_PARAMETER_TAG: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        MISSING_PROTOCOL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_PROTOCOL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_URL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        DESTINATION_URL_DEPRECATED: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_TAG_IN_URL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        MISSING_URL_TAG: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        DUPLICATE_URL_ID: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_URL_ID: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        FINAL_URL_SUFFIX_MALFORMED: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_TAG_IN_FINAL_URL_SUFFIX: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        INVALID_TOP_LEVEL_DOMAIN: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        MALFORMED_TOP_LEVEL_DOMAIN: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        MALFORMED_URL: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        MISSING_HOST: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        NULL_CUSTOM_PARAMETER_VALUE: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
        VALUE_TRACK_PARAMETER_NOT_SUPPORTED: _ClassVar[UrlFieldErrorEnum.UrlFieldError]
    UNSPECIFIED: UrlFieldErrorEnum.UrlFieldError
    UNKNOWN: UrlFieldErrorEnum.UrlFieldError
    INVALID_TRACKING_URL_TEMPLATE: UrlFieldErrorEnum.UrlFieldError
    INVALID_TAG_IN_TRACKING_URL_TEMPLATE: UrlFieldErrorEnum.UrlFieldError
    MISSING_TRACKING_URL_TEMPLATE_TAG: UrlFieldErrorEnum.UrlFieldError
    MISSING_PROTOCOL_IN_TRACKING_URL_TEMPLATE: UrlFieldErrorEnum.UrlFieldError
    INVALID_PROTOCOL_IN_TRACKING_URL_TEMPLATE: UrlFieldErrorEnum.UrlFieldError
    MALFORMED_TRACKING_URL_TEMPLATE: UrlFieldErrorEnum.UrlFieldError
    MISSING_HOST_IN_TRACKING_URL_TEMPLATE: UrlFieldErrorEnum.UrlFieldError
    INVALID_TLD_IN_TRACKING_URL_TEMPLATE: UrlFieldErrorEnum.UrlFieldError
    REDUNDANT_NESTED_TRACKING_URL_TEMPLATE_TAG: UrlFieldErrorEnum.UrlFieldError
    INVALID_FINAL_URL: UrlFieldErrorEnum.UrlFieldError
    INVALID_TAG_IN_FINAL_URL: UrlFieldErrorEnum.UrlFieldError
    REDUNDANT_NESTED_FINAL_URL_TAG: UrlFieldErrorEnum.UrlFieldError
    MISSING_PROTOCOL_IN_FINAL_URL: UrlFieldErrorEnum.UrlFieldError
    INVALID_PROTOCOL_IN_FINAL_URL: UrlFieldErrorEnum.UrlFieldError
    MALFORMED_FINAL_URL: UrlFieldErrorEnum.UrlFieldError
    MISSING_HOST_IN_FINAL_URL: UrlFieldErrorEnum.UrlFieldError
    INVALID_TLD_IN_FINAL_URL: UrlFieldErrorEnum.UrlFieldError
    INVALID_FINAL_MOBILE_URL: UrlFieldErrorEnum.UrlFieldError
    INVALID_TAG_IN_FINAL_MOBILE_URL: UrlFieldErrorEnum.UrlFieldError
    REDUNDANT_NESTED_FINAL_MOBILE_URL_TAG: UrlFieldErrorEnum.UrlFieldError
    MISSING_PROTOCOL_IN_FINAL_MOBILE_URL: UrlFieldErrorEnum.UrlFieldError
    INVALID_PROTOCOL_IN_FINAL_MOBILE_URL: UrlFieldErrorEnum.UrlFieldError
    MALFORMED_FINAL_MOBILE_URL: UrlFieldErrorEnum.UrlFieldError
    MISSING_HOST_IN_FINAL_MOBILE_URL: UrlFieldErrorEnum.UrlFieldError
    INVALID_TLD_IN_FINAL_MOBILE_URL: UrlFieldErrorEnum.UrlFieldError
    INVALID_FINAL_APP_URL: UrlFieldErrorEnum.UrlFieldError
    INVALID_TAG_IN_FINAL_APP_URL: UrlFieldErrorEnum.UrlFieldError
    REDUNDANT_NESTED_FINAL_APP_URL_TAG: UrlFieldErrorEnum.UrlFieldError
    MULTIPLE_APP_URLS_FOR_OSTYPE: UrlFieldErrorEnum.UrlFieldError
    INVALID_OSTYPE: UrlFieldErrorEnum.UrlFieldError
    INVALID_PROTOCOL_FOR_APP_URL: UrlFieldErrorEnum.UrlFieldError
    INVALID_PACKAGE_ID_FOR_APP_URL: UrlFieldErrorEnum.UrlFieldError
    URL_CUSTOM_PARAMETERS_COUNT_EXCEEDS_LIMIT: UrlFieldErrorEnum.UrlFieldError
    INVALID_CHARACTERS_IN_URL_CUSTOM_PARAMETER_KEY: UrlFieldErrorEnum.UrlFieldError
    INVALID_CHARACTERS_IN_URL_CUSTOM_PARAMETER_VALUE: UrlFieldErrorEnum.UrlFieldError
    INVALID_TAG_IN_URL_CUSTOM_PARAMETER_VALUE: UrlFieldErrorEnum.UrlFieldError
    REDUNDANT_NESTED_URL_CUSTOM_PARAMETER_TAG: UrlFieldErrorEnum.UrlFieldError
    MISSING_PROTOCOL: UrlFieldErrorEnum.UrlFieldError
    INVALID_PROTOCOL: UrlFieldErrorEnum.UrlFieldError
    INVALID_URL: UrlFieldErrorEnum.UrlFieldError
    DESTINATION_URL_DEPRECATED: UrlFieldErrorEnum.UrlFieldError
    INVALID_TAG_IN_URL: UrlFieldErrorEnum.UrlFieldError
    MISSING_URL_TAG: UrlFieldErrorEnum.UrlFieldError
    DUPLICATE_URL_ID: UrlFieldErrorEnum.UrlFieldError
    INVALID_URL_ID: UrlFieldErrorEnum.UrlFieldError
    FINAL_URL_SUFFIX_MALFORMED: UrlFieldErrorEnum.UrlFieldError
    INVALID_TAG_IN_FINAL_URL_SUFFIX: UrlFieldErrorEnum.UrlFieldError
    INVALID_TOP_LEVEL_DOMAIN: UrlFieldErrorEnum.UrlFieldError
    MALFORMED_TOP_LEVEL_DOMAIN: UrlFieldErrorEnum.UrlFieldError
    MALFORMED_URL: UrlFieldErrorEnum.UrlFieldError
    MISSING_HOST: UrlFieldErrorEnum.UrlFieldError
    NULL_CUSTOM_PARAMETER_VALUE: UrlFieldErrorEnum.UrlFieldError
    VALUE_TRACK_PARAMETER_NOT_SUPPORTED: UrlFieldErrorEnum.UrlFieldError

    def __init__(self) -> None:
        ...