"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/vision/v1p3beta1/geometry.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/vision/v1p3beta1/geometry.proto\x12\x1dgoogle.cloud.vision.v1p3beta1"\x1e\n\x06Vertex\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05"(\n\x10NormalizedVertex\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02"\x95\x01\n\x0cBoundingPoly\x127\n\x08vertices\x18\x01 \x03(\x0b2%.google.cloud.vision.v1p3beta1.Vertex\x12L\n\x13normalized_vertices\x18\x02 \x03(\x0b2/.google.cloud.vision.v1p3beta1.NormalizedVertex"+\n\x08Position\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02By\n!com.google.cloud.vision.v1p3beta1B\rGeometryProtoP\x01Z9cloud.google.com/go/vision/apiv1p3beta1/visionpb;visionpb\xf8\x01\x01\xa2\x02\x04GCVNb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.vision.v1p3beta1.geometry_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.vision.v1p3beta1B\rGeometryProtoP\x01Z9cloud.google.com/go/vision/apiv1p3beta1/visionpb;visionpb\xf8\x01\x01\xa2\x02\x04GCVN'
    _globals['_VERTEX']._serialized_start = 79
    _globals['_VERTEX']._serialized_end = 109
    _globals['_NORMALIZEDVERTEX']._serialized_start = 111
    _globals['_NORMALIZEDVERTEX']._serialized_end = 151
    _globals['_BOUNDINGPOLY']._serialized_start = 154
    _globals['_BOUNDINGPOLY']._serialized_end = 303
    _globals['_POSITION']._serialized_start = 305
    _globals['_POSITION']._serialized_end = 348