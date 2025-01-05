"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/batch/v1/task.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.batch.v1 import volume_pb2 as google_dot_cloud_dot_batch_dot_v1_dot_volume__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n google/cloud/batch/v1/task.proto\x12\x15google.cloud.batch.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a"google/cloud/batch/v1/volume.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"O\n\x0fComputeResource\x12\x11\n\tcpu_milli\x18\x01 \x01(\x03\x12\x12\n\nmemory_mib\x18\x02 \x01(\x03\x12\x15\n\rboot_disk_mib\x18\x04 \x01(\x03"\xdb\x01\n\x0bStatusEvent\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x13\n\x0bdescription\x18\x01 \x01(\t\x12.\n\nevent_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12<\n\x0etask_execution\x18\x04 \x01(\x0b2$.google.cloud.batch.v1.TaskExecution\x12;\n\ntask_state\x18\x05 \x01(\x0e2\'.google.cloud.batch.v1.TaskStatus.State""\n\rTaskExecution\x12\x11\n\texit_code\x18\x01 \x01(\x05"\xf2\x01\n\nTaskStatus\x126\n\x05state\x18\x01 \x01(\x0e2\'.google.cloud.batch.v1.TaskStatus.State\x129\n\rstatus_events\x18\x02 \x03(\x0b2".google.cloud.batch.v1.StatusEvent"q\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0c\n\x08ASSIGNED\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\r\n\tSUCCEEDED\x10\x05\x12\x0e\n\nUNEXECUTED\x10\x06"\x9e\x06\n\x08Runnable\x12>\n\tcontainer\x18\x01 \x01(\x0b2).google.cloud.batch.v1.Runnable.ContainerH\x00\x128\n\x06script\x18\x02 \x01(\x0b2&.google.cloud.batch.v1.Runnable.ScriptH\x00\x12:\n\x07barrier\x18\x06 \x01(\x0b2\'.google.cloud.batch.v1.Runnable.BarrierH\x00\x12\x19\n\x0cdisplay_name\x18\n \x01(\tB\x03\xe0A\x01\x12\x1a\n\x12ignore_exit_status\x18\x03 \x01(\x08\x12\x12\n\nbackground\x18\x04 \x01(\x08\x12\x12\n\nalways_run\x18\x05 \x01(\x08\x127\n\x0benvironment\x18\x07 \x01(\x0b2".google.cloud.batch.v1.Environment\x12*\n\x07timeout\x18\x08 \x01(\x0b2\x19.google.protobuf.Duration\x12;\n\x06labels\x18\t \x03(\x0b2+.google.cloud.batch.v1.Runnable.LabelsEntry\x1a\xcf\x01\n\tContainer\x12\x11\n\timage_uri\x18\x01 \x01(\t\x12\x10\n\x08commands\x18\x02 \x03(\t\x12\x12\n\nentrypoint\x18\x03 \x01(\t\x12\x0f\n\x07volumes\x18\x07 \x03(\t\x12\x0f\n\x07options\x18\x08 \x01(\t\x12\x1e\n\x16block_external_network\x18\t \x01(\x08\x12\x10\n\x08username\x18\n \x01(\t\x12\x10\n\x08password\x18\x0b \x01(\t\x12#\n\x16enable_image_streaming\x18\x0c \x01(\x08B\x03\xe0A\x01\x1a3\n\x06Script\x12\x0e\n\x04path\x18\x01 \x01(\tH\x00\x12\x0e\n\x04text\x18\x02 \x01(\tH\x00B\t\n\x07command\x1a\x17\n\x07Barrier\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x0c\n\nexecutable"\xfd\x03\n\x08TaskSpec\x122\n\trunnables\x18\x08 \x03(\x0b2\x1f.google.cloud.batch.v1.Runnable\x12@\n\x10compute_resource\x18\x03 \x01(\x0b2&.google.cloud.batch.v1.ComputeResource\x123\n\x10max_run_duration\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x12\x17\n\x0fmax_retry_count\x18\x05 \x01(\x05\x12B\n\x12lifecycle_policies\x18\t \x03(\x0b2&.google.cloud.batch.v1.LifecyclePolicy\x12K\n\x0cenvironments\x18\x06 \x03(\x0b21.google.cloud.batch.v1.TaskSpec.EnvironmentsEntryB\x02\x18\x01\x12.\n\x07volumes\x18\x07 \x03(\x0b2\x1d.google.cloud.batch.v1.Volume\x127\n\x0benvironment\x18\n \x01(\x0b2".google.cloud.batch.v1.Environment\x1a3\n\x11EnvironmentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x8a\x02\n\x0fLifecyclePolicy\x12=\n\x06action\x18\x01 \x01(\x0e2-.google.cloud.batch.v1.LifecyclePolicy.Action\x12P\n\x10action_condition\x18\x02 \x01(\x0b26.google.cloud.batch.v1.LifecyclePolicy.ActionCondition\x1a%\n\x0fActionCondition\x12\x12\n\nexit_codes\x18\x01 \x03(\x05"?\n\x06Action\x12\x16\n\x12ACTION_UNSPECIFIED\x10\x00\x12\x0e\n\nRETRY_TASK\x10\x01\x12\r\n\tFAIL_TASK\x10\x02"\xc0\x01\n\x04Task\x12\x0c\n\x04name\x18\x01 \x01(\t\x121\n\x06status\x18\x02 \x01(\x0b2!.google.cloud.batch.v1.TaskStatus:w\xeaAt\n\x19batch.googleapis.com/Task\x12Wprojects/{project}/locations/{location}/jobs/{job}/taskGroups/{task_group}/tasks/{task}"\x8f\x03\n\x0bEnvironment\x12D\n\tvariables\x18\x01 \x03(\x0b21.google.cloud.batch.v1.Environment.VariablesEntry\x12Q\n\x10secret_variables\x18\x02 \x03(\x0b27.google.cloud.batch.v1.Environment.SecretVariablesEntry\x12I\n\x13encrypted_variables\x18\x03 \x01(\x0b2,.google.cloud.batch.v1.Environment.KMSEnvMap\x1a2\n\tKMSEnvMap\x12\x10\n\x08key_name\x18\x01 \x01(\t\x12\x13\n\x0bcipher_text\x18\x02 \x01(\t\x1a0\n\x0eVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a6\n\x14SecretVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\xaa\x01\n\x19com.google.cloud.batch.v1B\tTaskProtoP\x01Z/cloud.google.com/go/batch/apiv1/batchpb;batchpb\xa2\x02\x03GCB\xaa\x02\x15Google.Cloud.Batch.V1\xca\x02\x15Google\\Cloud\\Batch\\V1\xea\x02\x18Google::Cloud::Batch::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.batch.v1.task_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.cloud.batch.v1B\tTaskProtoP\x01Z/cloud.google.com/go/batch/apiv1/batchpb;batchpb\xa2\x02\x03GCB\xaa\x02\x15Google.Cloud.Batch.V1\xca\x02\x15Google\\Cloud\\Batch\\V1\xea\x02\x18Google::Cloud::Batch::V1'
    _globals['_RUNNABLE_CONTAINER'].fields_by_name['enable_image_streaming']._loaded_options = None
    _globals['_RUNNABLE_CONTAINER'].fields_by_name['enable_image_streaming']._serialized_options = b'\xe0A\x01'
    _globals['_RUNNABLE_LABELSENTRY']._loaded_options = None
    _globals['_RUNNABLE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_RUNNABLE'].fields_by_name['display_name']._loaded_options = None
    _globals['_RUNNABLE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_TASKSPEC_ENVIRONMENTSENTRY']._loaded_options = None
    _globals['_TASKSPEC_ENVIRONMENTSENTRY']._serialized_options = b'8\x01'
    _globals['_TASKSPEC'].fields_by_name['environments']._loaded_options = None
    _globals['_TASKSPEC'].fields_by_name['environments']._serialized_options = b'\x18\x01'
    _globals['_TASK']._loaded_options = None
    _globals['_TASK']._serialized_options = b'\xeaAt\n\x19batch.googleapis.com/Task\x12Wprojects/{project}/locations/{location}/jobs/{job}/taskGroups/{task_group}/tasks/{task}'
    _globals['_ENVIRONMENT_VARIABLESENTRY']._loaded_options = None
    _globals['_ENVIRONMENT_VARIABLESENTRY']._serialized_options = b'8\x01'
    _globals['_ENVIRONMENT_SECRETVARIABLESENTRY']._loaded_options = None
    _globals['_ENVIRONMENT_SECRETVARIABLESENTRY']._serialized_options = b'8\x01'
    _globals['_COMPUTERESOURCE']._serialized_start = 220
    _globals['_COMPUTERESOURCE']._serialized_end = 299
    _globals['_STATUSEVENT']._serialized_start = 302
    _globals['_STATUSEVENT']._serialized_end = 521
    _globals['_TASKEXECUTION']._serialized_start = 523
    _globals['_TASKEXECUTION']._serialized_end = 557
    _globals['_TASKSTATUS']._serialized_start = 560
    _globals['_TASKSTATUS']._serialized_end = 802
    _globals['_TASKSTATUS_STATE']._serialized_start = 689
    _globals['_TASKSTATUS_STATE']._serialized_end = 802
    _globals['_RUNNABLE']._serialized_start = 805
    _globals['_RUNNABLE']._serialized_end = 1603
    _globals['_RUNNABLE_CONTAINER']._serialized_start = 1257
    _globals['_RUNNABLE_CONTAINER']._serialized_end = 1464
    _globals['_RUNNABLE_SCRIPT']._serialized_start = 1466
    _globals['_RUNNABLE_SCRIPT']._serialized_end = 1517
    _globals['_RUNNABLE_BARRIER']._serialized_start = 1519
    _globals['_RUNNABLE_BARRIER']._serialized_end = 1542
    _globals['_RUNNABLE_LABELSENTRY']._serialized_start = 1544
    _globals['_RUNNABLE_LABELSENTRY']._serialized_end = 1589
    _globals['_TASKSPEC']._serialized_start = 1606
    _globals['_TASKSPEC']._serialized_end = 2115
    _globals['_TASKSPEC_ENVIRONMENTSENTRY']._serialized_start = 2064
    _globals['_TASKSPEC_ENVIRONMENTSENTRY']._serialized_end = 2115
    _globals['_LIFECYCLEPOLICY']._serialized_start = 2118
    _globals['_LIFECYCLEPOLICY']._serialized_end = 2384
    _globals['_LIFECYCLEPOLICY_ACTIONCONDITION']._serialized_start = 2282
    _globals['_LIFECYCLEPOLICY_ACTIONCONDITION']._serialized_end = 2319
    _globals['_LIFECYCLEPOLICY_ACTION']._serialized_start = 2321
    _globals['_LIFECYCLEPOLICY_ACTION']._serialized_end = 2384
    _globals['_TASK']._serialized_start = 2387
    _globals['_TASK']._serialized_end = 2579
    _globals['_ENVIRONMENT']._serialized_start = 2582
    _globals['_ENVIRONMENT']._serialized_end = 2981
    _globals['_ENVIRONMENT_KMSENVMAP']._serialized_start = 2825
    _globals['_ENVIRONMENT_KMSENVMAP']._serialized_end = 2875
    _globals['_ENVIRONMENT_VARIABLESENTRY']._serialized_start = 2877
    _globals['_ENVIRONMENT_VARIABLESENTRY']._serialized_end = 2925
    _globals['_ENVIRONMENT_SECRETVARIABLESENTRY']._serialized_start = 2927
    _globals['_ENVIRONMENT_SECRETVARIABLESENTRY']._serialized_end = 2981