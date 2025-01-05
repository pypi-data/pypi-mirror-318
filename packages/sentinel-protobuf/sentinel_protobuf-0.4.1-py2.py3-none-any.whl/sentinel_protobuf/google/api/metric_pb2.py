"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/api/metric.proto')
_sym_db = _symbol_database.Default()
from ...google.api import label_pb2 as google_dot_api_dot_label__pb2
from ...google.api import launch_stage_pb2 as google_dot_api_dot_launch__stage__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17google/api/metric.proto\x12\ngoogle.api\x1a\x16google/api/label.proto\x1a\x1dgoogle/api/launch_stage.proto\x1a\x1egoogle/protobuf/duration.proto"\xac\x08\n\x10MetricDescriptor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x08 \x01(\t\x12+\n\x06labels\x18\x02 \x03(\x0b2\x1b.google.api.LabelDescriptor\x12<\n\x0bmetric_kind\x18\x03 \x01(\x0e2\'.google.api.MetricDescriptor.MetricKind\x12:\n\nvalue_type\x18\x04 \x01(\x0e2&.google.api.MetricDescriptor.ValueType\x12\x0c\n\x04unit\x18\x05 \x01(\t\x12\x13\n\x0bdescription\x18\x06 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x07 \x01(\t\x12G\n\x08metadata\x18\n \x01(\x0b25.google.api.MetricDescriptor.MetricDescriptorMetadata\x12-\n\x0claunch_stage\x18\x0c \x01(\x0e2\x17.google.api.LaunchStage\x12 \n\x18monitored_resource_types\x18\r \x03(\t\x1a\xbd\x03\n\x18MetricDescriptorMetadata\x121\n\x0claunch_stage\x18\x01 \x01(\x0e2\x17.google.api.LaunchStageB\x02\x18\x01\x120\n\rsample_period\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x12/\n\x0cingest_delay\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x12\x84\x01\n$time_series_resource_hierarchy_level\x18\x04 \x03(\x0e2V.google.api.MetricDescriptor.MetricDescriptorMetadata.TimeSeriesResourceHierarchyLevel"\x83\x01\n TimeSeriesResourceHierarchyLevel\x124\n0TIME_SERIES_RESOURCE_HIERARCHY_LEVEL_UNSPECIFIED\x10\x00\x12\x0b\n\x07PROJECT\x10\x01\x12\x10\n\x0cORGANIZATION\x10\x02\x12\n\n\x06FOLDER\x10\x03"O\n\nMetricKind\x12\x1b\n\x17METRIC_KIND_UNSPECIFIED\x10\x00\x12\t\n\x05GAUGE\x10\x01\x12\t\n\x05DELTA\x10\x02\x12\x0e\n\nCUMULATIVE\x10\x03"q\n\tValueType\x12\x1a\n\x16VALUE_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04BOOL\x10\x01\x12\t\n\x05INT64\x10\x02\x12\n\n\x06DOUBLE\x10\x03\x12\n\n\x06STRING\x10\x04\x12\x10\n\x0cDISTRIBUTION\x10\x05\x12\t\n\x05MONEY\x10\x06"u\n\x06Metric\x12\x0c\n\x04type\x18\x03 \x01(\t\x12.\n\x06labels\x18\x02 \x03(\x0b2\x1e.google.api.Metric.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B_\n\x0ecom.google.apiB\x0bMetricProtoP\x01Z7google.golang.org/genproto/googleapis/api/metric;metric\xa2\x02\x04GAPIb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.metric_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0ecom.google.apiB\x0bMetricProtoP\x01Z7google.golang.org/genproto/googleapis/api/metric;metric\xa2\x02\x04GAPI'
    _globals['_METRICDESCRIPTOR_METRICDESCRIPTORMETADATA'].fields_by_name['launch_stage']._loaded_options = None
    _globals['_METRICDESCRIPTOR_METRICDESCRIPTORMETADATA'].fields_by_name['launch_stage']._serialized_options = b'\x18\x01'
    _globals['_METRIC_LABELSENTRY']._loaded_options = None
    _globals['_METRIC_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_METRICDESCRIPTOR']._serialized_start = 127
    _globals['_METRICDESCRIPTOR']._serialized_end = 1195
    _globals['_METRICDESCRIPTOR_METRICDESCRIPTORMETADATA']._serialized_start = 554
    _globals['_METRICDESCRIPTOR_METRICDESCRIPTORMETADATA']._serialized_end = 999
    _globals['_METRICDESCRIPTOR_METRICDESCRIPTORMETADATA_TIMESERIESRESOURCEHIERARCHYLEVEL']._serialized_start = 868
    _globals['_METRICDESCRIPTOR_METRICDESCRIPTORMETADATA_TIMESERIESRESOURCEHIERARCHYLEVEL']._serialized_end = 999
    _globals['_METRICDESCRIPTOR_METRICKIND']._serialized_start = 1001
    _globals['_METRICDESCRIPTOR_METRICKIND']._serialized_end = 1080
    _globals['_METRICDESCRIPTOR_VALUETYPE']._serialized_start = 1082
    _globals['_METRICDESCRIPTOR_VALUETYPE']._serialized_end = 1195
    _globals['_METRIC']._serialized_start = 1197
    _globals['_METRIC']._serialized_end = 1314
    _globals['_METRIC_LABELSENTRY']._serialized_start = 1269
    _globals['_METRIC_LABELSENTRY']._serialized_end = 1314