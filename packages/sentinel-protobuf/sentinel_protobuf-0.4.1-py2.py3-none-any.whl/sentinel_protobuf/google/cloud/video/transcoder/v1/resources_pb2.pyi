from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Job(_message.Message):
    __slots__ = ('name', 'input_uri', 'output_uri', 'template_id', 'config', 'state', 'create_time', 'start_time', 'end_time', 'ttl_after_completion_days', 'labels', 'error', 'mode', 'batch_mode_priority', 'optimization')

    class ProcessingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROCESSING_STATE_UNSPECIFIED: _ClassVar[Job.ProcessingState]
        PENDING: _ClassVar[Job.ProcessingState]
        RUNNING: _ClassVar[Job.ProcessingState]
        SUCCEEDED: _ClassVar[Job.ProcessingState]
        FAILED: _ClassVar[Job.ProcessingState]
    PROCESSING_STATE_UNSPECIFIED: Job.ProcessingState
    PENDING: Job.ProcessingState
    RUNNING: Job.ProcessingState
    SUCCEEDED: Job.ProcessingState
    FAILED: Job.ProcessingState

    class ProcessingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROCESSING_MODE_UNSPECIFIED: _ClassVar[Job.ProcessingMode]
        PROCESSING_MODE_INTERACTIVE: _ClassVar[Job.ProcessingMode]
        PROCESSING_MODE_BATCH: _ClassVar[Job.ProcessingMode]
    PROCESSING_MODE_UNSPECIFIED: Job.ProcessingMode
    PROCESSING_MODE_INTERACTIVE: Job.ProcessingMode
    PROCESSING_MODE_BATCH: Job.ProcessingMode

    class OptimizationStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPTIMIZATION_STRATEGY_UNSPECIFIED: _ClassVar[Job.OptimizationStrategy]
        AUTODETECT: _ClassVar[Job.OptimizationStrategy]
        DISABLED: _ClassVar[Job.OptimizationStrategy]
    OPTIMIZATION_STRATEGY_UNSPECIFIED: Job.OptimizationStrategy
    AUTODETECT: Job.OptimizationStrategy
    DISABLED: Job.OptimizationStrategy

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_URI_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_URI_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TTL_AFTER_COMPLETION_DAYS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    BATCH_MODE_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    input_uri: str
    output_uri: str
    template_id: str
    config: JobConfig
    state: Job.ProcessingState
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    ttl_after_completion_days: int
    labels: _containers.ScalarMap[str, str]
    error: _status_pb2.Status
    mode: Job.ProcessingMode
    batch_mode_priority: int
    optimization: Job.OptimizationStrategy

    def __init__(self, name: _Optional[str]=..., input_uri: _Optional[str]=..., output_uri: _Optional[str]=..., template_id: _Optional[str]=..., config: _Optional[_Union[JobConfig, _Mapping]]=..., state: _Optional[_Union[Job.ProcessingState, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., ttl_after_completion_days: _Optional[int]=..., labels: _Optional[_Mapping[str, str]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., mode: _Optional[_Union[Job.ProcessingMode, str]]=..., batch_mode_priority: _Optional[int]=..., optimization: _Optional[_Union[Job.OptimizationStrategy, str]]=...) -> None:
        ...

class JobTemplate(_message.Message):
    __slots__ = ('name', 'config', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    config: JobConfig
    labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., config: _Optional[_Union[JobConfig, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class JobConfig(_message.Message):
    __slots__ = ('inputs', 'edit_list', 'elementary_streams', 'mux_streams', 'manifests', 'output', 'ad_breaks', 'pubsub_destination', 'sprite_sheets', 'overlays', 'encryptions')
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    EDIT_LIST_FIELD_NUMBER: _ClassVar[int]
    ELEMENTARY_STREAMS_FIELD_NUMBER: _ClassVar[int]
    MUX_STREAMS_FIELD_NUMBER: _ClassVar[int]
    MANIFESTS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    AD_BREAKS_FIELD_NUMBER: _ClassVar[int]
    PUBSUB_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    SPRITE_SHEETS_FIELD_NUMBER: _ClassVar[int]
    OVERLAYS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTIONS_FIELD_NUMBER: _ClassVar[int]
    inputs: _containers.RepeatedCompositeFieldContainer[Input]
    edit_list: _containers.RepeatedCompositeFieldContainer[EditAtom]
    elementary_streams: _containers.RepeatedCompositeFieldContainer[ElementaryStream]
    mux_streams: _containers.RepeatedCompositeFieldContainer[MuxStream]
    manifests: _containers.RepeatedCompositeFieldContainer[Manifest]
    output: Output
    ad_breaks: _containers.RepeatedCompositeFieldContainer[AdBreak]
    pubsub_destination: PubsubDestination
    sprite_sheets: _containers.RepeatedCompositeFieldContainer[SpriteSheet]
    overlays: _containers.RepeatedCompositeFieldContainer[Overlay]
    encryptions: _containers.RepeatedCompositeFieldContainer[Encryption]

    def __init__(self, inputs: _Optional[_Iterable[_Union[Input, _Mapping]]]=..., edit_list: _Optional[_Iterable[_Union[EditAtom, _Mapping]]]=..., elementary_streams: _Optional[_Iterable[_Union[ElementaryStream, _Mapping]]]=..., mux_streams: _Optional[_Iterable[_Union[MuxStream, _Mapping]]]=..., manifests: _Optional[_Iterable[_Union[Manifest, _Mapping]]]=..., output: _Optional[_Union[Output, _Mapping]]=..., ad_breaks: _Optional[_Iterable[_Union[AdBreak, _Mapping]]]=..., pubsub_destination: _Optional[_Union[PubsubDestination, _Mapping]]=..., sprite_sheets: _Optional[_Iterable[_Union[SpriteSheet, _Mapping]]]=..., overlays: _Optional[_Iterable[_Union[Overlay, _Mapping]]]=..., encryptions: _Optional[_Iterable[_Union[Encryption, _Mapping]]]=...) -> None:
        ...

class Input(_message.Message):
    __slots__ = ('key', 'uri', 'preprocessing_config')
    KEY_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    PREPROCESSING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    key: str
    uri: str
    preprocessing_config: PreprocessingConfig

    def __init__(self, key: _Optional[str]=..., uri: _Optional[str]=..., preprocessing_config: _Optional[_Union[PreprocessingConfig, _Mapping]]=...) -> None:
        ...

class Output(_message.Message):
    __slots__ = ('uri',)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str

    def __init__(self, uri: _Optional[str]=...) -> None:
        ...

class EditAtom(_message.Message):
    __slots__ = ('key', 'inputs', 'end_time_offset', 'start_time_offset')
    KEY_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    START_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    key: str
    inputs: _containers.RepeatedScalarFieldContainer[str]
    end_time_offset: _duration_pb2.Duration
    start_time_offset: _duration_pb2.Duration

    def __init__(self, key: _Optional[str]=..., inputs: _Optional[_Iterable[str]]=..., end_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., start_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class AdBreak(_message.Message):
    __slots__ = ('start_time_offset',)
    START_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    start_time_offset: _duration_pb2.Duration

    def __init__(self, start_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class ElementaryStream(_message.Message):
    __slots__ = ('key', 'video_stream', 'audio_stream', 'text_stream')
    KEY_FIELD_NUMBER: _ClassVar[int]
    VIDEO_STREAM_FIELD_NUMBER: _ClassVar[int]
    AUDIO_STREAM_FIELD_NUMBER: _ClassVar[int]
    TEXT_STREAM_FIELD_NUMBER: _ClassVar[int]
    key: str
    video_stream: VideoStream
    audio_stream: AudioStream
    text_stream: TextStream

    def __init__(self, key: _Optional[str]=..., video_stream: _Optional[_Union[VideoStream, _Mapping]]=..., audio_stream: _Optional[_Union[AudioStream, _Mapping]]=..., text_stream: _Optional[_Union[TextStream, _Mapping]]=...) -> None:
        ...

class MuxStream(_message.Message):
    __slots__ = ('key', 'file_name', 'container', 'elementary_streams', 'segment_settings', 'encryption_id')
    KEY_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    ELEMENTARY_STREAMS_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_ID_FIELD_NUMBER: _ClassVar[int]
    key: str
    file_name: str
    container: str
    elementary_streams: _containers.RepeatedScalarFieldContainer[str]
    segment_settings: SegmentSettings
    encryption_id: str

    def __init__(self, key: _Optional[str]=..., file_name: _Optional[str]=..., container: _Optional[str]=..., elementary_streams: _Optional[_Iterable[str]]=..., segment_settings: _Optional[_Union[SegmentSettings, _Mapping]]=..., encryption_id: _Optional[str]=...) -> None:
        ...

class Manifest(_message.Message):
    __slots__ = ('file_name', 'type', 'mux_streams', 'dash')

    class ManifestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MANIFEST_TYPE_UNSPECIFIED: _ClassVar[Manifest.ManifestType]
        HLS: _ClassVar[Manifest.ManifestType]
        DASH: _ClassVar[Manifest.ManifestType]
    MANIFEST_TYPE_UNSPECIFIED: Manifest.ManifestType
    HLS: Manifest.ManifestType
    DASH: Manifest.ManifestType

    class DashConfig(_message.Message):
        __slots__ = ('segment_reference_scheme',)

        class SegmentReferenceScheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SEGMENT_REFERENCE_SCHEME_UNSPECIFIED: _ClassVar[Manifest.DashConfig.SegmentReferenceScheme]
            SEGMENT_LIST: _ClassVar[Manifest.DashConfig.SegmentReferenceScheme]
            SEGMENT_TEMPLATE_NUMBER: _ClassVar[Manifest.DashConfig.SegmentReferenceScheme]
        SEGMENT_REFERENCE_SCHEME_UNSPECIFIED: Manifest.DashConfig.SegmentReferenceScheme
        SEGMENT_LIST: Manifest.DashConfig.SegmentReferenceScheme
        SEGMENT_TEMPLATE_NUMBER: Manifest.DashConfig.SegmentReferenceScheme
        SEGMENT_REFERENCE_SCHEME_FIELD_NUMBER: _ClassVar[int]
        segment_reference_scheme: Manifest.DashConfig.SegmentReferenceScheme

        def __init__(self, segment_reference_scheme: _Optional[_Union[Manifest.DashConfig.SegmentReferenceScheme, str]]=...) -> None:
            ...
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MUX_STREAMS_FIELD_NUMBER: _ClassVar[int]
    DASH_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    type: Manifest.ManifestType
    mux_streams: _containers.RepeatedScalarFieldContainer[str]
    dash: Manifest.DashConfig

    def __init__(self, file_name: _Optional[str]=..., type: _Optional[_Union[Manifest.ManifestType, str]]=..., mux_streams: _Optional[_Iterable[str]]=..., dash: _Optional[_Union[Manifest.DashConfig, _Mapping]]=...) -> None:
        ...

class PubsubDestination(_message.Message):
    __slots__ = ('topic',)
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    topic: str

    def __init__(self, topic: _Optional[str]=...) -> None:
        ...

class SpriteSheet(_message.Message):
    __slots__ = ('format', 'file_prefix', 'sprite_width_pixels', 'sprite_height_pixels', 'column_count', 'row_count', 'start_time_offset', 'end_time_offset', 'total_count', 'interval', 'quality')
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    FILE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    SPRITE_WIDTH_PIXELS_FIELD_NUMBER: _ClassVar[int]
    SPRITE_HEIGHT_PIXELS_FIELD_NUMBER: _ClassVar[int]
    COLUMN_COUNT_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    format: str
    file_prefix: str
    sprite_width_pixels: int
    sprite_height_pixels: int
    column_count: int
    row_count: int
    start_time_offset: _duration_pb2.Duration
    end_time_offset: _duration_pb2.Duration
    total_count: int
    interval: _duration_pb2.Duration
    quality: int

    def __init__(self, format: _Optional[str]=..., file_prefix: _Optional[str]=..., sprite_width_pixels: _Optional[int]=..., sprite_height_pixels: _Optional[int]=..., column_count: _Optional[int]=..., row_count: _Optional[int]=..., start_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., end_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., total_count: _Optional[int]=..., interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., quality: _Optional[int]=...) -> None:
        ...

class Overlay(_message.Message):
    __slots__ = ('image', 'animations')

    class FadeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FADE_TYPE_UNSPECIFIED: _ClassVar[Overlay.FadeType]
        FADE_IN: _ClassVar[Overlay.FadeType]
        FADE_OUT: _ClassVar[Overlay.FadeType]
    FADE_TYPE_UNSPECIFIED: Overlay.FadeType
    FADE_IN: Overlay.FadeType
    FADE_OUT: Overlay.FadeType

    class NormalizedCoordinate(_message.Message):
        __slots__ = ('x', 'y')
        X_FIELD_NUMBER: _ClassVar[int]
        Y_FIELD_NUMBER: _ClassVar[int]
        x: float
        y: float

        def __init__(self, x: _Optional[float]=..., y: _Optional[float]=...) -> None:
            ...

    class Image(_message.Message):
        __slots__ = ('uri', 'resolution', 'alpha')
        URI_FIELD_NUMBER: _ClassVar[int]
        RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        ALPHA_FIELD_NUMBER: _ClassVar[int]
        uri: str
        resolution: Overlay.NormalizedCoordinate
        alpha: float

        def __init__(self, uri: _Optional[str]=..., resolution: _Optional[_Union[Overlay.NormalizedCoordinate, _Mapping]]=..., alpha: _Optional[float]=...) -> None:
            ...

    class AnimationStatic(_message.Message):
        __slots__ = ('xy', 'start_time_offset')
        XY_FIELD_NUMBER: _ClassVar[int]
        START_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
        xy: Overlay.NormalizedCoordinate
        start_time_offset: _duration_pb2.Duration

        def __init__(self, xy: _Optional[_Union[Overlay.NormalizedCoordinate, _Mapping]]=..., start_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...

    class AnimationFade(_message.Message):
        __slots__ = ('fade_type', 'xy', 'start_time_offset', 'end_time_offset')
        FADE_TYPE_FIELD_NUMBER: _ClassVar[int]
        XY_FIELD_NUMBER: _ClassVar[int]
        START_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
        END_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
        fade_type: Overlay.FadeType
        xy: Overlay.NormalizedCoordinate
        start_time_offset: _duration_pb2.Duration
        end_time_offset: _duration_pb2.Duration

        def __init__(self, fade_type: _Optional[_Union[Overlay.FadeType, str]]=..., xy: _Optional[_Union[Overlay.NormalizedCoordinate, _Mapping]]=..., start_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., end_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...

    class AnimationEnd(_message.Message):
        __slots__ = ('start_time_offset',)
        START_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
        start_time_offset: _duration_pb2.Duration

        def __init__(self, start_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...

    class Animation(_message.Message):
        __slots__ = ('animation_static', 'animation_fade', 'animation_end')
        ANIMATION_STATIC_FIELD_NUMBER: _ClassVar[int]
        ANIMATION_FADE_FIELD_NUMBER: _ClassVar[int]
        ANIMATION_END_FIELD_NUMBER: _ClassVar[int]
        animation_static: Overlay.AnimationStatic
        animation_fade: Overlay.AnimationFade
        animation_end: Overlay.AnimationEnd

        def __init__(self, animation_static: _Optional[_Union[Overlay.AnimationStatic, _Mapping]]=..., animation_fade: _Optional[_Union[Overlay.AnimationFade, _Mapping]]=..., animation_end: _Optional[_Union[Overlay.AnimationEnd, _Mapping]]=...) -> None:
            ...
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    ANIMATIONS_FIELD_NUMBER: _ClassVar[int]
    image: Overlay.Image
    animations: _containers.RepeatedCompositeFieldContainer[Overlay.Animation]

    def __init__(self, image: _Optional[_Union[Overlay.Image, _Mapping]]=..., animations: _Optional[_Iterable[_Union[Overlay.Animation, _Mapping]]]=...) -> None:
        ...

class PreprocessingConfig(_message.Message):
    __slots__ = ('color', 'denoise', 'deblock', 'audio', 'crop', 'pad', 'deinterlace')

    class Color(_message.Message):
        __slots__ = ('saturation', 'contrast', 'brightness')
        SATURATION_FIELD_NUMBER: _ClassVar[int]
        CONTRAST_FIELD_NUMBER: _ClassVar[int]
        BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
        saturation: float
        contrast: float
        brightness: float

        def __init__(self, saturation: _Optional[float]=..., contrast: _Optional[float]=..., brightness: _Optional[float]=...) -> None:
            ...

    class Denoise(_message.Message):
        __slots__ = ('strength', 'tune')
        STRENGTH_FIELD_NUMBER: _ClassVar[int]
        TUNE_FIELD_NUMBER: _ClassVar[int]
        strength: float
        tune: str

        def __init__(self, strength: _Optional[float]=..., tune: _Optional[str]=...) -> None:
            ...

    class Deblock(_message.Message):
        __slots__ = ('strength', 'enabled')
        STRENGTH_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        strength: float
        enabled: bool

        def __init__(self, strength: _Optional[float]=..., enabled: bool=...) -> None:
            ...

    class Audio(_message.Message):
        __slots__ = ('lufs', 'high_boost', 'low_boost')
        LUFS_FIELD_NUMBER: _ClassVar[int]
        HIGH_BOOST_FIELD_NUMBER: _ClassVar[int]
        LOW_BOOST_FIELD_NUMBER: _ClassVar[int]
        lufs: float
        high_boost: bool
        low_boost: bool

        def __init__(self, lufs: _Optional[float]=..., high_boost: bool=..., low_boost: bool=...) -> None:
            ...

    class Crop(_message.Message):
        __slots__ = ('top_pixels', 'bottom_pixels', 'left_pixels', 'right_pixels')
        TOP_PIXELS_FIELD_NUMBER: _ClassVar[int]
        BOTTOM_PIXELS_FIELD_NUMBER: _ClassVar[int]
        LEFT_PIXELS_FIELD_NUMBER: _ClassVar[int]
        RIGHT_PIXELS_FIELD_NUMBER: _ClassVar[int]
        top_pixels: int
        bottom_pixels: int
        left_pixels: int
        right_pixels: int

        def __init__(self, top_pixels: _Optional[int]=..., bottom_pixels: _Optional[int]=..., left_pixels: _Optional[int]=..., right_pixels: _Optional[int]=...) -> None:
            ...

    class Pad(_message.Message):
        __slots__ = ('top_pixels', 'bottom_pixels', 'left_pixels', 'right_pixels')
        TOP_PIXELS_FIELD_NUMBER: _ClassVar[int]
        BOTTOM_PIXELS_FIELD_NUMBER: _ClassVar[int]
        LEFT_PIXELS_FIELD_NUMBER: _ClassVar[int]
        RIGHT_PIXELS_FIELD_NUMBER: _ClassVar[int]
        top_pixels: int
        bottom_pixels: int
        left_pixels: int
        right_pixels: int

        def __init__(self, top_pixels: _Optional[int]=..., bottom_pixels: _Optional[int]=..., left_pixels: _Optional[int]=..., right_pixels: _Optional[int]=...) -> None:
            ...

    class Deinterlace(_message.Message):
        __slots__ = ('yadif', 'bwdif')

        class YadifConfig(_message.Message):
            __slots__ = ('mode', 'disable_spatial_interlacing', 'parity', 'deinterlace_all_frames')
            MODE_FIELD_NUMBER: _ClassVar[int]
            DISABLE_SPATIAL_INTERLACING_FIELD_NUMBER: _ClassVar[int]
            PARITY_FIELD_NUMBER: _ClassVar[int]
            DEINTERLACE_ALL_FRAMES_FIELD_NUMBER: _ClassVar[int]
            mode: str
            disable_spatial_interlacing: bool
            parity: str
            deinterlace_all_frames: bool

            def __init__(self, mode: _Optional[str]=..., disable_spatial_interlacing: bool=..., parity: _Optional[str]=..., deinterlace_all_frames: bool=...) -> None:
                ...

        class BwdifConfig(_message.Message):
            __slots__ = ('mode', 'parity', 'deinterlace_all_frames')
            MODE_FIELD_NUMBER: _ClassVar[int]
            PARITY_FIELD_NUMBER: _ClassVar[int]
            DEINTERLACE_ALL_FRAMES_FIELD_NUMBER: _ClassVar[int]
            mode: str
            parity: str
            deinterlace_all_frames: bool

            def __init__(self, mode: _Optional[str]=..., parity: _Optional[str]=..., deinterlace_all_frames: bool=...) -> None:
                ...
        YADIF_FIELD_NUMBER: _ClassVar[int]
        BWDIF_FIELD_NUMBER: _ClassVar[int]
        yadif: PreprocessingConfig.Deinterlace.YadifConfig
        bwdif: PreprocessingConfig.Deinterlace.BwdifConfig

        def __init__(self, yadif: _Optional[_Union[PreprocessingConfig.Deinterlace.YadifConfig, _Mapping]]=..., bwdif: _Optional[_Union[PreprocessingConfig.Deinterlace.BwdifConfig, _Mapping]]=...) -> None:
            ...
    COLOR_FIELD_NUMBER: _ClassVar[int]
    DENOISE_FIELD_NUMBER: _ClassVar[int]
    DEBLOCK_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    CROP_FIELD_NUMBER: _ClassVar[int]
    PAD_FIELD_NUMBER: _ClassVar[int]
    DEINTERLACE_FIELD_NUMBER: _ClassVar[int]
    color: PreprocessingConfig.Color
    denoise: PreprocessingConfig.Denoise
    deblock: PreprocessingConfig.Deblock
    audio: PreprocessingConfig.Audio
    crop: PreprocessingConfig.Crop
    pad: PreprocessingConfig.Pad
    deinterlace: PreprocessingConfig.Deinterlace

    def __init__(self, color: _Optional[_Union[PreprocessingConfig.Color, _Mapping]]=..., denoise: _Optional[_Union[PreprocessingConfig.Denoise, _Mapping]]=..., deblock: _Optional[_Union[PreprocessingConfig.Deblock, _Mapping]]=..., audio: _Optional[_Union[PreprocessingConfig.Audio, _Mapping]]=..., crop: _Optional[_Union[PreprocessingConfig.Crop, _Mapping]]=..., pad: _Optional[_Union[PreprocessingConfig.Pad, _Mapping]]=..., deinterlace: _Optional[_Union[PreprocessingConfig.Deinterlace, _Mapping]]=...) -> None:
        ...

class VideoStream(_message.Message):
    __slots__ = ('h264', 'h265', 'vp9')

    class H264CodecSettings(_message.Message):
        __slots__ = ('width_pixels', 'height_pixels', 'frame_rate', 'bitrate_bps', 'pixel_format', 'rate_control_mode', 'crf_level', 'allow_open_gop', 'gop_frame_count', 'gop_duration', 'enable_two_pass', 'vbv_size_bits', 'vbv_fullness_bits', 'entropy_coder', 'b_pyramid', 'b_frame_count', 'aq_strength', 'profile', 'tune', 'preset')
        WIDTH_PIXELS_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_PIXELS_FIELD_NUMBER: _ClassVar[int]
        FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
        BITRATE_BPS_FIELD_NUMBER: _ClassVar[int]
        PIXEL_FORMAT_FIELD_NUMBER: _ClassVar[int]
        RATE_CONTROL_MODE_FIELD_NUMBER: _ClassVar[int]
        CRF_LEVEL_FIELD_NUMBER: _ClassVar[int]
        ALLOW_OPEN_GOP_FIELD_NUMBER: _ClassVar[int]
        GOP_FRAME_COUNT_FIELD_NUMBER: _ClassVar[int]
        GOP_DURATION_FIELD_NUMBER: _ClassVar[int]
        ENABLE_TWO_PASS_FIELD_NUMBER: _ClassVar[int]
        VBV_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
        VBV_FULLNESS_BITS_FIELD_NUMBER: _ClassVar[int]
        ENTROPY_CODER_FIELD_NUMBER: _ClassVar[int]
        B_PYRAMID_FIELD_NUMBER: _ClassVar[int]
        B_FRAME_COUNT_FIELD_NUMBER: _ClassVar[int]
        AQ_STRENGTH_FIELD_NUMBER: _ClassVar[int]
        PROFILE_FIELD_NUMBER: _ClassVar[int]
        TUNE_FIELD_NUMBER: _ClassVar[int]
        PRESET_FIELD_NUMBER: _ClassVar[int]
        width_pixels: int
        height_pixels: int
        frame_rate: float
        bitrate_bps: int
        pixel_format: str
        rate_control_mode: str
        crf_level: int
        allow_open_gop: bool
        gop_frame_count: int
        gop_duration: _duration_pb2.Duration
        enable_two_pass: bool
        vbv_size_bits: int
        vbv_fullness_bits: int
        entropy_coder: str
        b_pyramid: bool
        b_frame_count: int
        aq_strength: float
        profile: str
        tune: str
        preset: str

        def __init__(self, width_pixels: _Optional[int]=..., height_pixels: _Optional[int]=..., frame_rate: _Optional[float]=..., bitrate_bps: _Optional[int]=..., pixel_format: _Optional[str]=..., rate_control_mode: _Optional[str]=..., crf_level: _Optional[int]=..., allow_open_gop: bool=..., gop_frame_count: _Optional[int]=..., gop_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., enable_two_pass: bool=..., vbv_size_bits: _Optional[int]=..., vbv_fullness_bits: _Optional[int]=..., entropy_coder: _Optional[str]=..., b_pyramid: bool=..., b_frame_count: _Optional[int]=..., aq_strength: _Optional[float]=..., profile: _Optional[str]=..., tune: _Optional[str]=..., preset: _Optional[str]=...) -> None:
            ...

    class H265CodecSettings(_message.Message):
        __slots__ = ('width_pixels', 'height_pixels', 'frame_rate', 'bitrate_bps', 'pixel_format', 'rate_control_mode', 'crf_level', 'allow_open_gop', 'gop_frame_count', 'gop_duration', 'enable_two_pass', 'vbv_size_bits', 'vbv_fullness_bits', 'b_pyramid', 'b_frame_count', 'aq_strength', 'profile', 'tune', 'preset')
        WIDTH_PIXELS_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_PIXELS_FIELD_NUMBER: _ClassVar[int]
        FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
        BITRATE_BPS_FIELD_NUMBER: _ClassVar[int]
        PIXEL_FORMAT_FIELD_NUMBER: _ClassVar[int]
        RATE_CONTROL_MODE_FIELD_NUMBER: _ClassVar[int]
        CRF_LEVEL_FIELD_NUMBER: _ClassVar[int]
        ALLOW_OPEN_GOP_FIELD_NUMBER: _ClassVar[int]
        GOP_FRAME_COUNT_FIELD_NUMBER: _ClassVar[int]
        GOP_DURATION_FIELD_NUMBER: _ClassVar[int]
        ENABLE_TWO_PASS_FIELD_NUMBER: _ClassVar[int]
        VBV_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
        VBV_FULLNESS_BITS_FIELD_NUMBER: _ClassVar[int]
        B_PYRAMID_FIELD_NUMBER: _ClassVar[int]
        B_FRAME_COUNT_FIELD_NUMBER: _ClassVar[int]
        AQ_STRENGTH_FIELD_NUMBER: _ClassVar[int]
        PROFILE_FIELD_NUMBER: _ClassVar[int]
        TUNE_FIELD_NUMBER: _ClassVar[int]
        PRESET_FIELD_NUMBER: _ClassVar[int]
        width_pixels: int
        height_pixels: int
        frame_rate: float
        bitrate_bps: int
        pixel_format: str
        rate_control_mode: str
        crf_level: int
        allow_open_gop: bool
        gop_frame_count: int
        gop_duration: _duration_pb2.Duration
        enable_two_pass: bool
        vbv_size_bits: int
        vbv_fullness_bits: int
        b_pyramid: bool
        b_frame_count: int
        aq_strength: float
        profile: str
        tune: str
        preset: str

        def __init__(self, width_pixels: _Optional[int]=..., height_pixels: _Optional[int]=..., frame_rate: _Optional[float]=..., bitrate_bps: _Optional[int]=..., pixel_format: _Optional[str]=..., rate_control_mode: _Optional[str]=..., crf_level: _Optional[int]=..., allow_open_gop: bool=..., gop_frame_count: _Optional[int]=..., gop_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., enable_two_pass: bool=..., vbv_size_bits: _Optional[int]=..., vbv_fullness_bits: _Optional[int]=..., b_pyramid: bool=..., b_frame_count: _Optional[int]=..., aq_strength: _Optional[float]=..., profile: _Optional[str]=..., tune: _Optional[str]=..., preset: _Optional[str]=...) -> None:
            ...

    class Vp9CodecSettings(_message.Message):
        __slots__ = ('width_pixels', 'height_pixels', 'frame_rate', 'bitrate_bps', 'pixel_format', 'rate_control_mode', 'crf_level', 'gop_frame_count', 'gop_duration', 'profile')
        WIDTH_PIXELS_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_PIXELS_FIELD_NUMBER: _ClassVar[int]
        FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
        BITRATE_BPS_FIELD_NUMBER: _ClassVar[int]
        PIXEL_FORMAT_FIELD_NUMBER: _ClassVar[int]
        RATE_CONTROL_MODE_FIELD_NUMBER: _ClassVar[int]
        CRF_LEVEL_FIELD_NUMBER: _ClassVar[int]
        GOP_FRAME_COUNT_FIELD_NUMBER: _ClassVar[int]
        GOP_DURATION_FIELD_NUMBER: _ClassVar[int]
        PROFILE_FIELD_NUMBER: _ClassVar[int]
        width_pixels: int
        height_pixels: int
        frame_rate: float
        bitrate_bps: int
        pixel_format: str
        rate_control_mode: str
        crf_level: int
        gop_frame_count: int
        gop_duration: _duration_pb2.Duration
        profile: str

        def __init__(self, width_pixels: _Optional[int]=..., height_pixels: _Optional[int]=..., frame_rate: _Optional[float]=..., bitrate_bps: _Optional[int]=..., pixel_format: _Optional[str]=..., rate_control_mode: _Optional[str]=..., crf_level: _Optional[int]=..., gop_frame_count: _Optional[int]=..., gop_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., profile: _Optional[str]=...) -> None:
            ...
    H264_FIELD_NUMBER: _ClassVar[int]
    H265_FIELD_NUMBER: _ClassVar[int]
    VP9_FIELD_NUMBER: _ClassVar[int]
    h264: VideoStream.H264CodecSettings
    h265: VideoStream.H265CodecSettings
    vp9: VideoStream.Vp9CodecSettings

    def __init__(self, h264: _Optional[_Union[VideoStream.H264CodecSettings, _Mapping]]=..., h265: _Optional[_Union[VideoStream.H265CodecSettings, _Mapping]]=..., vp9: _Optional[_Union[VideoStream.Vp9CodecSettings, _Mapping]]=...) -> None:
        ...

class AudioStream(_message.Message):
    __slots__ = ('codec', 'bitrate_bps', 'channel_count', 'channel_layout', 'mapping', 'sample_rate_hertz', 'language_code', 'display_name')

    class AudioMapping(_message.Message):
        __slots__ = ('atom_key', 'input_key', 'input_track', 'input_channel', 'output_channel', 'gain_db')
        ATOM_KEY_FIELD_NUMBER: _ClassVar[int]
        INPUT_KEY_FIELD_NUMBER: _ClassVar[int]
        INPUT_TRACK_FIELD_NUMBER: _ClassVar[int]
        INPUT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        GAIN_DB_FIELD_NUMBER: _ClassVar[int]
        atom_key: str
        input_key: str
        input_track: int
        input_channel: int
        output_channel: int
        gain_db: float

        def __init__(self, atom_key: _Optional[str]=..., input_key: _Optional[str]=..., input_track: _Optional[int]=..., input_channel: _Optional[int]=..., output_channel: _Optional[int]=..., gain_db: _Optional[float]=...) -> None:
            ...
    CODEC_FIELD_NUMBER: _ClassVar[int]
    BITRATE_BPS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_COUNT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    MAPPING_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_HERTZ_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    codec: str
    bitrate_bps: int
    channel_count: int
    channel_layout: _containers.RepeatedScalarFieldContainer[str]
    mapping: _containers.RepeatedCompositeFieldContainer[AudioStream.AudioMapping]
    sample_rate_hertz: int
    language_code: str
    display_name: str

    def __init__(self, codec: _Optional[str]=..., bitrate_bps: _Optional[int]=..., channel_count: _Optional[int]=..., channel_layout: _Optional[_Iterable[str]]=..., mapping: _Optional[_Iterable[_Union[AudioStream.AudioMapping, _Mapping]]]=..., sample_rate_hertz: _Optional[int]=..., language_code: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...

class TextStream(_message.Message):
    __slots__ = ('codec', 'language_code', 'mapping', 'display_name')

    class TextMapping(_message.Message):
        __slots__ = ('atom_key', 'input_key', 'input_track')
        ATOM_KEY_FIELD_NUMBER: _ClassVar[int]
        INPUT_KEY_FIELD_NUMBER: _ClassVar[int]
        INPUT_TRACK_FIELD_NUMBER: _ClassVar[int]
        atom_key: str
        input_key: str
        input_track: int

        def __init__(self, atom_key: _Optional[str]=..., input_key: _Optional[str]=..., input_track: _Optional[int]=...) -> None:
            ...
    CODEC_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    MAPPING_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    codec: str
    language_code: str
    mapping: _containers.RepeatedCompositeFieldContainer[TextStream.TextMapping]
    display_name: str

    def __init__(self, codec: _Optional[str]=..., language_code: _Optional[str]=..., mapping: _Optional[_Iterable[_Union[TextStream.TextMapping, _Mapping]]]=..., display_name: _Optional[str]=...) -> None:
        ...

class SegmentSettings(_message.Message):
    __slots__ = ('segment_duration', 'individual_segments')
    SEGMENT_DURATION_FIELD_NUMBER: _ClassVar[int]
    INDIVIDUAL_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    segment_duration: _duration_pb2.Duration
    individual_segments: bool

    def __init__(self, segment_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., individual_segments: bool=...) -> None:
        ...

class Encryption(_message.Message):
    __slots__ = ('id', 'aes_128', 'sample_aes', 'mpeg_cenc', 'secret_manager_key_source', 'drm_systems')

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
    ID_FIELD_NUMBER: _ClassVar[int]
    AES_128_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_AES_FIELD_NUMBER: _ClassVar[int]
    MPEG_CENC_FIELD_NUMBER: _ClassVar[int]
    SECRET_MANAGER_KEY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DRM_SYSTEMS_FIELD_NUMBER: _ClassVar[int]
    id: str
    aes_128: Encryption.Aes128Encryption
    sample_aes: Encryption.SampleAesEncryption
    mpeg_cenc: Encryption.MpegCommonEncryption
    secret_manager_key_source: Encryption.SecretManagerSource
    drm_systems: Encryption.DrmSystems

    def __init__(self, id: _Optional[str]=..., aes_128: _Optional[_Union[Encryption.Aes128Encryption, _Mapping]]=..., sample_aes: _Optional[_Union[Encryption.SampleAesEncryption, _Mapping]]=..., mpeg_cenc: _Optional[_Union[Encryption.MpegCommonEncryption, _Mapping]]=..., secret_manager_key_source: _Optional[_Union[Encryption.SecretManagerSource, _Mapping]]=..., drm_systems: _Optional[_Union[Encryption.DrmSystems, _Mapping]]=...) -> None:
        ...