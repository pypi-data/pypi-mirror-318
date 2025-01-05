"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/v1/firestore.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.firestore.v1 import aggregation_result_pb2 as google_dot_firestore_dot_v1_dot_aggregation__result__pb2
from ....google.firestore.v1 import common_pb2 as google_dot_firestore_dot_v1_dot_common__pb2
from ....google.firestore.v1 import document_pb2 as google_dot_firestore_dot_v1_dot_document__pb2
from ....google.firestore.v1 import query_pb2 as google_dot_firestore_dot_v1_dot_query__pb2
from ....google.firestore.v1 import query_profile_pb2 as google_dot_firestore_dot_v1_dot_query__profile__pb2
from ....google.firestore.v1 import write_pb2 as google_dot_firestore_dot_v1_dot_write__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from ....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/firestore/v1/firestore.proto\x12\x13google.firestore.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a,google/firestore/v1/aggregation_result.proto\x1a google/firestore/v1/common.proto\x1a"google/firestore/v1/document.proto\x1a\x1fgoogle/firestore/v1/query.proto\x1a\'google/firestore/v1/query_profile.proto\x1a\x1fgoogle/firestore/v1/write.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto"\xb8\x01\n\x12GetDocumentRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12/\n\x04mask\x18\x02 \x01(\x0b2!.google.firestore.v1.DocumentMask\x12\x15\n\x0btransaction\x18\x03 \x01(\x0cH\x00\x12/\n\tread_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00B\x16\n\x14consistency_selector"\xbb\x02\n\x14ListDocumentsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rcollection_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x06 \x01(\tB\x03\xe0A\x01\x124\n\x04mask\x18\x07 \x01(\x0b2!.google.firestore.v1.DocumentMaskB\x03\xe0A\x01\x12\x15\n\x0btransaction\x18\x08 \x01(\x0cH\x00\x12/\n\tread_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x12\x14\n\x0cshow_missing\x18\x0c \x01(\x08B\x16\n\x14consistency_selector"b\n\x15ListDocumentsResponse\x120\n\tdocuments\x18\x01 \x03(\x0b2\x1d.google.firestore.v1.Document\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xc4\x01\n\x15CreateDocumentRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rcollection_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdocument_id\x18\x03 \x01(\t\x124\n\x08document\x18\x04 \x01(\x0b2\x1d.google.firestore.v1.DocumentB\x03\xe0A\x02\x12/\n\x04mask\x18\x05 \x01(\x0b2!.google.firestore.v1.DocumentMask"\xf3\x01\n\x15UpdateDocumentRequest\x124\n\x08document\x18\x01 \x01(\x0b2\x1d.google.firestore.v1.DocumentB\x03\xe0A\x02\x126\n\x0bupdate_mask\x18\x02 \x01(\x0b2!.google.firestore.v1.DocumentMask\x12/\n\x04mask\x18\x03 \x01(\x0b2!.google.firestore.v1.DocumentMask\x12;\n\x10current_document\x18\x04 \x01(\x0b2!.google.firestore.v1.Precondition"g\n\x15DeleteDocumentRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12;\n\x10current_document\x18\x02 \x01(\x0b2!.google.firestore.v1.Precondition"\x99\x02\n\x18BatchGetDocumentsRequest\x12\x15\n\x08database\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\tdocuments\x18\x02 \x03(\t\x12/\n\x04mask\x18\x03 \x01(\x0b2!.google.firestore.v1.DocumentMask\x12\x15\n\x0btransaction\x18\x04 \x01(\x0cH\x00\x12B\n\x0fnew_transaction\x18\x05 \x01(\x0b2\'.google.firestore.v1.TransactionOptionsH\x00\x12/\n\tread_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00B\x16\n\x14consistency_selector"\xac\x01\n\x19BatchGetDocumentsResponse\x12.\n\x05found\x18\x01 \x01(\x0b2\x1d.google.firestore.v1.DocumentH\x00\x12\x11\n\x07missing\x18\x02 \x01(\tH\x00\x12\x13\n\x0btransaction\x18\x03 \x01(\x0c\x12-\n\tread_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\n\x06result"j\n\x17BeginTransactionRequest\x12\x15\n\x08database\x18\x01 \x01(\tB\x03\xe0A\x02\x128\n\x07options\x18\x02 \x01(\x0b2\'.google.firestore.v1.TransactionOptions"/\n\x18BeginTransactionResponse\x12\x13\n\x0btransaction\x18\x01 \x01(\x0c"g\n\rCommitRequest\x12\x15\n\x08database\x18\x01 \x01(\tB\x03\xe0A\x02\x12*\n\x06writes\x18\x02 \x03(\x0b2\x1a.google.firestore.v1.Write\x12\x13\n\x0btransaction\x18\x03 \x01(\x0c"z\n\x0eCommitResponse\x127\n\rwrite_results\x18\x01 \x03(\x0b2 .google.firestore.v1.WriteResult\x12/\n\x0bcommit_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"B\n\x0fRollbackRequest\x12\x15\n\x08database\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0btransaction\x18\x02 \x01(\x0cB\x03\xe0A\x02"\xdd\x02\n\x0fRunQueryRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12@\n\x10structured_query\x18\x02 \x01(\x0b2$.google.firestore.v1.StructuredQueryH\x00\x12\x15\n\x0btransaction\x18\x05 \x01(\x0cH\x01\x12B\n\x0fnew_transaction\x18\x06 \x01(\x0b2\'.google.firestore.v1.TransactionOptionsH\x01\x12/\n\tread_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampH\x01\x12A\n\x0fexplain_options\x18\n \x01(\x0b2#.google.firestore.v1.ExplainOptionsB\x03\xe0A\x01B\x0c\n\nquery_typeB\x16\n\x14consistency_selector"\x87\x02\n\x10RunQueryResponse\x12\x13\n\x0btransaction\x18\x02 \x01(\x0c\x12/\n\x08document\x18\x01 \x01(\x0b2\x1d.google.firestore.v1.Document\x12-\n\tread_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x17\n\x0fskipped_results\x18\x04 \x01(\x05\x12\x0e\n\x04done\x18\x06 \x01(\x08H\x00\x12<\n\x0fexplain_metrics\x18\x0b \x01(\x0b2#.google.firestore.v1.ExplainMetricsB\x17\n\x15continuation_selector"\xff\x02\n\x1aRunAggregationQueryRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12W\n\x1cstructured_aggregation_query\x18\x02 \x01(\x0b2/.google.firestore.v1.StructuredAggregationQueryH\x00\x12\x15\n\x0btransaction\x18\x04 \x01(\x0cH\x01\x12B\n\x0fnew_transaction\x18\x05 \x01(\x0b2\'.google.firestore.v1.TransactionOptionsH\x01\x12/\n\tread_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampH\x01\x12A\n\x0fexplain_options\x18\x08 \x01(\x0b2#.google.firestore.v1.ExplainOptionsB\x03\xe0A\x01B\x0c\n\nquery_typeB\x16\n\x14consistency_selector"\xd7\x01\n\x1bRunAggregationQueryResponse\x126\n\x06result\x18\x01 \x01(\x0b2&.google.firestore.v1.AggregationResult\x12\x13\n\x0btransaction\x18\x02 \x01(\x0c\x12-\n\tread_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12<\n\x0fexplain_metrics\x18\n \x01(\x0b2#.google.firestore.v1.ExplainMetrics"\x85\x02\n\x15PartitionQueryRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12@\n\x10structured_query\x18\x02 \x01(\x0b2$.google.firestore.v1.StructuredQueryH\x00\x12\x17\n\x0fpartition_count\x18\x03 \x01(\x03\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12/\n\tread_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampH\x01B\x0c\n\nquery_typeB\x16\n\x14consistency_selector"b\n\x16PartitionQueryResponse\x12/\n\npartitions\x18\x01 \x03(\x0b2\x1b.google.firestore.v1.Cursor\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xe8\x01\n\x0cWriteRequest\x12\x15\n\x08database\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\tstream_id\x18\x02 \x01(\t\x12*\n\x06writes\x18\x03 \x03(\x0b2\x1a.google.firestore.v1.Write\x12\x14\n\x0cstream_token\x18\x04 \x01(\x0c\x12=\n\x06labels\x18\x05 \x03(\x0b2-.google.firestore.v1.WriteRequest.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xa2\x01\n\rWriteResponse\x12\x11\n\tstream_id\x18\x01 \x01(\t\x12\x14\n\x0cstream_token\x18\x02 \x01(\x0c\x127\n\rwrite_results\x18\x03 \x03(\x0b2 .google.firestore.v1.WriteResult\x12/\n\x0bcommit_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xf2\x01\n\rListenRequest\x12\x15\n\x08database\x18\x01 \x01(\tB\x03\xe0A\x02\x121\n\nadd_target\x18\x02 \x01(\x0b2\x1b.google.firestore.v1.TargetH\x00\x12\x17\n\rremove_target\x18\x03 \x01(\x05H\x00\x12>\n\x06labels\x18\x04 \x03(\x0b2..google.firestore.v1.ListenRequest.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x0f\n\rtarget_change"\xd5\x02\n\x0eListenResponse\x12:\n\rtarget_change\x18\x02 \x01(\x0b2!.google.firestore.v1.TargetChangeH\x00\x12>\n\x0fdocument_change\x18\x03 \x01(\x0b2#.google.firestore.v1.DocumentChangeH\x00\x12>\n\x0fdocument_delete\x18\x04 \x01(\x0b2#.google.firestore.v1.DocumentDeleteH\x00\x12>\n\x0fdocument_remove\x18\x06 \x01(\x0b2#.google.firestore.v1.DocumentRemoveH\x00\x126\n\x06filter\x18\x05 \x01(\x0b2$.google.firestore.v1.ExistenceFilterH\x00B\x0f\n\rresponse_type"\xd6\x03\n\x06Target\x128\n\x05query\x18\x02 \x01(\x0b2\'.google.firestore.v1.Target.QueryTargetH\x00\x12@\n\tdocuments\x18\x03 \x01(\x0b2+.google.firestore.v1.Target.DocumentsTargetH\x00\x12\x16\n\x0cresume_token\x18\x04 \x01(\x0cH\x01\x12/\n\tread_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampH\x01\x12\x11\n\ttarget_id\x18\x05 \x01(\x05\x12\x0c\n\x04once\x18\x06 \x01(\x08\x123\n\x0eexpected_count\x18\x0c \x01(\x0b2\x1b.google.protobuf.Int32Value\x1a$\n\x0fDocumentsTarget\x12\x11\n\tdocuments\x18\x02 \x03(\t\x1am\n\x0bQueryTarget\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12@\n\x10structured_query\x18\x02 \x01(\x0b2$.google.firestore.v1.StructuredQueryH\x00B\x0c\n\nquery_typeB\r\n\x0btarget_typeB\r\n\x0bresume_type"\xaa\x02\n\x0cTargetChange\x12N\n\x12target_change_type\x18\x01 \x01(\x0e22.google.firestore.v1.TargetChange.TargetChangeType\x12\x12\n\ntarget_ids\x18\x02 \x03(\x05\x12!\n\x05cause\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12\x14\n\x0cresume_token\x18\x04 \x01(\x0c\x12-\n\tread_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp"N\n\x10TargetChangeType\x12\r\n\tNO_CHANGE\x10\x00\x12\x07\n\x03ADD\x10\x01\x12\n\n\x06REMOVE\x10\x02\x12\x0b\n\x07CURRENT\x10\x03\x12\t\n\x05RESET\x10\x04"\x9f\x01\n\x18ListCollectionIdsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12/\n\tread_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00B\x16\n\x14consistency_selector"L\n\x19ListCollectionIdsResponse\x12\x16\n\x0ecollection_ids\x18\x01 \x03(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xc9\x01\n\x11BatchWriteRequest\x12\x15\n\x08database\x18\x01 \x01(\tB\x03\xe0A\x02\x12*\n\x06writes\x18\x02 \x03(\x0b2\x1a.google.firestore.v1.Write\x12B\n\x06labels\x18\x03 \x03(\x0b22.google.firestore.v1.BatchWriteRequest.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"q\n\x12BatchWriteResponse\x127\n\rwrite_results\x18\x01 \x03(\x0b2 .google.firestore.v1.WriteResult\x12"\n\x06status\x18\x02 \x03(\x0b2\x12.google.rpc.Status2\xda\x19\n\tFirestore\x12\x8f\x01\n\x0bGetDocument\x12\'.google.firestore.v1.GetDocumentRequest\x1a\x1d.google.firestore.v1.Document"8\x82\xd3\xe4\x93\x022\x120/v1/{name=projects/*/databases/*/documents/*/**}\x12\xf5\x01\n\rListDocuments\x12).google.firestore.v1.ListDocumentsRequest\x1a*.google.firestore.v1.ListDocumentsResponse"\x8c\x01\x82\xd3\xe4\x93\x02\x85\x01\x12B/v1/{parent=projects/*/databases/*/documents/*/**}/{collection_id}Z?\x12=/v1/{parent=projects/*/databases/*/documents}/{collection_id}\x12\xbf\x01\n\x0eUpdateDocument\x12*.google.firestore.v1.UpdateDocumentRequest\x1a\x1d.google.firestore.v1.Document"b\xdaA\x14document,update_mask\x82\xd3\xe4\x93\x02E29/v1/{document.name=projects/*/databases/*/documents/*/**}:\x08document\x12\x95\x01\n\x0eDeleteDocument\x12*.google.firestore.v1.DeleteDocumentRequest\x1a\x16.google.protobuf.Empty"?\xdaA\x04name\x82\xd3\xe4\x93\x022*0/v1/{name=projects/*/databases/*/documents/*/**}\x12\xb9\x01\n\x11BatchGetDocuments\x12-.google.firestore.v1.BatchGetDocumentsRequest\x1a..google.firestore.v1.BatchGetDocumentsResponse"C\x82\xd3\xe4\x93\x02="8/v1/{database=projects/*/databases/*}/documents:batchGet:\x01*0\x01\x12\xc7\x01\n\x10BeginTransaction\x12,.google.firestore.v1.BeginTransactionRequest\x1a-.google.firestore.v1.BeginTransactionResponse"V\xdaA\x08database\x82\xd3\xe4\x93\x02E"@/v1/{database=projects/*/databases/*}/documents:beginTransaction:\x01*\x12\xa6\x01\n\x06Commit\x12".google.firestore.v1.CommitRequest\x1a#.google.firestore.v1.CommitResponse"S\xdaA\x0fdatabase,writes\x82\xd3\xe4\x93\x02;"6/v1/{database=projects/*/databases/*}/documents:commit:\x01*\x12\xa4\x01\n\x08Rollback\x12$.google.firestore.v1.RollbackRequest\x1a\x16.google.protobuf.Empty"Z\xdaA\x14database,transaction\x82\xd3\xe4\x93\x02="8/v1/{database=projects/*/databases/*}/documents:rollback:\x01*\x12\xdf\x01\n\x08RunQuery\x12$.google.firestore.v1.RunQueryRequest\x1a%.google.firestore.v1.RunQueryResponse"\x83\x01\x82\xd3\xe4\x93\x02}"6/v1/{parent=projects/*/databases/*/documents}:runQuery:\x01*Z@";/v1/{parent=projects/*/databases/*/documents/*/**}:runQuery:\x01*0\x01\x12\x97\x02\n\x13RunAggregationQuery\x12/.google.firestore.v1.RunAggregationQueryRequest\x1a0.google.firestore.v1.RunAggregationQueryResponse"\x9a\x01\x82\xd3\xe4\x93\x02\x93\x01"A/v1/{parent=projects/*/databases/*/documents}:runAggregationQuery:\x01*ZK"F/v1/{parent=projects/*/databases/*/documents/*/**}:runAggregationQuery:\x01*0\x01\x12\xfc\x01\n\x0ePartitionQuery\x12*.google.firestore.v1.PartitionQueryRequest\x1a+.google.firestore.v1.PartitionQueryResponse"\x90\x01\x82\xd3\xe4\x93\x02\x89\x01"</v1/{parent=projects/*/databases/*/documents}:partitionQuery:\x01*ZF"A/v1/{parent=projects/*/databases/*/documents/*/**}:partitionQuery:\x01*\x12\x94\x01\n\x05Write\x12!.google.firestore.v1.WriteRequest\x1a".google.firestore.v1.WriteResponse"@\x82\xd3\xe4\x93\x02:"5/v1/{database=projects/*/databases/*}/documents:write:\x01*(\x010\x01\x12\x98\x01\n\x06Listen\x12".google.firestore.v1.ListenRequest\x1a#.google.firestore.v1.ListenResponse"A\x82\xd3\xe4\x93\x02;"6/v1/{database=projects/*/databases/*}/documents:listen:\x01*(\x010\x01\x12\x94\x02\n\x11ListCollectionIds\x12-.google.firestore.v1.ListCollectionIdsRequest\x1a..google.firestore.v1.ListCollectionIdsResponse"\x9f\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\x8f\x01"?/v1/{parent=projects/*/databases/*/documents}:listCollectionIds:\x01*ZI"D/v1/{parent=projects/*/databases/*/documents/*/**}:listCollectionIds:\x01*\x12\xa4\x01\n\nBatchWrite\x12&.google.firestore.v1.BatchWriteRequest\x1a\'.google.firestore.v1.BatchWriteResponse"E\x82\xd3\xe4\x93\x02?":/v1/{database=projects/*/databases/*}/documents:batchWrite:\x01*\x12\xaf\x01\n\x0eCreateDocument\x12*.google.firestore.v1.CreateDocumentRequest\x1a\x1d.google.firestore.v1.Document"R\x82\xd3\xe4\x93\x02L"@/v1/{parent=projects/*/databases/*/documents/**}/{collection_id}:\x08document\x1av\xcaA\x18firestore.googleapis.com\xd2AXhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/datastoreB\xbf\x01\n\x17com.google.firestore.v1B\x0eFirestoreProtoP\x01Z;cloud.google.com/go/firestore/apiv1/firestorepb;firestorepb\xaa\x02\x19Google.Cloud.Firestore.V1\xca\x02\x19Google\\Cloud\\Firestore\\V1\xea\x02\x1cGoogle::Cloud::Firestore::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.v1.firestore_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.firestore.v1B\x0eFirestoreProtoP\x01Z;cloud.google.com/go/firestore/apiv1/firestorepb;firestorepb\xaa\x02\x19Google.Cloud.Firestore.V1\xca\x02\x19Google\\Cloud\\Firestore\\V1\xea\x02\x1cGoogle::Cloud::Firestore::V1'
    _globals['_GETDOCUMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDOCUMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['collection_id']._loaded_options = None
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['collection_id']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['mask']._loaded_options = None
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['mask']._serialized_options = b'\xe0A\x01'
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
    _globals['_RUNQUERYREQUEST'].fields_by_name['explain_options']._loaded_options = None
    _globals['_RUNQUERYREQUEST'].fields_by_name['explain_options']._serialized_options = b'\xe0A\x01'
    _globals['_RUNAGGREGATIONQUERYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_RUNAGGREGATIONQUERYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_RUNAGGREGATIONQUERYREQUEST'].fields_by_name['explain_options']._loaded_options = None
    _globals['_RUNAGGREGATIONQUERYREQUEST'].fields_by_name['explain_options']._serialized_options = b'\xe0A\x01'
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
    _globals['_FIRESTORE'].methods_by_name['GetDocument']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/v1/{name=projects/*/databases/*/documents/*/**}'
    _globals['_FIRESTORE'].methods_by_name['ListDocuments']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['ListDocuments']._serialized_options = b'\x82\xd3\xe4\x93\x02\x85\x01\x12B/v1/{parent=projects/*/databases/*/documents/*/**}/{collection_id}Z?\x12=/v1/{parent=projects/*/databases/*/documents}/{collection_id}'
    _globals['_FIRESTORE'].methods_by_name['UpdateDocument']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['UpdateDocument']._serialized_options = b'\xdaA\x14document,update_mask\x82\xd3\xe4\x93\x02E29/v1/{document.name=projects/*/databases/*/documents/*/**}:\x08document'
    _globals['_FIRESTORE'].methods_by_name['DeleteDocument']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['DeleteDocument']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x022*0/v1/{name=projects/*/databases/*/documents/*/**}'
    _globals['_FIRESTORE'].methods_by_name['BatchGetDocuments']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['BatchGetDocuments']._serialized_options = b'\x82\xd3\xe4\x93\x02="8/v1/{database=projects/*/databases/*}/documents:batchGet:\x01*'
    _globals['_FIRESTORE'].methods_by_name['BeginTransaction']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['BeginTransaction']._serialized_options = b'\xdaA\x08database\x82\xd3\xe4\x93\x02E"@/v1/{database=projects/*/databases/*}/documents:beginTransaction:\x01*'
    _globals['_FIRESTORE'].methods_by_name['Commit']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['Commit']._serialized_options = b'\xdaA\x0fdatabase,writes\x82\xd3\xe4\x93\x02;"6/v1/{database=projects/*/databases/*}/documents:commit:\x01*'
    _globals['_FIRESTORE'].methods_by_name['Rollback']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['Rollback']._serialized_options = b'\xdaA\x14database,transaction\x82\xd3\xe4\x93\x02="8/v1/{database=projects/*/databases/*}/documents:rollback:\x01*'
    _globals['_FIRESTORE'].methods_by_name['RunQuery']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['RunQuery']._serialized_options = b'\x82\xd3\xe4\x93\x02}"6/v1/{parent=projects/*/databases/*/documents}:runQuery:\x01*Z@";/v1/{parent=projects/*/databases/*/documents/*/**}:runQuery:\x01*'
    _globals['_FIRESTORE'].methods_by_name['RunAggregationQuery']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['RunAggregationQuery']._serialized_options = b'\x82\xd3\xe4\x93\x02\x93\x01"A/v1/{parent=projects/*/databases/*/documents}:runAggregationQuery:\x01*ZK"F/v1/{parent=projects/*/databases/*/documents/*/**}:runAggregationQuery:\x01*'
    _globals['_FIRESTORE'].methods_by_name['PartitionQuery']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['PartitionQuery']._serialized_options = b'\x82\xd3\xe4\x93\x02\x89\x01"</v1/{parent=projects/*/databases/*/documents}:partitionQuery:\x01*ZF"A/v1/{parent=projects/*/databases/*/documents/*/**}:partitionQuery:\x01*'
    _globals['_FIRESTORE'].methods_by_name['Write']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['Write']._serialized_options = b'\x82\xd3\xe4\x93\x02:"5/v1/{database=projects/*/databases/*}/documents:write:\x01*'
    _globals['_FIRESTORE'].methods_by_name['Listen']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['Listen']._serialized_options = b'\x82\xd3\xe4\x93\x02;"6/v1/{database=projects/*/databases/*}/documents:listen:\x01*'
    _globals['_FIRESTORE'].methods_by_name['ListCollectionIds']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['ListCollectionIds']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x8f\x01"?/v1/{parent=projects/*/databases/*/documents}:listCollectionIds:\x01*ZI"D/v1/{parent=projects/*/databases/*/documents/*/**}:listCollectionIds:\x01*'
    _globals['_FIRESTORE'].methods_by_name['BatchWrite']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['BatchWrite']._serialized_options = b'\x82\xd3\xe4\x93\x02?":/v1/{database=projects/*/databases/*}/documents:batchWrite:\x01*'
    _globals['_FIRESTORE'].methods_by_name['CreateDocument']._loaded_options = None
    _globals['_FIRESTORE'].methods_by_name['CreateDocument']._serialized_options = b'\x82\xd3\xe4\x93\x02L"@/v1/{parent=projects/*/databases/*/documents/**}/{collection_id}:\x08document'
    _globals['_GETDOCUMENTREQUEST']._serialized_start = 491
    _globals['_GETDOCUMENTREQUEST']._serialized_end = 675
    _globals['_LISTDOCUMENTSREQUEST']._serialized_start = 678
    _globals['_LISTDOCUMENTSREQUEST']._serialized_end = 993
    _globals['_LISTDOCUMENTSRESPONSE']._serialized_start = 995
    _globals['_LISTDOCUMENTSRESPONSE']._serialized_end = 1093
    _globals['_CREATEDOCUMENTREQUEST']._serialized_start = 1096
    _globals['_CREATEDOCUMENTREQUEST']._serialized_end = 1292
    _globals['_UPDATEDOCUMENTREQUEST']._serialized_start = 1295
    _globals['_UPDATEDOCUMENTREQUEST']._serialized_end = 1538
    _globals['_DELETEDOCUMENTREQUEST']._serialized_start = 1540
    _globals['_DELETEDOCUMENTREQUEST']._serialized_end = 1643
    _globals['_BATCHGETDOCUMENTSREQUEST']._serialized_start = 1646
    _globals['_BATCHGETDOCUMENTSREQUEST']._serialized_end = 1927
    _globals['_BATCHGETDOCUMENTSRESPONSE']._serialized_start = 1930
    _globals['_BATCHGETDOCUMENTSRESPONSE']._serialized_end = 2102
    _globals['_BEGINTRANSACTIONREQUEST']._serialized_start = 2104
    _globals['_BEGINTRANSACTIONREQUEST']._serialized_end = 2210
    _globals['_BEGINTRANSACTIONRESPONSE']._serialized_start = 2212
    _globals['_BEGINTRANSACTIONRESPONSE']._serialized_end = 2259
    _globals['_COMMITREQUEST']._serialized_start = 2261
    _globals['_COMMITREQUEST']._serialized_end = 2364
    _globals['_COMMITRESPONSE']._serialized_start = 2366
    _globals['_COMMITRESPONSE']._serialized_end = 2488
    _globals['_ROLLBACKREQUEST']._serialized_start = 2490
    _globals['_ROLLBACKREQUEST']._serialized_end = 2556
    _globals['_RUNQUERYREQUEST']._serialized_start = 2559
    _globals['_RUNQUERYREQUEST']._serialized_end = 2908
    _globals['_RUNQUERYRESPONSE']._serialized_start = 2911
    _globals['_RUNQUERYRESPONSE']._serialized_end = 3174
    _globals['_RUNAGGREGATIONQUERYREQUEST']._serialized_start = 3177
    _globals['_RUNAGGREGATIONQUERYREQUEST']._serialized_end = 3560
    _globals['_RUNAGGREGATIONQUERYRESPONSE']._serialized_start = 3563
    _globals['_RUNAGGREGATIONQUERYRESPONSE']._serialized_end = 3778
    _globals['_PARTITIONQUERYREQUEST']._serialized_start = 3781
    _globals['_PARTITIONQUERYREQUEST']._serialized_end = 4042
    _globals['_PARTITIONQUERYRESPONSE']._serialized_start = 4044
    _globals['_PARTITIONQUERYRESPONSE']._serialized_end = 4142
    _globals['_WRITEREQUEST']._serialized_start = 4145
    _globals['_WRITEREQUEST']._serialized_end = 4377
    _globals['_WRITEREQUEST_LABELSENTRY']._serialized_start = 4332
    _globals['_WRITEREQUEST_LABELSENTRY']._serialized_end = 4377
    _globals['_WRITERESPONSE']._serialized_start = 4380
    _globals['_WRITERESPONSE']._serialized_end = 4542
    _globals['_LISTENREQUEST']._serialized_start = 4545
    _globals['_LISTENREQUEST']._serialized_end = 4787
    _globals['_LISTENREQUEST_LABELSENTRY']._serialized_start = 4332
    _globals['_LISTENREQUEST_LABELSENTRY']._serialized_end = 4377
    _globals['_LISTENRESPONSE']._serialized_start = 4790
    _globals['_LISTENRESPONSE']._serialized_end = 5131
    _globals['_TARGET']._serialized_start = 5134
    _globals['_TARGET']._serialized_end = 5604
    _globals['_TARGET_DOCUMENTSTARGET']._serialized_start = 5427
    _globals['_TARGET_DOCUMENTSTARGET']._serialized_end = 5463
    _globals['_TARGET_QUERYTARGET']._serialized_start = 5465
    _globals['_TARGET_QUERYTARGET']._serialized_end = 5574
    _globals['_TARGETCHANGE']._serialized_start = 5607
    _globals['_TARGETCHANGE']._serialized_end = 5905
    _globals['_TARGETCHANGE_TARGETCHANGETYPE']._serialized_start = 5827
    _globals['_TARGETCHANGE_TARGETCHANGETYPE']._serialized_end = 5905
    _globals['_LISTCOLLECTIONIDSREQUEST']._serialized_start = 5908
    _globals['_LISTCOLLECTIONIDSREQUEST']._serialized_end = 6067
    _globals['_LISTCOLLECTIONIDSRESPONSE']._serialized_start = 6069
    _globals['_LISTCOLLECTIONIDSRESPONSE']._serialized_end = 6145
    _globals['_BATCHWRITEREQUEST']._serialized_start = 6148
    _globals['_BATCHWRITEREQUEST']._serialized_end = 6349
    _globals['_BATCHWRITEREQUEST_LABELSENTRY']._serialized_start = 4332
    _globals['_BATCHWRITEREQUEST_LABELSENTRY']._serialized_end = 4377
    _globals['_BATCHWRITERESPONSE']._serialized_start = 6351
    _globals['_BATCHWRITERESPONSE']._serialized_end = 6464
    _globals['_FIRESTORE']._serialized_start = 6467
    _globals['_FIRESTORE']._serialized_end = 9757