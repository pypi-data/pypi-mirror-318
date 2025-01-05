"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/migration/v2alpha/migration_service.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.bigquery.migration.v2alpha import migration_entities_pb2 as google_dot_cloud_dot_bigquery_dot_migration_dot_v2alpha_dot_migration__entities__pb2
from ......google.cloud.bigquery.migration.v2alpha import migration_error_details_pb2 as google_dot_cloud_dot_bigquery_dot_migration_dot_v2alpha_dot_migration__error__details__pb2
from ......google.cloud.bigquery.migration.v2alpha import migration_metrics_pb2 as google_dot_cloud_dot_bigquery_dot_migration_dot_v2alpha_dot_migration__metrics__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/bigquery/migration/v2alpha/migration_service.proto\x12\'google.cloud.bigquery.migration.v2alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a@google/cloud/bigquery/migration/v2alpha/migration_entities.proto\x1aEgoogle/cloud/bigquery/migration/v2alpha/migration_error_details.proto\x1a?google/cloud/bigquery/migration/v2alpha/migration_metrics.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xb8\x01\n\x1eCreateMigrationWorkflowRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12[\n\x12migration_workflow\x18\x02 \x01(\x0b2:.google.cloud.bigquery.migration.v2alpha.MigrationWorkflowB\x03\xe0A\x02"\x96\x01\n\x1bGetMigrationWorkflowRequest\x12H\n\x04name\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\n2bigquerymigration.googleapis.com/MigrationWorkflow\x12-\n\tread_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xb0\x01\n\x1dListMigrationWorkflowsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12-\n\tread_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"\x92\x01\n\x1eListMigrationWorkflowsResponse\x12W\n\x13migration_workflows\x18\x01 \x03(\x0b2:.google.cloud.bigquery.migration.v2alpha.MigrationWorkflow\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"j\n\x1eDeleteMigrationWorkflowRequest\x12H\n\x04name\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\n2bigquerymigration.googleapis.com/MigrationWorkflow"i\n\x1dStartMigrationWorkflowRequest\x12H\n\x04name\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\n2bigquerymigration.googleapis.com/MigrationWorkflow"\x99\x01\n\x1aGetMigrationSubtaskRequest\x12G\n\x04name\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\n1bigquerymigration.googleapis.com/MigrationSubtask\x122\n\tread_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\xe4\x01\n\x1cListMigrationSubtasksRequest\x12J\n\x06parent\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\n2bigquerymigration.googleapis.com/MigrationWorkflow\x122\n\tread_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x05 \x01(\tB\x03\xe0A\x01"\x8f\x01\n\x1dListMigrationSubtasksResponse\x12U\n\x12migration_subtasks\x18\x01 \x03(\x0b29.google.cloud.bigquery.migration.v2alpha.MigrationSubtask\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xaa\r\n\x10MigrationService\x12\x8a\x02\n\x17CreateMigrationWorkflow\x12G.google.cloud.bigquery.migration.v2alpha.CreateMigrationWorkflowRequest\x1a:.google.cloud.bigquery.migration.v2alpha.MigrationWorkflow"j\xdaA\x19parent,migration_workflow\x82\xd3\xe4\x93\x02H"2/v2alpha/{parent=projects/*/locations/*}/workflows:\x12migration_workflow\x12\xdb\x01\n\x14GetMigrationWorkflow\x12D.google.cloud.bigquery.migration.v2alpha.GetMigrationWorkflowRequest\x1a:.google.cloud.bigquery.migration.v2alpha.MigrationWorkflow"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v2alpha/{name=projects/*/locations/*/workflows/*}\x12\xee\x01\n\x16ListMigrationWorkflows\x12F.google.cloud.bigquery.migration.v2alpha.ListMigrationWorkflowsRequest\x1aG.google.cloud.bigquery.migration.v2alpha.ListMigrationWorkflowsResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v2alpha/{parent=projects/*/locations/*}/workflows\x12\xbd\x01\n\x17DeleteMigrationWorkflow\x12G.google.cloud.bigquery.migration.v2alpha.DeleteMigrationWorkflowRequest\x1a\x16.google.protobuf.Empty"A\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v2alpha/{name=projects/*/locations/*/workflows/*}\x12\xc4\x01\n\x16StartMigrationWorkflow\x12F.google.cloud.bigquery.migration.v2alpha.StartMigrationWorkflowRequest\x1a\x16.google.protobuf.Empty"J\xdaA\x04name\x82\xd3\xe4\x93\x02="8/v2alpha/{name=projects/*/locations/*/workflows/*}:start:\x01*\x12\xe3\x01\n\x13GetMigrationSubtask\x12C.google.cloud.bigquery.migration.v2alpha.GetMigrationSubtaskRequest\x1a9.google.cloud.bigquery.migration.v2alpha.MigrationSubtask"L\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v2alpha/{name=projects/*/locations/*/workflows/*/subtasks/*}\x12\xf6\x01\n\x15ListMigrationSubtasks\x12E.google.cloud.bigquery.migration.v2alpha.ListMigrationSubtasksRequest\x1aF.google.cloud.bigquery.migration.v2alpha.ListMigrationSubtasksResponse"N\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v2alpha/{parent=projects/*/locations/*/workflows/*}/subtasks\x1aT\xcaA bigquerymigration.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe5\x01\n+com.google.cloud.bigquery.migration.v2alphaB\x15MigrationServiceProtoP\x01ZIcloud.google.com/go/bigquery/migration/apiv2alpha/migrationpb;migrationpb\xaa\x02\'Google.Cloud.BigQuery.Migration.V2Alpha\xca\x02\'Google\\Cloud\\BigQuery\\Migration\\V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.migration.v2alpha.migration_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.cloud.bigquery.migration.v2alphaB\x15MigrationServiceProtoP\x01ZIcloud.google.com/go/bigquery/migration/apiv2alpha/migrationpb;migrationpb\xaa\x02'Google.Cloud.BigQuery.Migration.V2Alpha\xca\x02'Google\\Cloud\\BigQuery\\Migration\\V2alpha"
    _globals['_CREATEMIGRATIONWORKFLOWREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEMIGRATIONWORKFLOWREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEMIGRATIONWORKFLOWREQUEST'].fields_by_name['migration_workflow']._loaded_options = None
    _globals['_CREATEMIGRATIONWORKFLOWREQUEST'].fields_by_name['migration_workflow']._serialized_options = b'\xe0A\x02'
    _globals['_GETMIGRATIONWORKFLOWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMIGRATIONWORKFLOWREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA4\n2bigquerymigration.googleapis.com/MigrationWorkflow'
    _globals['_LISTMIGRATIONWORKFLOWSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMIGRATIONWORKFLOWSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_DELETEMIGRATIONWORKFLOWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEMIGRATIONWORKFLOWREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA4\n2bigquerymigration.googleapis.com/MigrationWorkflow'
    _globals['_STARTMIGRATIONWORKFLOWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STARTMIGRATIONWORKFLOWREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA4\n2bigquerymigration.googleapis.com/MigrationWorkflow'
    _globals['_GETMIGRATIONSUBTASKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMIGRATIONSUBTASKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA3\n1bigquerymigration.googleapis.com/MigrationSubtask'
    _globals['_GETMIGRATIONSUBTASKREQUEST'].fields_by_name['read_mask']._loaded_options = None
    _globals['_GETMIGRATIONSUBTASKREQUEST'].fields_by_name['read_mask']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMIGRATIONSUBTASKSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMIGRATIONSUBTASKSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA4\n2bigquerymigration.googleapis.com/MigrationWorkflow'
    _globals['_LISTMIGRATIONSUBTASKSREQUEST'].fields_by_name['read_mask']._loaded_options = None
    _globals['_LISTMIGRATIONSUBTASKSREQUEST'].fields_by_name['read_mask']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMIGRATIONSUBTASKSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTMIGRATIONSUBTASKSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMIGRATIONSUBTASKSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTMIGRATIONSUBTASKSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMIGRATIONSUBTASKSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTMIGRATIONSUBTASKSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_MIGRATIONSERVICE']._loaded_options = None
    _globals['_MIGRATIONSERVICE']._serialized_options = b'\xcaA bigquerymigration.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_MIGRATIONSERVICE'].methods_by_name['CreateMigrationWorkflow']._loaded_options = None
    _globals['_MIGRATIONSERVICE'].methods_by_name['CreateMigrationWorkflow']._serialized_options = b'\xdaA\x19parent,migration_workflow\x82\xd3\xe4\x93\x02H"2/v2alpha/{parent=projects/*/locations/*}/workflows:\x12migration_workflow'
    _globals['_MIGRATIONSERVICE'].methods_by_name['GetMigrationWorkflow']._loaded_options = None
    _globals['_MIGRATIONSERVICE'].methods_by_name['GetMigrationWorkflow']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v2alpha/{name=projects/*/locations/*/workflows/*}'
    _globals['_MIGRATIONSERVICE'].methods_by_name['ListMigrationWorkflows']._loaded_options = None
    _globals['_MIGRATIONSERVICE'].methods_by_name['ListMigrationWorkflows']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v2alpha/{parent=projects/*/locations/*}/workflows'
    _globals['_MIGRATIONSERVICE'].methods_by_name['DeleteMigrationWorkflow']._loaded_options = None
    _globals['_MIGRATIONSERVICE'].methods_by_name['DeleteMigrationWorkflow']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v2alpha/{name=projects/*/locations/*/workflows/*}'
    _globals['_MIGRATIONSERVICE'].methods_by_name['StartMigrationWorkflow']._loaded_options = None
    _globals['_MIGRATIONSERVICE'].methods_by_name['StartMigrationWorkflow']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02="8/v2alpha/{name=projects/*/locations/*/workflows/*}:start:\x01*'
    _globals['_MIGRATIONSERVICE'].methods_by_name['GetMigrationSubtask']._loaded_options = None
    _globals['_MIGRATIONSERVICE'].methods_by_name['GetMigrationSubtask']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v2alpha/{name=projects/*/locations/*/workflows/*/subtasks/*}'
    _globals['_MIGRATIONSERVICE'].methods_by_name['ListMigrationSubtasks']._loaded_options = None
    _globals['_MIGRATIONSERVICE'].methods_by_name['ListMigrationSubtasks']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v2alpha/{parent=projects/*/locations/*/workflows/*}/subtasks'
    _globals['_CREATEMIGRATIONWORKFLOWREQUEST']._serialized_start = 489
    _globals['_CREATEMIGRATIONWORKFLOWREQUEST']._serialized_end = 673
    _globals['_GETMIGRATIONWORKFLOWREQUEST']._serialized_start = 676
    _globals['_GETMIGRATIONWORKFLOWREQUEST']._serialized_end = 826
    _globals['_LISTMIGRATIONWORKFLOWSREQUEST']._serialized_start = 829
    _globals['_LISTMIGRATIONWORKFLOWSREQUEST']._serialized_end = 1005
    _globals['_LISTMIGRATIONWORKFLOWSRESPONSE']._serialized_start = 1008
    _globals['_LISTMIGRATIONWORKFLOWSRESPONSE']._serialized_end = 1154
    _globals['_DELETEMIGRATIONWORKFLOWREQUEST']._serialized_start = 1156
    _globals['_DELETEMIGRATIONWORKFLOWREQUEST']._serialized_end = 1262
    _globals['_STARTMIGRATIONWORKFLOWREQUEST']._serialized_start = 1264
    _globals['_STARTMIGRATIONWORKFLOWREQUEST']._serialized_end = 1369
    _globals['_GETMIGRATIONSUBTASKREQUEST']._serialized_start = 1372
    _globals['_GETMIGRATIONSUBTASKREQUEST']._serialized_end = 1525
    _globals['_LISTMIGRATIONSUBTASKSREQUEST']._serialized_start = 1528
    _globals['_LISTMIGRATIONSUBTASKSREQUEST']._serialized_end = 1756
    _globals['_LISTMIGRATIONSUBTASKSRESPONSE']._serialized_start = 1759
    _globals['_LISTMIGRATIONSUBTASKSRESPONSE']._serialized_end = 1902
    _globals['_MIGRATIONSERVICE']._serialized_start = 1905
    _globals['_MIGRATIONSERVICE']._serialized_end = 3611