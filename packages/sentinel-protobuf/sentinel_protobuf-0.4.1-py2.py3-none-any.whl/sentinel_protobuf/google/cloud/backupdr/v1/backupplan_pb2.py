"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/backupdr/v1/backupplan.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import dayofweek_pb2 as google_dot_type_dot_dayofweek__pb2
from .....google.type import month_pb2 as google_dot_type_dot_month__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/backupdr/v1/backupplan.proto\x12\x18google.cloud.backupdr.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/type/dayofweek.proto\x1a\x17google/type/month.proto"\x99\x06\n\nBackupPlan\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x08\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01\x12E\n\x06labels\x18\x03 \x03(\x0b20.google.cloud.backupdr.v1.BackupPlan.LabelsEntryB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12?\n\x0cbackup_rules\x18\x06 \x03(\x0b2$.google.cloud.backupdr.v1.BackupRuleB\x03\xe0A\x02\x12>\n\x05state\x18\x07 \x01(\x0e2*.google.cloud.backupdr.v1.BackupPlan.StateB\x03\xe0A\x03\x12\x1a\n\rresource_type\x18\x08 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04etag\x18\t \x01(\tB\x03\xe0A\x01\x12A\n\x0cbackup_vault\x18\n \x01(\tB+\xe0A\x02\xfaA%\n#backupdr.googleapis.com/BackupVault\x12)\n\x1cbackup_vault_service_account\x18\x0b \x01(\tB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"T\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\x0c\n\x08INACTIVE\x10\x04:\x84\x01\xeaA\x80\x01\n"backupdr.googleapis.com/BackupPlan\x12Aprojects/{project}/locations/{location}/backupPlans/{backup_plan}*\x0bbackupPlans2\nbackupPlan"\xb0\x01\n\nBackupRule\x12\x17\n\x07rule_id\x18\x01 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12"\n\x15backup_retention_days\x18\x04 \x01(\x05B\x03\xe0A\x02\x12L\n\x11standard_schedule\x18\x05 \x01(\x0b2*.google.cloud.backupdr.v1.StandardScheduleB\x03\xe0A\x02H\x00B\x17\n\x15backup_schedule_oneof"\x97\x04\n\x10StandardSchedule\x12W\n\x0frecurrence_type\x18\x01 \x01(\x0e29.google.cloud.backupdr.v1.StandardSchedule.RecurrenceTypeB\x03\xe0A\x02\x12\x1d\n\x10hourly_frequency\x18\x02 \x01(\x05B\x03\xe0A\x01\x121\n\x0cdays_of_week\x18\x03 \x03(\x0e2\x16.google.type.DayOfWeekB\x03\xe0A\x01\x12\x1a\n\rdays_of_month\x18\x04 \x03(\x05B\x03\xe0A\x01\x12H\n\x11week_day_of_month\x18\x05 \x01(\x0b2(.google.cloud.backupdr.v1.WeekDayOfMonthB\x03\xe0A\x01\x12\'\n\x06months\x18\x06 \x03(\x0e2\x12.google.type.MonthB\x03\xe0A\x01\x12B\n\rbackup_window\x18\x07 \x01(\x0b2&.google.cloud.backupdr.v1.BackupWindowB\x03\xe0A\x02\x12\x16\n\ttime_zone\x18\x08 \x01(\tB\x03\xe0A\x02"m\n\x0eRecurrenceType\x12\x1f\n\x1bRECURRENCE_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06HOURLY\x10\x01\x12\t\n\x05DAILY\x10\x02\x12\n\n\x06WEEKLY\x10\x03\x12\x0b\n\x07MONTHLY\x10\x04\x12\n\n\x06YEARLY\x10\x05"L\n\x0cBackupWindow\x12\x1e\n\x11start_hour_of_day\x18\x01 \x01(\x05B\x03\xe0A\x02\x12\x1c\n\x0fend_hour_of_day\x18\x02 \x01(\x05B\x03\xe0A\x02"\xfa\x01\n\x0eWeekDayOfMonth\x12P\n\rweek_of_month\x18\x01 \x01(\x0e24.google.cloud.backupdr.v1.WeekDayOfMonth.WeekOfMonthB\x03\xe0A\x02\x120\n\x0bday_of_week\x18\x02 \x01(\x0e2\x16.google.type.DayOfWeekB\x03\xe0A\x02"d\n\x0bWeekOfMonth\x12\x1d\n\x19WEEK_OF_MONTH_UNSPECIFIED\x10\x00\x12\t\n\x05FIRST\x10\x01\x12\n\n\x06SECOND\x10\x02\x12\t\n\x05THIRD\x10\x03\x12\n\n\x06FOURTH\x10\x04\x12\x08\n\x04LAST\x10\x05"\xd3\x01\n\x17CreateBackupPlanRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"backupdr.googleapis.com/BackupPlan\x12\x1b\n\x0ebackup_plan_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12>\n\x0bbackup_plan\x18\x03 \x01(\x0b2$.google.cloud.backupdr.v1.BackupPlanB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x04 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\xb1\x01\n\x16ListBackupPlansRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"backupdr.googleapis.com/BackupPlan\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x83\x01\n\x17ListBackupPlansResponse\x12:\n\x0cbackup_plans\x18\x01 \x03(\x0b2$.google.cloud.backupdr.v1.BackupPlan\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"P\n\x14GetBackupPlanRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"backupdr.googleapis.com/BackupPlan"t\n\x17DeleteBackupPlanRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"backupdr.googleapis.com/BackupPlan\x12\x1f\n\nrequest_id\x18\x02 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01B\xbf\x01\n\x1ccom.google.cloud.backupdr.v1B\x0fBackupPlanProtoP\x01Z8cloud.google.com/go/backupdr/apiv1/backupdrpb;backupdrpb\xaa\x02\x18Google.Cloud.BackupDR.V1\xca\x02\x18Google\\Cloud\\BackupDR\\V1\xea\x02\x1bGoogle::Cloud::BackupDR::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.backupdr.v1.backupplan_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.backupdr.v1B\x0fBackupPlanProtoP\x01Z8cloud.google.com/go/backupdr/apiv1/backupdrpb;backupdrpb\xaa\x02\x18Google.Cloud.BackupDR.V1\xca\x02\x18Google\\Cloud\\BackupDR\\V1\xea\x02\x1bGoogle::Cloud::BackupDR::V1'
    _globals['_BACKUPPLAN_LABELSENTRY']._loaded_options = None
    _globals['_BACKUPPLAN_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_BACKUPPLAN'].fields_by_name['name']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x08'
    _globals['_BACKUPPLAN'].fields_by_name['description']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLAN'].fields_by_name['labels']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLAN'].fields_by_name['create_time']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLAN'].fields_by_name['update_time']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLAN'].fields_by_name['backup_rules']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['backup_rules']._serialized_options = b'\xe0A\x02'
    _globals['_BACKUPPLAN'].fields_by_name['state']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLAN'].fields_by_name['resource_type']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['resource_type']._serialized_options = b'\xe0A\x02'
    _globals['_BACKUPPLAN'].fields_by_name['etag']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLAN'].fields_by_name['backup_vault']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['backup_vault']._serialized_options = b'\xe0A\x02\xfaA%\n#backupdr.googleapis.com/BackupVault'
    _globals['_BACKUPPLAN'].fields_by_name['backup_vault_service_account']._loaded_options = None
    _globals['_BACKUPPLAN'].fields_by_name['backup_vault_service_account']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLAN']._loaded_options = None
    _globals['_BACKUPPLAN']._serialized_options = b'\xeaA\x80\x01\n"backupdr.googleapis.com/BackupPlan\x12Aprojects/{project}/locations/{location}/backupPlans/{backup_plan}*\x0bbackupPlans2\nbackupPlan'
    _globals['_BACKUPRULE'].fields_by_name['rule_id']._loaded_options = None
    _globals['_BACKUPRULE'].fields_by_name['rule_id']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_BACKUPRULE'].fields_by_name['backup_retention_days']._loaded_options = None
    _globals['_BACKUPRULE'].fields_by_name['backup_retention_days']._serialized_options = b'\xe0A\x02'
    _globals['_BACKUPRULE'].fields_by_name['standard_schedule']._loaded_options = None
    _globals['_BACKUPRULE'].fields_by_name['standard_schedule']._serialized_options = b'\xe0A\x02'
    _globals['_STANDARDSCHEDULE'].fields_by_name['recurrence_type']._loaded_options = None
    _globals['_STANDARDSCHEDULE'].fields_by_name['recurrence_type']._serialized_options = b'\xe0A\x02'
    _globals['_STANDARDSCHEDULE'].fields_by_name['hourly_frequency']._loaded_options = None
    _globals['_STANDARDSCHEDULE'].fields_by_name['hourly_frequency']._serialized_options = b'\xe0A\x01'
    _globals['_STANDARDSCHEDULE'].fields_by_name['days_of_week']._loaded_options = None
    _globals['_STANDARDSCHEDULE'].fields_by_name['days_of_week']._serialized_options = b'\xe0A\x01'
    _globals['_STANDARDSCHEDULE'].fields_by_name['days_of_month']._loaded_options = None
    _globals['_STANDARDSCHEDULE'].fields_by_name['days_of_month']._serialized_options = b'\xe0A\x01'
    _globals['_STANDARDSCHEDULE'].fields_by_name['week_day_of_month']._loaded_options = None
    _globals['_STANDARDSCHEDULE'].fields_by_name['week_day_of_month']._serialized_options = b'\xe0A\x01'
    _globals['_STANDARDSCHEDULE'].fields_by_name['months']._loaded_options = None
    _globals['_STANDARDSCHEDULE'].fields_by_name['months']._serialized_options = b'\xe0A\x01'
    _globals['_STANDARDSCHEDULE'].fields_by_name['backup_window']._loaded_options = None
    _globals['_STANDARDSCHEDULE'].fields_by_name['backup_window']._serialized_options = b'\xe0A\x02'
    _globals['_STANDARDSCHEDULE'].fields_by_name['time_zone']._loaded_options = None
    _globals['_STANDARDSCHEDULE'].fields_by_name['time_zone']._serialized_options = b'\xe0A\x02'
    _globals['_BACKUPWINDOW'].fields_by_name['start_hour_of_day']._loaded_options = None
    _globals['_BACKUPWINDOW'].fields_by_name['start_hour_of_day']._serialized_options = b'\xe0A\x02'
    _globals['_BACKUPWINDOW'].fields_by_name['end_hour_of_day']._loaded_options = None
    _globals['_BACKUPWINDOW'].fields_by_name['end_hour_of_day']._serialized_options = b'\xe0A\x02'
    _globals['_WEEKDAYOFMONTH'].fields_by_name['week_of_month']._loaded_options = None
    _globals['_WEEKDAYOFMONTH'].fields_by_name['week_of_month']._serialized_options = b'\xe0A\x02'
    _globals['_WEEKDAYOFMONTH'].fields_by_name['day_of_week']._loaded_options = None
    _globals['_WEEKDAYOFMONTH'].fields_by_name['day_of_week']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEBACKUPPLANREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEBACKUPPLANREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"backupdr.googleapis.com/BackupPlan'
    _globals['_CREATEBACKUPPLANREQUEST'].fields_by_name['backup_plan_id']._loaded_options = None
    _globals['_CREATEBACKUPPLANREQUEST'].fields_by_name['backup_plan_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEBACKUPPLANREQUEST'].fields_by_name['backup_plan']._loaded_options = None
    _globals['_CREATEBACKUPPLANREQUEST'].fields_by_name['backup_plan']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEBACKUPPLANREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEBACKUPPLANREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_LISTBACKUPPLANSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTBACKUPPLANSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"backupdr.googleapis.com/BackupPlan'
    _globals['_LISTBACKUPPLANSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTBACKUPPLANSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTBACKUPPLANSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTBACKUPPLANSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTBACKUPPLANSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTBACKUPPLANSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTBACKUPPLANSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTBACKUPPLANSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETBACKUPPLANREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETBACKUPPLANREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"backupdr.googleapis.com/BackupPlan'
    _globals['_DELETEBACKUPPLANREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEBACKUPPLANREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"backupdr.googleapis.com/BackupPlan'
    _globals['_DELETEBACKUPPLANREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEBACKUPPLANREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_BACKUPPLAN']._serialized_start = 248
    _globals['_BACKUPPLAN']._serialized_end = 1041
    _globals['_BACKUPPLAN_LABELSENTRY']._serialized_start = 775
    _globals['_BACKUPPLAN_LABELSENTRY']._serialized_end = 820
    _globals['_BACKUPPLAN_STATE']._serialized_start = 822
    _globals['_BACKUPPLAN_STATE']._serialized_end = 906
    _globals['_BACKUPRULE']._serialized_start = 1044
    _globals['_BACKUPRULE']._serialized_end = 1220
    _globals['_STANDARDSCHEDULE']._serialized_start = 1223
    _globals['_STANDARDSCHEDULE']._serialized_end = 1758
    _globals['_STANDARDSCHEDULE_RECURRENCETYPE']._serialized_start = 1649
    _globals['_STANDARDSCHEDULE_RECURRENCETYPE']._serialized_end = 1758
    _globals['_BACKUPWINDOW']._serialized_start = 1760
    _globals['_BACKUPWINDOW']._serialized_end = 1836
    _globals['_WEEKDAYOFMONTH']._serialized_start = 1839
    _globals['_WEEKDAYOFMONTH']._serialized_end = 2089
    _globals['_WEEKDAYOFMONTH_WEEKOFMONTH']._serialized_start = 1989
    _globals['_WEEKDAYOFMONTH_WEEKOFMONTH']._serialized_end = 2089
    _globals['_CREATEBACKUPPLANREQUEST']._serialized_start = 2092
    _globals['_CREATEBACKUPPLANREQUEST']._serialized_end = 2303
    _globals['_LISTBACKUPPLANSREQUEST']._serialized_start = 2306
    _globals['_LISTBACKUPPLANSREQUEST']._serialized_end = 2483
    _globals['_LISTBACKUPPLANSRESPONSE']._serialized_start = 2486
    _globals['_LISTBACKUPPLANSRESPONSE']._serialized_end = 2617
    _globals['_GETBACKUPPLANREQUEST']._serialized_start = 2619
    _globals['_GETBACKUPPLANREQUEST']._serialized_end = 2699
    _globals['_DELETEBACKUPPLANREQUEST']._serialized_start = 2701
    _globals['_DELETEBACKUPPLANREQUEST']._serialized_end = 2817