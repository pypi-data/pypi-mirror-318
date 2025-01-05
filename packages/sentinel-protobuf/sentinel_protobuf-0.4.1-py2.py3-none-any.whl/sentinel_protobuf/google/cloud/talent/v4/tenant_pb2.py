"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/talent/v4/tenant.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/cloud/talent/v4/tenant.proto\x12\x16google.cloud.talent.v4\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"v\n\x06Tenant\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x0bexternal_id\x18\x02 \x01(\tB\x03\xe0A\x02:D\xeaAA\n\x1ajobs.googleapis.com/Tenant\x12#projects/{project}/tenants/{tenant}Be\n\x1acom.google.cloud.talent.v4B\x0bTenantProtoP\x01Z2cloud.google.com/go/talent/apiv4/talentpb;talentpb\xa2\x02\x03CTSb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.talent.v4.tenant_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.talent.v4B\x0bTenantProtoP\x01Z2cloud.google.com/go/talent/apiv4/talentpb;talentpb\xa2\x02\x03CTS'
    _globals['_TENANT'].fields_by_name['external_id']._loaded_options = None
    _globals['_TENANT'].fields_by_name['external_id']._serialized_options = b'\xe0A\x02'
    _globals['_TENANT']._loaded_options = None
    _globals['_TENANT']._serialized_options = b'\xeaAA\n\x1ajobs.googleapis.com/Tenant\x12#projects/{project}/tenants/{tenant}'
    _globals['_TENANT']._serialized_start = 123
    _globals['_TENANT']._serialized_end = 241