"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/iam/admin/v1/audit_data.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/iam/admin/v1/audit_data.proto\x12\x13google.iam.admin.v1"\xa0\x01\n\tAuditData\x12H\n\x10permission_delta\x18\x01 \x01(\x0b2..google.iam.admin.v1.AuditData.PermissionDelta\x1aI\n\x0fPermissionDelta\x12\x19\n\x11added_permissions\x18\x01 \x03(\t\x12\x1b\n\x13removed_permissions\x18\x02 \x03(\tB\x98\x01\n\x17com.google.iam.admin.v1B\x0eAuditDataProtoP\x01Z3cloud.google.com/go/iam/admin/apiv1/adminpb;adminpb\xaa\x02\x19Google.Cloud.Iam.Admin.V1\xca\x02\x19Google\\Cloud\\Iam\\Admin\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.iam.admin.v1.audit_data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.iam.admin.v1B\x0eAuditDataProtoP\x01Z3cloud.google.com/go/iam/admin/apiv1/adminpb;adminpb\xaa\x02\x19Google.Cloud.Iam.Admin.V1\xca\x02\x19Google\\Cloud\\Iam\\Admin\\V1'
    _globals['_AUDITDATA']._serialized_start = 62
    _globals['_AUDITDATA']._serialized_end = 222
    _globals['_AUDITDATA_PERMISSIONDELTA']._serialized_start = 149
    _globals['_AUDITDATA_PERMISSIONDELTA']._serialized_end = 222