"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/bigquery_export.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/securitycenter/v1/bigquery_export.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xde\x03\n\x0eBigQueryExport\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x0e\n\x06filter\x18\x03 \x01(\t\x12\x0f\n\x07dataset\x18\x04 \x01(\t\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1f\n\x12most_recent_editor\x18\x07 \x01(\tB\x03\xe0A\x03\x12\x16\n\tprincipal\x18\x08 \x01(\tB\x03\xe0A\x03:\xe2\x01\xeaA\xde\x01\n,securitycenter.googleapis.com/BigQueryExport\x125organizations/{organization}/bigQueryExports/{export}\x12)folders/{folder}/bigQueryExports/{export}\x12+projects/{project}/bigQueryExports/{export}*\x0fbigQueryExports2\x0ebigQueryExportB\xed\x01\n"com.google.cloud.securitycenter.v1B\x13BigQueryExportProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.bigquery_export_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1B\x13BigQueryExportProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_BIGQUERYEXPORT'].fields_by_name['create_time']._loaded_options = None
    _globals['_BIGQUERYEXPORT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_BIGQUERYEXPORT'].fields_by_name['update_time']._loaded_options = None
    _globals['_BIGQUERYEXPORT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_BIGQUERYEXPORT'].fields_by_name['most_recent_editor']._loaded_options = None
    _globals['_BIGQUERYEXPORT'].fields_by_name['most_recent_editor']._serialized_options = b'\xe0A\x03'
    _globals['_BIGQUERYEXPORT'].fields_by_name['principal']._loaded_options = None
    _globals['_BIGQUERYEXPORT'].fields_by_name['principal']._serialized_options = b'\xe0A\x03'
    _globals['_BIGQUERYEXPORT']._loaded_options = None
    _globals['_BIGQUERYEXPORT']._serialized_options = b'\xeaA\xde\x01\n,securitycenter.googleapis.com/BigQueryExport\x125organizations/{organization}/bigQueryExports/{export}\x12)folders/{folder}/bigQueryExports/{export}\x12+projects/{project}/bigQueryExports/{export}*\x0fbigQueryExports2\x0ebigQueryExport'
    _globals['_BIGQUERYEXPORT']._serialized_start = 182
    _globals['_BIGQUERYEXPORT']._serialized_end = 660