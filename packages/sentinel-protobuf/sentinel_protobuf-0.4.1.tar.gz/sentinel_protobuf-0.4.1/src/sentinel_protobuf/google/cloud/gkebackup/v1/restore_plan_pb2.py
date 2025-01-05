"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/gkebackup/v1/restore_plan.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.gkebackup.v1 import restore_pb2 as google_dot_cloud_dot_gkebackup_dot_v1_dot_restore__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/gkebackup/v1/restore_plan.proto\x12\x19google.cloud.gkebackup.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\'google/cloud/gkebackup/v1/restore.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb4\x06\n\x0bRestorePlan\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x10\n\x03uid\x18\x02 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x05 \x01(\tB\x03\xe0A\x01\x12C\n\x0bbackup_plan\x18\x06 \x01(\tB.\xe0A\x05\xe0A\x02\xfaA%\n#gkebackup.googleapis.com/BackupPlan\x12<\n\x07cluster\x18\x07 \x01(\tB+\xe0A\x05\xe0A\x02\xfaA"\n container.googleapis.com/Cluster\x12E\n\x0erestore_config\x18\x08 \x01(\x0b2(.google.cloud.gkebackup.v1.RestoreConfigB\x03\xe0A\x02\x12G\n\x06labels\x18\t \x03(\x0b22.google.cloud.gkebackup.v1.RestorePlan.LabelsEntryB\x03\xe0A\x01\x12\x11\n\x04etag\x18\n \x01(\tB\x03\xe0A\x03\x12@\n\x05state\x18\x0b \x01(\x0e2,.google.cloud.gkebackup.v1.RestorePlan.StateB\x03\xe0A\x03\x12\x19\n\x0cstate_reason\x18\x0c \x01(\tB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"X\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x13\n\x0fCLUSTER_PENDING\x10\x01\x12\t\n\x05READY\x10\x02\x12\n\n\x06FAILED\x10\x03\x12\x0c\n\x08DELETING\x10\x04:n\xeaAk\n$gkebackup.googleapis.com/RestorePlan\x12Cprojects/{project}/locations/{location}/restorePlans/{restore_plan}B\xc7\x01\n\x1dcom.google.cloud.gkebackup.v1B\x10RestorePlanProtoP\x01Z;cloud.google.com/go/gkebackup/apiv1/gkebackuppb;gkebackuppb\xaa\x02\x19Google.Cloud.GkeBackup.V1\xca\x02\x19Google\\Cloud\\GkeBackup\\V1\xea\x02\x1cGoogle::Cloud::GkeBackup::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkebackup.v1.restore_plan_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.gkebackup.v1B\x10RestorePlanProtoP\x01Z;cloud.google.com/go/gkebackup/apiv1/gkebackuppb;gkebackuppb\xaa\x02\x19Google.Cloud.GkeBackup.V1\xca\x02\x19Google\\Cloud\\GkeBackup\\V1\xea\x02\x1cGoogle::Cloud::GkeBackup::V1'
    _globals['_RESTOREPLAN_LABELSENTRY']._loaded_options = None
    _globals['_RESTOREPLAN_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_RESTOREPLAN'].fields_by_name['name']._loaded_options = None
    _globals['_RESTOREPLAN'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_RESTOREPLAN'].fields_by_name['uid']._loaded_options = None
    _globals['_RESTOREPLAN'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_RESTOREPLAN'].fields_by_name['create_time']._loaded_options = None
    _globals['_RESTOREPLAN'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_RESTOREPLAN'].fields_by_name['update_time']._loaded_options = None
    _globals['_RESTOREPLAN'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_RESTOREPLAN'].fields_by_name['description']._loaded_options = None
    _globals['_RESTOREPLAN'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_RESTOREPLAN'].fields_by_name['backup_plan']._loaded_options = None
    _globals['_RESTOREPLAN'].fields_by_name['backup_plan']._serialized_options = b'\xe0A\x05\xe0A\x02\xfaA%\n#gkebackup.googleapis.com/BackupPlan'
    _globals['_RESTOREPLAN'].fields_by_name['cluster']._loaded_options = None
    _globals['_RESTOREPLAN'].fields_by_name['cluster']._serialized_options = b'\xe0A\x05\xe0A\x02\xfaA"\n container.googleapis.com/Cluster'
    _globals['_RESTOREPLAN'].fields_by_name['restore_config']._loaded_options = None
    _globals['_RESTOREPLAN'].fields_by_name['restore_config']._serialized_options = b'\xe0A\x02'
    _globals['_RESTOREPLAN'].fields_by_name['labels']._loaded_options = None
    _globals['_RESTOREPLAN'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_RESTOREPLAN'].fields_by_name['etag']._loaded_options = None
    _globals['_RESTOREPLAN'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_RESTOREPLAN'].fields_by_name['state']._loaded_options = None
    _globals['_RESTOREPLAN'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_RESTOREPLAN'].fields_by_name['state_reason']._loaded_options = None
    _globals['_RESTOREPLAN'].fields_by_name['state_reason']._serialized_options = b'\xe0A\x03'
    _globals['_RESTOREPLAN']._loaded_options = None
    _globals['_RESTOREPLAN']._serialized_options = b'\xeaAk\n$gkebackup.googleapis.com/RestorePlan\x12Cprojects/{project}/locations/{location}/restorePlans/{restore_plan}'
    _globals['_RESTOREPLAN']._serialized_start = 210
    _globals['_RESTOREPLAN']._serialized_end = 1030
    _globals['_RESTOREPLAN_LABELSENTRY']._serialized_start = 783
    _globals['_RESTOREPLAN_LABELSENTRY']._serialized_end = 828
    _globals['_RESTOREPLAN_STATE']._serialized_start = 830
    _globals['_RESTOREPLAN_STATE']._serialized_end = 918