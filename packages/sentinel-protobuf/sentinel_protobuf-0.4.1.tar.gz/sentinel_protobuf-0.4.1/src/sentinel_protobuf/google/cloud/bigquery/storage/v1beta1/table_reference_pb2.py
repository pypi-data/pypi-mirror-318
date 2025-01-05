"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/storage/v1beta1/table_reference.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/cloud/bigquery/storage/v1beta1/table_reference.proto\x12%google.cloud.bigquery.storage.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto"J\n\x0eTableReference\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x10\n\x08table_id\x18\x03 \x01(\t"C\n\x0eTableModifiers\x121\n\rsnapshot_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x85\x01\n)com.google.cloud.bigquery.storage.v1beta1B\x13TableReferenceProtoZCcloud.google.com/go/bigquery/storage/apiv1beta1/storagepb;storagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.storage.v1beta1.table_reference_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.bigquery.storage.v1beta1B\x13TableReferenceProtoZCcloud.google.com/go/bigquery/storage/apiv1beta1/storagepb;storagepb'
    _globals['_TABLEREFERENCE']._serialized_start = 135
    _globals['_TABLEREFERENCE']._serialized_end = 209
    _globals['_TABLEMODIFIERS']._serialized_start = 211
    _globals['_TABLEMODIFIERS']._serialized_end = 278