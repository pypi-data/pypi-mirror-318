from google.cloud.video.livestream.v1 import resources_pb2 as _resources_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ChannelActivity(_message.Message):
    __slots__ = ('message', 'streaming_state_change', 'streaming_error', 'input_accept', 'input_error', 'input_disconnect', 'event_state_change', 'scte35_command_received')
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STREAMING_STATE_CHANGE_FIELD_NUMBER: _ClassVar[int]
    STREAMING_ERROR_FIELD_NUMBER: _ClassVar[int]
    INPUT_ACCEPT_FIELD_NUMBER: _ClassVar[int]
    INPUT_ERROR_FIELD_NUMBER: _ClassVar[int]
    INPUT_DISCONNECT_FIELD_NUMBER: _ClassVar[int]
    EVENT_STATE_CHANGE_FIELD_NUMBER: _ClassVar[int]
    SCTE35_COMMAND_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    message: str
    streaming_state_change: StreamingStateChange
    streaming_error: StreamingError
    input_accept: InputAccept
    input_error: InputError
    input_disconnect: InputDisconnect
    event_state_change: EventStateChange
    scte35_command_received: Scte35Command

    def __init__(self, message: _Optional[str]=..., streaming_state_change: _Optional[_Union[StreamingStateChange, _Mapping]]=..., streaming_error: _Optional[_Union[StreamingError, _Mapping]]=..., input_accept: _Optional[_Union[InputAccept, _Mapping]]=..., input_error: _Optional[_Union[InputError, _Mapping]]=..., input_disconnect: _Optional[_Union[InputDisconnect, _Mapping]]=..., event_state_change: _Optional[_Union[EventStateChange, _Mapping]]=..., scte35_command_received: _Optional[_Union[Scte35Command, _Mapping]]=...) -> None:
        ...

class StreamingStateChange(_message.Message):
    __slots__ = ('new_state', 'previous_state')
    NEW_STATE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_STATE_FIELD_NUMBER: _ClassVar[int]
    new_state: _resources_pb2.Channel.StreamingState
    previous_state: _resources_pb2.Channel.StreamingState

    def __init__(self, new_state: _Optional[_Union[_resources_pb2.Channel.StreamingState, str]]=..., previous_state: _Optional[_Union[_resources_pb2.Channel.StreamingState, str]]=...) -> None:
        ...

