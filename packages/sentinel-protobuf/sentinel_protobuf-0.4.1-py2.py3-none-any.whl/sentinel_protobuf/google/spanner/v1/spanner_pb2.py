"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/spanner/v1/spanner.proto')
_sym_db = _symbol_database.Default()
from ....google.spanner.v1 import commit_response_pb2 as google_dot_spanner_dot_v1_dot_commit__response__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from ....google.spanner.v1 import keys_pb2 as google_dot_spanner_dot_v1_dot_keys__pb2
from ....google.spanner.v1 import mutation_pb2 as google_dot_spanner_dot_v1_dot_mutation__pb2
from ....google.spanner.v1 import result_set_pb2 as google_dot_spanner_dot_v1_dot_result__set__pb2
from ....google.spanner.v1 import transaction_pb2 as google_dot_spanner_dot_v1_dot_transaction__pb2
from ....google.spanner.v1 import type_pb2 as google_dot_spanner_dot_v1_dot_type__pb2
from ...google.spanner.v1.commit_response_pb2 import *
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fgoogle/spanner/v1/spanner.proto\x12\x11google.spanner.v1\x1a\'google/spanner/v1/commit_response.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x1cgoogle/spanner/v1/keys.proto\x1a google/spanner/v1/mutation.proto\x1a"google/spanner/v1/result_set.proto\x1a#google/spanner/v1/transaction.proto\x1a\x1cgoogle/spanner/v1/type.proto"\x83\x01\n\x14CreateSessionRequest\x129\n\x08database\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database\x120\n\x07session\x18\x02 \x01(\x0b2\x1a.google.spanner.v1.SessionB\x03\xe0A\x02"\xa9\x01\n\x1aBatchCreateSessionsRequest\x129\n\x08database\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database\x124\n\x10session_template\x18\x02 \x01(\x0b2\x1a.google.spanner.v1.Session\x12\x1a\n\rsession_count\x18\x03 \x01(\x05B\x03\xe0A\x02"J\n\x1bBatchCreateSessionsResponse\x12+\n\x07session\x18\x01 \x03(\x0b2\x1a.google.spanner.v1.Session"\xa3\x03\n\x07Session\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x126\n\x06labels\x18\x02 \x03(\x0b2&.google.spanner.v1.Session.LabelsEntry\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12B\n\x19approximate_last_use_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x14\n\x0ccreator_role\x18\x05 \x01(\t\x12\x18\n\x0bmultiplexed\x18\x06 \x01(\x08B\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:t\xeaAq\n\x1espanner.googleapis.com/Session\x12Oprojects/{project}/instances/{instance}/databases/{database}/sessions/{session}"I\n\x11GetSessionRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session"\x87\x01\n\x13ListSessionsRequest\x129\n\x08database\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"]\n\x14ListSessionsResponse\x12,\n\x08sessions\x18\x01 \x03(\x0b2\x1a.google.spanner.v1.Session\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"L\n\x14DeleteSessionRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session"\xdc\x01\n\x0eRequestOptions\x12<\n\x08priority\x18\x01 \x01(\x0e2*.google.spanner.v1.RequestOptions.Priority\x12\x13\n\x0brequest_tag\x18\x02 \x01(\t\x12\x17\n\x0ftransaction_tag\x18\x03 \x01(\t"^\n\x08Priority\x12\x18\n\x14PRIORITY_UNSPECIFIED\x10\x00\x12\x10\n\x0cPRIORITY_LOW\x10\x01\x12\x13\n\x0fPRIORITY_MEDIUM\x10\x02\x12\x11\n\rPRIORITY_HIGH\x10\x03"\xea\x04\n\x13DirectedReadOptions\x12R\n\x10include_replicas\x18\x01 \x01(\x0b26.google.spanner.v1.DirectedReadOptions.IncludeReplicasH\x00\x12R\n\x10exclude_replicas\x18\x02 \x01(\x0b26.google.spanner.v1.DirectedReadOptions.ExcludeReplicasH\x00\x1a\xad\x01\n\x10ReplicaSelection\x12\x10\n\x08location\x18\x01 \x01(\t\x12J\n\x04type\x18\x02 \x01(\x0e2<.google.spanner.v1.DirectedReadOptions.ReplicaSelection.Type";\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nREAD_WRITE\x10\x01\x12\r\n\tREAD_ONLY\x10\x02\x1a\x86\x01\n\x0fIncludeReplicas\x12S\n\x12replica_selections\x18\x01 \x03(\x0b27.google.spanner.v1.DirectedReadOptions.ReplicaSelection\x12\x1e\n\x16auto_failover_disabled\x18\x02 \x01(\x08\x1af\n\x0fExcludeReplicas\x12S\n\x12replica_selections\x18\x01 \x03(\x0b27.google.spanner.v1.DirectedReadOptions.ReplicaSelectionB\n\n\x08replicas"\x8d\x07\n\x11ExecuteSqlRequest\x127\n\x07session\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session\x12;\n\x0btransaction\x18\x02 \x01(\x0b2&.google.spanner.v1.TransactionSelector\x12\x10\n\x03sql\x18\x03 \x01(\tB\x03\xe0A\x02\x12\'\n\x06params\x18\x04 \x01(\x0b2\x17.google.protobuf.Struct\x12I\n\x0bparam_types\x18\x05 \x03(\x0b24.google.spanner.v1.ExecuteSqlRequest.ParamTypesEntry\x12\x14\n\x0cresume_token\x18\x06 \x01(\x0c\x12B\n\nquery_mode\x18\x07 \x01(\x0e2..google.spanner.v1.ExecuteSqlRequest.QueryMode\x12\x17\n\x0fpartition_token\x18\x08 \x01(\x0c\x12\r\n\x05seqno\x18\t \x01(\x03\x12H\n\rquery_options\x18\n \x01(\x0b21.google.spanner.v1.ExecuteSqlRequest.QueryOptions\x12:\n\x0frequest_options\x18\x0b \x01(\x0b2!.google.spanner.v1.RequestOptions\x12E\n\x15directed_read_options\x18\x0f \x01(\x0b2&.google.spanner.v1.DirectedReadOptions\x12\x1a\n\x12data_boost_enabled\x18\x10 \x01(\x08\x12\x1b\n\x0elast_statement\x18\x11 \x01(\x08B\x03\xe0A\x01\x1aO\n\x0cQueryOptions\x12\x19\n\x11optimizer_version\x18\x01 \x01(\t\x12$\n\x1coptimizer_statistics_package\x18\x02 \x01(\t\x1aJ\n\x0fParamTypesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b2\x17.google.spanner.v1.Type:\x028\x01"W\n\tQueryMode\x12\n\n\x06NORMAL\x10\x00\x12\x08\n\x04PLAN\x10\x01\x12\x0b\n\x07PROFILE\x10\x02\x12\x0e\n\nWITH_STATS\x10\x03\x12\x17\n\x13WITH_PLAN_AND_STATS\x10\x04"\xbe\x04\n\x16ExecuteBatchDmlRequest\x127\n\x07session\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session\x12@\n\x0btransaction\x18\x02 \x01(\x0b2&.google.spanner.v1.TransactionSelectorB\x03\xe0A\x02\x12L\n\nstatements\x18\x03 \x03(\x0b23.google.spanner.v1.ExecuteBatchDmlRequest.StatementB\x03\xe0A\x02\x12\x12\n\x05seqno\x18\x04 \x01(\x03B\x03\xe0A\x02\x12:\n\x0frequest_options\x18\x05 \x01(\x0b2!.google.spanner.v1.RequestOptions\x12\x1c\n\x0flast_statements\x18\x06 \x01(\x08B\x03\xe0A\x01\x1a\xec\x01\n\tStatement\x12\x10\n\x03sql\x18\x01 \x01(\tB\x03\xe0A\x02\x12\'\n\x06params\x18\x02 \x01(\x0b2\x17.google.protobuf.Struct\x12X\n\x0bparam_types\x18\x03 \x03(\x0b2C.google.spanner.v1.ExecuteBatchDmlRequest.Statement.ParamTypesEntry\x1aJ\n\x0fParamTypesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b2\x17.google.spanner.v1.Type:\x028\x01"\xc3\x01\n\x17ExecuteBatchDmlResponse\x121\n\x0bresult_sets\x18\x01 \x03(\x0b2\x1c.google.spanner.v1.ResultSet\x12"\n\x06status\x18\x02 \x01(\x0b2\x12.google.rpc.Status\x12Q\n\x0fprecommit_token\x18\x03 \x01(\x0b23.google.spanner.v1.MultiplexedSessionPrecommitTokenB\x03\xe0A\x01"H\n\x10PartitionOptions\x12\x1c\n\x14partition_size_bytes\x18\x01 \x01(\x03\x12\x16\n\x0emax_partitions\x18\x02 \x01(\x03"\xa3\x03\n\x15PartitionQueryRequest\x127\n\x07session\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session\x12;\n\x0btransaction\x18\x02 \x01(\x0b2&.google.spanner.v1.TransactionSelector\x12\x10\n\x03sql\x18\x03 \x01(\tB\x03\xe0A\x02\x12\'\n\x06params\x18\x04 \x01(\x0b2\x17.google.protobuf.Struct\x12M\n\x0bparam_types\x18\x05 \x03(\x0b28.google.spanner.v1.PartitionQueryRequest.ParamTypesEntry\x12>\n\x11partition_options\x18\x06 \x01(\x0b2#.google.spanner.v1.PartitionOptions\x1aJ\n\x0fParamTypesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b2\x17.google.spanner.v1.Type:\x028\x01"\xb1\x02\n\x14PartitionReadRequest\x127\n\x07session\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session\x12;\n\x0btransaction\x18\x02 \x01(\x0b2&.google.spanner.v1.TransactionSelector\x12\x12\n\x05table\x18\x03 \x01(\tB\x03\xe0A\x02\x12\r\n\x05index\x18\x04 \x01(\t\x12\x0f\n\x07columns\x18\x05 \x03(\t\x12/\n\x07key_set\x18\x06 \x01(\x0b2\x19.google.spanner.v1.KeySetB\x03\xe0A\x02\x12>\n\x11partition_options\x18\t \x01(\x0b2#.google.spanner.v1.PartitionOptions"$\n\tPartition\x12\x17\n\x0fpartition_token\x18\x01 \x01(\x0c"z\n\x11PartitionResponse\x120\n\npartitions\x18\x01 \x03(\x0b2\x1c.google.spanner.v1.Partition\x123\n\x0btransaction\x18\x02 \x01(\x0b2\x1e.google.spanner.v1.Transaction"\xf6\x05\n\x0bReadRequest\x127\n\x07session\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session\x12;\n\x0btransaction\x18\x02 \x01(\x0b2&.google.spanner.v1.TransactionSelector\x12\x12\n\x05table\x18\x03 \x01(\tB\x03\xe0A\x02\x12\r\n\x05index\x18\x04 \x01(\t\x12\x14\n\x07columns\x18\x05 \x03(\tB\x03\xe0A\x02\x12/\n\x07key_set\x18\x06 \x01(\x0b2\x19.google.spanner.v1.KeySetB\x03\xe0A\x02\x12\r\n\x05limit\x18\x08 \x01(\x03\x12\x14\n\x0cresume_token\x18\t \x01(\x0c\x12\x17\n\x0fpartition_token\x18\n \x01(\x0c\x12:\n\x0frequest_options\x18\x0b \x01(\x0b2!.google.spanner.v1.RequestOptions\x12E\n\x15directed_read_options\x18\x0e \x01(\x0b2&.google.spanner.v1.DirectedReadOptions\x12\x1a\n\x12data_boost_enabled\x18\x0f \x01(\x08\x12=\n\x08order_by\x18\x10 \x01(\x0e2&.google.spanner.v1.ReadRequest.OrderByB\x03\xe0A\x01\x12?\n\tlock_hint\x18\x11 \x01(\x0e2\'.google.spanner.v1.ReadRequest.LockHintB\x03\xe0A\x01"T\n\x07OrderBy\x12\x18\n\x14ORDER_BY_UNSPECIFIED\x10\x00\x12\x18\n\x14ORDER_BY_PRIMARY_KEY\x10\x01\x12\x15\n\x11ORDER_BY_NO_ORDER\x10\x02"T\n\x08LockHint\x12\x19\n\x15LOCK_HINT_UNSPECIFIED\x10\x00\x12\x14\n\x10LOCK_HINT_SHARED\x10\x01\x12\x17\n\x13LOCK_HINT_EXCLUSIVE\x10\x02"\x83\x02\n\x17BeginTransactionRequest\x127\n\x07session\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session\x12;\n\x07options\x18\x02 \x01(\x0b2%.google.spanner.v1.TransactionOptionsB\x03\xe0A\x02\x12:\n\x0frequest_options\x18\x03 \x01(\x0b2!.google.spanner.v1.RequestOptions\x126\n\x0cmutation_key\x18\x04 \x01(\x0b2\x1b.google.spanner.v1.MutationB\x03\xe0A\x01"\xd0\x03\n\rCommitRequest\x127\n\x07session\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session\x12\x18\n\x0etransaction_id\x18\x02 \x01(\x0cH\x00\x12G\n\x16single_use_transaction\x18\x03 \x01(\x0b2%.google.spanner.v1.TransactionOptionsH\x00\x12.\n\tmutations\x18\x04 \x03(\x0b2\x1b.google.spanner.v1.Mutation\x12\x1b\n\x13return_commit_stats\x18\x05 \x01(\x08\x128\n\x10max_commit_delay\x18\x08 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x12:\n\x0frequest_options\x18\x06 \x01(\x0b2!.google.spanner.v1.RequestOptions\x12Q\n\x0fprecommit_token\x18\t \x01(\x0b23.google.spanner.v1.MultiplexedSessionPrecommitTokenB\x03\xe0A\x01B\r\n\x0btransaction"g\n\x0fRollbackRequest\x127\n\x07session\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session\x12\x1b\n\x0etransaction_id\x18\x02 \x01(\x0cB\x03\xe0A\x02"\xce\x02\n\x11BatchWriteRequest\x127\n\x07session\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session\x12:\n\x0frequest_options\x18\x03 \x01(\x0b2!.google.spanner.v1.RequestOptions\x12P\n\x0fmutation_groups\x18\x04 \x03(\x0b22.google.spanner.v1.BatchWriteRequest.MutationGroupB\x03\xe0A\x02\x12,\n\x1fexclude_txn_from_change_streams\x18\x05 \x01(\x08B\x03\xe0A\x01\x1aD\n\rMutationGroup\x123\n\tmutations\x18\x01 \x03(\x0b2\x1b.google.spanner.v1.MutationB\x03\xe0A\x02"\x7f\n\x12BatchWriteResponse\x12\x0f\n\x07indexes\x18\x01 \x03(\x05\x12"\n\x06status\x18\x02 \x01(\x0b2\x12.google.rpc.Status\x124\n\x10commit_timestamp\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp2\x8b\x18\n\x07Spanner\x12\xa6\x01\n\rCreateSession\x12\'.google.spanner.v1.CreateSessionRequest\x1a\x1a.google.spanner.v1.Session"P\xdaA\x08database\x82\xd3\xe4\x93\x02?":/v1/{database=projects/*/instances/*/databases/*}/sessions:\x01*\x12\xe0\x01\n\x13BatchCreateSessions\x12-.google.spanner.v1.BatchCreateSessionsRequest\x1a..google.spanner.v1.BatchCreateSessionsResponse"j\xdaA\x16database,session_count\x82\xd3\xe4\x93\x02K"F/v1/{database=projects/*/instances/*/databases/*}/sessions:batchCreate:\x01*\x12\x97\x01\n\nGetSession\x12$.google.spanner.v1.GetSessionRequest\x1a\x1a.google.spanner.v1.Session"G\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/v1/{name=projects/*/instances/*/databases/*/sessions/*}\x12\xae\x01\n\x0cListSessions\x12&.google.spanner.v1.ListSessionsRequest\x1a\'.google.spanner.v1.ListSessionsResponse"M\xdaA\x08database\x82\xd3\xe4\x93\x02<\x12:/v1/{database=projects/*/instances/*/databases/*}/sessions\x12\x99\x01\n\rDeleteSession\x12\'.google.spanner.v1.DeleteSessionRequest\x1a\x16.google.protobuf.Empty"G\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v1/{name=projects/*/instances/*/databases/*/sessions/*}\x12\xa3\x01\n\nExecuteSql\x12$.google.spanner.v1.ExecuteSqlRequest\x1a\x1c.google.spanner.v1.ResultSet"Q\x82\xd3\xe4\x93\x02K"F/v1/{session=projects/*/instances/*/databases/*/sessions/*}:executeSql:\x01*\x12\xbe\x01\n\x13ExecuteStreamingSql\x12$.google.spanner.v1.ExecuteSqlRequest\x1a#.google.spanner.v1.PartialResultSet"Z\x82\xd3\xe4\x93\x02T"O/v1/{session=projects/*/instances/*/databases/*/sessions/*}:executeStreamingSql:\x01*0\x01\x12\xc0\x01\n\x0fExecuteBatchDml\x12).google.spanner.v1.ExecuteBatchDmlRequest\x1a*.google.spanner.v1.ExecuteBatchDmlResponse"V\x82\xd3\xe4\x93\x02P"K/v1/{session=projects/*/instances/*/databases/*/sessions/*}:executeBatchDml:\x01*\x12\x91\x01\n\x04Read\x12\x1e.google.spanner.v1.ReadRequest\x1a\x1c.google.spanner.v1.ResultSet"K\x82\xd3\xe4\x93\x02E"@/v1/{session=projects/*/instances/*/databases/*/sessions/*}:read:\x01*\x12\xac\x01\n\rStreamingRead\x12\x1e.google.spanner.v1.ReadRequest\x1a#.google.spanner.v1.PartialResultSet"T\x82\xd3\xe4\x93\x02N"I/v1/{session=projects/*/instances/*/databases/*/sessions/*}:streamingRead:\x01*0\x01\x12\xc9\x01\n\x10BeginTransaction\x12*.google.spanner.v1.BeginTransactionRequest\x1a\x1e.google.spanner.v1.Transaction"i\xdaA\x0fsession,options\x82\xd3\xe4\x93\x02Q"L/v1/{session=projects/*/instances/*/databases/*/sessions/*}:beginTransaction:\x01*\x12\xeb\x01\n\x06Commit\x12 .google.spanner.v1.CommitRequest\x1a!.google.spanner.v1.CommitResponse"\x9b\x01\xdaA session,transaction_id,mutations\xdaA(session,single_use_transaction,mutations\x82\xd3\xe4\x93\x02G"B/v1/{session=projects/*/instances/*/databases/*/sessions/*}:commit:\x01*\x12\xb0\x01\n\x08Rollback\x12".google.spanner.v1.RollbackRequest\x1a\x16.google.protobuf.Empty"h\xdaA\x16session,transaction_id\x82\xd3\xe4\x93\x02I"D/v1/{session=projects/*/instances/*/databases/*/sessions/*}:rollback:\x01*\x12\xb7\x01\n\x0ePartitionQuery\x12(.google.spanner.v1.PartitionQueryRequest\x1a$.google.spanner.v1.PartitionResponse"U\x82\xd3\xe4\x93\x02O"J/v1/{session=projects/*/instances/*/databases/*/sessions/*}:partitionQuery:\x01*\x12\xb4\x01\n\rPartitionRead\x12\'.google.spanner.v1.PartitionReadRequest\x1a$.google.spanner.v1.PartitionResponse"T\x82\xd3\xe4\x93\x02N"I/v1/{session=projects/*/instances/*/databases/*/sessions/*}:partitionRead:\x01*\x12\xc8\x01\n\nBatchWrite\x12$.google.spanner.v1.BatchWriteRequest\x1a%.google.spanner.v1.BatchWriteResponse"k\xdaA\x17session,mutation_groups\x82\xd3\xe4\x93\x02K"F/v1/{session=projects/*/instances/*/databases/*/sessions/*}:batchWrite:\x01*0\x01\x1aw\xcaA\x16spanner.googleapis.com\xd2A[https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/spanner.dataB\x91\x02\n\x15com.google.spanner.v1B\x0cSpannerProtoP\x01Z5cloud.google.com/go/spanner/apiv1/spannerpb;spannerpb\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1\xea\x02\x1aGoogle::Cloud::Spanner::V1\xeaA_\n\x1fspanner.googleapis.com/Database\x12<projects/{project}/instances/{instance}/databases/{database}P\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.spanner.v1.spanner_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x15com.google.spanner.v1B\x0cSpannerProtoP\x01Z5cloud.google.com/go/spanner/apiv1/spannerpb;spannerpb\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1\xea\x02\x1aGoogle::Cloud::Spanner::V1\xeaA_\n\x1fspanner.googleapis.com/Database\x12<projects/{project}/instances/{instance}/databases/{database}'
    _globals['_CREATESESSIONREQUEST'].fields_by_name['database']._loaded_options = None
    _globals['_CREATESESSIONREQUEST'].fields_by_name['database']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database'
    _globals['_CREATESESSIONREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_CREATESESSIONREQUEST'].fields_by_name['session']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHCREATESESSIONSREQUEST'].fields_by_name['database']._loaded_options = None
    _globals['_BATCHCREATESESSIONSREQUEST'].fields_by_name['database']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database'
    _globals['_BATCHCREATESESSIONSREQUEST'].fields_by_name['session_count']._loaded_options = None
    _globals['_BATCHCREATESESSIONSREQUEST'].fields_by_name['session_count']._serialized_options = b'\xe0A\x02'
    _globals['_SESSION_LABELSENTRY']._loaded_options = None
    _globals['_SESSION_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_SESSION'].fields_by_name['name']._loaded_options = None
    _globals['_SESSION'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION'].fields_by_name['create_time']._loaded_options = None
    _globals['_SESSION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION'].fields_by_name['approximate_last_use_time']._loaded_options = None
    _globals['_SESSION'].fields_by_name['approximate_last_use_time']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION'].fields_by_name['multiplexed']._loaded_options = None
    _globals['_SESSION'].fields_by_name['multiplexed']._serialized_options = b'\xe0A\x01'
    _globals['_SESSION']._loaded_options = None
    _globals['_SESSION']._serialized_options = b'\xeaAq\n\x1espanner.googleapis.com/Session\x12Oprojects/{project}/instances/{instance}/databases/{database}/sessions/{session}'
    _globals['_GETSESSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSESSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session'
    _globals['_LISTSESSIONSREQUEST'].fields_by_name['database']._loaded_options = None
    _globals['_LISTSESSIONSREQUEST'].fields_by_name['database']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database'
    _globals['_DELETESESSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESESSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session'
    _globals['_EXECUTESQLREQUEST_PARAMTYPESENTRY']._loaded_options = None
    _globals['_EXECUTESQLREQUEST_PARAMTYPESENTRY']._serialized_options = b'8\x01'
    _globals['_EXECUTESQLREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_EXECUTESQLREQUEST'].fields_by_name['session']._serialized_options = b'\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session'
    _globals['_EXECUTESQLREQUEST'].fields_by_name['sql']._loaded_options = None
    _globals['_EXECUTESQLREQUEST'].fields_by_name['sql']._serialized_options = b'\xe0A\x02'
    _globals['_EXECUTESQLREQUEST'].fields_by_name['last_statement']._loaded_options = None
    _globals['_EXECUTESQLREQUEST'].fields_by_name['last_statement']._serialized_options = b'\xe0A\x01'
    _globals['_EXECUTEBATCHDMLREQUEST_STATEMENT_PARAMTYPESENTRY']._loaded_options = None
    _globals['_EXECUTEBATCHDMLREQUEST_STATEMENT_PARAMTYPESENTRY']._serialized_options = b'8\x01'
    _globals['_EXECUTEBATCHDMLREQUEST_STATEMENT'].fields_by_name['sql']._loaded_options = None
    _globals['_EXECUTEBATCHDMLREQUEST_STATEMENT'].fields_by_name['sql']._serialized_options = b'\xe0A\x02'
    _globals['_EXECUTEBATCHDMLREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_EXECUTEBATCHDMLREQUEST'].fields_by_name['session']._serialized_options = b'\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session'
    _globals['_EXECUTEBATCHDMLREQUEST'].fields_by_name['transaction']._loaded_options = None
    _globals['_EXECUTEBATCHDMLREQUEST'].fields_by_name['transaction']._serialized_options = b'\xe0A\x02'
    _globals['_EXECUTEBATCHDMLREQUEST'].fields_by_name['statements']._loaded_options = None
    _globals['_EXECUTEBATCHDMLREQUEST'].fields_by_name['statements']._serialized_options = b'\xe0A\x02'
    _globals['_EXECUTEBATCHDMLREQUEST'].fields_by_name['seqno']._loaded_options = None
    _globals['_EXECUTEBATCHDMLREQUEST'].fields_by_name['seqno']._serialized_options = b'\xe0A\x02'
    _globals['_EXECUTEBATCHDMLREQUEST'].fields_by_name['last_statements']._loaded_options = None
    _globals['_EXECUTEBATCHDMLREQUEST'].fields_by_name['last_statements']._serialized_options = b'\xe0A\x01'
    _globals['_EXECUTEBATCHDMLRESPONSE'].fields_by_name['precommit_token']._loaded_options = None
    _globals['_EXECUTEBATCHDMLRESPONSE'].fields_by_name['precommit_token']._serialized_options = b'\xe0A\x01'
    _globals['_PARTITIONQUERYREQUEST_PARAMTYPESENTRY']._loaded_options = None
    _globals['_PARTITIONQUERYREQUEST_PARAMTYPESENTRY']._serialized_options = b'8\x01'
    _globals['_PARTITIONQUERYREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_PARTITIONQUERYREQUEST'].fields_by_name['session']._serialized_options = b'\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session'
    _globals['_PARTITIONQUERYREQUEST'].fields_by_name['sql']._loaded_options = None
    _globals['_PARTITIONQUERYREQUEST'].fields_by_name['sql']._serialized_options = b'\xe0A\x02'
    _globals['_PARTITIONREADREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_PARTITIONREADREQUEST'].fields_by_name['session']._serialized_options = b'\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session'
    _globals['_PARTITIONREADREQUEST'].fields_by_name['table']._loaded_options = None
    _globals['_PARTITIONREADREQUEST'].fields_by_name['table']._serialized_options = b'\xe0A\x02'
    _globals['_PARTITIONREADREQUEST'].fields_by_name['key_set']._loaded_options = None
    _globals['_PARTITIONREADREQUEST'].fields_by_name['key_set']._serialized_options = b'\xe0A\x02'
    _globals['_READREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_READREQUEST'].fields_by_name['session']._serialized_options = b'\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session'
    _globals['_READREQUEST'].fields_by_name['table']._loaded_options = None
    _globals['_READREQUEST'].fields_by_name['table']._serialized_options = b'\xe0A\x02'
    _globals['_READREQUEST'].fields_by_name['columns']._loaded_options = None
    _globals['_READREQUEST'].fields_by_name['columns']._serialized_options = b'\xe0A\x02'
    _globals['_READREQUEST'].fields_by_name['key_set']._loaded_options = None
    _globals['_READREQUEST'].fields_by_name['key_set']._serialized_options = b'\xe0A\x02'
    _globals['_READREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_READREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_READREQUEST'].fields_by_name['lock_hint']._loaded_options = None
    _globals['_READREQUEST'].fields_by_name['lock_hint']._serialized_options = b'\xe0A\x01'
    _globals['_BEGINTRANSACTIONREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_BEGINTRANSACTIONREQUEST'].fields_by_name['session']._serialized_options = b'\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session'
    _globals['_BEGINTRANSACTIONREQUEST'].fields_by_name['options']._loaded_options = None
    _globals['_BEGINTRANSACTIONREQUEST'].fields_by_name['options']._serialized_options = b'\xe0A\x02'
    _globals['_BEGINTRANSACTIONREQUEST'].fields_by_name['mutation_key']._loaded_options = None
    _globals['_BEGINTRANSACTIONREQUEST'].fields_by_name['mutation_key']._serialized_options = b'\xe0A\x01'
    _globals['_COMMITREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_COMMITREQUEST'].fields_by_name['session']._serialized_options = b'\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session'
    _globals['_COMMITREQUEST'].fields_by_name['max_commit_delay']._loaded_options = None
    _globals['_COMMITREQUEST'].fields_by_name['max_commit_delay']._serialized_options = b'\xe0A\x01'
    _globals['_COMMITREQUEST'].fields_by_name['precommit_token']._loaded_options = None
    _globals['_COMMITREQUEST'].fields_by_name['precommit_token']._serialized_options = b'\xe0A\x01'
    _globals['_ROLLBACKREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_ROLLBACKREQUEST'].fields_by_name['session']._serialized_options = b'\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session'
    _globals['_ROLLBACKREQUEST'].fields_by_name['transaction_id']._loaded_options = None
    _globals['_ROLLBACKREQUEST'].fields_by_name['transaction_id']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHWRITEREQUEST_MUTATIONGROUP'].fields_by_name['mutations']._loaded_options = None
    _globals['_BATCHWRITEREQUEST_MUTATIONGROUP'].fields_by_name['mutations']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHWRITEREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_BATCHWRITEREQUEST'].fields_by_name['session']._serialized_options = b'\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session'
    _globals['_BATCHWRITEREQUEST'].fields_by_name['mutation_groups']._loaded_options = None
    _globals['_BATCHWRITEREQUEST'].fields_by_name['mutation_groups']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHWRITEREQUEST'].fields_by_name['exclude_txn_from_change_streams']._loaded_options = None
    _globals['_BATCHWRITEREQUEST'].fields_by_name['exclude_txn_from_change_streams']._serialized_options = b'\xe0A\x01'
    _globals['_SPANNER']._loaded_options = None
    _globals['_SPANNER']._serialized_options = b'\xcaA\x16spanner.googleapis.com\xd2A[https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/spanner.data'
    _globals['_SPANNER'].methods_by_name['CreateSession']._loaded_options = None
    _globals['_SPANNER'].methods_by_name['CreateSession']._serialized_options = b'\xdaA\x08database\x82\xd3\xe4\x93\x02?":/v1/{database=projects/*/instances/*/databases/*}/sessions:\x01*'
    _globals['_SPANNER'].methods_by_name['BatchCreateSessions']._loaded_options = None
    _globals['_SPANNER'].methods_by_name['BatchCreateSessions']._serialized_options = b'\xdaA\x16database,session_count\x82\xd3\xe4\x93\x02K"F/v1/{database=projects/*/instances/*/databases/*}/sessions:batchCreate:\x01*'
    _globals['_SPANNER'].methods_by_name['GetSession']._loaded_options = None
    _globals['_SPANNER'].methods_by_name['GetSession']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/v1/{name=projects/*/instances/*/databases/*/sessions/*}'
    _globals['_SPANNER'].methods_by_name['ListSessions']._loaded_options = None
    _globals['_SPANNER'].methods_by_name['ListSessions']._serialized_options = b'\xdaA\x08database\x82\xd3\xe4\x93\x02<\x12:/v1/{database=projects/*/instances/*/databases/*}/sessions'
    _globals['_SPANNER'].methods_by_name['DeleteSession']._loaded_options = None
    _globals['_SPANNER'].methods_by_name['DeleteSession']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v1/{name=projects/*/instances/*/databases/*/sessions/*}'
    _globals['_SPANNER'].methods_by_name['ExecuteSql']._loaded_options = None
    _globals['_SPANNER'].methods_by_name['ExecuteSql']._serialized_options = b'\x82\xd3\xe4\x93\x02K"F/v1/{session=projects/*/instances/*/databases/*/sessions/*}:executeSql:\x01*'
    _globals['_SPANNER'].methods_by_name['ExecuteStreamingSql']._loaded_options = None
    _globals['_SPANNER'].methods_by_name['ExecuteStreamingSql']._serialized_options = b'\x82\xd3\xe4\x93\x02T"O/v1/{session=projects/*/instances/*/databases/*/sessions/*}:executeStreamingSql:\x01*'
    _globals['_SPANNER'].methods_by_name['ExecuteBatchDml']._loaded_options = None
    _globals['_SPANNER'].methods_by_name['ExecuteBatchDml']._serialized_options = b'\x82\xd3\xe4\x93\x02P"K/v1/{session=projects/*/instances/*/databases/*/sessions/*}:executeBatchDml:\x01*'
    _globals['_SPANNER'].methods_by_name['Read']._loaded_options = None
    _globals['_SPANNER'].methods_by_name['Read']._serialized_options = b'\x82\xd3\xe4\x93\x02E"@/v1/{session=projects/*/instances/*/databases/*/sessions/*}:read:\x01*'
    _globals['_SPANNER'].methods_by_name['StreamingRead']._loaded_options = None
    _globals['_SPANNER'].methods_by_name['StreamingRead']._serialized_options = b'\x82\xd3\xe4\x93\x02N"I/v1/{session=projects/*/instances/*/databases/*/sessions/*}:streamingRead:\x01*'
    _globals['_SPANNER'].methods_by_name['BeginTransaction']._loaded_options = None
    _globals['_SPANNER'].methods_by_name['BeginTransaction']._serialized_options = b'\xdaA\x0fsession,options\x82\xd3\xe4\x93\x02Q"L/v1/{session=projects/*/instances/*/databases/*/sessions/*}:beginTransaction:\x01*'
    _globals['_SPANNER'].methods_by_name['Commit']._loaded_options = None
    _globals['_SPANNER'].methods_by_name['Commit']._serialized_options = b'\xdaA session,transaction_id,mutations\xdaA(session,single_use_transaction,mutations\x82\xd3\xe4\x93\x02G"B/v1/{session=projects/*/instances/*/databases/*/sessions/*}:commit:\x01*'
    _globals['_SPANNER'].methods_by_name['Rollback']._loaded_options = None
    _globals['_SPANNER'].methods_by_name['Rollback']._serialized_options = b'\xdaA\x16session,transaction_id\x82\xd3\xe4\x93\x02I"D/v1/{session=projects/*/instances/*/databases/*/sessions/*}:rollback:\x01*'
    _globals['_SPANNER'].methods_by_name['PartitionQuery']._loaded_options = None
    _globals['_SPANNER'].methods_by_name['PartitionQuery']._serialized_options = b'\x82\xd3\xe4\x93\x02O"J/v1/{session=projects/*/instances/*/databases/*/sessions/*}:partitionQuery:\x01*'
    _globals['_SPANNER'].methods_by_name['PartitionRead']._loaded_options = None
    _globals['_SPANNER'].methods_by_name['PartitionRead']._serialized_options = b'\x82\xd3\xe4\x93\x02N"I/v1/{session=projects/*/instances/*/databases/*/sessions/*}:partitionRead:\x01*'
    _globals['_SPANNER'].methods_by_name['BatchWrite']._loaded_options = None
    _globals['_SPANNER'].methods_by_name['BatchWrite']._serialized_options = b'\xdaA\x17session,mutation_groups\x82\xd3\xe4\x93\x02K"F/v1/{session=projects/*/instances/*/databases/*/sessions/*}:batchWrite:\x01*'
    _globals['_CREATESESSIONREQUEST']._serialized_start = 527
    _globals['_CREATESESSIONREQUEST']._serialized_end = 658
    _globals['_BATCHCREATESESSIONSREQUEST']._serialized_start = 661
    _globals['_BATCHCREATESESSIONSREQUEST']._serialized_end = 830
    _globals['_BATCHCREATESESSIONSRESPONSE']._serialized_start = 832
    _globals['_BATCHCREATESESSIONSRESPONSE']._serialized_end = 906
    _globals['_SESSION']._serialized_start = 909
    _globals['_SESSION']._serialized_end = 1328
    _globals['_SESSION_LABELSENTRY']._serialized_start = 1165
    _globals['_SESSION_LABELSENTRY']._serialized_end = 1210
    _globals['_GETSESSIONREQUEST']._serialized_start = 1330
    _globals['_GETSESSIONREQUEST']._serialized_end = 1403
    _globals['_LISTSESSIONSREQUEST']._serialized_start = 1406
    _globals['_LISTSESSIONSREQUEST']._serialized_end = 1541
    _globals['_LISTSESSIONSRESPONSE']._serialized_start = 1543
    _globals['_LISTSESSIONSRESPONSE']._serialized_end = 1636
    _globals['_DELETESESSIONREQUEST']._serialized_start = 1638
    _globals['_DELETESESSIONREQUEST']._serialized_end = 1714
    _globals['_REQUESTOPTIONS']._serialized_start = 1717
    _globals['_REQUESTOPTIONS']._serialized_end = 1937
    _globals['_REQUESTOPTIONS_PRIORITY']._serialized_start = 1843
    _globals['_REQUESTOPTIONS_PRIORITY']._serialized_end = 1937
    _globals['_DIRECTEDREADOPTIONS']._serialized_start = 1940
    _globals['_DIRECTEDREADOPTIONS']._serialized_end = 2558
    _globals['_DIRECTEDREADOPTIONS_REPLICASELECTION']._serialized_start = 2132
    _globals['_DIRECTEDREADOPTIONS_REPLICASELECTION']._serialized_end = 2305
    _globals['_DIRECTEDREADOPTIONS_REPLICASELECTION_TYPE']._serialized_start = 2246
    _globals['_DIRECTEDREADOPTIONS_REPLICASELECTION_TYPE']._serialized_end = 2305
    _globals['_DIRECTEDREADOPTIONS_INCLUDEREPLICAS']._serialized_start = 2308
    _globals['_DIRECTEDREADOPTIONS_INCLUDEREPLICAS']._serialized_end = 2442
    _globals['_DIRECTEDREADOPTIONS_EXCLUDEREPLICAS']._serialized_start = 2444
    _globals['_DIRECTEDREADOPTIONS_EXCLUDEREPLICAS']._serialized_end = 2546
    _globals['_EXECUTESQLREQUEST']._serialized_start = 2561
    _globals['_EXECUTESQLREQUEST']._serialized_end = 3470
    _globals['_EXECUTESQLREQUEST_QUERYOPTIONS']._serialized_start = 3226
    _globals['_EXECUTESQLREQUEST_QUERYOPTIONS']._serialized_end = 3305
    _globals['_EXECUTESQLREQUEST_PARAMTYPESENTRY']._serialized_start = 3307
    _globals['_EXECUTESQLREQUEST_PARAMTYPESENTRY']._serialized_end = 3381
    _globals['_EXECUTESQLREQUEST_QUERYMODE']._serialized_start = 3383
    _globals['_EXECUTESQLREQUEST_QUERYMODE']._serialized_end = 3470
    _globals['_EXECUTEBATCHDMLREQUEST']._serialized_start = 3473
    _globals['_EXECUTEBATCHDMLREQUEST']._serialized_end = 4047
    _globals['_EXECUTEBATCHDMLREQUEST_STATEMENT']._serialized_start = 3811
    _globals['_EXECUTEBATCHDMLREQUEST_STATEMENT']._serialized_end = 4047
    _globals['_EXECUTEBATCHDMLREQUEST_STATEMENT_PARAMTYPESENTRY']._serialized_start = 3307
    _globals['_EXECUTEBATCHDMLREQUEST_STATEMENT_PARAMTYPESENTRY']._serialized_end = 3381
    _globals['_EXECUTEBATCHDMLRESPONSE']._serialized_start = 4050
    _globals['_EXECUTEBATCHDMLRESPONSE']._serialized_end = 4245
    _globals['_PARTITIONOPTIONS']._serialized_start = 4247
    _globals['_PARTITIONOPTIONS']._serialized_end = 4319
    _globals['_PARTITIONQUERYREQUEST']._serialized_start = 4322
    _globals['_PARTITIONQUERYREQUEST']._serialized_end = 4741
    _globals['_PARTITIONQUERYREQUEST_PARAMTYPESENTRY']._serialized_start = 3307
    _globals['_PARTITIONQUERYREQUEST_PARAMTYPESENTRY']._serialized_end = 3381
    _globals['_PARTITIONREADREQUEST']._serialized_start = 4744
    _globals['_PARTITIONREADREQUEST']._serialized_end = 5049
    _globals['_PARTITION']._serialized_start = 5051
    _globals['_PARTITION']._serialized_end = 5087
    _globals['_PARTITIONRESPONSE']._serialized_start = 5089
    _globals['_PARTITIONRESPONSE']._serialized_end = 5211
    _globals['_READREQUEST']._serialized_start = 5214
    _globals['_READREQUEST']._serialized_end = 5972
    _globals['_READREQUEST_ORDERBY']._serialized_start = 5802
    _globals['_READREQUEST_ORDERBY']._serialized_end = 5886
    _globals['_READREQUEST_LOCKHINT']._serialized_start = 5888
    _globals['_READREQUEST_LOCKHINT']._serialized_end = 5972
    _globals['_BEGINTRANSACTIONREQUEST']._serialized_start = 5975
    _globals['_BEGINTRANSACTIONREQUEST']._serialized_end = 6234
    _globals['_COMMITREQUEST']._serialized_start = 6237
    _globals['_COMMITREQUEST']._serialized_end = 6701
    _globals['_ROLLBACKREQUEST']._serialized_start = 6703
    _globals['_ROLLBACKREQUEST']._serialized_end = 6806
    _globals['_BATCHWRITEREQUEST']._serialized_start = 6809
    _globals['_BATCHWRITEREQUEST']._serialized_end = 7143
    _globals['_BATCHWRITEREQUEST_MUTATIONGROUP']._serialized_start = 7075
    _globals['_BATCHWRITEREQUEST_MUTATIONGROUP']._serialized_end = 7143
    _globals['_BATCHWRITERESPONSE']._serialized_start = 7145
    _globals['_BATCHWRITERESPONSE']._serialized_end = 7272
    _globals['_SPANNER']._serialized_start = 7275
    _globals['_SPANNER']._serialized_end = 10358