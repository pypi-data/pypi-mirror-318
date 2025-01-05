"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/migration/v2/migration_entities.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.bigquery.migration.v2 import migration_error_details_pb2 as google_dot_cloud_dot_bigquery_dot_migration_dot_v2_dot_migration__error__details__pb2
from ......google.cloud.bigquery.migration.v2 import migration_metrics_pb2 as google_dot_cloud_dot_bigquery_dot_migration_dot_v2_dot_migration__metrics__pb2
from ......google.cloud.bigquery.migration.v2 import translation_config_pb2 as google_dot_cloud_dot_bigquery_dot_migration_dot_v2_dot_translation__config__pb2
from ......google.cloud.bigquery.migration.v2 import translation_details_pb2 as google_dot_cloud_dot_bigquery_dot_migration_dot_v2_dot_translation__details__pb2
from ......google.cloud.bigquery.migration.v2 import translation_usability_pb2 as google_dot_cloud_dot_bigquery_dot_migration_dot_v2_dot_translation__usability__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.rpc import error_details_pb2 as google_dot_rpc_dot_error__details__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/cloud/bigquery/migration/v2/migration_entities.proto\x12"google.cloud.bigquery.migration.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a@google/cloud/bigquery/migration/v2/migration_error_details.proto\x1a:google/cloud/bigquery/migration/v2/migration_metrics.proto\x1a;google/cloud/bigquery/migration/v2/translation_config.proto\x1a<google/cloud/bigquery/migration/v2/translation_details.proto\x1a>google/cloud/bigquery/migration/v2/translation_usability.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/rpc/error_details.proto"\xf6\x04\n\x11MigrationWorkflow\x12\x17\n\x04name\x18\x01 \x01(\tB\t\xe0A\x03\xe0A\x05\xe0A\x08\x12\x14\n\x0cdisplay_name\x18\x06 \x01(\t\x12O\n\x05tasks\x18\x02 \x03(\x0b2@.google.cloud.bigquery.migration.v2.MigrationWorkflow.TasksEntry\x12O\n\x05state\x18\x03 \x01(\x0e2;.google.cloud.bigquery.migration.v2.MigrationWorkflow.StateB\x03\xe0A\x03\x12/\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x10last_update_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a_\n\nTasksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12@\n\x05value\x18\x02 \x01(\x0b21.google.cloud.bigquery.migration.v2.MigrationTask:\x028\x01"Q\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\t\n\x05DRAFT\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\n\n\x06PAUSED\x10\x03\x12\r\n\tCOMPLETED\x10\x04:u\xeaAr\n2bigquerymigration.googleapis.com/MigrationWorkflow\x12<projects/{project}/locations/{location}/workflows/{workflow}"\xb4\x07\n\rMigrationTask\x12b\n\x1atranslation_config_details\x18\x0e \x01(\x0b2<.google.cloud.bigquery.migration.v2.TranslationConfigDetailsH\x00\x12U\n\x13translation_details\x18\x10 \x01(\x0b26.google.cloud.bigquery.migration.v2.TranslationDetailsH\x00\x12\x12\n\x02id\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x05\x12\x0c\n\x04type\x18\x02 \x01(\t\x12K\n\x05state\x18\x04 \x01(\x0e27.google.cloud.bigquery.migration.v2.MigrationTask.StateB\x03\xe0A\x03\x124\n\x10processing_error\x18\x05 \x01(\x0b2\x15.google.rpc.ErrorInfoB\x03\xe0A\x03\x12/\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x10last_update_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\\\n\x16resource_error_details\x18\x11 \x03(\x0b27.google.cloud.bigquery.migration.v2.ResourceErrorDetailB\x03\xe0A\x03\x12\x1c\n\x14resource_error_count\x18\x12 \x01(\x05\x12?\n\x07metrics\x18\x13 \x03(\x0b2..google.cloud.bigquery.migration.v2.TimeSeries\x12Q\n\x0btask_result\x18\x14 \x01(\x0b27.google.cloud.bigquery.migration.v2.MigrationTaskResultB\x03\xe0A\x03\x12$\n\x1ctotal_processing_error_count\x18\x15 \x01(\x05\x12"\n\x1atotal_resource_error_count\x18\x16 \x01(\x05"r\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x11\n\rORCHESTRATING\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\n\n\x06PAUSED\x10\x04\x12\r\n\tSUCCEEDED\x10\x05\x12\n\n\x06FAILED\x10\x06B\x0e\n\x0ctask_details"\xf4\x05\n\x10MigrationSubtask\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x05\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12N\n\x05state\x18\x05 \x01(\x0e2:.google.cloud.bigquery.migration.v2.MigrationSubtask.StateB\x03\xe0A\x03\x124\n\x10processing_error\x18\x06 \x01(\x0b2\x15.google.rpc.ErrorInfoB\x03\xe0A\x03\x12\\\n\x16resource_error_details\x18\x0c \x03(\x0b27.google.cloud.bigquery.migration.v2.ResourceErrorDetailB\x03\xe0A\x03\x12\x1c\n\x14resource_error_count\x18\r \x01(\x05\x12/\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x10last_update_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12?\n\x07metrics\x18\x0b \x03(\x0b2..google.cloud.bigquery.migration.v2.TimeSeries"v\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\n\n\x06PAUSED\x10\x05\x12\x16\n\x12PENDING_DEPENDENCY\x10\x06:\x88\x01\xeaA\x84\x01\n1bigquerymigration.googleapis.com/MigrationSubtask\x12Oprojects/{project}/locations/{location}/workflows/{workflow}/subtasks/{subtask}"~\n\x13MigrationTaskResult\x12\\\n\x17translation_task_result\x18\x02 \x01(\x0b29.google.cloud.bigquery.migration.v2.TranslationTaskResultH\x00B\t\n\x07details"\xb7\x01\n\x15TranslationTaskResult\x12H\n\x13translated_literals\x18\x01 \x03(\x0b2+.google.cloud.bigquery.migration.v2.Literal\x12T\n\x13report_log_messages\x18\x02 \x03(\x0b27.google.cloud.bigquery.migration.v2.GcsReportLogMessageB\xd2\x01\n&com.google.cloud.bigquery.migration.v2B\x16MigrationEntitiesProtoP\x01ZDcloud.google.com/go/bigquery/migration/apiv2/migrationpb;migrationpb\xaa\x02"Google.Cloud.BigQuery.Migration.V2\xca\x02"Google\\Cloud\\BigQuery\\Migration\\V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.migration.v2.migration_entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.bigquery.migration.v2B\x16MigrationEntitiesProtoP\x01ZDcloud.google.com/go/bigquery/migration/apiv2/migrationpb;migrationpb\xaa\x02"Google.Cloud.BigQuery.Migration.V2\xca\x02"Google\\Cloud\\BigQuery\\Migration\\V2'
    _globals['_MIGRATIONWORKFLOW_TASKSENTRY']._loaded_options = None
    _globals['_MIGRATIONWORKFLOW_TASKSENTRY']._serialized_options = b'8\x01'
    _globals['_MIGRATIONWORKFLOW'].fields_by_name['name']._loaded_options = None
    _globals['_MIGRATIONWORKFLOW'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x05\xe0A\x08'
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
    _globals['_MIGRATIONTASK'].fields_by_name['resource_error_details']._loaded_options = None
    _globals['_MIGRATIONTASK'].fields_by_name['resource_error_details']._serialized_options = b'\xe0A\x03'
    _globals['_MIGRATIONTASK'].fields_by_name['task_result']._loaded_options = None
    _globals['_MIGRATIONTASK'].fields_by_name['task_result']._serialized_options = b'\xe0A\x03'
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
    _globals['_MIGRATIONWORKFLOW']._serialized_start = 538
    _globals['_MIGRATIONWORKFLOW']._serialized_end = 1168
    _globals['_MIGRATIONWORKFLOW_TASKSENTRY']._serialized_start = 871
    _globals['_MIGRATIONWORKFLOW_TASKSENTRY']._serialized_end = 966
    _globals['_MIGRATIONWORKFLOW_STATE']._serialized_start = 968
    _globals['_MIGRATIONWORKFLOW_STATE']._serialized_end = 1049
    _globals['_MIGRATIONTASK']._serialized_start = 1171
    _globals['_MIGRATIONTASK']._serialized_end = 2119
    _globals['_MIGRATIONTASK_STATE']._serialized_start = 1989
    _globals['_MIGRATIONTASK_STATE']._serialized_end = 2103
    _globals['_MIGRATIONSUBTASK']._serialized_start = 2122
    _globals['_MIGRATIONSUBTASK']._serialized_end = 2878
    _globals['_MIGRATIONSUBTASK_STATE']._serialized_start = 2621
    _globals['_MIGRATIONSUBTASK_STATE']._serialized_end = 2739
    _globals['_MIGRATIONTASKRESULT']._serialized_start = 2880
    _globals['_MIGRATIONTASKRESULT']._serialized_end = 3006
    _globals['_TRANSLATIONTASKRESULT']._serialized_start = 3009
    _globals['_TRANSLATIONTASKRESULT']._serialized_end = 3192