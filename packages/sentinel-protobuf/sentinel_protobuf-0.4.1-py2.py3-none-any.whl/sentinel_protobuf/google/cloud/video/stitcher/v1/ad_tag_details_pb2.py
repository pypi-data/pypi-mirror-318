"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/video/stitcher/v1/ad_tag_details.proto')
_sym_db = _symbol_database.Default()
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/video/stitcher/v1/ad_tag_details.proto\x12\x1egoogle.cloud.video.stitcher.v1\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto"\xff\x01\n\x0fLiveAdTagDetail\x12\x0c\n\x04name\x18\x01 \x01(\t\x12>\n\x0bad_requests\x18\x02 \x03(\x0b2).google.cloud.video.stitcher.v1.AdRequest:\x9d\x01\xeaA\x99\x01\n,videostitcher.googleapis.com/LiveAdTagDetail\x12iprojects/{project}/locations/{location}/liveSessions/{live_session}/liveAdTagDetails/{live_ad_tag_detail}"\xf9\x01\n\x0eVodAdTagDetail\x12\x0c\n\x04name\x18\x01 \x01(\t\x12>\n\x0bad_requests\x18\x02 \x03(\x0b2).google.cloud.video.stitcher.v1.AdRequest:\x98\x01\xeaA\x94\x01\n+videostitcher.googleapis.com/VodAdTagDetail\x12eprojects/{project}/locations/{location}/vodSessions/{vod_session}/vodAdTagDetails/{vod_ad_tag_detail}"\xb0\x01\n\tAdRequest\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12I\n\x10request_metadata\x18\x02 \x01(\x0b2/.google.cloud.video.stitcher.v1.RequestMetadata\x12K\n\x11response_metadata\x18\x03 \x01(\x0b20.google.cloud.video.stitcher.v1.ResponseMetadata";\n\x0fRequestMetadata\x12(\n\x07headers\x18\x01 \x01(\x0b2\x17.google.protobuf.Struct"\xaf\x01\n\x10ResponseMetadata\x12\r\n\x05error\x18\x01 \x01(\t\x12(\n\x07headers\x18\x02 \x01(\x0b2\x17.google.protobuf.Struct\x12\x13\n\x0bstatus_code\x18\x03 \x01(\t\x12\x12\n\nsize_bytes\x18\x04 \x01(\x05\x12+\n\x08duration\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12\x0c\n\x04body\x18\x06 \x01(\tBy\n"com.google.cloud.video.stitcher.v1B\x11AdTagDetailsProtoP\x01Z>cloud.google.com/go/video/stitcher/apiv1/stitcherpb;stitcherpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.video.stitcher.v1.ad_tag_details_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.video.stitcher.v1B\x11AdTagDetailsProtoP\x01Z>cloud.google.com/go/video/stitcher/apiv1/stitcherpb;stitcherpb'
    _globals['_LIVEADTAGDETAIL']._loaded_options = None
    _globals['_LIVEADTAGDETAIL']._serialized_options = b'\xeaA\x99\x01\n,videostitcher.googleapis.com/LiveAdTagDetail\x12iprojects/{project}/locations/{location}/liveSessions/{live_session}/liveAdTagDetails/{live_ad_tag_detail}'
    _globals['_VODADTAGDETAIL']._loaded_options = None
    _globals['_VODADTAGDETAIL']._serialized_options = b'\xeaA\x94\x01\n+videostitcher.googleapis.com/VodAdTagDetail\x12eprojects/{project}/locations/{location}/vodSessions/{vod_session}/vodAdTagDetails/{vod_ad_tag_detail}'
    _globals['_LIVEADTAGDETAIL']._serialized_start = 177
    _globals['_LIVEADTAGDETAIL']._serialized_end = 432
    _globals['_VODADTAGDETAIL']._serialized_start = 435
    _globals['_VODADTAGDETAIL']._serialized_end = 684
    _globals['_ADREQUEST']._serialized_start = 687
    _globals['_ADREQUEST']._serialized_end = 863
    _globals['_REQUESTMETADATA']._serialized_start = 865
    _globals['_REQUESTMETADATA']._serialized_end = 924
    _globals['_RESPONSEMETADATA']._serialized_start = 927
    _globals['_RESPONSEMETADATA']._serialized_end = 1102