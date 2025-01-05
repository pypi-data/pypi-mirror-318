from google.ads.searchads360.v0.enums import served_asset_field_type_pb2 as _served_asset_field_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AssetUsage(_message.Message):
    __slots__ = ('asset', 'served_asset_field_type')
    ASSET_FIELD_NUMBER: _ClassVar[int]
    SERVED_ASSET_FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    asset: str
    served_asset_field_type: _served_asset_field_type_pb2.ServedAssetFieldTypeEnum.ServedAssetFieldType

    def __init__(self, asset: _Optional[str]=..., served_asset_field_type: _Optional[_Union[_served_asset_field_type_pb2.ServedAssetFieldTypeEnum.ServedAssetFieldType, str]]=...) -> None:
        ...