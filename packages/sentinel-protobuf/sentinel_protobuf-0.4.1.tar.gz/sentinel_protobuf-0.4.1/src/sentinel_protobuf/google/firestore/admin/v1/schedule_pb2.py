"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/admin/v1/schedule.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import dayofweek_pb2 as google_dot_type_dot_dayofweek__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/firestore/admin/v1/schedule.proto\x12\x19google.firestore.admin.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/type/dayofweek.proto"\xd6\x03\n\x0eBackupSchedule\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12,\n\tretention\x18\x06 \x01(\x0b2\x19.google.protobuf.Duration\x12F\n\x10daily_recurrence\x18\x07 \x01(\x0b2*.google.firestore.admin.v1.DailyRecurrenceH\x00\x12H\n\x11weekly_recurrence\x18\x08 \x01(\x0b2+.google.firestore.admin.v1.WeeklyRecurrenceH\x00:w\xeaAt\n\'firestore.googleapis.com/BackupSchedule\x12Iprojects/{project}/databases/{database}/backupSchedules/{backup_schedule}B\x0c\n\nrecurrence"\x11\n\x0fDailyRecurrence"7\n\x10WeeklyRecurrence\x12#\n\x03day\x18\x02 \x01(\x0e2\x16.google.type.DayOfWeekB\xdc\x01\n\x1dcom.google.firestore.admin.v1B\rScheduleProtoP\x01Z9cloud.google.com/go/firestore/apiv1/admin/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02\x1fGoogle.Cloud.Firestore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Firestore\\Admin\\V1\xea\x02#Google::Cloud::Firestore::Admin::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.admin.v1.schedule_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.firestore.admin.v1B\rScheduleProtoP\x01Z9cloud.google.com/go/firestore/apiv1/admin/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02\x1fGoogle.Cloud.Firestore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Firestore\\Admin\\V1\xea\x02#Google::Cloud::Firestore::Admin::V1'
    _globals['_BACKUPSCHEDULE'].fields_by_name['name']._loaded_options = None
    _globals['_BACKUPSCHEDULE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPSCHEDULE'].fields_by_name['create_time']._loaded_options = None
    _globals['_BACKUPSCHEDULE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPSCHEDULE'].fields_by_name['update_time']._loaded_options = None
    _globals['_BACKUPSCHEDULE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPSCHEDULE']._loaded_options = None
    _globals['_BACKUPSCHEDULE']._serialized_options = b"\xeaAt\n'firestore.googleapis.com/BackupSchedule\x12Iprojects/{project}/databases/{database}/backupSchedules/{backup_schedule}"
    _globals['_BACKUPSCHEDULE']._serialized_start = 226
    _globals['_BACKUPSCHEDULE']._serialized_end = 696
    _globals['_DAILYRECURRENCE']._serialized_start = 698
    _globals['_DAILYRECURRENCE']._serialized_end = 715
    _globals['_WEEKLYRECURRENCE']._serialized_start = 717
    _globals['_WEEKLYRECURRENCE']._serialized_end = 772