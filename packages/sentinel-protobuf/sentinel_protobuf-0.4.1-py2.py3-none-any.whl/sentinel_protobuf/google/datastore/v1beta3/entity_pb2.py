"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/datastore/v1beta3/entity.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/datastore/v1beta3/entity.proto\x12\x18google.datastore.v1beta3\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x18google/type/latlng.proto"7\n\x0bPartitionId\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x14\n\x0cnamespace_id\x18\x04 \x01(\t"\xc1\x01\n\x03Key\x12;\n\x0cpartition_id\x18\x01 \x01(\x0b2%.google.datastore.v1beta3.PartitionId\x127\n\x04path\x18\x02 \x03(\x0b2).google.datastore.v1beta3.Key.PathElement\x1aD\n\x0bPathElement\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\x0c\n\x02id\x18\x02 \x01(\x03H\x00\x12\x0e\n\x04name\x18\x03 \x01(\tH\x00B\t\n\x07id_type"=\n\nArrayValue\x12/\n\x06values\x18\x01 \x03(\x0b2\x1f.google.datastore.v1beta3.Value"\x80\x04\n\x05Value\x120\n\nnull_value\x18\x0b \x01(\x0e2\x1a.google.protobuf.NullValueH\x00\x12\x17\n\rboolean_value\x18\x01 \x01(\x08H\x00\x12\x17\n\rinteger_value\x18\x02 \x01(\x03H\x00\x12\x16\n\x0cdouble_value\x18\x03 \x01(\x01H\x00\x125\n\x0ftimestamp_value\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x122\n\tkey_value\x18\x05 \x01(\x0b2\x1d.google.datastore.v1beta3.KeyH\x00\x12\x16\n\x0cstring_value\x18\x11 \x01(\tH\x00\x12\x14\n\nblob_value\x18\x12 \x01(\x0cH\x00\x12.\n\x0fgeo_point_value\x18\x08 \x01(\x0b2\x13.google.type.LatLngH\x00\x128\n\x0centity_value\x18\x06 \x01(\x0b2 .google.datastore.v1beta3.EntityH\x00\x12;\n\x0barray_value\x18\t \x01(\x0b2$.google.datastore.v1beta3.ArrayValueH\x00\x12\x0f\n\x07meaning\x18\x0e \x01(\x05\x12\x1c\n\x14exclude_from_indexes\x18\x13 \x01(\x08B\x0c\n\nvalue_type"\xce\x01\n\x06Entity\x12*\n\x03key\x18\x01 \x01(\x0b2\x1d.google.datastore.v1beta3.Key\x12D\n\nproperties\x18\x03 \x03(\x0b20.google.datastore.v1beta3.Entity.PropertiesEntry\x1aR\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b2\x1f.google.datastore.v1beta3.Value:\x028\x01B\xd5\x01\n\x1ccom.google.datastore.v1beta3B\x0bEntityProtoP\x01Z@cloud.google.com/go/datastore/apiv1beta3/datastorepb;datastorepb\xaa\x02\x1eGoogle.Cloud.Datastore.V1Beta3\xca\x02\x1eGoogle\\Cloud\\Datastore\\V1beta3\xea\x02!Google::Cloud::Datastore::V1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.datastore.v1beta3.entity_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.datastore.v1beta3B\x0bEntityProtoP\x01Z@cloud.google.com/go/datastore/apiv1beta3/datastorepb;datastorepb\xaa\x02\x1eGoogle.Cloud.Datastore.V1Beta3\xca\x02\x1eGoogle\\Cloud\\Datastore\\V1beta3\xea\x02!Google::Cloud::Datastore::V1beta3'
    _globals['_ENTITY_PROPERTIESENTRY']._loaded_options = None
    _globals['_ENTITY_PROPERTIESENTRY']._serialized_options = b'8\x01'
    _globals['_PARTITIONID']._serialized_start = 186
    _globals['_PARTITIONID']._serialized_end = 241
    _globals['_KEY']._serialized_start = 244
    _globals['_KEY']._serialized_end = 437
    _globals['_KEY_PATHELEMENT']._serialized_start = 369
    _globals['_KEY_PATHELEMENT']._serialized_end = 437
    _globals['_ARRAYVALUE']._serialized_start = 439
    _globals['_ARRAYVALUE']._serialized_end = 500
    _globals['_VALUE']._serialized_start = 503
    _globals['_VALUE']._serialized_end = 1015
    _globals['_ENTITY']._serialized_start = 1018
    _globals['_ENTITY']._serialized_end = 1224
    _globals['_ENTITY_PROPERTIESENTRY']._serialized_start = 1142
    _globals['_ENTITY_PROPERTIESENTRY']._serialized_end = 1224