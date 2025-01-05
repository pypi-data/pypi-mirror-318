"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/v1/document.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/firestore/v1/document.proto\x12\x13google.firestore.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x18google/type/latlng.proto"\x80\x02\n\x08Document\x12\x0c\n\x04name\x18\x01 \x01(\t\x129\n\x06fields\x18\x02 \x03(\x0b2).google.firestore.v1.Document.FieldsEntry\x12/\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1aI\n\x0bFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b2\x1a.google.firestore.v1.Value:\x028\x01"\xae\x03\n\x05Value\x120\n\nnull_value\x18\x0b \x01(\x0e2\x1a.google.protobuf.NullValueH\x00\x12\x17\n\rboolean_value\x18\x01 \x01(\x08H\x00\x12\x17\n\rinteger_value\x18\x02 \x01(\x03H\x00\x12\x16\n\x0cdouble_value\x18\x03 \x01(\x01H\x00\x125\n\x0ftimestamp_value\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x12\x16\n\x0cstring_value\x18\x11 \x01(\tH\x00\x12\x15\n\x0bbytes_value\x18\x12 \x01(\x0cH\x00\x12\x19\n\x0freference_value\x18\x05 \x01(\tH\x00\x12.\n\x0fgeo_point_value\x18\x08 \x01(\x0b2\x13.google.type.LatLngH\x00\x126\n\x0barray_value\x18\t \x01(\x0b2\x1f.google.firestore.v1.ArrayValueH\x00\x122\n\tmap_value\x18\x06 \x01(\x0b2\x1d.google.firestore.v1.MapValueH\x00B\x0c\n\nvalue_type"8\n\nArrayValue\x12*\n\x06values\x18\x01 \x03(\x0b2\x1a.google.firestore.v1.Value"\x90\x01\n\x08MapValue\x129\n\x06fields\x18\x01 \x03(\x0b2).google.firestore.v1.MapValue.FieldsEntry\x1aI\n\x0bFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b2\x1a.google.firestore.v1.Value:\x028\x01B\xc5\x01\n\x17com.google.firestore.v1B\rDocumentProtoP\x01Z;cloud.google.com/go/firestore/apiv1/firestorepb;firestorepb\xa2\x02\x04GCFS\xaa\x02\x19Google.Cloud.Firestore.V1\xca\x02\x19Google\\Cloud\\Firestore\\V1\xea\x02\x1cGoogle::Cloud::Firestore::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.v1.document_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.firestore.v1B\rDocumentProtoP\x01Z;cloud.google.com/go/firestore/apiv1/firestorepb;firestorepb\xa2\x02\x04GCFS\xaa\x02\x19Google.Cloud.Firestore.V1\xca\x02\x19Google\\Cloud\\Firestore\\V1\xea\x02\x1cGoogle::Cloud::Firestore::V1'
    _globals['_DOCUMENT_FIELDSENTRY']._loaded_options = None
    _globals['_DOCUMENT_FIELDSENTRY']._serialized_options = b'8\x01'
    _globals['_MAPVALUE_FIELDSENTRY']._loaded_options = None
    _globals['_MAPVALUE_FIELDSENTRY']._serialized_options = b'8\x01'
    _globals['_DOCUMENT']._serialized_start = 182
    _globals['_DOCUMENT']._serialized_end = 438
    _globals['_DOCUMENT_FIELDSENTRY']._serialized_start = 365
    _globals['_DOCUMENT_FIELDSENTRY']._serialized_end = 438
    _globals['_VALUE']._serialized_start = 441
    _globals['_VALUE']._serialized_end = 871
    _globals['_ARRAYVALUE']._serialized_start = 873
    _globals['_ARRAYVALUE']._serialized_end = 929
    _globals['_MAPVALUE']._serialized_start = 932
    _globals['_MAPVALUE']._serialized_end = 1076
    _globals['_MAPVALUE_FIELDSENTRY']._serialized_start = 365
    _globals['_MAPVALUE_FIELDSENTRY']._serialized_end = 438