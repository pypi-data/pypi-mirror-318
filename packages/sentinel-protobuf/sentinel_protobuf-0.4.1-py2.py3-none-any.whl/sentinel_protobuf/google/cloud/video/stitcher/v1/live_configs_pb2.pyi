from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.video.stitcher.v1 import fetch_options_pb2 as _fetch_options_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AdTracking(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AD_TRACKING_UNSPECIFIED: _ClassVar[AdTracking]
    CLIENT: _ClassVar[AdTracking]
    SERVER: _ClassVar[AdTracking]
AD_TRACKING_UNSPECIFIED: AdTracking
CLIENT: AdTracking
SERVER: AdTracking

class LiveConfig(_message.Message):
    __slots__ = ('name', 'source_uri', 'ad_tag_uri', 'gam_live_config', 'state', 'ad_tracking', 'default_slate', 'stitching_policy', 'prefetch_config', 'source_fetch_options')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[LiveConfig.State]
        CREATING: _ClassVar[LiveConfig.State]
        READY: _ClassVar[LiveConfig.State]
        DELETING: _ClassVar[LiveConfig.State]
    STATE_UNSPECIFIED: LiveConfig.State
    CREATING: LiveConfig.State
    READY: LiveConfig.State
    DELETING: LiveConfig.State

    class StitchingPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STITCHING_POLICY_UNSPECIFIED: _ClassVar[LiveConfig.StitchingPolicy]
        CUT_CURRENT: _ClassVar[LiveConfig.StitchingPolicy]
        COMPLETE_AD: _ClassVar[LiveConfig.StitchingPolicy]
    STITCHING_POLICY_UNSPECIFIED: LiveConfig.StitchingPolicy
    CUT_CURRENT: LiveConfig.StitchingPolicy
    COMPLETE_AD: LiveConfig.StitchingPolicy
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    AD_TAG_URI_FIELD_NUMBER: _ClassVar[int]
    GAM_LIVE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    AD_TRACKING_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SLATE_FIELD_NUMBER: _ClassVar[int]
    STITCHING_POLICY_FIELD_NUMBER: _ClassVar[int]
    PREFETCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FETCH_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    source_uri: str
    ad_tag_uri: str
    gam_live_config: GamLiveConfig
    state: LiveConfig.State
    ad_tracking: AdTracking
    default_slate: str
    stitching_policy: LiveConfig.StitchingPolicy
    prefetch_config: PrefetchConfig
    source_fetch_options: _fetch_options_pb2.FetchOptions

    def __init__(self, name: _Optional[str]=..., source_uri: _Optional[str]=..., ad_tag_uri: _Optional[str]=..., gam_live_config: _Optional[_Union[GamLiveConfig, _Mapping]]=..., state: _Optional[_Union[LiveConfig.State, str]]=..., ad_tracking: _Optional[_Union[AdTracking, str]]=..., default_slate: _Optional[str]=..., stitching_policy: _Optional[_Union[LiveConfig.StitchingPolicy, str]]=..., prefetch_config: _Optional[_Union[PrefetchConfig, _Mapping]]=..., source_fetch_options: _Optional[_Union[_fetch_options_pb2.FetchOptions, _Mapping]]=...) -> None:
        ...

class PrefetchConfig(_message.Message):
    __slots__ = ('enabled', 'initial_ad_request_duration')
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    INITIAL_AD_REQUEST_DURATION_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    initial_ad_request_duration: _duration_pb2.Duration

    def __init__(self, enabled: bool=..., initial_ad_request_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class GamLiveConfig(_message.Message):
    __slots__ = ('network_code', 'asset_key', 'custom_asset_key')
    NETWORK_CODE_FIELD_NUMBER: _ClassVar[int]
    ASSET_KEY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ASSET_KEY_FIELD_NUMBER: _ClassVar[int]
    network_code: str
    asset_key: str
    custom_asset_key: str

    def __init__(self, network_code: _Optional[str]=..., asset_key: _Optional[str]=..., custom_asset_key: _Optional[str]=...) -> None:
        ...