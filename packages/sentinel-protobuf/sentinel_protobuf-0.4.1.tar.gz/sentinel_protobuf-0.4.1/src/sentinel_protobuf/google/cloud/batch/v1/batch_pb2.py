"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/batch/v1/batch.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.batch.v1 import job_pb2 as google_dot_cloud_dot_batch_dot_v1_dot_job__pb2
from .....google.cloud.batch.v1 import task_pb2 as google_dot_cloud_dot_batch_dot_v1_dot_task__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!google/cloud/batch/v1/batch.proto\x12\x15google.cloud.batch.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/cloud/batch/v1/job.proto\x1a google/cloud/batch/v1/task.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x9b\x01\n\x10CreateJobRequest\x120\n\x06parent\x18\x01 \x01(\tB \xe0A\x02\xfaA\x1a\x12\x18batch.googleapis.com/Job\x12\x0e\n\x06job_id\x18\x02 \x01(\t\x12,\n\x03job\x18\x03 \x01(\x0b2\x1a.google.cloud.batch.v1.JobB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"?\n\rGetJobRequest\x12.\n\x04name\x18\x01 \x01(\tB \xe0A\x02\xfaA\x1a\n\x18batch.googleapis.com/Job"N\n\x10DeleteJobRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x06reason\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"o\n\x0fListJobsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"j\n\x10ListJobsResponse\x12(\n\x04jobs\x18\x01 \x03(\x0b2\x1a.google.cloud.batch.v1.Job\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\x81\x01\n\x10ListTasksRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ebatch.googleapis.com/TaskGroup\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"m\n\x11ListTasksResponse\x12*\n\x05tasks\x18\x01 \x03(\x0b2\x1b.google.cloud.batch.v1.Task\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"A\n\x0eGetTaskRequest\x12/\n\x04name\x18\x01 \x01(\tB!\xe0A\x02\xfaA\x1b\n\x19batch.googleapis.com/Task"\x80\x02\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x032\xb6\x08\n\x0cBatchService\x12\x9b\x01\n\tCreateJob\x12\'.google.cloud.batch.v1.CreateJobRequest\x1a\x1a.google.cloud.batch.v1.Job"I\xdaA\x11parent,job,job_id\x82\xd3\xe4\x93\x02/"(/v1/{parent=projects/*/locations/*}/jobs:\x03job\x12\x83\x01\n\x06GetJob\x12$.google.cloud.batch.v1.GetJobRequest\x1a\x1a.google.cloud.batch.v1.Job"7\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/v1/{name=projects/*/locations/*/jobs/*}\x12\xcf\x01\n\tDeleteJob\x12\'.google.cloud.batch.v1.DeleteJobRequest\x1a\x1d.google.longrunning.Operation"z\xcaA@\n\x15google.protobuf.Empty\x12\'google.cloud.batch.v1.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02**(/v1/{name=projects/*/locations/*/jobs/*}\x12\x96\x01\n\x08ListJobs\x12&.google.cloud.batch.v1.ListJobsRequest\x1a\'.google.cloud.batch.v1.ListJobsResponse"9\xdaA\x06parent\x82\xd3\xe4\x93\x02*\x12(/v1/{parent=projects/*/locations/*}/jobs\x12\x9b\x01\n\x07GetTask\x12%.google.cloud.batch.v1.GetTaskRequest\x1a\x1b.google.cloud.batch.v1.Task"L\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1/{name=projects/*/locations/*/jobs/*/taskGroups/*/tasks/*}\x12\xae\x01\n\tListTasks\x12\'.google.cloud.batch.v1.ListTasksRequest\x1a(.google.cloud.batch.v1.ListTasksResponse"N\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1/{parent=projects/*/locations/*/jobs/*/taskGroups/*}/tasks\x1aH\xcaA\x14batch.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xab\x01\n\x19com.google.cloud.batch.v1B\nBatchProtoP\x01Z/cloud.google.com/go/batch/apiv1/batchpb;batchpb\xa2\x02\x03GCB\xaa\x02\x15Google.Cloud.Batch.V1\xca\x02\x15Google\\Cloud\\Batch\\V1\xea\x02\x18Google::Cloud::Batch::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.batch.v1.batch_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.cloud.batch.v1B\nBatchProtoP\x01Z/cloud.google.com/go/batch/apiv1/batchpb;batchpb\xa2\x02\x03GCB\xaa\x02\x15Google.Cloud.Batch.V1\xca\x02\x15Google\\Cloud\\Batch\\V1\xea\x02\x18Google::Cloud::Batch::V1'
    _globals['_CREATEJOBREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEJOBREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1a\x12\x18batch.googleapis.com/Job'
    _globals['_CREATEJOBREQUEST'].fields_by_name['job']._loaded_options = None
    _globals['_CREATEJOBREQUEST'].fields_by_name['job']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEJOBREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEJOBREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_GETJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1a\n\x18batch.googleapis.com/Job'
    _globals['_DELETEJOBREQUEST'].fields_by_name['reason']._loaded_options = None
    _globals['_DELETEJOBREQUEST'].fields_by_name['reason']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEJOBREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEJOBREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_LISTJOBSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTJOBSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTTASKSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTASKSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \n\x1ebatch.googleapis.com/TaskGroup'
    _globals['_GETTASKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTASKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1b\n\x19batch.googleapis.com/Task'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHSERVICE']._loaded_options = None
    _globals['_BATCHSERVICE']._serialized_options = b'\xcaA\x14batch.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_BATCHSERVICE'].methods_by_name['CreateJob']._loaded_options = None
    _globals['_BATCHSERVICE'].methods_by_name['CreateJob']._serialized_options = b'\xdaA\x11parent,job,job_id\x82\xd3\xe4\x93\x02/"(/v1/{parent=projects/*/locations/*}/jobs:\x03job'
    _globals['_BATCHSERVICE'].methods_by_name['GetJob']._loaded_options = None
    _globals['_BATCHSERVICE'].methods_by_name['GetJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/v1/{name=projects/*/locations/*/jobs/*}'
    _globals['_BATCHSERVICE'].methods_by_name['DeleteJob']._loaded_options = None
    _globals['_BATCHSERVICE'].methods_by_name['DeleteJob']._serialized_options = b"\xcaA@\n\x15google.protobuf.Empty\x12'google.cloud.batch.v1.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02**(/v1/{name=projects/*/locations/*/jobs/*}"
    _globals['_BATCHSERVICE'].methods_by_name['ListJobs']._loaded_options = None
    _globals['_BATCHSERVICE'].methods_by_name['ListJobs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02*\x12(/v1/{parent=projects/*/locations/*}/jobs'
    _globals['_BATCHSERVICE'].methods_by_name['GetTask']._loaded_options = None
    _globals['_BATCHSERVICE'].methods_by_name['GetTask']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1/{name=projects/*/locations/*/jobs/*/taskGroups/*/tasks/*}'
    _globals['_BATCHSERVICE'].methods_by_name['ListTasks']._loaded_options = None
    _globals['_BATCHSERVICE'].methods_by_name['ListTasks']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1/{parent=projects/*/locations/*/jobs/*/taskGroups/*}/tasks'
    _globals['_CREATEJOBREQUEST']._serialized_start = 371
    _globals['_CREATEJOBREQUEST']._serialized_end = 526
    _globals['_GETJOBREQUEST']._serialized_start = 528
    _globals['_GETJOBREQUEST']._serialized_end = 591
    _globals['_DELETEJOBREQUEST']._serialized_start = 593
    _globals['_DELETEJOBREQUEST']._serialized_end = 671
    _globals['_LISTJOBSREQUEST']._serialized_start = 673
    _globals['_LISTJOBSREQUEST']._serialized_end = 784
    _globals['_LISTJOBSRESPONSE']._serialized_start = 786
    _globals['_LISTJOBSRESPONSE']._serialized_end = 892
    _globals['_LISTTASKSREQUEST']._serialized_start = 895
    _globals['_LISTTASKSREQUEST']._serialized_end = 1024
    _globals['_LISTTASKSRESPONSE']._serialized_start = 1026
    _globals['_LISTTASKSRESPONSE']._serialized_end = 1135
    _globals['_GETTASKREQUEST']._serialized_start = 1137
    _globals['_GETTASKREQUEST']._serialized_end = 1202
    _globals['_OPERATIONMETADATA']._serialized_start = 1205
    _globals['_OPERATIONMETADATA']._serialized_end = 1461
    _globals['_BATCHSERVICE']._serialized_start = 1464
    _globals['_BATCHSERVICE']._serialized_end = 2542