"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/v3/snooze.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ....google.monitoring.v3 import common_pb2 as google_dot_monitoring_dot_v3_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!google/monitoring/v3/snooze.proto\x12\x14google.monitoring.v3\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a!google/monitoring/v3/common.proto"\xc5\x02\n\x06Snooze\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12<\n\x08criteria\x18\x03 \x01(\x0b2%.google.monitoring.v3.Snooze.CriteriaB\x03\xe0A\x02\x129\n\x08interval\x18\x04 \x01(\x0b2".google.monitoring.v3.TimeIntervalB\x03\xe0A\x02\x12\x19\n\x0cdisplay_name\x18\x05 \x01(\tB\x03\xe0A\x02\x1aH\n\x08Criteria\x12<\n\x08policies\x18\x01 \x03(\tB*\xfaA\'\n%monitoring.googleapis.com/AlertPolicy:J\xeaAG\n monitoring.googleapis.com/Snooze\x12#projects/{project}/snoozes/{snooze}B\xc6\x01\n\x18com.google.monitoring.v3B\x0bSnoozeProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.v3.snooze_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.monitoring.v3B\x0bSnoozeProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3'
    _globals['_SNOOZE_CRITERIA'].fields_by_name['policies']._loaded_options = None
    _globals['_SNOOZE_CRITERIA'].fields_by_name['policies']._serialized_options = b"\xfaA'\n%monitoring.googleapis.com/AlertPolicy"
    _globals['_SNOOZE'].fields_by_name['name']._loaded_options = None
    _globals['_SNOOZE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_SNOOZE'].fields_by_name['criteria']._loaded_options = None
    _globals['_SNOOZE'].fields_by_name['criteria']._serialized_options = b'\xe0A\x02'
    _globals['_SNOOZE'].fields_by_name['interval']._loaded_options = None
    _globals['_SNOOZE'].fields_by_name['interval']._serialized_options = b'\xe0A\x02'
    _globals['_SNOOZE'].fields_by_name['display_name']._loaded_options = None
    _globals['_SNOOZE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_SNOOZE']._loaded_options = None
    _globals['_SNOOZE']._serialized_options = b'\xeaAG\n monitoring.googleapis.com/Snooze\x12#projects/{project}/snoozes/{snooze}'
    _globals['_SNOOZE']._serialized_start = 155
    _globals['_SNOOZE']._serialized_end = 480
    _globals['_SNOOZE_CRITERIA']._serialized_start = 332
    _globals['_SNOOZE_CRITERIA']._serialized_end = 404