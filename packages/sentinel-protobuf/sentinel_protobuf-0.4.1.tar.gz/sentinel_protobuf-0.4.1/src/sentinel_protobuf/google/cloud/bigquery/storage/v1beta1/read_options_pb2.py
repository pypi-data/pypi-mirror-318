"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/storage/v1beta1/read_options.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/bigquery/storage/v1beta1/read_options.proto\x12%google.cloud.bigquery.storage.v1beta1"D\n\x10TableReadOptions\x12\x17\n\x0fselected_fields\x18\x01 \x03(\t\x12\x17\n\x0frow_restriction\x18\x02 \x01(\tBp\n)com.google.cloud.bigquery.storage.v1beta1ZCcloud.google.com/go/bigquery/storage/apiv1beta1/storagepb;storagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.storage.v1beta1.read_options_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.bigquery.storage.v1beta1ZCcloud.google.com/go/bigquery/storage/apiv1beta1/storagepb;storagepb'
    _globals['_TABLEREADOPTIONS']._serialized_start = 99
    _globals['_TABLEREADOPTIONS']._serialized_end = 167