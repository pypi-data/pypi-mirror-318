"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1beta1/table_spec.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.automl.v1beta1 import io_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_io__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/automl/v1beta1/table_spec.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x19google/api/resource.proto\x1a$google/cloud/automl/v1beta1/io.proto"\xc1\x02\n\tTableSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1b\n\x13time_column_spec_id\x18\x02 \x01(\t\x12\x11\n\trow_count\x18\x03 \x01(\x03\x12\x17\n\x0fvalid_row_count\x18\x04 \x01(\x03\x12\x14\n\x0ccolumn_count\x18\x07 \x01(\x03\x12?\n\rinput_configs\x18\x05 \x03(\x0b2(.google.cloud.automl.v1beta1.InputConfig\x12\x0c\n\x04etag\x18\x06 \x01(\t:x\xeaAu\n\x1fautoml.googleapis.com/TableSpec\x12Rprojects/{project}/locations/{location}/datasets/{dataset}/tableSpecs/{table_spec}B\x9b\x01\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1beta1.table_spec_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1'
    _globals['_TABLESPEC']._loaded_options = None
    _globals['_TABLESPEC']._serialized_options = b'\xeaAu\n\x1fautoml.googleapis.com/TableSpec\x12Rprojects/{project}/locations/{location}/datasets/{dataset}/tableSpecs/{table_spec}'
    _globals['_TABLESPEC']._serialized_start = 143
    _globals['_TABLESPEC']._serialized_end = 464