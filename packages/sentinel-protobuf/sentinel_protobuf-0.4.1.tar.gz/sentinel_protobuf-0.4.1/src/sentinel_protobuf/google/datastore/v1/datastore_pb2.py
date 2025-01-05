"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/datastore/v1/datastore.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import routing_pb2 as google_dot_api_dot_routing__pb2
from ....google.datastore.v1 import aggregation_result_pb2 as google_dot_datastore_dot_v1_dot_aggregation__result__pb2
from ....google.datastore.v1 import entity_pb2 as google_dot_datastore_dot_v1_dot_entity__pb2
from ....google.datastore.v1 import query_pb2 as google_dot_datastore_dot_v1_dot_query__pb2
from ....google.datastore.v1 import query_profile_pb2 as google_dot_datastore_dot_v1_dot_query__profile__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/datastore/v1/datastore.proto\x12\x13google.datastore.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x18google/api/routing.proto\x1a,google/datastore/v1/aggregation_result.proto\x1a google/datastore/v1/entity.proto\x1a\x1fgoogle/datastore/v1/query.proto\x1a\'google/datastore/v1/query_profile.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xdc\x01\n\rLookupRequest\x12\x17\n\nproject_id\x18\x08 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdatabase_id\x18\t \x01(\t\x126\n\x0cread_options\x18\x01 \x01(\x0b2 .google.datastore.v1.ReadOptions\x12+\n\x04keys\x18\x03 \x03(\x0b2\x18.google.datastore.v1.KeyB\x03\xe0A\x02\x128\n\rproperty_mask\x18\x05 \x01(\x0b2!.google.datastore.v1.PropertyMask"\xe6\x01\n\x0eLookupResponse\x120\n\x05found\x18\x01 \x03(\x0b2!.google.datastore.v1.EntityResult\x122\n\x07missing\x18\x02 \x03(\x0b2!.google.datastore.v1.EntityResult\x12*\n\x08deferred\x18\x03 \x03(\x0b2\x18.google.datastore.v1.Key\x12\x13\n\x0btransaction\x18\x05 \x01(\x0c\x12-\n\tread_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x9b\x03\n\x0fRunQueryRequest\x12\x17\n\nproject_id\x18\x08 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdatabase_id\x18\t \x01(\t\x126\n\x0cpartition_id\x18\x02 \x01(\x0b2 .google.datastore.v1.PartitionId\x126\n\x0cread_options\x18\x01 \x01(\x0b2 .google.datastore.v1.ReadOptions\x12+\n\x05query\x18\x03 \x01(\x0b2\x1a.google.datastore.v1.QueryH\x00\x122\n\tgql_query\x18\x07 \x01(\x0b2\x1d.google.datastore.v1.GqlQueryH\x00\x128\n\rproperty_mask\x18\n \x01(\x0b2!.google.datastore.v1.PropertyMask\x12A\n\x0fexplain_options\x18\x0c \x01(\x0b2#.google.datastore.v1.ExplainOptionsB\x03\xe0A\x01B\x0c\n\nquery_type"\xc6\x01\n\x10RunQueryResponse\x124\n\x05batch\x18\x01 \x01(\x0b2%.google.datastore.v1.QueryResultBatch\x12)\n\x05query\x18\x02 \x01(\x0b2\x1a.google.datastore.v1.Query\x12\x13\n\x0btransaction\x18\x05 \x01(\x0c\x12<\n\x0fexplain_metrics\x18\t \x01(\x0b2#.google.datastore.v1.ExplainMetrics"\x83\x03\n\x1aRunAggregationQueryRequest\x12\x17\n\nproject_id\x18\x08 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdatabase_id\x18\t \x01(\t\x126\n\x0cpartition_id\x18\x02 \x01(\x0b2 .google.datastore.v1.PartitionId\x126\n\x0cread_options\x18\x01 \x01(\x0b2 .google.datastore.v1.ReadOptions\x12B\n\x11aggregation_query\x18\x03 \x01(\x0b2%.google.datastore.v1.AggregationQueryH\x00\x122\n\tgql_query\x18\x07 \x01(\x0b2\x1d.google.datastore.v1.GqlQueryH\x00\x12A\n\x0fexplain_options\x18\x0b \x01(\x0b2#.google.datastore.v1.ExplainOptionsB\x03\xe0A\x01B\x0c\n\nquery_type"\xe2\x01\n\x1bRunAggregationQueryResponse\x12:\n\x05batch\x18\x01 \x01(\x0b2+.google.datastore.v1.AggregationResultBatch\x124\n\x05query\x18\x02 \x01(\x0b2%.google.datastore.v1.AggregationQuery\x12\x13\n\x0btransaction\x18\x05 \x01(\x0c\x12<\n\x0fexplain_metrics\x18\t \x01(\x0b2#.google.datastore.v1.ExplainMetrics"\x8d\x01\n\x17BeginTransactionRequest\x12\x17\n\nproject_id\x18\x08 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdatabase_id\x18\t \x01(\t\x12D\n\x13transaction_options\x18\n \x01(\x0b2\'.google.datastore.v1.TransactionOptions"/\n\x18BeginTransactionResponse\x12\x13\n\x0btransaction\x18\x01 \x01(\x0c"Y\n\x0fRollbackRequest\x12\x17\n\nproject_id\x18\x08 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdatabase_id\x18\t \x01(\t\x12\x18\n\x0btransaction\x18\x01 \x01(\x0cB\x03\xe0A\x02"\x12\n\x10RollbackResponse"\xe8\x02\n\rCommitRequest\x12\x17\n\nproject_id\x18\x08 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdatabase_id\x18\t \x01(\t\x125\n\x04mode\x18\x05 \x01(\x0e2\'.google.datastore.v1.CommitRequest.Mode\x12\x15\n\x0btransaction\x18\x01 \x01(\x0cH\x00\x12I\n\x16single_use_transaction\x18\n \x01(\x0b2\'.google.datastore.v1.TransactionOptionsH\x00\x120\n\tmutations\x18\x06 \x03(\x0b2\x1d.google.datastore.v1.Mutation"F\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x11\n\rTRANSACTIONAL\x10\x01\x12\x15\n\x11NON_TRANSACTIONAL\x10\x02B\x16\n\x14transaction_selector"\x97\x01\n\x0eCommitResponse\x12=\n\x10mutation_results\x18\x03 \x03(\x0b2#.google.datastore.v1.MutationResult\x12\x15\n\rindex_updates\x18\x04 \x01(\x05\x12/\n\x0bcommit_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.Timestamp"o\n\x12AllocateIdsRequest\x12\x17\n\nproject_id\x18\x08 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdatabase_id\x18\t \x01(\t\x12+\n\x04keys\x18\x01 \x03(\x0b2\x18.google.datastore.v1.KeyB\x03\xe0A\x02"=\n\x13AllocateIdsResponse\x12&\n\x04keys\x18\x01 \x03(\x0b2\x18.google.datastore.v1.Key"n\n\x11ReserveIdsRequest\x12\x17\n\nproject_id\x18\x08 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdatabase_id\x18\t \x01(\t\x12+\n\x04keys\x18\x01 \x03(\x0b2\x18.google.datastore.v1.KeyB\x03\xe0A\x02"\x14\n\x12ReserveIdsResponse"\xf2\x04\n\x08Mutation\x12-\n\x06insert\x18\x04 \x01(\x0b2\x1b.google.datastore.v1.EntityH\x00\x12-\n\x06update\x18\x05 \x01(\x0b2\x1b.google.datastore.v1.EntityH\x00\x12-\n\x06upsert\x18\x06 \x01(\x0b2\x1b.google.datastore.v1.EntityH\x00\x12*\n\x06delete\x18\x07 \x01(\x0b2\x18.google.datastore.v1.KeyH\x00\x12\x16\n\x0cbase_version\x18\x08 \x01(\x03H\x01\x121\n\x0bupdate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampH\x01\x12^\n\x1cconflict_resolution_strategy\x18\n \x01(\x0e28.google.datastore.v1.Mutation.ConflictResolutionStrategy\x128\n\rproperty_mask\x18\t \x01(\x0b2!.google.datastore.v1.PropertyMask\x12H\n\x13property_transforms\x18\x0c \x03(\x0b2&.google.datastore.v1.PropertyTransformB\x03\xe0A\x01"R\n\x1aConflictResolutionStrategy\x12\x18\n\x14STRATEGY_UNSPECIFIED\x10\x00\x12\x10\n\x0cSERVER_VALUE\x10\x01\x12\x08\n\x04FAIL\x10\x03B\x0b\n\toperationB\x1d\n\x1bconflict_detection_strategy"\xe3\x03\n\x11PropertyTransform\x12\x15\n\x08property\x18\x01 \x01(\tB\x03\xe0A\x01\x12Q\n\x13set_to_server_value\x18\x02 \x01(\x0e22.google.datastore.v1.PropertyTransform.ServerValueH\x00\x12/\n\tincrement\x18\x03 \x01(\x0b2\x1a.google.datastore.v1.ValueH\x00\x12-\n\x07maximum\x18\x04 \x01(\x0b2\x1a.google.datastore.v1.ValueH\x00\x12-\n\x07minimum\x18\x05 \x01(\x0b2\x1a.google.datastore.v1.ValueH\x00\x12B\n\x17append_missing_elements\x18\x06 \x01(\x0b2\x1f.google.datastore.v1.ArrayValueH\x00\x12@\n\x15remove_all_from_array\x18\x07 \x01(\x0b2\x1f.google.datastore.v1.ArrayValueH\x00"=\n\x0bServerValue\x12\x1c\n\x18SERVER_VALUE_UNSPECIFIED\x10\x00\x12\x10\n\x0cREQUEST_TIME\x10\x01B\x10\n\x0etransform_type"\xfc\x01\n\x0eMutationResult\x12%\n\x03key\x18\x03 \x01(\x0b2\x18.google.datastore.v1.Key\x12\x0f\n\x07version\x18\x04 \x01(\x03\x12/\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x19\n\x11conflict_detected\x18\x05 \x01(\x08\x125\n\x11transform_results\x18\x08 \x03(\x0b2\x1a.google.datastore.v1.Value"\x1d\n\x0cPropertyMask\x12\r\n\x05paths\x18\x01 \x03(\t"\xca\x02\n\x0bReadOptions\x12L\n\x10read_consistency\x18\x01 \x01(\x0e20.google.datastore.v1.ReadOptions.ReadConsistencyH\x00\x12\x15\n\x0btransaction\x18\x02 \x01(\x0cH\x00\x12B\n\x0fnew_transaction\x18\x03 \x01(\x0b2\'.google.datastore.v1.TransactionOptionsH\x00\x12/\n\tread_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00"M\n\x0fReadConsistency\x12 \n\x1cREAD_CONSISTENCY_UNSPECIFIED\x10\x00\x12\n\n\x06STRONG\x10\x01\x12\x0c\n\x08EVENTUAL\x10\x02B\x12\n\x10consistency_type"\x92\x02\n\x12TransactionOptions\x12G\n\nread_write\x18\x01 \x01(\x0b21.google.datastore.v1.TransactionOptions.ReadWriteH\x00\x12E\n\tread_only\x18\x02 \x01(\x0b20.google.datastore.v1.TransactionOptions.ReadOnlyH\x00\x1a)\n\tReadWrite\x12\x1c\n\x14previous_transaction\x18\x01 \x01(\x0c\x1a9\n\x08ReadOnly\x12-\n\tread_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x06\n\x04mode2\xe1\r\n\tDatastore\x12\xc0\x01\n\x06Lookup\x12".google.datastore.v1.LookupRequest\x1a#.google.datastore.v1.LookupResponse"m\xdaA\x1cproject_id,read_options,keys\x82\xd3\xe4\x93\x02%" /v1/projects/{project_id}:lookup:\x01*\x8a\xd3\xe4\x93\x02\x1d\x12\x0c\n\nproject_id\x12\r\n\x0bdatabase_id\x12\xa9\x01\n\x08RunQuery\x12$.google.datastore.v1.RunQueryRequest\x1a%.google.datastore.v1.RunQueryResponse"P\x82\xd3\xe4\x93\x02\'""/v1/projects/{project_id}:runQuery:\x01*\x8a\xd3\xe4\x93\x02\x1d\x12\x0c\n\nproject_id\x12\r\n\x0bdatabase_id\x12\xd5\x01\n\x13RunAggregationQuery\x12/.google.datastore.v1.RunAggregationQueryRequest\x1a0.google.datastore.v1.RunAggregationQueryResponse"[\x82\xd3\xe4\x93\x022"-/v1/projects/{project_id}:runAggregationQuery:\x01*\x8a\xd3\xe4\x93\x02\x1d\x12\x0c\n\nproject_id\x12\r\n\x0bdatabase_id\x12\xd6\x01\n\x10BeginTransaction\x12,.google.datastore.v1.BeginTransactionRequest\x1a-.google.datastore.v1.BeginTransactionResponse"e\xdaA\nproject_id\x82\xd3\xe4\x93\x02/"*/v1/projects/{project_id}:beginTransaction:\x01*\x8a\xd3\xe4\x93\x02\x1d\x12\x0c\n\nproject_id\x12\r\n\x0bdatabase_id\x12\xe6\x01\n\x06Commit\x12".google.datastore.v1.CommitRequest\x1a#.google.datastore.v1.CommitResponse"\x92\x01\xdaA%project_id,mode,transaction,mutations\xdaA\x19project_id,mode,mutations\x82\xd3\xe4\x93\x02%" /v1/projects/{project_id}:commit:\x01*\x8a\xd3\xe4\x93\x02\x1d\x12\x0c\n\nproject_id\x12\r\n\x0bdatabase_id\x12\xc2\x01\n\x08Rollback\x12$.google.datastore.v1.RollbackRequest\x1a%.google.datastore.v1.RollbackResponse"i\xdaA\x16project_id,transaction\x82\xd3\xe4\x93\x02\'""/v1/projects/{project_id}:rollback:\x01*\x8a\xd3\xe4\x93\x02\x1d\x12\x0c\n\nproject_id\x12\r\n\x0bdatabase_id\x12\xc7\x01\n\x0bAllocateIds\x12\'.google.datastore.v1.AllocateIdsRequest\x1a(.google.datastore.v1.AllocateIdsResponse"e\xdaA\x0fproject_id,keys\x82\xd3\xe4\x93\x02*"%/v1/projects/{project_id}:allocateIds:\x01*\x8a\xd3\xe4\x93\x02\x1d\x12\x0c\n\nproject_id\x12\r\n\x0bdatabase_id\x12\xc3\x01\n\nReserveIds\x12&.google.datastore.v1.ReserveIdsRequest\x1a\'.google.datastore.v1.ReserveIdsResponse"d\xdaA\x0fproject_id,keys\x82\xd3\xe4\x93\x02)"$/v1/projects/{project_id}:reserveIds:\x01*\x8a\xd3\xe4\x93\x02\x1d\x12\x0c\n\nproject_id\x12\r\n\x0bdatabase_id\x1av\xcaA\x18datastore.googleapis.com\xd2AXhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/datastoreB\xbf\x01\n\x17com.google.datastore.v1B\x0eDatastoreProtoP\x01Z;cloud.google.com/go/datastore/apiv1/datastorepb;datastorepb\xaa\x02\x19Google.Cloud.Datastore.V1\xca\x02\x19Google\\Cloud\\Datastore\\V1\xea\x02\x1cGoogle::Cloud::Datastore::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.datastore.v1.datastore_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.datastore.v1B\x0eDatastoreProtoP\x01Z;cloud.google.com/go/datastore/apiv1/datastorepb;datastorepb\xaa\x02\x19Google.Cloud.Datastore.V1\xca\x02\x19Google\\Cloud\\Datastore\\V1\xea\x02\x1cGoogle::Cloud::Datastore::V1'
    _globals['_LOOKUPREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_LOOKUPREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_LOOKUPREQUEST'].fields_by_name['keys']._loaded_options = None
    _globals['_LOOKUPREQUEST'].fields_by_name['keys']._serialized_options = b'\xe0A\x02'
    _globals['_RUNQUERYREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_RUNQUERYREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_RUNQUERYREQUEST'].fields_by_name['explain_options']._loaded_options = None
    _globals['_RUNQUERYREQUEST'].fields_by_name['explain_options']._serialized_options = b'\xe0A\x01'
    _globals['_RUNAGGREGATIONQUERYREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_RUNAGGREGATIONQUERYREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_RUNAGGREGATIONQUERYREQUEST'].fields_by_name['explain_options']._loaded_options = None
    _globals['_RUNAGGREGATIONQUERYREQUEST'].fields_by_name['explain_options']._serialized_options = b'\xe0A\x01'
    _globals['_BEGINTRANSACTIONREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_BEGINTRANSACTIONREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_ROLLBACKREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_ROLLBACKREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_ROLLBACKREQUEST'].fields_by_name['transaction']._loaded_options = None
    _globals['_ROLLBACKREQUEST'].fields_by_name['transaction']._serialized_options = b'\xe0A\x02'
    _globals['_COMMITREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_COMMITREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_ALLOCATEIDSREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_ALLOCATEIDSREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_ALLOCATEIDSREQUEST'].fields_by_name['keys']._loaded_options = None
    _globals['_ALLOCATEIDSREQUEST'].fields_by_name['keys']._serialized_options = b'\xe0A\x02'
    _globals['_RESERVEIDSREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_RESERVEIDSREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_RESERVEIDSREQUEST'].fields_by_name['keys']._loaded_options = None
    _globals['_RESERVEIDSREQUEST'].fields_by_name['keys']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATION'].fields_by_name['property_transforms']._loaded_options = None
    _globals['_MUTATION'].fields_by_name['property_transforms']._serialized_options = b'\xe0A\x01'
    _globals['_PROPERTYTRANSFORM'].fields_by_name['property']._loaded_options = None
    _globals['_PROPERTYTRANSFORM'].fields_by_name['property']._serialized_options = b'\xe0A\x01'
    _globals['_DATASTORE']._loaded_options = None
    _globals['_DATASTORE']._serialized_options = b'\xcaA\x18datastore.googleapis.com\xd2AXhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/datastore'
    _globals['_DATASTORE'].methods_by_name['Lookup']._loaded_options = None
    _globals['_DATASTORE'].methods_by_name['Lookup']._serialized_options = b'\xdaA\x1cproject_id,read_options,keys\x82\xd3\xe4\x93\x02%" /v1/projects/{project_id}:lookup:\x01*\x8a\xd3\xe4\x93\x02\x1d\x12\x0c\n\nproject_id\x12\r\n\x0bdatabase_id'
    _globals['_DATASTORE'].methods_by_name['RunQuery']._loaded_options = None
    _globals['_DATASTORE'].methods_by_name['RunQuery']._serialized_options = b'\x82\xd3\xe4\x93\x02\'""/v1/projects/{project_id}:runQuery:\x01*\x8a\xd3\xe4\x93\x02\x1d\x12\x0c\n\nproject_id\x12\r\n\x0bdatabase_id'
    _globals['_DATASTORE'].methods_by_name['RunAggregationQuery']._loaded_options = None
    _globals['_DATASTORE'].methods_by_name['RunAggregationQuery']._serialized_options = b'\x82\xd3\xe4\x93\x022"-/v1/projects/{project_id}:runAggregationQuery:\x01*\x8a\xd3\xe4\x93\x02\x1d\x12\x0c\n\nproject_id\x12\r\n\x0bdatabase_id'
    _globals['_DATASTORE'].methods_by_name['BeginTransaction']._loaded_options = None
    _globals['_DATASTORE'].methods_by_name['BeginTransaction']._serialized_options = b'\xdaA\nproject_id\x82\xd3\xe4\x93\x02/"*/v1/projects/{project_id}:beginTransaction:\x01*\x8a\xd3\xe4\x93\x02\x1d\x12\x0c\n\nproject_id\x12\r\n\x0bdatabase_id'
    _globals['_DATASTORE'].methods_by_name['Commit']._loaded_options = None
    _globals['_DATASTORE'].methods_by_name['Commit']._serialized_options = b'\xdaA%project_id,mode,transaction,mutations\xdaA\x19project_id,mode,mutations\x82\xd3\xe4\x93\x02%" /v1/projects/{project_id}:commit:\x01*\x8a\xd3\xe4\x93\x02\x1d\x12\x0c\n\nproject_id\x12\r\n\x0bdatabase_id'
    _globals['_DATASTORE'].methods_by_name['Rollback']._loaded_options = None
    _globals['_DATASTORE'].methods_by_name['Rollback']._serialized_options = b'\xdaA\x16project_id,transaction\x82\xd3\xe4\x93\x02\'""/v1/projects/{project_id}:rollback:\x01*\x8a\xd3\xe4\x93\x02\x1d\x12\x0c\n\nproject_id\x12\r\n\x0bdatabase_id'
    _globals['_DATASTORE'].methods_by_name['AllocateIds']._loaded_options = None
    _globals['_DATASTORE'].methods_by_name['AllocateIds']._serialized_options = b'\xdaA\x0fproject_id,keys\x82\xd3\xe4\x93\x02*"%/v1/projects/{project_id}:allocateIds:\x01*\x8a\xd3\xe4\x93\x02\x1d\x12\x0c\n\nproject_id\x12\r\n\x0bdatabase_id'
    _globals['_DATASTORE'].methods_by_name['ReserveIds']._loaded_options = None
    _globals['_DATASTORE'].methods_by_name['ReserveIds']._serialized_options = b'\xdaA\x0fproject_id,keys\x82\xd3\xe4\x93\x02)"$/v1/projects/{project_id}:reserveIds:\x01*\x8a\xd3\xe4\x93\x02\x1d\x12\x0c\n\nproject_id\x12\r\n\x0bdatabase_id'
    _globals['_LOOKUPREQUEST']._serialized_start = 362
    _globals['_LOOKUPREQUEST']._serialized_end = 582
    _globals['_LOOKUPRESPONSE']._serialized_start = 585
    _globals['_LOOKUPRESPONSE']._serialized_end = 815
    _globals['_RUNQUERYREQUEST']._serialized_start = 818
    _globals['_RUNQUERYREQUEST']._serialized_end = 1229
    _globals['_RUNQUERYRESPONSE']._serialized_start = 1232
    _globals['_RUNQUERYRESPONSE']._serialized_end = 1430
    _globals['_RUNAGGREGATIONQUERYREQUEST']._serialized_start = 1433
    _globals['_RUNAGGREGATIONQUERYREQUEST']._serialized_end = 1820
    _globals['_RUNAGGREGATIONQUERYRESPONSE']._serialized_start = 1823
    _globals['_RUNAGGREGATIONQUERYRESPONSE']._serialized_end = 2049
    _globals['_BEGINTRANSACTIONREQUEST']._serialized_start = 2052
    _globals['_BEGINTRANSACTIONREQUEST']._serialized_end = 2193
    _globals['_BEGINTRANSACTIONRESPONSE']._serialized_start = 2195
    _globals['_BEGINTRANSACTIONRESPONSE']._serialized_end = 2242
    _globals['_ROLLBACKREQUEST']._serialized_start = 2244
    _globals['_ROLLBACKREQUEST']._serialized_end = 2333
    _globals['_ROLLBACKRESPONSE']._serialized_start = 2335
    _globals['_ROLLBACKRESPONSE']._serialized_end = 2353
    _globals['_COMMITREQUEST']._serialized_start = 2356
    _globals['_COMMITREQUEST']._serialized_end = 2716
    _globals['_COMMITREQUEST_MODE']._serialized_start = 2622
    _globals['_COMMITREQUEST_MODE']._serialized_end = 2692
    _globals['_COMMITRESPONSE']._serialized_start = 2719
    _globals['_COMMITRESPONSE']._serialized_end = 2870
    _globals['_ALLOCATEIDSREQUEST']._serialized_start = 2872
    _globals['_ALLOCATEIDSREQUEST']._serialized_end = 2983
    _globals['_ALLOCATEIDSRESPONSE']._serialized_start = 2985
    _globals['_ALLOCATEIDSRESPONSE']._serialized_end = 3046
    _globals['_RESERVEIDSREQUEST']._serialized_start = 3048
    _globals['_RESERVEIDSREQUEST']._serialized_end = 3158
    _globals['_RESERVEIDSRESPONSE']._serialized_start = 3160
    _globals['_RESERVEIDSRESPONSE']._serialized_end = 3180
    _globals['_MUTATION']._serialized_start = 3183
    _globals['_MUTATION']._serialized_end = 3809
    _globals['_MUTATION_CONFLICTRESOLUTIONSTRATEGY']._serialized_start = 3683
    _globals['_MUTATION_CONFLICTRESOLUTIONSTRATEGY']._serialized_end = 3765
    _globals['_PROPERTYTRANSFORM']._serialized_start = 3812
    _globals['_PROPERTYTRANSFORM']._serialized_end = 4295
    _globals['_PROPERTYTRANSFORM_SERVERVALUE']._serialized_start = 4216
    _globals['_PROPERTYTRANSFORM_SERVERVALUE']._serialized_end = 4277
    _globals['_MUTATIONRESULT']._serialized_start = 4298
    _globals['_MUTATIONRESULT']._serialized_end = 4550
    _globals['_PROPERTYMASK']._serialized_start = 4552
    _globals['_PROPERTYMASK']._serialized_end = 4581
    _globals['_READOPTIONS']._serialized_start = 4584
    _globals['_READOPTIONS']._serialized_end = 4914
    _globals['_READOPTIONS_READCONSISTENCY']._serialized_start = 4817
    _globals['_READOPTIONS_READCONSISTENCY']._serialized_end = 4894
    _globals['_TRANSACTIONOPTIONS']._serialized_start = 4917
    _globals['_TRANSACTIONOPTIONS']._serialized_end = 5191
    _globals['_TRANSACTIONOPTIONS_READWRITE']._serialized_start = 5083
    _globals['_TRANSACTIONOPTIONS_READWRITE']._serialized_end = 5124
    _globals['_TRANSACTIONOPTIONS_READONLY']._serialized_start = 5126
    _globals['_TRANSACTIONOPTIONS_READONLY']._serialized_end = 5183
    _globals['_DATASTORE']._serialized_start = 5194
    _globals['_DATASTORE']._serialized_end = 6955