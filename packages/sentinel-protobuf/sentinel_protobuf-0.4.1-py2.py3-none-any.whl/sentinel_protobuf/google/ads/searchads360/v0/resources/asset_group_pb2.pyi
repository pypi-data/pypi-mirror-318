from google.ads.searchads360.v0.enums import ad_strength_pb2 as _ad_strength_pb2
from google.ads.searchads360.v0.enums import asset_group_status_pb2 as _asset_group_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AssetGroup(_message.Message):
    __slots__ = ('resource_name', 'id', 'campaign', 'name', 'final_urls', 'final_mobile_urls', 'status', 'path1', 'path2', 'ad_strength')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FINAL_URLS_FIELD_NUMBER: _ClassVar[int]
    FINAL_MOBILE_URLS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PATH1_FIELD_NUMBER: _ClassVar[int]
    PATH2_FIELD_NUMBER: _ClassVar[int]
    AD_STRENGTH_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    campaign: str
    name: str
    final_urls: _containers.RepeatedScalarFieldContainer[str]
    final_mobile_urls: _containers.RepeatedScalarFieldContainer[str]
    status: _asset_group_status_pb2.AssetGroupStatusEnum.AssetGroupStatus
    path1: str
    path2: str
    ad_strength: _ad_strength_pb2.AdStrengthEnum.AdStrength

    def __init__(self, resource_name: _Optional[str]=..., id: _Optional[int]=..., campaign: _Optional[str]=..., name: _Optional[str]=..., final_urls: _Optional[_Iterable[str]]=..., final_mobile_urls: _Optional[_Iterable[str]]=..., status: _Optional[_Union[_asset_group_status_pb2.AssetGroupStatusEnum.AssetGroupStatus, str]]=..., path1: _Optional[str]=..., path2: _Optional[str]=..., ad_strength: _Optional[_Union[_ad_strength_pb2.AdStrengthEnum.AdStrength, str]]=...) -> None:
        ...