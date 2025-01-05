"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/tasks/v2/task.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.tasks.v2 import target_pb2 as google_dot_cloud_dot_tasks_dot_v2_dot_target__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n google/cloud/tasks/v2/task.proto\x12\x15google.cloud.tasks.v2\x1a\x19google/api/resource.proto\x1a"google/cloud/tasks/v2/target.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xb4\x05\n\x04Task\x12\x0c\n\x04name\x18\x01 \x01(\t\x12N\n\x17app_engine_http_request\x18\x02 \x01(\x0b2+.google.cloud.tasks.v2.AppEngineHttpRequestH\x00\x12:\n\x0chttp_request\x18\x03 \x01(\x0b2".google.cloud.tasks.v2.HttpRequestH\x00\x121\n\rschedule_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x11dispatch_deadline\x18\x06 \x01(\x0b2\x19.google.protobuf.Duration\x12\x16\n\x0edispatch_count\x18\x07 \x01(\x05\x12\x16\n\x0eresponse_count\x18\x08 \x01(\x05\x125\n\rfirst_attempt\x18\t \x01(\x0b2\x1e.google.cloud.tasks.v2.Attempt\x124\n\x0clast_attempt\x18\n \x01(\x0b2\x1e.google.cloud.tasks.v2.Attempt\x12.\n\x04view\x18\x0b \x01(\x0e2 .google.cloud.tasks.v2.Task.View"1\n\x04View\x12\x14\n\x10VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x08\n\x04FULL\x10\x02:h\xeaAe\n\x1ecloudtasks.googleapis.com/Task\x12Cprojects/{project}/locations/{location}/queues/{queue}/tasks/{task}B\x0e\n\x0cmessage_type"\xcf\x01\n\x07Attempt\x121\n\rschedule_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x121\n\rdispatch_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x121\n\rresponse_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12+\n\x0fresponse_status\x18\x04 \x01(\x0b2\x12.google.rpc.StatusBh\n\x19com.google.cloud.tasks.v2B\tTaskProtoP\x01Z>cloud.google.com/go/cloudtasks/apiv2/cloudtaskspb;cloudtaskspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.tasks.v2.task_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.cloud.tasks.v2B\tTaskProtoP\x01Z>cloud.google.com/go/cloudtasks/apiv2/cloudtaskspb;cloudtaskspb'
    _globals['_TASK']._loaded_options = None
    _globals['_TASK']._serialized_options = b'\xeaAe\n\x1ecloudtasks.googleapis.com/Task\x12Cprojects/{project}/locations/{location}/queues/{queue}/tasks/{task}'
    _globals['_TASK']._serialized_start = 213
    _globals['_TASK']._serialized_end = 905
    _globals['_TASK_VIEW']._serialized_start = 734
    _globals['_TASK_VIEW']._serialized_end = 783
    _globals['_ATTEMPT']._serialized_start = 908
    _globals['_ATTEMPT']._serialized_end = 1115