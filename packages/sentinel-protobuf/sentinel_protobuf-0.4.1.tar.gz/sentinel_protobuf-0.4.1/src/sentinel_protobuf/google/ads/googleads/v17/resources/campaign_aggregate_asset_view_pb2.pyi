from google.ads.googleads.v17.enums import asset_field_type_pb2 as _asset_field_type_pb2
from google.ads.googleads.v17.enums import asset_source_pb2 as _asset_source_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CampaignAggregateAssetView(_message.Message):
    __slots__ = ("resource_name", "campaign", "asset", "asset_source", "field_type")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    ASSET_SOURCE_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    campaign: str
    asset: str
    asset_source: _asset_source_pb2.AssetSourceEnum.AssetSource
    field_type: _asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType
    def __init__(self, resource_name: _Optional[str] = ..., campaign: _Optional[str] = ..., asset: _Optional[str] = ..., asset_source: _Optional[_Union[_asset_source_pb2.AssetSourceEnum.AssetSource, str]] = ..., field_type: _Optional[_Union[_asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType, str]] = ...) -> None: ...
