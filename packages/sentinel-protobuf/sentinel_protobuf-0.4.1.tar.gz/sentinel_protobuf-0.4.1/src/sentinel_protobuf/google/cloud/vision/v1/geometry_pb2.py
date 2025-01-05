"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/vision/v1/geometry.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/cloud/vision/v1/geometry.proto\x12\x16google.cloud.vision.v1"\x1e\n\x06Vertex\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05"(\n\x10NormalizedVertex\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02"\x87\x01\n\x0cBoundingPoly\x120\n\x08vertices\x18\x01 \x03(\x0b2\x1e.google.cloud.vision.v1.Vertex\x12E\n\x13normalized_vertices\x18\x02 \x03(\x0b2(.google.cloud.vision.v1.NormalizedVertex"+\n\x08Position\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02Bn\n\x1acom.google.cloud.vision.v1B\rGeometryProtoP\x01Z5cloud.google.com/go/vision/v2/apiv1/visionpb;visionpb\xf8\x01\x01\xa2\x02\x04GCVNb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.vision.v1.geometry_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.vision.v1B\rGeometryProtoP\x01Z5cloud.google.com/go/vision/v2/apiv1/visionpb;visionpb\xf8\x01\x01\xa2\x02\x04GCVN'
    _globals['_VERTEX']._serialized_start = 65
    _globals['_VERTEX']._serialized_end = 95
    _globals['_NORMALIZEDVERTEX']._serialized_start = 97
    _globals['_NORMALIZEDVERTEX']._serialized_end = 137
    _globals['_BOUNDINGPOLY']._serialized_start = 140
    _globals['_BOUNDINGPOLY']._serialized_end = 275
    _globals['_POSITION']._serialized_start = 277
    _globals['_POSITION']._serialized_end = 320