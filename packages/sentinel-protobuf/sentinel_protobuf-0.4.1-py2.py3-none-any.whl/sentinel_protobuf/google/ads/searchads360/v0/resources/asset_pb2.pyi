from google.ads.searchads360.v0.common import asset_types_pb2 as _asset_types_pb2
from google.ads.searchads360.v0.enums import asset_engine_status_pb2 as _asset_engine_status_pb2
from google.ads.searchads360.v0.enums import asset_status_pb2 as _asset_status_pb2
from google.ads.searchads360.v0.enums import asset_type_pb2 as _asset_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Asset(_message.Message):
    __slots__ = ("resource_name", "id", "name", "type", "final_urls", "tracking_url_template", "status", "creation_time", "last_modified_time", "engine_status", "youtube_video_asset", "image_asset", "text_asset", "callout_asset", "sitelink_asset", "page_feed_asset", "mobile_app_asset", "call_asset", "call_to_action_asset", "location_asset")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FINAL_URLS_FIELD_NUMBER: _ClassVar[int]
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    ENGINE_STATUS_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_VIDEO_ASSET_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ASSET_FIELD_NUMBER: _ClassVar[int]
    TEXT_ASSET_FIELD_NUMBER: _ClassVar[int]
    CALLOUT_ASSET_FIELD_NUMBER: _ClassVar[int]
    SITELINK_ASSET_FIELD_NUMBER: _ClassVar[int]
    PAGE_FEED_ASSET_FIELD_NUMBER: _ClassVar[int]
    MOBILE_APP_ASSET_FIELD_NUMBER: _ClassVar[int]
    CALL_ASSET_FIELD_NUMBER: _ClassVar[int]
    CALL_TO_ACTION_ASSET_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ASSET_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    type: _asset_type_pb2.AssetTypeEnum.AssetType
    final_urls: _containers.RepeatedScalarFieldContainer[str]
    tracking_url_template: str
    status: _asset_status_pb2.AssetStatusEnum.AssetStatus
    creation_time: str
    last_modified_time: str
    engine_status: _asset_engine_status_pb2.AssetEngineStatusEnum.AssetEngineStatus
    youtube_video_asset: _asset_types_pb2.YoutubeVideoAsset
    image_asset: _asset_types_pb2.ImageAsset
    text_asset: _asset_types_pb2.TextAsset
    callout_asset: _asset_types_pb2.UnifiedCalloutAsset
    sitelink_asset: _asset_types_pb2.UnifiedSitelinkAsset
    page_feed_asset: _asset_types_pb2.UnifiedPageFeedAsset
    mobile_app_asset: _asset_types_pb2.MobileAppAsset
    call_asset: _asset_types_pb2.UnifiedCallAsset
    call_to_action_asset: _asset_types_pb2.CallToActionAsset
    location_asset: _asset_types_pb2.UnifiedLocationAsset
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., type: _Optional[_Union[_asset_type_pb2.AssetTypeEnum.AssetType, str]] = ..., final_urls: _Optional[_Iterable[str]] = ..., tracking_url_template: _Optional[str] = ..., status: _Optional[_Union[_asset_status_pb2.AssetStatusEnum.AssetStatus, str]] = ..., creation_time: _Optional[str] = ..., last_modified_time: _Optional[str] = ..., engine_status: _Optional[_Union[_asset_engine_status_pb2.AssetEngineStatusEnum.AssetEngineStatus, str]] = ..., youtube_video_asset: _Optional[_Union[_asset_types_pb2.YoutubeVideoAsset, _Mapping]] = ..., image_asset: _Optional[_Union[_asset_types_pb2.ImageAsset, _Mapping]] = ..., text_asset: _Optional[_Union[_asset_types_pb2.TextAsset, _Mapping]] = ..., callout_asset: _Optional[_Union[_asset_types_pb2.UnifiedCalloutAsset, _Mapping]] = ..., sitelink_asset: _Optional[_Union[_asset_types_pb2.UnifiedSitelinkAsset, _Mapping]] = ..., page_feed_asset: _Optional[_Union[_asset_types_pb2.UnifiedPageFeedAsset, _Mapping]] = ..., mobile_app_asset: _Optional[_Union[_asset_types_pb2.MobileAppAsset, _Mapping]] = ..., call_asset: _Optional[_Union[_asset_types_pb2.UnifiedCallAsset, _Mapping]] = ..., call_to_action_asset: _Optional[_Union[_asset_types_pb2.CallToActionAsset, _Mapping]] = ..., location_asset: _Optional[_Union[_asset_types_pb2.UnifiedLocationAsset, _Mapping]] = ...) -> None: ...
