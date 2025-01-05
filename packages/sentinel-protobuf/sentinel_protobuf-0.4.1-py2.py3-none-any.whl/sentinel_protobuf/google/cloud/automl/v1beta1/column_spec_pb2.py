"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1beta1/column_spec.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.automl.v1beta1 import data_stats_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_data__stats__pb2
from .....google.cloud.automl.v1beta1 import data_types_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_data__types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/automl/v1beta1/column_spec.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x19google/api/resource.proto\x1a,google/cloud/automl/v1beta1/data_stats.proto\x1a,google/cloud/automl/v1beta1/data_types.proto"\x9b\x04\n\nColumnSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x128\n\tdata_type\x18\x02 \x01(\x0b2%.google.cloud.automl.v1beta1.DataType\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12:\n\ndata_stats\x18\x04 \x01(\x0b2&.google.cloud.automl.v1beta1.DataStats\x12X\n\x16top_correlated_columns\x18\x05 \x03(\x0b28.google.cloud.automl.v1beta1.ColumnSpec.CorrelatedColumn\x12\x0c\n\x04etag\x18\x06 \x01(\t\x1at\n\x10CorrelatedColumn\x12\x16\n\x0ecolumn_spec_id\x18\x01 \x01(\t\x12H\n\x11correlation_stats\x18\x02 \x01(\x0b2-.google.cloud.automl.v1beta1.CorrelationStats:\x94\x01\xeaA\x90\x01\n automl.googleapis.com/ColumnSpec\x12lprojects/{project}/locations/{location}/datasets/{dataset}/tableSpecs/{table_spec}/columnSpecs/{column_spec}B\x9b\x01\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1beta1.column_spec_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1'
    _globals['_COLUMNSPEC']._loaded_options = None
    _globals['_COLUMNSPEC']._serialized_options = b'\xeaA\x90\x01\n automl.googleapis.com/ColumnSpec\x12lprojects/{project}/locations/{location}/datasets/{dataset}/tableSpecs/{table_spec}/columnSpecs/{column_spec}'
    _globals['_COLUMNSPEC']._serialized_start = 198
    _globals['_COLUMNSPEC']._serialized_end = 737
    _globals['_COLUMNSPEC_CORRELATEDCOLUMN']._serialized_start = 470
    _globals['_COLUMNSPEC_CORRELATEDCOLUMN']._serialized_end = 586