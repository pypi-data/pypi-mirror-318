from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClickLocation(_message.Message):
    __slots__ = ("city", "country", "metro", "most_specific", "region")
    CITY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    METRO_FIELD_NUMBER: _ClassVar[int]
    MOST_SPECIFIC_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    city: str
    country: str
    metro: str
    most_specific: str
    region: str
    def __init__(self, city: _Optional[str] = ..., country: _Optional[str] = ..., metro: _Optional[str] = ..., most_specific: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...
