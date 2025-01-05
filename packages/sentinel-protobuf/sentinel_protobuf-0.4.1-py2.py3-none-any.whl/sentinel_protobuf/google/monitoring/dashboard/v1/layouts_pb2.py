"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/monitoring/dashboard/v1/layouts.proto')
_sym_db = _symbol_database.Default()
from .....google.monitoring.dashboard.v1 import widget_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_widget__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/monitoring/dashboard/v1/layouts.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a+google/monitoring/dashboard/v1/widget.proto"V\n\nGridLayout\x12\x0f\n\x07columns\x18\x01 \x01(\x03\x127\n\x07widgets\x18\x02 \x03(\x0b2&.google.monitoring.dashboard.v1.Widget"\xde\x01\n\x0cMosaicLayout\x12\x0f\n\x07columns\x18\x01 \x01(\x05\x12@\n\x05tiles\x18\x03 \x03(\x0b21.google.monitoring.dashboard.v1.MosaicLayout.Tile\x1a{\n\x04Tile\x12\r\n\x05x_pos\x18\x01 \x01(\x05\x12\r\n\x05y_pos\x18\x02 \x01(\x05\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0e\n\x06height\x18\x04 \x01(\x05\x126\n\x06widget\x18\x05 \x01(\x0b2&.google.monitoring.dashboard.v1.Widget"\x98\x01\n\tRowLayout\x12;\n\x04rows\x18\x01 \x03(\x0b2-.google.monitoring.dashboard.v1.RowLayout.Row\x1aN\n\x03Row\x12\x0e\n\x06weight\x18\x01 \x01(\x03\x127\n\x07widgets\x18\x02 \x03(\x0b2&.google.monitoring.dashboard.v1.Widget"\xa7\x01\n\x0cColumnLayout\x12D\n\x07columns\x18\x01 \x03(\x0b23.google.monitoring.dashboard.v1.ColumnLayout.Column\x1aQ\n\x06Column\x12\x0e\n\x06weight\x18\x01 \x01(\x03\x127\n\x07widgets\x18\x02 \x03(\x0b2&.google.monitoring.dashboard.v1.WidgetB\xf5\x01\n"com.google.monitoring.dashboard.v1B\x0cLayoutsProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.dashboard.v1.layouts_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.monitoring.dashboard.v1B\x0cLayoutsProtoP\x01ZFcloud.google.com/go/monitoring/dashboard/apiv1/dashboardpb;dashboardpb\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1'
    _globals['_GRIDLAYOUT']._serialized_start = 125
    _globals['_GRIDLAYOUT']._serialized_end = 211
    _globals['_MOSAICLAYOUT']._serialized_start = 214
    _globals['_MOSAICLAYOUT']._serialized_end = 436
    _globals['_MOSAICLAYOUT_TILE']._serialized_start = 313
    _globals['_MOSAICLAYOUT_TILE']._serialized_end = 436
    _globals['_ROWLAYOUT']._serialized_start = 439
    _globals['_ROWLAYOUT']._serialized_end = 591
    _globals['_ROWLAYOUT_ROW']._serialized_start = 513
    _globals['_ROWLAYOUT_ROW']._serialized_end = 591
    _globals['_COLUMNLAYOUT']._serialized_start = 594
    _globals['_COLUMNLAYOUT']._serialized_end = 761
    _globals['_COLUMNLAYOUT_COLUMN']._serialized_start = 680
    _globals['_COLUMNLAYOUT_COLUMN']._serialized_end = 761