from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.video.livestream.v1 import outputs_pb2 as _outputs_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Input(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'type', 'tier', 'uri', 'preprocessing_config', 'security_rules', 'input_stream_property')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Input.Type]
        RTMP_PUSH: _ClassVar[Input.Type]
        SRT_PUSH: _ClassVar[Input.Type]
    TYPE_UNSPECIFIED: Input.Type
    RTMP_PUSH: Input.Type
    SRT_PUSH: Input.Type

    class Tier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIER_UNSPECIFIED: _ClassVar[Input.Tier]
        SD: _ClassVar[Input.Tier]
        HD: _ClassVar[Input.Tier]
        UHD: _ClassVar[Input.Tier]
    TIER_UNSPECIFIED: Input.Tier
    SD: Input.Tier
    HD: Input.Tier
    UHD: Input.Tier

    class SecurityRule(_message.Message):
        __slots__ = ('ip_ranges',)
        IP_RANGES_FIELD_NUMBER: _ClassVar[int]
        ip_ranges: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, ip_ranges: _Optional[_Iterable[str]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    PREPROCESSING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SECURITY_RULES_FIELD_NUMBER: _ClassVar[int]
    INPUT_STREAM_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    type: Input.Type
    tier: Input.Tier
    uri: str
    preprocessing_config: _outputs_pb2.PreprocessingConfig
    security_rules: Input.SecurityRule
    input_stream_property: InputStreamProperty

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., type: _Optional[_Union[Input.Type, str]]=..., tier: _Optional[_Union[Input.Tier, str]]=..., uri: _Optional[str]=..., preprocessing_config: _Optional[_Union[_outputs_pb2.PreprocessingConfig, _Mapping]]=..., security_rules: _Optional[_Union[Input.SecurityRule, _Mapping]]=..., input_stream_property: _Optional[_Union[InputStreamProperty, _Mapping]]=...) -> None:
        ...

class Channel(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'input_attachments', 'active_input', 'output', 'elementary_streams', 'mux_streams', 'manifests', 'sprite_sheets', 'streaming_state', 'streaming_error', 'log_config', 'timecode_config', 'encryptions', 'input_config', 'retention_config', 'static_overlays')

    class StreamingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STREAMING_STATE_UNSPECIFIED: _ClassVar[Channel.StreamingState]
        STREAMING: _ClassVar[Channel.StreamingState]
        AWAITING_INPUT: _ClassVar[Channel.StreamingState]
        STREAMING_ERROR: _ClassVar[Channel.StreamingState]
        STREAMING_NO_INPUT: _ClassVar[Channel.StreamingState]
        STOPPED: _ClassVar[Channel.StreamingState]
        STARTING: _ClassVar[Channel.StreamingState]
        STOPPING: _ClassVar[Channel.StreamingState]
    STREAMING_STATE_UNSPECIFIED: Channel.StreamingState
    STREAMING: Channel.StreamingState
    AWAITING_INPUT: Channel.StreamingState
    STREAMING_ERROR: Channel.StreamingState
    STREAMING_NO_INPUT: Channel.StreamingState
    STOPPED: Channel.StreamingState
    STARTING: Channel.StreamingState
    STOPPING: Channel.StreamingState

    class Output(_message.Message):
        __slots__ = ('uri',)
        URI_FIELD_NUMBER: _ClassVar[int]
        uri: str

        def __init__(self, uri: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    INPUT_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_INPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    ELEMENTARY_STREAMS_FIELD_NUMBER: _ClassVar[int]
    MUX_STREAMS_FIELD_NUMBER: _ClassVar[int]
    MANIFESTS_FIELD_NUMBER: _ClassVar[int]
    SPRITE_SHEETS_FIELD_NUMBER: _ClassVar[int]
    STREAMING_STATE_FIELD_NUMBER: _ClassVar[int]
    STREAMING_ERROR_FIELD_NUMBER: _ClassVar[int]
    LOG_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TIMECODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTIONS_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RETENTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATIC_OVERLAYS_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    input_attachments: _containers.RepeatedCompositeFieldContainer[InputAttachment]
    active_input: str
    output: Channel.Output
    elementary_streams: _containers.RepeatedCompositeFieldContainer[_outputs_pb2.ElementaryStream]
    mux_streams: _containers.RepeatedCompositeFieldContainer[_outputs_pb2.MuxStream]
    manifests: _containers.RepeatedCompositeFieldContainer[_outputs_pb2.Manifest]
    sprite_sheets: _containers.RepeatedCompositeFieldContainer[_outputs_pb2.SpriteSheet]
    streaming_state: Channel.StreamingState
    streaming_error: _status_pb2.Status
    log_config: LogConfig
    timecode_config: _outputs_pb2.TimecodeConfig
    encryptions: _containers.RepeatedCompositeFieldContainer[Encryption]
    input_config: InputConfig
    retention_config: RetentionConfig
    static_overlays: _containers.RepeatedCompositeFieldContainer[StaticOverlay]

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., input_attachments: _Optional[_Iterable[_Union[InputAttachment, _Mapping]]]=..., active_input: _Optional[str]=..., output: _Optional[_Union[Channel.Output, _Mapping]]=..., elementary_streams: _Optional[_Iterable[_Union[_outputs_pb2.ElementaryStream, _Mapping]]]=..., mux_streams: _Optional[_Iterable[_Union[_outputs_pb2.MuxStream, _Mapping]]]=..., manifests: _Optional[_Iterable[_Union[_outputs_pb2.Manifest, _Mapping]]]=..., sprite_sheets: _Optional[_Iterable[_Union[_outputs_pb2.SpriteSheet, _Mapping]]]=..., streaming_state: _Optional[_Union[Channel.StreamingState, str]]=..., streaming_error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., log_config: _Optional[_Union[LogConfig, _Mapping]]=..., timecode_config: _Optional[_Union[_outputs_pb2.TimecodeConfig, _Mapping]]=..., encryptions: _Optional[_Iterable[_Union[Encryption, _Mapping]]]=..., input_config: _Optional[_Union[InputConfig, _Mapping]]=..., retention_config: _Optional[_Union[RetentionConfig, _Mapping]]=..., static_overlays: _Optional[_Iterable[_Union[StaticOverlay, _Mapping]]]=...) -> None:
        ...

