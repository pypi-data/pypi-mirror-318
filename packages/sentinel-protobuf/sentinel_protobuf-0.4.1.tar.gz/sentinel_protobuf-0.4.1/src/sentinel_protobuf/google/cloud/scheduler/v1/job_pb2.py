"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/scheduler/v1/job.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.scheduler.v1 import target_pb2 as google_dot_cloud_dot_scheduler_dot_v1_dot_target__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/cloud/scheduler/v1/job.proto\x12\x19google.cloud.scheduler.v1\x1a\x19google/api/resource.proto\x1a&google/cloud/scheduler/v1/target.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xcb\x06\n\x03Job\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12@\n\rpubsub_target\x18\x04 \x01(\x0b2\'.google.cloud.scheduler.v1.PubsubTargetH\x00\x12P\n\x16app_engine_http_target\x18\x05 \x01(\x0b2..google.cloud.scheduler.v1.AppEngineHttpTargetH\x00\x12<\n\x0bhttp_target\x18\x06 \x01(\x0b2%.google.cloud.scheduler.v1.HttpTargetH\x00\x12\x10\n\x08schedule\x18\x14 \x01(\t\x12\x11\n\ttime_zone\x18\x15 \x01(\t\x124\n\x10user_update_time\x18\t \x01(\x0b2\x1a.google.protobuf.Timestamp\x123\n\x05state\x18\n \x01(\x0e2$.google.cloud.scheduler.v1.Job.State\x12"\n\x06status\x18\x0b \x01(\x0b2\x12.google.rpc.Status\x121\n\rschedule_time\x18\x11 \x01(\x0b2\x1a.google.protobuf.Timestamp\x125\n\x11last_attempt_time\x18\x12 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12<\n\x0cretry_config\x18\x13 \x01(\x0b2&.google.cloud.scheduler.v1.RetryConfig\x123\n\x10attempt_deadline\x18\x16 \x01(\x0b2\x19.google.protobuf.Duration"X\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\n\n\x06PAUSED\x10\x02\x12\x0c\n\x08DISABLED\x10\x03\x12\x11\n\rUPDATE_FAILED\x10\x04:Z\xeaAW\n!cloudscheduler.googleapis.com/Job\x122projects/{project}/locations/{location}/jobs/{job}B\x08\n\x06target"\xe2\x01\n\x0bRetryConfig\x12\x13\n\x0bretry_count\x18\x01 \x01(\x05\x125\n\x12max_retry_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x127\n\x14min_backoff_duration\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x127\n\x14max_backoff_duration\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x12\x15\n\rmax_doublings\x18\x05 \x01(\x05Bh\n\x1dcom.google.cloud.scheduler.v1B\x08JobProtoP\x01Z;cloud.google.com/go/scheduler/apiv1/schedulerpb;schedulerpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.scheduler.v1.job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.scheduler.v1B\x08JobProtoP\x01Z;cloud.google.com/go/scheduler/apiv1/schedulerpb;schedulerpb'
    _globals['_JOB']._loaded_options = None
    _globals['_JOB']._serialized_options = b'\xeaAW\n!cloudscheduler.googleapis.com/Job\x122projects/{project}/locations/{location}/jobs/{job}'
    _globals['_JOB']._serialized_start = 224
    _globals['_JOB']._serialized_end = 1067
    _globals['_JOB_STATE']._serialized_start = 877
    _globals['_JOB_STATE']._serialized_end = 965
    _globals['_RETRYCONFIG']._serialized_start = 1070
    _globals['_RETRYCONFIG']._serialized_end = 1296