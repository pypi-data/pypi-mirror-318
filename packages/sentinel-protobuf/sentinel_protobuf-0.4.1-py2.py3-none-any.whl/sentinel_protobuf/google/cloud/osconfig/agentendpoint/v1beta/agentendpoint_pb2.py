"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/osconfig/agentendpoint/v1beta/agentendpoint.proto')
_sym_db = _symbol_database.Default()
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.cloud.osconfig.agentendpoint.v1beta import guest_policies_pb2 as google_dot_cloud_dot_osconfig_dot_agentendpoint_dot_v1beta_dot_guest__policies__pb2
from ......google.cloud.osconfig.agentendpoint.v1beta import tasks_pb2 as google_dot_cloud_dot_osconfig_dot_agentendpoint_dot_v1beta_dot_tasks__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/osconfig/agentendpoint/v1beta/agentendpoint.proto\x12*google.cloud.osconfig.agentendpoint.v1beta\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a?google/cloud/osconfig/agentendpoint/v1beta/guest_policies.proto\x1a6google/cloud/osconfig/agentendpoint/v1beta/tasks.proto"\\\n\x1eReceiveTaskNotificationRequest\x12\x1e\n\x11instance_id_token\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\ragent_version\x18\x02 \x01(\tB\x03\xe0A\x02"!\n\x1fReceiveTaskNotificationResponse"6\n\x14StartNextTaskRequest\x12\x1e\n\x11instance_id_token\x18\x01 \x01(\tB\x03\xe0A\x02"W\n\x15StartNextTaskResponse\x12>\n\x04task\x18\x01 \x01(\x0b20.google.cloud.osconfig.agentendpoint.v1beta.Task"\xfd\x02\n\x19ReportTaskProgressRequest\x12\x1e\n\x11instance_id_token\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07task_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12L\n\ttask_type\x18\x03 \x01(\x0e24.google.cloud.osconfig.agentendpoint.v1beta.TaskTypeB\x03\xe0A\x02\x12k\n\x1bapply_patches_task_progress\x18\x04 \x01(\x0b2D.google.cloud.osconfig.agentendpoint.v1beta.ApplyPatchesTaskProgressH\x00\x12c\n\x17exec_step_task_progress\x18\x05 \x01(\x0b2@.google.cloud.osconfig.agentendpoint.v1beta.ExecStepTaskProgressH\x00B\n\n\x08progress"o\n\x1aReportTaskProgressResponse\x12Q\n\x0etask_directive\x18\x01 \x01(\x0e29.google.cloud.osconfig.agentendpoint.v1beta.TaskDirective"\x8a\x03\n\x19ReportTaskCompleteRequest\x12\x1e\n\x11instance_id_token\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07task_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12L\n\ttask_type\x18\x03 \x01(\x0e24.google.cloud.osconfig.agentendpoint.v1beta.TaskTypeB\x03\xe0A\x02\x12\x15\n\rerror_message\x18\x04 \x01(\t\x12g\n\x19apply_patches_task_output\x18\x05 \x01(\x0b2B.google.cloud.osconfig.agentendpoint.v1beta.ApplyPatchesTaskOutputH\x00\x12_\n\x15exec_step_task_output\x18\x06 \x01(\x0b2>.google.cloud.osconfig.agentendpoint.v1beta.ExecStepTaskOutputH\x00B\x08\n\x06output"\x1c\n\x1aReportTaskCompleteResponse"\xd1\x01\n\x14RegisterAgentRequest\x12\x1e\n\x11instance_id_token\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\ragent_version\x18\x02 \x01(\tB\x03\xe0A\x02\x12#\n\x16supported_capabilities\x18\x03 \x03(\tB\x03\xe0A\x02\x12\x14\n\x0cos_long_name\x18\x04 \x01(\t\x12\x15\n\ros_short_name\x18\x05 \x01(\t\x12\x12\n\nos_version\x18\x06 \x01(\t\x12\x17\n\x0fos_architecture\x18\x07 \x01(\t"\x17\n\x15RegisterAgentResponse2\xa5\n\n\x14AgentEndpointService\x12\xd8\x01\n\x17ReceiveTaskNotification\x12J.google.cloud.osconfig.agentendpoint.v1beta.ReceiveTaskNotificationRequest\x1aK.google.cloud.osconfig.agentendpoint.v1beta.ReceiveTaskNotificationResponse""\xdaA\x1finstance_id_token,agent_version0\x01\x12\xaa\x01\n\rStartNextTask\x12@.google.cloud.osconfig.agentendpoint.v1beta.StartNextTaskRequest\x1aA.google.cloud.osconfig.agentendpoint.v1beta.StartNextTaskResponse"\x14\xdaA\x11instance_id_token\x12\xcb\x01\n\x12ReportTaskProgress\x12E.google.cloud.osconfig.agentendpoint.v1beta.ReportTaskProgressRequest\x1aF.google.cloud.osconfig.agentendpoint.v1beta.ReportTaskProgressResponse"&\xdaA#instance_id_token,task_id,task_type\x12\xd9\x01\n\x12ReportTaskComplete\x12E.google.cloud.osconfig.agentendpoint.v1beta.ReportTaskCompleteRequest\x1aF.google.cloud.osconfig.agentendpoint.v1beta.ReportTaskCompleteResponse"4\xdaA1instance_id_token,task_id,task_type,error_message\x12\xec\x01\n\x1aLookupEffectiveGuestPolicy\x12M.google.cloud.osconfig.agentendpoint.v1beta.LookupEffectiveGuestPolicyRequest\x1a@.google.cloud.osconfig.agentendpoint.v1beta.EffectiveGuestPolicy"=\xdaA:instance_id_token,os_short_name,os_version,os_architecture\x12\xcf\x01\n\rRegisterAgent\x12@.google.cloud.osconfig.agentendpoint.v1beta.RegisterAgentRequest\x1aA.google.cloud.osconfig.agentendpoint.v1beta.RegisterAgentResponse"9\xdaA6instance_id_token,agent_version,supported_capabilities\x1a\x1a\xcaA\x17osconfig.googleapis.comB\xbb\x01\n.com.google.cloud.osconfig.agentendpoint.v1betaB\x12AgentEndpointProtoP\x01ZTcloud.google.com/go/osconfig/agentendpoint/apiv1beta/agentendpointpb;agentendpointpb\xca\x02\x1cGoogle\\Cloud\\OsConfig\\V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.osconfig.agentendpoint.v1beta.agentendpoint_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n.com.google.cloud.osconfig.agentendpoint.v1betaB\x12AgentEndpointProtoP\x01ZTcloud.google.com/go/osconfig/agentendpoint/apiv1beta/agentendpointpb;agentendpointpb\xca\x02\x1cGoogle\\Cloud\\OsConfig\\V1beta'
    _globals['_RECEIVETASKNOTIFICATIONREQUEST'].fields_by_name['instance_id_token']._loaded_options = None
    _globals['_RECEIVETASKNOTIFICATIONREQUEST'].fields_by_name['instance_id_token']._serialized_options = b'\xe0A\x02'
    _globals['_RECEIVETASKNOTIFICATIONREQUEST'].fields_by_name['agent_version']._loaded_options = None
    _globals['_RECEIVETASKNOTIFICATIONREQUEST'].fields_by_name['agent_version']._serialized_options = b'\xe0A\x02'
    _globals['_STARTNEXTTASKREQUEST'].fields_by_name['instance_id_token']._loaded_options = None
    _globals['_STARTNEXTTASKREQUEST'].fields_by_name['instance_id_token']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTTASKPROGRESSREQUEST'].fields_by_name['instance_id_token']._loaded_options = None
    _globals['_REPORTTASKPROGRESSREQUEST'].fields_by_name['instance_id_token']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTTASKPROGRESSREQUEST'].fields_by_name['task_id']._loaded_options = None
    _globals['_REPORTTASKPROGRESSREQUEST'].fields_by_name['task_id']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTTASKPROGRESSREQUEST'].fields_by_name['task_type']._loaded_options = None
    _globals['_REPORTTASKPROGRESSREQUEST'].fields_by_name['task_type']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTTASKCOMPLETEREQUEST'].fields_by_name['instance_id_token']._loaded_options = None
    _globals['_REPORTTASKCOMPLETEREQUEST'].fields_by_name['instance_id_token']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTTASKCOMPLETEREQUEST'].fields_by_name['task_id']._loaded_options = None
    _globals['_REPORTTASKCOMPLETEREQUEST'].fields_by_name['task_id']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTTASKCOMPLETEREQUEST'].fields_by_name['task_type']._loaded_options = None
    _globals['_REPORTTASKCOMPLETEREQUEST'].fields_by_name['task_type']._serialized_options = b'\xe0A\x02'
    _globals['_REGISTERAGENTREQUEST'].fields_by_name['instance_id_token']._loaded_options = None
    _globals['_REGISTERAGENTREQUEST'].fields_by_name['instance_id_token']._serialized_options = b'\xe0A\x02'
    _globals['_REGISTERAGENTREQUEST'].fields_by_name['agent_version']._loaded_options = None
    _globals['_REGISTERAGENTREQUEST'].fields_by_name['agent_version']._serialized_options = b'\xe0A\x02'
    _globals['_REGISTERAGENTREQUEST'].fields_by_name['supported_capabilities']._loaded_options = None
    _globals['_REGISTERAGENTREQUEST'].fields_by_name['supported_capabilities']._serialized_options = b'\xe0A\x02'
    _globals['_AGENTENDPOINTSERVICE']._loaded_options = None
    _globals['_AGENTENDPOINTSERVICE']._serialized_options = b'\xcaA\x17osconfig.googleapis.com'
    _globals['_AGENTENDPOINTSERVICE'].methods_by_name['ReceiveTaskNotification']._loaded_options = None
    _globals['_AGENTENDPOINTSERVICE'].methods_by_name['ReceiveTaskNotification']._serialized_options = b'\xdaA\x1finstance_id_token,agent_version'
    _globals['_AGENTENDPOINTSERVICE'].methods_by_name['StartNextTask']._loaded_options = None
    _globals['_AGENTENDPOINTSERVICE'].methods_by_name['StartNextTask']._serialized_options = b'\xdaA\x11instance_id_token'
    _globals['_AGENTENDPOINTSERVICE'].methods_by_name['ReportTaskProgress']._loaded_options = None
    _globals['_AGENTENDPOINTSERVICE'].methods_by_name['ReportTaskProgress']._serialized_options = b'\xdaA#instance_id_token,task_id,task_type'
    _globals['_AGENTENDPOINTSERVICE'].methods_by_name['ReportTaskComplete']._loaded_options = None
    _globals['_AGENTENDPOINTSERVICE'].methods_by_name['ReportTaskComplete']._serialized_options = b'\xdaA1instance_id_token,task_id,task_type,error_message'
    _globals['_AGENTENDPOINTSERVICE'].methods_by_name['LookupEffectiveGuestPolicy']._loaded_options = None
    _globals['_AGENTENDPOINTSERVICE'].methods_by_name['LookupEffectiveGuestPolicy']._serialized_options = b'\xdaA:instance_id_token,os_short_name,os_version,os_architecture'
    _globals['_AGENTENDPOINTSERVICE'].methods_by_name['RegisterAgent']._loaded_options = None
    _globals['_AGENTENDPOINTSERVICE'].methods_by_name['RegisterAgent']._serialized_options = b'\xdaA6instance_id_token,agent_version,supported_capabilities'
    _globals['_RECEIVETASKNOTIFICATIONREQUEST']._serialized_start = 289
    _globals['_RECEIVETASKNOTIFICATIONREQUEST']._serialized_end = 381
    _globals['_RECEIVETASKNOTIFICATIONRESPONSE']._serialized_start = 383
    _globals['_RECEIVETASKNOTIFICATIONRESPONSE']._serialized_end = 416
    _globals['_STARTNEXTTASKREQUEST']._serialized_start = 418
    _globals['_STARTNEXTTASKREQUEST']._serialized_end = 472
    _globals['_STARTNEXTTASKRESPONSE']._serialized_start = 474
    _globals['_STARTNEXTTASKRESPONSE']._serialized_end = 561
    _globals['_REPORTTASKPROGRESSREQUEST']._serialized_start = 564
    _globals['_REPORTTASKPROGRESSREQUEST']._serialized_end = 945
    _globals['_REPORTTASKPROGRESSRESPONSE']._serialized_start = 947
    _globals['_REPORTTASKPROGRESSRESPONSE']._serialized_end = 1058
    _globals['_REPORTTASKCOMPLETEREQUEST']._serialized_start = 1061
    _globals['_REPORTTASKCOMPLETEREQUEST']._serialized_end = 1455
    _globals['_REPORTTASKCOMPLETERESPONSE']._serialized_start = 1457
    _globals['_REPORTTASKCOMPLETERESPONSE']._serialized_end = 1485
    _globals['_REGISTERAGENTREQUEST']._serialized_start = 1488
    _globals['_REGISTERAGENTREQUEST']._serialized_end = 1697
    _globals['_REGISTERAGENTRESPONSE']._serialized_start = 1699
    _globals['_REGISTERAGENTRESPONSE']._serialized_end = 1722
    _globals['_AGENTENDPOINTSERVICE']._serialized_start = 1725
    _globals['_AGENTENDPOINTSERVICE']._serialized_end = 3042