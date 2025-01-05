from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class FeedItemSetLink(_message.Message):
    __slots__ = ('resource_name', 'feed_item', 'feed_item_set')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    FEED_ITEM_FIELD_NUMBER: _ClassVar[int]
    FEED_ITEM_SET_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    feed_item: str
    feed_item_set: str

    def __init__(self, resource_name: _Optional[str]=..., feed_item: _Optional[str]=..., feed_item_set: _Optional[str]=...) -> None:
        ...