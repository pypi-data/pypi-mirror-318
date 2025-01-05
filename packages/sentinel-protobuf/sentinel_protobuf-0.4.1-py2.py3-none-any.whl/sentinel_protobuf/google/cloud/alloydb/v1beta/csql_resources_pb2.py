"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/alloydb/v1beta/csql_resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/alloydb/v1beta/csql_resources.proto\x12\x1bgoogle.cloud.alloydb.v1beta\x1a\x1fgoogle/api/field_behavior.proto"`\n\x17CloudSQLBackupRunSource\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x18\n\x0binstance_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rbackup_run_id\x18\x03 \x01(\x03B\x03\xe0A\x02B\xcf\x01\n\x1fcom.google.cloud.alloydb.v1betaB\x12CsqlResourcesProtoP\x01Z9cloud.google.com/go/alloydb/apiv1beta/alloydbpb;alloydbpb\xaa\x02\x1bGoogle.Cloud.AlloyDb.V1Beta\xca\x02\x1bGoogle\\Cloud\\AlloyDb\\V1beta\xea\x02\x1eGoogle::Cloud::AlloyDB::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.alloydb.v1beta.csql_resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.alloydb.v1betaB\x12CsqlResourcesProtoP\x01Z9cloud.google.com/go/alloydb/apiv1beta/alloydbpb;alloydbpb\xaa\x02\x1bGoogle.Cloud.AlloyDb.V1Beta\xca\x02\x1bGoogle\\Cloud\\AlloyDb\\V1beta\xea\x02\x1eGoogle::Cloud::AlloyDB::V1beta'
    _globals['_CLOUDSQLBACKUPRUNSOURCE'].fields_by_name['instance_id']._loaded_options = None
    _globals['_CLOUDSQLBACKUPRUNSOURCE'].fields_by_name['instance_id']._serialized_options = b'\xe0A\x02'
    _globals['_CLOUDSQLBACKUPRUNSOURCE'].fields_by_name['backup_run_id']._loaded_options = None
    _globals['_CLOUDSQLBACKUPRUNSOURCE'].fields_by_name['backup_run_id']._serialized_options = b'\xe0A\x02'
    _globals['_CLOUDSQLBACKUPRUNSOURCE']._serialized_start = 114
    _globals['_CLOUDSQLBACKUPRUNSOURCE']._serialized_end = 210