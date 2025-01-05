from google.ads.googleads.v16.common import asset_usage_pb2 as _asset_usage_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupAdAssetCombinationView(_message.Message):
    __slots__ = ("resource_name", "served_assets", "enabled")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVED_ASSETS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    served_assets: _containers.RepeatedCompositeFieldContainer[_asset_usage_pb2.AssetUsage]
    enabled: bool
    def __init__(self, resource_name: _Optional[str] = ..., served_assets: _Optional[_Iterable[_Union[_asset_usage_pb2.AssetUsage, _Mapping]]] = ..., enabled: bool = ...) -> None: ...
