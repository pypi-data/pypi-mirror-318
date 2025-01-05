"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/notebooks/v1/schedule.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.notebooks.v1 import execution_pb2 as google_dot_cloud_dot_notebooks_dot_v1_dot_execution__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/notebooks/v1/schedule.proto\x12\x19google.cloud.notebooks.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a)google/cloud/notebooks/v1/execution.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8c\x05\n\x08Schedule\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x128\n\x05state\x18\x04 \x01(\x0e2).google.cloud.notebooks.v1.Schedule.State\x12\x15\n\rcron_schedule\x18\x05 \x01(\t\x12\x11\n\ttime_zone\x18\x06 \x01(\t\x124\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12H\n\x12execution_template\x18\t \x01(\x0b2,.google.cloud.notebooks.v1.ExecutionTemplate\x12D\n\x11recent_executions\x18\n \x03(\x0b2$.google.cloud.notebooks.v1.ExecutionB\x03\xe0A\x03"x\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\n\n\x06PAUSED\x10\x02\x12\x0c\n\x08DISABLED\x10\x03\x12\x11\n\rUPDATE_FAILED\x10\x04\x12\x10\n\x0cINITIALIZING\x10\x05\x12\x0c\n\x08DELETING\x10\x06:c\xeaA`\n!notebooks.googleapis.com/Schedule\x12;projects/{project}/location/{location}/schedules/{schedule}Bm\n\x1dcom.google.cloud.notebooks.v1B\rScheduleProtoP\x01Z;cloud.google.com/go/notebooks/apiv1/notebookspb;notebookspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.notebooks.v1.schedule_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.notebooks.v1B\rScheduleProtoP\x01Z;cloud.google.com/go/notebooks/apiv1/notebookspb;notebookspb'
    _globals['_SCHEDULE'].fields_by_name['name']._loaded_options = None
    _globals['_SCHEDULE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_SCHEDULE'].fields_by_name['display_name']._loaded_options = None
    _globals['_SCHEDULE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_SCHEDULE'].fields_by_name['create_time']._loaded_options = None
    _globals['_SCHEDULE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SCHEDULE'].fields_by_name['update_time']._loaded_options = None
    _globals['_SCHEDULE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_SCHEDULE'].fields_by_name['recent_executions']._loaded_options = None
    _globals['_SCHEDULE'].fields_by_name['recent_executions']._serialized_options = b'\xe0A\x03'
    _globals['_SCHEDULE']._loaded_options = None
    _globals['_SCHEDULE']._serialized_options = b'\xeaA`\n!notebooks.googleapis.com/Schedule\x12;projects/{project}/location/{location}/schedules/{schedule}'
    _globals['_SCHEDULE']._serialized_start = 208
    _globals['_SCHEDULE']._serialized_end = 860
    _globals['_SCHEDULE_STATE']._serialized_start = 639
    _globals['_SCHEDULE_STATE']._serialized_end = 759