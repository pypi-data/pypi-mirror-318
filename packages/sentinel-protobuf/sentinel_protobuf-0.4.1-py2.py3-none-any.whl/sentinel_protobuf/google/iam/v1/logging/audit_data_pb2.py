"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/iam/v1/logging/audit_data.proto')
_sym_db = _symbol_database.Default()
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/iam/v1/logging/audit_data.proto\x12\x15google.iam.v1.logging\x1a\x1agoogle/iam/v1/policy.proto"=\n\tAuditData\x120\n\x0cpolicy_delta\x18\x02 \x01(\x0b2\x1a.google.iam.v1.PolicyDeltaB\x86\x01\n\x19com.google.iam.v1.loggingB\x0eAuditDataProtoP\x01Z9cloud.google.com/go/iam/apiv1/logging/loggingpb;loggingpb\xaa\x02\x1bGoogle.Cloud.Iam.V1.Loggingb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.iam.v1.logging.audit_data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.iam.v1.loggingB\x0eAuditDataProtoP\x01Z9cloud.google.com/go/iam/apiv1/logging/loggingpb;loggingpb\xaa\x02\x1bGoogle.Cloud.Iam.V1.Logging'
    _globals['_AUDITDATA']._serialized_start = 93
    _globals['_AUDITDATA']._serialized_end = 154