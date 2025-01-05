"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/documentai/v1/geometry.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/documentai/v1/geometry.proto\x12\x1agoogle.cloud.documentai.v1"\x1e\n\x06Vertex\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05"(\n\x10NormalizedVertex\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02"\x8f\x01\n\x0cBoundingPoly\x124\n\x08vertices\x18\x01 \x03(\x0b2".google.cloud.documentai.v1.Vertex\x12I\n\x13normalized_vertices\x18\x02 \x03(\x0b2,.google.cloud.documentai.v1.NormalizedVertexB\xcb\x01\n\x1ecom.google.cloud.documentai.v1B\rGeometryProtoP\x01Z>cloud.google.com/go/documentai/apiv1/documentaipb;documentaipb\xaa\x02\x1aGoogle.Cloud.DocumentAI.V1\xca\x02\x1aGoogle\\Cloud\\DocumentAI\\V1\xea\x02\x1dGoogle::Cloud::DocumentAI::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.documentai.v1.geometry_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.documentai.v1B\rGeometryProtoP\x01Z>cloud.google.com/go/documentai/apiv1/documentaipb;documentaipb\xaa\x02\x1aGoogle.Cloud.DocumentAI.V1\xca\x02\x1aGoogle\\Cloud\\DocumentAI\\V1\xea\x02\x1dGoogle::Cloud::DocumentAI::V1'
    _globals['_VERTEX']._serialized_start = 73
    _globals['_VERTEX']._serialized_end = 103
    _globals['_NORMALIZEDVERTEX']._serialized_start = 105
    _globals['_NORMALIZEDVERTEX']._serialized_end = 145
    _globals['_BOUNDINGPOLY']._serialized_start = 148
    _globals['_BOUNDINGPOLY']._serialized_end = 291