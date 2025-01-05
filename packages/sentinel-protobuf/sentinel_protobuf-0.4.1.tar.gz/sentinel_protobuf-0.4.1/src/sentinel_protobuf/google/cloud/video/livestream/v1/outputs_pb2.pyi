from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.type import datetime_pb2 as _datetime_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

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
    __slots__ = ('key', 'container', 'elementary_streams', 'segment_settings', 'encryption_id')
    KEY_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    ELEMENTARY_STREAMS_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_ID_FIELD_NUMBER: _ClassVar[int]
    key: str
    container: str
    elementary_streams: _containers.RepeatedScalarFieldContainer[str]
    segment_settings: SegmentSettings
    encryption_id: str

    def __init__(self, key: _Optional[str]=..., container: _Optional[str]=..., elementary_streams: _Optional[_Iterable[str]]=..., segment_settings: _Optional[_Union[SegmentSettings, _Mapping]]=..., encryption_id: _Optional[str]=...) -> None:
        ...

class Manifest(_message.Message):
    __slots__ = ('file_name', 'type', 'mux_streams', 'max_segment_count', 'segment_keep_duration', 'use_timecode_as_timeline', 'key')

    class ManifestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MANIFEST_TYPE_UNSPECIFIED: _ClassVar[Manifest.ManifestType]
        HLS: _ClassVar[Manifest.ManifestType]
        DASH: _ClassVar[Manifest.ManifestType]
    MANIFEST_TYPE_UNSPECIFIED: Manifest.ManifestType
    HLS: Manifest.ManifestType
    DASH: Manifest.ManifestType
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MUX_STREAMS_FIELD_NUMBER: _ClassVar[int]
    MAX_SEGMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_KEEP_DURATION_FIELD_NUMBER: _ClassVar[int]
    USE_TIMECODE_AS_TIMELINE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    type: Manifest.ManifestType
    mux_streams: _containers.RepeatedScalarFieldContainer[str]
    max_segment_count: int
    segment_keep_duration: _duration_pb2.Duration
    use_timecode_as_timeline: bool
    key: str

    def __init__(self, file_name: _Optional[str]=..., type: _Optional[_Union[Manifest.ManifestType, str]]=..., mux_streams: _Optional[_Iterable[str]]=..., max_segment_count: _Optional[int]=..., segment_keep_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., use_timecode_as_timeline: bool=..., key: _Optional[str]=...) -> None:
        ...

class SpriteSheet(_message.Message):
    __slots__ = ('format', 'file_prefix', 'sprite_width_pixels', 'sprite_height_pixels', 'column_count', 'row_count', 'interval', 'quality')
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    FILE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    SPRITE_WIDTH_PIXELS_FIELD_NUMBER: _ClassVar[int]
    SPRITE_HEIGHT_PIXELS_FIELD_NUMBER: _ClassVar[int]
    COLUMN_COUNT_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    format: str
    file_prefix: str
    sprite_width_pixels: int
    sprite_height_pixels: int
    column_count: int
    row_count: int
    interval: _duration_pb2.Duration
    quality: int

    def __init__(self, format: _Optional[str]=..., file_prefix: _Optional[str]=..., sprite_width_pixels: _Optional[int]=..., sprite_height_pixels: _Optional[int]=..., column_count: _Optional[int]=..., row_count: _Optional[int]=..., interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., quality: _Optional[int]=...) -> None:
        ...

class PreprocessingConfig(_message.Message):
    __slots__ = ('audio', 'crop', 'pad')

    class Audio(_message.Message):
        __slots__ = ('lufs',)
        LUFS_FIELD_NUMBER: _ClassVar[int]
        lufs: float

        def __init__(self, lufs: _Optional[float]=...) -> None:
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
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    CROP_FIELD_NUMBER: _ClassVar[int]
    PAD_FIELD_NUMBER: _ClassVar[int]
    audio: PreprocessingConfig.Audio
    crop: PreprocessingConfig.Crop
    pad: PreprocessingConfig.Pad

    def __init__(self, audio: _Optional[_Union[PreprocessingConfig.Audio, _Mapping]]=..., crop: _Optional[_Union[PreprocessingConfig.Crop, _Mapping]]=..., pad: _Optional[_Union[PreprocessingConfig.Pad, _Mapping]]=...) -> None:
        ...

