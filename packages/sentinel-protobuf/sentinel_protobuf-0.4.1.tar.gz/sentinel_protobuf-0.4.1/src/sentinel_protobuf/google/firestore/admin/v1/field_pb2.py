"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/admin/v1/field.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.firestore.admin.v1 import index_pb2 as google_dot_firestore_dot_admin_dot_v1_dot_index__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/firestore/admin/v1/field.proto\x12\x19google.firestore.admin.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a%google/firestore/admin/v1/index.proto"\xc5\x04\n\x05Field\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12B\n\x0cindex_config\x18\x02 \x01(\x0b2,.google.firestore.admin.v1.Field.IndexConfig\x12>\n\nttl_config\x18\x03 \x01(\x0b2*.google.firestore.admin.v1.Field.TtlConfig\x1a\x89\x01\n\x0bIndexConfig\x121\n\x07indexes\x18\x01 \x03(\x0b2 .google.firestore.admin.v1.Index\x12\x1c\n\x14uses_ancestor_config\x18\x02 \x01(\x08\x12\x16\n\x0eancestor_field\x18\x03 \x01(\t\x12\x11\n\treverting\x18\x04 \x01(\x08\x1a\x9d\x01\n\tTtlConfig\x12D\n\x05state\x18\x01 \x01(\x0e20.google.firestore.admin.v1.Field.TtlConfig.StateB\x03\xe0A\x03"J\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x10\n\x0cNEEDS_REPAIR\x10\x03:y\xeaAv\n\x1efirestore.googleapis.com/Field\x12Tprojects/{project}/databases/{database}/collectionGroups/{collection}/fields/{field}B\xd9\x01\n\x1dcom.google.firestore.admin.v1B\nFieldProtoP\x01Z9cloud.google.com/go/firestore/apiv1/admin/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02\x1fGoogle.Cloud.Firestore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Firestore\\Admin\\V1\xea\x02#Google::Cloud::Firestore::Admin::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.admin.v1.field_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.firestore.admin.v1B\nFieldProtoP\x01Z9cloud.google.com/go/firestore/apiv1/admin/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02\x1fGoogle.Cloud.Firestore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Firestore\\Admin\\V1\xea\x02#Google::Cloud::Firestore::Admin::V1'
    _globals['_FIELD_TTLCONFIG'].fields_by_name['state']._loaded_options = None
    _globals['_FIELD_TTLCONFIG'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_FIELD'].fields_by_name['name']._loaded_options = None
    _globals['_FIELD'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_FIELD']._loaded_options = None
    _globals['_FIELD']._serialized_options = b'\xeaAv\n\x1efirestore.googleapis.com/Field\x12Tprojects/{project}/databases/{database}/collectionGroups/{collection}/fields/{field}'
    _globals['_FIELD']._serialized_start = 168
    _globals['_FIELD']._serialized_end = 749
    _globals['_FIELD_INDEXCONFIG']._serialized_start = 329
    _globals['_FIELD_INDEXCONFIG']._serialized_end = 466
    _globals['_FIELD_TTLCONFIG']._serialized_start = 469
    _globals['_FIELD_TTLCONFIG']._serialized_end = 626
    _globals['_FIELD_TTLCONFIG_STATE']._serialized_start = 552
    _globals['_FIELD_TTLCONFIG_STATE']._serialized_end = 626