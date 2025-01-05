"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/alloydb/v1alpha/csql_resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/alloydb/v1alpha/csql_resources.proto\x12\x1cgoogle.cloud.alloydb.v1alpha\x1a\x1fgoogle/api/field_behavior.proto"`\n\x17CloudSQLBackupRunSource\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x18\n\x0binstance_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rbackup_run_id\x18\x03 \x01(\x03B\x03\xe0A\x02B\xd4\x01\n com.google.cloud.alloydb.v1alphaB\x12CsqlResourcesProtoP\x01Z:cloud.google.com/go/alloydb/apiv1alpha/alloydbpb;alloydbpb\xaa\x02\x1cGoogle.Cloud.AlloyDb.V1Alpha\xca\x02\x1cGoogle\\Cloud\\AlloyDb\\V1alpha\xea\x02\x1fGoogle::Cloud::AlloyDB::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.alloydb.v1alpha.csql_resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.alloydb.v1alphaB\x12CsqlResourcesProtoP\x01Z:cloud.google.com/go/alloydb/apiv1alpha/alloydbpb;alloydbpb\xaa\x02\x1cGoogle.Cloud.AlloyDb.V1Alpha\xca\x02\x1cGoogle\\Cloud\\AlloyDb\\V1alpha\xea\x02\x1fGoogle::Cloud::AlloyDB::V1alpha'
    _globals['_CLOUDSQLBACKUPRUNSOURCE'].fields_by_name['instance_id']._loaded_options = None
    _globals['_CLOUDSQLBACKUPRUNSOURCE'].fields_by_name['instance_id']._serialized_options = b'\xe0A\x02'
    _globals['_CLOUDSQLBACKUPRUNSOURCE'].fields_by_name['backup_run_id']._loaded_options = None
    _globals['_CLOUDSQLBACKUPRUNSOURCE'].fields_by_name['backup_run_id']._serialized_options = b'\xe0A\x02'
    _globals['_CLOUDSQLBACKUPRUNSOURCE']._serialized_start = 116
    _globals['_CLOUDSQLBACKUPRUNSOURCE']._serialized_end = 212