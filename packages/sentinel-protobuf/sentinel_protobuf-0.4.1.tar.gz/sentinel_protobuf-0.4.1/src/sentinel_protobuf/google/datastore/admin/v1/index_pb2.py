"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/datastore/admin/v1/index.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/datastore/admin/v1/index.proto\x12\x19google.datastore.admin.v1\x1a\x1fgoogle/api/field_behavior.proto"\xe6\x04\n\x05Index\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x15\n\x08index_id\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04kind\x18\x04 \x01(\tB\x03\xe0A\x02\x12D\n\x08ancestor\x18\x05 \x01(\x0e2-.google.datastore.admin.v1.Index.AncestorModeB\x03\xe0A\x02\x12I\n\nproperties\x18\x06 \x03(\x0b20.google.datastore.admin.v1.Index.IndexedPropertyB\x03\xe0A\x02\x12:\n\x05state\x18\x07 \x01(\x0e2&.google.datastore.admin.v1.Index.StateB\x03\xe0A\x03\x1ah\n\x0fIndexedProperty\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12B\n\tdirection\x18\x02 \x01(\x0e2*.google.datastore.admin.v1.Index.DirectionB\x03\xe0A\x02"J\n\x0cAncestorMode\x12\x1d\n\x19ANCESTOR_MODE_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\x11\n\rALL_ANCESTORS\x10\x02"E\n\tDirection\x12\x19\n\x15DIRECTION_UNSPECIFIED\x10\x00\x12\r\n\tASCENDING\x10\x01\x12\x0e\n\nDESCENDING\x10\x02"P\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\t\n\x05ERROR\x10\x04B\xd2\x01\n\x1dcom.google.datastore.admin.v1B\nIndexProtoP\x01Z9cloud.google.com/go/datastore/admin/apiv1/adminpb;adminpb\xaa\x02\x1fGoogle.Cloud.Datastore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Datastore\\Admin\\V1\xea\x02#Google::Cloud::Datastore::Admin::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.datastore.admin.v1.index_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.datastore.admin.v1B\nIndexProtoP\x01Z9cloud.google.com/go/datastore/admin/apiv1/adminpb;adminpb\xaa\x02\x1fGoogle.Cloud.Datastore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Datastore\\Admin\\V1\xea\x02#Google::Cloud::Datastore::Admin::V1'
    _globals['_INDEX_INDEXEDPROPERTY'].fields_by_name['name']._loaded_options = None
    _globals['_INDEX_INDEXEDPROPERTY'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_INDEX_INDEXEDPROPERTY'].fields_by_name['direction']._loaded_options = None
    _globals['_INDEX_INDEXEDPROPERTY'].fields_by_name['direction']._serialized_options = b'\xe0A\x02'
    _globals['_INDEX'].fields_by_name['project_id']._loaded_options = None
    _globals['_INDEX'].fields_by_name['project_id']._serialized_options = b'\xe0A\x03'
    _globals['_INDEX'].fields_by_name['index_id']._loaded_options = None
    _globals['_INDEX'].fields_by_name['index_id']._serialized_options = b'\xe0A\x03'
    _globals['_INDEX'].fields_by_name['kind']._loaded_options = None
    _globals['_INDEX'].fields_by_name['kind']._serialized_options = b'\xe0A\x02'
    _globals['_INDEX'].fields_by_name['ancestor']._loaded_options = None
    _globals['_INDEX'].fields_by_name['ancestor']._serialized_options = b'\xe0A\x02'
    _globals['_INDEX'].fields_by_name['properties']._loaded_options = None
    _globals['_INDEX'].fields_by_name['properties']._serialized_options = b'\xe0A\x02'
    _globals['_INDEX'].fields_by_name['state']._loaded_options = None
    _globals['_INDEX'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_INDEX']._serialized_start = 102
    _globals['_INDEX']._serialized_end = 716
    _globals['_INDEX_INDEXEDPROPERTY']._serialized_start = 383
    _globals['_INDEX_INDEXEDPROPERTY']._serialized_end = 487
    _globals['_INDEX_ANCESTORMODE']._serialized_start = 489
    _globals['_INDEX_ANCESTORMODE']._serialized_end = 563
    _globals['_INDEX_DIRECTION']._serialized_start = 565
    _globals['_INDEX_DIRECTION']._serialized_end = 634
    _globals['_INDEX_STATE']._serialized_start = 636
    _globals['_INDEX_STATE']._serialized_end = 716