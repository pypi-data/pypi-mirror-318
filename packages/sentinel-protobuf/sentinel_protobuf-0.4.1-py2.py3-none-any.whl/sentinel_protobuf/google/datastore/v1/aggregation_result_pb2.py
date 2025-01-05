"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/datastore/v1/aggregation_result.proto')
_sym_db = _symbol_database.Default()
from ....google.datastore.v1 import entity_pb2 as google_dot_datastore_dot_v1_dot_entity__pb2
from ....google.datastore.v1 import query_pb2 as google_dot_datastore_dot_v1_dot_query__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/datastore/v1/aggregation_result.proto\x12\x13google.datastore.v1\x1a google/datastore/v1/entity.proto\x1a\x1fgoogle/datastore/v1/query.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xca\x01\n\x11AggregationResult\x12]\n\x14aggregate_properties\x18\x02 \x03(\x0b2?.google.datastore.v1.AggregationResult.AggregatePropertiesEntry\x1aV\n\x18AggregatePropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b2\x1a.google.datastore.v1.Value:\x028\x01"\xd9\x01\n\x16AggregationResultBatch\x12C\n\x13aggregation_results\x18\x01 \x03(\x0b2&.google.datastore.v1.AggregationResult\x12K\n\x0cmore_results\x18\x02 \x01(\x0e25.google.datastore.v1.QueryResultBatch.MoreResultsType\x12-\n\tread_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\xc7\x01\n\x17com.google.datastore.v1B\x16AggregationResultProtoP\x01Z;cloud.google.com/go/datastore/apiv1/datastorepb;datastorepb\xaa\x02\x19Google.Cloud.Datastore.V1\xca\x02\x19Google\\Cloud\\Datastore\\V1\xea\x02\x1cGoogle::Cloud::Datastore::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.datastore.v1.aggregation_result_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.datastore.v1B\x16AggregationResultProtoP\x01Z;cloud.google.com/go/datastore/apiv1/datastorepb;datastorepb\xaa\x02\x19Google.Cloud.Datastore.V1\xca\x02\x19Google\\Cloud\\Datastore\\V1\xea\x02\x1cGoogle::Cloud::Datastore::V1'
    _globals['_AGGREGATIONRESULT_AGGREGATEPROPERTIESENTRY']._loaded_options = None
    _globals['_AGGREGATIONRESULT_AGGREGATEPROPERTIESENTRY']._serialized_options = b'8\x01'
    _globals['_AGGREGATIONRESULT']._serialized_start = 170
    _globals['_AGGREGATIONRESULT']._serialized_end = 372
    _globals['_AGGREGATIONRESULT_AGGREGATEPROPERTIESENTRY']._serialized_start = 286
    _globals['_AGGREGATIONRESULT_AGGREGATEPROPERTIESENTRY']._serialized_end = 372
    _globals['_AGGREGATIONRESULTBATCH']._serialized_start = 375
    _globals['_AGGREGATIONRESULTBATCH']._serialized_end = 592