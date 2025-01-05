from google.ads.googleads.v18.enums import asset_field_type_pb2 as _asset_field_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AssetFieldTypeView(_message.Message):
    __slots__ = ('resource_name', 'field_type')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    field_type: _asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType

    def __init__(self, resource_name: _Optional[str]=..., field_type: _Optional[_Union[_asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType, str]]=...) -> None:
        ...