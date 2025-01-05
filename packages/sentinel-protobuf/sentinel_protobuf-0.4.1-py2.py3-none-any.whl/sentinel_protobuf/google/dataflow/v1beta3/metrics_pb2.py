"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/dataflow/v1beta3/metrics.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/dataflow/v1beta3/metrics.proto\x12\x17google.dataflow.v1beta3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb1\x01\n\x14MetricStructuredName\x12\x0e\n\x06origin\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12K\n\x07context\x18\x03 \x03(\x0b2:.google.dataflow.v1beta3.MetricStructuredName.ContextEntry\x1a.\n\x0cContextEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xc0\x03\n\x0cMetricUpdate\x12;\n\x04name\x18\x01 \x01(\x0b2-.google.dataflow.v1beta3.MetricStructuredName\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12\x12\n\ncumulative\x18\x03 \x01(\x08\x12&\n\x06scalar\x18\x04 \x01(\x0b2\x16.google.protobuf.Value\x12(\n\x08mean_sum\x18\x05 \x01(\x0b2\x16.google.protobuf.Value\x12*\n\nmean_count\x18\x06 \x01(\x0b2\x16.google.protobuf.Value\x12#\n\x03set\x18\x07 \x01(\x0b2\x16.google.protobuf.Value\x12,\n\x0cdistribution\x18\x0b \x01(\x0b2\x16.google.protobuf.Value\x12%\n\x05gauge\x18\x0c \x01(\x0b2\x16.google.protobuf.Value\x12(\n\x08internal\x18\x08 \x01(\x0b2\x16.google.protobuf.Value\x12/\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.Timestamp"|\n\x14GetJobMetricsRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0e\n\x06job_id\x18\x02 \x01(\t\x12.\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x10\n\x08location\x18\x04 \x01(\t"u\n\nJobMetrics\x12/\n\x0bmetric_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x126\n\x07metrics\x18\x02 \x03(\x0b2%.google.dataflow.v1beta3.MetricUpdate"|\n\x1dGetJobExecutionDetailsRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0e\n\x06job_id\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t"\xb8\x01\n\x12ProgressTimeseries\x12\x18\n\x10current_progress\x18\x01 \x01(\x01\x12F\n\x0bdata_points\x18\x02 \x03(\x0b21.google.dataflow.v1beta3.ProgressTimeseries.Point\x1a@\n\x05Point\x12(\n\x04time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\r\n\x05value\x18\x02 \x01(\x01"\xad\x02\n\x0cStageSummary\x12\x10\n\x08stage_id\x18\x01 \x01(\t\x126\n\x05state\x18\x02 \x01(\x0e2\'.google.dataflow.v1beta3.ExecutionState\x12.\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12=\n\x08progress\x18\x05 \x01(\x0b2+.google.dataflow.v1beta3.ProgressTimeseries\x126\n\x07metrics\x18\x06 \x03(\x0b2%.google.dataflow.v1beta3.MetricUpdate"e\n\x13JobExecutionDetails\x125\n\x06stages\x18\x01 \x03(\x0b2%.google.dataflow.v1beta3.StageSummary\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xee\x01\n\x1fGetStageExecutionDetailsRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0e\n\x06job_id\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x10\n\x08stage_id\x18\x04 \x01(\t\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t\x12.\n\nstart_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xc3\x02\n\x0fWorkItemDetails\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x12\n\nattempt_id\x18\x02 \x01(\t\x12.\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x126\n\x05state\x18\x05 \x01(\x0e2\'.google.dataflow.v1beta3.ExecutionState\x12=\n\x08progress\x18\x06 \x01(\x0b2+.google.dataflow.v1beta3.ProgressTimeseries\x126\n\x07metrics\x18\x07 \x03(\x0b2%.google.dataflow.v1beta3.MetricUpdate"b\n\rWorkerDetails\x12\x13\n\x0bworker_name\x18\x01 \x01(\t\x12<\n\nwork_items\x18\x02 \x03(\x0b2(.google.dataflow.v1beta3.WorkItemDetails"i\n\x15StageExecutionDetails\x127\n\x07workers\x18\x01 \x03(\x0b2&.google.dataflow.v1beta3.WorkerDetails\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t*\xc5\x01\n\x0eExecutionState\x12\x1b\n\x17EXECUTION_STATE_UNKNOWN\x10\x00\x12\x1f\n\x1bEXECUTION_STATE_NOT_STARTED\x10\x01\x12\x1b\n\x17EXECUTION_STATE_RUNNING\x10\x02\x12\x1d\n\x19EXECUTION_STATE_SUCCEEDED\x10\x03\x12\x1a\n\x16EXECUTION_STATE_FAILED\x10\x04\x12\x1d\n\x19EXECUTION_STATE_CANCELLED\x10\x052\x9f\x07\n\x0eMetricsV1Beta3\x12\xe9\x01\n\rGetJobMetrics\x12-.google.dataflow.v1beta3.GetJobMetricsRequest\x1a#.google.dataflow.v1beta3.JobMetrics"\x83\x01\x82\xd3\xe4\x93\x02}\x12F/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/metricsZ3\x121/v1b3/projects/{project_id}/jobs/{job_id}/metrics\x12\xd7\x01\n\x16GetJobExecutionDetails\x126.google.dataflow.v1beta3.GetJobExecutionDetailsRequest\x1a,.google.dataflow.v1beta3.JobExecutionDetails"W\x82\xd3\xe4\x93\x02Q\x12O/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/executionDetails\x12\xef\x01\n\x18GetStageExecutionDetails\x128.google.dataflow.v1beta3.GetStageExecutionDetailsRequest\x1a..google.dataflow.v1beta3.StageExecutionDetails"i\x82\xd3\xe4\x93\x02c\x12a/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/stages/{stage_id}/executionDetails\x1a\xd4\x01\xcaA\x17dataflow.googleapis.com\xd2A\xb6\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/compute.readonly,https://www.googleapis.com/auth/userinfo.emailB\xcf\x01\n\x1bcom.google.dataflow.v1beta3B\x0cMetricsProtoP\x01Z=cloud.google.com/go/dataflow/apiv1beta3/dataflowpb;dataflowpb\xaa\x02\x1dGoogle.Cloud.Dataflow.V1Beta3\xca\x02\x1dGoogle\\Cloud\\Dataflow\\V1beta3\xea\x02 Google::Cloud::Dataflow::V1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.dataflow.v1beta3.metrics_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.dataflow.v1beta3B\x0cMetricsProtoP\x01Z=cloud.google.com/go/dataflow/apiv1beta3/dataflowpb;dataflowpb\xaa\x02\x1dGoogle.Cloud.Dataflow.V1Beta3\xca\x02\x1dGoogle\\Cloud\\Dataflow\\V1beta3\xea\x02 Google::Cloud::Dataflow::V1beta3'
    _globals['_METRICSTRUCTUREDNAME_CONTEXTENTRY']._loaded_options = None
    _globals['_METRICSTRUCTUREDNAME_CONTEXTENTRY']._serialized_options = b'8\x01'
    _globals['_METRICSV1BETA3']._loaded_options = None
    _globals['_METRICSV1BETA3']._serialized_options = b'\xcaA\x17dataflow.googleapis.com\xd2A\xb6\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/compute.readonly,https://www.googleapis.com/auth/userinfo.email'
    _globals['_METRICSV1BETA3'].methods_by_name['GetJobMetrics']._loaded_options = None
    _globals['_METRICSV1BETA3'].methods_by_name['GetJobMetrics']._serialized_options = b'\x82\xd3\xe4\x93\x02}\x12F/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/metricsZ3\x121/v1b3/projects/{project_id}/jobs/{job_id}/metrics'
    _globals['_METRICSV1BETA3'].methods_by_name['GetJobExecutionDetails']._loaded_options = None
    _globals['_METRICSV1BETA3'].methods_by_name['GetJobExecutionDetails']._serialized_options = b'\x82\xd3\xe4\x93\x02Q\x12O/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/executionDetails'
    _globals['_METRICSV1BETA3'].methods_by_name['GetStageExecutionDetails']._loaded_options = None
    _globals['_METRICSV1BETA3'].methods_by_name['GetStageExecutionDetails']._serialized_options = b'\x82\xd3\xe4\x93\x02c\x12a/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/stages/{stage_id}/executionDetails'
    _globals['_EXECUTIONSTATE']._serialized_start = 2555
    _globals['_EXECUTIONSTATE']._serialized_end = 2752
    _globals['_METRICSTRUCTUREDNAME']._serialized_start = 185
    _globals['_METRICSTRUCTUREDNAME']._serialized_end = 362
    _globals['_METRICSTRUCTUREDNAME_CONTEXTENTRY']._serialized_start = 316
    _globals['_METRICSTRUCTUREDNAME_CONTEXTENTRY']._serialized_end = 362
    _globals['_METRICUPDATE']._serialized_start = 365
    _globals['_METRICUPDATE']._serialized_end = 813
    _globals['_GETJOBMETRICSREQUEST']._serialized_start = 815
    _globals['_GETJOBMETRICSREQUEST']._serialized_end = 939
    _globals['_JOBMETRICS']._serialized_start = 941
    _globals['_JOBMETRICS']._serialized_end = 1058
    _globals['_GETJOBEXECUTIONDETAILSREQUEST']._serialized_start = 1060
    _globals['_GETJOBEXECUTIONDETAILSREQUEST']._serialized_end = 1184
    _globals['_PROGRESSTIMESERIES']._serialized_start = 1187
    _globals['_PROGRESSTIMESERIES']._serialized_end = 1371
    _globals['_PROGRESSTIMESERIES_POINT']._serialized_start = 1307
    _globals['_PROGRESSTIMESERIES_POINT']._serialized_end = 1371
    _globals['_STAGESUMMARY']._serialized_start = 1374
    _globals['_STAGESUMMARY']._serialized_end = 1675
    _globals['_JOBEXECUTIONDETAILS']._serialized_start = 1677
    _globals['_JOBEXECUTIONDETAILS']._serialized_end = 1778
    _globals['_GETSTAGEEXECUTIONDETAILSREQUEST']._serialized_start = 1781
    _globals['_GETSTAGEEXECUTIONDETAILSREQUEST']._serialized_end = 2019
    _globals['_WORKITEMDETAILS']._serialized_start = 2022
    _globals['_WORKITEMDETAILS']._serialized_end = 2345
    _globals['_WORKERDETAILS']._serialized_start = 2347
    _globals['_WORKERDETAILS']._serialized_end = 2445
    _globals['_STAGEEXECUTIONDETAILS']._serialized_start = 2447
    _globals['_STAGEEXECUTIONDETAILS']._serialized_end = 2552
    _globals['_METRICSV1BETA3']._serialized_start = 2755
    _globals['_METRICSV1BETA3']._serialized_end = 3682