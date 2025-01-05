"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/scheduler/v1/cloudscheduler.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.scheduler.v1 import job_pb2 as google_dot_cloud_dot_scheduler_dot_v1_dot_job__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/scheduler/v1/cloudscheduler.proto\x12\x19google.cloud.scheduler.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/cloud/scheduler/v1/job.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"s\n\x0fListJobsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!cloudscheduler.googleapis.com/Job\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t"Y\n\x10ListJobsResponse\x12,\n\x04jobs\x18\x01 \x03(\x0b2\x1e.google.cloud.scheduler.v1.Job\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"H\n\rGetJobRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!cloudscheduler.googleapis.com/Job"\x7f\n\x10CreateJobRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!cloudscheduler.googleapis.com/Job\x120\n\x03job\x18\x02 \x01(\x0b2\x1e.google.cloud.scheduler.v1.JobB\x03\xe0A\x02"u\n\x10UpdateJobRequest\x120\n\x03job\x18\x01 \x01(\x0b2\x1e.google.cloud.scheduler.v1.JobB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"K\n\x10DeleteJobRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!cloudscheduler.googleapis.com/Job"J\n\x0fPauseJobRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!cloudscheduler.googleapis.com/Job"K\n\x10ResumeJobRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!cloudscheduler.googleapis.com/Job"H\n\rRunJobRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!cloudscheduler.googleapis.com/Job2\xb3\n\n\x0eCloudScheduler\x12\x9e\x01\n\x08ListJobs\x12*.google.cloud.scheduler.v1.ListJobsRequest\x1a+.google.cloud.scheduler.v1.ListJobsResponse"9\xdaA\x06parent\x82\xd3\xe4\x93\x02*\x12(/v1/{parent=projects/*/locations/*}/jobs\x12\x8b\x01\n\x06GetJob\x12(.google.cloud.scheduler.v1.GetJobRequest\x1a\x1e.google.cloud.scheduler.v1.Job"7\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/v1/{name=projects/*/locations/*/jobs/*}\x12\x9c\x01\n\tCreateJob\x12+.google.cloud.scheduler.v1.CreateJobRequest\x1a\x1e.google.cloud.scheduler.v1.Job"B\xdaA\nparent,job\x82\xd3\xe4\x93\x02/"(/v1/{parent=projects/*/locations/*}/jobs:\x03job\x12\xa5\x01\n\tUpdateJob\x12+.google.cloud.scheduler.v1.UpdateJobRequest\x1a\x1e.google.cloud.scheduler.v1.Job"K\xdaA\x0fjob,update_mask\x82\xd3\xe4\x93\x0232,/v1/{job.name=projects/*/locations/*/jobs/*}:\x03job\x12\x89\x01\n\tDeleteJob\x12+.google.cloud.scheduler.v1.DeleteJobRequest\x1a\x16.google.protobuf.Empty"7\xdaA\x04name\x82\xd3\xe4\x93\x02**(/v1/{name=projects/*/locations/*/jobs/*}\x12\x98\x01\n\x08PauseJob\x12*.google.cloud.scheduler.v1.PauseJobRequest\x1a\x1e.google.cloud.scheduler.v1.Job"@\xdaA\x04name\x82\xd3\xe4\x93\x023"./v1/{name=projects/*/locations/*/jobs/*}:pause:\x01*\x12\x9b\x01\n\tResumeJob\x12+.google.cloud.scheduler.v1.ResumeJobRequest\x1a\x1e.google.cloud.scheduler.v1.Job"A\xdaA\x04name\x82\xd3\xe4\x93\x024"//v1/{name=projects/*/locations/*/jobs/*}:resume:\x01*\x12\x92\x01\n\x06RunJob\x12(.google.cloud.scheduler.v1.RunJobRequest\x1a\x1e.google.cloud.scheduler.v1.Job">\xdaA\x04name\x82\xd3\xe4\x93\x021",/v1/{name=projects/*/locations/*/jobs/*}:run:\x01*\x1aQ\xcaA\x1dcloudscheduler.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBz\n\x1dcom.google.cloud.scheduler.v1B\x0eSchedulerProtoP\x01Z;cloud.google.com/go/scheduler/apiv1/schedulerpb;schedulerpb\xa2\x02\tSCHEDULERb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.scheduler.v1.cloudscheduler_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.scheduler.v1B\x0eSchedulerProtoP\x01Z;cloud.google.com/go/scheduler/apiv1/schedulerpb;schedulerpb\xa2\x02\tSCHEDULER'
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
    _globals['_CLOUDSCHEDULER'].methods_by_name['ListJobs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02*\x12(/v1/{parent=projects/*/locations/*}/jobs'
    _globals['_CLOUDSCHEDULER'].methods_by_name['GetJob']._loaded_options = None
    _globals['_CLOUDSCHEDULER'].methods_by_name['GetJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/v1/{name=projects/*/locations/*/jobs/*}'
    _globals['_CLOUDSCHEDULER'].methods_by_name['CreateJob']._loaded_options = None
    _globals['_CLOUDSCHEDULER'].methods_by_name['CreateJob']._serialized_options = b'\xdaA\nparent,job\x82\xd3\xe4\x93\x02/"(/v1/{parent=projects/*/locations/*}/jobs:\x03job'
    _globals['_CLOUDSCHEDULER'].methods_by_name['UpdateJob']._loaded_options = None
    _globals['_CLOUDSCHEDULER'].methods_by_name['UpdateJob']._serialized_options = b'\xdaA\x0fjob,update_mask\x82\xd3\xe4\x93\x0232,/v1/{job.name=projects/*/locations/*/jobs/*}:\x03job'
    _globals['_CLOUDSCHEDULER'].methods_by_name['DeleteJob']._loaded_options = None
    _globals['_CLOUDSCHEDULER'].methods_by_name['DeleteJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02**(/v1/{name=projects/*/locations/*/jobs/*}'
    _globals['_CLOUDSCHEDULER'].methods_by_name['PauseJob']._loaded_options = None
    _globals['_CLOUDSCHEDULER'].methods_by_name['PauseJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023"./v1/{name=projects/*/locations/*/jobs/*}:pause:\x01*'
    _globals['_CLOUDSCHEDULER'].methods_by_name['ResumeJob']._loaded_options = None
    _globals['_CLOUDSCHEDULER'].methods_by_name['ResumeJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024"//v1/{name=projects/*/locations/*/jobs/*}:resume:\x01*'
    _globals['_CLOUDSCHEDULER'].methods_by_name['RunJob']._loaded_options = None
    _globals['_CLOUDSCHEDULER'].methods_by_name['RunJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021",/v1/{name=projects/*/locations/*/jobs/*}:run:\x01*'
    _globals['_LISTJOBSREQUEST']._serialized_start = 292
    _globals['_LISTJOBSREQUEST']._serialized_end = 407
    _globals['_LISTJOBSRESPONSE']._serialized_start = 409
    _globals['_LISTJOBSRESPONSE']._serialized_end = 498
    _globals['_GETJOBREQUEST']._serialized_start = 500
    _globals['_GETJOBREQUEST']._serialized_end = 572
    _globals['_CREATEJOBREQUEST']._serialized_start = 574
    _globals['_CREATEJOBREQUEST']._serialized_end = 701
    _globals['_UPDATEJOBREQUEST']._serialized_start = 703
    _globals['_UPDATEJOBREQUEST']._serialized_end = 820
    _globals['_DELETEJOBREQUEST']._serialized_start = 822
    _globals['_DELETEJOBREQUEST']._serialized_end = 897
    _globals['_PAUSEJOBREQUEST']._serialized_start = 899
    _globals['_PAUSEJOBREQUEST']._serialized_end = 973
    _globals['_RESUMEJOBREQUEST']._serialized_start = 975
    _globals['_RESUMEJOBREQUEST']._serialized_end = 1050
    _globals['_RUNJOBREQUEST']._serialized_start = 1052
    _globals['_RUNJOBREQUEST']._serialized_end = 1124
    _globals['_CLOUDSCHEDULER']._serialized_start = 1127
    _globals['_CLOUDSCHEDULER']._serialized_end = 2458