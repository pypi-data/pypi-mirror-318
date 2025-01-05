"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/storage/v1/arrow.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/bigquery/storage/v1/arrow.proto\x12 google.cloud.bigquery.storage.v1"(\n\x0bArrowSchema\x12\x19\n\x11serialized_schema\x18\x01 \x01(\x0c"J\n\x10ArrowRecordBatch\x12\x1f\n\x17serialized_record_batch\x18\x01 \x01(\x0c\x12\x15\n\trow_count\x18\x02 \x01(\x03B\x02\x18\x01"\xcf\x01\n\x19ArrowSerializationOptions\x12h\n\x12buffer_compression\x18\x02 \x01(\x0e2L.google.cloud.bigquery.storage.v1.ArrowSerializationOptions.CompressionCodec"H\n\x10CompressionCodec\x12\x1b\n\x17COMPRESSION_UNSPECIFIED\x10\x00\x12\r\n\tLZ4_FRAME\x10\x01\x12\x08\n\x04ZSTD\x10\x02B\xba\x01\n$com.google.cloud.bigquery.storage.v1B\nArrowProtoP\x01Z>cloud.google.com/go/bigquery/storage/apiv1/storagepb;storagepb\xaa\x02 Google.Cloud.BigQuery.Storage.V1\xca\x02 Google\\Cloud\\BigQuery\\Storage\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.storage.v1.arrow_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.bigquery.storage.v1B\nArrowProtoP\x01Z>cloud.google.com/go/bigquery/storage/apiv1/storagepb;storagepb\xaa\x02 Google.Cloud.BigQuery.Storage.V1\xca\x02 Google\\Cloud\\BigQuery\\Storage\\V1'
    _globals['_ARROWRECORDBATCH'].fields_by_name['row_count']._loaded_options = None
    _globals['_ARROWRECORDBATCH'].fields_by_name['row_count']._serialized_options = b'\x18\x01'
    _globals['_ARROWSCHEMA']._serialized_start = 82
    _globals['_ARROWSCHEMA']._serialized_end = 122
    _globals['_ARROWRECORDBATCH']._serialized_start = 124
    _globals['_ARROWRECORDBATCH']._serialized_end = 198
    _globals['_ARROWSERIALIZATIONOPTIONS']._serialized_start = 201
    _globals['_ARROWSERIALIZATIONOPTIONS']._serialized_end = 408
    _globals['_ARROWSERIALIZATIONOPTIONS_COMPRESSIONCODEC']._serialized_start = 336
    _globals['_ARROWSERIALIZATIONOPTIONS_COMPRESSIONCODEC']._serialized_end = 408