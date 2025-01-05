"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/admin/v1/operation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.firestore.admin.v1 import index_pb2 as google_dot_firestore_dot_admin_dot_v1_dot_index__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/firestore/admin/v1/operation.proto\x12\x19google.firestore.admin.v1\x1a\x19google/api/resource.proto\x1a%google/firestore/admin/v1/index.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbd\x02\n\x16IndexOperationMetadata\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\r\n\x05index\x18\x03 \x01(\t\x128\n\x05state\x18\x04 \x01(\x0e2).google.firestore.admin.v1.OperationState\x12?\n\x12progress_documents\x18\x05 \x01(\x0b2#.google.firestore.admin.v1.Progress\x12;\n\x0eprogress_bytes\x18\x06 \x01(\x0b2#.google.firestore.admin.v1.Progress"\x99\x07\n\x16FieldOperationMetadata\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\r\n\x05field\x18\x03 \x01(\t\x12_\n\x13index_config_deltas\x18\x04 \x03(\x0b2B.google.firestore.admin.v1.FieldOperationMetadata.IndexConfigDelta\x128\n\x05state\x18\x05 \x01(\x0e2).google.firestore.admin.v1.OperationState\x12?\n\x12progress_documents\x18\x06 \x01(\x0b2#.google.firestore.admin.v1.Progress\x12;\n\x0eprogress_bytes\x18\x07 \x01(\x0b2#.google.firestore.admin.v1.Progress\x12Z\n\x10ttl_config_delta\x18\x08 \x01(\x0b2@.google.firestore.admin.v1.FieldOperationMetadata.TtlConfigDelta\x1a\xe7\x01\n\x10IndexConfigDelta\x12b\n\x0bchange_type\x18\x01 \x01(\x0e2M.google.firestore.admin.v1.FieldOperationMetadata.IndexConfigDelta.ChangeType\x12/\n\x05index\x18\x02 \x01(\x0b2 .google.firestore.admin.v1.Index">\n\nChangeType\x12\x1b\n\x17CHANGE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03ADD\x10\x01\x12\n\n\x06REMOVE\x10\x02\x1a\xb2\x01\n\x0eTtlConfigDelta\x12`\n\x0bchange_type\x18\x01 \x01(\x0e2K.google.firestore.admin.v1.FieldOperationMetadata.TtlConfigDelta.ChangeType">\n\nChangeType\x12\x1b\n\x17CHANGE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03ADD\x10\x01\x12\n\n\x06REMOVE\x10\x02"\xb6\x03\n\x17ExportDocumentsMetadata\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12B\n\x0foperation_state\x18\x03 \x01(\x0e2).google.firestore.admin.v1.OperationState\x12?\n\x12progress_documents\x18\x04 \x01(\x0b2#.google.firestore.admin.v1.Progress\x12;\n\x0eprogress_bytes\x18\x05 \x01(\x0b2#.google.firestore.admin.v1.Progress\x12\x16\n\x0ecollection_ids\x18\x06 \x03(\t\x12\x19\n\x11output_uri_prefix\x18\x07 \x01(\t\x12\x15\n\rnamespace_ids\x18\x08 \x03(\t\x121\n\rsnapshot_time\x18\t \x01(\x0b2\x1a.google.protobuf.Timestamp"\x82\x03\n\x17ImportDocumentsMetadata\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12B\n\x0foperation_state\x18\x03 \x01(\x0e2).google.firestore.admin.v1.OperationState\x12?\n\x12progress_documents\x18\x04 \x01(\x0b2#.google.firestore.admin.v1.Progress\x12;\n\x0eprogress_bytes\x18\x05 \x01(\x0b2#.google.firestore.admin.v1.Progress\x12\x16\n\x0ecollection_ids\x18\x06 \x03(\t\x12\x18\n\x10input_uri_prefix\x18\x07 \x01(\t\x12\x15\n\rnamespace_ids\x18\x08 \x03(\t"\x9f\x03\n\x1bBulkDeleteDocumentsMetadata\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12B\n\x0foperation_state\x18\x03 \x01(\x0e2).google.firestore.admin.v1.OperationState\x12?\n\x12progress_documents\x18\x04 \x01(\x0b2#.google.firestore.admin.v1.Progress\x12;\n\x0eprogress_bytes\x18\x05 \x01(\x0b2#.google.firestore.admin.v1.Progress\x12\x16\n\x0ecollection_ids\x18\x06 \x03(\t\x12\x15\n\rnamespace_ids\x18\x07 \x03(\t\x121\n\rsnapshot_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.Timestamp"4\n\x17ExportDocumentsResponse\x12\x19\n\x11output_uri_prefix\x18\x01 \x01(\t"\xed\x02\n\x17RestoreDatabaseMetadata\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12B\n\x0foperation_state\x18\x03 \x01(\x0e2).google.firestore.admin.v1.OperationState\x128\n\x08database\x18\x04 \x01(\tB&\xfaA#\n!firestore.googleapis.com/Database\x124\n\x06backup\x18\x05 \x01(\tB$\xfaA!\n\x1ffirestore.googleapis.com/Backup\x12@\n\x13progress_percentage\x18\x08 \x01(\x0b2#.google.firestore.admin.v1.Progress":\n\x08Progress\x12\x16\n\x0eestimated_work\x18\x01 \x01(\x03\x12\x16\n\x0ecompleted_work\x18\x02 \x01(\x03*\x9e\x01\n\x0eOperationState\x12\x1f\n\x1bOPERATION_STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cINITIALIZING\x10\x01\x12\x0e\n\nPROCESSING\x10\x02\x12\x0e\n\nCANCELLING\x10\x03\x12\x0e\n\nFINALIZING\x10\x04\x12\x0e\n\nSUCCESSFUL\x10\x05\x12\n\n\x06FAILED\x10\x06\x12\r\n\tCANCELLED\x10\x07B\xdd\x01\n\x1dcom.google.firestore.admin.v1B\x0eOperationProtoP\x01Z9cloud.google.com/go/firestore/apiv1/admin/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02\x1fGoogle.Cloud.Firestore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Firestore\\Admin\\V1\xea\x02#Google::Cloud::Firestore::Admin::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.admin.v1.operation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.firestore.admin.v1B\x0eOperationProtoP\x01Z9cloud.google.com/go/firestore/apiv1/admin/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02\x1fGoogle.Cloud.Firestore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Firestore\\Admin\\V1\xea\x02#Google::Cloud::Firestore::Admin::V1'
    _globals['_RESTOREDATABASEMETADATA'].fields_by_name['database']._loaded_options = None
    _globals['_RESTOREDATABASEMETADATA'].fields_by_name['database']._serialized_options = b'\xfaA#\n!firestore.googleapis.com/Database'
    _globals['_RESTOREDATABASEMETADATA'].fields_by_name['backup']._loaded_options = None
    _globals['_RESTOREDATABASEMETADATA'].fields_by_name['backup']._serialized_options = b'\xfaA!\n\x1ffirestore.googleapis.com/Backup'
    _globals['_OPERATIONSTATE']._serialized_start = 3146
    _globals['_OPERATIONSTATE']._serialized_end = 3304
    _globals['_INDEXOPERATIONMETADATA']._serialized_start = 172
    _globals['_INDEXOPERATIONMETADATA']._serialized_end = 489
    _globals['_FIELDOPERATIONMETADATA']._serialized_start = 492
    _globals['_FIELDOPERATIONMETADATA']._serialized_end = 1413
    _globals['_FIELDOPERATIONMETADATA_INDEXCONFIGDELTA']._serialized_start = 1001
    _globals['_FIELDOPERATIONMETADATA_INDEXCONFIGDELTA']._serialized_end = 1232
    _globals['_FIELDOPERATIONMETADATA_INDEXCONFIGDELTA_CHANGETYPE']._serialized_start = 1170
    _globals['_FIELDOPERATIONMETADATA_INDEXCONFIGDELTA_CHANGETYPE']._serialized_end = 1232
    _globals['_FIELDOPERATIONMETADATA_TTLCONFIGDELTA']._serialized_start = 1235
    _globals['_FIELDOPERATIONMETADATA_TTLCONFIGDELTA']._serialized_end = 1413
    _globals['_FIELDOPERATIONMETADATA_TTLCONFIGDELTA_CHANGETYPE']._serialized_start = 1170
    _globals['_FIELDOPERATIONMETADATA_TTLCONFIGDELTA_CHANGETYPE']._serialized_end = 1232
    _globals['_EXPORTDOCUMENTSMETADATA']._serialized_start = 1416
    _globals['_EXPORTDOCUMENTSMETADATA']._serialized_end = 1854
    _globals['_IMPORTDOCUMENTSMETADATA']._serialized_start = 1857
    _globals['_IMPORTDOCUMENTSMETADATA']._serialized_end = 2243
    _globals['_BULKDELETEDOCUMENTSMETADATA']._serialized_start = 2246
    _globals['_BULKDELETEDOCUMENTSMETADATA']._serialized_end = 2661
    _globals['_EXPORTDOCUMENTSRESPONSE']._serialized_start = 2663
    _globals['_EXPORTDOCUMENTSRESPONSE']._serialized_end = 2715
    _globals['_RESTOREDATABASEMETADATA']._serialized_start = 2718
    _globals['_RESTOREDATABASEMETADATA']._serialized_end = 3083
    _globals['_PROGRESS']._serialized_start = 3085
    _globals['_PROGRESS']._serialized_end = 3143