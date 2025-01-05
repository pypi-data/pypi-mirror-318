from google.ads.googleads.v18.enums import tracking_code_page_format_pb2 as _tracking_code_page_format_pb2
from google.ads.googleads.v18.enums import tracking_code_type_pb2 as _tracking_code_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TagSnippet(_message.Message):
    __slots__ = ("type", "page_format", "global_site_tag", "event_snippet")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_SITE_TAG_FIELD_NUMBER: _ClassVar[int]
    EVENT_SNIPPET_FIELD_NUMBER: _ClassVar[int]
    type: _tracking_code_type_pb2.TrackingCodeTypeEnum.TrackingCodeType
    page_format: _tracking_code_page_format_pb2.TrackingCodePageFormatEnum.TrackingCodePageFormat
    global_site_tag: str
    event_snippet: str
    def __init__(self, type: _Optional[_Union[_tracking_code_type_pb2.TrackingCodeTypeEnum.TrackingCodeType, str]] = ..., page_format: _Optional[_Union[_tracking_code_page_format_pb2.TrackingCodePageFormatEnum.TrackingCodePageFormat, str]] = ..., global_site_tag: _Optional[str] = ..., event_snippet: _Optional[str] = ...) -> None: ...