class StreamingError(_message.Message):
    __slots__ = ('error',)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _status_pb2.Status

    def __init__(self, error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class InputAccept(_message.Message):
    __slots__ = ('stream_id', 'input_attachment', 'input_stream_property')
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_STREAM_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    stream_id: str
    input_attachment: str
    input_stream_property: InputStreamProperty

    def __init__(self, stream_id: _Optional[str]=..., input_attachment: _Optional[str]=..., input_stream_property: _Optional[_Union[InputStreamProperty, _Mapping]]=...) -> None:
        ...

class InputError(_message.Message):
    __slots__ = ('stream_id', 'input_attachment', 'input_stream_property', 'error')
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_STREAM_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    stream_id: str
    input_attachment: str
    input_stream_property: InputStreamProperty
    error: _status_pb2.Status

    def __init__(self, stream_id: _Optional[str]=..., input_attachment: _Optional[str]=..., input_stream_property: _Optional[_Union[InputStreamProperty, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class InputStreamProperty(_message.Message):
    __slots__ = ('video_streams', 'audio_streams')
    VIDEO_STREAMS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_STREAMS_FIELD_NUMBER: _ClassVar[int]
    video_streams: _containers.RepeatedCompositeFieldContainer[VideoStream]
    audio_streams: _containers.RepeatedCompositeFieldContainer[AudioStream]

    def __init__(self, video_streams: _Optional[_Iterable[_Union[VideoStream, _Mapping]]]=..., audio_streams: _Optional[_Iterable[_Union[AudioStream, _Mapping]]]=...) -> None:
        ...

class VideoStream(_message.Message):
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

class AudioStream(_message.Message):
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

class InputDisconnect(_message.Message):
    __slots__ = ('stream_id', 'input_attachment')
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    stream_id: str
    input_attachment: str

    def __init__(self, stream_id: _Optional[str]=..., input_attachment: _Optional[str]=...) -> None:
        ...

class EventStateChange(_message.Message):
    __slots__ = ('event_id', 'new_state', 'previous_state')
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_STATE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_STATE_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    new_state: _resources_pb2.Event.State
    previous_state: _resources_pb2.Event.State

    def __init__(self, event_id: _Optional[str]=..., new_state: _Optional[_Union[_resources_pb2.Event.State, str]]=..., previous_state: _Optional[_Union[_resources_pb2.Event.State, str]]=...) -> None:
        ...

class Scte35Command(_message.Message):
    __slots__ = ('splice_info_section',)

    class SpliceTime(_message.Message):
        __slots__ = ('time_specified_flag', 'pts_time')
        TIME_SPECIFIED_FLAG_FIELD_NUMBER: _ClassVar[int]
        PTS_TIME_FIELD_NUMBER: _ClassVar[int]
        time_specified_flag: bool
        pts_time: int

        def __init__(self, time_specified_flag: bool=..., pts_time: _Optional[int]=...) -> None:
            ...

    class BreakDuration(_message.Message):
        __slots__ = ('auto_return', 'duration')
        AUTO_RETURN_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        auto_return: bool
        duration: int

        def __init__(self, auto_return: bool=..., duration: _Optional[int]=...) -> None:
            ...

    class Component(_message.Message):
        __slots__ = ('component_tag', 'splice_time')
        COMPONENT_TAG_FIELD_NUMBER: _ClassVar[int]
        SPLICE_TIME_FIELD_NUMBER: _ClassVar[int]
        component_tag: int
        splice_time: Scte35Command.SpliceTime

        def __init__(self, component_tag: _Optional[int]=..., splice_time: _Optional[_Union[Scte35Command.SpliceTime, _Mapping]]=...) -> None:
            ...

    class SpliceInsert(_message.Message):
        __slots__ = ('splice_event_id', 'splice_event_cancel_indicator', 'out_of_network_indicator', 'program_splice_flag', 'duration_flag', 'splice_immediate_flag', 'splice_time', 'break_duration', 'unique_program_id', 'avail_num', 'avails_expected', 'component_count', 'components')
        SPLICE_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
        SPLICE_EVENT_CANCEL_INDICATOR_FIELD_NUMBER: _ClassVar[int]
        OUT_OF_NETWORK_INDICATOR_FIELD_NUMBER: _ClassVar[int]
        PROGRAM_SPLICE_FLAG_FIELD_NUMBER: _ClassVar[int]
        DURATION_FLAG_FIELD_NUMBER: _ClassVar[int]
        SPLICE_IMMEDIATE_FLAG_FIELD_NUMBER: _ClassVar[int]
        SPLICE_TIME_FIELD_NUMBER: _ClassVar[int]
        BREAK_DURATION_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_PROGRAM_ID_FIELD_NUMBER: _ClassVar[int]
        AVAIL_NUM_FIELD_NUMBER: _ClassVar[int]
        AVAILS_EXPECTED_FIELD_NUMBER: _ClassVar[int]
        COMPONENT_COUNT_FIELD_NUMBER: _ClassVar[int]
        COMPONENTS_FIELD_NUMBER: _ClassVar[int]
        splice_event_id: int
        splice_event_cancel_indicator: bool
        out_of_network_indicator: bool
        program_splice_flag: bool
        duration_flag: bool
        splice_immediate_flag: bool
        splice_time: Scte35Command.SpliceTime
        break_duration: Scte35Command.BreakDuration
        unique_program_id: int
        avail_num: int
        avails_expected: int
        component_count: int
        components: _containers.RepeatedCompositeFieldContainer[Scte35Command.Component]

        def __init__(self, splice_event_id: _Optional[int]=..., splice_event_cancel_indicator: bool=..., out_of_network_indicator: bool=..., program_splice_flag: bool=..., duration_flag: bool=..., splice_immediate_flag: bool=..., splice_time: _Optional[_Union[Scte35Command.SpliceTime, _Mapping]]=..., break_duration: _Optional[_Union[Scte35Command.BreakDuration, _Mapping]]=..., unique_program_id: _Optional[int]=..., avail_num: _Optional[int]=..., avails_expected: _Optional[int]=..., component_count: _Optional[int]=..., components: _Optional[_Iterable[_Union[Scte35Command.Component, _Mapping]]]=...) -> None:
            ...

    class SpliceInfoSection(_message.Message):
        __slots__ = ('pts_adjustment', 'splice_insert')
        PTS_ADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
        SPLICE_INSERT_FIELD_NUMBER: _ClassVar[int]
        pts_adjustment: int
        splice_insert: Scte35Command.SpliceInsert

        def __init__(self, pts_adjustment: _Optional[int]=..., splice_insert: _Optional[_Union[Scte35Command.SpliceInsert, _Mapping]]=...) -> None:
            ...
    SPLICE_INFO_SECTION_FIELD_NUMBER: _ClassVar[int]
    splice_info_section: Scte35Command.SpliceInfoSection

    def __init__(self, splice_info_section: _Optional[_Union[Scte35Command.SpliceInfoSection, _Mapping]]=...) -> None:
        ...