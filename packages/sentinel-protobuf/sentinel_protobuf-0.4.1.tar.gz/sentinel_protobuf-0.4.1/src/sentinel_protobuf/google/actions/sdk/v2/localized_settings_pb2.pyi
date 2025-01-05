from google.actions.sdk.v2 import theme_customization_pb2 as _theme_customization_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LocalizedSettings(_message.Message):
    __slots__ = ('display_name', 'pronunciation', 'short_description', 'full_description', 'small_logo_image', 'large_banner_image', 'developer_name', 'developer_email', 'terms_of_service_url', 'voice', 'voice_locale', 'privacy_policy_url', 'sample_invocations', 'theme_customization')
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PRONUNCIATION_FIELD_NUMBER: _ClassVar[int]
    SHORT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FULL_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SMALL_LOGO_IMAGE_FIELD_NUMBER: _ClassVar[int]
    LARGE_BANNER_IMAGE_FIELD_NUMBER: _ClassVar[int]
    DEVELOPER_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVELOPER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    TERMS_OF_SERVICE_URL_FIELD_NUMBER: _ClassVar[int]
    VOICE_FIELD_NUMBER: _ClassVar[int]
    VOICE_LOCALE_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_POLICY_URL_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_INVOCATIONS_FIELD_NUMBER: _ClassVar[int]
    THEME_CUSTOMIZATION_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    pronunciation: str
    short_description: str
    full_description: str
    small_logo_image: str
    large_banner_image: str
    developer_name: str
    developer_email: str
    terms_of_service_url: str
    voice: str
    voice_locale: str
    privacy_policy_url: str
    sample_invocations: _containers.RepeatedScalarFieldContainer[str]
    theme_customization: _theme_customization_pb2.ThemeCustomization

    def __init__(self, display_name: _Optional[str]=..., pronunciation: _Optional[str]=..., short_description: _Optional[str]=..., full_description: _Optional[str]=..., small_logo_image: _Optional[str]=..., large_banner_image: _Optional[str]=..., developer_name: _Optional[str]=..., developer_email: _Optional[str]=..., terms_of_service_url: _Optional[str]=..., voice: _Optional[str]=..., voice_locale: _Optional[str]=..., privacy_policy_url: _Optional[str]=..., sample_invocations: _Optional[_Iterable[str]]=..., theme_customization: _Optional[_Union[_theme_customization_pb2.ThemeCustomization, _Mapping]]=...) -> None:
        ...