from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ClientInfo(_message.Message):
    __slots__ = ('application_id', 'application_version', 'platform', 'operating_system', 'api_client', 'device_model', 'language_code', 'operating_system_build')

    class Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLATFORM_UNSPECIFIED: _ClassVar[ClientInfo.Platform]
        EDITOR: _ClassVar[ClientInfo.Platform]
        MAC_OS: _ClassVar[ClientInfo.Platform]
        WINDOWS: _ClassVar[ClientInfo.Platform]
        LINUX: _ClassVar[ClientInfo.Platform]
        ANDROID: _ClassVar[ClientInfo.Platform]
        IOS: _ClassVar[ClientInfo.Platform]
        WEB_GL: _ClassVar[ClientInfo.Platform]
    PLATFORM_UNSPECIFIED: ClientInfo.Platform
    EDITOR: ClientInfo.Platform
    MAC_OS: ClientInfo.Platform
    WINDOWS: ClientInfo.Platform
    LINUX: ClientInfo.Platform
    ANDROID: ClientInfo.Platform
    IOS: ClientInfo.Platform
    WEB_GL: ClientInfo.Platform
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_VERSION_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    OPERATING_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    API_CLIENT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MODEL_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    OPERATING_SYSTEM_BUILD_FIELD_NUMBER: _ClassVar[int]
    application_id: str
    application_version: str
    platform: ClientInfo.Platform
    operating_system: str
    api_client: str
    device_model: str
    language_code: str
    operating_system_build: str

    def __init__(self, application_id: _Optional[str]=..., application_version: _Optional[str]=..., platform: _Optional[_Union[ClientInfo.Platform, str]]=..., operating_system: _Optional[str]=..., api_client: _Optional[str]=..., device_model: _Optional[str]=..., language_code: _Optional[str]=..., operating_system_build: _Optional[str]=...) -> None:
        ...