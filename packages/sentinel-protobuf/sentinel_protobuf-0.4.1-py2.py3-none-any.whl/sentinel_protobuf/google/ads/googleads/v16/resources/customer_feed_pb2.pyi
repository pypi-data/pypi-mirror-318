from google.ads.googleads.v16.common import matching_function_pb2 as _matching_function_pb2
from google.ads.googleads.v16.enums import feed_link_status_pb2 as _feed_link_status_pb2
from google.ads.googleads.v16.enums import placeholder_type_pb2 as _placeholder_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CustomerFeed(_message.Message):
    __slots__ = ("resource_name", "feed", "placeholder_types", "matching_function", "status")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    FEED_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_TYPES_FIELD_NUMBER: _ClassVar[int]
    MATCHING_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    feed: str
    placeholder_types: _containers.RepeatedScalarFieldContainer[_placeholder_type_pb2.PlaceholderTypeEnum.PlaceholderType]
    matching_function: _matching_function_pb2.MatchingFunction
    status: _feed_link_status_pb2.FeedLinkStatusEnum.FeedLinkStatus
    def __init__(self, resource_name: _Optional[str] = ..., feed: _Optional[str] = ..., placeholder_types: _Optional[_Iterable[_Union[_placeholder_type_pb2.PlaceholderTypeEnum.PlaceholderType, str]]] = ..., matching_function: _Optional[_Union[_matching_function_pb2.MatchingFunction, _Mapping]] = ..., status: _Optional[_Union[_feed_link_status_pb2.FeedLinkStatusEnum.FeedLinkStatus, str]] = ...) -> None: ...
