from google.ads.googleads.v17.common import feed_item_set_filter_type_infos_pb2 as _feed_item_set_filter_type_infos_pb2
from google.ads.googleads.v17.enums import feed_item_set_status_pb2 as _feed_item_set_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FeedItemSet(_message.Message):
    __slots__ = ('resource_name', 'feed', 'feed_item_set_id', 'display_name', 'status', 'dynamic_location_set_filter', 'dynamic_affiliate_location_set_filter')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    FEED_FIELD_NUMBER: _ClassVar[int]
    FEED_ITEM_SET_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_LOCATION_SET_FILTER_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_AFFILIATE_LOCATION_SET_FILTER_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    feed: str
    feed_item_set_id: int
    display_name: str
    status: _feed_item_set_status_pb2.FeedItemSetStatusEnum.FeedItemSetStatus
    dynamic_location_set_filter: _feed_item_set_filter_type_infos_pb2.DynamicLocationSetFilter
    dynamic_affiliate_location_set_filter: _feed_item_set_filter_type_infos_pb2.DynamicAffiliateLocationSetFilter

    def __init__(self, resource_name: _Optional[str]=..., feed: _Optional[str]=..., feed_item_set_id: _Optional[int]=..., display_name: _Optional[str]=..., status: _Optional[_Union[_feed_item_set_status_pb2.FeedItemSetStatusEnum.FeedItemSetStatus, str]]=..., dynamic_location_set_filter: _Optional[_Union[_feed_item_set_filter_type_infos_pb2.DynamicLocationSetFilter, _Mapping]]=..., dynamic_affiliate_location_set_filter: _Optional[_Union[_feed_item_set_filter_type_infos_pb2.DynamicAffiliateLocationSetFilter, _Mapping]]=...) -> None:
        ...