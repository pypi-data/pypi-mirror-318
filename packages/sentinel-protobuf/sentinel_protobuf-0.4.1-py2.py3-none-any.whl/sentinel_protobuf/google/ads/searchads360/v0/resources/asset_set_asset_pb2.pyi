from google.ads.searchads360.v0.enums import asset_set_asset_status_pb2 as _asset_set_asset_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AssetSetAsset(_message.Message):
    __slots__ = ('resource_name', 'asset_set', 'asset', 'status')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_SET_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    asset_set: str
    asset: str
    status: _asset_set_asset_status_pb2.AssetSetAssetStatusEnum.AssetSetAssetStatus

    def __init__(self, resource_name: _Optional[str]=..., asset_set: _Optional[str]=..., asset: _Optional[str]=..., status: _Optional[_Union[_asset_set_asset_status_pb2.AssetSetAssetStatusEnum.AssetSetAssetStatus, str]]=...) -> None:
        ...