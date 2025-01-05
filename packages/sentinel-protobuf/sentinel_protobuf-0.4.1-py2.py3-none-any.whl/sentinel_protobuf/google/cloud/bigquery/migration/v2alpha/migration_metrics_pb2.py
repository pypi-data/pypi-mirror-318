"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/migration/v2alpha/migration_metrics.proto')
_sym_db = _symbol_database.Default()
from ......google.api import distribution_pb2 as google_dot_api_dot_distribution__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import metric_pb2 as google_dot_api_dot_metric__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/bigquery/migration/v2alpha/migration_metrics.proto\x12\'google.cloud.bigquery.migration.v2alpha\x1a\x1dgoogle/api/distribution.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x17google/api/metric.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xea\x01\n\nTimeSeries\x12\x13\n\x06metric\x18\x01 \x01(\tB\x03\xe0A\x02\x12?\n\nvalue_type\x18\x02 \x01(\x0e2&.google.api.MetricDescriptor.ValueTypeB\x03\xe0A\x02\x12A\n\x0bmetric_kind\x18\x03 \x01(\x0e2\'.google.api.MetricDescriptor.MetricKindB\x03\xe0A\x01\x12C\n\x06points\x18\x04 \x03(\x0b2..google.cloud.bigquery.migration.v2alpha.PointB\x03\xe0A\x02"\x94\x01\n\x05Point\x12G\n\x08interval\x18\x01 \x01(\x0b25.google.cloud.bigquery.migration.v2alpha.TimeInterval\x12B\n\x05value\x18\x02 \x01(\x0b23.google.cloud.bigquery.migration.v2alpha.TypedValue"v\n\x0cTimeInterval\x123\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02"\xaa\x01\n\nTypedValue\x12\x14\n\nbool_value\x18\x01 \x01(\x08H\x00\x12\x15\n\x0bint64_value\x18\x02 \x01(\x03H\x00\x12\x16\n\x0cdouble_value\x18\x03 \x01(\x01H\x00\x12\x16\n\x0cstring_value\x18\x04 \x01(\tH\x00\x126\n\x12distribution_value\x18\x05 \x01(\x0b2\x18.google.api.DistributionH\x00B\x07\n\x05valueB\xe5\x01\n+com.google.cloud.bigquery.migration.v2alphaB\x15MigrationMetricsProtoP\x01ZIcloud.google.com/go/bigquery/migration/apiv2alpha/migrationpb;migrationpb\xaa\x02\'Google.Cloud.BigQuery.Migration.V2Alpha\xca\x02\'Google\\Cloud\\BigQuery\\Migration\\V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.migration.v2alpha.migration_metrics_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.cloud.bigquery.migration.v2alphaB\x15MigrationMetricsProtoP\x01ZIcloud.google.com/go/bigquery/migration/apiv2alpha/migrationpb;migrationpb\xaa\x02'Google.Cloud.BigQuery.Migration.V2Alpha\xca\x02'Google\\Cloud\\BigQuery\\Migration\\V2alpha"
    _globals['_TIMESERIES'].fields_by_name['metric']._loaded_options = None
    _globals['_TIMESERIES'].fields_by_name['metric']._serialized_options = b'\xe0A\x02'
    _globals['_TIMESERIES'].fields_by_name['value_type']._loaded_options = None
    _globals['_TIMESERIES'].fields_by_name['value_type']._serialized_options = b'\xe0A\x02'
    _globals['_TIMESERIES'].fields_by_name['metric_kind']._loaded_options = None
    _globals['_TIMESERIES'].fields_by_name['metric_kind']._serialized_options = b'\xe0A\x01'
    _globals['_TIMESERIES'].fields_by_name['points']._loaded_options = None
    _globals['_TIMESERIES'].fields_by_name['points']._serialized_options = b'\xe0A\x02'
    _globals['_TIMEINTERVAL'].fields_by_name['start_time']._loaded_options = None
    _globals['_TIMEINTERVAL'].fields_by_name['start_time']._serialized_options = b'\xe0A\x01'
    _globals['_TIMEINTERVAL'].fields_by_name['end_time']._loaded_options = None
    _globals['_TIMEINTERVAL'].fields_by_name['end_time']._serialized_options = b'\xe0A\x02'
    _globals['_TIMESERIES']._serialized_start = 231
    _globals['_TIMESERIES']._serialized_end = 465
    _globals['_POINT']._serialized_start = 468
    _globals['_POINT']._serialized_end = 616
    _globals['_TIMEINTERVAL']._serialized_start = 618
    _globals['_TIMEINTERVAL']._serialized_end = 736
    _globals['_TYPEDVALUE']._serialized_start = 739
    _globals['_TYPEDVALUE']._serialized_end = 909