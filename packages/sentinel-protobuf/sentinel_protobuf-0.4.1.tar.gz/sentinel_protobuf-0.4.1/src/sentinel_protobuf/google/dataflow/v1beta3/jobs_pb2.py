"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/dataflow/v1beta3/jobs.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from ....google.dataflow.v1beta3 import environment_pb2 as google_dot_dataflow_dot_v1beta3_dot_environment__pb2
from ....google.dataflow.v1beta3 import snapshots_pb2 as google_dot_dataflow_dot_v1beta3_dot_snapshots__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/dataflow/v1beta3/jobs.proto\x12\x17google.dataflow.v1beta3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a)google/dataflow/v1beta3/environment.proto\x1a\'google/dataflow/v1beta3/snapshots.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xae\t\n\x03Job\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12.\n\x04type\x18\x04 \x01(\x0e2 .google.dataflow.v1beta3.JobType\x129\n\x0benvironment\x18\x05 \x01(\x0b2$.google.dataflow.v1beta3.Environment\x12,\n\x05steps\x18\x06 \x03(\x0b2\x1d.google.dataflow.v1beta3.Step\x12\x16\n\x0esteps_location\x18\x18 \x01(\t\x128\n\rcurrent_state\x18\x07 \x01(\x0e2!.google.dataflow.v1beta3.JobState\x126\n\x12current_state_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12:\n\x0frequested_state\x18\t \x01(\x0e2!.google.dataflow.v1beta3.JobState\x12A\n\x0eexecution_info\x18\n \x01(\x0b2).google.dataflow.v1beta3.JobExecutionInfo\x12/\n\x0bcreate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x16\n\x0ereplace_job_id\x18\x0c \x01(\t\x12V\n\x16transform_name_mapping\x18\r \x03(\x0b26.google.dataflow.v1beta3.Job.TransformNameMappingEntry\x12\x19\n\x11client_request_id\x18\x0e \x01(\t\x12\x1a\n\x12replaced_by_job_id\x18\x0f \x01(\t\x12\x12\n\ntemp_files\x18\x10 \x03(\t\x128\n\x06labels\x18\x11 \x03(\x0b2(.google.dataflow.v1beta3.Job.LabelsEntry\x12\x10\n\x08location\x18\x12 \x01(\t\x12J\n\x14pipeline_description\x18\x13 \x01(\x0b2,.google.dataflow.v1beta3.PipelineDescription\x12B\n\x0cstage_states\x18\x14 \x03(\x0b2,.google.dataflow.v1beta3.ExecutionStageState\x12:\n\x0cjob_metadata\x18\x15 \x01(\x0b2$.google.dataflow.v1beta3.JobMetadata\x12.\n\nstart_time\x18\x16 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12 \n\x18created_from_snapshot_id\x18\x17 \x01(\t\x12\x15\n\rsatisfies_pzs\x18\x19 \x01(\x08\x1a;\n\x19TransformNameMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01";\n\x12DatastoreIODetails\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t"6\n\x0fPubSubIODetails\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x14\n\x0csubscription\x18\x02 \x01(\t"%\n\rFileIODetails\x12\x14\n\x0cfile_pattern\x18\x01 \x01(\t"N\n\x11BigTableIODetails\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x13\n\x0binstance_id\x18\x02 \x01(\t\x12\x10\n\x08table_id\x18\x03 \x01(\t"V\n\x11BigQueryIODetails\x12\r\n\x05table\x18\x01 \x01(\t\x12\x0f\n\x07dataset\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x03 \x01(\t\x12\r\n\x05query\x18\x04 \x01(\t"P\n\x10SpannerIODetails\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x13\n\x0binstance_id\x18\x02 \x01(\t\x12\x13\n\x0bdatabase_id\x18\x03 \x01(\t"\xe9\x01\n\nSdkVersion\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x1c\n\x14version_display_name\x18\x02 \x01(\t\x12P\n\x12sdk_support_status\x18\x03 \x01(\x0e24.google.dataflow.v1beta3.SdkVersion.SdkSupportStatus"Z\n\x10SdkSupportStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tSUPPORTED\x10\x01\x12\t\n\x05STALE\x10\x02\x12\x0e\n\nDEPRECATED\x10\x03\x12\x0f\n\x0bUNSUPPORTED\x10\x04"\xe0\x03\n\x0bJobMetadata\x128\n\x0bsdk_version\x18\x01 \x01(\x0b2#.google.dataflow.v1beta3.SdkVersion\x12B\n\x0fspanner_details\x18\x02 \x03(\x0b2).google.dataflow.v1beta3.SpannerIODetails\x12D\n\x10bigquery_details\x18\x03 \x03(\x0b2*.google.dataflow.v1beta3.BigQueryIODetails\x12E\n\x11big_table_details\x18\x04 \x03(\x0b2*.google.dataflow.v1beta3.BigTableIODetails\x12@\n\x0epubsub_details\x18\x05 \x03(\x0b2(.google.dataflow.v1beta3.PubSubIODetails\x12<\n\x0cfile_details\x18\x06 \x03(\x0b2&.google.dataflow.v1beta3.FileIODetails\x12F\n\x11datastore_details\x18\x07 \x03(\x0b2+.google.dataflow.v1beta3.DatastoreIODetails"\xad\x01\n\x13ExecutionStageState\x12\x1c\n\x14execution_stage_name\x18\x01 \x01(\t\x12@\n\x15execution_stage_state\x18\x02 \x01(\x0e2!.google.dataflow.v1beta3.JobState\x126\n\x12current_state_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xf3\x01\n\x13PipelineDescription\x12N\n\x1boriginal_pipeline_transform\x18\x01 \x03(\x0b2).google.dataflow.v1beta3.TransformSummary\x12P\n\x18execution_pipeline_stage\x18\x02 \x03(\x0b2..google.dataflow.v1beta3.ExecutionStageSummary\x12:\n\x0cdisplay_data\x18\x03 \x03(\x0b2$.google.dataflow.v1beta3.DisplayData"\xd8\x01\n\x10TransformSummary\x12/\n\x04kind\x18\x01 \x01(\x0e2!.google.dataflow.v1beta3.KindType\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12:\n\x0cdisplay_data\x18\x04 \x03(\x0b2$.google.dataflow.v1beta3.DisplayData\x12\x1e\n\x16output_collection_name\x18\x05 \x03(\t\x12\x1d\n\x15input_collection_name\x18\x06 \x03(\t"\xfc\x05\n\x15ExecutionStageSummary\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12/\n\x04kind\x18\x03 \x01(\x0e2!.google.dataflow.v1beta3.KindType\x12P\n\x0cinput_source\x18\x04 \x03(\x0b2:.google.dataflow.v1beta3.ExecutionStageSummary.StageSource\x12Q\n\routput_source\x18\x05 \x03(\x0b2:.google.dataflow.v1beta3.ExecutionStageSummary.StageSource\x12\x1a\n\x12prerequisite_stage\x18\x08 \x03(\t\x12^\n\x13component_transform\x18\x06 \x03(\x0b2A.google.dataflow.v1beta3.ExecutionStageSummary.ComponentTransform\x12X\n\x10component_source\x18\x07 \x03(\x0b2>.google.dataflow.v1beta3.ExecutionStageSummary.ComponentSource\x1al\n\x0bStageSource\x12\x11\n\tuser_name\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12(\n original_transform_or_collection\x18\x03 \x01(\t\x12\x12\n\nsize_bytes\x18\x04 \x01(\x03\x1aQ\n\x12ComponentTransform\x12\x11\n\tuser_name\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1a\n\x12original_transform\x18\x03 \x01(\t\x1a\\\n\x0fComponentSource\x12\x11\n\tuser_name\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12(\n original_transform_or_collection\x18\x03 \x01(\t"\xcc\x02\n\x0bDisplayData\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x13\n\tstr_value\x18\x04 \x01(\tH\x00\x12\x15\n\x0bint64_value\x18\x05 \x01(\x03H\x00\x12\x15\n\x0bfloat_value\x18\x06 \x01(\x02H\x00\x12\x1a\n\x10java_class_value\x18\x07 \x01(\tH\x00\x125\n\x0ftimestamp_value\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x123\n\x0eduration_value\x18\t \x01(\x0b2\x19.google.protobuf.DurationH\x00\x12\x14\n\nbool_value\x18\n \x01(\x08H\x00\x12\x17\n\x0fshort_str_value\x18\x0b \x01(\t\x12\x0b\n\x03url\x18\x0c \x01(\t\x12\r\n\x05label\x18\r \x01(\tB\x07\n\x05Value"O\n\x04Step\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12+\n\nproperties\x18\x03 \x01(\x0b2\x17.google.protobuf.Struct"\xb8\x01\n\x10JobExecutionInfo\x12E\n\x06stages\x18\x01 \x03(\x0b25.google.dataflow.v1beta3.JobExecutionInfo.StagesEntry\x1a]\n\x0bStagesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12=\n\x05value\x18\x02 \x01(\x0b2..google.dataflow.v1beta3.JobExecutionStageInfo:\x028\x01"*\n\x15JobExecutionStageInfo\x12\x11\n\tstep_name\x18\x01 \x03(\t"\xab\x01\n\x10CreateJobRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12)\n\x03job\x18\x02 \x01(\x0b2\x1c.google.dataflow.v1beta3.Job\x12.\n\x04view\x18\x03 \x01(\x0e2 .google.dataflow.v1beta3.JobView\x12\x16\n\x0ereplace_job_id\x18\x04 \x01(\t\x12\x10\n\x08location\x18\x05 \x01(\t"u\n\rGetJobRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0e\n\x06job_id\x18\x02 \x01(\t\x12.\n\x04view\x18\x03 \x01(\x0e2 .google.dataflow.v1beta3.JobView\x12\x10\n\x08location\x18\x04 \x01(\t"s\n\x10UpdateJobRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0e\n\x06job_id\x18\x02 \x01(\t\x12)\n\x03job\x18\x03 \x01(\x0b2\x1c.google.dataflow.v1beta3.Job\x12\x10\n\x08location\x18\x04 \x01(\t"\x8f\x02\n\x0fListJobsRequest\x12?\n\x06filter\x18\x05 \x01(\x0e2/.google.dataflow.v1beta3.ListJobsRequest.Filter\x12\x12\n\nproject_id\x18\x01 \x01(\t\x122\n\x04view\x18\x02 \x01(\x0e2 .google.dataflow.v1beta3.JobViewB\x02\x18\x01\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08location\x18\x11 \x01(\t":\n\x06Filter\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03ALL\x10\x01\x12\x0e\n\nTERMINATED\x10\x02\x12\n\n\x06ACTIVE\x10\x03"\x1e\n\x0eFailedLocation\x12\x0c\n\x04name\x18\x01 \x01(\t"\x99\x01\n\x10ListJobsResponse\x12*\n\x04jobs\x18\x01 \x03(\x0b2\x1c.google.dataflow.v1beta3.Job\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12@\n\x0ffailed_location\x18\x03 \x03(\x0b2\'.google.dataflow.v1beta3.FailedLocation"\xa1\x01\n\x12SnapshotJobRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0e\n\x06job_id\x18\x02 \x01(\t\x12&\n\x03ttl\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x12\x10\n\x08location\x18\x04 \x01(\t\x12\x18\n\x10snapshot_sources\x18\x05 \x01(\x08\x12\x13\n\x0bdescription\x18\x06 \x01(\t",\n\x16CheckActiveJobsRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t"4\n\x17CheckActiveJobsResponse\x12\x19\n\x11active_jobs_exist\x18\x01 \x01(\x08*\xae\x01\n\x08KindType\x12\x10\n\x0cUNKNOWN_KIND\x10\x00\x12\x0f\n\x0bPAR_DO_KIND\x10\x01\x12\x15\n\x11GROUP_BY_KEY_KIND\x10\x02\x12\x10\n\x0cFLATTEN_KIND\x10\x03\x12\r\n\tREAD_KIND\x10\x04\x12\x0e\n\nWRITE_KIND\x10\x05\x12\x11\n\rCONSTANT_KIND\x10\x06\x12\x12\n\x0eSINGLETON_KIND\x10\x07\x12\x10\n\x0cSHUFFLE_KIND\x10\x08*\xc3\x02\n\x08JobState\x12\x15\n\x11JOB_STATE_UNKNOWN\x10\x00\x12\x15\n\x11JOB_STATE_STOPPED\x10\x01\x12\x15\n\x11JOB_STATE_RUNNING\x10\x02\x12\x12\n\x0eJOB_STATE_DONE\x10\x03\x12\x14\n\x10JOB_STATE_FAILED\x10\x04\x12\x17\n\x13JOB_STATE_CANCELLED\x10\x05\x12\x15\n\x11JOB_STATE_UPDATED\x10\x06\x12\x16\n\x12JOB_STATE_DRAINING\x10\x07\x12\x15\n\x11JOB_STATE_DRAINED\x10\x08\x12\x15\n\x11JOB_STATE_PENDING\x10\t\x12\x18\n\x14JOB_STATE_CANCELLING\x10\n\x12\x14\n\x10JOB_STATE_QUEUED\x10\x0b\x12"\n\x1eJOB_STATE_RESOURCE_CLEANING_UP\x10\x0c*a\n\x07JobView\x12\x14\n\x10JOB_VIEW_UNKNOWN\x10\x00\x12\x14\n\x10JOB_VIEW_SUMMARY\x10\x01\x12\x10\n\x0cJOB_VIEW_ALL\x10\x02\x12\x18\n\x14JOB_VIEW_DESCRIPTION\x10\x032\x91\x0c\n\x0bJobsV1Beta3\x12\xc1\x01\n\tCreateJob\x12).google.dataflow.v1beta3.CreateJobRequest\x1a\x1c.google.dataflow.v1beta3.Job"k\x82\xd3\xe4\x93\x02e"5/v1b3/projects/{project_id}/locations/{location}/jobs:\x03jobZ\'" /v1b3/projects/{project_id}/jobs:\x03job\x12\xc3\x01\n\x06GetJob\x12&.google.dataflow.v1beta3.GetJobRequest\x1a\x1c.google.dataflow.v1beta3.Job"s\x82\xd3\xe4\x93\x02m\x12>/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}Z+\x12)/v1b3/projects/{project_id}/jobs/{job_id}\x12\xd3\x01\n\tUpdateJob\x12).google.dataflow.v1beta3.UpdateJobRequest\x1a\x1c.google.dataflow.v1beta3.Job"}\x82\xd3\xe4\x93\x02w\x1a>/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}:\x03jobZ0\x1a)/v1b3/projects/{project_id}/jobs/{job_id}:\x03job\x12\xc2\x01\n\x08ListJobs\x12(.google.dataflow.v1beta3.ListJobsRequest\x1a).google.dataflow.v1beta3.ListJobsResponse"a\x82\xd3\xe4\x93\x02[\x125/v1b3/projects/{project_id}/locations/{location}/jobsZ"\x12 /v1b3/projects/{project_id}/jobs\x12\x9e\x01\n\x12AggregatedListJobs\x12(.google.dataflow.v1beta3.ListJobsRequest\x1a).google.dataflow.v1beta3.ListJobsResponse"3\x82\xd3\xe4\x93\x02-\x12+/v1b3/projects/{project_id}/jobs:aggregated\x12v\n\x0fCheckActiveJobs\x12/.google.dataflow.v1beta3.CheckActiveJobsRequest\x1a0.google.dataflow.v1beta3.CheckActiveJobsResponse"\x00\x12\xec\x01\n\x0bSnapshotJob\x12+.google.dataflow.v1beta3.SnapshotJobRequest\x1a!.google.dataflow.v1beta3.Snapshot"\x8c\x01\x82\xd3\xe4\x93\x02\x85\x01"G/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}:snapshot:\x01*Z7"2/v1b3/projects/{project_id}/jobs/{job_id}:snapshot:\x01*\x1a\xd4\x01\xcaA\x17dataflow.googleapis.com\xd2A\xb6\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/compute.readonly,https://www.googleapis.com/auth/userinfo.emailB\xcc\x01\n\x1bcom.google.dataflow.v1beta3B\tJobsProtoP\x01Z=cloud.google.com/go/dataflow/apiv1beta3/dataflowpb;dataflowpb\xaa\x02\x1dGoogle.Cloud.Dataflow.V1Beta3\xca\x02\x1dGoogle\\Cloud\\Dataflow\\V1beta3\xea\x02 Google::Cloud::Dataflow::V1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.dataflow.v1beta3.jobs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.dataflow.v1beta3B\tJobsProtoP\x01Z=cloud.google.com/go/dataflow/apiv1beta3/dataflowpb;dataflowpb\xaa\x02\x1dGoogle.Cloud.Dataflow.V1Beta3\xca\x02\x1dGoogle\\Cloud\\Dataflow\\V1beta3\xea\x02 Google::Cloud::Dataflow::V1beta3'
    _globals['_JOB_TRANSFORMNAMEMAPPINGENTRY']._loaded_options = None
    _globals['_JOB_TRANSFORMNAMEMAPPINGENTRY']._serialized_options = b'8\x01'
    _globals['_JOB_LABELSENTRY']._loaded_options = None
    _globals['_JOB_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_JOBEXECUTIONINFO_STAGESENTRY']._loaded_options = None
    _globals['_JOBEXECUTIONINFO_STAGESENTRY']._serialized_options = b'8\x01'
    _globals['_LISTJOBSREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_LISTJOBSREQUEST'].fields_by_name['view']._serialized_options = b'\x18\x01'
    _globals['_JOBSV1BETA3']._loaded_options = None
    _globals['_JOBSV1BETA3']._serialized_options = b'\xcaA\x17dataflow.googleapis.com\xd2A\xb6\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/compute.readonly,https://www.googleapis.com/auth/userinfo.email'
    _globals['_JOBSV1BETA3'].methods_by_name['CreateJob']._loaded_options = None
    _globals['_JOBSV1BETA3'].methods_by_name['CreateJob']._serialized_options = b'\x82\xd3\xe4\x93\x02e"5/v1b3/projects/{project_id}/locations/{location}/jobs:\x03jobZ\'" /v1b3/projects/{project_id}/jobs:\x03job'
    _globals['_JOBSV1BETA3'].methods_by_name['GetJob']._loaded_options = None
    _globals['_JOBSV1BETA3'].methods_by_name['GetJob']._serialized_options = b'\x82\xd3\xe4\x93\x02m\x12>/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}Z+\x12)/v1b3/projects/{project_id}/jobs/{job_id}'
    _globals['_JOBSV1BETA3'].methods_by_name['UpdateJob']._loaded_options = None
    _globals['_JOBSV1BETA3'].methods_by_name['UpdateJob']._serialized_options = b'\x82\xd3\xe4\x93\x02w\x1a>/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}:\x03jobZ0\x1a)/v1b3/projects/{project_id}/jobs/{job_id}:\x03job'
    _globals['_JOBSV1BETA3'].methods_by_name['ListJobs']._loaded_options = None
    _globals['_JOBSV1BETA3'].methods_by_name['ListJobs']._serialized_options = b'\x82\xd3\xe4\x93\x02[\x125/v1b3/projects/{project_id}/locations/{location}/jobsZ"\x12 /v1b3/projects/{project_id}/jobs'
    _globals['_JOBSV1BETA3'].methods_by_name['AggregatedListJobs']._loaded_options = None
    _globals['_JOBSV1BETA3'].methods_by_name['AggregatedListJobs']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/v1b3/projects/{project_id}/jobs:aggregated'
    _globals['_JOBSV1BETA3'].methods_by_name['SnapshotJob']._loaded_options = None
    _globals['_JOBSV1BETA3'].methods_by_name['SnapshotJob']._serialized_options = b'\x82\xd3\xe4\x93\x02\x85\x01"G/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}:snapshot:\x01*Z7"2/v1b3/projects/{project_id}/jobs/{job_id}:snapshot:\x01*'
    _globals['_KINDTYPE']._serialized_start = 5815
    _globals['_KINDTYPE']._serialized_end = 5989
    _globals['_JOBSTATE']._serialized_start = 5992
    _globals['_JOBSTATE']._serialized_end = 6315
    _globals['_JOBVIEW']._serialized_start = 6317
    _globals['_JOBVIEW']._serialized_end = 6414
    _globals['_JOB']._serialized_start = 298
    _globals['_JOB']._serialized_end = 1496
    _globals['_JOB_TRANSFORMNAMEMAPPINGENTRY']._serialized_start = 1390
    _globals['_JOB_TRANSFORMNAMEMAPPINGENTRY']._serialized_end = 1449
    _globals['_JOB_LABELSENTRY']._serialized_start = 1451
    _globals['_JOB_LABELSENTRY']._serialized_end = 1496
    _globals['_DATASTOREIODETAILS']._serialized_start = 1498
    _globals['_DATASTOREIODETAILS']._serialized_end = 1557
    _globals['_PUBSUBIODETAILS']._serialized_start = 1559
    _globals['_PUBSUBIODETAILS']._serialized_end = 1613
    _globals['_FILEIODETAILS']._serialized_start = 1615
    _globals['_FILEIODETAILS']._serialized_end = 1652
    _globals['_BIGTABLEIODETAILS']._serialized_start = 1654
    _globals['_BIGTABLEIODETAILS']._serialized_end = 1732
    _globals['_BIGQUERYIODETAILS']._serialized_start = 1734
    _globals['_BIGQUERYIODETAILS']._serialized_end = 1820
    _globals['_SPANNERIODETAILS']._serialized_start = 1822
    _globals['_SPANNERIODETAILS']._serialized_end = 1902
    _globals['_SDKVERSION']._serialized_start = 1905
    _globals['_SDKVERSION']._serialized_end = 2138
    _globals['_SDKVERSION_SDKSUPPORTSTATUS']._serialized_start = 2048
    _globals['_SDKVERSION_SDKSUPPORTSTATUS']._serialized_end = 2138
    _globals['_JOBMETADATA']._serialized_start = 2141
    _globals['_JOBMETADATA']._serialized_end = 2621
    _globals['_EXECUTIONSTAGESTATE']._serialized_start = 2624
    _globals['_EXECUTIONSTAGESTATE']._serialized_end = 2797
    _globals['_PIPELINEDESCRIPTION']._serialized_start = 2800
    _globals['_PIPELINEDESCRIPTION']._serialized_end = 3043
    _globals['_TRANSFORMSUMMARY']._serialized_start = 3046
    _globals['_TRANSFORMSUMMARY']._serialized_end = 3262
    _globals['_EXECUTIONSTAGESUMMARY']._serialized_start = 3265
    _globals['_EXECUTIONSTAGESUMMARY']._serialized_end = 4029
    _globals['_EXECUTIONSTAGESUMMARY_STAGESOURCE']._serialized_start = 3744
    _globals['_EXECUTIONSTAGESUMMARY_STAGESOURCE']._serialized_end = 3852
    _globals['_EXECUTIONSTAGESUMMARY_COMPONENTTRANSFORM']._serialized_start = 3854
    _globals['_EXECUTIONSTAGESUMMARY_COMPONENTTRANSFORM']._serialized_end = 3935
    _globals['_EXECUTIONSTAGESUMMARY_COMPONENTSOURCE']._serialized_start = 3937
    _globals['_EXECUTIONSTAGESUMMARY_COMPONENTSOURCE']._serialized_end = 4029
    _globals['_DISPLAYDATA']._serialized_start = 4032
    _globals['_DISPLAYDATA']._serialized_end = 4364
    _globals['_STEP']._serialized_start = 4366
    _globals['_STEP']._serialized_end = 4445
    _globals['_JOBEXECUTIONINFO']._serialized_start = 4448
    _globals['_JOBEXECUTIONINFO']._serialized_end = 4632
    _globals['_JOBEXECUTIONINFO_STAGESENTRY']._serialized_start = 4539
    _globals['_JOBEXECUTIONINFO_STAGESENTRY']._serialized_end = 4632
    _globals['_JOBEXECUTIONSTAGEINFO']._serialized_start = 4634
    _globals['_JOBEXECUTIONSTAGEINFO']._serialized_end = 4676
    _globals['_CREATEJOBREQUEST']._serialized_start = 4679
    _globals['_CREATEJOBREQUEST']._serialized_end = 4850
    _globals['_GETJOBREQUEST']._serialized_start = 4852
    _globals['_GETJOBREQUEST']._serialized_end = 4969
    _globals['_UPDATEJOBREQUEST']._serialized_start = 4971
    _globals['_UPDATEJOBREQUEST']._serialized_end = 5086
    _globals['_LISTJOBSREQUEST']._serialized_start = 5089
    _globals['_LISTJOBSREQUEST']._serialized_end = 5360
    _globals['_LISTJOBSREQUEST_FILTER']._serialized_start = 5302
    _globals['_LISTJOBSREQUEST_FILTER']._serialized_end = 5360
    _globals['_FAILEDLOCATION']._serialized_start = 5362
    _globals['_FAILEDLOCATION']._serialized_end = 5392
    _globals['_LISTJOBSRESPONSE']._serialized_start = 5395
    _globals['_LISTJOBSRESPONSE']._serialized_end = 5548
    _globals['_SNAPSHOTJOBREQUEST']._serialized_start = 5551
    _globals['_SNAPSHOTJOBREQUEST']._serialized_end = 5712
    _globals['_CHECKACTIVEJOBSREQUEST']._serialized_start = 5714
    _globals['_CHECKACTIVEJOBSREQUEST']._serialized_end = 5758
    _globals['_CHECKACTIVEJOBSRESPONSE']._serialized_start = 5760
    _globals['_CHECKACTIVEJOBSRESPONSE']._serialized_end = 5812
    _globals['_JOBSV1BETA3']._serialized_start = 6417
    _globals['_JOBSV1BETA3']._serialized_end = 7970