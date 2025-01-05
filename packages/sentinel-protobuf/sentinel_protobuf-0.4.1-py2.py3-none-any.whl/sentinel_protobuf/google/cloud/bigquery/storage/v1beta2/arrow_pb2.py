"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/storage/v1beta2/arrow.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/bigquery/storage/v1beta2/arrow.proto\x12%google.cloud.bigquery.storage.v1beta2"(\n\x0bArrowSchema\x12\x19\n\x11serialized_schema\x18\x01 \x01(\x0c"3\n\x10ArrowRecordBatch\x12\x1f\n\x17serialized_record_batch\x18\x01 \x01(\x0c"\xb6\x01\n\x19ArrowSerializationOptions\x12W\n\x06format\x18\x01 \x01(\x0e2G.google.cloud.bigquery.storage.v1beta2.ArrowSerializationOptions.Format"@\n\x06Format\x12\x16\n\x12FORMAT_UNSPECIFIED\x10\x00\x12\x0e\n\nARROW_0_14\x10\x01\x12\x0e\n\nARROW_0_15\x10\x02B~\n)com.google.cloud.bigquery.storage.v1beta2B\nArrowProtoP\x01ZCcloud.google.com/go/bigquery/storage/apiv1beta2/storagepb;storagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.storage.v1beta2.arrow_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.bigquery.storage.v1beta2B\nArrowProtoP\x01ZCcloud.google.com/go/bigquery/storage/apiv1beta2/storagepb;storagepb'
    _globals['_ARROWSCHEMA']._serialized_start = 92
    _globals['_ARROWSCHEMA']._serialized_end = 132
    _globals['_ARROWRECORDBATCH']._serialized_start = 134
    _globals['_ARROWRECORDBATCH']._serialized_end = 185
    _globals['_ARROWSERIALIZATIONOPTIONS']._serialized_start = 188
    _globals['_ARROWSERIALIZATIONOPTIONS']._serialized_end = 370
    _globals['_ARROWSERIALIZATIONOPTIONS_FORMAT']._serialized_start = 306
    _globals['_ARROWSERIALIZATIONOPTIONS_FORMAT']._serialized_end = 370