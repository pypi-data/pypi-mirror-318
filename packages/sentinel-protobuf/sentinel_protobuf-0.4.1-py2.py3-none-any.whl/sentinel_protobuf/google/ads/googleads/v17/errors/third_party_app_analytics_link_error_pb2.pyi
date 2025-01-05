from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ThirdPartyAppAnalyticsLinkErrorEnum(_message.Message):
    __slots__ = ()

    class ThirdPartyAppAnalyticsLinkError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ThirdPartyAppAnalyticsLinkErrorEnum.ThirdPartyAppAnalyticsLinkError]
        UNKNOWN: _ClassVar[ThirdPartyAppAnalyticsLinkErrorEnum.ThirdPartyAppAnalyticsLinkError]
        INVALID_ANALYTICS_PROVIDER_ID: _ClassVar[ThirdPartyAppAnalyticsLinkErrorEnum.ThirdPartyAppAnalyticsLinkError]
        INVALID_MOBILE_APP_ID: _ClassVar[ThirdPartyAppAnalyticsLinkErrorEnum.ThirdPartyAppAnalyticsLinkError]
        MOBILE_APP_IS_NOT_ENABLED: _ClassVar[ThirdPartyAppAnalyticsLinkErrorEnum.ThirdPartyAppAnalyticsLinkError]
        CANNOT_REGENERATE_SHAREABLE_LINK_ID_FOR_REMOVED_LINK: _ClassVar[ThirdPartyAppAnalyticsLinkErrorEnum.ThirdPartyAppAnalyticsLinkError]
    UNSPECIFIED: ThirdPartyAppAnalyticsLinkErrorEnum.ThirdPartyAppAnalyticsLinkError
    UNKNOWN: ThirdPartyAppAnalyticsLinkErrorEnum.ThirdPartyAppAnalyticsLinkError
    INVALID_ANALYTICS_PROVIDER_ID: ThirdPartyAppAnalyticsLinkErrorEnum.ThirdPartyAppAnalyticsLinkError
    INVALID_MOBILE_APP_ID: ThirdPartyAppAnalyticsLinkErrorEnum.ThirdPartyAppAnalyticsLinkError
    MOBILE_APP_IS_NOT_ENABLED: ThirdPartyAppAnalyticsLinkErrorEnum.ThirdPartyAppAnalyticsLinkError
    CANNOT_REGENERATE_SHAREABLE_LINK_ID_FOR_REMOVED_LINK: ThirdPartyAppAnalyticsLinkErrorEnum.ThirdPartyAppAnalyticsLinkError

    def __init__(self) -> None:
        ...