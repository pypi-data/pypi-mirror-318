from google.ads.googleads.v17.enums import search_term_targeting_status_pb2 as _search_term_targeting_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchTermView(_message.Message):
    __slots__ = ("resource_name", "search_term", "ad_group", "status")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TERM_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    search_term: str
    ad_group: str
    status: _search_term_targeting_status_pb2.SearchTermTargetingStatusEnum.SearchTermTargetingStatus
    def __init__(self, resource_name: _Optional[str] = ..., search_term: _Optional[str] = ..., ad_group: _Optional[str] = ..., status: _Optional[_Union[_search_term_targeting_status_pb2.SearchTermTargetingStatusEnum.SearchTermTargetingStatus, str]] = ...) -> None: ...
