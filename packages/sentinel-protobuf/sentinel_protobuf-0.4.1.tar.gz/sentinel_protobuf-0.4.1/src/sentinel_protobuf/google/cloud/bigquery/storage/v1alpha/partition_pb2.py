"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/storage/v1alpha/partition.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/bigquery/storage/v1alpha/partition.proto\x12%google.cloud.bigquery.storage.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"3\n\x0bFieldSchema\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04type\x18\x02 \x01(\tB\x03\xe0A\x02"\xb0\x01\n\x11StorageDescriptor\x12\x19\n\x0clocation_uri\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cinput_format\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x1a\n\routput_format\x18\x03 \x01(\tB\x03\xe0A\x01\x12I\n\nserde_info\x18\x04 \x01(\x0b20.google.cloud.bigquery.storage.v1alpha.SerDeInfoB\x03\xe0A\x01"\xd0\x01\n\tSerDeInfo\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x01\x12"\n\x15serialization_library\x18\x02 \x01(\tB\x03\xe0A\x02\x12Y\n\nparameters\x18\x03 \x03(\x0b2@.google.cloud.bigquery.storage.v1alpha.SerDeInfo.ParametersEntryB\x03\xe0A\x01\x1a1\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x9a\x03\n\x12MetastorePartition\x12\x13\n\x06values\x18\x01 \x03(\tB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12Y\n\x12storage_descriptor\x18\x03 \x01(\x0b28.google.cloud.bigquery.storage.v1alpha.StorageDescriptorB\x03\xe0A\x01\x12b\n\nparameters\x18\x04 \x03(\x0b2I.google.cloud.bigquery.storage.v1alpha.MetastorePartition.ParametersEntryB\x03\xe0A\x01\x12G\n\x06fields\x18\x05 \x03(\x0b22.google.cloud.bigquery.storage.v1alpha.FieldSchemaB\x03\xe0A\x01\x1a1\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"l\n\x16MetastorePartitionList\x12R\n\npartitions\x18\x01 \x03(\x0b29.google.cloud.bigquery.storage.v1alpha.MetastorePartitionB\x03\xe0A\x02"\xba\x01\n\nReadStream\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x08:\x95\x01\xeaA\x91\x01\n)bigquerystorage.googleapis.com/ReadStream\x12Kprojects/{project}/locations/{location}/sessions/{session}/streams/{stream}*\x0breadStreams2\nreadStream"U\n\nStreamList\x12G\n\x07streams\x18\x01 \x03(\x0b21.google.cloud.bigquery.storage.v1alpha.ReadStreamB\x03\xe0A\x03"/\n\x18MetastorePartitionValues\x12\x13\n\x06values\x18\x01 \x03(\tB\x03\xe0A\x02B\xdb\x01\n)com.google.cloud.bigquery.storage.v1alphaB\x17MetastorePartitionProtoP\x01ZCcloud.google.com/go/bigquery/storage/apiv1alpha/storagepb;storagepb\xaa\x02%Google.Cloud.BigQuery.Storage.V1Alpha\xca\x02%Google\\Cloud\\BigQuery\\Storage\\V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.storage.v1alpha.partition_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.bigquery.storage.v1alphaB\x17MetastorePartitionProtoP\x01ZCcloud.google.com/go/bigquery/storage/apiv1alpha/storagepb;storagepb\xaa\x02%Google.Cloud.BigQuery.Storage.V1Alpha\xca\x02%Google\\Cloud\\BigQuery\\Storage\\V1alpha'
    _globals['_FIELDSCHEMA'].fields_by_name['name']._loaded_options = None
    _globals['_FIELDSCHEMA'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_FIELDSCHEMA'].fields_by_name['type']._loaded_options = None
    _globals['_FIELDSCHEMA'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_STORAGEDESCRIPTOR'].fields_by_name['location_uri']._loaded_options = None
    _globals['_STORAGEDESCRIPTOR'].fields_by_name['location_uri']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGEDESCRIPTOR'].fields_by_name['input_format']._loaded_options = None
    _globals['_STORAGEDESCRIPTOR'].fields_by_name['input_format']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGEDESCRIPTOR'].fields_by_name['output_format']._loaded_options = None
    _globals['_STORAGEDESCRIPTOR'].fields_by_name['output_format']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGEDESCRIPTOR'].fields_by_name['serde_info']._loaded_options = None
    _globals['_STORAGEDESCRIPTOR'].fields_by_name['serde_info']._serialized_options = b'\xe0A\x01'
    _globals['_SERDEINFO_PARAMETERSENTRY']._loaded_options = None
    _globals['_SERDEINFO_PARAMETERSENTRY']._serialized_options = b'8\x01'
    _globals['_SERDEINFO'].fields_by_name['name']._loaded_options = None
    _globals['_SERDEINFO'].fields_by_name['name']._serialized_options = b'\xe0A\x01'
    _globals['_SERDEINFO'].fields_by_name['serialization_library']._loaded_options = None
    _globals['_SERDEINFO'].fields_by_name['serialization_library']._serialized_options = b'\xe0A\x02'
    _globals['_SERDEINFO'].fields_by_name['parameters']._loaded_options = None
    _globals['_SERDEINFO'].fields_by_name['parameters']._serialized_options = b'\xe0A\x01'
    _globals['_METASTOREPARTITION_PARAMETERSENTRY']._loaded_options = None
    _globals['_METASTOREPARTITION_PARAMETERSENTRY']._serialized_options = b'8\x01'
    _globals['_METASTOREPARTITION'].fields_by_name['values']._loaded_options = None
    _globals['_METASTOREPARTITION'].fields_by_name['values']._serialized_options = b'\xe0A\x02'
    _globals['_METASTOREPARTITION'].fields_by_name['create_time']._loaded_options = None
    _globals['_METASTOREPARTITION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_METASTOREPARTITION'].fields_by_name['storage_descriptor']._loaded_options = None
    _globals['_METASTOREPARTITION'].fields_by_name['storage_descriptor']._serialized_options = b'\xe0A\x01'
    _globals['_METASTOREPARTITION'].fields_by_name['parameters']._loaded_options = None
    _globals['_METASTOREPARTITION'].fields_by_name['parameters']._serialized_options = b'\xe0A\x01'
    _globals['_METASTOREPARTITION'].fields_by_name['fields']._loaded_options = None
    _globals['_METASTOREPARTITION'].fields_by_name['fields']._serialized_options = b'\xe0A\x01'
    _globals['_METASTOREPARTITIONLIST'].fields_by_name['partitions']._loaded_options = None
    _globals['_METASTOREPARTITIONLIST'].fields_by_name['partitions']._serialized_options = b'\xe0A\x02'
    _globals['_READSTREAM'].fields_by_name['name']._loaded_options = None
    _globals['_READSTREAM'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x08'
    _globals['_READSTREAM']._loaded_options = None
    _globals['_READSTREAM']._serialized_options = b'\xeaA\x91\x01\n)bigquerystorage.googleapis.com/ReadStream\x12Kprojects/{project}/locations/{location}/sessions/{session}/streams/{stream}*\x0breadStreams2\nreadStream'
    _globals['_STREAMLIST'].fields_by_name['streams']._loaded_options = None
    _globals['_STREAMLIST'].fields_by_name['streams']._serialized_options = b'\xe0A\x03'
    _globals['_METASTOREPARTITIONVALUES'].fields_by_name['values']._loaded_options = None
    _globals['_METASTOREPARTITIONVALUES'].fields_by_name['values']._serialized_options = b'\xe0A\x02'
    _globals['_FIELDSCHEMA']._serialized_start = 189
    _globals['_FIELDSCHEMA']._serialized_end = 240
    _globals['_STORAGEDESCRIPTOR']._serialized_start = 243
    _globals['_STORAGEDESCRIPTOR']._serialized_end = 419
    _globals['_SERDEINFO']._serialized_start = 422
    _globals['_SERDEINFO']._serialized_end = 630
    _globals['_SERDEINFO_PARAMETERSENTRY']._serialized_start = 581
    _globals['_SERDEINFO_PARAMETERSENTRY']._serialized_end = 630
    _globals['_METASTOREPARTITION']._serialized_start = 633
    _globals['_METASTOREPARTITION']._serialized_end = 1043
    _globals['_METASTOREPARTITION_PARAMETERSENTRY']._serialized_start = 581
    _globals['_METASTOREPARTITION_PARAMETERSENTRY']._serialized_end = 630
    _globals['_METASTOREPARTITIONLIST']._serialized_start = 1045
    _globals['_METASTOREPARTITIONLIST']._serialized_end = 1153
    _globals['_READSTREAM']._serialized_start = 1156
    _globals['_READSTREAM']._serialized_end = 1342
    _globals['_STREAMLIST']._serialized_start = 1344
    _globals['_STREAMLIST']._serialized_end = 1429
    _globals['_METASTOREPARTITIONVALUES']._serialized_start = 1431
    _globals['_METASTOREPARTITIONVALUES']._serialized_end = 1478