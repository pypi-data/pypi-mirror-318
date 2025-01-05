"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/talent/v4beta1/job_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.talent.v4beta1 import common_pb2 as google_dot_cloud_dot_talent_dot_v4beta1_dot_common__pb2
from .....google.cloud.talent.v4beta1 import filters_pb2 as google_dot_cloud_dot_talent_dot_v4beta1_dot_filters__pb2
from .....google.cloud.talent.v4beta1 import histogram_pb2 as google_dot_cloud_dot_talent_dot_v4beta1_dot_histogram__pb2
from .....google.cloud.talent.v4beta1 import job_pb2 as google_dot_cloud_dot_talent_dot_v4beta1_dot_job__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/talent/v4beta1/job_service.proto\x12\x1bgoogle.cloud.talent.v4beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/talent/v4beta1/common.proto\x1a)google/cloud/talent/v4beta1/filters.proto\x1a+google/cloud/talent/v4beta1/histogram.proto\x1a%google/cloud/talent/v4beta1/job.proto\x1a#google/longrunning/operations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"w\n\x10CreateJobRequest\x12/\n\x06parent\x18\x01 \x01(\tB\x1f\xe0A\x02\xfaA\x19\x12\x17jobs.googleapis.com/Job\x122\n\x03job\x18\x02 \x01(\x0b2 .google.cloud.talent.v4beta1.JobB\x03\xe0A\x02">\n\rGetJobRequest\x12-\n\x04name\x18\x01 \x01(\tB\x1f\xe0A\x02\xfaA\x19\n\x17jobs.googleapis.com/Job"w\n\x10UpdateJobRequest\x122\n\x03job\x18\x01 \x01(\x0b2 .google.cloud.talent.v4beta1.JobB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"A\n\x10DeleteJobRequest\x12-\n\x04name\x18\x01 \x01(\tB\x1f\xe0A\x02\xfaA\x19\n\x17jobs.googleapis.com/Job"^\n\x16BatchDeleteJobsRequest\x12/\n\x06parent\x18\x01 \x01(\tB\x1f\xe0A\x02\xfaA\x19\x12\x17jobs.googleapis.com/Job\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x02"\xb6\x01\n\x0fListJobsRequest\x12/\n\x06parent\x18\x01 \x01(\tB\x1f\xe0A\x02\xfaA\x19\x12\x17jobs.googleapis.com/Job\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x126\n\x08job_view\x18\x05 \x01(\x0e2$.google.cloud.talent.v4beta1.JobView"\x9c\x01\n\x10ListJobsResponse\x12.\n\x04jobs\x18\x01 \x03(\x0b2 .google.cloud.talent.v4beta1.Job\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12?\n\x08metadata\x18\x03 \x01(\x0b2-.google.cloud.talent.v4beta1.ResponseMetadata"\x86\r\n\x11SearchJobsRequest\x12/\n\x06parent\x18\x01 \x01(\tB\x1f\xe0A\x02\xfaA\x19\x12\x17jobs.googleapis.com/Job\x12N\n\x0bsearch_mode\x18\x02 \x01(\x0e29.google.cloud.talent.v4beta1.SearchJobsRequest.SearchMode\x12K\n\x10request_metadata\x18\x03 \x01(\x0b2,.google.cloud.talent.v4beta1.RequestMetadataB\x03\xe0A\x02\x128\n\tjob_query\x18\x04 \x01(\x0b2%.google.cloud.talent.v4beta1.JobQuery\x12\x19\n\x11enable_broadening\x18\x05 \x01(\x08\x12\'\n\x1brequire_precise_result_size\x18\x06 \x01(\x08B\x02\x18\x01\x12F\n\x11histogram_queries\x18\x07 \x03(\x0b2+.google.cloud.talent.v4beta1.HistogramQuery\x126\n\x08job_view\x18\x08 \x01(\x0e2$.google.cloud.talent.v4beta1.JobView\x12\x0e\n\x06offset\x18\t \x01(\x05\x12\x11\n\tpage_size\x18\n \x01(\x05\x12\x12\n\npage_token\x18\x0b \x01(\t\x12\x10\n\x08order_by\x18\x0c \x01(\t\x12b\n\x15diversification_level\x18\r \x01(\x0e2C.google.cloud.talent.v4beta1.SearchJobsRequest.DiversificationLevel\x12]\n\x13custom_ranking_info\x18\x0e \x01(\x0b2@.google.cloud.talent.v4beta1.SearchJobsRequest.CustomRankingInfo\x12\x1d\n\x15disable_keyword_match\x18\x10 \x01(\x08\x12[\n\x12keyword_match_mode\x18\x12 \x01(\x0e2?.google.cloud.talent.v4beta1.SearchJobsRequest.KeywordMatchMode\x12c\n\x13relevance_threshold\x18\x13 \x01(\x0e2A.google.cloud.talent.v4beta1.SearchJobsRequest.RelevanceThresholdB\x03\xe0A\x01\x1a\x9a\x02\n\x11CustomRankingInfo\x12o\n\x10importance_level\x18\x01 \x01(\x0e2P.google.cloud.talent.v4beta1.SearchJobsRequest.CustomRankingInfo.ImportanceLevelB\x03\xe0A\x02\x12\x1f\n\x12ranking_expression\x18\x02 \x01(\tB\x03\xe0A\x02"s\n\x0fImportanceLevel\x12 \n\x1cIMPORTANCE_LEVEL_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\x07\n\x03LOW\x10\x02\x12\x08\n\x04MILD\x10\x03\x12\n\n\x06MEDIUM\x10\x04\x12\x08\n\x04HIGH\x10\x05\x12\x0b\n\x07EXTREME\x10\x06"R\n\nSearchMode\x12\x1b\n\x17SEARCH_MODE_UNSPECIFIED\x10\x00\x12\x0e\n\nJOB_SEARCH\x10\x01\x12\x17\n\x13FEATURED_JOB_SEARCH\x10\x02"W\n\x14DiversificationLevel\x12%\n!DIVERSIFICATION_LEVEL_UNSPECIFIED\x10\x00\x12\x0c\n\x08DISABLED\x10\x01\x12\n\n\x06SIMPLE\x10\x02"\x87\x01\n\x10KeywordMatchMode\x12"\n\x1eKEYWORD_MATCH_MODE_UNSPECIFIED\x10\x00\x12\x1a\n\x16KEYWORD_MATCH_DISABLED\x10\x01\x12\x15\n\x11KEYWORD_MATCH_ALL\x10\x02\x12\x1c\n\x18KEYWORD_MATCH_TITLE_ONLY\x10\x03"d\n\x12RelevanceThreshold\x12#\n\x1fRELEVANCE_THRESHOLD_UNSPECIFIED\x10\x00\x12\n\n\x06LOWEST\x10\x01\x12\x07\n\x03LOW\x10\x02\x12\n\n\x06MEDIUM\x10\x03\x12\x08\n\x04HIGH\x10\x04"\xd7\x06\n\x12SearchJobsResponse\x12R\n\rmatching_jobs\x18\x01 \x03(\x0b2;.google.cloud.talent.v4beta1.SearchJobsResponse.MatchingJob\x12R\n\x17histogram_query_results\x18\x02 \x03(\x0b21.google.cloud.talent.v4beta1.HistogramQueryResult\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\x12?\n\x10location_filters\x18\x04 \x03(\x0b2%.google.cloud.talent.v4beta1.Location\x12\x1c\n\x14estimated_total_size\x18\x05 \x01(\x05\x12\x12\n\ntotal_size\x18\x06 \x01(\x05\x12?\n\x08metadata\x18\x07 \x01(\x0b2-.google.cloud.talent.v4beta1.ResponseMetadata\x12"\n\x1abroadened_query_jobs_count\x18\x08 \x01(\x05\x12I\n\x10spell_correction\x18\t \x01(\x0b2/.google.cloud.talent.v4beta1.SpellingCorrection\x1a\xdc\x01\n\x0bMatchingJob\x12-\n\x03job\x18\x01 \x01(\x0b2 .google.cloud.talent.v4beta1.Job\x12\x13\n\x0bjob_summary\x18\x02 \x01(\t\x12\x19\n\x11job_title_snippet\x18\x03 \x01(\t\x12\x1b\n\x13search_text_snippet\x18\x04 \x01(\t\x12Q\n\x0ccommute_info\x18\x05 \x01(\x0b2;.google.cloud.talent.v4beta1.SearchJobsResponse.CommuteInfo\x1a~\n\x0bCommuteInfo\x12;\n\x0cjob_location\x18\x01 \x01(\x0b2%.google.cloud.talent.v4beta1.Location\x122\n\x0ftravel_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"~\n\x16BatchCreateJobsRequest\x12/\n\x06parent\x18\x01 \x01(\tB\x1f\xe0A\x02\xfaA\x19\x12\x17jobs.googleapis.com/Job\x123\n\x04jobs\x18\x02 \x03(\x0b2 .google.cloud.talent.v4beta1.JobB\x03\xe0A\x02"\xaf\x01\n\x16BatchUpdateJobsRequest\x12/\n\x06parent\x18\x01 \x01(\tB\x1f\xe0A\x02\xfaA\x19\x12\x17jobs.googleapis.com/Job\x123\n\x04jobs\x18\x02 \x03(\x0b2 .google.cloud.talent.v4beta1.JobB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xc4\x01\n\x12JobOperationResult\x12N\n\x0bjob_results\x18\x01 \x03(\x0b29.google.cloud.talent.v4beta1.JobOperationResult.JobResult\x1a^\n\tJobResult\x12-\n\x03job\x18\x01 \x01(\x0b2 .google.cloud.talent.v4beta1.Job\x12"\n\x06status\x18\x02 \x01(\x0b2\x12.google.rpc.Status*v\n\x07JobView\x12\x18\n\x14JOB_VIEW_UNSPECIFIED\x10\x00\x12\x14\n\x10JOB_VIEW_ID_ONLY\x10\x01\x12\x14\n\x10JOB_VIEW_MINIMAL\x10\x02\x12\x12\n\x0eJOB_VIEW_SMALL\x10\x03\x12\x11\n\rJOB_VIEW_FULL\x10\x042\xce\x12\n\nJobService\x12\xc9\x01\n\tCreateJob\x12-.google.cloud.talent.v4beta1.CreateJobRequest\x1a .google.cloud.talent.v4beta1.Job"k\xdaA\nparent,job\x82\xd3\xe4\x93\x02X"+/v4beta1/{parent=projects/*/tenants/*}/jobs:\x01*Z&"!/v4beta1/{parent=projects/*}/jobs:\x01*\x12\x9b\x02\n\x0fBatchCreateJobs\x123.google.cloud.talent.v4beta1.BatchCreateJobsRequest\x1a\x1d.google.longrunning.Operation"\xb3\x01\xcaA,\n\x12JobOperationResult\x12\x16BatchOperationMetadata\xdaA\x0bparent,jobs\x82\xd3\xe4\x93\x02p"7/v4beta1/{parent=projects/*/tenants/*}/jobs:batchCreate:\x01*Z2"-/v4beta1/{parent=projects/*}/jobs:batchCreate:\x01*\x12\xb7\x01\n\x06GetJob\x12*.google.cloud.talent.v4beta1.GetJobRequest\x1a .google.cloud.talent.v4beta1.Job"_\xdaA\x04name\x82\xd3\xe4\x93\x02R\x12+/v4beta1/{name=projects/*/tenants/*/jobs/*}Z#\x12!/v4beta1/{name=projects/*/jobs/*}\x12\xca\x01\n\tUpdateJob\x12-.google.cloud.talent.v4beta1.UpdateJobRequest\x1a .google.cloud.talent.v4beta1.Job"l\xdaA\x03job\x82\xd3\xe4\x93\x02`2//v4beta1/{job.name=projects/*/tenants/*/jobs/*}:\x01*Z*2%/v4beta1/{job.name=projects/*/jobs/*}:\x01*\x12\x9b\x02\n\x0fBatchUpdateJobs\x123.google.cloud.talent.v4beta1.BatchUpdateJobsRequest\x1a\x1d.google.longrunning.Operation"\xb3\x01\xcaA,\n\x12JobOperationResult\x12\x16BatchOperationMetadata\xdaA\x0bparent,jobs\x82\xd3\xe4\x93\x02p"7/v4beta1/{parent=projects/*/tenants/*}/jobs:batchUpdate:\x01*Z2"-/v4beta1/{parent=projects/*}/jobs:batchUpdate:\x01*\x12\xb3\x01\n\tDeleteJob\x12-.google.cloud.talent.v4beta1.DeleteJobRequest\x1a\x16.google.protobuf.Empty"_\xdaA\x04name\x82\xd3\xe4\x93\x02R*+/v4beta1/{name=projects/*/tenants/*/jobs/*}Z#*!/v4beta1/{name=projects/*/jobs/*}\x12\xe4\x01\n\x0fBatchDeleteJobs\x123.google.cloud.talent.v4beta1.BatchDeleteJobsRequest\x1a\x16.google.protobuf.Empty"\x83\x01\xdaA\rparent,filter\x82\xd3\xe4\x93\x02m"7/v4beta1/{parent=projects/*/tenants/*}/jobs:batchDelete:\x01*Z/"-/v4beta1/{parent=projects/*}/jobs:batchDelete\x12\xd1\x01\n\x08ListJobs\x12,.google.cloud.talent.v4beta1.ListJobsRequest\x1a-.google.cloud.talent.v4beta1.ListJobsResponse"h\xdaA\rparent,filter\x82\xd3\xe4\x93\x02R\x12+/v4beta1/{parent=projects/*/tenants/*}/jobsZ#\x12!/v4beta1/{parent=projects/*}/jobs\x12\xdb\x01\n\nSearchJobs\x12..google.cloud.talent.v4beta1.SearchJobsRequest\x1a/.google.cloud.talent.v4beta1.SearchJobsResponse"l\x82\xd3\xe4\x93\x02f"2/v4beta1/{parent=projects/*/tenants/*}/jobs:search:\x01*Z-"(/v4beta1/{parent=projects/*}/jobs:search:\x01*\x12\xf3\x01\n\x12SearchJobsForAlert\x12..google.cloud.talent.v4beta1.SearchJobsRequest\x1a/.google.cloud.talent.v4beta1.SearchJobsResponse"|\x82\xd3\xe4\x93\x02v":/v4beta1/{parent=projects/*/tenants/*}/jobs:searchForAlert:\x01*Z5"0/v4beta1/{parent=projects/*}/jobs:searchForAlert:\x01*\x1al\xcaA\x13jobs.googleapis.com\xd2AShttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobsBs\n\x1fcom.google.cloud.talent.v4beta1B\x0fJobServiceProtoP\x01Z7cloud.google.com/go/talent/apiv4beta1/talentpb;talentpb\xa2\x02\x03CTSb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.talent.v4beta1.job_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.talent.v4beta1B\x0fJobServiceProtoP\x01Z7cloud.google.com/go/talent/apiv4beta1/talentpb;talentpb\xa2\x02\x03CTS'
    _globals['_CREATEJOBREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEJOBREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x19\x12\x17jobs.googleapis.com/Job'
    _globals['_CREATEJOBREQUEST'].fields_by_name['job']._loaded_options = None
    _globals['_CREATEJOBREQUEST'].fields_by_name['job']._serialized_options = b'\xe0A\x02'
    _globals['_GETJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x19\n\x17jobs.googleapis.com/Job'
    _globals['_UPDATEJOBREQUEST'].fields_by_name['job']._loaded_options = None
    _globals['_UPDATEJOBREQUEST'].fields_by_name['job']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x19\n\x17jobs.googleapis.com/Job'
    _globals['_BATCHDELETEJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHDELETEJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x19\x12\x17jobs.googleapis.com/Job'
    _globals['_BATCHDELETEJOBSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_BATCHDELETEJOBSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_LISTJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x19\x12\x17jobs.googleapis.com/Job'
    _globals['_LISTJOBSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTJOBSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHJOBSREQUEST_CUSTOMRANKINGINFO'].fields_by_name['importance_level']._loaded_options = None
    _globals['_SEARCHJOBSREQUEST_CUSTOMRANKINGINFO'].fields_by_name['importance_level']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHJOBSREQUEST_CUSTOMRANKINGINFO'].fields_by_name['ranking_expression']._loaded_options = None
    _globals['_SEARCHJOBSREQUEST_CUSTOMRANKINGINFO'].fields_by_name['ranking_expression']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_SEARCHJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x19\x12\x17jobs.googleapis.com/Job'
    _globals['_SEARCHJOBSREQUEST'].fields_by_name['request_metadata']._loaded_options = None
    _globals['_SEARCHJOBSREQUEST'].fields_by_name['request_metadata']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHJOBSREQUEST'].fields_by_name['require_precise_result_size']._loaded_options = None
    _globals['_SEARCHJOBSREQUEST'].fields_by_name['require_precise_result_size']._serialized_options = b'\x18\x01'
    _globals['_SEARCHJOBSREQUEST'].fields_by_name['relevance_threshold']._loaded_options = None
    _globals['_SEARCHJOBSREQUEST'].fields_by_name['relevance_threshold']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHCREATEJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHCREATEJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x19\x12\x17jobs.googleapis.com/Job'
    _globals['_BATCHCREATEJOBSREQUEST'].fields_by_name['jobs']._loaded_options = None
    _globals['_BATCHCREATEJOBSREQUEST'].fields_by_name['jobs']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHUPDATEJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHUPDATEJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x19\x12\x17jobs.googleapis.com/Job'
    _globals['_BATCHUPDATEJOBSREQUEST'].fields_by_name['jobs']._loaded_options = None
    _globals['_BATCHUPDATEJOBSREQUEST'].fields_by_name['jobs']._serialized_options = b'\xe0A\x02'
    _globals['_JOBSERVICE']._loaded_options = None
    _globals['_JOBSERVICE']._serialized_options = b'\xcaA\x13jobs.googleapis.com\xd2AShttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobs'
    _globals['_JOBSERVICE'].methods_by_name['CreateJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['CreateJob']._serialized_options = b'\xdaA\nparent,job\x82\xd3\xe4\x93\x02X"+/v4beta1/{parent=projects/*/tenants/*}/jobs:\x01*Z&"!/v4beta1/{parent=projects/*}/jobs:\x01*'
    _globals['_JOBSERVICE'].methods_by_name['BatchCreateJobs']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['BatchCreateJobs']._serialized_options = b'\xcaA,\n\x12JobOperationResult\x12\x16BatchOperationMetadata\xdaA\x0bparent,jobs\x82\xd3\xe4\x93\x02p"7/v4beta1/{parent=projects/*/tenants/*}/jobs:batchCreate:\x01*Z2"-/v4beta1/{parent=projects/*}/jobs:batchCreate:\x01*'
    _globals['_JOBSERVICE'].methods_by_name['GetJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['GetJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02R\x12+/v4beta1/{name=projects/*/tenants/*/jobs/*}Z#\x12!/v4beta1/{name=projects/*/jobs/*}'
    _globals['_JOBSERVICE'].methods_by_name['UpdateJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['UpdateJob']._serialized_options = b'\xdaA\x03job\x82\xd3\xe4\x93\x02`2//v4beta1/{job.name=projects/*/tenants/*/jobs/*}:\x01*Z*2%/v4beta1/{job.name=projects/*/jobs/*}:\x01*'
    _globals['_JOBSERVICE'].methods_by_name['BatchUpdateJobs']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['BatchUpdateJobs']._serialized_options = b'\xcaA,\n\x12JobOperationResult\x12\x16BatchOperationMetadata\xdaA\x0bparent,jobs\x82\xd3\xe4\x93\x02p"7/v4beta1/{parent=projects/*/tenants/*}/jobs:batchUpdate:\x01*Z2"-/v4beta1/{parent=projects/*}/jobs:batchUpdate:\x01*'
    _globals['_JOBSERVICE'].methods_by_name['DeleteJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['DeleteJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02R*+/v4beta1/{name=projects/*/tenants/*/jobs/*}Z#*!/v4beta1/{name=projects/*/jobs/*}'
    _globals['_JOBSERVICE'].methods_by_name['BatchDeleteJobs']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['BatchDeleteJobs']._serialized_options = b'\xdaA\rparent,filter\x82\xd3\xe4\x93\x02m"7/v4beta1/{parent=projects/*/tenants/*}/jobs:batchDelete:\x01*Z/"-/v4beta1/{parent=projects/*}/jobs:batchDelete'
    _globals['_JOBSERVICE'].methods_by_name['ListJobs']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['ListJobs']._serialized_options = b'\xdaA\rparent,filter\x82\xd3\xe4\x93\x02R\x12+/v4beta1/{parent=projects/*/tenants/*}/jobsZ#\x12!/v4beta1/{parent=projects/*}/jobs'
    _globals['_JOBSERVICE'].methods_by_name['SearchJobs']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['SearchJobs']._serialized_options = b'\x82\xd3\xe4\x93\x02f"2/v4beta1/{parent=projects/*/tenants/*}/jobs:search:\x01*Z-"(/v4beta1/{parent=projects/*}/jobs:search:\x01*'
    _globals['_JOBSERVICE'].methods_by_name['SearchJobsForAlert']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['SearchJobsForAlert']._serialized_options = b'\x82\xd3\xe4\x93\x02v":/v4beta1/{parent=projects/*/tenants/*}/jobs:searchForAlert:\x01*Z5"0/v4beta1/{parent=projects/*}/jobs:searchForAlert:\x01*'
    _globals['_JOBVIEW']._serialized_start = 4368
    _globals['_JOBVIEW']._serialized_end = 4486
    _globals['_CREATEJOBREQUEST']._serialized_start = 519
    _globals['_CREATEJOBREQUEST']._serialized_end = 638
    _globals['_GETJOBREQUEST']._serialized_start = 640
    _globals['_GETJOBREQUEST']._serialized_end = 702
    _globals['_UPDATEJOBREQUEST']._serialized_start = 704
    _globals['_UPDATEJOBREQUEST']._serialized_end = 823
    _globals['_DELETEJOBREQUEST']._serialized_start = 825
    _globals['_DELETEJOBREQUEST']._serialized_end = 890
    _globals['_BATCHDELETEJOBSREQUEST']._serialized_start = 892
    _globals['_BATCHDELETEJOBSREQUEST']._serialized_end = 986
    _globals['_LISTJOBSREQUEST']._serialized_start = 989
    _globals['_LISTJOBSREQUEST']._serialized_end = 1171
    _globals['_LISTJOBSRESPONSE']._serialized_start = 1174
    _globals['_LISTJOBSRESPONSE']._serialized_end = 1330
    _globals['_SEARCHJOBSREQUEST']._serialized_start = 1333
    _globals['_SEARCHJOBSREQUEST']._serialized_end = 3003
    _globals['_SEARCHJOBSREQUEST_CUSTOMRANKINGINFO']._serialized_start = 2308
    _globals['_SEARCHJOBSREQUEST_CUSTOMRANKINGINFO']._serialized_end = 2590
    _globals['_SEARCHJOBSREQUEST_CUSTOMRANKINGINFO_IMPORTANCELEVEL']._serialized_start = 2475
    _globals['_SEARCHJOBSREQUEST_CUSTOMRANKINGINFO_IMPORTANCELEVEL']._serialized_end = 2590
    _globals['_SEARCHJOBSREQUEST_SEARCHMODE']._serialized_start = 2592
    _globals['_SEARCHJOBSREQUEST_SEARCHMODE']._serialized_end = 2674
    _globals['_SEARCHJOBSREQUEST_DIVERSIFICATIONLEVEL']._serialized_start = 2676
    _globals['_SEARCHJOBSREQUEST_DIVERSIFICATIONLEVEL']._serialized_end = 2763
    _globals['_SEARCHJOBSREQUEST_KEYWORDMATCHMODE']._serialized_start = 2766
    _globals['_SEARCHJOBSREQUEST_KEYWORDMATCHMODE']._serialized_end = 2901
    _globals['_SEARCHJOBSREQUEST_RELEVANCETHRESHOLD']._serialized_start = 2903
    _globals['_SEARCHJOBSREQUEST_RELEVANCETHRESHOLD']._serialized_end = 3003
    _globals['_SEARCHJOBSRESPONSE']._serialized_start = 3006
    _globals['_SEARCHJOBSRESPONSE']._serialized_end = 3861
    _globals['_SEARCHJOBSRESPONSE_MATCHINGJOB']._serialized_start = 3513
    _globals['_SEARCHJOBSRESPONSE_MATCHINGJOB']._serialized_end = 3733
    _globals['_SEARCHJOBSRESPONSE_COMMUTEINFO']._serialized_start = 3735
    _globals['_SEARCHJOBSRESPONSE_COMMUTEINFO']._serialized_end = 3861
    _globals['_BATCHCREATEJOBSREQUEST']._serialized_start = 3863
    _globals['_BATCHCREATEJOBSREQUEST']._serialized_end = 3989
    _globals['_BATCHUPDATEJOBSREQUEST']._serialized_start = 3992
    _globals['_BATCHUPDATEJOBSREQUEST']._serialized_end = 4167
    _globals['_JOBOPERATIONRESULT']._serialized_start = 4170
    _globals['_JOBOPERATIONRESULT']._serialized_end = 4366
    _globals['_JOBOPERATIONRESULT_JOBRESULT']._serialized_start = 4272
    _globals['_JOBOPERATIONRESULT_JOBRESULT']._serialized_end = 4366
    _globals['_JOBSERVICE']._serialized_start = 4489
    _globals['_JOBSERVICE']._serialized_end = 6871