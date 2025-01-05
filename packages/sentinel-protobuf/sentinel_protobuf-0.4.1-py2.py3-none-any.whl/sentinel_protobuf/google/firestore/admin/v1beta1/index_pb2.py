"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/admin/v1beta1/index.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/firestore/admin/v1beta1/index.proto\x12\x1egoogle.firestore.admin.v1beta1\x1a\x1cgoogle/api/annotations.proto"\xb0\x01\n\nIndexField\x12\x12\n\nfield_path\x18\x01 \x01(\t\x12=\n\x04mode\x18\x02 \x01(\x0e2/.google.firestore.admin.v1beta1.IndexField.Mode"O\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\r\n\tASCENDING\x10\x02\x12\x0e\n\nDESCENDING\x10\x03\x12\x12\n\x0eARRAY_CONTAINS\x10\x04"\xe8\x01\n\x05Index\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rcollection_id\x18\x02 \x01(\t\x12:\n\x06fields\x18\x03 \x03(\x0b2*.google.firestore.admin.v1beta1.IndexField\x12:\n\x05state\x18\x06 \x01(\x0e2+.google.firestore.admin.v1beta1.Index.State"B\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x03\x12\t\n\x05READY\x10\x02\x12\t\n\x05ERROR\x10\x05B\xa0\x01\n"com.google.firestore.admin.v1beta1B\nIndexProtoP\x01Z>cloud.google.com/go/firestore/admin/apiv1beta1/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02$Google.Cloud.Firestore.Admin.V1Beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.admin.v1beta1.index_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.firestore.admin.v1beta1B\nIndexProtoP\x01Z>cloud.google.com/go/firestore/admin/apiv1beta1/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02$Google.Cloud.Firestore.Admin.V1Beta1'
    _globals['_INDEXFIELD']._serialized_start = 109
    _globals['_INDEXFIELD']._serialized_end = 285
    _globals['_INDEXFIELD_MODE']._serialized_start = 206
    _globals['_INDEXFIELD_MODE']._serialized_end = 285
    _globals['_INDEX']._serialized_start = 288
    _globals['_INDEX']._serialized_end = 520
    _globals['_INDEX_STATE']._serialized_start = 454
    _globals['_INDEX_STATE']._serialized_end = 520