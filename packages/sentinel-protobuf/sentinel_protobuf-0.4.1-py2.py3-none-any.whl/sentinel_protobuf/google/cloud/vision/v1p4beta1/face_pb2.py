"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/vision/v1p4beta1/face.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.vision.v1p4beta1 import geometry_pb2 as google_dot_cloud_dot_vision_dot_v1p4beta1_dot_geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/vision/v1p4beta1/face.proto\x12\x1dgoogle.cloud.vision.v1p4beta1\x1a,google/cloud/vision/v1p4beta1/geometry.proto".\n\x15FaceRecognitionParams\x12\x15\n\rcelebrity_set\x18\x01 \x03(\t"D\n\tCelebrity\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t"h\n\x15FaceRecognitionResult\x12;\n\tcelebrity\x18\x01 \x01(\x0b2(.google.cloud.vision.v1p4beta1.Celebrity\x12\x12\n\nconfidence\x18\x02 \x01(\x02Bz\n!com.google.cloud.vision.v1p4beta1B\x0eCelebrityProtoP\x01Z9cloud.google.com/go/vision/apiv1p4beta1/visionpb;visionpb\xf8\x01\x01\xa2\x02\x04GCVNb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.vision.v1p4beta1.face_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.vision.v1p4beta1B\x0eCelebrityProtoP\x01Z9cloud.google.com/go/vision/apiv1p4beta1/visionpb;visionpb\xf8\x01\x01\xa2\x02\x04GCVN'
    _globals['_FACERECOGNITIONPARAMS']._serialized_start = 121
    _globals['_FACERECOGNITIONPARAMS']._serialized_end = 167
    _globals['_CELEBRITY']._serialized_start = 169
    _globals['_CELEBRITY']._serialized_end = 237
    _globals['_FACERECOGNITIONRESULT']._serialized_start = 239
    _globals['_FACERECOGNITIONRESULT']._serialized_end = 343