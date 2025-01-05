from google.ads.searchads360.v0.common import asset_usage_pb2 as _asset_usage_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AssetGroupTopCombinationView(_message.Message):
    __slots__ = ('resource_name', 'asset_group_top_combinations')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_GROUP_TOP_COMBINATIONS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    asset_group_top_combinations: _containers.RepeatedCompositeFieldContainer[AssetGroupAssetCombinationData]

    def __init__(self, resource_name: _Optional[str]=..., asset_group_top_combinations: _Optional[_Iterable[_Union[AssetGroupAssetCombinationData, _Mapping]]]=...) -> None:
        ...

class AssetGroupAssetCombinationData(_message.Message):
    __slots__ = ('asset_combination_served_assets',)
    ASSET_COMBINATION_SERVED_ASSETS_FIELD_NUMBER: _ClassVar[int]
    asset_combination_served_assets: _containers.RepeatedCompositeFieldContainer[_asset_usage_pb2.AssetUsage]

    def __init__(self, asset_combination_served_assets: _Optional[_Iterable[_Union[_asset_usage_pb2.AssetUsage, _Mapping]]]=...) -> None:
        ...