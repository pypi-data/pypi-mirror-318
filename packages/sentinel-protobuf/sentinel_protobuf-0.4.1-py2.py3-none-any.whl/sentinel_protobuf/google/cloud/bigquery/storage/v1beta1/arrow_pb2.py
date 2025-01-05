"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/storage/v1beta1/arrow.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/bigquery/storage/v1beta1/arrow.proto\x12%google.cloud.bigquery.storage.v1beta1"(\n\x0bArrowSchema\x12\x19\n\x11serialized_schema\x18\x01 \x01(\x0c"F\n\x10ArrowRecordBatch\x12\x1f\n\x17serialized_record_batch\x18\x01 \x01(\x0c\x12\x11\n\trow_count\x18\x02 \x01(\x03B|\n)com.google.cloud.bigquery.storage.v1beta1B\nArrowProtoZCcloud.google.com/go/bigquery/storage/apiv1beta1/storagepb;storagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.storage.v1beta1.arrow_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.bigquery.storage.v1beta1B\nArrowProtoZCcloud.google.com/go/bigquery/storage/apiv1beta1/storagepb;storagepb'
    _globals['_ARROWSCHEMA']._serialized_start = 92
    _globals['_ARROWSCHEMA']._serialized_end = 132
    _globals['_ARROWRECORDBATCH']._serialized_start = 134
    _globals['_ARROWRECORDBATCH']._serialized_end = 204