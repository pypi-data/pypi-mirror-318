"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/video/livestream/logging/v1/logs.proto')
_sym_db = _symbol_database.Default()
from .......google.cloud.video.livestream.v1 import resources_pb2 as google_dot_cloud_dot_video_dot_livestream_dot_v1_dot_resources__pb2
from .......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/video/livestream/logging/v1/logs.proto\x12(google.cloud.video.livestream.logging.v1\x1a0google/cloud/video/livestream/v1/resources.proto\x1a\x17google/rpc/status.proto"\x93\x05\n\x0fChannelActivity\x12\x0f\n\x07message\x18\x01 \x01(\t\x12`\n\x16streaming_state_change\x18\x02 \x01(\x0b2>.google.cloud.video.livestream.logging.v1.StreamingStateChangeH\x00\x12S\n\x0fstreaming_error\x18\x03 \x01(\x0b28.google.cloud.video.livestream.logging.v1.StreamingErrorH\x00\x12M\n\x0cinput_accept\x18\x04 \x01(\x0b25.google.cloud.video.livestream.logging.v1.InputAcceptH\x00\x12K\n\x0binput_error\x18\x05 \x01(\x0b24.google.cloud.video.livestream.logging.v1.InputErrorH\x00\x12U\n\x10input_disconnect\x18\x06 \x01(\x0b29.google.cloud.video.livestream.logging.v1.InputDisconnectH\x00\x12X\n\x12event_state_change\x18\x07 \x01(\x0b2:.google.cloud.video.livestream.logging.v1.EventStateChangeH\x00\x12Z\n\x17scte35_command_received\x18\x08 \x01(\x0b27.google.cloud.video.livestream.logging.v1.Scte35CommandH\x00B\x0f\n\ractivity_type"\xb5\x01\n\x14StreamingStateChange\x12K\n\tnew_state\x18\x01 \x01(\x0e28.google.cloud.video.livestream.v1.Channel.StreamingState\x12P\n\x0eprevious_state\x18\x02 \x01(\x0e28.google.cloud.video.livestream.v1.Channel.StreamingState"3\n\x0eStreamingError\x12!\n\x05error\x18\x01 \x01(\x0b2\x12.google.rpc.Status"\x98\x01\n\x0bInputAccept\x12\x11\n\tstream_id\x18\x01 \x01(\t\x12\x18\n\x10input_attachment\x18\x02 \x01(\t\x12\\\n\x15input_stream_property\x18\x03 \x01(\x0b2=.google.cloud.video.livestream.logging.v1.InputStreamProperty"\xba\x01\n\nInputError\x12\x11\n\tstream_id\x18\x01 \x01(\t\x12\x18\n\x10input_attachment\x18\x02 \x01(\t\x12\\\n\x15input_stream_property\x18\x03 \x01(\x0b2=.google.cloud.video.livestream.logging.v1.InputStreamProperty\x12!\n\x05error\x18\x04 \x01(\x0b2\x12.google.rpc.Status"\xb1\x01\n\x13InputStreamProperty\x12L\n\rvideo_streams\x18\x01 \x03(\x0b25.google.cloud.video.livestream.logging.v1.VideoStream\x12L\n\raudio_streams\x18\x02 \x03(\x0b25.google.cloud.video.livestream.logging.v1.AudioStream"i\n\x0bVideoStream\x12\r\n\x05index\x18\x01 \x01(\x05\x12K\n\x0cvideo_format\x18\x02 \x01(\x0b25.google.cloud.video.livestream.logging.v1.VideoFormat"]\n\x0bVideoFormat\x12\r\n\x05codec\x18\x01 \x01(\t\x12\x14\n\x0cwidth_pixels\x18\x02 \x01(\x05\x12\x15\n\rheight_pixels\x18\x03 \x01(\x05\x12\x12\n\nframe_rate\x18\x04 \x01(\x01"i\n\x0bAudioStream\x12\r\n\x05index\x18\x01 \x01(\x05\x12K\n\x0caudio_format\x18\x02 \x01(\x0b25.google.cloud.video.livestream.logging.v1.AudioFormat"K\n\x0bAudioFormat\x12\r\n\x05codec\x18\x01 \x01(\t\x12\x15\n\rchannel_count\x18\x02 \x01(\x05\x12\x16\n\x0echannel_layout\x18\x03 \x03(\t">\n\x0fInputDisconnect\x12\x11\n\tstream_id\x18\x01 \x01(\t\x12\x18\n\x10input_attachment\x18\x02 \x01(\t"\xad\x01\n\x10EventStateChange\x12\x10\n\x08event_id\x18\x01 \x01(\t\x12@\n\tnew_state\x18\x02 \x01(\x0e2-.google.cloud.video.livestream.v1.Event.State\x12E\n\x0eprevious_state\x18\x03 \x01(\x0e2-.google.cloud.video.livestream.v1.Event.State"\xa9\x08\n\rScte35Command\x12f\n\x13splice_info_section\x18\x01 \x01(\x0b2I.google.cloud.video.livestream.logging.v1.Scte35Command.SpliceInfoSection\x1a;\n\nSpliceTime\x12\x1b\n\x13time_specified_flag\x18\x01 \x01(\x08\x12\x10\n\x08pts_time\x18\x02 \x01(\x03\x1a6\n\rBreakDuration\x12\x13\n\x0bauto_return\x18\x01 \x01(\x08\x12\x10\n\x08duration\x18\x02 \x01(\x03\x1a{\n\tComponent\x12\x15\n\rcomponent_tag\x18\x01 \x01(\x05\x12W\n\x0bsplice_time\x18\x02 \x01(\x0b2B.google.cloud.video.livestream.logging.v1.Scte35Command.SpliceTime\x1a\xb2\x04\n\x0cSpliceInsert\x12\x17\n\x0fsplice_event_id\x18\x01 \x01(\x05\x12%\n\x1dsplice_event_cancel_indicator\x18\x02 \x01(\x08\x12 \n\x18out_of_network_indicator\x18\x03 \x01(\x08\x12\x1b\n\x13program_splice_flag\x18\x04 \x01(\x08\x12\x15\n\rduration_flag\x18\x05 \x01(\x08\x12\x1d\n\x15splice_immediate_flag\x18\x06 \x01(\x08\x12W\n\x0bsplice_time\x18\x07 \x01(\x0b2B.google.cloud.video.livestream.logging.v1.Scte35Command.SpliceTime\x12]\n\x0ebreak_duration\x18\x08 \x01(\x0b2E.google.cloud.video.livestream.logging.v1.Scte35Command.BreakDuration\x12\x19\n\x11unique_program_id\x18\t \x01(\x05\x12\x11\n\tavail_num\x18\n \x01(\x05\x12\x17\n\x0favails_expected\x18\x0b \x01(\x05\x12\x17\n\x0fcomponent_count\x18\x0c \x01(\x05\x12U\n\ncomponents\x18\r \x03(\x0b2A.google.cloud.video.livestream.logging.v1.Scte35Command.Component\x1a\x88\x01\n\x11SpliceInfoSection\x12\x16\n\x0epts_adjustment\x18\x01 \x01(\x03\x12[\n\rsplice_insert\x18\x02 \x01(\x0b2D.google.cloud.video.livestream.logging.v1.Scte35Command.SpliceInsertB\x83\x01\n,com.google.cloud.video.livestream.logging.v1B\tLogsProtoP\x01ZFcloud.google.com/go/video/livestream/logging/apiv1/loggingpb;loggingpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.video.livestream.logging.v1.logs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.cloud.video.livestream.logging.v1B\tLogsProtoP\x01ZFcloud.google.com/go/video/livestream/logging/apiv1/loggingpb;loggingpb'
    _globals['_CHANNELACTIVITY']._serialized_start = 173
    _globals['_CHANNELACTIVITY']._serialized_end = 832
    _globals['_STREAMINGSTATECHANGE']._serialized_start = 835
    _globals['_STREAMINGSTATECHANGE']._serialized_end = 1016
    _globals['_STREAMINGERROR']._serialized_start = 1018
    _globals['_STREAMINGERROR']._serialized_end = 1069
    _globals['_INPUTACCEPT']._serialized_start = 1072
    _globals['_INPUTACCEPT']._serialized_end = 1224
    _globals['_INPUTERROR']._serialized_start = 1227
    _globals['_INPUTERROR']._serialized_end = 1413
    _globals['_INPUTSTREAMPROPERTY']._serialized_start = 1416
    _globals['_INPUTSTREAMPROPERTY']._serialized_end = 1593
    _globals['_VIDEOSTREAM']._serialized_start = 1595
    _globals['_VIDEOSTREAM']._serialized_end = 1700
    _globals['_VIDEOFORMAT']._serialized_start = 1702
    _globals['_VIDEOFORMAT']._serialized_end = 1795
    _globals['_AUDIOSTREAM']._serialized_start = 1797
    _globals['_AUDIOSTREAM']._serialized_end = 1902
    _globals['_AUDIOFORMAT']._serialized_start = 1904
    _globals['_AUDIOFORMAT']._serialized_end = 1979
    _globals['_INPUTDISCONNECT']._serialized_start = 1981
    _globals['_INPUTDISCONNECT']._serialized_end = 2043
    _globals['_EVENTSTATECHANGE']._serialized_start = 2046
    _globals['_EVENTSTATECHANGE']._serialized_end = 2219
    _globals['_SCTE35COMMAND']._serialized_start = 2222
    _globals['_SCTE35COMMAND']._serialized_end = 3287
    _globals['_SCTE35COMMAND_SPLICETIME']._serialized_start = 2343
    _globals['_SCTE35COMMAND_SPLICETIME']._serialized_end = 2402
    _globals['_SCTE35COMMAND_BREAKDURATION']._serialized_start = 2404
    _globals['_SCTE35COMMAND_BREAKDURATION']._serialized_end = 2458
    _globals['_SCTE35COMMAND_COMPONENT']._serialized_start = 2460
    _globals['_SCTE35COMMAND_COMPONENT']._serialized_end = 2583
    _globals['_SCTE35COMMAND_SPLICEINSERT']._serialized_start = 2586
    _globals['_SCTE35COMMAND_SPLICEINSERT']._serialized_end = 3148
    _globals['_SCTE35COMMAND_SPLICEINFOSECTION']._serialized_start = 3151
    _globals['_SCTE35COMMAND_SPLICEINFOSECTION']._serialized_end = 3287