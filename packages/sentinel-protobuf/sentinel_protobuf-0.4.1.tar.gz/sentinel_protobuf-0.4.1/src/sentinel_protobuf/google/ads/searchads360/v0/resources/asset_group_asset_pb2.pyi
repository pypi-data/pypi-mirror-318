from google.ads.searchads360.v0.enums import asset_field_type_pb2 as _asset_field_type_pb2
from google.ads.searchads360.v0.enums import asset_link_status_pb2 as _asset_link_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AssetGroupAsset(_message.Message):
    __slots__ = ('resource_name', 'asset_group', 'asset', 'field_type', 'status')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_GROUP_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    asset_group: str
    asset: str
    field_type: _asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType
    status: _asset_link_status_pb2.AssetLinkStatusEnum.AssetLinkStatus

    def __init__(self, resource_name: _Optional[str]=..., asset_group: _Optional[str]=..., asset: _Optional[str]=..., field_type: _Optional[_Union[_asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType, str]]=..., status: _Optional[_Union[_asset_link_status_pb2.AssetLinkStatusEnum.AssetLinkStatus, str]]=...) -> None:
        ...