"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/v3/metric.proto')
_sym_db = _symbol_database.Default()
from ....google.api import label_pb2 as google_dot_api_dot_label__pb2
from ....google.api import metric_pb2 as google_dot_api_dot_metric__pb2
from ....google.api import monitored_resource_pb2 as google_dot_api_dot_monitored__resource__pb2
from ....google.monitoring.v3 import common_pb2 as google_dot_monitoring_dot_v3_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!google/monitoring/v3/metric.proto\x12\x14google.monitoring.v3\x1a\x16google/api/label.proto\x1a\x17google/api/metric.proto\x1a#google/api/monitored_resource.proto\x1a!google/monitoring/v3/common.proto"n\n\x05Point\x124\n\x08interval\x18\x01 \x01(\x0b2".google.monitoring.v3.TimeInterval\x12/\n\x05value\x18\x02 \x01(\x0b2 .google.monitoring.v3.TypedValue"\xe4\x02\n\nTimeSeries\x12"\n\x06metric\x18\x01 \x01(\x0b2\x12.google.api.Metric\x12/\n\x08resource\x18\x02 \x01(\x0b2\x1d.google.api.MonitoredResource\x127\n\x08metadata\x18\x07 \x01(\x0b2%.google.api.MonitoredResourceMetadata\x12<\n\x0bmetric_kind\x18\x03 \x01(\x0e2\'.google.api.MetricDescriptor.MetricKind\x12:\n\nvalue_type\x18\x04 \x01(\x0e2&.google.api.MetricDescriptor.ValueType\x12+\n\x06points\x18\x05 \x03(\x0b2\x1b.google.monitoring.v3.Point\x12\x0c\n\x04unit\x18\x08 \x01(\t\x12\x13\n\x0bdescription\x18\t \x01(\t"\xce\x02\n\x14TimeSeriesDescriptor\x126\n\x11label_descriptors\x18\x01 \x03(\x0b2\x1b.google.api.LabelDescriptor\x12U\n\x11point_descriptors\x18\x05 \x03(\x0b2:.google.monitoring.v3.TimeSeriesDescriptor.ValueDescriptor\x1a\xa6\x01\n\x0fValueDescriptor\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\nvalue_type\x18\x02 \x01(\x0e2&.google.api.MetricDescriptor.ValueType\x12<\n\x0bmetric_kind\x18\x03 \x01(\x0e2\'.google.api.MetricDescriptor.MetricKind\x12\x0c\n\x04unit\x18\x04 \x01(\t"\x86\x02\n\x0eTimeSeriesData\x126\n\x0clabel_values\x18\x01 \x03(\x0b2 .google.monitoring.v3.LabelValue\x12B\n\npoint_data\x18\x02 \x03(\x0b2..google.monitoring.v3.TimeSeriesData.PointData\x1ax\n\tPointData\x120\n\x06values\x18\x01 \x03(\x0b2 .google.monitoring.v3.TypedValue\x129\n\rtime_interval\x18\x02 \x01(\x0b2".google.monitoring.v3.TimeInterval"Z\n\nLabelValue\x12\x14\n\nbool_value\x18\x01 \x01(\x08H\x00\x12\x15\n\x0bint64_value\x18\x02 \x01(\x03H\x00\x12\x16\n\x0cstring_value\x18\x03 \x01(\tH\x00B\x07\n\x05value"Q\n\nQueryError\x122\n\x07locator\x18\x01 \x01(\x0b2!.google.monitoring.v3.TextLocator\x12\x0f\n\x07message\x18\x02 \x01(\t"\xa0\x02\n\x0bTextLocator\x12\x0e\n\x06source\x18\x01 \x01(\t\x12B\n\x0estart_position\x18\x02 \x01(\x0b2*.google.monitoring.v3.TextLocator.Position\x12@\n\x0cend_position\x18\x03 \x01(\x0b2*.google.monitoring.v3.TextLocator.Position\x129\n\x0enested_locator\x18\x04 \x01(\x0b2!.google.monitoring.v3.TextLocator\x12\x16\n\x0enesting_reason\x18\x05 \x01(\t\x1a(\n\x08Position\x12\x0c\n\x04line\x18\x01 \x01(\x05\x12\x0e\n\x06column\x18\x02 \x01(\x05B\xc6\x01\n\x18com.google.monitoring.v3B\x0bMetricProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.v3.metric_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.monitoring.v3B\x0bMetricProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3'
    _globals['_POINT']._serialized_start = 180
    _globals['_POINT']._serialized_end = 290
    _globals['_TIMESERIES']._serialized_start = 293
    _globals['_TIMESERIES']._serialized_end = 649
    _globals['_TIMESERIESDESCRIPTOR']._serialized_start = 652
    _globals['_TIMESERIESDESCRIPTOR']._serialized_end = 986
    _globals['_TIMESERIESDESCRIPTOR_VALUEDESCRIPTOR']._serialized_start = 820
    _globals['_TIMESERIESDESCRIPTOR_VALUEDESCRIPTOR']._serialized_end = 986
    _globals['_TIMESERIESDATA']._serialized_start = 989
    _globals['_TIMESERIESDATA']._serialized_end = 1251
    _globals['_TIMESERIESDATA_POINTDATA']._serialized_start = 1131
    _globals['_TIMESERIESDATA_POINTDATA']._serialized_end = 1251
    _globals['_LABELVALUE']._serialized_start = 1253
    _globals['_LABELVALUE']._serialized_end = 1343
    _globals['_QUERYERROR']._serialized_start = 1345
    _globals['_QUERYERROR']._serialized_end = 1426
    _globals['_TEXTLOCATOR']._serialized_start = 1429
    _globals['_TEXTLOCATOR']._serialized_end = 1717
    _globals['_TEXTLOCATOR_POSITION']._serialized_start = 1677
    _globals['_TEXTLOCATOR_POSITION']._serialized_end = 1717