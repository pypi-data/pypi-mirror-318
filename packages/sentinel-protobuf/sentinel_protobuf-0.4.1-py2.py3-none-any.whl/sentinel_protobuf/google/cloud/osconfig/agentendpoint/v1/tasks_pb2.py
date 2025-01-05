"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/osconfig/agentendpoint/v1/tasks.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.osconfig.agentendpoint.v1 import config_common_pb2 as google_dot_cloud_dot_osconfig_dot_agentendpoint_dot_v1_dot_config__common__pb2
from ......google.cloud.osconfig.agentendpoint.v1 import os_policy_pb2 as google_dot_cloud_dot_osconfig_dot_agentendpoint_dot_v1_dot_os__policy__pb2
from ......google.cloud.osconfig.agentendpoint.v1 import patch_jobs_pb2 as google_dot_cloud_dot_osconfig_dot_agentendpoint_dot_v1_dot_patch__jobs__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/osconfig/agentendpoint/v1/tasks.proto\x12&google.cloud.osconfig.agentendpoint.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a:google/cloud/osconfig/agentendpoint/v1/config_common.proto\x1a6google/cloud/osconfig/agentendpoint/v1/os_policy.proto\x1a7google/cloud/osconfig/agentendpoint/v1/patch_jobs.proto"\xc8\x04\n\x04Task\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12C\n\ttask_type\x18\x02 \x01(\x0e20.google.cloud.osconfig.agentendpoint.v1.TaskType\x12M\n\x0etask_directive\x18\x03 \x01(\x0e25.google.cloud.osconfig.agentendpoint.v1.TaskDirective\x12V\n\x12apply_patches_task\x18\x04 \x01(\x0b28.google.cloud.osconfig.agentendpoint.v1.ApplyPatchesTaskH\x00\x12N\n\x0eexec_step_task\x18\x05 \x01(\x0b24.google.cloud.osconfig.agentendpoint.v1.ExecStepTaskH\x00\x12T\n\x11apply_config_task\x18\x07 \x01(\x0b27.google.cloud.osconfig.agentendpoint.v1.ApplyConfigTaskH\x00\x12W\n\x0eservice_labels\x18\x06 \x03(\x0b2?.google.cloud.osconfig.agentendpoint.v1.Task.ServiceLabelsEntry\x1a4\n\x12ServiceLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x0e\n\x0ctask_details"n\n\x10ApplyPatchesTask\x12I\n\x0cpatch_config\x18\x01 \x01(\x0b23.google.cloud.osconfig.agentendpoint.v1.PatchConfig\x12\x0f\n\x07dry_run\x18\x03 \x01(\x08"\xe1\x01\n\x18ApplyPatchesTaskProgress\x12Z\n\x05state\x18\x01 \x01(\x0e2F.google.cloud.osconfig.agentendpoint.v1.ApplyPatchesTaskProgress.StateB\x03\xe0A\x02"i\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07STARTED\x10\x04\x12\x17\n\x13DOWNLOADING_PATCHES\x10\x01\x12\x14\n\x10APPLYING_PATCHES\x10\x02\x12\r\n\tREBOOTING\x10\x03"\xcc\x01\n\x16ApplyPatchesTaskOutput\x12X\n\x05state\x18\x01 \x01(\x0e2D.google.cloud.osconfig.agentendpoint.v1.ApplyPatchesTaskOutput.StateB\x03\xe0A\x02"X\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\x1d\n\x19SUCCEEDED_REBOOT_REQUIRED\x10\x02\x12\n\n\x06FAILED\x10\x03"S\n\x0cExecStepTask\x12C\n\texec_step\x18\x01 \x01(\x0b20.google.cloud.osconfig.agentendpoint.v1.ExecStep"\x9b\x01\n\x14ExecStepTaskProgress\x12V\n\x05state\x18\x01 \x01(\x0e2B.google.cloud.osconfig.agentendpoint.v1.ExecStepTaskProgress.StateB\x03\xe0A\x02"+\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07STARTED\x10\x01"\xcf\x01\n\x12ExecStepTaskOutput\x12T\n\x05state\x18\x01 \x01(\x0e2@.google.cloud.osconfig.agentendpoint.v1.ExecStepTaskOutput.StateB\x03\xe0A\x02\x12\x16\n\texit_code\x18\x02 \x01(\x05B\x03\xe0A\x02"K\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tCOMPLETED\x10\x01\x12\r\n\tTIMED_OUT\x10\x02\x12\r\n\tCANCELLED\x10\x03"\xe3\x02\n\x0fApplyConfigTask\x12U\n\x0bos_policies\x18\x01 \x03(\x0b2@.google.cloud.osconfig.agentendpoint.v1.ApplyConfigTask.OSPolicy\x1a\xf8\x01\n\x08OSPolicy\x12\n\n\x02id\x18\x01 \x01(\t\x12C\n\x04mode\x18\x02 \x01(\x0e25.google.cloud.osconfig.agentendpoint.v1.OSPolicy.Mode\x12M\n\x14os_policy_assignment\x18\x03 \x01(\tB/\xfaA,\n*osconfig.googleapis.com/OSPolicyAssignment\x12L\n\tresources\x18\x04 \x03(\x0b29.google.cloud.osconfig.agentendpoint.v1.OSPolicy.Resource"\xb1\x01\n\x17ApplyConfigTaskProgress\x12T\n\x05state\x18\x01 \x01(\x0e2E.google.cloud.osconfig.agentendpoint.v1.ApplyConfigTaskProgress.State"@\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07STARTED\x10\x01\x12\x13\n\x0fAPPLYING_CONFIG\x10\x02"\x87\x04\n\x15ApplyConfigTaskOutput\x12W\n\x05state\x18\x01 \x01(\x0e2C.google.cloud.osconfig.agentendpoint.v1.ApplyConfigTaskOutput.StateB\x03\xe0A\x02\x12g\n\x11os_policy_results\x18\x02 \x03(\x0b2L.google.cloud.osconfig.agentendpoint.v1.ApplyConfigTaskOutput.OSPolicyResult\x1a\xe1\x01\n\x0eOSPolicyResult\x12\x14\n\x0cos_policy_id\x18\x01 \x01(\t\x12M\n\x14os_policy_assignment\x18\x02 \x01(\tB/\xfaA,\n*osconfig.googleapis.com/OSPolicyAssignment\x12j\n\x1eos_policy_resource_compliances\x18\x03 \x03(\x0b2B.google.cloud.osconfig.agentendpoint.v1.OSPolicyResourceCompliance"H\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\n\n\x06FAILED\x10\x02\x12\r\n\tCANCELLED\x10\x03*G\n\rTaskDirective\x12\x1e\n\x1aTASK_DIRECTIVE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CONTINUE\x10\x01\x12\x08\n\x04STOP\x10\x02*c\n\x08TaskType\x12\x19\n\x15TASK_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rAPPLY_PATCHES\x10\x01\x12\x12\n\x0eEXEC_STEP_TASK\x10\x02\x12\x15\n\x11APPLY_CONFIG_TASK\x10\x03B\x8b\x02\n*com.google.cloud.osconfig.agentendpoint.v1B\x05TasksP\x01ZPcloud.google.com/go/osconfig/agentendpoint/apiv1/agentendpointpb;agentendpointpb\xeaA\x80\x01\n*osconfig.googleapis.com/OSPolicyAssignment\x12Rprojects/{project}/locations/{location}/osPolicyAssignments/{os_policy_assignment}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.osconfig.agentendpoint.v1.tasks_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.osconfig.agentendpoint.v1B\x05TasksP\x01ZPcloud.google.com/go/osconfig/agentendpoint/apiv1/agentendpointpb;agentendpointpb\xeaA\x80\x01\n*osconfig.googleapis.com/OSPolicyAssignment\x12Rprojects/{project}/locations/{location}/osPolicyAssignments/{os_policy_assignment}'
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
    _globals['_APPLYCONFIGTASK_OSPOLICY'].fields_by_name['os_policy_assignment']._loaded_options = None
    _globals['_APPLYCONFIGTASK_OSPOLICY'].fields_by_name['os_policy_assignment']._serialized_options = b'\xfaA,\n*osconfig.googleapis.com/OSPolicyAssignment'
    _globals['_APPLYCONFIGTASKOUTPUT_OSPOLICYRESULT'].fields_by_name['os_policy_assignment']._loaded_options = None
    _globals['_APPLYCONFIGTASKOUTPUT_OSPOLICYRESULT'].fields_by_name['os_policy_assignment']._serialized_options = b'\xfaA,\n*osconfig.googleapis.com/OSPolicyAssignment'
    _globals['_APPLYCONFIGTASKOUTPUT'].fields_by_name['state']._loaded_options = None
    _globals['_APPLYCONFIGTASKOUTPUT'].fields_by_name['state']._serialized_options = b'\xe0A\x02'
    _globals['_TASKDIRECTIVE']._serialized_start = 2974
    _globals['_TASKDIRECTIVE']._serialized_end = 3045
    _globals['_TASKTYPE']._serialized_start = 3047
    _globals['_TASKTYPE']._serialized_end = 3146
    _globals['_TASK']._serialized_start = 328
    _globals['_TASK']._serialized_end = 912
    _globals['_TASK_SERVICELABELSENTRY']._serialized_start = 844
    _globals['_TASK_SERVICELABELSENTRY']._serialized_end = 896
    _globals['_APPLYPATCHESTASK']._serialized_start = 914
    _globals['_APPLYPATCHESTASK']._serialized_end = 1024
    _globals['_APPLYPATCHESTASKPROGRESS']._serialized_start = 1027
    _globals['_APPLYPATCHESTASKPROGRESS']._serialized_end = 1252
    _globals['_APPLYPATCHESTASKPROGRESS_STATE']._serialized_start = 1147
    _globals['_APPLYPATCHESTASKPROGRESS_STATE']._serialized_end = 1252
    _globals['_APPLYPATCHESTASKOUTPUT']._serialized_start = 1255
    _globals['_APPLYPATCHESTASKOUTPUT']._serialized_end = 1459
    _globals['_APPLYPATCHESTASKOUTPUT_STATE']._serialized_start = 1371
    _globals['_APPLYPATCHESTASKOUTPUT_STATE']._serialized_end = 1459
    _globals['_EXECSTEPTASK']._serialized_start = 1461
    _globals['_EXECSTEPTASK']._serialized_end = 1544
    _globals['_EXECSTEPTASKPROGRESS']._serialized_start = 1547
    _globals['_EXECSTEPTASKPROGRESS']._serialized_end = 1702
    _globals['_EXECSTEPTASKPROGRESS_STATE']._serialized_start = 1659
    _globals['_EXECSTEPTASKPROGRESS_STATE']._serialized_end = 1702
    _globals['_EXECSTEPTASKOUTPUT']._serialized_start = 1705
    _globals['_EXECSTEPTASKOUTPUT']._serialized_end = 1912
    _globals['_EXECSTEPTASKOUTPUT_STATE']._serialized_start = 1837
    _globals['_EXECSTEPTASKOUTPUT_STATE']._serialized_end = 1912
    _globals['_APPLYCONFIGTASK']._serialized_start = 1915
    _globals['_APPLYCONFIGTASK']._serialized_end = 2270
    _globals['_APPLYCONFIGTASK_OSPOLICY']._serialized_start = 2022
    _globals['_APPLYCONFIGTASK_OSPOLICY']._serialized_end = 2270
    _globals['_APPLYCONFIGTASKPROGRESS']._serialized_start = 2273
    _globals['_APPLYCONFIGTASKPROGRESS']._serialized_end = 2450
    _globals['_APPLYCONFIGTASKPROGRESS_STATE']._serialized_start = 2386
    _globals['_APPLYCONFIGTASKPROGRESS_STATE']._serialized_end = 2450
    _globals['_APPLYCONFIGTASKOUTPUT']._serialized_start = 2453
    _globals['_APPLYCONFIGTASKOUTPUT']._serialized_end = 2972
    _globals['_APPLYCONFIGTASKOUTPUT_OSPOLICYRESULT']._serialized_start = 2673
    _globals['_APPLYCONFIGTASKOUTPUT_OSPOLICYRESULT']._serialized_end = 2898
    _globals['_APPLYCONFIGTASKOUTPUT_STATE']._serialized_start = 2900
    _globals['_APPLYCONFIGTASKOUTPUT_STATE']._serialized_end = 2972