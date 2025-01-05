"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/storage/v1beta2/stream.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.bigquery.storage.v1beta2 import arrow_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1beta2_dot_arrow__pb2
from ......google.cloud.bigquery.storage.v1beta2 import avro_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1beta2_dot_avro__pb2
from ......google.cloud.bigquery.storage.v1beta2 import table_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1beta2_dot_table__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/bigquery/storage/v1beta2/stream.proto\x12%google.cloud.bigquery.storage.v1beta2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/bigquery/storage/v1beta2/arrow.proto\x1a0google/cloud/bigquery/storage/v1beta2/avro.proto\x1a1google/cloud/bigquery/storage/v1beta2/table.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf2\x07\n\x0bReadSession\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bexpire_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12K\n\x0bdata_format\x18\x03 \x01(\x0e21.google.cloud.bigquery.storage.v1beta2.DataFormatB\x03\xe0A\x05\x12M\n\x0bavro_schema\x18\x04 \x01(\x0b21.google.cloud.bigquery.storage.v1beta2.AvroSchemaB\x03\xe0A\x03H\x00\x12O\n\x0carrow_schema\x18\x05 \x01(\x0b22.google.cloud.bigquery.storage.v1beta2.ArrowSchemaB\x03\xe0A\x03H\x00\x124\n\x05table\x18\x06 \x01(\tB%\xe0A\x05\xfaA\x1f\n\x1dbigquery.googleapis.com/Table\x12_\n\x0ftable_modifiers\x18\x07 \x01(\x0b2A.google.cloud.bigquery.storage.v1beta2.ReadSession.TableModifiersB\x03\xe0A\x01\x12^\n\x0cread_options\x18\x08 \x01(\x0b2C.google.cloud.bigquery.storage.v1beta2.ReadSession.TableReadOptionsB\x03\xe0A\x01\x12G\n\x07streams\x18\n \x03(\x0b21.google.cloud.bigquery.storage.v1beta2.ReadStreamB\x03\xe0A\x03\x1aC\n\x0eTableModifiers\x121\n\rsnapshot_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a\xb0\x01\n\x10TableReadOptions\x12\x17\n\x0fselected_fields\x18\x01 \x03(\t\x12\x17\n\x0frow_restriction\x18\x02 \x01(\t\x12j\n\x1barrow_serialization_options\x18\x03 \x01(\x0b2@.google.cloud.bigquery.storage.v1beta2.ArrowSerializationOptionsB\x03\xe0A\x01:k\xeaAh\n*bigquerystorage.googleapis.com/ReadSession\x12:projects/{project}/locations/{location}/sessions/{session}B\x08\n\x06schema"\x9c\x01\n\nReadStream\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03:{\xeaAx\n)bigquerystorage.googleapis.com/ReadStream\x12Kprojects/{project}/locations/{location}/sessions/{session}/streams/{stream}"\xe7\x03\n\x0bWriteStream\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12J\n\x04type\x18\x02 \x01(\x0e27.google.cloud.bigquery.storage.v1beta2.WriteStream.TypeB\x03\xe0A\x05\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bcommit_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12M\n\x0ctable_schema\x18\x05 \x01(\x0b22.google.cloud.bigquery.storage.v1beta2.TableSchemaB\x03\xe0A\x03"F\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\r\n\tCOMMITTED\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\x0c\n\x08BUFFERED\x10\x03:v\xeaAs\n*bigquerystorage.googleapis.com/WriteStream\x12Eprojects/{project}/datasets/{dataset}/tables/{table}/streams/{stream}*>\n\nDataFormat\x12\x1b\n\x17DATA_FORMAT_UNSPECIFIED\x10\x00\x12\x08\n\x04AVRO\x10\x01\x12\t\n\x05ARROW\x10\x02B\xd7\x01\n)com.google.cloud.bigquery.storage.v1beta2B\x0bStreamProtoP\x01ZCcloud.google.com/go/bigquery/storage/apiv1beta2/storagepb;storagepb\xeaAU\n\x1dbigquery.googleapis.com/Table\x124projects/{project}/datasets/{dataset}/tables/{table}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.storage.v1beta2.stream_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.bigquery.storage.v1beta2B\x0bStreamProtoP\x01ZCcloud.google.com/go/bigquery/storage/apiv1beta2/storagepb;storagepb\xeaAU\n\x1dbigquery.googleapis.com/Table\x124projects/{project}/datasets/{dataset}/tables/{table}'
    _globals['_READSESSION_TABLEREADOPTIONS'].fields_by_name['arrow_serialization_options']._loaded_options = None
    _globals['_READSESSION_TABLEREADOPTIONS'].fields_by_name['arrow_serialization_options']._serialized_options = b'\xe0A\x01'
    _globals['_READSESSION'].fields_by_name['name']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_READSESSION'].fields_by_name['expire_time']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x03'
    _globals['_READSESSION'].fields_by_name['data_format']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['data_format']._serialized_options = b'\xe0A\x05'
    _globals['_READSESSION'].fields_by_name['avro_schema']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['avro_schema']._serialized_options = b'\xe0A\x03'
    _globals['_READSESSION'].fields_by_name['arrow_schema']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['arrow_schema']._serialized_options = b'\xe0A\x03'
    _globals['_READSESSION'].fields_by_name['table']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['table']._serialized_options = b'\xe0A\x05\xfaA\x1f\n\x1dbigquery.googleapis.com/Table'
    _globals['_READSESSION'].fields_by_name['table_modifiers']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['table_modifiers']._serialized_options = b'\xe0A\x01'
    _globals['_READSESSION'].fields_by_name['read_options']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['read_options']._serialized_options = b'\xe0A\x01'
    _globals['_READSESSION'].fields_by_name['streams']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['streams']._serialized_options = b'\xe0A\x03'
    _globals['_READSESSION']._loaded_options = None
    _globals['_READSESSION']._serialized_options = b'\xeaAh\n*bigquerystorage.googleapis.com/ReadSession\x12:projects/{project}/locations/{location}/sessions/{session}'
    _globals['_READSTREAM'].fields_by_name['name']._loaded_options = None
    _globals['_READSTREAM'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_READSTREAM']._loaded_options = None
    _globals['_READSTREAM']._serialized_options = b'\xeaAx\n)bigquerystorage.googleapis.com/ReadStream\x12Kprojects/{project}/locations/{location}/sessions/{session}/streams/{stream}'
    _globals['_WRITESTREAM'].fields_by_name['name']._loaded_options = None
    _globals['_WRITESTREAM'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_WRITESTREAM'].fields_by_name['type']._loaded_options = None
    _globals['_WRITESTREAM'].fields_by_name['type']._serialized_options = b'\xe0A\x05'
    _globals['_WRITESTREAM'].fields_by_name['create_time']._loaded_options = None
    _globals['_WRITESTREAM'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_WRITESTREAM'].fields_by_name['commit_time']._loaded_options = None
    _globals['_WRITESTREAM'].fields_by_name['commit_time']._serialized_options = b'\xe0A\x03'
    _globals['_WRITESTREAM'].fields_by_name['table_schema']._loaded_options = None
    _globals['_WRITESTREAM'].fields_by_name['table_schema']._serialized_options = b'\xe0A\x03'
    _globals['_WRITESTREAM']._loaded_options = None
    _globals['_WRITESTREAM']._serialized_options = b'\xeaAs\n*bigquerystorage.googleapis.com/WriteStream\x12Eprojects/{project}/datasets/{dataset}/tables/{table}/streams/{stream}'
    _globals['_DATAFORMAT']._serialized_start = 2000
    _globals['_DATAFORMAT']._serialized_end = 2062
    _globals['_READSESSION']._serialized_start = 339
    _globals['_READSESSION']._serialized_end = 1349
    _globals['_READSESSION_TABLEMODIFIERS']._serialized_start = 984
    _globals['_READSESSION_TABLEMODIFIERS']._serialized_end = 1051
    _globals['_READSESSION_TABLEREADOPTIONS']._serialized_start = 1054
    _globals['_READSESSION_TABLEREADOPTIONS']._serialized_end = 1230
    _globals['_READSTREAM']._serialized_start = 1352
    _globals['_READSTREAM']._serialized_end = 1508
    _globals['_WRITESTREAM']._serialized_start = 1511
    _globals['_WRITESTREAM']._serialized_end = 1998
    _globals['_WRITESTREAM_TYPE']._serialized_start = 1808
    _globals['_WRITESTREAM_TYPE']._serialized_end = 1878