class VideoStream(_message.Message):
    __slots__ = ('h264',)

    class H264CodecSettings(_message.Message):
        __slots__ = ('width_pixels', 'height_pixels', 'frame_rate', 'bitrate_bps', 'allow_open_gop', 'gop_frame_count', 'gop_duration', 'vbv_size_bits', 'vbv_fullness_bits', 'entropy_coder', 'b_pyramid', 'b_frame_count', 'aq_strength', 'profile', 'tune')
        WIDTH_PIXELS_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_PIXELS_FIELD_NUMBER: _ClassVar[int]
        FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
        BITRATE_BPS_FIELD_NUMBER: _ClassVar[int]
        ALLOW_OPEN_GOP_FIELD_NUMBER: _ClassVar[int]
        GOP_FRAME_COUNT_FIELD_NUMBER: _ClassVar[int]
        GOP_DURATION_FIELD_NUMBER: _ClassVar[int]
        VBV_SIZE_BITS_FIELD_NUMBER: _ClassVar[int]
        VBV_FULLNESS_BITS_FIELD_NUMBER: _ClassVar[int]
        ENTROPY_CODER_FIELD_NUMBER: _ClassVar[int]
        B_PYRAMID_FIELD_NUMBER: _ClassVar[int]
        B_FRAME_COUNT_FIELD_NUMBER: _ClassVar[int]
        AQ_STRENGTH_FIELD_NUMBER: _ClassVar[int]
        PROFILE_FIELD_NUMBER: _ClassVar[int]
        TUNE_FIELD_NUMBER: _ClassVar[int]
        width_pixels: int
        height_pixels: int
        frame_rate: float
        bitrate_bps: int
        allow_open_gop: bool
        gop_frame_count: int
        gop_duration: _duration_pb2.Duration
        vbv_size_bits: int
        vbv_fullness_bits: int
        entropy_coder: str
        b_pyramid: bool
        b_frame_count: int
        aq_strength: float
        profile: str
        tune: str

        def __init__(self, width_pixels: _Optional[int]=..., height_pixels: _Optional[int]=..., frame_rate: _Optional[float]=..., bitrate_bps: _Optional[int]=..., allow_open_gop: bool=..., gop_frame_count: _Optional[int]=..., gop_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., vbv_size_bits: _Optional[int]=..., vbv_fullness_bits: _Optional[int]=..., entropy_coder: _Optional[str]=..., b_pyramid: bool=..., b_frame_count: _Optional[int]=..., aq_strength: _Optional[float]=..., profile: _Optional[str]=..., tune: _Optional[str]=...) -> None:
            ...
    H264_FIELD_NUMBER: _ClassVar[int]
    h264: VideoStream.H264CodecSettings

    def __init__(self, h264: _Optional[_Union[VideoStream.H264CodecSettings, _Mapping]]=...) -> None:
        ...

class AudioStream(_message.Message):
    __slots__ = ('transmux', 'codec', 'bitrate_bps', 'channel_count', 'channel_layout', 'mapping', 'sample_rate_hertz')

    class AudioMapping(_message.Message):
        __slots__ = ('input_key', 'input_track', 'input_channel', 'output_channel', 'gain_db')
        INPUT_KEY_FIELD_NUMBER: _ClassVar[int]
        INPUT_TRACK_FIELD_NUMBER: _ClassVar[int]
        INPUT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        GAIN_DB_FIELD_NUMBER: _ClassVar[int]
        input_key: str
        input_track: int
        input_channel: int
        output_channel: int
        gain_db: float

        def __init__(self, input_key: _Optional[str]=..., input_track: _Optional[int]=..., input_channel: _Optional[int]=..., output_channel: _Optional[int]=..., gain_db: _Optional[float]=...) -> None:
            ...
    TRANSMUX_FIELD_NUMBER: _ClassVar[int]
    CODEC_FIELD_NUMBER: _ClassVar[int]
    BITRATE_BPS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_COUNT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    MAPPING_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_HERTZ_FIELD_NUMBER: _ClassVar[int]
    transmux: bool
    codec: str
    bitrate_bps: int
    channel_count: int
    channel_layout: _containers.RepeatedScalarFieldContainer[str]
    mapping: _containers.RepeatedCompositeFieldContainer[AudioStream.AudioMapping]
    sample_rate_hertz: int

    def __init__(self, transmux: bool=..., codec: _Optional[str]=..., bitrate_bps: _Optional[int]=..., channel_count: _Optional[int]=..., channel_layout: _Optional[_Iterable[str]]=..., mapping: _Optional[_Iterable[_Union[AudioStream.AudioMapping, _Mapping]]]=..., sample_rate_hertz: _Optional[int]=...) -> None:
        ...

class TextStream(_message.Message):
    __slots__ = ('codec',)
    CODEC_FIELD_NUMBER: _ClassVar[int]
    codec: str

    def __init__(self, codec: _Optional[str]=...) -> None:
        ...

class SegmentSettings(_message.Message):
    __slots__ = ('segment_duration',)
    SEGMENT_DURATION_FIELD_NUMBER: _ClassVar[int]
    segment_duration: _duration_pb2.Duration

    def __init__(self, segment_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class TimecodeConfig(_message.Message):
    __slots__ = ('source', 'utc_offset', 'time_zone')

    class TimecodeSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIMECODE_SOURCE_UNSPECIFIED: _ClassVar[TimecodeConfig.TimecodeSource]
        MEDIA_TIMESTAMP: _ClassVar[TimecodeConfig.TimecodeSource]
        EMBEDDED_TIMECODE: _ClassVar[TimecodeConfig.TimecodeSource]
    TIMECODE_SOURCE_UNSPECIFIED: TimecodeConfig.TimecodeSource
    MEDIA_TIMESTAMP: TimecodeConfig.TimecodeSource
    EMBEDDED_TIMECODE: TimecodeConfig.TimecodeSource
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    UTC_OFFSET_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    source: TimecodeConfig.TimecodeSource
    utc_offset: _duration_pb2.Duration
    time_zone: _datetime_pb2.TimeZone

    def __init__(self, source: _Optional[_Union[TimecodeConfig.TimecodeSource, str]]=..., utc_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., time_zone: _Optional[_Union[_datetime_pb2.TimeZone, _Mapping]]=...) -> None:
        ...