class NormalizedCoordinate(_message.Message):
    __slots__ = ('x', 'y')
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float

    def __init__(self, x: _Optional[float]=..., y: _Optional[float]=...) -> None:
        ...

class NormalizedResolution(_message.Message):
    __slots__ = ('w', 'h')
    W_FIELD_NUMBER: _ClassVar[int]
    H_FIELD_NUMBER: _ClassVar[int]
    w: float
    h: float

    def __init__(self, w: _Optional[float]=..., h: _Optional[float]=...) -> None:
        ...

class StaticOverlay(_message.Message):
    __slots__ = ('asset', 'resolution', 'position', 'opacity')
    ASSET_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    OPACITY_FIELD_NUMBER: _ClassVar[int]
    asset: str
    resolution: NormalizedResolution
    position: NormalizedCoordinate
    opacity: float

    def __init__(self, asset: _Optional[str]=..., resolution: _Optional[_Union[NormalizedResolution, _Mapping]]=..., position: _Optional[_Union[NormalizedCoordinate, _Mapping]]=..., opacity: _Optional[float]=...) -> None:
        ...

class InputConfig(_message.Message):
    __slots__ = ('input_switch_mode',)

    class InputSwitchMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INPUT_SWITCH_MODE_UNSPECIFIED: _ClassVar[InputConfig.InputSwitchMode]
        FAILOVER_PREFER_PRIMARY: _ClassVar[InputConfig.InputSwitchMode]
        MANUAL: _ClassVar[InputConfig.InputSwitchMode]
    INPUT_SWITCH_MODE_UNSPECIFIED: InputConfig.InputSwitchMode
    FAILOVER_PREFER_PRIMARY: InputConfig.InputSwitchMode
    MANUAL: InputConfig.InputSwitchMode
    INPUT_SWITCH_MODE_FIELD_NUMBER: _ClassVar[int]
    input_switch_mode: InputConfig.InputSwitchMode

    def __init__(self, input_switch_mode: _Optional[_Union[InputConfig.InputSwitchMode, str]]=...) -> None:
        ...

class LogConfig(_message.Message):
    __slots__ = ('log_severity',)

    class LogSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOG_SEVERITY_UNSPECIFIED: _ClassVar[LogConfig.LogSeverity]
        OFF: _ClassVar[LogConfig.LogSeverity]
        DEBUG: _ClassVar[LogConfig.LogSeverity]
        INFO: _ClassVar[LogConfig.LogSeverity]
        WARNING: _ClassVar[LogConfig.LogSeverity]
        ERROR: _ClassVar[LogConfig.LogSeverity]
    LOG_SEVERITY_UNSPECIFIED: LogConfig.LogSeverity
    OFF: LogConfig.LogSeverity
    DEBUG: LogConfig.LogSeverity
    INFO: LogConfig.LogSeverity
    WARNING: LogConfig.LogSeverity
    ERROR: LogConfig.LogSeverity
    LOG_SEVERITY_FIELD_NUMBER: _ClassVar[int]
    log_severity: LogConfig.LogSeverity

    def __init__(self, log_severity: _Optional[_Union[LogConfig.LogSeverity, str]]=...) -> None:
        ...

