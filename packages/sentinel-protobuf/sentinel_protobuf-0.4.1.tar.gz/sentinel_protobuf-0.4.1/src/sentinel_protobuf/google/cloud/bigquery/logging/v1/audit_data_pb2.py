"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/logging/v1/audit_data.proto')
_sym_db = _symbol_database.Default()
from ......google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from ......google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/bigquery/logging/v1/audit_data.proto\x12 google.cloud.bigquery.logging.v1\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xac\x0e\n\tAuditData\x12T\n\x14table_insert_request\x18\x01 \x01(\x0b24.google.cloud.bigquery.logging.v1.TableInsertRequestH\x00\x12T\n\x14table_update_request\x18\x10 \x01(\x0b24.google.cloud.bigquery.logging.v1.TableUpdateRequestH\x00\x12T\n\x14dataset_list_request\x18\x02 \x01(\x0b24.google.cloud.bigquery.logging.v1.DatasetListRequestH\x00\x12X\n\x16dataset_insert_request\x18\x03 \x01(\x0b26.google.cloud.bigquery.logging.v1.DatasetInsertRequestH\x00\x12X\n\x16dataset_update_request\x18\x04 \x01(\x0b26.google.cloud.bigquery.logging.v1.DatasetUpdateRequestH\x00\x12P\n\x12job_insert_request\x18\x05 \x01(\x0b22.google.cloud.bigquery.logging.v1.JobInsertRequestH\x00\x12N\n\x11job_query_request\x18\x06 \x01(\x0b21.google.cloud.bigquery.logging.v1.JobQueryRequestH\x00\x12d\n\x1djob_get_query_results_request\x18\x07 \x01(\x0b2;.google.cloud.bigquery.logging.v1.JobGetQueryResultsRequestH\x00\x12Y\n\x17table_data_list_request\x18\x08 \x01(\x0b26.google.cloud.bigquery.logging.v1.TableDataListRequestH\x00\x12D\n\x16set_iam_policy_request\x18\x14 \x01(\x0b2".google.iam.v1.SetIamPolicyRequestH\x00\x12V\n\x15table_insert_response\x18\t \x01(\x0b25.google.cloud.bigquery.logging.v1.TableInsertResponseH\x01\x12V\n\x15table_update_response\x18\n \x01(\x0b25.google.cloud.bigquery.logging.v1.TableUpdateResponseH\x01\x12Z\n\x17dataset_insert_response\x18\x0b \x01(\x0b27.google.cloud.bigquery.logging.v1.DatasetInsertResponseH\x01\x12Z\n\x17dataset_update_response\x18\x0c \x01(\x0b27.google.cloud.bigquery.logging.v1.DatasetUpdateResponseH\x01\x12R\n\x13job_insert_response\x18\x12 \x01(\x0b23.google.cloud.bigquery.logging.v1.JobInsertResponseH\x01\x12P\n\x12job_query_response\x18\r \x01(\x0b22.google.cloud.bigquery.logging.v1.JobQueryResponseH\x01\x12f\n\x1ejob_get_query_results_response\x18\x0e \x01(\x0b2<.google.cloud.bigquery.logging.v1.JobGetQueryResultsResponseH\x01\x12Y\n\x17job_query_done_response\x18\x0f \x01(\x0b26.google.cloud.bigquery.logging.v1.JobQueryDoneResponseH\x01\x120\n\x0fpolicy_response\x18\x15 \x01(\x0b2\x15.google.iam.v1.PolicyH\x01\x12P\n\x13job_completed_event\x18\x11 \x01(\x0b23.google.cloud.bigquery.logging.v1.JobCompletedEvent\x12T\n\x16table_data_read_events\x18\x13 \x03(\x0b24.google.cloud.bigquery.logging.v1.TableDataReadEventB\t\n\x07requestB\n\n\x08response"O\n\x12TableInsertRequest\x129\n\x08resource\x18\x01 \x01(\x0b2\'.google.cloud.bigquery.logging.v1.Table"O\n\x12TableUpdateRequest\x129\n\x08resource\x18\x01 \x01(\x0b2\'.google.cloud.bigquery.logging.v1.Table"P\n\x13TableInsertResponse\x129\n\x08resource\x18\x01 \x01(\x0b2\'.google.cloud.bigquery.logging.v1.Table"P\n\x13TableUpdateResponse\x129\n\x08resource\x18\x01 \x01(\x0b2\'.google.cloud.bigquery.logging.v1.Table"&\n\x12DatasetListRequest\x12\x10\n\x08list_all\x18\x01 \x01(\x08"S\n\x14DatasetInsertRequest\x12;\n\x08resource\x18\x01 \x01(\x0b2).google.cloud.bigquery.logging.v1.Dataset"T\n\x15DatasetInsertResponse\x12;\n\x08resource\x18\x01 \x01(\x0b2).google.cloud.bigquery.logging.v1.Dataset"S\n\x14DatasetUpdateRequest\x12;\n\x08resource\x18\x01 \x01(\x0b2).google.cloud.bigquery.logging.v1.Dataset"T\n\x15DatasetUpdateResponse\x12;\n\x08resource\x18\x01 \x01(\x0b2).google.cloud.bigquery.logging.v1.Dataset"K\n\x10JobInsertRequest\x127\n\x08resource\x18\x01 \x01(\x0b2%.google.cloud.bigquery.logging.v1.Job"L\n\x11JobInsertResponse\x127\n\x08resource\x18\x01 \x01(\x0b2%.google.cloud.bigquery.logging.v1.Job"\xa2\x01\n\x0fJobQueryRequest\x12\r\n\x05query\x18\x01 \x01(\t\x12\x13\n\x0bmax_results\x18\x02 \x01(\r\x12F\n\x0fdefault_dataset\x18\x03 \x01(\x0b2-.google.cloud.bigquery.logging.v1.DatasetName\x12\x12\n\nproject_id\x18\x04 \x01(\t\x12\x0f\n\x07dry_run\x18\x05 \x01(\x08"]\n\x10JobQueryResponse\x12\x15\n\rtotal_results\x18\x01 \x01(\x04\x122\n\x03job\x18\x02 \x01(\x0b2%.google.cloud.bigquery.logging.v1.Job"C\n\x19JobGetQueryResultsRequest\x12\x13\n\x0bmax_results\x18\x01 \x01(\r\x12\x11\n\tstart_row\x18\x02 \x01(\x04"g\n\x1aJobGetQueryResultsResponse\x12\x15\n\rtotal_results\x18\x01 \x01(\x04\x122\n\x03job\x18\x02 \x01(\x0b2%.google.cloud.bigquery.logging.v1.Job"J\n\x14JobQueryDoneResponse\x122\n\x03job\x18\x01 \x01(\x0b2%.google.cloud.bigquery.logging.v1.Job"[\n\x11JobCompletedEvent\x12\x12\n\nevent_name\x18\x01 \x01(\t\x122\n\x03job\x18\x02 \x01(\x0b2%.google.cloud.bigquery.logging.v1.Job"p\n\x12TableDataReadEvent\x12?\n\ntable_name\x18\x01 \x01(\x0b2+.google.cloud.bigquery.logging.v1.TableName\x12\x19\n\x11referenced_fields\x18\x02 \x03(\t">\n\x14TableDataListRequest\x12\x11\n\tstart_row\x18\x01 \x01(\x04\x12\x13\n\x0bmax_results\x18\x02 \x01(\r"\xe9\x03\n\x05Table\x12?\n\ntable_name\x18\x01 \x01(\x0b2+.google.cloud.bigquery.logging.v1.TableName\x129\n\x04info\x18\x02 \x01(\x0b2+.google.cloud.bigquery.logging.v1.TableInfo\x12\x13\n\x0bschema_json\x18\x08 \x01(\t\x12C\n\x04view\x18\x04 \x01(\x0b25.google.cloud.bigquery.logging.v1.TableViewDefinition\x12/\n\x0bexpire_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x121\n\rtruncate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.Timestamp\x12D\n\nencryption\x18\n \x01(\x0b20.google.cloud.bigquery.logging.v1.EncryptionInfo"\xaf\x01\n\tTableInfo\x12\x15\n\rfriendly_name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12G\n\x06labels\x18\x03 \x03(\x0b27.google.cloud.bigquery.logging.v1.TableInfo.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"$\n\x13TableViewDefinition\x12\r\n\x05query\x18\x01 \x01(\t"\xeb\x02\n\x07Dataset\x12C\n\x0cdataset_name\x18\x01 \x01(\x0b2-.google.cloud.bigquery.logging.v1.DatasetName\x12;\n\x04info\x18\x02 \x01(\x0b2-.google.cloud.bigquery.logging.v1.DatasetInfo\x12/\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12:\n\x03acl\x18\x06 \x01(\x0b2-.google.cloud.bigquery.logging.v1.BigQueryAcl\x12@\n\x1ddefault_table_expire_duration\x18\x08 \x01(\x0b2\x19.google.protobuf.Duration"\xb3\x01\n\x0bDatasetInfo\x12\x15\n\rfriendly_name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12I\n\x06labels\x18\x03 \x03(\x0b29.google.cloud.bigquery.logging.v1.DatasetInfo.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xfb\x01\n\x0bBigQueryAcl\x12D\n\x07entries\x18\x01 \x03(\x0b23.google.cloud.bigquery.logging.v1.BigQueryAcl.Entry\x1a\xa5\x01\n\x05Entry\x12\x0c\n\x04role\x18\x01 \x01(\t\x12\x13\n\x0bgroup_email\x18\x02 \x01(\t\x12\x12\n\nuser_email\x18\x03 \x01(\t\x12\x0e\n\x06domain\x18\x04 \x01(\t\x12\x15\n\rspecial_group\x18\x05 \x01(\t\x12>\n\tview_name\x18\x06 \x01(\x0b2+.google.cloud.bigquery.logging.v1.TableName"\x9b\x02\n\x03Job\x12;\n\x08job_name\x18\x01 \x01(\x0b2).google.cloud.bigquery.logging.v1.JobName\x12M\n\x11job_configuration\x18\x02 \x01(\x0b22.google.cloud.bigquery.logging.v1.JobConfiguration\x12?\n\njob_status\x18\x03 \x01(\x0b2+.google.cloud.bigquery.logging.v1.JobStatus\x12G\n\x0ejob_statistics\x18\x04 \x01(\x0b2/.google.cloud.bigquery.logging.v1.JobStatistics"\xbb\x0c\n\x10JobConfiguration\x12I\n\x05query\x18\x05 \x01(\x0b28.google.cloud.bigquery.logging.v1.JobConfiguration.QueryH\x00\x12G\n\x04load\x18\x06 \x01(\x0b27.google.cloud.bigquery.logging.v1.JobConfiguration.LoadH\x00\x12M\n\x07extract\x18\x07 \x01(\x0b2:.google.cloud.bigquery.logging.v1.JobConfiguration.ExtractH\x00\x12R\n\ntable_copy\x18\x08 \x01(\x0b2<.google.cloud.bigquery.logging.v1.JobConfiguration.TableCopyH\x00\x12\x0f\n\x07dry_run\x18\t \x01(\x08\x12N\n\x06labels\x18\x03 \x03(\x0b2>.google.cloud.bigquery.logging.v1.JobConfiguration.LabelsEntry\x1a\xb3\x03\n\x05Query\x12\r\n\x05query\x18\x01 \x01(\t\x12F\n\x11destination_table\x18\x02 \x01(\x0b2+.google.cloud.bigquery.logging.v1.TableName\x12\x1a\n\x12create_disposition\x18\x03 \x01(\t\x12\x19\n\x11write_disposition\x18\x04 \x01(\t\x12F\n\x0fdefault_dataset\x18\x05 \x01(\x0b2-.google.cloud.bigquery.logging.v1.DatasetName\x12L\n\x11table_definitions\x18\x06 \x03(\x0b21.google.cloud.bigquery.logging.v1.TableDefinition\x12\x16\n\x0equery_priority\x18\x07 \x01(\t\x12V\n\x1cdestination_table_encryption\x18\x08 \x01(\x0b20.google.cloud.bigquery.logging.v1.EncryptionInfo\x12\x16\n\x0estatement_type\x18\t \x01(\t\x1a\x87\x02\n\x04Load\x12\x13\n\x0bsource_uris\x18\x01 \x03(\t\x12\x13\n\x0bschema_json\x18\x06 \x01(\t\x12F\n\x11destination_table\x18\x03 \x01(\x0b2+.google.cloud.bigquery.logging.v1.TableName\x12\x1a\n\x12create_disposition\x18\x04 \x01(\t\x12\x19\n\x11write_disposition\x18\x05 \x01(\t\x12V\n\x1cdestination_table_encryption\x18\x07 \x01(\x0b20.google.cloud.bigquery.logging.v1.EncryptionInfo\x1af\n\x07Extract\x12\x18\n\x10destination_uris\x18\x01 \x03(\t\x12A\n\x0csource_table\x18\x02 \x01(\x0b2+.google.cloud.bigquery.logging.v1.TableName\x1a\xa6\x02\n\tTableCopy\x12B\n\rsource_tables\x18\x01 \x03(\x0b2+.google.cloud.bigquery.logging.v1.TableName\x12F\n\x11destination_table\x18\x02 \x01(\x0b2+.google.cloud.bigquery.logging.v1.TableName\x12\x1a\n\x12create_disposition\x18\x03 \x01(\t\x12\x19\n\x11write_disposition\x18\x04 \x01(\t\x12V\n\x1cdestination_table_encryption\x18\x05 \x01(\x0b20.google.cloud.bigquery.logging.v1.EncryptionInfo\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x0f\n\rconfiguration"4\n\x0fTableDefinition\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bsource_uris\x18\x02 \x03(\t"l\n\tJobStatus\x12\r\n\x05state\x18\x01 \x01(\t\x12!\n\x05error\x18\x02 \x01(\x0b2\x12.google.rpc.Status\x12-\n\x11additional_errors\x18\x03 \x03(\x0b2\x12.google.rpc.Status"\xce\x05\n\rJobStatistics\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12.\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x1d\n\x15total_processed_bytes\x18\x04 \x01(\x03\x12\x1a\n\x12total_billed_bytes\x18\x05 \x01(\x03\x12\x14\n\x0cbilling_tier\x18\x07 \x01(\x05\x12\x15\n\rtotal_slot_ms\x18\x08 \x01(\x03\x12g\n\x11reservation_usage\x18\x0e \x03(\x0b2H.google.cloud.bigquery.logging.v1.JobStatistics.ReservationResourceUsageB\x02\x18\x01\x12\x13\n\x0breservation\x18\x10 \x01(\t\x12F\n\x11referenced_tables\x18\t \x03(\x0b2+.google.cloud.bigquery.logging.v1.TableName\x12\x1e\n\x16total_tables_processed\x18\n \x01(\x05\x12E\n\x10referenced_views\x18\x0b \x03(\x0b2+.google.cloud.bigquery.logging.v1.TableName\x12\x1d\n\x15total_views_processed\x18\x0c \x01(\x05\x12\x1e\n\x16query_output_row_count\x18\x0f \x01(\x03\x12\x1f\n\x17total_load_output_bytes\x18\r \x01(\x03\x1a9\n\x18ReservationResourceUsage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07slot_ms\x18\x02 \x01(\x03"5\n\x0bDatasetName\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t"E\n\tTableName\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x10\n\x08table_id\x18\x03 \x01(\t"?\n\x07JobName\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0e\n\x06job_id\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t"&\n\x0eEncryptionInfo\x12\x14\n\x0ckms_key_name\x18\x01 \x01(\tB\x9b\x01\n$com.google.cloud.bigquery.logging.v1B\x0eAuditDataProtoP\x01Z>cloud.google.com/go/bigquery/logging/apiv1/loggingpb;loggingpb\xaa\x02 Google.Cloud.BigQuery.Logging.V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.logging.v1.audit_data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.bigquery.logging.v1B\x0eAuditDataProtoP\x01Z>cloud.google.com/go/bigquery/logging/apiv1/loggingpb;loggingpb\xaa\x02 Google.Cloud.BigQuery.Logging.V1'
    _globals['_TABLEINFO_LABELSENTRY']._loaded_options = None
    _globals['_TABLEINFO_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_DATASETINFO_LABELSENTRY']._loaded_options = None
    _globals['_DATASETINFO_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_JOBCONFIGURATION_LABELSENTRY']._loaded_options = None
    _globals['_JOBCONFIGURATION_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_JOBSTATISTICS'].fields_by_name['reservation_usage']._loaded_options = None
    _globals['_JOBSTATISTICS'].fields_by_name['reservation_usage']._serialized_options = b'\x18\x01'
    _globals['_AUDITDATA']._serialized_start = 238
    _globals['_AUDITDATA']._serialized_end = 2074
    _globals['_TABLEINSERTREQUEST']._serialized_start = 2076
    _globals['_TABLEINSERTREQUEST']._serialized_end = 2155
    _globals['_TABLEUPDATEREQUEST']._serialized_start = 2157
    _globals['_TABLEUPDATEREQUEST']._serialized_end = 2236
    _globals['_TABLEINSERTRESPONSE']._serialized_start = 2238
    _globals['_TABLEINSERTRESPONSE']._serialized_end = 2318
    _globals['_TABLEUPDATERESPONSE']._serialized_start = 2320
    _globals['_TABLEUPDATERESPONSE']._serialized_end = 2400
    _globals['_DATASETLISTREQUEST']._serialized_start = 2402
    _globals['_DATASETLISTREQUEST']._serialized_end = 2440
    _globals['_DATASETINSERTREQUEST']._serialized_start = 2442
    _globals['_DATASETINSERTREQUEST']._serialized_end = 2525
    _globals['_DATASETINSERTRESPONSE']._serialized_start = 2527
    _globals['_DATASETINSERTRESPONSE']._serialized_end = 2611
    _globals['_DATASETUPDATEREQUEST']._serialized_start = 2613
    _globals['_DATASETUPDATEREQUEST']._serialized_end = 2696
    _globals['_DATASETUPDATERESPONSE']._serialized_start = 2698
    _globals['_DATASETUPDATERESPONSE']._serialized_end = 2782
    _globals['_JOBINSERTREQUEST']._serialized_start = 2784
    _globals['_JOBINSERTREQUEST']._serialized_end = 2859
    _globals['_JOBINSERTRESPONSE']._serialized_start = 2861
    _globals['_JOBINSERTRESPONSE']._serialized_end = 2937
    _globals['_JOBQUERYREQUEST']._serialized_start = 2940
    _globals['_JOBQUERYREQUEST']._serialized_end = 3102
    _globals['_JOBQUERYRESPONSE']._serialized_start = 3104
    _globals['_JOBQUERYRESPONSE']._serialized_end = 3197
    _globals['_JOBGETQUERYRESULTSREQUEST']._serialized_start = 3199
    _globals['_JOBGETQUERYRESULTSREQUEST']._serialized_end = 3266
    _globals['_JOBGETQUERYRESULTSRESPONSE']._serialized_start = 3268
    _globals['_JOBGETQUERYRESULTSRESPONSE']._serialized_end = 3371
    _globals['_JOBQUERYDONERESPONSE']._serialized_start = 3373
    _globals['_JOBQUERYDONERESPONSE']._serialized_end = 3447
    _globals['_JOBCOMPLETEDEVENT']._serialized_start = 3449
    _globals['_JOBCOMPLETEDEVENT']._serialized_end = 3540
    _globals['_TABLEDATAREADEVENT']._serialized_start = 3542
    _globals['_TABLEDATAREADEVENT']._serialized_end = 3654
    _globals['_TABLEDATALISTREQUEST']._serialized_start = 3656
    _globals['_TABLEDATALISTREQUEST']._serialized_end = 3718
    _globals['_TABLE']._serialized_start = 3721
    _globals['_TABLE']._serialized_end = 4210
    _globals['_TABLEINFO']._serialized_start = 4213
    _globals['_TABLEINFO']._serialized_end = 4388
    _globals['_TABLEINFO_LABELSENTRY']._serialized_start = 4343
    _globals['_TABLEINFO_LABELSENTRY']._serialized_end = 4388
    _globals['_TABLEVIEWDEFINITION']._serialized_start = 4390
    _globals['_TABLEVIEWDEFINITION']._serialized_end = 4426
    _globals['_DATASET']._serialized_start = 4429
    _globals['_DATASET']._serialized_end = 4792
    _globals['_DATASETINFO']._serialized_start = 4795
    _globals['_DATASETINFO']._serialized_end = 4974
    _globals['_DATASETINFO_LABELSENTRY']._serialized_start = 4343
    _globals['_DATASETINFO_LABELSENTRY']._serialized_end = 4388
    _globals['_BIGQUERYACL']._serialized_start = 4977
    _globals['_BIGQUERYACL']._serialized_end = 5228
    _globals['_BIGQUERYACL_ENTRY']._serialized_start = 5063
    _globals['_BIGQUERYACL_ENTRY']._serialized_end = 5228
    _globals['_JOB']._serialized_start = 5231
    _globals['_JOB']._serialized_end = 5514
    _globals['_JOBCONFIGURATION']._serialized_start = 5517
    _globals['_JOBCONFIGURATION']._serialized_end = 7112
    _globals['_JOBCONFIGURATION_QUERY']._serialized_start = 5946
    _globals['_JOBCONFIGURATION_QUERY']._serialized_end = 6381
    _globals['_JOBCONFIGURATION_LOAD']._serialized_start = 6384
    _globals['_JOBCONFIGURATION_LOAD']._serialized_end = 6647
    _globals['_JOBCONFIGURATION_EXTRACT']._serialized_start = 6649
    _globals['_JOBCONFIGURATION_EXTRACT']._serialized_end = 6751
    _globals['_JOBCONFIGURATION_TABLECOPY']._serialized_start = 6754
    _globals['_JOBCONFIGURATION_TABLECOPY']._serialized_end = 7048
    _globals['_JOBCONFIGURATION_LABELSENTRY']._serialized_start = 4343
    _globals['_JOBCONFIGURATION_LABELSENTRY']._serialized_end = 4388
    _globals['_TABLEDEFINITION']._serialized_start = 7114
    _globals['_TABLEDEFINITION']._serialized_end = 7166
    _globals['_JOBSTATUS']._serialized_start = 7168
    _globals['_JOBSTATUS']._serialized_end = 7276
    _globals['_JOBSTATISTICS']._serialized_start = 7279
    _globals['_JOBSTATISTICS']._serialized_end = 7997
    _globals['_JOBSTATISTICS_RESERVATIONRESOURCEUSAGE']._serialized_start = 7940
    _globals['_JOBSTATISTICS_RESERVATIONRESOURCEUSAGE']._serialized_end = 7997
    _globals['_DATASETNAME']._serialized_start = 7999
    _globals['_DATASETNAME']._serialized_end = 8052
    _globals['_TABLENAME']._serialized_start = 8054
    _globals['_TABLENAME']._serialized_end = 8123
    _globals['_JOBNAME']._serialized_start = 8125
    _globals['_JOBNAME']._serialized_end = 8188
    _globals['_ENCRYPTIONINFO']._serialized_start = 8190
    _globals['_ENCRYPTIONINFO']._serialized_end = 8228