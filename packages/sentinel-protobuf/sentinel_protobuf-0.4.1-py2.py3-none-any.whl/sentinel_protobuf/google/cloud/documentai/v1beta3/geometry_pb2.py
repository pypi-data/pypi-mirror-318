"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/documentai/v1beta3/geometry.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/documentai/v1beta3/geometry.proto\x12\x1fgoogle.cloud.documentai.v1beta3"\x1e\n\x06Vertex\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05"(\n\x10NormalizedVertex\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02"\x99\x01\n\x0cBoundingPoly\x129\n\x08vertices\x18\x01 \x03(\x0b2\'.google.cloud.documentai.v1beta3.Vertex\x12N\n\x13normalized_vertices\x18\x02 \x03(\x0b21.google.cloud.documentai.v1beta3.NormalizedVertexB\xe4\x01\n#com.google.cloud.documentai.v1beta3B\rGeometryProtoP\x01ZCcloud.google.com/go/documentai/apiv1beta3/documentaipb;documentaipb\xaa\x02\x1fGoogle.Cloud.DocumentAI.V1Beta3\xca\x02\x1fGoogle\\Cloud\\DocumentAI\\V1beta3\xea\x02"Google::Cloud::DocumentAI::V1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.documentai.v1beta3.geometry_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.documentai.v1beta3B\rGeometryProtoP\x01ZCcloud.google.com/go/documentai/apiv1beta3/documentaipb;documentaipb\xaa\x02\x1fGoogle.Cloud.DocumentAI.V1Beta3\xca\x02\x1fGoogle\\Cloud\\DocumentAI\\V1beta3\xea\x02"Google::Cloud::DocumentAI::V1beta3'
    _globals['_VERTEX']._serialized_start = 83
    _globals['_VERTEX']._serialized_end = 113
    _globals['_NORMALIZEDVERTEX']._serialized_start = 115
    _globals['_NORMALIZEDVERTEX']._serialized_end = 155
    _globals['_BOUNDINGPOLY']._serialized_start = 158
    _globals['_BOUNDINGPOLY']._serialized_end = 311