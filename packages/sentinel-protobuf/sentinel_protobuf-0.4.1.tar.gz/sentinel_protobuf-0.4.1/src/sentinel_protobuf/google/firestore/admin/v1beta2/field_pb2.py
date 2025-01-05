"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/admin/v1beta2/field.proto')
_sym_db = _symbol_database.Default()
from .....google.firestore.admin.v1beta2 import index_pb2 as google_dot_firestore_dot_admin_dot_v1beta2_dot_index__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/firestore/admin/v1beta2/field.proto\x12\x1egoogle.firestore.admin.v1beta2\x1a*google/firestore/admin/v1beta2/index.proto\x1a\x1cgoogle/api/annotations.proto"\xef\x01\n\x05Field\x12\x0c\n\x04name\x18\x01 \x01(\t\x12G\n\x0cindex_config\x18\x02 \x01(\x0b21.google.firestore.admin.v1beta2.Field.IndexConfig\x1a\x8e\x01\n\x0bIndexConfig\x126\n\x07indexes\x18\x01 \x03(\x0b2%.google.firestore.admin.v1beta2.Index\x12\x1c\n\x14uses_ancestor_config\x18\x02 \x01(\x08\x12\x16\n\x0eancestor_field\x18\x03 \x01(\t\x12\x11\n\treverting\x18\x04 \x01(\x08B\xa0\x01\n"com.google.firestore.admin.v1beta2B\nFieldProtoP\x01Z>cloud.google.com/go/firestore/admin/apiv1beta2/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02$Google.Cloud.Firestore.Admin.V1Beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.admin.v1beta2.field_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.firestore.admin.v1beta2B\nFieldProtoP\x01Z>cloud.google.com/go/firestore/admin/apiv1beta2/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02$Google.Cloud.Firestore.Admin.V1Beta2'
    _globals['_FIELD']._serialized_start = 153
    _globals['_FIELD']._serialized_end = 392
    _globals['_FIELD_INDEXCONFIG']._serialized_start = 250
    _globals['_FIELD_INDEXCONFIG']._serialized_end = 392