"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/osconfig/v1beta/patch_deployments.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.osconfig.v1beta import patch_jobs_pb2 as google_dot_cloud_dot_osconfig_dot_v1beta_dot_patch__jobs__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import datetime_pb2 as google_dot_type_dot_datetime__pb2
from .....google.type import dayofweek_pb2 as google_dot_type_dot_dayofweek__pb2
from .....google.type import timeofday_pb2 as google_dot_type_dot_timeofday__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/osconfig/v1beta/patch_deployments.proto\x12\x1cgoogle.cloud.osconfig.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/osconfig/v1beta/patch_jobs.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoogle/type/datetime.proto\x1a\x1bgoogle/type/dayofweek.proto\x1a\x1bgoogle/type/timeofday.proto"\x84\x07\n\x0fPatchDeployment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01\x12O\n\x0finstance_filter\x18\x03 \x01(\x0b21.google.cloud.osconfig.v1beta.PatchInstanceFilterB\x03\xe0A\x02\x12D\n\x0cpatch_config\x18\x04 \x01(\x0b2).google.cloud.osconfig.v1beta.PatchConfigB\x03\xe0A\x01\x120\n\x08duration\x18\x05 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x12O\n\x11one_time_schedule\x18\x06 \x01(\x0b2-.google.cloud.osconfig.v1beta.OneTimeScheduleB\x03\xe0A\x02H\x00\x12R\n\x12recurring_schedule\x18\x07 \x01(\x0b2/.google.cloud.osconfig.v1beta.RecurringScheduleB\x03\xe0A\x02H\x00\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12:\n\x11last_execute_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12@\n\x07rollout\x18\x0b \x01(\x0b2*.google.cloud.osconfig.v1beta.PatchRolloutB\x03\xe0A\x01\x12G\n\x05state\x18\x0c \x01(\x0e23.google.cloud.osconfig.v1beta.PatchDeployment.StateB\x03\xe0A\x03"6\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\n\n\x06PAUSED\x10\x02:d\xeaAa\n\'osconfig.googleapis.com/PatchDeployment\x126projects/{project}/patchDeployments/{patch_deployment}B\n\n\x08schedule"H\n\x0fOneTimeSchedule\x125\n\x0cexecute_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02"\x92\x05\n\x11RecurringSchedule\x12-\n\ttime_zone\x18\x01 \x01(\x0b2\x15.google.type.TimeZoneB\x03\xe0A\x02\x123\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x121\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x120\n\x0btime_of_day\x18\x04 \x01(\x0b2\x16.google.type.TimeOfDayB\x03\xe0A\x02\x12Q\n\tfrequency\x18\x05 \x01(\x0e29.google.cloud.osconfig.v1beta.RecurringSchedule.FrequencyB\x03\xe0A\x02\x12C\n\x06weekly\x18\x06 \x01(\x0b2,.google.cloud.osconfig.v1beta.WeeklyScheduleB\x03\xe0A\x02H\x00\x12E\n\x07monthly\x18\x07 \x01(\x0b2-.google.cloud.osconfig.v1beta.MonthlyScheduleB\x03\xe0A\x02H\x00\x12:\n\x11last_execute_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12:\n\x11next_execute_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"J\n\tFrequency\x12\x19\n\x15FREQUENCY_UNSPECIFIED\x10\x00\x12\n\n\x06WEEKLY\x10\x01\x12\x0b\n\x07MONTHLY\x10\x02\x12\t\n\x05DAILY\x10\x03B\x11\n\x0fschedule_config"B\n\x0eWeeklySchedule\x120\n\x0bday_of_week\x18\x01 \x01(\x0e2\x16.google.type.DayOfWeekB\x03\xe0A\x02"\x8b\x01\n\x0fMonthlySchedule\x12N\n\x11week_day_of_month\x18\x01 \x01(\x0b2,.google.cloud.osconfig.v1beta.WeekDayOfMonthB\x03\xe0A\x02H\x00\x12\x18\n\tmonth_day\x18\x02 \x01(\x05B\x03\xe0A\x02H\x00B\x0e\n\x0cday_of_month"v\n\x0eWeekDayOfMonth\x12\x19\n\x0cweek_ordinal\x18\x01 \x01(\x05B\x03\xe0A\x02\x120\n\x0bday_of_week\x18\x02 \x01(\x0e2\x16.google.type.DayOfWeekB\x03\xe0A\x02\x12\x17\n\nday_offset\x18\x03 \x01(\x05B\x03\xe0A\x01"\xa3\x01\n\x1cCreatePatchDeploymentRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12 \n\x13patch_deployment_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12L\n\x10patch_deployment\x18\x03 \x01(\x0b2-.google.cloud.osconfig.v1beta.PatchDeploymentB\x03\xe0A\x02".\n\x19GetPatchDeploymentRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"c\n\x1bListPatchDeploymentsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x81\x01\n\x1cListPatchDeploymentsResponse\x12H\n\x11patch_deployments\x18\x01 \x03(\x0b2-.google.cloud.osconfig.v1beta.PatchDeployment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"1\n\x1cDeletePatchDeploymentRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"\xa2\x01\n\x1cUpdatePatchDeploymentRequest\x12L\n\x10patch_deployment\x18\x01 \x01(\x0b2-.google.cloud.osconfig.v1beta.PatchDeploymentB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\\\n\x1bPausePatchDeploymentRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'osconfig.googleapis.com/PatchDeployment"]\n\x1cResumePatchDeploymentRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'osconfig.googleapis.com/PatchDeploymentBr\n com.google.cloud.osconfig.v1betaB\x10PatchDeploymentsZ<cloud.google.com/go/osconfig/apiv1beta/osconfigpb;osconfigpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.osconfig.v1beta.patch_deployments_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.osconfig.v1betaB\x10PatchDeploymentsZ<cloud.google.com/go/osconfig/apiv1beta/osconfigpb;osconfigpb'
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
    _globals['_CREATEPATCHDEPLOYMENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPATCHDEPLOYMENTREQUEST'].fields_by_name['patch_deployment_id']._loaded_options = None
    _globals['_CREATEPATCHDEPLOYMENTREQUEST'].fields_by_name['patch_deployment_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPATCHDEPLOYMENTREQUEST'].fields_by_name['patch_deployment']._loaded_options = None
    _globals['_CREATEPATCHDEPLOYMENTREQUEST'].fields_by_name['patch_deployment']._serialized_options = b'\xe0A\x02'
    _globals['_GETPATCHDEPLOYMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPATCHDEPLOYMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_LISTPATCHDEPLOYMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPATCHDEPLOYMENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_LISTPATCHDEPLOYMENTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTPATCHDEPLOYMENTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPATCHDEPLOYMENTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTPATCHDEPLOYMENTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEPATCHDEPLOYMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPATCHDEPLOYMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPATCHDEPLOYMENTREQUEST'].fields_by_name['patch_deployment']._loaded_options = None
    _globals['_UPDATEPATCHDEPLOYMENTREQUEST'].fields_by_name['patch_deployment']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPATCHDEPLOYMENTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEPATCHDEPLOYMENTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_PAUSEPATCHDEPLOYMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_PAUSEPATCHDEPLOYMENTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'osconfig.googleapis.com/PatchDeployment"
    _globals['_RESUMEPATCHDEPLOYMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESUMEPATCHDEPLOYMENTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'osconfig.googleapis.com/PatchDeployment"
    _globals['_PATCHDEPLOYMENT']._serialized_start = 379
    _globals['_PATCHDEPLOYMENT']._serialized_end = 1279
    _globals['_PATCHDEPLOYMENT_STATE']._serialized_start = 1111
    _globals['_PATCHDEPLOYMENT_STATE']._serialized_end = 1165
    _globals['_ONETIMESCHEDULE']._serialized_start = 1281
    _globals['_ONETIMESCHEDULE']._serialized_end = 1353
    _globals['_RECURRINGSCHEDULE']._serialized_start = 1356
    _globals['_RECURRINGSCHEDULE']._serialized_end = 2014
    _globals['_RECURRINGSCHEDULE_FREQUENCY']._serialized_start = 1921
    _globals['_RECURRINGSCHEDULE_FREQUENCY']._serialized_end = 1995
    _globals['_WEEKLYSCHEDULE']._serialized_start = 2016
    _globals['_WEEKLYSCHEDULE']._serialized_end = 2082
    _globals['_MONTHLYSCHEDULE']._serialized_start = 2085
    _globals['_MONTHLYSCHEDULE']._serialized_end = 2224
    _globals['_WEEKDAYOFMONTH']._serialized_start = 2226
    _globals['_WEEKDAYOFMONTH']._serialized_end = 2344
    _globals['_CREATEPATCHDEPLOYMENTREQUEST']._serialized_start = 2347
    _globals['_CREATEPATCHDEPLOYMENTREQUEST']._serialized_end = 2510
    _globals['_GETPATCHDEPLOYMENTREQUEST']._serialized_start = 2512
    _globals['_GETPATCHDEPLOYMENTREQUEST']._serialized_end = 2558
    _globals['_LISTPATCHDEPLOYMENTSREQUEST']._serialized_start = 2560
    _globals['_LISTPATCHDEPLOYMENTSREQUEST']._serialized_end = 2659
    _globals['_LISTPATCHDEPLOYMENTSRESPONSE']._serialized_start = 2662
    _globals['_LISTPATCHDEPLOYMENTSRESPONSE']._serialized_end = 2791
    _globals['_DELETEPATCHDEPLOYMENTREQUEST']._serialized_start = 2793
    _globals['_DELETEPATCHDEPLOYMENTREQUEST']._serialized_end = 2842
    _globals['_UPDATEPATCHDEPLOYMENTREQUEST']._serialized_start = 2845
    _globals['_UPDATEPATCHDEPLOYMENTREQUEST']._serialized_end = 3007
    _globals['_PAUSEPATCHDEPLOYMENTREQUEST']._serialized_start = 3009
    _globals['_PAUSEPATCHDEPLOYMENTREQUEST']._serialized_end = 3101
    _globals['_RESUMEPATCHDEPLOYMENTREQUEST']._serialized_start = 3103
    _globals['_RESUMEPATCHDEPLOYMENTREQUEST']._serialized_end = 3196