"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/video/stitcher/v1/stitch_details.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/video/stitcher/v1/stitch_details.proto\x12\x1egoogle.cloud.video.stitcher.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto"\x87\x02\n\x0fVodStitchDetail\x12\x0c\n\x04name\x18\x01 \x01(\t\x12I\n\x11ad_stitch_details\x18\x03 \x03(\x0b2..google.cloud.video.stitcher.v1.AdStitchDetail:\x9a\x01\xeaA\x96\x01\n,videostitcher.googleapis.com/VodStitchDetail\x12fprojects/{project}/locations/{location}/vodSessions/{vod_session}/vodStitchDetails/{vod_stitch_detail}"\xa5\x02\n\x0eAdStitchDetail\x12\x18\n\x0bad_break_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05ad_id\x18\x02 \x01(\tB\x03\xe0A\x02\x126\n\x0ead_time_offset\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x02\x12\x18\n\x0bskip_reason\x18\x04 \x01(\tB\x03\xe0A\x01\x12M\n\x05media\x18\x05 \x03(\x0b29.google.cloud.video.stitcher.v1.AdStitchDetail.MediaEntryB\x03\xe0A\x01\x1aD\n\nMediaEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value:\x028\x01Bz\n"com.google.cloud.video.stitcher.v1B\x12StitchDetailsProtoP\x01Z>cloud.google.com/go/video/stitcher/apiv1/stitcherpb;stitcherpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.video.stitcher.v1.stitch_details_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.video.stitcher.v1B\x12StitchDetailsProtoP\x01Z>cloud.google.com/go/video/stitcher/apiv1/stitcherpb;stitcherpb'
    _globals['_VODSTITCHDETAIL']._loaded_options = None
    _globals['_VODSTITCHDETAIL']._serialized_options = b'\xeaA\x96\x01\n,videostitcher.googleapis.com/VodStitchDetail\x12fprojects/{project}/locations/{location}/vodSessions/{vod_session}/vodStitchDetails/{vod_stitch_detail}'
    _globals['_ADSTITCHDETAIL_MEDIAENTRY']._loaded_options = None
    _globals['_ADSTITCHDETAIL_MEDIAENTRY']._serialized_options = b'8\x01'
    _globals['_ADSTITCHDETAIL'].fields_by_name['ad_break_id']._loaded_options = None
    _globals['_ADSTITCHDETAIL'].fields_by_name['ad_break_id']._serialized_options = b'\xe0A\x02'
    _globals['_ADSTITCHDETAIL'].fields_by_name['ad_id']._loaded_options = None
    _globals['_ADSTITCHDETAIL'].fields_by_name['ad_id']._serialized_options = b'\xe0A\x02'
    _globals['_ADSTITCHDETAIL'].fields_by_name['ad_time_offset']._loaded_options = None
    _globals['_ADSTITCHDETAIL'].fields_by_name['ad_time_offset']._serialized_options = b'\xe0A\x02'
    _globals['_ADSTITCHDETAIL'].fields_by_name['skip_reason']._loaded_options = None
    _globals['_ADSTITCHDETAIL'].fields_by_name['skip_reason']._serialized_options = b'\xe0A\x01'
    _globals['_ADSTITCHDETAIL'].fields_by_name['media']._loaded_options = None
    _globals['_ADSTITCHDETAIL'].fields_by_name['media']._serialized_options = b'\xe0A\x01'
    _globals['_VODSTITCHDETAIL']._serialized_start = 210
    _globals['_VODSTITCHDETAIL']._serialized_end = 473
    _globals['_ADSTITCHDETAIL']._serialized_start = 476
    _globals['_ADSTITCHDETAIL']._serialized_end = 769
    _globals['_ADSTITCHDETAIL_MEDIAENTRY']._serialized_start = 701
    _globals['_ADSTITCHDETAIL_MEDIAENTRY']._serialized_end = 769