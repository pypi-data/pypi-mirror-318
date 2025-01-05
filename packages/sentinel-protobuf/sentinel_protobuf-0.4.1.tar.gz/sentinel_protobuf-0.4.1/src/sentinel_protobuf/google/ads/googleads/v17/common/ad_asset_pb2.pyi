from google.ads.googleads.v17.common import asset_policy_pb2 as _asset_policy_pb2
from google.ads.googleads.v17.enums import asset_performance_label_pb2 as _asset_performance_label_pb2
from google.ads.googleads.v17.enums import served_asset_field_type_pb2 as _served_asset_field_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdTextAsset(_message.Message):
    __slots__ = ("text", "pinned_field", "asset_performance_label", "policy_summary_info")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    PINNED_FIELD_FIELD_NUMBER: _ClassVar[int]
    ASSET_PERFORMANCE_LABEL_FIELD_NUMBER: _ClassVar[int]
    POLICY_SUMMARY_INFO_FIELD_NUMBER: _ClassVar[int]
    text: str
    pinned_field: _served_asset_field_type_pb2.ServedAssetFieldTypeEnum.ServedAssetFieldType
    asset_performance_label: _asset_performance_label_pb2.AssetPerformanceLabelEnum.AssetPerformanceLabel
    policy_summary_info: _asset_policy_pb2.AdAssetPolicySummary
    def __init__(self, text: _Optional[str] = ..., pinned_field: _Optional[_Union[_served_asset_field_type_pb2.ServedAssetFieldTypeEnum.ServedAssetFieldType, str]] = ..., asset_performance_label: _Optional[_Union[_asset_performance_label_pb2.AssetPerformanceLabelEnum.AssetPerformanceLabel, str]] = ..., policy_summary_info: _Optional[_Union[_asset_policy_pb2.AdAssetPolicySummary, _Mapping]] = ...) -> None: ...

class AdImageAsset(_message.Message):
    __slots__ = ("asset",)
    ASSET_FIELD_NUMBER: _ClassVar[int]
    asset: str
    def __init__(self, asset: _Optional[str] = ...) -> None: ...

class AdVideoAsset(_message.Message):
    __slots__ = ("asset", "ad_video_asset_info")
    ASSET_FIELD_NUMBER: _ClassVar[int]
    AD_VIDEO_ASSET_INFO_FIELD_NUMBER: _ClassVar[int]
    asset: str
    ad_video_asset_info: AdVideoAssetInfo
    def __init__(self, asset: _Optional[str] = ..., ad_video_asset_info: _Optional[_Union[AdVideoAssetInfo, _Mapping]] = ...) -> None: ...

class AdVideoAssetInfo(_message.Message):
    __slots__ = ("ad_video_asset_inventory_preferences",)
    AD_VIDEO_ASSET_INVENTORY_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    ad_video_asset_inventory_preferences: AdVideoAssetInventoryPreferences
    def __init__(self, ad_video_asset_inventory_preferences: _Optional[_Union[AdVideoAssetInventoryPreferences, _Mapping]] = ...) -> None: ...

class AdVideoAssetInventoryPreferences(_message.Message):
    __slots__ = ("in_feed_preference", "in_stream_preference", "shorts_preference")
    IN_FEED_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    IN_STREAM_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    SHORTS_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    in_feed_preference: bool
    in_stream_preference: bool
    shorts_preference: bool
    def __init__(self, in_feed_preference: bool = ..., in_stream_preference: bool = ..., shorts_preference: bool = ...) -> None: ...

class AdMediaBundleAsset(_message.Message):
    __slots__ = ("asset",)
    ASSET_FIELD_NUMBER: _ClassVar[int]
    asset: str
    def __init__(self, asset: _Optional[str] = ...) -> None: ...

class AdDemandGenCarouselCardAsset(_message.Message):
    __slots__ = ("asset",)
    ASSET_FIELD_NUMBER: _ClassVar[int]
    asset: str
    def __init__(self, asset: _Optional[str] = ...) -> None: ...

class AdCallToActionAsset(_message.Message):
    __slots__ = ("asset",)
    ASSET_FIELD_NUMBER: _ClassVar[int]
    asset: str
    def __init__(self, asset: _Optional[str] = ...) -> None: ...
