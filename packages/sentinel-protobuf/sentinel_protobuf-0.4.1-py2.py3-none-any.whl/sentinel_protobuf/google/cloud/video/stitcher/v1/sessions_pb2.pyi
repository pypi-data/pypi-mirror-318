from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.video.stitcher.v1 import companions_pb2 as _companions_pb2
from google.cloud.video.stitcher.v1 import events_pb2 as _events_pb2
from google.cloud.video.stitcher.v1 import live_configs_pb2 as _live_configs_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class VodSession(_message.Message):
    __slots__ = ('name', 'interstitials', 'play_uri', 'source_uri', 'ad_tag_uri', 'ad_tag_macro_map', 'manifest_options', 'asset_id', 'ad_tracking', 'gam_settings', 'vod_config')

    class GamSettings(_message.Message):
        __slots__ = ('network_code', 'stream_id')
        NETWORK_CODE_FIELD_NUMBER: _ClassVar[int]
        STREAM_ID_FIELD_NUMBER: _ClassVar[int]
        network_code: str
        stream_id: str

        def __init__(self, network_code: _Optional[str]=..., stream_id: _Optional[str]=...) -> None:
            ...

    class AdTagMacroMapEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    INTERSTITIALS_FIELD_NUMBER: _ClassVar[int]
    PLAY_URI_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    AD_TAG_URI_FIELD_NUMBER: _ClassVar[int]
    AD_TAG_MACRO_MAP_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    AD_TRACKING_FIELD_NUMBER: _ClassVar[int]
    GAM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    VOD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    interstitials: Interstitials
    play_uri: str
    source_uri: str
    ad_tag_uri: str
    ad_tag_macro_map: _containers.ScalarMap[str, str]
    manifest_options: ManifestOptions
    asset_id: str
    ad_tracking: _live_configs_pb2.AdTracking
    gam_settings: VodSession.GamSettings
    vod_config: str

    def __init__(self, name: _Optional[str]=..., interstitials: _Optional[_Union[Interstitials, _Mapping]]=..., play_uri: _Optional[str]=..., source_uri: _Optional[str]=..., ad_tag_uri: _Optional[str]=..., ad_tag_macro_map: _Optional[_Mapping[str, str]]=..., manifest_options: _Optional[_Union[ManifestOptions, _Mapping]]=..., asset_id: _Optional[str]=..., ad_tracking: _Optional[_Union[_live_configs_pb2.AdTracking, str]]=..., gam_settings: _Optional[_Union[VodSession.GamSettings, _Mapping]]=..., vod_config: _Optional[str]=...) -> None:
        ...

class Interstitials(_message.Message):
    __slots__ = ('ad_breaks', 'session_content')
    AD_BREAKS_FIELD_NUMBER: _ClassVar[int]
    SESSION_CONTENT_FIELD_NUMBER: _ClassVar[int]
    ad_breaks: _containers.RepeatedCompositeFieldContainer[VodSessionAdBreak]
    session_content: VodSessionContent

    def __init__(self, ad_breaks: _Optional[_Iterable[_Union[VodSessionAdBreak, _Mapping]]]=..., session_content: _Optional[_Union[VodSessionContent, _Mapping]]=...) -> None:
        ...

class VodSessionAd(_message.Message):
    __slots__ = ('duration', 'companion_ads', 'activity_events')
    DURATION_FIELD_NUMBER: _ClassVar[int]
    COMPANION_ADS_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_EVENTS_FIELD_NUMBER: _ClassVar[int]
    duration: _duration_pb2.Duration
    companion_ads: _companions_pb2.CompanionAds
    activity_events: _containers.RepeatedCompositeFieldContainer[_events_pb2.Event]

    def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., companion_ads: _Optional[_Union[_companions_pb2.CompanionAds, _Mapping]]=..., activity_events: _Optional[_Iterable[_Union[_events_pb2.Event, _Mapping]]]=...) -> None:
        ...

