"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/migration/v2alpha/assessment_task.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/bigquery/migration/v2alpha/assessment_task.proto\x12\'google.cloud.bigquery.migration.v2alpha\x1a\x1fgoogle/api/field_behavior.proto"\x84\x01\n\x15AssessmentTaskDetails\x12\x17\n\ninput_path\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x0eoutput_dataset\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x0equerylogs_path\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bdata_source\x18\x04 \x01(\tB\x03\xe0A\x02"Q\n$AssessmentOrchestrationResultDetails\x12)\n\x1coutput_tables_schema_version\x18\x01 \x01(\tB\x03\xe0A\x01B\xe3\x01\n+com.google.cloud.bigquery.migration.v2alphaB\x13AssessmentTaskProtoP\x01ZIcloud.google.com/go/bigquery/migration/apiv2alpha/migrationpb;migrationpb\xaa\x02\'Google.Cloud.BigQuery.Migration.V2Alpha\xca\x02\'Google\\Cloud\\BigQuery\\Migration\\V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.migration.v2alpha.assessment_task_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.cloud.bigquery.migration.v2alphaB\x13AssessmentTaskProtoP\x01ZIcloud.google.com/go/bigquery/migration/apiv2alpha/migrationpb;migrationpb\xaa\x02'Google.Cloud.BigQuery.Migration.V2Alpha\xca\x02'Google\\Cloud\\BigQuery\\Migration\\V2alpha"
    _globals['_ASSESSMENTTASKDETAILS'].fields_by_name['input_path']._loaded_options = None
    _globals['_ASSESSMENTTASKDETAILS'].fields_by_name['input_path']._serialized_options = b'\xe0A\x02'
    _globals['_ASSESSMENTTASKDETAILS'].fields_by_name['output_dataset']._loaded_options = None
    _globals['_ASSESSMENTTASKDETAILS'].fields_by_name['output_dataset']._serialized_options = b'\xe0A\x02'
    _globals['_ASSESSMENTTASKDETAILS'].fields_by_name['querylogs_path']._loaded_options = None
    _globals['_ASSESSMENTTASKDETAILS'].fields_by_name['querylogs_path']._serialized_options = b'\xe0A\x01'
    _globals['_ASSESSMENTTASKDETAILS'].fields_by_name['data_source']._loaded_options = None
    _globals['_ASSESSMENTTASKDETAILS'].fields_by_name['data_source']._serialized_options = b'\xe0A\x02'
    _globals['_ASSESSMENTORCHESTRATIONRESULTDETAILS'].fields_by_name['output_tables_schema_version']._loaded_options = None
    _globals['_ASSESSMENTORCHESTRATIONRESULTDETAILS'].fields_by_name['output_tables_schema_version']._serialized_options = b'\xe0A\x01'
    _globals['_ASSESSMENTTASKDETAILS']._serialized_start = 140
    _globals['_ASSESSMENTTASKDETAILS']._serialized_end = 272
    _globals['_ASSESSMENTORCHESTRATIONRESULTDETAILS']._serialized_start = 274
    _globals['_ASSESSMENTORCHESTRATIONRESULTDETAILS']._serialized_end = 355