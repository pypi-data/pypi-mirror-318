"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/datastore/v1beta3/datastore.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.datastore.v1beta3 import entity_pb2 as google_dot_datastore_dot_v1beta3_dot_entity__pb2
from ....google.datastore.v1beta3 import query_pb2 as google_dot_datastore_dot_v1beta3_dot_query__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/datastore/v1beta3/datastore.proto\x12\x18google.datastore.v1beta3\x1a\x1cgoogle/api/annotations.proto\x1a%google/datastore/v1beta3/entity.proto\x1a$google/datastore/v1beta3/query.proto"\x8d\x01\n\rLookupRequest\x12\x12\n\nproject_id\x18\x08 \x01(\t\x12;\n\x0cread_options\x18\x01 \x01(\x0b2%.google.datastore.v1beta3.ReadOptions\x12+\n\x04keys\x18\x03 \x03(\x0b2\x1d.google.datastore.v1beta3.Key"\xb1\x01\n\x0eLookupResponse\x125\n\x05found\x18\x01 \x03(\x0b2&.google.datastore.v1beta3.EntityResult\x127\n\x07missing\x18\x02 \x03(\x0b2&.google.datastore.v1beta3.EntityResult\x12/\n\x08deferred\x18\x03 \x03(\x0b2\x1d.google.datastore.v1beta3.Key"\x98\x02\n\x0fRunQueryRequest\x12\x12\n\nproject_id\x18\x08 \x01(\t\x12;\n\x0cpartition_id\x18\x02 \x01(\x0b2%.google.datastore.v1beta3.PartitionId\x12;\n\x0cread_options\x18\x01 \x01(\x0b2%.google.datastore.v1beta3.ReadOptions\x120\n\x05query\x18\x03 \x01(\x0b2\x1f.google.datastore.v1beta3.QueryH\x00\x127\n\tgql_query\x18\x07 \x01(\x0b2".google.datastore.v1beta3.GqlQueryH\x00B\x0c\n\nquery_type"}\n\x10RunQueryResponse\x129\n\x05batch\x18\x01 \x01(\x0b2*.google.datastore.v1beta3.QueryResultBatch\x12.\n\x05query\x18\x02 \x01(\x0b2\x1f.google.datastore.v1beta3.Query"x\n\x17BeginTransactionRequest\x12\x12\n\nproject_id\x18\x08 \x01(\t\x12I\n\x13transaction_options\x18\n \x01(\x0b2,.google.datastore.v1beta3.TransactionOptions"/\n\x18BeginTransactionResponse\x12\x13\n\x0btransaction\x18\x01 \x01(\x0c":\n\x0fRollbackRequest\x12\x12\n\nproject_id\x18\x08 \x01(\t\x12\x13\n\x0btransaction\x18\x01 \x01(\x0c"\x12\n\x10RollbackResponse"\x8d\x02\n\rCommitRequest\x12\x12\n\nproject_id\x18\x08 \x01(\t\x12:\n\x04mode\x18\x05 \x01(\x0e2,.google.datastore.v1beta3.CommitRequest.Mode\x12\x15\n\x0btransaction\x18\x01 \x01(\x0cH\x00\x125\n\tmutations\x18\x06 \x03(\x0b2".google.datastore.v1beta3.Mutation"F\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x11\n\rTRANSACTIONAL\x10\x01\x12\x15\n\x11NON_TRANSACTIONAL\x10\x02B\x16\n\x14transaction_selector"k\n\x0eCommitResponse\x12B\n\x10mutation_results\x18\x03 \x03(\x0b2(.google.datastore.v1beta3.MutationResult\x12\x15\n\rindex_updates\x18\x04 \x01(\x05"U\n\x12AllocateIdsRequest\x12\x12\n\nproject_id\x18\x08 \x01(\t\x12+\n\x04keys\x18\x01 \x03(\x0b2\x1d.google.datastore.v1beta3.Key"B\n\x13AllocateIdsResponse\x12+\n\x04keys\x18\x01 \x03(\x0b2\x1d.google.datastore.v1beta3.Key"i\n\x11ReserveIdsRequest\x12\x12\n\nproject_id\x18\x08 \x01(\t\x12\x13\n\x0bdatabase_id\x18\t \x01(\t\x12+\n\x04keys\x18\x01 \x03(\x0b2\x1d.google.datastore.v1beta3.Key"\x14\n\x12ReserveIdsResponse"\x9b\x02\n\x08Mutation\x122\n\x06insert\x18\x04 \x01(\x0b2 .google.datastore.v1beta3.EntityH\x00\x122\n\x06update\x18\x05 \x01(\x0b2 .google.datastore.v1beta3.EntityH\x00\x122\n\x06upsert\x18\x06 \x01(\x0b2 .google.datastore.v1beta3.EntityH\x00\x12/\n\x06delete\x18\x07 \x01(\x0b2\x1d.google.datastore.v1beta3.KeyH\x00\x12\x16\n\x0cbase_version\x18\x08 \x01(\x03H\x01B\x0b\n\toperationB\x1d\n\x1bconflict_detection_strategy"h\n\x0eMutationResult\x12*\n\x03key\x18\x03 \x01(\x0b2\x1d.google.datastore.v1beta3.Key\x12\x0f\n\x07version\x18\x04 \x01(\x03\x12\x19\n\x11conflict_detected\x18\x05 \x01(\x08"\xda\x01\n\x0bReadOptions\x12Q\n\x10read_consistency\x18\x01 \x01(\x0e25.google.datastore.v1beta3.ReadOptions.ReadConsistencyH\x00\x12\x15\n\x0btransaction\x18\x02 \x01(\x0cH\x00"M\n\x0fReadConsistency\x12 \n\x1cREAD_CONSISTENCY_UNSPECIFIED\x10\x00\x12\n\n\x06STRONG\x10\x01\x12\x0c\n\x08EVENTUAL\x10\x02B\x12\n\x10consistency_type"\xed\x01\n\x12TransactionOptions\x12L\n\nread_write\x18\x01 \x01(\x0b26.google.datastore.v1beta3.TransactionOptions.ReadWriteH\x00\x12J\n\tread_only\x18\x02 \x01(\x0b25.google.datastore.v1beta3.TransactionOptions.ReadOnlyH\x00\x1a)\n\tReadWrite\x12\x1c\n\x14previous_transaction\x18\x01 \x01(\x0c\x1a\n\n\x08ReadOnlyB\x06\n\x04mode2\xd7\x08\n\tDatastore\x12\x8d\x01\n\x06Lookup\x12\'.google.datastore.v1beta3.LookupRequest\x1a(.google.datastore.v1beta3.LookupResponse"0\x82\xd3\xe4\x93\x02*"%/v1beta3/projects/{project_id}:lookup:\x01*\x12\x95\x01\n\x08RunQuery\x12).google.datastore.v1beta3.RunQueryRequest\x1a*.google.datastore.v1beta3.RunQueryResponse"2\x82\xd3\xe4\x93\x02,"\'/v1beta3/projects/{project_id}:runQuery:\x01*\x12\xb5\x01\n\x10BeginTransaction\x121.google.datastore.v1beta3.BeginTransactionRequest\x1a2.google.datastore.v1beta3.BeginTransactionResponse":\x82\xd3\xe4\x93\x024"//v1beta3/projects/{project_id}:beginTransaction:\x01*\x12\x8d\x01\n\x06Commit\x12\'.google.datastore.v1beta3.CommitRequest\x1a(.google.datastore.v1beta3.CommitResponse"0\x82\xd3\xe4\x93\x02*"%/v1beta3/projects/{project_id}:commit:\x01*\x12\x95\x01\n\x08Rollback\x12).google.datastore.v1beta3.RollbackRequest\x1a*.google.datastore.v1beta3.RollbackResponse"2\x82\xd3\xe4\x93\x02,"\'/v1beta3/projects/{project_id}:rollback:\x01*\x12\xa1\x01\n\x0bAllocateIds\x12,.google.datastore.v1beta3.AllocateIdsRequest\x1a-.google.datastore.v1beta3.AllocateIdsResponse"5\x82\xd3\xe4\x93\x02/"*/v1beta3/projects/{project_id}:allocateIds:\x01*\x12\x9d\x01\n\nReserveIds\x12+.google.datastore.v1beta3.ReserveIdsRequest\x1a,.google.datastore.v1beta3.ReserveIdsResponse"4\x82\xd3\xe4\x93\x02.")/v1beta3/projects/{project_id}:reserveIds:\x01*B\xd8\x01\n\x1ccom.google.datastore.v1beta3B\x0eDatastoreProtoP\x01Z@cloud.google.com/go/datastore/apiv1beta3/datastorepb;datastorepb\xaa\x02\x1eGoogle.Cloud.Datastore.V1Beta3\xca\x02\x1eGoogle\\Cloud\\Datastore\\V1beta3\xea\x02!Google::Cloud::Datastore::V1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.datastore.v1beta3.datastore_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.datastore.v1beta3B\x0eDatastoreProtoP\x01Z@cloud.google.com/go/datastore/apiv1beta3/datastorepb;datastorepb\xaa\x02\x1eGoogle.Cloud.Datastore.V1Beta3\xca\x02\x1eGoogle\\Cloud\\Datastore\\V1beta3\xea\x02!Google::Cloud::Datastore::V1beta3'
    _globals['_DATASTORE'].methods_by_name['Lookup']._loaded_options = None
    _globals['_DATASTORE'].methods_by_name['Lookup']._serialized_options = b'\x82\xd3\xe4\x93\x02*"%/v1beta3/projects/{project_id}:lookup:\x01*'
    _globals['_DATASTORE'].methods_by_name['RunQuery']._loaded_options = None
    _globals['_DATASTORE'].methods_by_name['RunQuery']._serialized_options = b'\x82\xd3\xe4\x93\x02,"\'/v1beta3/projects/{project_id}:runQuery:\x01*'
    _globals['_DATASTORE'].methods_by_name['BeginTransaction']._loaded_options = None
    _globals['_DATASTORE'].methods_by_name['BeginTransaction']._serialized_options = b'\x82\xd3\xe4\x93\x024"//v1beta3/projects/{project_id}:beginTransaction:\x01*'
    _globals['_DATASTORE'].methods_by_name['Commit']._loaded_options = None
    _globals['_DATASTORE'].methods_by_name['Commit']._serialized_options = b'\x82\xd3\xe4\x93\x02*"%/v1beta3/projects/{project_id}:commit:\x01*'
    _globals['_DATASTORE'].methods_by_name['Rollback']._loaded_options = None
    _globals['_DATASTORE'].methods_by_name['Rollback']._serialized_options = b'\x82\xd3\xe4\x93\x02,"\'/v1beta3/projects/{project_id}:rollback:\x01*'
    _globals['_DATASTORE'].methods_by_name['AllocateIds']._loaded_options = None
    _globals['_DATASTORE'].methods_by_name['AllocateIds']._serialized_options = b'\x82\xd3\xe4\x93\x02/"*/v1beta3/projects/{project_id}:allocateIds:\x01*'
    _globals['_DATASTORE'].methods_by_name['ReserveIds']._loaded_options = None
    _globals['_DATASTORE'].methods_by_name['ReserveIds']._serialized_options = b'\x82\xd3\xe4\x93\x02.")/v1beta3/projects/{project_id}:reserveIds:\x01*'
    _globals['_LOOKUPREQUEST']._serialized_start = 178
    _globals['_LOOKUPREQUEST']._serialized_end = 319
    _globals['_LOOKUPRESPONSE']._serialized_start = 322
    _globals['_LOOKUPRESPONSE']._serialized_end = 499
    _globals['_RUNQUERYREQUEST']._serialized_start = 502
    _globals['_RUNQUERYREQUEST']._serialized_end = 782
    _globals['_RUNQUERYRESPONSE']._serialized_start = 784
    _globals['_RUNQUERYRESPONSE']._serialized_end = 909
    _globals['_BEGINTRANSACTIONREQUEST']._serialized_start = 911
    _globals['_BEGINTRANSACTIONREQUEST']._serialized_end = 1031
    _globals['_BEGINTRANSACTIONRESPONSE']._serialized_start = 1033
    _globals['_BEGINTRANSACTIONRESPONSE']._serialized_end = 1080
    _globals['_ROLLBACKREQUEST']._serialized_start = 1082
    _globals['_ROLLBACKREQUEST']._serialized_end = 1140
    _globals['_ROLLBACKRESPONSE']._serialized_start = 1142
    _globals['_ROLLBACKRESPONSE']._serialized_end = 1160
    _globals['_COMMITREQUEST']._serialized_start = 1163
    _globals['_COMMITREQUEST']._serialized_end = 1432
    _globals['_COMMITREQUEST_MODE']._serialized_start = 1338
    _globals['_COMMITREQUEST_MODE']._serialized_end = 1408
    _globals['_COMMITRESPONSE']._serialized_start = 1434
    _globals['_COMMITRESPONSE']._serialized_end = 1541
    _globals['_ALLOCATEIDSREQUEST']._serialized_start = 1543
    _globals['_ALLOCATEIDSREQUEST']._serialized_end = 1628
    _globals['_ALLOCATEIDSRESPONSE']._serialized_start = 1630
    _globals['_ALLOCATEIDSRESPONSE']._serialized_end = 1696
    _globals['_RESERVEIDSREQUEST']._serialized_start = 1698
    _globals['_RESERVEIDSREQUEST']._serialized_end = 1803
    _globals['_RESERVEIDSRESPONSE']._serialized_start = 1805
    _globals['_RESERVEIDSRESPONSE']._serialized_end = 1825
    _globals['_MUTATION']._serialized_start = 1828
    _globals['_MUTATION']._serialized_end = 2111
    _globals['_MUTATIONRESULT']._serialized_start = 2113
    _globals['_MUTATIONRESULT']._serialized_end = 2217
    _globals['_READOPTIONS']._serialized_start = 2220
    _globals['_READOPTIONS']._serialized_end = 2438
    _globals['_READOPTIONS_READCONSISTENCY']._serialized_start = 2341
    _globals['_READOPTIONS_READCONSISTENCY']._serialized_end = 2418
    _globals['_TRANSACTIONOPTIONS']._serialized_start = 2441
    _globals['_TRANSACTIONOPTIONS']._serialized_end = 2678
    _globals['_TRANSACTIONOPTIONS_READWRITE']._serialized_start = 2617
    _globals['_TRANSACTIONOPTIONS_READWRITE']._serialized_end = 2658
    _globals['_TRANSACTIONOPTIONS_READONLY']._serialized_start = 2660
    _globals['_TRANSACTIONOPTIONS_READONLY']._serialized_end = 2670
    _globals['_DATASTORE']._serialized_start = 2681
    _globals['_DATASTORE']._serialized_end = 3792