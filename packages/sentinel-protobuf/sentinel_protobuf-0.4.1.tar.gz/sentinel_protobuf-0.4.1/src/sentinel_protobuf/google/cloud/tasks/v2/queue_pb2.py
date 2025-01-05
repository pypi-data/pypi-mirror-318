"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/tasks/v2/queue.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.tasks.v2 import target_pb2 as google_dot_cloud_dot_tasks_dot_v2_dot_target__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!google/cloud/tasks/v2/queue.proto\x12\x15google.cloud.tasks.v2\x1a\x19google/api/resource.proto\x1a"google/cloud/tasks/v2/target.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb2\x04\n\x05Queue\x12\x0c\n\x04name\x18\x01 \x01(\t\x12L\n\x1bapp_engine_routing_override\x18\x02 \x01(\x0b2\'.google.cloud.tasks.v2.AppEngineRouting\x126\n\x0brate_limits\x18\x03 \x01(\x0b2!.google.cloud.tasks.v2.RateLimits\x128\n\x0cretry_config\x18\x04 \x01(\x0b2".google.cloud.tasks.v2.RetryConfig\x121\n\x05state\x18\x05 \x01(\x0e2".google.cloud.tasks.v2.Queue.State\x12.\n\npurge_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12S\n\x1astackdriver_logging_config\x18\t \x01(\x0b2/.google.cloud.tasks.v2.StackdriverLoggingConfig"E\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\n\n\x06PAUSED\x10\x02\x12\x0c\n\x08DISABLED\x10\x03:\\\xeaAY\n\x1fcloudtasks.googleapis.com/Queue\x126projects/{project}/locations/{location}/queues/{queue}"j\n\nRateLimits\x12!\n\x19max_dispatches_per_second\x18\x01 \x01(\x01\x12\x16\n\x0emax_burst_size\x18\x02 \x01(\x05\x12!\n\x19max_concurrent_dispatches\x18\x03 \x01(\x05"\xd1\x01\n\x0bRetryConfig\x12\x14\n\x0cmax_attempts\x18\x01 \x01(\x05\x125\n\x12max_retry_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x12.\n\x0bmin_backoff\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x12.\n\x0bmax_backoff\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x12\x15\n\rmax_doublings\x18\x05 \x01(\x05"2\n\x18StackdriverLoggingConfig\x12\x16\n\x0esampling_ratio\x18\x01 \x01(\x01Bi\n\x19com.google.cloud.tasks.v2B\nQueueProtoP\x01Z>cloud.google.com/go/cloudtasks/apiv2/cloudtaskspb;cloudtaskspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.tasks.v2.queue_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.cloud.tasks.v2B\nQueueProtoP\x01Z>cloud.google.com/go/cloudtasks/apiv2/cloudtaskspb;cloudtaskspb'
    _globals['_QUEUE']._loaded_options = None
    _globals['_QUEUE']._serialized_options = b'\xeaAY\n\x1fcloudtasks.googleapis.com/Queue\x126projects/{project}/locations/{location}/queues/{queue}'
    _globals['_QUEUE']._serialized_start = 189
    _globals['_QUEUE']._serialized_end = 751
    _globals['_QUEUE_STATE']._serialized_start = 588
    _globals['_QUEUE_STATE']._serialized_end = 657
    _globals['_RATELIMITS']._serialized_start = 753
    _globals['_RATELIMITS']._serialized_end = 859
    _globals['_RETRYCONFIG']._serialized_start = 862
    _globals['_RETRYCONFIG']._serialized_end = 1071
    _globals['_STACKDRIVERLOGGINGCONFIG']._serialized_start = 1073
    _globals['_STACKDRIVERLOGGINGCONFIG']._serialized_end = 1123