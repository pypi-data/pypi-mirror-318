"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/scheduler/v1beta1/cloudscheduler.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.scheduler.v1beta1 import job_pb2 as google_dot_cloud_dot_scheduler_dot_v1beta1_dot_job__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/scheduler/v1beta1/cloudscheduler.proto\x12\x1egoogle.cloud.scheduler.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/scheduler/v1beta1/job.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xa3\x01\n\x0fListJobsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!cloudscheduler.googleapis.com/Job\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t\x12\x1e\n\x16legacy_app_engine_cron\x18\x07 \x01(\x08"^\n\x10ListJobsResponse\x121\n\x04jobs\x18\x01 \x03(\x0b2#.google.cloud.scheduler.v1beta1.Job\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"H\n\rGetJobRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!cloudscheduler.googleapis.com/Job"\x84\x01\n\x10CreateJobRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!cloudscheduler.googleapis.com/Job\x125\n\x03job\x18\x02 \x01(\x0b2#.google.cloud.scheduler.v1beta1.JobB\x03\xe0A\x02"z\n\x10UpdateJobRequest\x125\n\x03job\x18\x01 \x01(\x0b2#.google.cloud.scheduler.v1beta1.JobB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"k\n\x10DeleteJobRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!cloudscheduler.googleapis.com/Job\x12\x1e\n\x16legacy_app_engine_cron\x18\x02 \x01(\x08"J\n\x0fPauseJobRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!cloudscheduler.googleapis.com/Job"K\n\x10ResumeJobRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!cloudscheduler.googleapis.com/Job"h\n\rRunJobRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!cloudscheduler.googleapis.com/Job\x12\x1e\n\x16legacy_app_engine_cron\x18\x02 \x01(\x082\xa6\x0b\n\x0eCloudScheduler\x12\xad\x01\n\x08ListJobs\x12/.google.cloud.scheduler.v1beta1.ListJobsRequest\x1a0.google.cloud.scheduler.v1beta1.ListJobsResponse">\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1beta1/{parent=projects/*/locations/*}/jobs\x12\x9a\x01\n\x06GetJob\x12-.google.cloud.scheduler.v1beta1.GetJobRequest\x1a#.google.cloud.scheduler.v1beta1.Job"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1beta1/{name=projects/*/locations/*/jobs/*}\x12\xab\x01\n\tCreateJob\x120.google.cloud.scheduler.v1beta1.CreateJobRequest\x1a#.google.cloud.scheduler.v1beta1.Job"G\xdaA\nparent,job\x82\xd3\xe4\x93\x024"-/v1beta1/{parent=projects/*/locations/*}/jobs:\x03job\x12\xb4\x01\n\tUpdateJob\x120.google.cloud.scheduler.v1beta1.UpdateJobRequest\x1a#.google.cloud.scheduler.v1beta1.Job"P\xdaA\x0fjob,update_mask\x82\xd3\xe4\x93\x02821/v1beta1/{job.name=projects/*/locations/*/jobs/*}:\x03job\x12\x93\x01\n\tDeleteJob\x120.google.cloud.scheduler.v1beta1.DeleteJobRequest\x1a\x16.google.protobuf.Empty"<\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1beta1/{name=projects/*/locations/*/jobs/*}\x12\xa7\x01\n\x08PauseJob\x12/.google.cloud.scheduler.v1beta1.PauseJobRequest\x1a#.google.cloud.scheduler.v1beta1.Job"E\xdaA\x04name\x82\xd3\xe4\x93\x028"3/v1beta1/{name=projects/*/locations/*/jobs/*}:pause:\x01*\x12\xaa\x01\n\tResumeJob\x120.google.cloud.scheduler.v1beta1.ResumeJobRequest\x1a#.google.cloud.scheduler.v1beta1.Job"F\xdaA\x04name\x82\xd3\xe4\x93\x029"4/v1beta1/{name=projects/*/locations/*/jobs/*}:resume:\x01*\x12\xa1\x01\n\x06RunJob\x12-.google.cloud.scheduler.v1beta1.RunJobRequest\x1a#.google.cloud.scheduler.v1beta1.Job"C\xdaA\x04name\x82\xd3\xe4\x93\x026"1/v1beta1/{name=projects/*/locations/*/jobs/*}:run:\x01*\x1aQ\xcaA\x1dcloudscheduler.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x84\x01\n"com.google.cloud.scheduler.v1beta1B\x0eSchedulerProtoP\x01Z@cloud.google.com/go/scheduler/apiv1beta1/schedulerpb;schedulerpb\xa2\x02\tSCHEDULERb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.scheduler.v1beta1.cloudscheduler_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.scheduler.v1beta1B\x0eSchedulerProtoP\x01Z@cloud.google.com/go/scheduler/apiv1beta1/schedulerpb;schedulerpb\xa2\x02\tSCHEDULER'
    _globals['_LISTJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!cloudscheduler.googleapis.com/Job'
    _globals['_GETJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!cloudscheduler.googleapis.com/Job'
    _globals['_CREATEJOBREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEJOBREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!cloudscheduler.googleapis.com/Job'
    _globals['_CREATEJOBREQUEST'].fields_by_name['job']._loaded_options = None
    _globals['_CREATEJOBREQUEST'].fields_by_name['job']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEJOBREQUEST'].fields_by_name['job']._loaded_options = None
    _globals['_UPDATEJOBREQUEST'].fields_by_name['job']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!cloudscheduler.googleapis.com/Job'
    _globals['_PAUSEJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_PAUSEJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!cloudscheduler.googleapis.com/Job'
    _globals['_RESUMEJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESUMEJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!cloudscheduler.googleapis.com/Job'
    _globals['_RUNJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RUNJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!cloudscheduler.googleapis.com/Job'
    _globals['_CLOUDSCHEDULER']._loaded_options = None
    _globals['_CLOUDSCHEDULER']._serialized_options = b'\xcaA\x1dcloudscheduler.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CLOUDSCHEDULER'].methods_by_name['ListJobs']._loaded_options = None
    _globals['_CLOUDSCHEDULER'].methods_by_name['ListJobs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1beta1/{parent=projects/*/locations/*}/jobs'
    _globals['_CLOUDSCHEDULER'].methods_by_name['GetJob']._loaded_options = None
    _globals['_CLOUDSCHEDULER'].methods_by_name['GetJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1beta1/{name=projects/*/locations/*/jobs/*}'
    _globals['_CLOUDSCHEDULER'].methods_by_name['CreateJob']._loaded_options = None
    _globals['_CLOUDSCHEDULER'].methods_by_name['CreateJob']._serialized_options = b'\xdaA\nparent,job\x82\xd3\xe4\x93\x024"-/v1beta1/{parent=projects/*/locations/*}/jobs:\x03job'
    _globals['_CLOUDSCHEDULER'].methods_by_name['UpdateJob']._loaded_options = None
    _globals['_CLOUDSCHEDULER'].methods_by_name['UpdateJob']._serialized_options = b'\xdaA\x0fjob,update_mask\x82\xd3\xe4\x93\x02821/v1beta1/{job.name=projects/*/locations/*/jobs/*}:\x03job'
    _globals['_CLOUDSCHEDULER'].methods_by_name['DeleteJob']._loaded_options = None
    _globals['_CLOUDSCHEDULER'].methods_by_name['DeleteJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1beta1/{name=projects/*/locations/*/jobs/*}'
    _globals['_CLOUDSCHEDULER'].methods_by_name['PauseJob']._loaded_options = None
    _globals['_CLOUDSCHEDULER'].methods_by_name['PauseJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028"3/v1beta1/{name=projects/*/locations/*/jobs/*}:pause:\x01*'
    _globals['_CLOUDSCHEDULER'].methods_by_name['ResumeJob']._loaded_options = None
    _globals['_CLOUDSCHEDULER'].methods_by_name['ResumeJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029"4/v1beta1/{name=projects/*/locations/*/jobs/*}:resume:\x01*'
    _globals['_CLOUDSCHEDULER'].methods_by_name['RunJob']._loaded_options = None
    _globals['_CLOUDSCHEDULER'].methods_by_name['RunJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026"1/v1beta1/{name=projects/*/locations/*/jobs/*}:run:\x01*'
    _globals['_LISTJOBSREQUEST']._serialized_start = 308
    _globals['_LISTJOBSREQUEST']._serialized_end = 471
    _globals['_LISTJOBSRESPONSE']._serialized_start = 473
    _globals['_LISTJOBSRESPONSE']._serialized_end = 567
    _globals['_GETJOBREQUEST']._serialized_start = 569
    _globals['_GETJOBREQUEST']._serialized_end = 641
    _globals['_CREATEJOBREQUEST']._serialized_start = 644
    _globals['_CREATEJOBREQUEST']._serialized_end = 776
    _globals['_UPDATEJOBREQUEST']._serialized_start = 778
    _globals['_UPDATEJOBREQUEST']._serialized_end = 900
    _globals['_DELETEJOBREQUEST']._serialized_start = 902
    _globals['_DELETEJOBREQUEST']._serialized_end = 1009
    _globals['_PAUSEJOBREQUEST']._serialized_start = 1011
    _globals['_PAUSEJOBREQUEST']._serialized_end = 1085
    _globals['_RESUMEJOBREQUEST']._serialized_start = 1087
    _globals['_RESUMEJOBREQUEST']._serialized_end = 1162
    _globals['_RUNJOBREQUEST']._serialized_start = 1164
    _globals['_RUNJOBREQUEST']._serialized_end = 1268
    _globals['_CLOUDSCHEDULER']._serialized_start = 1271
    _globals['_CLOUDSCHEDULER']._serialized_end = 2717