"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/admin/v1beta1/firestore_admin.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.firestore.admin.v1beta1 import index_pb2 as google_dot_firestore_dot_admin_dot_v1beta1_dot_index__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/firestore/admin/v1beta1/firestore_admin.proto\x12\x1egoogle.firestore.admin.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a*google/firestore/admin/v1beta1/index.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/api/client.proto"\x80\x03\n\x16IndexOperationMetadata\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\r\n\x05index\x18\x03 \x01(\t\x12\\\n\x0eoperation_type\x18\x04 \x01(\x0e2D.google.firestore.admin.v1beta1.IndexOperationMetadata.OperationType\x12\x11\n\tcancelled\x18\x05 \x01(\x08\x12C\n\x11document_progress\x18\x06 \x01(\x0b2(.google.firestore.admin.v1beta1.Progress"C\n\rOperationType\x12\x1e\n\x1aOPERATION_TYPE_UNSPECIFIED\x10\x00\x12\x12\n\x0eCREATING_INDEX\x10\x01":\n\x08Progress\x12\x16\n\x0ework_completed\x18\x01 \x01(\x03\x12\x16\n\x0ework_estimated\x18\x02 \x01(\x03"Z\n\x12CreateIndexRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x124\n\x05index\x18\x02 \x01(\x0b2%.google.firestore.admin.v1beta1.Index"\x1f\n\x0fGetIndexRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"[\n\x12ListIndexesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t""\n\x12DeleteIndexRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"f\n\x13ListIndexesResponse\x126\n\x07indexes\x18\x01 \x03(\x0b2%.google.firestore.admin.v1beta1.Index\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"Y\n\x16ExportDocumentsRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0ecollection_ids\x18\x03 \x03(\t\x12\x19\n\x11output_uri_prefix\x18\x04 \x01(\t"X\n\x16ImportDocumentsRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0ecollection_ids\x18\x03 \x03(\t\x12\x18\n\x10input_uri_prefix\x18\x04 \x01(\t"4\n\x17ExportDocumentsResponse\x12\x19\n\x11output_uri_prefix\x18\x01 \x01(\t"\xfb\x02\n\x17ExportDocumentsMetadata\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12G\n\x0foperation_state\x18\x03 \x01(\x0e2..google.firestore.admin.v1beta1.OperationState\x12D\n\x12progress_documents\x18\x04 \x01(\x0b2(.google.firestore.admin.v1beta1.Progress\x12@\n\x0eprogress_bytes\x18\x05 \x01(\x0b2(.google.firestore.admin.v1beta1.Progress\x12\x16\n\x0ecollection_ids\x18\x06 \x03(\t\x12\x19\n\x11output_uri_prefix\x18\x07 \x01(\t"\xfa\x02\n\x17ImportDocumentsMetadata\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12G\n\x0foperation_state\x18\x03 \x01(\x0e2..google.firestore.admin.v1beta1.OperationState\x12D\n\x12progress_documents\x18\x04 \x01(\x0b2(.google.firestore.admin.v1beta1.Progress\x12@\n\x0eprogress_bytes\x18\x05 \x01(\x0b2(.google.firestore.admin.v1beta1.Progress\x12\x16\n\x0ecollection_ids\x18\x06 \x03(\t\x12\x18\n\x10input_uri_prefix\x18\x07 \x01(\t*\x94\x01\n\x0eOperationState\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cINITIALIZING\x10\x01\x12\x0e\n\nPROCESSING\x10\x02\x12\x0e\n\nCANCELLING\x10\x03\x12\x0e\n\nFINALIZING\x10\x04\x12\x0e\n\nSUCCESSFUL\x10\x05\x12\n\n\x06FAILED\x10\x06\x12\r\n\tCANCELLED\x10\x072\xf0\x08\n\x0eFirestoreAdmin\x12\xa1\x01\n\x0bCreateIndex\x122.google.firestore.admin.v1beta1.CreateIndexRequest\x1a\x1d.google.longrunning.Operation"?\x82\xd3\xe4\x93\x029"0/v1beta1/{parent=projects/*/databases/*}/indexes:\x05index\x12\xb0\x01\n\x0bListIndexes\x122.google.firestore.admin.v1beta1.ListIndexesRequest\x1a3.google.firestore.admin.v1beta1.ListIndexesResponse"8\x82\xd3\xe4\x93\x022\x120/v1beta1/{parent=projects/*/databases/*}/indexes\x12\x9c\x01\n\x08GetIndex\x12/.google.firestore.admin.v1beta1.GetIndexRequest\x1a%.google.firestore.admin.v1beta1.Index"8\x82\xd3\xe4\x93\x022\x120/v1beta1/{name=projects/*/databases/*/indexes/*}\x12\x93\x01\n\x0bDeleteIndex\x122.google.firestore.admin.v1beta1.DeleteIndexRequest\x1a\x16.google.protobuf.Empty"8\x82\xd3\xe4\x93\x022*0/v1beta1/{name=projects/*/databases/*/indexes/*}\x12\xab\x01\n\x0fExportDocuments\x126.google.firestore.admin.v1beta1.ExportDocumentsRequest\x1a\x1d.google.longrunning.Operation"A\x82\xd3\xe4\x93\x02;"6/v1beta1/{name=projects/*/databases/*}:exportDocuments:\x01*\x12\xab\x01\n\x0fImportDocuments\x126.google.firestore.admin.v1beta1.ImportDocumentsRequest\x1a\x1d.google.longrunning.Operation"A\x82\xd3\xe4\x93\x02;"6/v1beta1/{name=projects/*/databases/*}:importDocuments:\x01*\x1av\xcaA\x18firestore.googleapis.com\xd2AXhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/datastoreB\xa9\x01\n"com.google.firestore.admin.v1beta1B\x13FirestoreAdminProtoP\x01Z>cloud.google.com/go/firestore/admin/apiv1beta1/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02$Google.Cloud.Firestore.Admin.V1Beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.admin.v1beta1.firestore_admin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.firestore.admin.v1beta1B\x13FirestoreAdminProtoP\x01Z>cloud.google.com/go/firestore/admin/apiv1beta1/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02$Google.Cloud.Firestore.Admin.V1Beta1'
    _globals['_FIRESTOREADMIN']._loaded_options = None
    _globals['_FIRESTOREADMIN']._serialized_options = b'\xcaA\x18firestore.googleapis.com\xd2AXhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/datastore'
    _globals['_FIRESTOREADMIN'].methods_by_name['CreateIndex']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['CreateIndex']._serialized_options = b'\x82\xd3\xe4\x93\x029"0/v1beta1/{parent=projects/*/databases/*}/indexes:\x05index'
    _globals['_FIRESTOREADMIN'].methods_by_name['ListIndexes']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['ListIndexes']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/v1beta1/{parent=projects/*/databases/*}/indexes'
    _globals['_FIRESTOREADMIN'].methods_by_name['GetIndex']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['GetIndex']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/v1beta1/{name=projects/*/databases/*/indexes/*}'
    _globals['_FIRESTOREADMIN'].methods_by_name['DeleteIndex']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['DeleteIndex']._serialized_options = b'\x82\xd3\xe4\x93\x022*0/v1beta1/{name=projects/*/databases/*/indexes/*}'
    _globals['_FIRESTOREADMIN'].methods_by_name['ExportDocuments']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['ExportDocuments']._serialized_options = b'\x82\xd3\xe4\x93\x02;"6/v1beta1/{name=projects/*/databases/*}:exportDocuments:\x01*'
    _globals['_FIRESTOREADMIN'].methods_by_name['ImportDocuments']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['ImportDocuments']._serialized_options = b'\x82\xd3\xe4\x93\x02;"6/v1beta1/{name=projects/*/databases/*}:importDocuments:\x01*'
    _globals['_OPERATIONSTATE']._serialized_start = 2090
    _globals['_OPERATIONSTATE']._serialized_end = 2238
    _globals['_INDEXOPERATIONMETADATA']._serialized_start = 287
    _globals['_INDEXOPERATIONMETADATA']._serialized_end = 671
    _globals['_INDEXOPERATIONMETADATA_OPERATIONTYPE']._serialized_start = 604
    _globals['_INDEXOPERATIONMETADATA_OPERATIONTYPE']._serialized_end = 671
    _globals['_PROGRESS']._serialized_start = 673
    _globals['_PROGRESS']._serialized_end = 731
    _globals['_CREATEINDEXREQUEST']._serialized_start = 733
    _globals['_CREATEINDEXREQUEST']._serialized_end = 823
    _globals['_GETINDEXREQUEST']._serialized_start = 825
    _globals['_GETINDEXREQUEST']._serialized_end = 856
    _globals['_LISTINDEXESREQUEST']._serialized_start = 858
    _globals['_LISTINDEXESREQUEST']._serialized_end = 949
    _globals['_DELETEINDEXREQUEST']._serialized_start = 951
    _globals['_DELETEINDEXREQUEST']._serialized_end = 985
    _globals['_LISTINDEXESRESPONSE']._serialized_start = 987
    _globals['_LISTINDEXESRESPONSE']._serialized_end = 1089
    _globals['_EXPORTDOCUMENTSREQUEST']._serialized_start = 1091
    _globals['_EXPORTDOCUMENTSREQUEST']._serialized_end = 1180
    _globals['_IMPORTDOCUMENTSREQUEST']._serialized_start = 1182
    _globals['_IMPORTDOCUMENTSREQUEST']._serialized_end = 1270
    _globals['_EXPORTDOCUMENTSRESPONSE']._serialized_start = 1272
    _globals['_EXPORTDOCUMENTSRESPONSE']._serialized_end = 1324
    _globals['_EXPORTDOCUMENTSMETADATA']._serialized_start = 1327
    _globals['_EXPORTDOCUMENTSMETADATA']._serialized_end = 1706
    _globals['_IMPORTDOCUMENTSMETADATA']._serialized_start = 1709
    _globals['_IMPORTDOCUMENTSMETADATA']._serialized_end = 2087
    _globals['_FIRESTOREADMIN']._serialized_start = 2241
    _globals['_FIRESTOREADMIN']._serialized_end = 3377