class VodSessionContent(_message.Message):
    __slots__ = ('duration',)
    DURATION_FIELD_NUMBER: _ClassVar[int]
    duration: _duration_pb2.Duration

    def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class VodSessionAdBreak(_message.Message):
    __slots__ = ('progress_events', 'ads', 'end_time_offset', 'start_time_offset')
    PROGRESS_EVENTS_FIELD_NUMBER: _ClassVar[int]
    ADS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    START_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    progress_events: _containers.RepeatedCompositeFieldContainer[_events_pb2.ProgressEvent]
    ads: _containers.RepeatedCompositeFieldContainer[VodSessionAd]
    end_time_offset: _duration_pb2.Duration
    start_time_offset: _duration_pb2.Duration

    def __init__(self, progress_events: _Optional[_Iterable[_Union[_events_pb2.ProgressEvent, _Mapping]]]=..., ads: _Optional[_Iterable[_Union[VodSessionAd, _Mapping]]]=..., end_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., start_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class LiveSession(_message.Message):
    __slots__ = ('name', 'play_uri', 'ad_tag_macros', 'manifest_options', 'gam_settings', 'live_config', 'ad_tracking')

    class GamSettings(_message.Message):
        __slots__ = ('stream_id', 'targeting_parameters')

        class TargetingParametersEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        STREAM_ID_FIELD_NUMBER: _ClassVar[int]
        TARGETING_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        stream_id: str
        targeting_parameters: _containers.ScalarMap[str, str]

        def __init__(self, stream_id: _Optional[str]=..., targeting_parameters: _Optional[_Mapping[str, str]]=...) -> None:
            ...

    class AdTagMacrosEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PLAY_URI_FIELD_NUMBER: _ClassVar[int]
    AD_TAG_MACROS_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    GAM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    LIVE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AD_TRACKING_FIELD_NUMBER: _ClassVar[int]
    name: str
    play_uri: str
    ad_tag_macros: _containers.ScalarMap[str, str]
    manifest_options: ManifestOptions
    gam_settings: LiveSession.GamSettings
    live_config: str
    ad_tracking: _live_configs_pb2.AdTracking

    def __init__(self, name: _Optional[str]=..., play_uri: _Optional[str]=..., ad_tag_macros: _Optional[_Mapping[str, str]]=..., manifest_options: _Optional[_Union[ManifestOptions, _Mapping]]=..., gam_settings: _Optional[_Union[LiveSession.GamSettings, _Mapping]]=..., live_config: _Optional[str]=..., ad_tracking: _Optional[_Union[_live_configs_pb2.AdTracking, str]]=...) -> None:
        ...

class ManifestOptions(_message.Message):
    __slots__ = ('include_renditions', 'bitrate_order')

    class OrderPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ORDER_POLICY_UNSPECIFIED: _ClassVar[ManifestOptions.OrderPolicy]
        ASCENDING: _ClassVar[ManifestOptions.OrderPolicy]
        DESCENDING: _ClassVar[ManifestOptions.OrderPolicy]
    ORDER_POLICY_UNSPECIFIED: ManifestOptions.OrderPolicy
    ASCENDING: ManifestOptions.OrderPolicy
    DESCENDING: ManifestOptions.OrderPolicy
    INCLUDE_RENDITIONS_FIELD_NUMBER: _ClassVar[int]
    BITRATE_ORDER_FIELD_NUMBER: _ClassVar[int]
    include_renditions: _containers.RepeatedCompositeFieldContainer[RenditionFilter]
    bitrate_order: ManifestOptions.OrderPolicy

    def __init__(self, include_renditions: _Optional[_Iterable[_Union[RenditionFilter, _Mapping]]]=..., bitrate_order: _Optional[_Union[ManifestOptions.OrderPolicy, str]]=...) -> None:
        ...

class RenditionFilter(_message.Message):
    __slots__ = ('bitrate_bps', 'codecs')
    BITRATE_BPS_FIELD_NUMBER: _ClassVar[int]
    CODECS_FIELD_NUMBER: _ClassVar[int]
    bitrate_bps: int
    codecs: str

    def __init__(self, bitrate_bps: _Optional[int]=..., codecs: _Optional[str]=...) -> None:
        ...