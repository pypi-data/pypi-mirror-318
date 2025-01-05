"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/websecurityscanner/v1alpha/finding_type_stats.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.websecurityscanner.v1alpha import finding_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1alpha_dot_finding__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/cloud/websecurityscanner/v1alpha/finding_type_stats.proto\x12\'google.cloud.websecurityscanner.v1alpha\x1a5google/cloud/websecurityscanner/v1alpha/finding.proto"}\n\x10FindingTypeStats\x12R\n\x0cfinding_type\x18\x01 \x01(\x0e2<.google.cloud.websecurityscanner.v1alpha.Finding.FindingType\x12\x15\n\rfinding_count\x18\x02 \x01(\x05B\xa3\x01\n+com.google.cloud.websecurityscanner.v1alphaB\x15FindingTypeStatsProtoP\x01Z[cloud.google.com/go/websecurityscanner/apiv1alpha/websecurityscannerpb;websecurityscannerpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.websecurityscanner.v1alpha.finding_type_stats_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n+com.google.cloud.websecurityscanner.v1alphaB\x15FindingTypeStatsProtoP\x01Z[cloud.google.com/go/websecurityscanner/apiv1alpha/websecurityscannerpb;websecurityscannerpb'
    _globals['_FINDINGTYPESTATS']._serialized_start = 164
    _globals['_FINDINGTYPESTATS']._serialized_end = 289