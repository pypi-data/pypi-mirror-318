from google.ads.googleads.v18.enums import app_url_operating_system_type_pb2 as _app_url_operating_system_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FinalAppUrl(_message.Message):
    __slots__ = ("os_type", "url")
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    os_type: _app_url_operating_system_type_pb2.AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType
    url: str
    def __init__(self, os_type: _Optional[_Union[_app_url_operating_system_type_pb2.AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType, str]] = ..., url: _Optional[str] = ...) -> None: ...
