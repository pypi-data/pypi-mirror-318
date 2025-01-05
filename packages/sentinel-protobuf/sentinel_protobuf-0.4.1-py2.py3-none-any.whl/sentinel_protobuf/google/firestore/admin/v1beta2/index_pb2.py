"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/admin/v1beta2/index.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/firestore/admin/v1beta2/index.proto\x12\x1egoogle.firestore.admin.v1beta2\x1a\x1cgoogle/api/annotations.proto"\xc0\x05\n\x05Index\x12\x0c\n\x04name\x18\x01 \x01(\t\x12E\n\x0bquery_scope\x18\x02 \x01(\x0e20.google.firestore.admin.v1beta2.Index.QueryScope\x12@\n\x06fields\x18\x03 \x03(\x0b20.google.firestore.admin.v1beta2.Index.IndexField\x12:\n\x05state\x18\x04 \x01(\x0e2+.google.firestore.admin.v1beta2.Index.State\x1a\xc7\x02\n\nIndexField\x12\x12\n\nfield_path\x18\x01 \x01(\t\x12G\n\x05order\x18\x02 \x01(\x0e26.google.firestore.admin.v1beta2.Index.IndexField.OrderH\x00\x12T\n\x0carray_config\x18\x03 \x01(\x0e2<.google.firestore.admin.v1beta2.Index.IndexField.ArrayConfigH\x00"=\n\x05Order\x12\x15\n\x11ORDER_UNSPECIFIED\x10\x00\x12\r\n\tASCENDING\x10\x01\x12\x0e\n\nDESCENDING\x10\x02"9\n\x0bArrayConfig\x12\x1c\n\x18ARRAY_CONFIG_UNSPECIFIED\x10\x00\x12\x0c\n\x08CONTAINS\x10\x01B\x0c\n\nvalue_mode"O\n\nQueryScope\x12\x1b\n\x17QUERY_SCOPE_UNSPECIFIED\x10\x00\x12\x0e\n\nCOLLECTION\x10\x01\x12\x14\n\x10COLLECTION_GROUP\x10\x02"I\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x10\n\x0cNEEDS_REPAIR\x10\x03B\xa0\x01\n"com.google.firestore.admin.v1beta2B\nIndexProtoP\x01Z>cloud.google.com/go/firestore/admin/apiv1beta2/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02$Google.Cloud.Firestore.Admin.V1Beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.admin.v1beta2.index_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.firestore.admin.v1beta2B\nIndexProtoP\x01Z>cloud.google.com/go/firestore/admin/apiv1beta2/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02$Google.Cloud.Firestore.Admin.V1Beta2'
    _globals['_INDEX']._serialized_start = 109
    _globals['_INDEX']._serialized_end = 813
    _globals['_INDEX_INDEXFIELD']._serialized_start = 330
    _globals['_INDEX_INDEXFIELD']._serialized_end = 657
    _globals['_INDEX_INDEXFIELD_ORDER']._serialized_start = 523
    _globals['_INDEX_INDEXFIELD_ORDER']._serialized_end = 584
    _globals['_INDEX_INDEXFIELD_ARRAYCONFIG']._serialized_start = 586
    _globals['_INDEX_INDEXFIELD_ARRAYCONFIG']._serialized_end = 643
    _globals['_INDEX_QUERYSCOPE']._serialized_start = 659
    _globals['_INDEX_QUERYSCOPE']._serialized_end = 738
    _globals['_INDEX_STATE']._serialized_start = 740
    _globals['_INDEX_STATE']._serialized_end = 813