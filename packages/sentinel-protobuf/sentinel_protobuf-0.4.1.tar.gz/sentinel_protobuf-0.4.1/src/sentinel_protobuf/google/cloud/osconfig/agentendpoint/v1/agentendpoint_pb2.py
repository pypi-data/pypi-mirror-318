"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/osconfig/agentendpoint/v1/agentendpoint.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.cloud.osconfig.agentendpoint.v1 import inventory_pb2 as google_dot_cloud_dot_osconfig_dot_agentendpoint_dot_v1_dot_inventory__pb2
from ......google.cloud.osconfig.agentendpoint.v1 import tasks_pb2 as google_dot_cloud_dot_osconfig_dot_agentendpoint_dot_v1_dot_tasks__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/osconfig/agentendpoint/v1/agentendpoint.proto\x12&google.cloud.osconfig.agentendpoint.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a6google/cloud/osconfig/agentendpoint/v1/inventory.proto\x1a2google/cloud/osconfig/agentendpoint/v1/tasks.proto"\\\n\x1eReceiveTaskNotificationRequest\x12\x1e\n\x11instance_id_token\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\ragent_version\x18\x02 \x01(\tB\x03\xe0A\x02"!\n\x1fReceiveTaskNotificationResponse"6\n\x14StartNextTaskRequest\x12\x1e\n\x11instance_id_token\x18\x01 \x01(\tB\x03\xe0A\x02"S\n\x15StartNextTaskResponse\x12:\n\x04task\x18\x01 \x01(\x0b2,.google.cloud.osconfig.agentendpoint.v1.Task"\xd8\x03\n\x19ReportTaskProgressRequest\x12\x1e\n\x11instance_id_token\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07task_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12H\n\ttask_type\x18\x03 \x01(\x0e20.google.cloud.osconfig.agentendpoint.v1.TaskTypeB\x03\xe0A\x02\x12g\n\x1bapply_patches_task_progress\x18\x04 \x01(\x0b2@.google.cloud.osconfig.agentendpoint.v1.ApplyPatchesTaskProgressH\x00\x12_\n\x17exec_step_task_progress\x18\x05 \x01(\x0b2<.google.cloud.osconfig.agentendpoint.v1.ExecStepTaskProgressH\x00\x12e\n\x1aapply_config_task_progress\x18\x06 \x01(\x0b2?.google.cloud.osconfig.agentendpoint.v1.ApplyConfigTaskProgressH\x00B\n\n\x08progress"k\n\x1aReportTaskProgressResponse\x12M\n\x0etask_directive\x18\x01 \x01(\x0e25.google.cloud.osconfig.agentendpoint.v1.TaskDirective"\xe1\x03\n\x19ReportTaskCompleteRequest\x12\x1e\n\x11instance_id_token\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07task_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12H\n\ttask_type\x18\x03 \x01(\x0e20.google.cloud.osconfig.agentendpoint.v1.TaskTypeB\x03\xe0A\x02\x12\x15\n\rerror_message\x18\x04 \x01(\t\x12c\n\x19apply_patches_task_output\x18\x05 \x01(\x0b2>.google.cloud.osconfig.agentendpoint.v1.ApplyPatchesTaskOutputH\x00\x12[\n\x15exec_step_task_output\x18\x06 \x01(\x0b2:.google.cloud.osconfig.agentendpoint.v1.ExecStepTaskOutputH\x00\x12a\n\x18apply_config_task_output\x18\x07 \x01(\x0b2=.google.cloud.osconfig.agentendpoint.v1.ApplyConfigTaskOutputH\x00B\x08\n\x06output"\x1c\n\x1aReportTaskCompleteResponse"\xd1\x01\n\x14RegisterAgentRequest\x12\x1e\n\x11instance_id_token\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\ragent_version\x18\x02 \x01(\tB\x03\xe0A\x02\x12#\n\x16supported_capabilities\x18\x03 \x03(\tB\x03\xe0A\x02\x12\x14\n\x0cos_long_name\x18\x04 \x01(\t\x12\x15\n\ros_short_name\x18\x05 \x01(\t\x12\x12\n\nos_version\x18\x06 \x01(\t\x12\x17\n\x0fos_architecture\x18\x07 \x01(\t"\x17\n\x15RegisterAgentResponse"\xa4\x01\n\x16ReportInventoryRequest\x12\x1e\n\x11instance_id_token\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1f\n\x12inventory_checksum\x18\x02 \x01(\tB\x03\xe0A\x02\x12I\n\tinventory\x18\x03 \x01(\x0b21.google.cloud.osconfig.agentendpoint.v1.InventoryB\x03\xe0A\x01"8\n\x17ReportInventoryResponse\x12\x1d\n\x15report_full_inventory\x18\x01 \x01(\x082\xd6\t\n\x14AgentEndpointService\x12\xd0\x01\n\x17ReceiveTaskNotification\x12F.google.cloud.osconfig.agentendpoint.v1.ReceiveTaskNotificationRequest\x1aG.google.cloud.osconfig.agentendpoint.v1.ReceiveTaskNotificationResponse""\xdaA\x1finstance_id_token,agent_version0\x01\x12\xa2\x01\n\rStartNextTask\x12<.google.cloud.osconfig.agentendpoint.v1.StartNextTaskRequest\x1a=.google.cloud.osconfig.agentendpoint.v1.StartNextTaskResponse"\x14\xdaA\x11instance_id_token\x12\xc3\x01\n\x12ReportTaskProgress\x12A.google.cloud.osconfig.agentendpoint.v1.ReportTaskProgressRequest\x1aB.google.cloud.osconfig.agentendpoint.v1.ReportTaskProgressResponse"&\xdaA#instance_id_token,task_id,task_type\x12\xd1\x01\n\x12ReportTaskComplete\x12A.google.cloud.osconfig.agentendpoint.v1.ReportTaskCompleteRequest\x1aB.google.cloud.osconfig.agentendpoint.v1.ReportTaskCompleteResponse"4\xdaA1instance_id_token,task_id,task_type,error_message\x12\xc7\x01\n\rRegisterAgent\x12<.google.cloud.osconfig.agentendpoint.v1.RegisterAgentRequest\x1a=.google.cloud.osconfig.agentendpoint.v1.RegisterAgentResponse"9\xdaA6instance_id_token,agent_version,supported_capabilities\x12\xc5\x01\n\x0fReportInventory\x12>.google.cloud.osconfig.agentendpoint.v1.ReportInventoryRequest\x1a?.google.cloud.osconfig.agentendpoint.v1.ReportInventoryResponse"1\xdaA.instance_id_token,inventory_checksum,inventory\x1a\x1a\xcaA\x17osconfig.googleapis.comB\x94\x01\n*com.google.cloud.osconfig.agentendpoint.v1B\x12AgentEndpointProtoP\x01ZPcloud.google.com/go/osconfig/agentendpoint/apiv1/agentendpointpb;agentendpointpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.osconfig.agentendpoint.v1.agentendpoint_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.osconfig.agentendpoint.v1B\x12AgentEndpointProtoP\x01ZPcloud.google.com/go/osconfig/agentendpoint/apiv1/agentendpointpb;agentendpointpb'
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
    _globals['_REPORTINVENTORYREQUEST'].fields_by_name['instance_id_token']._loaded_options = None
    _globals['_REPORTINVENTORYREQUEST'].fields_by_name['instance_id_token']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTINVENTORYREQUEST'].fields_by_name['inventory_checksum']._loaded_options = None
    _globals['_REPORTINVENTORYREQUEST'].fields_by_name['inventory_checksum']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTINVENTORYREQUEST'].fields_by_name['inventory']._loaded_options = None
    _globals['_REPORTINVENTORYREQUEST'].fields_by_name['inventory']._serialized_options = b'\xe0A\x01'
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
    _globals['_AGENTENDPOINTSERVICE'].methods_by_name['RegisterAgent']._loaded_options = None
    _globals['_AGENTENDPOINTSERVICE'].methods_by_name['RegisterAgent']._serialized_options = b'\xdaA6instance_id_token,agent_version,supported_capabilities'
    _globals['_AGENTENDPOINTSERVICE'].methods_by_name['ReportInventory']._loaded_options = None
    _globals['_AGENTENDPOINTSERVICE'].methods_by_name['ReportInventory']._serialized_options = b'\xdaA.instance_id_token,inventory_checksum,inventory'
    _globals['_RECEIVETASKNOTIFICATIONREQUEST']._serialized_start = 298
    _globals['_RECEIVETASKNOTIFICATIONREQUEST']._serialized_end = 390
    _globals['_RECEIVETASKNOTIFICATIONRESPONSE']._serialized_start = 392
    _globals['_RECEIVETASKNOTIFICATIONRESPONSE']._serialized_end = 425
    _globals['_STARTNEXTTASKREQUEST']._serialized_start = 427
    _globals['_STARTNEXTTASKREQUEST']._serialized_end = 481
    _globals['_STARTNEXTTASKRESPONSE']._serialized_start = 483
    _globals['_STARTNEXTTASKRESPONSE']._serialized_end = 566
    _globals['_REPORTTASKPROGRESSREQUEST']._serialized_start = 569
    _globals['_REPORTTASKPROGRESSREQUEST']._serialized_end = 1041
    _globals['_REPORTTASKPROGRESSRESPONSE']._serialized_start = 1043
    _globals['_REPORTTASKPROGRESSRESPONSE']._serialized_end = 1150
    _globals['_REPORTTASKCOMPLETEREQUEST']._serialized_start = 1153
    _globals['_REPORTTASKCOMPLETEREQUEST']._serialized_end = 1634
    _globals['_REPORTTASKCOMPLETERESPONSE']._serialized_start = 1636
    _globals['_REPORTTASKCOMPLETERESPONSE']._serialized_end = 1664
    _globals['_REGISTERAGENTREQUEST']._serialized_start = 1667
    _globals['_REGISTERAGENTREQUEST']._serialized_end = 1876
    _globals['_REGISTERAGENTRESPONSE']._serialized_start = 1878
    _globals['_REGISTERAGENTRESPONSE']._serialized_end = 1901
    _globals['_REPORTINVENTORYREQUEST']._serialized_start = 1904
    _globals['_REPORTINVENTORYREQUEST']._serialized_end = 2068
    _globals['_REPORTINVENTORYRESPONSE']._serialized_start = 2070
    _globals['_REPORTINVENTORYRESPONSE']._serialized_end = 2126
    _globals['_AGENTENDPOINTSERVICE']._serialized_start = 2129
    _globals['_AGENTENDPOINTSERVICE']._serialized_end = 3367