"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/osconfig/agentendpoint/v1beta/tasks.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.cloud.osconfig.agentendpoint.v1beta import patch_jobs_pb2 as google_dot_cloud_dot_osconfig_dot_agentendpoint_dot_v1beta_dot_patch__jobs__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/osconfig/agentendpoint/v1beta/tasks.proto\x12*google.cloud.osconfig.agentendpoint.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a;google/cloud/osconfig/agentendpoint/v1beta/patch_jobs.proto"\x86\x04\n\x04Task\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12G\n\ttask_type\x18\x02 \x01(\x0e24.google.cloud.osconfig.agentendpoint.v1beta.TaskType\x12Q\n\x0etask_directive\x18\x03 \x01(\x0e29.google.cloud.osconfig.agentendpoint.v1beta.TaskDirective\x12Z\n\x12apply_patches_task\x18\x04 \x01(\x0b2<.google.cloud.osconfig.agentendpoint.v1beta.ApplyPatchesTaskH\x00\x12R\n\x0eexec_step_task\x18\x05 \x01(\x0b28.google.cloud.osconfig.agentendpoint.v1beta.ExecStepTaskH\x00\x12[\n\x0eservice_labels\x18\x06 \x03(\x0b2C.google.cloud.osconfig.agentendpoint.v1beta.Task.ServiceLabelsEntry\x1a4\n\x12ServiceLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x0e\n\x0ctask_details"r\n\x10ApplyPatchesTask\x12M\n\x0cpatch_config\x18\x01 \x01(\x0b27.google.cloud.osconfig.agentendpoint.v1beta.PatchConfig\x12\x0f\n\x07dry_run\x18\x03 \x01(\x08"\xe5\x01\n\x18ApplyPatchesTaskProgress\x12^\n\x05state\x18\x01 \x01(\x0e2J.google.cloud.osconfig.agentendpoint.v1beta.ApplyPatchesTaskProgress.StateB\x03\xe0A\x02"i\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07STARTED\x10\x04\x12\x17\n\x13DOWNLOADING_PATCHES\x10\x01\x12\x14\n\x10APPLYING_PATCHES\x10\x02\x12\r\n\tREBOOTING\x10\x03"\xd0\x01\n\x16ApplyPatchesTaskOutput\x12\\\n\x05state\x18\x01 \x01(\x0e2H.google.cloud.osconfig.agentendpoint.v1beta.ApplyPatchesTaskOutput.StateB\x03\xe0A\x02"X\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\x1d\n\x19SUCCEEDED_REBOOT_REQUIRED\x10\x02\x12\n\n\x06FAILED\x10\x03"W\n\x0cExecStepTask\x12G\n\texec_step\x18\x01 \x01(\x0b24.google.cloud.osconfig.agentendpoint.v1beta.ExecStep"\x9f\x01\n\x14ExecStepTaskProgress\x12Z\n\x05state\x18\x01 \x01(\x0e2F.google.cloud.osconfig.agentendpoint.v1beta.ExecStepTaskProgress.StateB\x03\xe0A\x02"+\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07STARTED\x10\x01"\xd3\x01\n\x12ExecStepTaskOutput\x12X\n\x05state\x18\x01 \x01(\x0e2D.google.cloud.osconfig.agentendpoint.v1beta.ExecStepTaskOutput.StateB\x03\xe0A\x02\x12\x16\n\texit_code\x18\x02 \x01(\x05B\x03\xe0A\x02"K\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tCOMPLETED\x10\x01\x12\r\n\tTIMED_OUT\x10\x02\x12\r\n\tCANCELLED\x10\x03*G\n\rTaskDirective\x12\x1e\n\x1aTASK_DIRECTIVE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CONTINUE\x10\x01\x12\x08\n\x04STOP\x10\x02*L\n\x08TaskType\x12\x19\n\x15TASK_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rAPPLY_PATCHES\x10\x01\x12\x12\n\x0eEXEC_STEP_TASK\x10\x02B\xac\x01\n.com.google.cloud.osconfig.agentendpoint.v1betaB\x05TasksZTcloud.google.com/go/osconfig/agentendpoint/apiv1beta/agentendpointpb;agentendpointpb\xca\x02\x1cGoogle\\Cloud\\OsConfig\\V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.osconfig.agentendpoint.v1beta.tasks_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n.com.google.cloud.osconfig.agentendpoint.v1betaB\x05TasksZTcloud.google.com/go/osconfig/agentendpoint/apiv1beta/agentendpointpb;agentendpointpb\xca\x02\x1cGoogle\\Cloud\\OsConfig\\V1beta'
    _globals['_TASK_SERVICELABELSENTRY']._loaded_options = None
    _globals['_TASK_SERVICELABELSENTRY']._serialized_options = b'8\x01'
    _globals['_APPLYPATCHESTASKPROGRESS'].fields_by_name['state']._loaded_options = None
    _globals['_APPLYPATCHESTASKPROGRESS'].fields_by_name['state']._serialized_options = b'\xe0A\x02'
    _globals['_APPLYPATCHESTASKOUTPUT'].fields_by_name['state']._loaded_options = None
    _globals['_APPLYPATCHESTASKOUTPUT'].fields_by_name['state']._serialized_options = b'\xe0A\x02'
    _globals['_EXECSTEPTASKPROGRESS'].fields_by_name['state']._loaded_options = None
    _globals['_EXECSTEPTASKPROGRESS'].fields_by_name['state']._serialized_options = b'\xe0A\x02'
    _globals['_EXECSTEPTASKOUTPUT'].fields_by_name['state']._loaded_options = None
    _globals['_EXECSTEPTASKOUTPUT'].fields_by_name['state']._serialized_options = b'\xe0A\x02'
    _globals['_EXECSTEPTASKOUTPUT'].fields_by_name['exit_code']._loaded_options = None
    _globals['_EXECSTEPTASKOUTPUT'].fields_by_name['exit_code']._serialized_options = b'\xe0A\x02'
    _globals['_TASKDIRECTIVE']._serialized_start = 1741
    _globals['_TASKDIRECTIVE']._serialized_end = 1812
    _globals['_TASKTYPE']._serialized_start = 1814
    _globals['_TASKTYPE']._serialized_end = 1890
    _globals['_TASK']._serialized_start = 197
    _globals['_TASK']._serialized_end = 715
    _globals['_TASK_SERVICELABELSENTRY']._serialized_start = 647
    _globals['_TASK_SERVICELABELSENTRY']._serialized_end = 699
    _globals['_APPLYPATCHESTASK']._serialized_start = 717
    _globals['_APPLYPATCHESTASK']._serialized_end = 831
    _globals['_APPLYPATCHESTASKPROGRESS']._serialized_start = 834
    _globals['_APPLYPATCHESTASKPROGRESS']._serialized_end = 1063
    _globals['_APPLYPATCHESTASKPROGRESS_STATE']._serialized_start = 958
    _globals['_APPLYPATCHESTASKPROGRESS_STATE']._serialized_end = 1063
    _globals['_APPLYPATCHESTASKOUTPUT']._serialized_start = 1066
    _globals['_APPLYPATCHESTASKOUTPUT']._serialized_end = 1274
    _globals['_APPLYPATCHESTASKOUTPUT_STATE']._serialized_start = 1186
    _globals['_APPLYPATCHESTASKOUTPUT_STATE']._serialized_end = 1274
    _globals['_EXECSTEPTASK']._serialized_start = 1276
    _globals['_EXECSTEPTASK']._serialized_end = 1363
    _globals['_EXECSTEPTASKPROGRESS']._serialized_start = 1366
    _globals['_EXECSTEPTASKPROGRESS']._serialized_end = 1525
    _globals['_EXECSTEPTASKPROGRESS_STATE']._serialized_start = 1482
    _globals['_EXECSTEPTASKPROGRESS_STATE']._serialized_end = 1525
    _globals['_EXECSTEPTASKOUTPUT']._serialized_start = 1528
    _globals['_EXECSTEPTASKOUTPUT']._serialized_end = 1739
    _globals['_EXECSTEPTASKOUTPUT_STATE']._serialized_start = 1664
    _globals['_EXECSTEPTASKOUTPUT_STATE']._serialized_end = 1739