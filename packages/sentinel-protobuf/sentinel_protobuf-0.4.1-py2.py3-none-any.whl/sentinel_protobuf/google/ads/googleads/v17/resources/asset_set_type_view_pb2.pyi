from google.ads.googleads.v17.enums import asset_set_type_pb2 as _asset_set_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AssetSetTypeView(_message.Message):
    __slots__ = ('resource_name', 'asset_set_type')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_SET_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    asset_set_type: _asset_set_type_pb2.AssetSetTypeEnum.AssetSetType

    def __init__(self, resource_name: _Optional[str]=..., asset_set_type: _Optional[_Union[_asset_set_type_pb2.AssetSetTypeEnum.AssetSetType, str]]=...) -> None:
        ...