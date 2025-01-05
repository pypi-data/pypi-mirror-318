"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/video/livestream/v1/outputs.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ......google.type import datetime_pb2 as google_dot_type_dot_datetime__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/video/livestream/v1/outputs.proto\x12 google.cloud.video.livestream.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1agoogle/type/datetime.proto"\x87\x02\n\x10ElementaryStream\x12\x0b\n\x03key\x18\x04 \x01(\t\x12E\n\x0cvideo_stream\x18\x01 \x01(\x0b2-.google.cloud.video.livestream.v1.VideoStreamH\x00\x12E\n\x0caudio_stream\x18\x02 \x01(\x0b2-.google.cloud.video.livestream.v1.AudioStreamH\x00\x12C\n\x0btext_stream\x18\x03 \x01(\x0b2,.google.cloud.video.livestream.v1.TextStreamH\x00B\x13\n\x11elementary_stream"\xab\x01\n\tMuxStream\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x11\n\tcontainer\x18\x03 \x01(\t\x12\x1a\n\x12elementary_streams\x18\x04 \x03(\t\x12K\n\x10segment_settings\x18\x05 \x01(\x0b21.google.cloud.video.livestream.v1.SegmentSettings\x12\x15\n\rencryption_id\x18\x06 \x01(\t"\xce\x02\n\x08Manifest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12J\n\x04type\x18\x02 \x01(\x0e27.google.cloud.video.livestream.v1.Manifest.ManifestTypeB\x03\xe0A\x02\x12\x18\n\x0bmux_streams\x18\x03 \x03(\tB\x03\xe0A\x02\x12\x19\n\x11max_segment_count\x18\x04 \x01(\x05\x128\n\x15segment_keep_duration\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12 \n\x18use_timecode_as_timeline\x18\x06 \x01(\x08\x12\x10\n\x03key\x18\x07 \x01(\tB\x03\xe0A\x01"@\n\x0cManifestType\x12\x1d\n\x19MANIFEST_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03HLS\x10\x01\x12\x08\n\x04DASH\x10\x02"\xe3\x01\n\x0bSpriteSheet\x12\x0e\n\x06format\x18\x01 \x01(\t\x12\x18\n\x0bfile_prefix\x18\x02 \x01(\tB\x03\xe0A\x02\x12 \n\x13sprite_width_pixels\x18\x03 \x01(\x05B\x03\xe0A\x02\x12!\n\x14sprite_height_pixels\x18\x04 \x01(\x05B\x03\xe0A\x02\x12\x14\n\x0ccolumn_count\x18\x05 \x01(\x05\x12\x11\n\trow_count\x18\x06 \x01(\x05\x12+\n\x08interval\x18\x07 \x01(\x0b2\x19.google.protobuf.Duration\x12\x0f\n\x07quality\x18\x08 \x01(\x05"\xc5\x03\n\x13PreprocessingConfig\x12J\n\x05audio\x18\x01 \x01(\x0b2;.google.cloud.video.livestream.v1.PreprocessingConfig.Audio\x12H\n\x04crop\x18\x02 \x01(\x0b2:.google.cloud.video.livestream.v1.PreprocessingConfig.Crop\x12F\n\x03pad\x18\x03 \x01(\x0b29.google.cloud.video.livestream.v1.PreprocessingConfig.Pad\x1a\x15\n\x05Audio\x12\x0c\n\x04lufs\x18\x01 \x01(\x01\x1a\\\n\x04Crop\x12\x12\n\ntop_pixels\x18\x01 \x01(\x05\x12\x15\n\rbottom_pixels\x18\x02 \x01(\x05\x12\x13\n\x0bleft_pixels\x18\x03 \x01(\x05\x12\x14\n\x0cright_pixels\x18\x04 \x01(\x05\x1a[\n\x03Pad\x12\x12\n\ntop_pixels\x18\x01 \x01(\x05\x12\x15\n\rbottom_pixels\x18\x02 \x01(\x05\x12\x13\n\x0bleft_pixels\x18\x03 \x01(\x05\x12\x14\n\x0cright_pixels\x18\x04 \x01(\x05"\xff\x03\n\x0bVideoStream\x12O\n\x04h264\x18\x14 \x01(\x0b2?.google.cloud.video.livestream.v1.VideoStream.H264CodecSettingsH\x00\x1a\x8c\x03\n\x11H264CodecSettings\x12\x14\n\x0cwidth_pixels\x18\x01 \x01(\x05\x12\x15\n\rheight_pixels\x18\x02 \x01(\x05\x12\x17\n\nframe_rate\x18\x03 \x01(\x01B\x03\xe0A\x02\x12\x18\n\x0bbitrate_bps\x18\x04 \x01(\x05B\x03\xe0A\x02\x12\x16\n\x0eallow_open_gop\x18\x06 \x01(\x08\x12\x19\n\x0fgop_frame_count\x18\x07 \x01(\x05H\x00\x121\n\x0cgop_duration\x18\x08 \x01(\x0b2\x19.google.protobuf.DurationH\x00\x12\x15\n\rvbv_size_bits\x18\t \x01(\x05\x12\x19\n\x11vbv_fullness_bits\x18\n \x01(\x05\x12\x15\n\rentropy_coder\x18\x0b \x01(\t\x12\x11\n\tb_pyramid\x18\x0c \x01(\x08\x12\x15\n\rb_frame_count\x18\r \x01(\x05\x12\x13\n\x0baq_strength\x18\x0e \x01(\x01\x12\x0f\n\x07profile\x18\x0f \x01(\t\x12\x0c\n\x04tune\x18\x10 \x01(\tB\n\n\x08gop_modeB\x10\n\x0ecodec_settings"\xec\x02\n\x0bAudioStream\x12\x10\n\x08transmux\x18\x08 \x01(\x08\x12\r\n\x05codec\x18\x01 \x01(\t\x12\x18\n\x0bbitrate_bps\x18\x02 \x01(\x05B\x03\xe0A\x02\x12\x15\n\rchannel_count\x18\x03 \x01(\x05\x12\x16\n\x0echannel_layout\x18\x04 \x03(\t\x12K\n\x07mapping\x18\x05 \x03(\x0b2:.google.cloud.video.livestream.v1.AudioStream.AudioMapping\x12\x19\n\x11sample_rate_hertz\x18\x06 \x01(\x05\x1a\x8a\x01\n\x0cAudioMapping\x12\x16\n\tinput_key\x18\x06 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0binput_track\x18\x02 \x01(\x05B\x03\xe0A\x02\x12\x1a\n\rinput_channel\x18\x03 \x01(\x05B\x03\xe0A\x02\x12\x1b\n\x0eoutput_channel\x18\x04 \x01(\x05B\x03\xe0A\x02\x12\x0f\n\x07gain_db\x18\x05 \x01(\x01" \n\nTextStream\x12\x12\n\x05codec\x18\x01 \x01(\tB\x03\xe0A\x02"F\n\x0fSegmentSettings\x123\n\x10segment_duration\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration"\xac\x02\n\x0eTimecodeConfig\x12O\n\x06source\x18\x01 \x01(\x0e2?.google.cloud.video.livestream.v1.TimecodeConfig.TimecodeSource\x12/\n\nutc_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationH\x00\x12*\n\ttime_zone\x18\x03 \x01(\x0b2\x15.google.type.TimeZoneH\x00"]\n\x0eTimecodeSource\x12\x1f\n\x1bTIMECODE_SOURCE_UNSPECIFIED\x10\x00\x12\x13\n\x0fMEDIA_TIMESTAMP\x10\x01\x12\x15\n\x11EMBEDDED_TIMECODE\x10\x02B\r\n\x0btime_offsetB\xe9\x01\n$com.google.cloud.video.livestream.v1B\x0cOutputsProtoP\x01ZDcloud.google.com/go/video/livestream/apiv1/livestreampb;livestreampb\xaa\x02 Google.Cloud.Video.LiveStream.V1\xca\x02 Google\\Cloud\\Video\\LiveStream\\V1\xea\x02$Google::Cloud::Video::LiveStream::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.video.livestream.v1.outputs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.video.livestream.v1B\x0cOutputsProtoP\x01ZDcloud.google.com/go/video/livestream/apiv1/livestreampb;livestreampb\xaa\x02 Google.Cloud.Video.LiveStream.V1\xca\x02 Google\\Cloud\\Video\\LiveStream\\V1\xea\x02$Google::Cloud::Video::LiveStream::V1'
    _globals['_MANIFEST'].fields_by_name['type']._loaded_options = None
    _globals['_MANIFEST'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_MANIFEST'].fields_by_name['mux_streams']._loaded_options = None
    _globals['_MANIFEST'].fields_by_name['mux_streams']._serialized_options = b'\xe0A\x02'
    _globals['_MANIFEST'].fields_by_name['key']._loaded_options = None
    _globals['_MANIFEST'].fields_by_name['key']._serialized_options = b'\xe0A\x01'
    _globals['_SPRITESHEET'].fields_by_name['file_prefix']._loaded_options = None
    _globals['_SPRITESHEET'].fields_by_name['file_prefix']._serialized_options = b'\xe0A\x02'
    _globals['_SPRITESHEET'].fields_by_name['sprite_width_pixels']._loaded_options = None
    _globals['_SPRITESHEET'].fields_by_name['sprite_width_pixels']._serialized_options = b'\xe0A\x02'
    _globals['_SPRITESHEET'].fields_by_name['sprite_height_pixels']._loaded_options = None
    _globals['_SPRITESHEET'].fields_by_name['sprite_height_pixels']._serialized_options = b'\xe0A\x02'
    _globals['_VIDEOSTREAM_H264CODECSETTINGS'].fields_by_name['frame_rate']._loaded_options = None
    _globals['_VIDEOSTREAM_H264CODECSETTINGS'].fields_by_name['frame_rate']._serialized_options = b'\xe0A\x02'
    _globals['_VIDEOSTREAM_H264CODECSETTINGS'].fields_by_name['bitrate_bps']._loaded_options = None
    _globals['_VIDEOSTREAM_H264CODECSETTINGS'].fields_by_name['bitrate_bps']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIOSTREAM_AUDIOMAPPING'].fields_by_name['input_key']._loaded_options = None
    _globals['_AUDIOSTREAM_AUDIOMAPPING'].fields_by_name['input_key']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIOSTREAM_AUDIOMAPPING'].fields_by_name['input_track']._loaded_options = None
    _globals['_AUDIOSTREAM_AUDIOMAPPING'].fields_by_name['input_track']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIOSTREAM_AUDIOMAPPING'].fields_by_name['input_channel']._loaded_options = None
    _globals['_AUDIOSTREAM_AUDIOMAPPING'].fields_by_name['input_channel']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIOSTREAM_AUDIOMAPPING'].fields_by_name['output_channel']._loaded_options = None
    _globals['_AUDIOSTREAM_AUDIOMAPPING'].fields_by_name['output_channel']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIOSTREAM'].fields_by_name['bitrate_bps']._loaded_options = None
    _globals['_AUDIOSTREAM'].fields_by_name['bitrate_bps']._serialized_options = b'\xe0A\x02'
    _globals['_TEXTSTREAM'].fields_by_name['codec']._loaded_options = None
    _globals['_TEXTSTREAM'].fields_by_name['codec']._serialized_options = b'\xe0A\x02'
    _globals['_ELEMENTARYSTREAM']._serialized_start = 178
    _globals['_ELEMENTARYSTREAM']._serialized_end = 441
    _globals['_MUXSTREAM']._serialized_start = 444
    _globals['_MUXSTREAM']._serialized_end = 615
    _globals['_MANIFEST']._serialized_start = 618
    _globals['_MANIFEST']._serialized_end = 952
    _globals['_MANIFEST_MANIFESTTYPE']._serialized_start = 888
    _globals['_MANIFEST_MANIFESTTYPE']._serialized_end = 952
    _globals['_SPRITESHEET']._serialized_start = 955
    _globals['_SPRITESHEET']._serialized_end = 1182
    _globals['_PREPROCESSINGCONFIG']._serialized_start = 1185
    _globals['_PREPROCESSINGCONFIG']._serialized_end = 1638
    _globals['_PREPROCESSINGCONFIG_AUDIO']._serialized_start = 1430
    _globals['_PREPROCESSINGCONFIG_AUDIO']._serialized_end = 1451
    _globals['_PREPROCESSINGCONFIG_CROP']._serialized_start = 1453
    _globals['_PREPROCESSINGCONFIG_CROP']._serialized_end = 1545
    _globals['_PREPROCESSINGCONFIG_PAD']._serialized_start = 1547
    _globals['_PREPROCESSINGCONFIG_PAD']._serialized_end = 1638
    _globals['_VIDEOSTREAM']._serialized_start = 1641
    _globals['_VIDEOSTREAM']._serialized_end = 2152
    _globals['_VIDEOSTREAM_H264CODECSETTINGS']._serialized_start = 1738
    _globals['_VIDEOSTREAM_H264CODECSETTINGS']._serialized_end = 2134
    _globals['_AUDIOSTREAM']._serialized_start = 2155
    _globals['_AUDIOSTREAM']._serialized_end = 2519
    _globals['_AUDIOSTREAM_AUDIOMAPPING']._serialized_start = 2381
    _globals['_AUDIOSTREAM_AUDIOMAPPING']._serialized_end = 2519
    _globals['_TEXTSTREAM']._serialized_start = 2521
    _globals['_TEXTSTREAM']._serialized_end = 2553
    _globals['_SEGMENTSETTINGS']._serialized_start = 2555
    _globals['_SEGMENTSETTINGS']._serialized_end = 2625
    _globals['_TIMECODECONFIG']._serialized_start = 2628
    _globals['_TIMECODECONFIG']._serialized_end = 2928
    _globals['_TIMECODECONFIG_TIMECODESOURCE']._serialized_start = 2820
    _globals['_TIMECODECONFIG_TIMECODESOURCE']._serialized_end = 2913