"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/osconfig/v1/patch_deployments.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.osconfig.v1 import patch_jobs_pb2 as google_dot_cloud_dot_osconfig_dot_v1_dot_patch__jobs__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import datetime_pb2 as google_dot_type_dot_datetime__pb2
from .....google.type import dayofweek_pb2 as google_dot_type_dot_dayofweek__pb2
from .....google.type import timeofday_pb2 as google_dot_type_dot_timeofday__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/osconfig/v1/patch_deployments.proto\x12\x18google.cloud.osconfig.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a)google/cloud/osconfig/v1/patch_jobs.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoogle/type/datetime.proto\x1a\x1bgoogle/type/dayofweek.proto\x1a\x1bgoogle/type/timeofday.proto"\xec\x06\n\x0fPatchDeployment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01\x12K\n\x0finstance_filter\x18\x03 \x01(\x0b2-.google.cloud.osconfig.v1.PatchInstanceFilterB\x03\xe0A\x02\x12@\n\x0cpatch_config\x18\x04 \x01(\x0b2%.google.cloud.osconfig.v1.PatchConfigB\x03\xe0A\x01\x120\n\x08duration\x18\x05 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x12K\n\x11one_time_schedule\x18\x06 \x01(\x0b2).google.cloud.osconfig.v1.OneTimeScheduleB\x03\xe0A\x02H\x00\x12N\n\x12recurring_schedule\x18\x07 \x01(\x0b2+.google.cloud.osconfig.v1.RecurringScheduleB\x03\xe0A\x02H\x00\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12:\n\x11last_execute_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12<\n\x07rollout\x18\x0b \x01(\x0b2&.google.cloud.osconfig.v1.PatchRolloutB\x03\xe0A\x01\x12C\n\x05state\x18\x0c \x01(\x0e2/.google.cloud.osconfig.v1.PatchDeployment.StateB\x03\xe0A\x03"6\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\n\n\x06PAUSED\x10\x02:d\xeaAa\n\'osconfig.googleapis.com/PatchDeployment\x126projects/{project}/patchDeployments/{patch_deployment}B\n\n\x08schedule"H\n\x0fOneTimeSchedule\x125\n\x0cexecute_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02"\x86\x05\n\x11RecurringSchedule\x12-\n\ttime_zone\x18\x01 \x01(\x0b2\x15.google.type.TimeZoneB\x03\xe0A\x02\x123\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x121\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x120\n\x0btime_of_day\x18\x04 \x01(\x0b2\x16.google.type.TimeOfDayB\x03\xe0A\x02\x12M\n\tfrequency\x18\x05 \x01(\x0e25.google.cloud.osconfig.v1.RecurringSchedule.FrequencyB\x03\xe0A\x02\x12?\n\x06weekly\x18\x06 \x01(\x0b2(.google.cloud.osconfig.v1.WeeklyScheduleB\x03\xe0A\x02H\x00\x12A\n\x07monthly\x18\x07 \x01(\x0b2).google.cloud.osconfig.v1.MonthlyScheduleB\x03\xe0A\x02H\x00\x12:\n\x11last_execute_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12:\n\x11next_execute_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"J\n\tFrequency\x12\x19\n\x15FREQUENCY_UNSPECIFIED\x10\x00\x12\n\n\x06WEEKLY\x10\x01\x12\x0b\n\x07MONTHLY\x10\x02\x12\t\n\x05DAILY\x10\x03B\x11\n\x0fschedule_config"B\n\x0eWeeklySchedule\x120\n\x0bday_of_week\x18\x01 \x01(\x0e2\x16.google.type.DayOfWeekB\x03\xe0A\x02"\x87\x01\n\x0fMonthlySchedule\x12J\n\x11week_day_of_month\x18\x01 \x01(\x0b2(.google.cloud.osconfig.v1.WeekDayOfMonthB\x03\xe0A\x02H\x00\x12\x18\n\tmonth_day\x18\x02 \x01(\x05B\x03\xe0A\x02H\x00B\x0e\n\x0cday_of_month"v\n\x0eWeekDayOfMonth\x12\x19\n\x0cweek_ordinal\x18\x01 \x01(\x05B\x03\xe0A\x02\x120\n\x0bday_of_week\x18\x02 \x01(\x0e2\x16.google.type.DayOfWeekB\x03\xe0A\x02\x12\x17\n\nday_offset\x18\x03 \x01(\x05B\x03\xe0A\x01"\xcf\x01\n\x1cCreatePatchDeploymentRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12 \n\x13patch_deployment_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12H\n\x10patch_deployment\x18\x03 \x01(\x0b2).google.cloud.osconfig.v1.PatchDeploymentB\x03\xe0A\x02"Z\n\x19GetPatchDeploymentRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'osconfig.googleapis.com/PatchDeployment"\x93\x01\n\x1bListPatchDeploymentsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"}\n\x1cListPatchDeploymentsResponse\x12D\n\x11patch_deployments\x18\x01 \x03(\x0b2).google.cloud.osconfig.v1.PatchDeployment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"]\n\x1cDeletePatchDeploymentRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'osconfig.googleapis.com/PatchDeployment"\x9e\x01\n\x1cUpdatePatchDeploymentRequest\x12H\n\x10patch_deployment\x18\x01 \x01(\x0b2).google.cloud.osconfig.v1.PatchDeploymentB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\\\n\x1bPausePatchDeploymentRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'osconfig.googleapis.com/PatchDeployment"]\n\x1cResumePatchDeploymentRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'osconfig.googleapis.com/PatchDeploymentB\xbe\x01\n\x1ccom.google.cloud.osconfig.v1B\x10PatchDeploymentsZ8cloud.google.com/go/osconfig/apiv1/osconfigpb;osconfigpb\xaa\x02\x18Google.Cloud.OsConfig.V1\xca\x02\x18Google\\Cloud\\OsConfig\\V1\xea\x02\x1bGoogle::Cloud::OsConfig::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.osconfig.v1.patch_deployments_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.osconfig.v1B\x10PatchDeploymentsZ8cloud.google.com/go/osconfig/apiv1/osconfigpb;osconfigpb\xaa\x02\x18Google.Cloud.OsConfig.V1\xca\x02\x18Google\\Cloud\\OsConfig\\V1\xea\x02\x1bGoogle::Cloud::OsConfig::V1'
    _globals['_PATCHDEPLOYMENT'].fields_by_name['description']._loaded_options = None
    _globals['_PATCHDEPLOYMENT'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_PATCHDEPLOYMENT'].fields_by_name['instance_filter']._loaded_options = None
    _globals['_PATCHDEPLOYMENT'].fields_by_name['instance_filter']._serialized_options = b'\xe0A\x02'
    _globals['_PATCHDEPLOYMENT'].fields_by_name['patch_config']._loaded_options = None
    _globals['_PATCHDEPLOYMENT'].fields_by_name['patch_config']._serialized_options = b'\xe0A\x01'
    _globals['_PATCHDEPLOYMENT'].fields_by_name['duration']._loaded_options = None
    _globals['_PATCHDEPLOYMENT'].fields_by_name['duration']._serialized_options = b'\xe0A\x01'
    _globals['_PATCHDEPLOYMENT'].fields_by_name['one_time_schedule']._loaded_options = None
    _globals['_PATCHDEPLOYMENT'].fields_by_name['one_time_schedule']._serialized_options = b'\xe0A\x02'
    _globals['_PATCHDEPLOYMENT'].fields_by_name['recurring_schedule']._loaded_options = None
    _globals['_PATCHDEPLOYMENT'].fields_by_name['recurring_schedule']._serialized_options = b'\xe0A\x02'
    _globals['_PATCHDEPLOYMENT'].fields_by_name['create_time']._loaded_options = None
    _globals['_PATCHDEPLOYMENT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_PATCHDEPLOYMENT'].fields_by_name['update_time']._loaded_options = None
    _globals['_PATCHDEPLOYMENT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_PATCHDEPLOYMENT'].fields_by_name['last_execute_time']._loaded_options = None
    _globals['_PATCHDEPLOYMENT'].fields_by_name['last_execute_time']._serialized_options = b'\xe0A\x03'
    _globals['_PATCHDEPLOYMENT'].fields_by_name['rollout']._loaded_options = None
    _globals['_PATCHDEPLOYMENT'].fields_by_name['rollout']._serialized_options = b'\xe0A\x01'
    _globals['_PATCHDEPLOYMENT'].fields_by_name['state']._loaded_options = None
    _globals['_PATCHDEPLOYMENT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_PATCHDEPLOYMENT']._loaded_options = None
    _globals['_PATCHDEPLOYMENT']._serialized_options = b"\xeaAa\n'osconfig.googleapis.com/PatchDeployment\x126projects/{project}/patchDeployments/{patch_deployment}"
    _globals['_ONETIMESCHEDULE'].fields_by_name['execute_time']._loaded_options = None
    _globals['_ONETIMESCHEDULE'].fields_by_name['execute_time']._serialized_options = b'\xe0A\x02'
    _globals['_RECURRINGSCHEDULE'].fields_by_name['time_zone']._loaded_options = None
    _globals['_RECURRINGSCHEDULE'].fields_by_name['time_zone']._serialized_options = b'\xe0A\x02'
    _globals['_RECURRINGSCHEDULE'].fields_by_name['start_time']._loaded_options = None
    _globals['_RECURRINGSCHEDULE'].fields_by_name['start_time']._serialized_options = b'\xe0A\x01'
    _globals['_RECURRINGSCHEDULE'].fields_by_name['end_time']._loaded_options = None
    _globals['_RECURRINGSCHEDULE'].fields_by_name['end_time']._serialized_options = b'\xe0A\x01'
    _globals['_RECURRINGSCHEDULE'].fields_by_name['time_of_day']._loaded_options = None
    _globals['_RECURRINGSCHEDULE'].fields_by_name['time_of_day']._serialized_options = b'\xe0A\x02'
    _globals['_RECURRINGSCHEDULE'].fields_by_name['frequency']._loaded_options = None
    _globals['_RECURRINGSCHEDULE'].fields_by_name['frequency']._serialized_options = b'\xe0A\x02'
    _globals['_RECURRINGSCHEDULE'].fields_by_name['weekly']._loaded_options = None
    _globals['_RECURRINGSCHEDULE'].fields_by_name['weekly']._serialized_options = b'\xe0A\x02'
    _globals['_RECURRINGSCHEDULE'].fields_by_name['monthly']._loaded_options = None
    _globals['_RECURRINGSCHEDULE'].fields_by_name['monthly']._serialized_options = b'\xe0A\x02'
    _globals['_RECURRINGSCHEDULE'].fields_by_name['last_execute_time']._loaded_options = None
    _globals['_RECURRINGSCHEDULE'].fields_by_name['last_execute_time']._serialized_options = b'\xe0A\x03'
    _globals['_RECURRINGSCHEDULE'].fields_by_name['next_execute_time']._loaded_options = None
    _globals['_RECURRINGSCHEDULE'].fields_by_name['next_execute_time']._serialized_options = b'\xe0A\x03'
    _globals['_WEEKLYSCHEDULE'].fields_by_name['day_of_week']._loaded_options = None
    _globals['_WEEKLYSCHEDULE'].fields_by_name['day_of_week']._serialized_options = b'\xe0A\x02'
    _globals['_MONTHLYSCHEDULE'].fields_by_name['week_day_of_month']._loaded_options = None
    _globals['_MONTHLYSCHEDULE'].fields_by_name['week_day_of_month']._serialized_options = b'\xe0A\x02'
    _globals['_MONTHLYSCHEDULE'].fields_by_name['month_day']._loaded_options = None
    _globals['_MONTHLYSCHEDULE'].fields_by_name['month_day']._serialized_options = b'\xe0A\x02'
    _globals['_WEEKDAYOFMONTH'].fields_by_name['week_ordinal']._loaded_options = None
    _globals['_WEEKDAYOFMONTH'].fields_by_name['week_ordinal']._serialized_options = b'\xe0A\x02'
    _globals['_WEEKDAYOFMONTH'].fields_by_name['day_of_week']._loaded_options = None
    _globals['_WEEKDAYOFMONTH'].fields_by_name['day_of_week']._serialized_options = b'\xe0A\x02'
    _globals['_WEEKDAYOFMONTH'].fields_by_name['day_offset']._loaded_options = None
    _globals['_WEEKDAYOFMONTH'].fields_by_name['day_offset']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEPATCHDEPLOYMENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPATCHDEPLOYMENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_CREATEPATCHDEPLOYMENTREQUEST'].fields_by_name['patch_deployment_id']._loaded_options = None
    _globals['_CREATEPATCHDEPLOYMENTREQUEST'].fields_by_name['patch_deployment_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPATCHDEPLOYMENTREQUEST'].fields_by_name['patch_deployment']._loaded_options = None
    _globals['_CREATEPATCHDEPLOYMENTREQUEST'].fields_by_name['patch_deployment']._serialized_options = b'\xe0A\x02'
    _globals['_GETPATCHDEPLOYMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPATCHDEPLOYMENTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'osconfig.googleapis.com/PatchDeployment"
    _globals['_LISTPATCHDEPLOYMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPATCHDEPLOYMENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_LISTPATCHDEPLOYMENTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTPATCHDEPLOYMENTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPATCHDEPLOYMENTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTPATCHDEPLOYMENTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEPATCHDEPLOYMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPATCHDEPLOYMENTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'osconfig.googleapis.com/PatchDeployment"
    _globals['_UPDATEPATCHDEPLOYMENTREQUEST'].fields_by_name['patch_deployment']._loaded_options = None
    _globals['_UPDATEPATCHDEPLOYMENTREQUEST'].fields_by_name['patch_deployment']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPATCHDEPLOYMENTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEPATCHDEPLOYMENTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_PAUSEPATCHDEPLOYMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_PAUSEPATCHDEPLOYMENTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'osconfig.googleapis.com/PatchDeployment"
    _globals['_RESUMEPATCHDEPLOYMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESUMEPATCHDEPLOYMENTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'osconfig.googleapis.com/PatchDeployment"
    _globals['_PATCHDEPLOYMENT']._serialized_start = 367
    _globals['_PATCHDEPLOYMENT']._serialized_end = 1243
    _globals['_PATCHDEPLOYMENT_STATE']._serialized_start = 1075
    _globals['_PATCHDEPLOYMENT_STATE']._serialized_end = 1129
    _globals['_ONETIMESCHEDULE']._serialized_start = 1245
    _globals['_ONETIMESCHEDULE']._serialized_end = 1317
    _globals['_RECURRINGSCHEDULE']._serialized_start = 1320
    _globals['_RECURRINGSCHEDULE']._serialized_end = 1966
    _globals['_RECURRINGSCHEDULE_FREQUENCY']._serialized_start = 1873
    _globals['_RECURRINGSCHEDULE_FREQUENCY']._serialized_end = 1947
    _globals['_WEEKLYSCHEDULE']._serialized_start = 1968
    _globals['_WEEKLYSCHEDULE']._serialized_end = 2034
    _globals['_MONTHLYSCHEDULE']._serialized_start = 2037
    _globals['_MONTHLYSCHEDULE']._serialized_end = 2172
    _globals['_WEEKDAYOFMONTH']._serialized_start = 2174
    _globals['_WEEKDAYOFMONTH']._serialized_end = 2292
    _globals['_CREATEPATCHDEPLOYMENTREQUEST']._serialized_start = 2295
    _globals['_CREATEPATCHDEPLOYMENTREQUEST']._serialized_end = 2502
    _globals['_GETPATCHDEPLOYMENTREQUEST']._serialized_start = 2504
    _globals['_GETPATCHDEPLOYMENTREQUEST']._serialized_end = 2594
    _globals['_LISTPATCHDEPLOYMENTSREQUEST']._serialized_start = 2597
    _globals['_LISTPATCHDEPLOYMENTSREQUEST']._serialized_end = 2744
    _globals['_LISTPATCHDEPLOYMENTSRESPONSE']._serialized_start = 2746
    _globals['_LISTPATCHDEPLOYMENTSRESPONSE']._serialized_end = 2871
    _globals['_DELETEPATCHDEPLOYMENTREQUEST']._serialized_start = 2873
    _globals['_DELETEPATCHDEPLOYMENTREQUEST']._serialized_end = 2966
    _globals['_UPDATEPATCHDEPLOYMENTREQUEST']._serialized_start = 2969
    _globals['_UPDATEPATCHDEPLOYMENTREQUEST']._serialized_end = 3127
    _globals['_PAUSEPATCHDEPLOYMENTREQUEST']._serialized_start = 3129
    _globals['_PAUSEPATCHDEPLOYMENTREQUEST']._serialized_end = 3221
    _globals['_RESUMEPATCHDEPLOYMENTREQUEST']._serialized_start = 3223
    _globals['_RESUMEPATCHDEPLOYMENTREQUEST']._serialized_end = 3316