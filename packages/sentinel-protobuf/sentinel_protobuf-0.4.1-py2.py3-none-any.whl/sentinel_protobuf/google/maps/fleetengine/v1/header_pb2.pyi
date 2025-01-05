from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RequestHeader(_message.Message):
    __slots__ = ('language_code', 'region_code', 'sdk_version', 'os_version', 'device_model', 'sdk_type', 'maps_sdk_version', 'nav_sdk_version', 'platform', 'manufacturer', 'android_api_level', 'trace_id')

    class SdkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SDK_TYPE_UNSPECIFIED: _ClassVar[RequestHeader.SdkType]
        CONSUMER: _ClassVar[RequestHeader.SdkType]
        DRIVER: _ClassVar[RequestHeader.SdkType]
        JAVASCRIPT: _ClassVar[RequestHeader.SdkType]
    SDK_TYPE_UNSPECIFIED: RequestHeader.SdkType
    CONSUMER: RequestHeader.SdkType
    DRIVER: RequestHeader.SdkType
    JAVASCRIPT: RequestHeader.SdkType

    class Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLATFORM_UNSPECIFIED: _ClassVar[RequestHeader.Platform]
        ANDROID: _ClassVar[RequestHeader.Platform]
        IOS: _ClassVar[RequestHeader.Platform]
        WEB: _ClassVar[RequestHeader.Platform]
    PLATFORM_UNSPECIFIED: RequestHeader.Platform
    ANDROID: RequestHeader.Platform
    IOS: RequestHeader.Platform
    WEB: RequestHeader.Platform
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    SDK_VERSION_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MODEL_FIELD_NUMBER: _ClassVar[int]
    SDK_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAPS_SDK_VERSION_FIELD_NUMBER: _ClassVar[int]
    NAV_SDK_VERSION_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    ANDROID_API_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    language_code: str
    region_code: str
    sdk_version: str
    os_version: str
    device_model: str
    sdk_type: RequestHeader.SdkType
    maps_sdk_version: str
    nav_sdk_version: str
    platform: RequestHeader.Platform
    manufacturer: str
    android_api_level: int
    trace_id: str

    def __init__(self, language_code: _Optional[str]=..., region_code: _Optional[str]=..., sdk_version: _Optional[str]=..., os_version: _Optional[str]=..., device_model: _Optional[str]=..., sdk_type: _Optional[_Union[RequestHeader.SdkType, str]]=..., maps_sdk_version: _Optional[str]=..., nav_sdk_version: _Optional[str]=..., platform: _Optional[_Union[RequestHeader.Platform, str]]=..., manufacturer: _Optional[str]=..., android_api_level: _Optional[int]=..., trace_id: _Optional[str]=...) -> None:
        ...