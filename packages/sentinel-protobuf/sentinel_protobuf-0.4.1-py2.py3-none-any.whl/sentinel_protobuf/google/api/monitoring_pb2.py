"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/api/monitoring.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bgoogle/api/monitoring.proto\x12\ngoogle.api"\xec\x01\n\nMonitoring\x12K\n\x15producer_destinations\x18\x01 \x03(\x0b2,.google.api.Monitoring.MonitoringDestination\x12K\n\x15consumer_destinations\x18\x02 \x03(\x0b2,.google.api.Monitoring.MonitoringDestination\x1aD\n\x15MonitoringDestination\x12\x1a\n\x12monitored_resource\x18\x01 \x01(\t\x12\x0f\n\x07metrics\x18\x02 \x03(\tBq\n\x0ecom.google.apiB\x0fMonitoringProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPIb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.monitoring_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0ecom.google.apiB\x0fMonitoringProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPI'
    _globals['_MONITORING']._serialized_start = 44
    _globals['_MONITORING']._serialized_end = 280
    _globals['_MONITORING_MONITORINGDESTINATION']._serialized_start = 212
    _globals['_MONITORING_MONITORINGDESTINATION']._serialized_end = 280