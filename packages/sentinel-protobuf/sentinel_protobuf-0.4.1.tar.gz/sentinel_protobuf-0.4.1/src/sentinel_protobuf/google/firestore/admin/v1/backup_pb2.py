"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/admin/v1/backup.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/firestore/admin/v1/backup.proto\x12\x19google.firestore.admin.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe0\x04\n\x06Backup\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12;\n\x08database\x18\x02 \x01(\tB)\xe0A\x03\xfaA#\n!firestore.googleapis.com/Database\x12\x19\n\x0cdatabase_uid\x18\x07 \x01(\tB\x03\xe0A\x03\x126\n\rsnapshot_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bexpire_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12;\n\x05stats\x18\x06 \x01(\x0b2\'.google.firestore.admin.v1.Backup.StatsB\x03\xe0A\x03\x12;\n\x05state\x18\x08 \x01(\x0e2\'.google.firestore.admin.v1.Backup.StateB\x03\xe0A\x03\x1aW\n\x05Stats\x12\x17\n\nsize_bytes\x18\x01 \x01(\x03B\x03\xe0A\x03\x12\x1b\n\x0edocument_count\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x18\n\x0bindex_count\x18\x03 \x01(\x03B\x03\xe0A\x03"J\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x11\n\rNOT_AVAILABLE\x10\x03:^\xeaA[\n\x1ffirestore.googleapis.com/Backup\x128projects/{project}/locations/{location}/backups/{backup}B\xda\x01\n\x1dcom.google.firestore.admin.v1B\x0bBackupProtoP\x01Z9cloud.google.com/go/firestore/apiv1/admin/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02\x1fGoogle.Cloud.Firestore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Firestore\\Admin\\V1\xea\x02#Google::Cloud::Firestore::Admin::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.admin.v1.backup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.firestore.admin.v1B\x0bBackupProtoP\x01Z9cloud.google.com/go/firestore/apiv1/admin/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02\x1fGoogle.Cloud.Firestore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Firestore\\Admin\\V1\xea\x02#Google::Cloud::Firestore::Admin::V1'
    _globals['_BACKUP_STATS'].fields_by_name['size_bytes']._loaded_options = None
    _globals['_BACKUP_STATS'].fields_by_name['size_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP_STATS'].fields_by_name['document_count']._loaded_options = None
    _globals['_BACKUP_STATS'].fields_by_name['document_count']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP_STATS'].fields_by_name['index_count']._loaded_options = None
    _globals['_BACKUP_STATS'].fields_by_name['index_count']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['name']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['database']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['database']._serialized_options = b'\xe0A\x03\xfaA#\n!firestore.googleapis.com/Database'
    _globals['_BACKUP'].fields_by_name['database_uid']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['database_uid']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['snapshot_time']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['snapshot_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['expire_time']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['stats']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['stats']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['state']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP']._loaded_options = None
    _globals['_BACKUP']._serialized_options = b'\xeaA[\n\x1ffirestore.googleapis.com/Backup\x128projects/{project}/locations/{location}/backups/{backup}'
    _globals['_BACKUP']._serialized_start = 163
    _globals['_BACKUP']._serialized_end = 771
    _globals['_BACKUP_STATS']._serialized_start = 512
    _globals['_BACKUP_STATS']._serialized_end = 599
    _globals['_BACKUP_STATE']._serialized_start = 601
    _globals['_BACKUP_STATE']._serialized_end = 675