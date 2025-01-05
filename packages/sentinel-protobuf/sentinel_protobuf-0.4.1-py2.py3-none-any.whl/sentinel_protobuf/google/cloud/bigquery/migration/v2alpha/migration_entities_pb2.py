"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/migration/v2alpha/migration_entities.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.bigquery.migration.v2alpha import assessment_task_pb2 as google_dot_cloud_dot_bigquery_dot_migration_dot_v2alpha_dot_assessment__task__pb2
from ......google.cloud.bigquery.migration.v2alpha import migration_error_details_pb2 as google_dot_cloud_dot_bigquery_dot_migration_dot_v2alpha_dot_migration__error__details__pb2
from ......google.cloud.bigquery.migration.v2alpha import migration_metrics_pb2 as google_dot_cloud_dot_bigquery_dot_migration_dot_v2alpha_dot_migration__metrics__pb2
from ......google.cloud.bigquery.migration.v2alpha import translation_task_pb2 as google_dot_cloud_dot_bigquery_dot_migration_dot_v2alpha_dot_translation__task__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.rpc import error_details_pb2 as google_dot_rpc_dot_error__details__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/cloud/bigquery/migration/v2alpha/migration_entities.proto\x12\'google.cloud.bigquery.migration.v2alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a=google/cloud/bigquery/migration/v2alpha/assessment_task.proto\x1aEgoogle/cloud/bigquery/migration/v2alpha/migration_error_details.proto\x1a?google/cloud/bigquery/migration/v2alpha/migration_metrics.proto\x1a>google/cloud/bigquery/migration/v2alpha/translation_task.proto\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/rpc/error_details.proto"\x82\x05\n\x11MigrationWorkflow\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x05\x12\x14\n\x0cdisplay_name\x18\x06 \x01(\t\x12T\n\x05tasks\x18\x02 \x03(\x0b2E.google.cloud.bigquery.migration.v2alpha.MigrationWorkflow.TasksEntry\x12T\n\x05state\x18\x03 \x01(\x0e2@.google.cloud.bigquery.migration.v2alpha.MigrationWorkflow.StateB\x03\xe0A\x03\x12/\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x10last_update_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1ad\n\nTasksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12E\n\x05value\x18\x02 \x01(\x0b26.google.cloud.bigquery.migration.v2alpha.MigrationTask:\x028\x01"Q\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\t\n\x05DRAFT\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\n\n\x06PAUSED\x10\x03\x12\r\n\tCOMPLETED\x10\x04:u\xeaAr\n2bigquerymigration.googleapis.com/MigrationWorkflow\x12<projects/{project}/locations/{location}/workflows/{workflow}"\x81\x06\n\rMigrationTask\x12a\n\x17assessment_task_details\x18\x0c \x01(\x0b2>.google.cloud.bigquery.migration.v2alpha.AssessmentTaskDetailsH\x00\x12c\n\x18translation_task_details\x18\r \x01(\x0b2?.google.cloud.bigquery.migration.v2alpha.TranslationTaskDetailsH\x00\x12\x12\n\x02id\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x05\x12\x0c\n\x04type\x18\x02 \x01(\t\x12%\n\x07details\x18\x03 \x01(\x0b2\x14.google.protobuf.Any\x12P\n\x05state\x18\x04 \x01(\x0e2<.google.cloud.bigquery.migration.v2alpha.MigrationTask.StateB\x03\xe0A\x03\x124\n\x10processing_error\x18\x05 \x01(\x0b2\x15.google.rpc.ErrorInfoB\x03\xe0A\x03\x12/\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x10last_update_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12l\n\x14orchestration_result\x18\n \x01(\x0b2I.google.cloud.bigquery.migration.v2alpha.MigrationTaskOrchestrationResultB\x03\xe0A\x03"r\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x11\n\rORCHESTRATING\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\n\n\x06PAUSED\x10\x04\x12\r\n\tSUCCEEDED\x10\x05\x12\n\n\x06FAILED\x10\x06B\x0e\n\x0ctask_details"\xeb\x05\n\x10MigrationSubtask\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x05\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12S\n\x05state\x18\x05 \x01(\x0e2?.google.cloud.bigquery.migration.v2alpha.MigrationSubtask.StateB\x03\xe0A\x03\x124\n\x10processing_error\x18\x06 \x01(\x0b2\x15.google.rpc.ErrorInfoB\x03\xe0A\x03\x12a\n\x16resource_error_details\x18\x0c \x03(\x0b2<.google.cloud.bigquery.migration.v2alpha.ResourceErrorDetailB\x03\xe0A\x03\x12\x1c\n\x14resource_error_count\x18\r \x01(\x05\x12/\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x10last_update_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12D\n\x07metrics\x18\x0b \x03(\x0b23.google.cloud.bigquery.migration.v2alpha.TimeSeries"^\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\n\n\x06PAUSED\x10\x05:\x88\x01\xeaA\x84\x01\n1bigquerymigration.googleapis.com/MigrationSubtask\x12Oprojects/{project}/locations/{location}/workflows/{workflow}/subtasks/{subtask}"\x9a\x01\n MigrationTaskOrchestrationResult\x12k\n\x12assessment_details\x18\x01 \x01(\x0b2M.google.cloud.bigquery.migration.v2alpha.AssessmentOrchestrationResultDetailsH\x00B\t\n\x07detailsB\xe6\x01\n+com.google.cloud.bigquery.migration.v2alphaB\x16MigrationEntitiesProtoP\x01ZIcloud.google.com/go/bigquery/migration/apiv2alpha/migrationpb;migrationpb\xaa\x02\'Google.Cloud.BigQuery.Migration.V2Alpha\xca\x02\'Google\\Cloud\\BigQuery\\Migration\\V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.migration.v2alpha.migration_entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.cloud.bigquery.migration.v2alphaB\x16MigrationEntitiesProtoP\x01ZIcloud.google.com/go/bigquery/migration/apiv2alpha/migrationpb;migrationpb\xaa\x02'Google.Cloud.BigQuery.Migration.V2Alpha\xca\x02'Google\\Cloud\\BigQuery\\Migration\\V2alpha"
    _globals['_MIGRATIONWORKFLOW_TASKSENTRY']._loaded_options = None
    _globals['_MIGRATIONWORKFLOW_TASKSENTRY']._serialized_options = b'8\x01'
    _globals['_MIGRATIONWORKFLOW'].fields_by_name['name']._loaded_options = None
    _globals['_MIGRATIONWORKFLOW'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x05'
    _globals['_MIGRATIONWORKFLOW'].fields_by_name['state']._loaded_options = None
    _globals['_MIGRATIONWORKFLOW'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_MIGRATIONWORKFLOW']._loaded_options = None
    _globals['_MIGRATIONWORKFLOW']._serialized_options = b'\xeaAr\n2bigquerymigration.googleapis.com/MigrationWorkflow\x12<projects/{project}/locations/{location}/workflows/{workflow}'
    _globals['_MIGRATIONTASK'].fields_by_name['id']._loaded_options = None
    _globals['_MIGRATIONTASK'].fields_by_name['id']._serialized_options = b'\xe0A\x03\xe0A\x05'
    _globals['_MIGRATIONTASK'].fields_by_name['state']._loaded_options = None
    _globals['_MIGRATIONTASK'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_MIGRATIONTASK'].fields_by_name['processing_error']._loaded_options = None
    _globals['_MIGRATIONTASK'].fields_by_name['processing_error']._serialized_options = b'\xe0A\x03'
    _globals['_MIGRATIONTASK'].fields_by_name['orchestration_result']._loaded_options = None
    _globals['_MIGRATIONTASK'].fields_by_name['orchestration_result']._serialized_options = b'\xe0A\x03'
    _globals['_MIGRATIONSUBTASK'].fields_by_name['name']._loaded_options = None
    _globals['_MIGRATIONSUBTASK'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x05'
    _globals['_MIGRATIONSUBTASK'].fields_by_name['state']._loaded_options = None
    _globals['_MIGRATIONSUBTASK'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_MIGRATIONSUBTASK'].fields_by_name['processing_error']._loaded_options = None
    _globals['_MIGRATIONSUBTASK'].fields_by_name['processing_error']._serialized_options = b'\xe0A\x03'
    _globals['_MIGRATIONSUBTASK'].fields_by_name['resource_error_details']._loaded_options = None
    _globals['_MIGRATIONSUBTASK'].fields_by_name['resource_error_details']._serialized_options = b'\xe0A\x03'
    _globals['_MIGRATIONSUBTASK']._loaded_options = None
    _globals['_MIGRATIONSUBTASK']._serialized_options = b'\xeaA\x84\x01\n1bigquerymigration.googleapis.com/MigrationSubtask\x12Oprojects/{project}/locations/{location}/workflows/{workflow}/subtasks/{subtask}'
    _globals['_MIGRATIONWORKFLOW']._serialized_start = 525
    _globals['_MIGRATIONWORKFLOW']._serialized_end = 1167
    _globals['_MIGRATIONWORKFLOW_TASKSENTRY']._serialized_start = 865
    _globals['_MIGRATIONWORKFLOW_TASKSENTRY']._serialized_end = 965
    _globals['_MIGRATIONWORKFLOW_STATE']._serialized_start = 967
    _globals['_MIGRATIONWORKFLOW_STATE']._serialized_end = 1048
    _globals['_MIGRATIONTASK']._serialized_start = 1170
    _globals['_MIGRATIONTASK']._serialized_end = 1939
    _globals['_MIGRATIONTASK_STATE']._serialized_start = 1809
    _globals['_MIGRATIONTASK_STATE']._serialized_end = 1923
    _globals['_MIGRATIONSUBTASK']._serialized_start = 1942
    _globals['_MIGRATIONSUBTASK']._serialized_end = 2689
    _globals['_MIGRATIONSUBTASK_STATE']._serialized_start = 2456
    _globals['_MIGRATIONSUBTASK_STATE']._serialized_end = 2550
    _globals['_MIGRATIONTASKORCHESTRATIONRESULT']._serialized_start = 2692
    _globals['_MIGRATIONTASKORCHESTRATIONRESULT']._serialized_end = 2846