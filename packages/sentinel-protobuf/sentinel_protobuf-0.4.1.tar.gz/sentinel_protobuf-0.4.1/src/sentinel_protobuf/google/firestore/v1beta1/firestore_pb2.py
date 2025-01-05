"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/v1beta1/firestore.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.firestore.v1beta1 import common_pb2 as google_dot_firestore_dot_v1beta1_dot_common__pb2
from ....google.firestore.v1beta1 import document_pb2 as google_dot_firestore_dot_v1beta1_dot_document__pb2
from ....google.firestore.v1beta1 import query_pb2 as google_dot_firestore_dot_v1beta1_dot_query__pb2
from ....google.firestore.v1beta1 import write_pb2 as google_dot_firestore_dot_v1beta1_dot_write__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/firestore/v1beta1/firestore.proto\x12\x18google.firestore.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a%google/firestore/v1beta1/common.proto\x1a\'google/firestore/v1beta1/document.proto\x1a$google/firestore/v1beta1/query.proto\x1a$google/firestore/v1beta1/write.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xbd\x01\n\x12GetDocumentRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x124\n\x04mask\x18\x02 \x01(\x0b2&.google.firestore.v1beta1.DocumentMask\x12\x15\n\x0btransaction\x18\x03 \x01(\x0cH\x00\x12/\n\tread_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00B\x16\n\x14consistency_selector"\xac\x02\n\x14ListDocumentsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rcollection_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x06 \x01(\t\x124\n\x04mask\x18\x07 \x01(\x0b2&.google.firestore.v1beta1.DocumentMask\x12\x15\n\x0btransaction\x18\x08 \x01(\x0cH\x00\x12/\n\tread_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x12\x14\n\x0cshow_missing\x18\x0c \x01(\x08B\x16\n\x14consistency_selector"g\n\x15ListDocumentsResponse\x125\n\tdocuments\x18\x01 \x03(\x0b2".google.firestore.v1beta1.Document\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xce\x01\n\x15CreateDocumentRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rcollection_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdocument_id\x18\x03 \x01(\t\x129\n\x08document\x18\x04 \x01(\x0b2".google.firestore.v1beta1.DocumentB\x03\xe0A\x02\x124\n\x04mask\x18\x05 \x01(\x0b2&.google.firestore.v1beta1.DocumentMask"\x87\x02\n\x15UpdateDocumentRequest\x129\n\x08document\x18\x01 \x01(\x0b2".google.firestore.v1beta1.DocumentB\x03\xe0A\x02\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b2&.google.firestore.v1beta1.DocumentMask\x124\n\x04mask\x18\x03 \x01(\x0b2&.google.firestore.v1beta1.DocumentMask\x12@\n\x10current_document\x18\x04 \x01(\x0b2&.google.firestore.v1beta1.Precondition"l\n\x15DeleteDocumentRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12@\n\x10current_document\x18\x02 \x01(\x0b2&.google.firestore.v1beta1.Precondition"\xa3\x02\n\x18BatchGetDocumentsRequest\x12\x15\n\x08database\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\tdocuments\x18\x02 \x03(\t\x124\n\x04mask\x18\x03 \x01(\x0b2&.google.firestore.v1beta1.DocumentMask\x12\x15\n\x0btransaction\x18\x04 \x01(\x0cH\x00\x12G\n\x0fnew_transaction\x18\x05 \x01(\x0b2,.google.firestore.v1beta1.TransactionOptionsH\x00\x12/\n\tread_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00B\x16\n\x14consistency_selector"\xb1\x01\n\x19BatchGetDocumentsResponse\x123\n\x05found\x18\x01 \x01(\x0b2".google.firestore.v1beta1.DocumentH\x00\x12\x11\n\x07missing\x18\x02 \x01(\tH\x00\x12\x13\n\x0btransaction\x18\x03 \x01(\x0c\x12-\n\tread_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\n\x06result"o\n\x17BeginTransactionRequest\x12\x15\n\x08database\x18\x01 \x01(\tB\x03\xe0A\x02\x12=\n\x07options\x18\x02 \x01(\x0b2,.google.firestore.v1beta1.TransactionOptions"/\n\x18BeginTransactionResponse\x12\x13\n\x0btransaction\x18\x01 \x01(\x0c"l\n\rCommitRequest\x12\x15\n\x08database\x18\x01 \x01(\tB\x03\xe0A\x02\x12/\n\x06writes\x18\x02 \x03(\x0b2\x1f.google.firestore.v1beta1.Write\x12\x13\n\x0btransaction\x18\x03 \x01(\x0c"\x7f\n\x0eCommitResponse\x12<\n\rwrite_results\x18\x01 \x03(\x0b2%.google.firestore.v1beta1.WriteResult\x12/\n\x0bcommit_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"B\n\x0fRollbackRequest\x12\x15\n\x08database\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0btransaction\x18\x02 \x01(\x0cB\x03\xe0A\x02"\xa4\x02\n\x0fRunQueryRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12E\n\x10structured_query\x18\x02 \x01(\x0b2).google.firestore.v1beta1.StructuredQueryH\x00\x12\x15\n\x0btransaction\x18\x05 \x01(\x0cH\x01\x12G\n\x0fnew_transaction\x18\x06 \x01(\x0b2,.google.firestore.v1beta1.TransactionOptionsH\x01\x12/\n\tread_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampH\x01B\x0c\n\nquery_typeB\x16\n\x14consistency_selector"\xa5\x01\n\x10RunQueryResponse\x12\x13\n\x0btransaction\x18\x02 \x01(\x0c\x124\n\x08document\x18\x01 \x01(\x0b2".google.firestore.v1beta1.Document\x12-\n\tread_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x17\n\x0fskipped_results\x18\x04 \x01(\x05"\xc1\x01\n\x15PartitionQueryRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12E\n\x10structured_query\x18\x02 \x01(\x0b2).google.firestore.v1beta1.StructuredQueryH\x00\x12\x17\n\x0fpartition_count\x18\x03 \x01(\x03\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x11\n\tpage_size\x18\x05 \x01(\x05B\x0c\n\nquery_type"g\n\x16PartitionQueryResponse\x124\n\npartitions\x18\x01 \x03(\x0b2 .google.firestore.v1beta1.Cursor\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xf2\x01\n\x0cWriteRequest\x12\x15\n\x08database\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\tstream_id\x18\x02 \x01(\t\x12/\n\x06writes\x18\x03 \x03(\x0b2\x1f.google.firestore.v1beta1.Write\x12\x14\n\x0cstream_token\x18\x04 \x01(\x0c\x12B\n\x06labels\x18\x05 \x03(\x0b22.google.firestore.v1beta1.WriteRequest.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xa7\x01\n\rWriteResponse\x12\x11\n\tstream_id\x18\x01 \x01(\t\x12\x14\n\x0cstream_token\x18\x02 \x01(\x0c\x12<\n\rwrite_results\x18\x03 \x03(\x0b2%.google.firestore.v1beta1.WriteResult\x12/\n\x0bcommit_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xfc\x01\n\rListenRequest\x12\x15\n\x08database\x18\x01 \x01(\tB\x03\xe0A\x02\x126\n\nadd_target\x18\x02 \x01(\x0b2 .google.firestore.v1beta1.TargetH\x00\x12\x17\n\rremove_target\x18\x03 \x01(\x05H\x00\x12C\n\x06labels\x18\x04 \x03(\x0b23.google.firestore.v1beta1.ListenRequest.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x0f\n\rtarget_change"\xee\x02\n\x0eListenResponse\x12?\n\rtarget_change\x18\x02 \x01(\x0b2&.google.firestore.v1beta1.TargetChangeH\x00\x12C\n\x0fdocument_change\x18\x03 \x01(\x0b2(.google.firestore.v1beta1.DocumentChangeH\x00\x12C\n\x0fdocument_delete\x18\x04 \x01(\x0b2(.google.firestore.v1beta1.DocumentDeleteH\x00\x12C\n\x0fdocument_remove\x18\x06 \x01(\x0b2(.google.firestore.v1beta1.DocumentRemoveH\x00\x12;\n\x06filter\x18\x05 \x01(\x0b2).google.firestore.v1beta1.ExistenceFilterH\x00B\x0f\n\rresponse_type"\xb0\x03\n\x06Target\x12=\n\x05query\x18\x02 \x01(\x0b2,.google.firestore.v1beta1.Target.QueryTargetH\x00\x12E\n\tdocuments\x18\x03 \x01(\x0b20.google.firestore.v1beta1.Target.DocumentsTargetH\x00\x12\x16\n\x0cresume_token\x18\x04 \x01(\x0cH\x01\x12/\n\tread_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampH\x01\x12\x11\n\ttarget_id\x18\x05 \x01(\x05\x12\x0c\n\x04once\x18\x06 \x01(\x08\x1a$\n\x0fDocumentsTarget\x12\x11\n\tdocuments\x18\x02 \x03(\t\x1ar\n\x0bQueryTarget\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12E\n\x10structured_query\x18\x02 \x01(\x0b2).google.firestore.v1beta1.StructuredQueryH\x00B\x0c\n\nquery_typeB\r\n\x0btarget_typeB\r\n\x0bresume_type"\xaf\x02\n\x0cTargetChange\x12S\n\x12target_change_type\x18\x01 \x01(\x0e27.google.firestore.v1beta1.TargetChange.TargetChangeType\x12\x12\n\ntarget_ids\x18\x02 \x03(\x05\x12!\n\x05cause\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12\x14\n\x0cresume_token\x18\x04 \x01(\x0c\x12-\n\tread_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp"N\n\x10TargetChangeType\x12\r\n\tNO_CHANGE\x10\x00\x12\x07\n\x03ADD\x10\x01\x12\n\n\x06REMOVE\x10\x02\x12\x0b\n\x07CURRENT\x10\x03\x12\t\n\x05RESET\x10\x04"V\n\x18ListCollectionIdsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"L\n\x19ListCollectionIdsResponse\x12\x16\n\x0ecollection_ids\x18\x01 \x03(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xd3\x01\n\x11BatchWriteRequest\x12\x15\n\x08database\x18\x01 \x01(\tB\x03\xe0A\x02\x12/\n\x06writes\x18\x02 \x03(\x0b2\x1f.google.firestore.v1beta1.Write\x12G\n\x06labels\x18\x03 \x03(\x0b27.google.firestore.v1beta1.BatchWriteRequest.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"v\n\x12BatchWriteResponse\x12<\n\rwrite_results\x18\x01 \x03(\x0b2%.google.firestore.v1beta1.WriteResult\x12"\n\x06status\x18\x02 \x03(\x0b2\x12.google.rpc.Status2\xe4\x18\n\tFirestore\x12\x9e\x01\n\x0bGetDocument\x12,.google.firestore.v1beta1.GetDocumentRequest\x1a".google.firestore.v1beta1.Document"=\x82\xd3\xe4\x93\x027\x125/v1beta1/{name=projects/*/databases/*/documents/*/**}\x12\xc1\x01\n\rListDocuments\x12..google.firestore.v1beta1.ListDocumentsRequest\x1a/.google.firestore.v1beta1.ListDocumentsResponse"O\x82\xd3\xe4\x93\x02I\x12G/v1beta1/{parent=projects/*/databases/*/documents/*/**}/{collection_id}\x12\xce\x01\n\x0eUpdateDocument\x12/.google.firestore.v1beta1.UpdateDocumentRequest\x1a".google.firestore.v1beta1.Document"g\xdaA\x14document,update_mask\x82\xd3\xe4\x93\x02J2>/v1beta1/{document.name=projects/*/databases/*/documents/*/**}:\x08document\x12\x9f\x01\n\x0eDeleteDocument\x12/.google.firestore.v1beta1.DeleteDocumentRequest\x1a\x16.google.protobuf.Empty"D\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v1beta1/{name=projects/*/databases/*/documents/*/**}\x12\xc8\x01\n\x11BatchGetDocuments\x122.google.firestore.v1beta1.BatchGetDocumentsRequest\x1a3.google.firestore.v1beta1.BatchGetDocumentsResponse"H\x82\xd3\xe4\x93\x02B"=/v1beta1/{database=projects/*/databases/*}/documents:batchGet:\x01*0\x01\x12\xd6\x01\n\x10BeginTransaction\x121.google.firestore.v1beta1.BeginTransactionRequest\x1a2.google.firestore.v1beta1.BeginTransactionResponse"[\xdaA\x08database\x82\xd3\xe4\x93\x02J"E/v1beta1/{database=projects/*/databases/*}/documents:beginTransaction:\x01*\x12\xb5\x01\n\x06Commit\x12\'.google.firestore.v1beta1.CommitRequest\x1a(.google.firestore.v1beta1.CommitResponse"X\xdaA\x0fdatabase,writes\x82\xd3\xe4\x93\x02@";/v1beta1/{database=projects/*/databases/*}/documents:commit:\x01*\x12\xae\x01\n\x08Rollback\x12).google.firestore.v1beta1.RollbackRequest\x1a\x16.google.protobuf.Empty"_\xdaA\x14database,transaction\x82\xd3\xe4\x93\x02B"=/v1beta1/{database=projects/*/databases/*}/documents:rollback:\x01*\x12\xf4\x01\n\x08RunQuery\x12).google.firestore.v1beta1.RunQueryRequest\x1a*.google.firestore.v1beta1.RunQueryResponse"\x8e\x01\x82\xd3\xe4\x93\x02\x87\x01";/v1beta1/{parent=projects/*/databases/*/documents}:runQuery:\x01*ZE"@/v1beta1/{parent=projects/*/databases/*/documents/*/**}:runQuery:\x01*0\x01\x12\x90\x02\n\x0ePartitionQuery\x12/.google.firestore.v1beta1.PartitionQueryRequest\x1a0.google.firestore.v1beta1.PartitionQueryResponse"\x9a\x01\x82\xd3\xe4\x93\x02\x93\x01"A/v1beta1/{parent=projects/*/databases/*/documents}:partitionQuery:\x01*ZK"F/v1beta1/{parent=projects/*/databases/*/documents/*/**}:partitionQuery:\x01*\x12\xa3\x01\n\x05Write\x12&.google.firestore.v1beta1.WriteRequest\x1a\'.google.firestore.v1beta1.WriteResponse"E\x82\xd3\xe4\x93\x02?":/v1beta1/{database=projects/*/databases/*}/documents:write:\x01*(\x010\x01\x12\xa7\x01\n\x06Listen\x12\'.google.firestore.v1beta1.ListenRequest\x1a(.google.firestore.v1beta1.ListenResponse"F\x82\xd3\xe4\x93\x02@";/v1beta1/{database=projects/*/databases/*}/documents:listen:\x01*(\x010\x01\x12\xa8\x02\n\x11ListCollectionIds\x122.google.firestore.v1beta1.ListCollectionIdsRequest\x1a3.google.firestore.v1beta1.ListCollectionIdsResponse"\xa9\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\x99\x01"D/v1beta1/{parent=projects/*/databases/*/documents}:listCollectionIds:\x01*ZN"I/v1beta1/{parent=projects/*/databases/*/documents/*/**}:listCollectionIds:\x01*\x12\xb3\x01\n\nBatchWrite\x12+.google.firestore.v1beta1.BatchWriteRequest\x1a,.google.firestore.v1beta1.BatchWriteResponse"J\x82\xd3\xe4\x93\x02D"?/v1beta1/{database=projects/*/databases/*}/documents:batchWrite:\x01*\x12\xbe\x01\n\x0eCreateDocument\x12/.google.firestore.v1beta1.CreateDocumentRequest\x1a".google.firestore.v1beta1.Document"W\x82\xd3\xe4\x93\x02Q"E/v1beta1/{parent=projects/*/databases/*/documents/**}/{collection_id}:\x08document\x1av\xcaA\x18firestore.googleapis.com\xd2AXhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/datastoreB\xdf\x01\n\x1ccom.google.firestore.v1beta1B\x0eFirestoreProtoP\x01Z@cloud.google.com/go/firestore/apiv1beta1/firestorepb;firestorepb\xa2\x02\x04GCFS\xaa\x02\x1eGoogle.Cloud.Firestore.V1Beta1\xca\x02\x1eGoogle\\Cloud\\Firestore\\V1beta1\xea\x02!Google::Cloud::Firestore::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.v1beta1.firestore_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.firestore.v1beta1B\x0eFirestoreProtoP\x01Z@cloud.google.com/go/firestore/apiv1beta1/firestorepb;firestorepb\xa2\x02\x04GCFS\xaa\x02\x1eGoogle.Cloud.Firestore.V1Beta1\xca\x02\x1eGoogle\\Cloud\\Firestore\\V1beta1\xea\x02!Google::Cloud::Firestore::V1beta1'
    _globals['_GETDOCUMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDOCUMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['collection_id']._loaded_options = None
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['collection_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDOCUMENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDOCUMENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDOCUMENTREQUEST'].fields_by_name['collection_id']._loaded_options = None
    _globals['_CREATEDOCUMENTREQUEST'].fields_by_name['collection_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDOCUMENTREQUEST'].fields_by_name['document']._loaded_options = None
    _globals['_CREATEDOCUMENTREQUEST'].fields_by_name['document']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDOCUMENTREQUEST'].fields_by_name['document']._loaded_options = None
    _globals['_UPDATEDOCUMENTREQUEST'].fields_by_name['document']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEDOCUMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDOCUMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHGETDOCUMENTSREQUEST'].fields_by_name['database']._loaded_options = None
    _globals['_BATCHGETDOCUMENTSREQUEST'].fields_by_name['database']._serialized_options = b'\xe0A\x02'
    _globals['_BEGINTRANSACTIONREQUEST'].fields_by_name['database']._loaded_options = None
    _globals['_BEGINTRANSACTIONREQUEST'].fields_by_name['database']._serialized_options = b'\xe0A\x02'
    _globals['_COMMITREQUEST'].fields_by_name['database']._loaded_options = None
    _globals['_COMMITREQUEST'].fields_by_name['database']._serialized_options = b'\xe0A\x02'
    _globals['_ROLLBACKREQUEST'].fields_by_name['database']._loaded_options = None
    _globals['_ROLLBACKREQUEST'].fields_by_name['database']._serialized_options = b'\xe0A\x02'
    _globals['_ROLLBACKREQUEST'].fields_by_name['transaction']._loaded_options = None
    _globals['_ROLLBACKREQUEST'].fields_by_name['transaction']._serialized_options = b'\xe0A\x02'
    _globals['_RUNQUERYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_RUNQUERYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_PARTITIONQUERYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_PARTITIONQUERYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_WRITEREQUEST_LABELSENTRY']._loaded_options = None
    _globals['_WRITEREQUEST_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_WRITEREQUEST'].fields_by_name['database']._loaded_options = None
    _globals['_WRITEREQUEST'].fields_by_name['database']._serialized_options = b'\xe0A\x02'
    _globals['_LISTENREQUEST_LABELSENTRY']._loaded_options = None
    _globals['_LISTENREQUEST_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_LISTENREQUEST'].fields_by_name['database']._loaded_options = None
    _globals['_LISTENREQUEST'].fields_by_name['database']._serialized_options = b'\xe0A\x02'
    _globals['_LISTCOLLECTIONIDSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCOLLECTIONIDSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHWRITEREQUEST_LABELSENTRY']._loaded_options = None
    _globals['_BATCHWRITEREQUEST_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_BATCHWRITEREQUEST'].fields_by_name['database']._loaded_options = None
    _globals['_BATCHWRITEREQUEST'].fields_by_name['database']._serialized_options = b'\xe0A\x02'
    _globals['_FIRESTORE']._loaded_options = None
    _globals['_FIRESTORE']._serialized_options = b'\xcaA\x18firestore.googleapis.com\xd2AXhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/datastore'
    _globals['_FIRESTORE'].methods_by_name['GetDocument']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['GetDocument']._serialized_options = b'\x82\xd3\xe4\x93\x027\x125/v1beta1/{name=projects/*/databases/*/documents/*/**}'
    _globals['_FIRESTORE'].methods_by_name['ListDocuments']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['ListDocuments']._serialized_options = b'\x82\xd3\xe4\x93\x02I\x12G/v1beta1/{parent=projects/*/databases/*/documents/*/**}/{collection_id}'
    _globals['_FIRESTORE'].methods_by_name['UpdateDocument']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['UpdateDocument']._serialized_options = b'\xdaA\x14document,update_mask\x82\xd3\xe4\x93\x02J2>/v1beta1/{document.name=projects/*/databases/*/documents/*/**}:\x08document'
    _globals['_FIRESTORE'].methods_by_name['DeleteDocument']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['DeleteDocument']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v1beta1/{name=projects/*/databases/*/documents/*/**}'
    _globals['_FIRESTORE'].methods_by_name['BatchGetDocuments']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['BatchGetDocuments']._serialized_options = b'\x82\xd3\xe4\x93\x02B"=/v1beta1/{database=projects/*/databases/*}/documents:batchGet:\x01*'
    _globals['_FIRESTORE'].methods_by_name['BeginTransaction']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['BeginTransaction']._serialized_options = b'\xdaA\x08database\x82\xd3\xe4\x93\x02J"E/v1beta1/{database=projects/*/databases/*}/documents:beginTransaction:\x01*'
    _globals['_FIRESTORE'].methods_by_name['Commit']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['Commit']._serialized_options = b'\xdaA\x0fdatabase,writes\x82\xd3\xe4\x93\x02@";/v1beta1/{database=projects/*/databases/*}/documents:commit:\x01*'
    _globals['_FIRESTORE'].methods_by_name['Rollback']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['Rollback']._serialized_options = b'\xdaA\x14database,transaction\x82\xd3\xe4\x93\x02B"=/v1beta1/{database=projects/*/databases/*}/documents:rollback:\x01*'
    _globals['_FIRESTORE'].methods_by_name['RunQuery']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['RunQuery']._serialized_options = b'\x82\xd3\xe4\x93\x02\x87\x01";/v1beta1/{parent=projects/*/databases/*/documents}:runQuery:\x01*ZE"@/v1beta1/{parent=projects/*/databases/*/documents/*/**}:runQuery:\x01*'
    _globals['_FIRESTORE'].methods_by_name['PartitionQuery']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['PartitionQuery']._serialized_options = b'\x82\xd3\xe4\x93\x02\x93\x01"A/v1beta1/{parent=projects/*/databases/*/documents}:partitionQuery:\x01*ZK"F/v1beta1/{parent=projects/*/databases/*/documents/*/**}:partitionQuery:\x01*'
    _globals['_FIRESTORE'].methods_by_name['Write']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['Write']._serialized_options = b'\x82\xd3\xe4\x93\x02?":/v1beta1/{database=projects/*/databases/*}/documents:write:\x01*'
    _globals['_FIRESTORE'].methods_by_name['Listen']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['Listen']._serialized_options = b'\x82\xd3\xe4\x93\x02@";/v1beta1/{database=projects/*/databases/*}/documents:listen:\x01*'
    _globals['_FIRESTORE'].methods_by_name['ListCollectionIds']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['ListCollectionIds']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x99\x01"D/v1beta1/{parent=projects/*/databases/*/documents}:listCollectionIds:\x01*ZN"I/v1beta1/{parent=projects/*/databases/*/documents/*/**}:listCollectionIds:\x01*'
    _globals['_FIRESTORE'].methods_by_name['BatchWrite']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['BatchWrite']._serialized_options = b'\x82\xd3\xe4\x93\x02D"?/v1beta1/{database=projects/*/databases/*}/documents:batchWrite:\x01*'
    _globals['_FIRESTORE'].methods_by_name['CreateDocument']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['CreateDocument']._serialized_options = b'\x82\xd3\xe4\x93\x02Q"E/v1beta1/{parent=projects/*/databases/*/documents/**}/{collection_id}:\x08document'
    _globals['_GETDOCUMENTREQUEST']._serialized_start = 402
    _globals['_GETDOCUMENTREQUEST']._serialized_end = 591
    _globals['_LISTDOCUMENTSREQUEST']._serialized_start = 594
    _globals['_LISTDOCUMENTSREQUEST']._serialized_end = 894
    _globals['_LISTDOCUMENTSRESPONSE']._serialized_start = 896
    _globals['_LISTDOCUMENTSRESPONSE']._serialized_end = 999
    _globals['_CREATEDOCUMENTREQUEST']._serialized_start = 1002
    _globals['_CREATEDOCUMENTREQUEST']._serialized_end = 1208
    _globals['_UPDATEDOCUMENTREQUEST']._serialized_start = 1211
    _globals['_UPDATEDOCUMENTREQUEST']._serialized_end = 1474
    _globals['_DELETEDOCUMENTREQUEST']._serialized_start = 1476
    _globals['_DELETEDOCUMENTREQUEST']._serialized_end = 1584
    _globals['_BATCHGETDOCUMENTSREQUEST']._serialized_start = 1587
    _globals['_BATCHGETDOCUMENTSREQUEST']._serialized_end = 1878
    _globals['_BATCHGETDOCUMENTSRESPONSE']._serialized_start = 1881
    _globals['_BATCHGETDOCUMENTSRESPONSE']._serialized_end = 2058
    _globals['_BEGINTRANSACTIONREQUEST']._serialized_start = 2060
    _globals['_BEGINTRANSACTIONREQUEST']._serialized_end = 2171
    _globals['_BEGINTRANSACTIONRESPONSE']._serialized_start = 2173
    _globals['_BEGINTRANSACTIONRESPONSE']._serialized_end = 2220
    _globals['_COMMITREQUEST']._serialized_start = 2222
    _globals['_COMMITREQUEST']._serialized_end = 2330
    _globals['_COMMITRESPONSE']._serialized_start = 2332
    _globals['_COMMITRESPONSE']._serialized_end = 2459
    _globals['_ROLLBACKREQUEST']._serialized_start = 2461
    _globals['_ROLLBACKREQUEST']._serialized_end = 2527
    _globals['_RUNQUERYREQUEST']._serialized_start = 2530
    _globals['_RUNQUERYREQUEST']._serialized_end = 2822
    _globals['_RUNQUERYRESPONSE']._serialized_start = 2825
    _globals['_RUNQUERYRESPONSE']._serialized_end = 2990
    _globals['_PARTITIONQUERYREQUEST']._serialized_start = 2993
    _globals['_PARTITIONQUERYREQUEST']._serialized_end = 3186
    _globals['_PARTITIONQUERYRESPONSE']._serialized_start = 3188
    _globals['_PARTITIONQUERYRESPONSE']._serialized_end = 3291
    _globals['_WRITEREQUEST']._serialized_start = 3294
    _globals['_WRITEREQUEST']._serialized_end = 3536
    _globals['_WRITEREQUEST_LABELSENTRY']._serialized_start = 3491
    _globals['_WRITEREQUEST_LABELSENTRY']._serialized_end = 3536
    _globals['_WRITERESPONSE']._serialized_start = 3539
    _globals['_WRITERESPONSE']._serialized_end = 3706
    _globals['_LISTENREQUEST']._serialized_start = 3709
    _globals['_LISTENREQUEST']._serialized_end = 3961
    _globals['_LISTENREQUEST_LABELSENTRY']._serialized_start = 3491
    _globals['_LISTENREQUEST_LABELSENTRY']._serialized_end = 3536
    _globals['_LISTENRESPONSE']._serialized_start = 3964
    _globals['_LISTENRESPONSE']._serialized_end = 4330
    _globals['_TARGET']._serialized_start = 4333
    _globals['_TARGET']._serialized_end = 4765
    _globals['_TARGET_DOCUMENTSTARGET']._serialized_start = 4583
    _globals['_TARGET_DOCUMENTSTARGET']._serialized_end = 4619
    _globals['_TARGET_QUERYTARGET']._serialized_start = 4621
    _globals['_TARGET_QUERYTARGET']._serialized_end = 4735
    _globals['_TARGETCHANGE']._serialized_start = 4768
    _globals['_TARGETCHANGE']._serialized_end = 5071
    _globals['_TARGETCHANGE_TARGETCHANGETYPE']._serialized_start = 4993
    _globals['_TARGETCHANGE_TARGETCHANGETYPE']._serialized_end = 5071
    _globals['_LISTCOLLECTIONIDSREQUEST']._serialized_start = 5073
    _globals['_LISTCOLLECTIONIDSREQUEST']._serialized_end = 5159
    _globals['_LISTCOLLECTIONIDSRESPONSE']._serialized_start = 5161
    _globals['_LISTCOLLECTIONIDSRESPONSE']._serialized_end = 5237
    _globals['_BATCHWRITEREQUEST']._serialized_start = 5240
    _globals['_BATCHWRITEREQUEST']._serialized_end = 5451
    _globals['_BATCHWRITEREQUEST_LABELSENTRY']._serialized_start = 3491
    _globals['_BATCHWRITEREQUEST_LABELSENTRY']._serialized_end = 3536
    _globals['_BATCHWRITERESPONSE']._serialized_start = 5453
    _globals['_BATCHWRITERESPONSE']._serialized_end = 5571
    _globals['_FIRESTORE']._serialized_start = 5574
    _globals['_FIRESTORE']._serialized_end = 8746