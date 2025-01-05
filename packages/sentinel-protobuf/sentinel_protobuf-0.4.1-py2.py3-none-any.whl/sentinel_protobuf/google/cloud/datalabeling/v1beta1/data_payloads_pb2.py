"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datalabeling/v1beta1/data_payloads.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/datalabeling/v1beta1/data_payloads.proto\x12!google.cloud.datalabeling.v1beta1\x1a\x1egoogle/protobuf/duration.proto"a\n\x0cImagePayload\x12\x11\n\tmime_type\x18\x01 \x01(\t\x12\x17\n\x0fimage_thumbnail\x18\x02 \x01(\x0c\x12\x11\n\timage_uri\x18\x03 \x01(\t\x12\x12\n\nsigned_uri\x18\x04 \x01(\t"#\n\x0bTextPayload\x12\x14\n\x0ctext_content\x18\x01 \x01(\t"S\n\x0eVideoThumbnail\x12\x11\n\tthumbnail\x18\x01 \x01(\x0c\x12.\n\x0btime_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"\xa9\x01\n\x0cVideoPayload\x12\x11\n\tmime_type\x18\x01 \x01(\t\x12\x11\n\tvideo_uri\x18\x02 \x01(\t\x12K\n\x10video_thumbnails\x18\x03 \x03(\x0b21.google.cloud.datalabeling.v1beta1.VideoThumbnail\x12\x12\n\nframe_rate\x18\x04 \x01(\x02\x12\x12\n\nsigned_uri\x18\x05 \x01(\tB\xe3\x01\n%com.google.cloud.datalabeling.v1beta1P\x01ZIcloud.google.com/go/datalabeling/apiv1beta1/datalabelingpb;datalabelingpb\xaa\x02!Google.Cloud.DataLabeling.V1Beta1\xca\x02!Google\\Cloud\\DataLabeling\\V1beta1\xea\x02$Google::Cloud::DataLabeling::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datalabeling.v1beta1.data_payloads_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.datalabeling.v1beta1P\x01ZIcloud.google.com/go/datalabeling/apiv1beta1/datalabelingpb;datalabelingpb\xaa\x02!Google.Cloud.DataLabeling.V1Beta1\xca\x02!Google\\Cloud\\DataLabeling\\V1beta1\xea\x02$Google::Cloud::DataLabeling::V1beta1'
    _globals['_IMAGEPAYLOAD']._serialized_start = 124
    _globals['_IMAGEPAYLOAD']._serialized_end = 221
    _globals['_TEXTPAYLOAD']._serialized_start = 223
    _globals['_TEXTPAYLOAD']._serialized_end = 258
    _globals['_VIDEOTHUMBNAIL']._serialized_start = 260
    _globals['_VIDEOTHUMBNAIL']._serialized_end = 343
    _globals['_VIDEOPAYLOAD']._serialized_start = 346
    _globals['_VIDEOPAYLOAD']._serialized_end = 515