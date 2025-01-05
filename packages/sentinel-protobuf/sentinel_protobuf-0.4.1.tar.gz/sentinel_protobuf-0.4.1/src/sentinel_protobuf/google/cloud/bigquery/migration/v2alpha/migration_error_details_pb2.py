"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/migration/v2alpha/migration_error_details.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.rpc import error_details_pb2 as google_dot_rpc_dot_error__details__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/cloud/bigquery/migration/v2alpha/migration_error_details.proto\x12\'google.cloud.bigquery.migration.v2alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1egoogle/rpc/error_details.proto"\xb7\x01\n\x13ResourceErrorDetail\x124\n\rresource_info\x18\x01 \x01(\x0b2\x18.google.rpc.ResourceInfoB\x03\xe0A\x02\x12P\n\rerror_details\x18\x02 \x03(\x0b24.google.cloud.bigquery.migration.v2alpha.ErrorDetailB\x03\xe0A\x02\x12\x18\n\x0berror_count\x18\x03 \x01(\x05B\x03\xe0A\x02"\x8c\x01\n\x0bErrorDetail\x12M\n\x08location\x18\x01 \x01(\x0b26.google.cloud.bigquery.migration.v2alpha.ErrorLocationB\x03\xe0A\x01\x12.\n\nerror_info\x18\x02 \x01(\x0b2\x15.google.rpc.ErrorInfoB\x03\xe0A\x02"7\n\rErrorLocation\x12\x11\n\x04line\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x13\n\x06column\x18\x02 \x01(\x05B\x03\xe0A\x01B\xea\x01\n+com.google.cloud.bigquery.migration.v2alphaB\x1aMigrationErrorDetailsProtoP\x01ZIcloud.google.com/go/bigquery/migration/apiv2alpha/migrationpb;migrationpb\xaa\x02\'Google.Cloud.BigQuery.Migration.V2Alpha\xca\x02\'Google\\Cloud\\BigQuery\\Migration\\V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.migration.v2alpha.migration_error_details_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.cloud.bigquery.migration.v2alphaB\x1aMigrationErrorDetailsProtoP\x01ZIcloud.google.com/go/bigquery/migration/apiv2alpha/migrationpb;migrationpb\xaa\x02'Google.Cloud.BigQuery.Migration.V2Alpha\xca\x02'Google\\Cloud\\BigQuery\\Migration\\V2alpha"
    _globals['_RESOURCEERRORDETAIL'].fields_by_name['resource_info']._loaded_options = None
    _globals['_RESOURCEERRORDETAIL'].fields_by_name['resource_info']._serialized_options = b'\xe0A\x02'
    _globals['_RESOURCEERRORDETAIL'].fields_by_name['error_details']._loaded_options = None
    _globals['_RESOURCEERRORDETAIL'].fields_by_name['error_details']._serialized_options = b'\xe0A\x02'
    _globals['_RESOURCEERRORDETAIL'].fields_by_name['error_count']._loaded_options = None
    _globals['_RESOURCEERRORDETAIL'].fields_by_name['error_count']._serialized_options = b'\xe0A\x02'
    _globals['_ERRORDETAIL'].fields_by_name['location']._loaded_options = None
    _globals['_ERRORDETAIL'].fields_by_name['location']._serialized_options = b'\xe0A\x01'
    _globals['_ERRORDETAIL'].fields_by_name['error_info']._loaded_options = None
    _globals['_ERRORDETAIL'].fields_by_name['error_info']._serialized_options = b'\xe0A\x02'
    _globals['_ERRORLOCATION'].fields_by_name['line']._loaded_options = None
    _globals['_ERRORLOCATION'].fields_by_name['line']._serialized_options = b'\xe0A\x01'
    _globals['_ERRORLOCATION'].fields_by_name['column']._loaded_options = None
    _globals['_ERRORLOCATION'].fields_by_name['column']._serialized_options = b'\xe0A\x01'
    _globals['_RESOURCEERRORDETAIL']._serialized_start = 180
    _globals['_RESOURCEERRORDETAIL']._serialized_end = 363
    _globals['_ERRORDETAIL']._serialized_start = 366
    _globals['_ERRORDETAIL']._serialized_end = 506
    _globals['_ERRORLOCATION']._serialized_start = 508
    _globals['_ERRORLOCATION']._serialized_end = 563