class RetentionConfig(_message.Message):
    __slots__ = ('retention_window_duration',)
    RETENTION_WINDOW_DURATION_FIELD_NUMBER: _ClassVar[int]
    retention_window_duration: _duration_pb2.Duration

    def __init__(self, retention_window_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class InputStreamProperty(_message.Message):
    __slots__ = ('last_establish_time', 'video_streams', 'audio_streams')
    LAST_ESTABLISH_TIME_FIELD_NUMBER: _ClassVar[int]
    VIDEO_STREAMS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_STREAMS_FIELD_NUMBER: _ClassVar[int]
    last_establish_time: _timestamp_pb2.Timestamp
    video_streams: _containers.RepeatedCompositeFieldContainer[VideoStreamProperty]
    audio_streams: _containers.RepeatedCompositeFieldContainer[AudioStreamProperty]

    def __init__(self, last_establish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., video_streams: _Optional[_Iterable[_Union[VideoStreamProperty, _Mapping]]]=..., audio_streams: _Optional[_Iterable[_Union[AudioStreamProperty, _Mapping]]]=...) -> None:
        ...

class VideoStreamProperty(_message.Message):
    __slots__ = ('index', 'video_format')
    INDEX_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FORMAT_FIELD_NUMBER: _ClassVar[int]
    index: int
    video_format: VideoFormat

    def __init__(self, index: _Optional[int]=..., video_format: _Optional[_Union[VideoFormat, _Mapping]]=...) -> None:
        ...

class VideoFormat(_message.Message):
    __slots__ = ('codec', 'width_pixels', 'height_pixels', 'frame_rate')
    CODEC_FIELD_NUMBER: _ClassVar[int]
    WIDTH_PIXELS_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_PIXELS_FIELD_NUMBER: _ClassVar[int]
    FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
    codec: str
    width_pixels: int
    height_pixels: int
    frame_rate: float

    def __init__(self, codec: _Optional[str]=..., width_pixels: _Optional[int]=..., height_pixels: _Optional[int]=..., frame_rate: _Optional[float]=...) -> None:
        ...

class AudioStreamProperty(_message.Message):
    __slots__ = ('index', 'audio_format')
    INDEX_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FORMAT_FIELD_NUMBER: _ClassVar[int]
    index: int
    audio_format: AudioFormat

    def __init__(self, index: _Optional[int]=..., audio_format: _Optional[_Union[AudioFormat, _Mapping]]=...) -> None:
        ...

class AudioFormat(_message.Message):
    __slots__ = ('codec', 'channel_count', 'channel_layout')
    CODEC_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_COUNT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    codec: str
    channel_count: int
    channel_layout: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, codec: _Optional[str]=..., channel_count: _Optional[int]=..., channel_layout: _Optional[_Iterable[str]]=...) -> None:
        ...

class InputAttachment(_message.Message):
    __slots__ = ('key', 'input', 'automatic_failover')

    class AutomaticFailover(_message.Message):
        __slots__ = ('input_keys',)
        INPUT_KEYS_FIELD_NUMBER: _ClassVar[int]
        input_keys: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, input_keys: _Optional[_Iterable[str]]=...) -> None:
            ...
    KEY_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_FAILOVER_FIELD_NUMBER: _ClassVar[int]
    key: str
    input: str
    automatic_failover: InputAttachment.AutomaticFailover

    def __init__(self, key: _Optional[str]=..., input: _Optional[str]=..., automatic_failover: _Optional[_Union[InputAttachment.AutomaticFailover, _Mapping]]=...) -> None:
        ...

