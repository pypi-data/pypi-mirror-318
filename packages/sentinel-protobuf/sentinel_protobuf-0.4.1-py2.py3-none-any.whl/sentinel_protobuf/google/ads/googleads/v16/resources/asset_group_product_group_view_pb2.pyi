from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class AssetGroupProductGroupView(_message.Message):
    __slots__ = ('resource_name', 'asset_group', 'asset_group_listing_group_filter')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_GROUP_FIELD_NUMBER: _ClassVar[int]
    ASSET_GROUP_LISTING_GROUP_FILTER_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    asset_group: str
    asset_group_listing_group_filter: str

    def __init__(self, resource_name: _Optional[str]=..., asset_group: _Optional[str]=..., asset_group_listing_group_filter: _Optional[str]=...) -> None:
        ...