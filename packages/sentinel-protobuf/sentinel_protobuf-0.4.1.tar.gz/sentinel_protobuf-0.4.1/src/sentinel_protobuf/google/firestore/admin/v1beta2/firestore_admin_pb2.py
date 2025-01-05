"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/admin/v1beta2/firestore_admin.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.firestore.admin.v1beta2 import field_pb2 as google_dot_firestore_dot_admin_dot_v1beta2_dot_field__pb2
from .....google.firestore.admin.v1beta2 import index_pb2 as google_dot_firestore_dot_admin_dot_v1beta2_dot_index__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/firestore/admin/v1beta2/firestore_admin.proto\x12\x1egoogle.firestore.admin.v1beta2\x1a\x1cgoogle/api/annotations.proto\x1a*google/firestore/admin/v1beta2/field.proto\x1a*google/firestore/admin/v1beta2/index.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/api/client.proto"Z\n\x12CreateIndexRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x124\n\x05index\x18\x02 \x01(\x0b2%.google.firestore.admin.v1beta2.Index"[\n\x12ListIndexesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"f\n\x13ListIndexesResponse\x126\n\x07indexes\x18\x01 \x03(\x0b2%.google.firestore.admin.v1beta2.Index\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x1f\n\x0fGetIndexRequest\x12\x0c\n\x04name\x18\x01 \x01(\t""\n\x12DeleteIndexRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"{\n\x12UpdateFieldRequest\x124\n\x05field\x18\x01 \x01(\x0b2%.google.firestore.admin.v1beta2.Field\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x1f\n\x0fGetFieldRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"Z\n\x11ListFieldsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"d\n\x12ListFieldsResponse\x125\n\x06fields\x18\x01 \x03(\x0b2%.google.firestore.admin.v1beta2.Field\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"Y\n\x16ExportDocumentsRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0ecollection_ids\x18\x02 \x03(\t\x12\x19\n\x11output_uri_prefix\x18\x03 \x01(\t"X\n\x16ImportDocumentsRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0ecollection_ids\x18\x02 \x03(\t\x12\x18\n\x10input_uri_prefix\x18\x03 \x01(\t2\xeb\r\n\x0eFirestoreAdmin\x12\xb4\x01\n\x0bCreateIndex\x122.google.firestore.admin.v1beta2.CreateIndexRequest\x1a\x1d.google.longrunning.Operation"R\x82\xd3\xe4\x93\x02L"C/v1beta2/{parent=projects/*/databases/*/collectionGroups/*}/indexes:\x05index\x12\xc3\x01\n\x0bListIndexes\x122.google.firestore.admin.v1beta2.ListIndexesRequest\x1a3.google.firestore.admin.v1beta2.ListIndexesResponse"K\x82\xd3\xe4\x93\x02E\x12C/v1beta2/{parent=projects/*/databases/*/collectionGroups/*}/indexes\x12\xaf\x01\n\x08GetIndex\x12/.google.firestore.admin.v1beta2.GetIndexRequest\x1a%.google.firestore.admin.v1beta2.Index"K\x82\xd3\xe4\x93\x02E\x12C/v1beta2/{name=projects/*/databases/*/collectionGroups/*/indexes/*}\x12\xa6\x01\n\x0bDeleteIndex\x122.google.firestore.admin.v1beta2.DeleteIndexRequest\x1a\x16.google.protobuf.Empty"K\x82\xd3\xe4\x93\x02E*C/v1beta2/{name=projects/*/databases/*/collectionGroups/*/indexes/*}\x12\xae\x01\n\x08GetField\x12/.google.firestore.admin.v1beta2.GetFieldRequest\x1a%.google.firestore.admin.v1beta2.Field"J\x82\xd3\xe4\x93\x02D\x12B/v1beta2/{name=projects/*/databases/*/collectionGroups/*/fields/*}\x12\xb9\x01\n\x0bUpdateField\x122.google.firestore.admin.v1beta2.UpdateFieldRequest\x1a\x1d.google.longrunning.Operation"W\x82\xd3\xe4\x93\x02Q2H/v1beta2/{field.name=projects/*/databases/*/collectionGroups/*/fields/*}:\x05field\x12\xbf\x01\n\nListFields\x121.google.firestore.admin.v1beta2.ListFieldsRequest\x1a2.google.firestore.admin.v1beta2.ListFieldsResponse"J\x82\xd3\xe4\x93\x02D\x12B/v1beta2/{parent=projects/*/databases/*/collectionGroups/*}/fields\x12\xab\x01\n\x0fExportDocuments\x126.google.firestore.admin.v1beta2.ExportDocumentsRequest\x1a\x1d.google.longrunning.Operation"A\x82\xd3\xe4\x93\x02;"6/v1beta2/{name=projects/*/databases/*}:exportDocuments:\x01*\x12\xab\x01\n\x0fImportDocuments\x126.google.firestore.admin.v1beta2.ImportDocumentsRequest\x1a\x1d.google.longrunning.Operation"A\x82\xd3\xe4\x93\x02;"6/v1beta2/{name=projects/*/databases/*}:importDocuments:\x01*\x1av\xcaA\x18firestore.googleapis.com\xd2AXhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/datastoreB\xa9\x01\n"com.google.firestore.admin.v1beta2B\x13FirestoreAdminProtoP\x01Z>cloud.google.com/go/firestore/admin/apiv1beta2/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02$Google.Cloud.Firestore.Admin.V1Beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.admin.v1beta2.firestore_admin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.firestore.admin.v1beta2B\x13FirestoreAdminProtoP\x01Z>cloud.google.com/go/firestore/admin/apiv1beta2/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02$Google.Cloud.Firestore.Admin.V1Beta2'
    _globals['_FIRESTOREADMIN']._loaded_options = None
    _globals['_FIRESTOREADMIN']._serialized_options = b'\xcaA\x18firestore.googleapis.com\xd2AXhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/datastore'
    _globals['_FIRESTOREADMIN'].methods_by_name['CreateIndex']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['CreateIndex']._serialized_options = b'\x82\xd3\xe4\x93\x02L"C/v1beta2/{parent=projects/*/databases/*/collectionGroups/*}/indexes:\x05index'
    _globals['_FIRESTOREADMIN'].methods_by_name['ListIndexes']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['ListIndexes']._serialized_options = b'\x82\xd3\xe4\x93\x02E\x12C/v1beta2/{parent=projects/*/databases/*/collectionGroups/*}/indexes'
    _globals['_FIRESTOREADMIN'].methods_by_name['GetIndex']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['GetIndex']._serialized_options = b'\x82\xd3\xe4\x93\x02E\x12C/v1beta2/{name=projects/*/databases/*/collectionGroups/*/indexes/*}'
    _globals['_FIRESTOREADMIN'].methods_by_name['DeleteIndex']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['DeleteIndex']._serialized_options = b'\x82\xd3\xe4\x93\x02E*C/v1beta2/{name=projects/*/databases/*/collectionGroups/*/indexes/*}'
    _globals['_FIRESTOREADMIN'].methods_by_name['GetField']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['GetField']._serialized_options = b'\x82\xd3\xe4\x93\x02D\x12B/v1beta2/{name=projects/*/databases/*/collectionGroups/*/fields/*}'
    _globals['_FIRESTOREADMIN'].methods_by_name['UpdateField']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['UpdateField']._serialized_options = b'\x82\xd3\xe4\x93\x02Q2H/v1beta2/{field.name=projects/*/databases/*/collectionGroups/*/fields/*}:\x05field'
    _globals['_FIRESTOREADMIN'].methods_by_name['ListFields']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['ListFields']._serialized_options = b'\x82\xd3\xe4\x93\x02D\x12B/v1beta2/{parent=projects/*/databases/*/collectionGroups/*}/fields'
    _globals['_FIRESTOREADMIN'].methods_by_name['ExportDocuments']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['ExportDocuments']._serialized_options = b'\x82\xd3\xe4\x93\x02;"6/v1beta2/{name=projects/*/databases/*}:exportDocuments:\x01*'
    _globals['_FIRESTOREADMIN'].methods_by_name['ImportDocuments']._loaded_options = None
    _globals['_FIRESTOREADMIN'].methods_by_name['ImportDocuments']._serialized_options = b'\x82\xd3\xe4\x93\x02;"6/v1beta2/{name=projects/*/databases/*}:importDocuments:\x01*'
    _globals['_CREATEINDEXREQUEST']._serialized_start = 331
    _globals['_CREATEINDEXREQUEST']._serialized_end = 421
    _globals['_LISTINDEXESREQUEST']._serialized_start = 423
    _globals['_LISTINDEXESREQUEST']._serialized_end = 514
    _globals['_LISTINDEXESRESPONSE']._serialized_start = 516
    _globals['_LISTINDEXESRESPONSE']._serialized_end = 618
    _globals['_GETINDEXREQUEST']._serialized_start = 620
    _globals['_GETINDEXREQUEST']._serialized_end = 651
    _globals['_DELETEINDEXREQUEST']._serialized_start = 653
    _globals['_DELETEINDEXREQUEST']._serialized_end = 687
    _globals['_UPDATEFIELDREQUEST']._serialized_start = 689
    _globals['_UPDATEFIELDREQUEST']._serialized_end = 812
    _globals['_GETFIELDREQUEST']._serialized_start = 814
    _globals['_GETFIELDREQUEST']._serialized_end = 845
    _globals['_LISTFIELDSREQUEST']._serialized_start = 847
    _globals['_LISTFIELDSREQUEST']._serialized_end = 937
    _globals['_LISTFIELDSRESPONSE']._serialized_start = 939
    _globals['_LISTFIELDSRESPONSE']._serialized_end = 1039
    _globals['_EXPORTDOCUMENTSREQUEST']._serialized_start = 1041
    _globals['_EXPORTDOCUMENTSREQUEST']._serialized_end = 1130
    _globals['_IMPORTDOCUMENTSREQUEST']._serialized_start = 1132
    _globals['_IMPORTDOCUMENTSREQUEST']._serialized_end = 1220
    _globals['_FIRESTOREADMIN']._serialized_start = 1223
    _globals['_FIRESTOREADMIN']._serialized_end = 2994