class Event(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'input_switch', 'ad_break', 'return_to_program', 'slate', 'mute', 'unmute', 'execute_now', 'execution_time', 'state', 'error')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Event.State]
        SCHEDULED: _ClassVar[Event.State]
        RUNNING: _ClassVar[Event.State]
        SUCCEEDED: _ClassVar[Event.State]
        FAILED: _ClassVar[Event.State]
        PENDING: _ClassVar[Event.State]
        STOPPED: _ClassVar[Event.State]
    STATE_UNSPECIFIED: Event.State
    SCHEDULED: Event.State
    RUNNING: Event.State
    SUCCEEDED: Event.State
    FAILED: Event.State
    PENDING: Event.State
    STOPPED: Event.State

    class InputSwitchTask(_message.Message):
        __slots__ = ('input_key',)
        INPUT_KEY_FIELD_NUMBER: _ClassVar[int]
        input_key: str

        def __init__(self, input_key: _Optional[str]=...) -> None:
            ...

    class AdBreakTask(_message.Message):
        __slots__ = ('duration',)
        DURATION_FIELD_NUMBER: _ClassVar[int]
        duration: _duration_pb2.Duration

        def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...

    class SlateTask(_message.Message):
        __slots__ = ('duration', 'asset')
        DURATION_FIELD_NUMBER: _ClassVar[int]
        ASSET_FIELD_NUMBER: _ClassVar[int]
        duration: _duration_pb2.Duration
        asset: str

        def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., asset: _Optional[str]=...) -> None:
            ...

    class ReturnToProgramTask(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class MuteTask(_message.Message):
        __slots__ = ('duration',)
        DURATION_FIELD_NUMBER: _ClassVar[int]
        duration: _duration_pb2.Duration

        def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...

    class UnmuteTask(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    INPUT_SWITCH_FIELD_NUMBER: _ClassVar[int]
    AD_BREAK_FIELD_NUMBER: _ClassVar[int]
    RETURN_TO_PROGRAM_FIELD_NUMBER: _ClassVar[int]
    SLATE_FIELD_NUMBER: _ClassVar[int]
    MUTE_FIELD_NUMBER: _ClassVar[int]
    UNMUTE_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_NOW_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    input_switch: Event.InputSwitchTask
    ad_break: Event.AdBreakTask
    return_to_program: Event.ReturnToProgramTask
    slate: Event.SlateTask
    mute: Event.MuteTask
    unmute: Event.UnmuteTask
    execute_now: bool
    execution_time: _timestamp_pb2.Timestamp
    state: Event.State
    error: _status_pb2.Status

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., input_switch: _Optional[_Union[Event.InputSwitchTask, _Mapping]]=..., ad_break: _Optional[_Union[Event.AdBreakTask, _Mapping]]=..., return_to_program: _Optional[_Union[Event.ReturnToProgramTask, _Mapping]]=..., slate: _Optional[_Union[Event.SlateTask, _Mapping]]=..., mute: _Optional[_Union[Event.MuteTask, _Mapping]]=..., unmute: _Optional[_Union[Event.UnmuteTask, _Mapping]]=..., execute_now: bool=..., execution_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[Event.State, str]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class Clip(_message.Message):
    __slots__ = ('name', 'create_time', 'start_time', 'update_time', 'labels', 'state', 'output_uri', 'error', 'slices', 'clip_manifests')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Clip.State]
        PENDING: _ClassVar[Clip.State]
        CREATING: _ClassVar[Clip.State]
        SUCCEEDED: _ClassVar[Clip.State]
        FAILED: _ClassVar[Clip.State]
    STATE_UNSPECIFIED: Clip.State
    PENDING: Clip.State
    CREATING: Clip.State
    SUCCEEDED: Clip.State
    FAILED: Clip.State

    class TimeSlice(_message.Message):
        __slots__ = ('markin_time', 'markout_time')
        MARKIN_TIME_FIELD_NUMBER: _ClassVar[int]
        MARKOUT_TIME_FIELD_NUMBER: _ClassVar[int]
        markin_time: _timestamp_pb2.Timestamp
        markout_time: _timestamp_pb2.Timestamp

        def __init__(self, markin_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., markout_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class Slice(_message.Message):
        __slots__ = ('time_slice',)
        TIME_SLICE_FIELD_NUMBER: _ClassVar[int]
        time_slice: Clip.TimeSlice

        def __init__(self, time_slice: _Optional[_Union[Clip.TimeSlice, _Mapping]]=...) -> None:
            ...

    class ClipManifest(_message.Message):
        __slots__ = ('manifest_key', 'output_uri')
        MANIFEST_KEY_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_URI_FIELD_NUMBER: _ClassVar[int]
        manifest_key: str
        output_uri: str

        def __init__(self, manifest_key: _Optional[str]=..., output_uri: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_URI_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SLICES_FIELD_NUMBER: _ClassVar[int]
    CLIP_MANIFESTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    state: Clip.State
    output_uri: str
    error: _status_pb2.Status
    slices: _containers.RepeatedCompositeFieldContainer[Clip.Slice]
    clip_manifests: _containers.RepeatedCompositeFieldContainer[Clip.ClipManifest]

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., state: _Optional[_Union[Clip.State, str]]=..., output_uri: _Optional[str]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., slices: _Optional[_Iterable[_Union[Clip.Slice, _Mapping]]]=..., clip_manifests: _Optional[_Iterable[_Union[Clip.ClipManifest, _Mapping]]]=...) -> None:
        ...

class Asset(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'video', 'image', 'crc32c', 'state', 'error')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Asset.State]
        CREATING: _ClassVar[Asset.State]
        ACTIVE: _ClassVar[Asset.State]
        DELETING: _ClassVar[Asset.State]
        ERROR: _ClassVar[Asset.State]
    STATE_UNSPECIFIED: Asset.State
    CREATING: Asset.State
    ACTIVE: Asset.State
    DELETING: Asset.State
    ERROR: Asset.State

    class VideoAsset(_message.Message):
        __slots__ = ('uri',)
        URI_FIELD_NUMBER: _ClassVar[int]
        uri: str

        def __init__(self, uri: _Optional[str]=...) -> None:
            ...

    class ImageAsset(_message.Message):
        __slots__ = ('uri',)
        URI_FIELD_NUMBER: _ClassVar[int]
        uri: str

        def __init__(self, uri: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    CRC32C_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    video: Asset.VideoAsset
    image: Asset.ImageAsset
    crc32c: str
    state: Asset.State
    error: _status_pb2.Status

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., video: _Optional[_Union[Asset.VideoAsset, _Mapping]]=..., image: _Optional[_Union[Asset.ImageAsset, _Mapping]]=..., crc32c: _Optional[str]=..., state: _Optional[_Union[Asset.State, str]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class Encryption(_message.Message):
    __slots__ = ('id', 'secret_manager_key_source', 'drm_systems', 'aes128', 'sample_aes', 'mpeg_cenc')

    class SecretManagerSource(_message.Message):
        __slots__ = ('secret_version',)
        SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
        secret_version: str

        def __init__(self, secret_version: _Optional[str]=...) -> None:
            ...

    class Widevine(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class Fairplay(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class Playready(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class Clearkey(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class DrmSystems(_message.Message):
        __slots__ = ('widevine', 'fairplay', 'playready', 'clearkey')
        WIDEVINE_FIELD_NUMBER: _ClassVar[int]
        FAIRPLAY_FIELD_NUMBER: _ClassVar[int]
        PLAYREADY_FIELD_NUMBER: _ClassVar[int]
        CLEARKEY_FIELD_NUMBER: _ClassVar[int]
        widevine: Encryption.Widevine
        fairplay: Encryption.Fairplay
        playready: Encryption.Playready
        clearkey: Encryption.Clearkey

        def __init__(self, widevine: _Optional[_Union[Encryption.Widevine, _Mapping]]=..., fairplay: _Optional[_Union[Encryption.Fairplay, _Mapping]]=..., playready: _Optional[_Union[Encryption.Playready, _Mapping]]=..., clearkey: _Optional[_Union[Encryption.Clearkey, _Mapping]]=...) -> None:
            ...

    class Aes128Encryption(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class SampleAesEncryption(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class MpegCommonEncryption(_message.Message):
        __slots__ = ('scheme',)
        SCHEME_FIELD_NUMBER: _ClassVar[int]
        scheme: str

        def __init__(self, scheme: _Optional[str]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_MANAGER_KEY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DRM_SYSTEMS_FIELD_NUMBER: _ClassVar[int]
    AES128_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_AES_FIELD_NUMBER: _ClassVar[int]
    MPEG_CENC_FIELD_NUMBER: _ClassVar[int]
    id: str
    secret_manager_key_source: Encryption.SecretManagerSource
    drm_systems: Encryption.DrmSystems
    aes128: Encryption.Aes128Encryption
    sample_aes: Encryption.SampleAesEncryption
    mpeg_cenc: Encryption.MpegCommonEncryption

    def __init__(self, id: _Optional[str]=..., secret_manager_key_source: _Optional[_Union[Encryption.SecretManagerSource, _Mapping]]=..., drm_systems: _Optional[_Union[Encryption.DrmSystems, _Mapping]]=..., aes128: _Optional[_Union[Encryption.Aes128Encryption, _Mapping]]=..., sample_aes: _Optional[_Union[Encryption.SampleAesEncryption, _Mapping]]=..., mpeg_cenc: _Optional[_Union[Encryption.MpegCommonEncryption, _Mapping]]=...) -> None:
        ...

class Pool(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'network_config')

    class NetworkConfig(_message.Message):
        __slots__ = ('peered_network',)
        PEERED_NETWORK_FIELD_NUMBER: _ClassVar[int]
        peered_network: str

        def __init__(self, peered_network: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    network_config: Pool.NetworkConfig

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., network_config: _Optional[_Union[Pool.NetworkConfig, _Mapping]]=...) -> None:
        ...