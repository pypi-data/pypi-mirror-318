from google.ads.googleads.v16.common import asset_policy_pb2 as _asset_policy_pb2
from google.ads.googleads.v16.enums import asset_performance_label_pb2 as _asset_performance_label_pb2
from google.ads.googleads.v16.enums import served_asset_field_type_pb2 as _served_asset_field_type_pb2
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
    __slots__ = ("asset",)
    ASSET_FIELD_NUMBER: _ClassVar[int]
    asset: str
    def __init__(self, asset: _Optional[str] = ...) -> None: ...

class AdMediaBundleAsset(_message.Message):
    __slots__ = ("asset",)
    ASSET_FIELD_NUMBER: _ClassVar[int]
    asset: str
    def __init__(self, asset: _Optional[str] = ...) -> None: ...

class AdDiscoveryCarouselCardAsset(_message.Message):
    __slots__ = ("asset",)
    ASSET_FIELD_NUMBER: _ClassVar[int]
    asset: str
    def __init__(self, asset: _Optional[str] = ...) -> None: ...

class AdCallToActionAsset(_message.Message):
    __slots__ = ("asset",)
    ASSET_FIELD_NUMBER: _ClassVar[int]
    asset: str
    def __init__(self, asset: _Optional[str] = ...) -> None: ...
