"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1beta1/tables.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.automl.v1beta1 import classification_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_classification__pb2
from .....google.cloud.automl.v1beta1 import column_spec_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_column__spec__pb2
from .....google.cloud.automl.v1beta1 import data_items_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_data__items__pb2
from .....google.cloud.automl.v1beta1 import data_stats_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_data__stats__pb2
from .....google.cloud.automl.v1beta1 import ranges_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_ranges__pb2
from .....google.cloud.automl.v1beta1 import regression_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_regression__pb2
from .....google.cloud.automl.v1beta1 import temporal_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_temporal__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/automl/v1beta1/tables.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a0google/cloud/automl/v1beta1/classification.proto\x1a-google/cloud/automl/v1beta1/column_spec.proto\x1a,google/cloud/automl/v1beta1/data_items.proto\x1a,google/cloud/automl/v1beta1/data_stats.proto\x1a(google/cloud/automl/v1beta1/ranges.proto\x1a,google/cloud/automl/v1beta1/regression.proto\x1a*google/cloud/automl/v1beta1/temporal.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb0\x03\n\x15TablesDatasetMetadata\x12\x1d\n\x15primary_table_spec_id\x18\x01 \x01(\t\x12\x1d\n\x15target_column_spec_id\x18\x02 \x01(\t\x12\x1d\n\x15weight_column_spec_id\x18\x03 \x01(\t\x12\x1d\n\x15ml_use_column_spec_id\x18\x04 \x01(\t\x12t\n\x1atarget_column_correlations\x18\x06 \x03(\x0b2P.google.cloud.automl.v1beta1.TablesDatasetMetadata.TargetColumnCorrelationsEntry\x125\n\x11stats_update_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1an\n\x1dTargetColumnCorrelationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12<\n\x05value\x18\x02 \x01(\x0b2-.google.cloud.automl.v1beta1.CorrelationStats:\x028\x01"\x96\x04\n\x13TablesModelMetadata\x12-\n#optimization_objective_recall_value\x18\x11 \x01(\x02H\x00\x120\n&optimization_objective_precision_value\x18\x12 \x01(\x02H\x00\x12C\n\x12target_column_spec\x18\x02 \x01(\x0b2\'.google.cloud.automl.v1beta1.ColumnSpec\x12K\n\x1ainput_feature_column_specs\x18\x03 \x03(\x0b2\'.google.cloud.automl.v1beta1.ColumnSpec\x12\x1e\n\x16optimization_objective\x18\x04 \x01(\t\x12T\n\x18tables_model_column_info\x18\x05 \x03(\x0b22.google.cloud.automl.v1beta1.TablesModelColumnInfo\x12%\n\x1dtrain_budget_milli_node_hours\x18\x06 \x01(\x03\x12#\n\x1btrain_cost_milli_node_hours\x18\x07 \x01(\x03\x12\x1e\n\x16disable_early_stopping\x18\x0c \x01(\x08B*\n(additional_optimization_objective_config"\xfd\x01\n\x10TablesAnnotation\x12\r\n\x05score\x18\x01 \x01(\x02\x12E\n\x13prediction_interval\x18\x04 \x01(\x0b2(.google.cloud.automl.v1beta1.DoubleRange\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x12T\n\x18tables_model_column_info\x18\x03 \x03(\x0b22.google.cloud.automl.v1beta1.TablesModelColumnInfo\x12\x16\n\x0ebaseline_score\x18\x05 \x01(\x02"j\n\x15TablesModelColumnInfo\x12\x18\n\x10column_spec_name\x18\x01 \x01(\t\x12\x1b\n\x13column_display_name\x18\x02 \x01(\t\x12\x1a\n\x12feature_importance\x18\x03 \x01(\x02B\x9b\x01\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1beta1.tables_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1'
    _globals['_TABLESDATASETMETADATA_TARGETCOLUMNCORRELATIONSENTRY']._loaded_options = None
    _globals['_TABLESDATASETMETADATA_TARGETCOLUMNCORRELATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_TABLESDATASETMETADATA']._serialized_start = 458
    _globals['_TABLESDATASETMETADATA']._serialized_end = 890
    _globals['_TABLESDATASETMETADATA_TARGETCOLUMNCORRELATIONSENTRY']._serialized_start = 780
    _globals['_TABLESDATASETMETADATA_TARGETCOLUMNCORRELATIONSENTRY']._serialized_end = 890
    _globals['_TABLESMODELMETADATA']._serialized_start = 893
    _globals['_TABLESMODELMETADATA']._serialized_end = 1427
    _globals['_TABLESANNOTATION']._serialized_start = 1430
    _globals['_TABLESANNOTATION']._serialized_end = 1683
    _globals['_TABLESMODELCOLUMNINFO']._serialized_start = 1685
    _globals['_TABLESMODELCOLUMNINFO']._serialized_end = 1791