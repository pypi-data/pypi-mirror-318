from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class KeywordThemeConstant(_message.Message):
    __slots__ = ("resource_name", "country_code", "language_code", "display_name")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    country_code: str
    language_code: str
    display_name: str
    def __init__(self, resource_name: _Optional[str] = ..., country_code: _Optional[str] = ..., language_code: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...
