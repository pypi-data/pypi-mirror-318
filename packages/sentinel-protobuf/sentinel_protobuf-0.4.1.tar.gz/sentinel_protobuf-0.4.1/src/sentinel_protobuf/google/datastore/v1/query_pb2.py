"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/datastore/v1/query.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.datastore.v1 import entity_pb2 as google_dot_datastore_dot_v1_dot_entity__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fgoogle/datastore/v1/query.proto\x12\x13google.datastore.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a google/datastore/v1/entity.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x91\x02\n\x0cEntityResult\x12+\n\x06entity\x18\x01 \x01(\x0b2\x1b.google.datastore.v1.Entity\x12\x0f\n\x07version\x18\x04 \x01(\x03\x12/\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0e\n\x06cursor\x18\x03 \x01(\x0c"Q\n\nResultType\x12\x1b\n\x17RESULT_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04FULL\x10\x01\x12\x0e\n\nPROJECTION\x10\x02\x12\x0c\n\x08KEY_ONLY\x10\x03"\xaf\x03\n\x05Query\x123\n\nprojection\x18\x02 \x03(\x0b2\x1f.google.datastore.v1.Projection\x121\n\x04kind\x18\x03 \x03(\x0b2#.google.datastore.v1.KindExpression\x12+\n\x06filter\x18\x04 \x01(\x0b2\x1b.google.datastore.v1.Filter\x121\n\x05order\x18\x05 \x03(\x0b2".google.datastore.v1.PropertyOrder\x12;\n\x0bdistinct_on\x18\x06 \x03(\x0b2&.google.datastore.v1.PropertyReference\x12\x14\n\x0cstart_cursor\x18\x07 \x01(\x0c\x12\x12\n\nend_cursor\x18\x08 \x01(\x0c\x12\x0e\n\x06offset\x18\n \x01(\x05\x12*\n\x05limit\x18\x0c \x01(\x0b2\x1b.google.protobuf.Int32Value\x12;\n\x0cfind_nearest\x18\r \x01(\x0b2 .google.datastore.v1.FindNearestB\x03\xe0A\x01"\xe4\x04\n\x10AggregationQuery\x122\n\x0cnested_query\x18\x01 \x01(\x0b2\x1a.google.datastore.v1.QueryH\x00\x12L\n\x0caggregations\x18\x03 \x03(\x0b21.google.datastore.v1.AggregationQuery.AggregationB\x03\xe0A\x01\x1a\xbf\x03\n\x0bAggregation\x12H\n\x05count\x18\x01 \x01(\x0b27.google.datastore.v1.AggregationQuery.Aggregation.CountH\x00\x12D\n\x03sum\x18\x02 \x01(\x0b25.google.datastore.v1.AggregationQuery.Aggregation.SumH\x00\x12D\n\x03avg\x18\x03 \x01(\x0b25.google.datastore.v1.AggregationQuery.Aggregation.AvgH\x00\x12\x12\n\x05alias\x18\x07 \x01(\tB\x03\xe0A\x01\x1a8\n\x05Count\x12/\n\x05up_to\x18\x01 \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x01\x1a?\n\x03Sum\x128\n\x08property\x18\x01 \x01(\x0b2&.google.datastore.v1.PropertyReference\x1a?\n\x03Avg\x128\n\x08property\x18\x01 \x01(\x0b2&.google.datastore.v1.PropertyReferenceB\n\n\x08operatorB\x0c\n\nquery_type"\x1e\n\x0eKindExpression\x12\x0c\n\x04name\x18\x01 \x01(\t"!\n\x11PropertyReference\x12\x0c\n\x04name\x18\x02 \x01(\t"F\n\nProjection\x128\n\x08property\x18\x01 \x01(\x0b2&.google.datastore.v1.PropertyReference"\xd1\x01\n\rPropertyOrder\x128\n\x08property\x18\x01 \x01(\x0b2&.google.datastore.v1.PropertyReference\x12?\n\tdirection\x18\x02 \x01(\x0e2,.google.datastore.v1.PropertyOrder.Direction"E\n\tDirection\x12\x19\n\x15DIRECTION_UNSPECIFIED\x10\x00\x12\r\n\tASCENDING\x10\x01\x12\x0e\n\nDESCENDING\x10\x02"\x99\x01\n\x06Filter\x12@\n\x10composite_filter\x18\x01 \x01(\x0b2$.google.datastore.v1.CompositeFilterH\x00\x12>\n\x0fproperty_filter\x18\x02 \x01(\x0b2#.google.datastore.v1.PropertyFilterH\x00B\r\n\x0bfilter_type"\xb1\x01\n\x0fCompositeFilter\x129\n\x02op\x18\x01 \x01(\x0e2-.google.datastore.v1.CompositeFilter.Operator\x12,\n\x07filters\x18\x02 \x03(\x0b2\x1b.google.datastore.v1.Filter"5\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\x07\n\x03AND\x10\x01\x12\x06\n\x02OR\x10\x02"\xea\x02\n\x0ePropertyFilter\x128\n\x08property\x18\x01 \x01(\x0b2&.google.datastore.v1.PropertyReference\x128\n\x02op\x18\x02 \x01(\x0e2,.google.datastore.v1.PropertyFilter.Operator\x12)\n\x05value\x18\x03 \x01(\x0b2\x1a.google.datastore.v1.Value"\xb8\x01\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\r\n\tLESS_THAN\x10\x01\x12\x16\n\x12LESS_THAN_OR_EQUAL\x10\x02\x12\x10\n\x0cGREATER_THAN\x10\x03\x12\x19\n\x15GREATER_THAN_OR_EQUAL\x10\x04\x12\t\n\x05EQUAL\x10\x05\x12\x06\n\x02IN\x10\x06\x12\r\n\tNOT_EQUAL\x10\t\x12\x10\n\x0cHAS_ANCESTOR\x10\x0b\x12\n\n\x06NOT_IN\x10\r"\xd3\x03\n\x0bFindNearest\x12D\n\x0fvector_property\x18\x01 \x01(\x0b2&.google.datastore.v1.PropertyReferenceB\x03\xe0A\x02\x125\n\x0cquery_vector\x18\x02 \x01(\x0b2\x1a.google.datastore.v1.ValueB\x03\xe0A\x02\x12O\n\x10distance_measure\x18\x03 \x01(\x0e20.google.datastore.v1.FindNearest.DistanceMeasureB\x03\xe0A\x02\x12/\n\x05limit\x18\x04 \x01(\x0b2\x1b.google.protobuf.Int32ValueB\x03\xe0A\x02\x12%\n\x18distance_result_property\x18\x05 \x01(\tB\x03\xe0A\x01\x12=\n\x12distance_threshold\x18\x06 \x01(\x0b2\x1c.google.protobuf.DoubleValueB\x03\xe0A\x01"_\n\x0fDistanceMeasure\x12 \n\x1cDISTANCE_MEASURE_UNSPECIFIED\x10\x00\x12\r\n\tEUCLIDEAN\x10\x01\x12\n\n\x06COSINE\x10\x02\x12\x0f\n\x0bDOT_PRODUCT\x10\x03"\xa5\x02\n\x08GqlQuery\x12\x14\n\x0cquery_string\x18\x01 \x01(\t\x12\x16\n\x0eallow_literals\x18\x02 \x01(\x08\x12H\n\x0enamed_bindings\x18\x05 \x03(\x0b20.google.datastore.v1.GqlQuery.NamedBindingsEntry\x12C\n\x13positional_bindings\x18\x04 \x03(\x0b2&.google.datastore.v1.GqlQueryParameter\x1a\\\n\x12NamedBindingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x125\n\x05value\x18\x02 \x01(\x0b2&.google.datastore.v1.GqlQueryParameter:\x028\x01"d\n\x11GqlQueryParameter\x12+\n\x05value\x18\x02 \x01(\x0b2\x1a.google.datastore.v1.ValueH\x00\x12\x10\n\x06cursor\x18\x03 \x01(\x0cH\x00B\x10\n\x0eparameter_type"\x8d\x04\n\x10QueryResultBatch\x12\x17\n\x0fskipped_results\x18\x06 \x01(\x05\x12\x16\n\x0eskipped_cursor\x18\x03 \x01(\x0c\x12H\n\x12entity_result_type\x18\x01 \x01(\x0e2,.google.datastore.v1.EntityResult.ResultType\x129\n\x0eentity_results\x18\x02 \x03(\x0b2!.google.datastore.v1.EntityResult\x12\x12\n\nend_cursor\x18\x04 \x01(\x0c\x12K\n\x0cmore_results\x18\x05 \x01(\x0e25.google.datastore.v1.QueryResultBatch.MoreResultsType\x12\x18\n\x10snapshot_version\x18\x07 \x01(\x03\x12-\n\tread_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x98\x01\n\x0fMoreResultsType\x12!\n\x1dMORE_RESULTS_TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cNOT_FINISHED\x10\x01\x12\x1c\n\x18MORE_RESULTS_AFTER_LIMIT\x10\x02\x12\x1d\n\x19MORE_RESULTS_AFTER_CURSOR\x10\x04\x12\x13\n\x0fNO_MORE_RESULTS\x10\x03B\xbb\x01\n\x17com.google.datastore.v1B\nQueryProtoP\x01Z;cloud.google.com/go/datastore/apiv1/datastorepb;datastorepb\xaa\x02\x19Google.Cloud.Datastore.V1\xca\x02\x19Google\\Cloud\\Datastore\\V1\xea\x02\x1cGoogle::Cloud::Datastore::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.datastore.v1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.datastore.v1B\nQueryProtoP\x01Z;cloud.google.com/go/datastore/apiv1/datastorepb;datastorepb\xaa\x02\x19Google.Cloud.Datastore.V1\xca\x02\x19Google\\Cloud\\Datastore\\V1\xea\x02\x1cGoogle::Cloud::Datastore::V1'
    _globals['_QUERY'].fields_by_name['find_nearest']._loaded_options = None
    _globals['_QUERY'].fields_by_name['find_nearest']._serialized_options = b'\xe0A\x01'
    _globals['_AGGREGATIONQUERY_AGGREGATION_COUNT'].fields_by_name['up_to']._loaded_options = None
    _globals['_AGGREGATIONQUERY_AGGREGATION_COUNT'].fields_by_name['up_to']._serialized_options = b'\xe0A\x01'
    _globals['_AGGREGATIONQUERY_AGGREGATION'].fields_by_name['alias']._loaded_options = None
    _globals['_AGGREGATIONQUERY_AGGREGATION'].fields_by_name['alias']._serialized_options = b'\xe0A\x01'
    _globals['_AGGREGATIONQUERY'].fields_by_name['aggregations']._loaded_options = None
    _globals['_AGGREGATIONQUERY'].fields_by_name['aggregations']._serialized_options = b'\xe0A\x01'
    _globals['_FINDNEAREST'].fields_by_name['vector_property']._loaded_options = None
    _globals['_FINDNEAREST'].fields_by_name['vector_property']._serialized_options = b'\xe0A\x02'
    _globals['_FINDNEAREST'].fields_by_name['query_vector']._loaded_options = None
    _globals['_FINDNEAREST'].fields_by_name['query_vector']._serialized_options = b'\xe0A\x02'
    _globals['_FINDNEAREST'].fields_by_name['distance_measure']._loaded_options = None
    _globals['_FINDNEAREST'].fields_by_name['distance_measure']._serialized_options = b'\xe0A\x02'
    _globals['_FINDNEAREST'].fields_by_name['limit']._loaded_options = None
    _globals['_FINDNEAREST'].fields_by_name['limit']._serialized_options = b'\xe0A\x02'
    _globals['_FINDNEAREST'].fields_by_name['distance_result_property']._loaded_options = None
    _globals['_FINDNEAREST'].fields_by_name['distance_result_property']._serialized_options = b'\xe0A\x01'
    _globals['_FINDNEAREST'].fields_by_name['distance_threshold']._loaded_options = None
    _globals['_FINDNEAREST'].fields_by_name['distance_threshold']._serialized_options = b'\xe0A\x01'
    _globals['_GQLQUERY_NAMEDBINDINGSENTRY']._loaded_options = None
    _globals['_GQLQUERY_NAMEDBINDINGSENTRY']._serialized_options = b'8\x01'
    _globals['_ENTITYRESULT']._serialized_start = 189
    _globals['_ENTITYRESULT']._serialized_end = 462
    _globals['_ENTITYRESULT_RESULTTYPE']._serialized_start = 381
    _globals['_ENTITYRESULT_RESULTTYPE']._serialized_end = 462
    _globals['_QUERY']._serialized_start = 465
    _globals['_QUERY']._serialized_end = 896
    _globals['_AGGREGATIONQUERY']._serialized_start = 899
    _globals['_AGGREGATIONQUERY']._serialized_end = 1511
    _globals['_AGGREGATIONQUERY_AGGREGATION']._serialized_start = 1050
    _globals['_AGGREGATIONQUERY_AGGREGATION']._serialized_end = 1497
    _globals['_AGGREGATIONQUERY_AGGREGATION_COUNT']._serialized_start = 1299
    _globals['_AGGREGATIONQUERY_AGGREGATION_COUNT']._serialized_end = 1355
    _globals['_AGGREGATIONQUERY_AGGREGATION_SUM']._serialized_start = 1357
    _globals['_AGGREGATIONQUERY_AGGREGATION_SUM']._serialized_end = 1420
    _globals['_AGGREGATIONQUERY_AGGREGATION_AVG']._serialized_start = 1422
    _globals['_AGGREGATIONQUERY_AGGREGATION_AVG']._serialized_end = 1485
    _globals['_KINDEXPRESSION']._serialized_start = 1513
    _globals['_KINDEXPRESSION']._serialized_end = 1543
    _globals['_PROPERTYREFERENCE']._serialized_start = 1545
    _globals['_PROPERTYREFERENCE']._serialized_end = 1578
    _globals['_PROJECTION']._serialized_start = 1580
    _globals['_PROJECTION']._serialized_end = 1650
    _globals['_PROPERTYORDER']._serialized_start = 1653
    _globals['_PROPERTYORDER']._serialized_end = 1862
    _globals['_PROPERTYORDER_DIRECTION']._serialized_start = 1793
    _globals['_PROPERTYORDER_DIRECTION']._serialized_end = 1862
    _globals['_FILTER']._serialized_start = 1865
    _globals['_FILTER']._serialized_end = 2018
    _globals['_COMPOSITEFILTER']._serialized_start = 2021
    _globals['_COMPOSITEFILTER']._serialized_end = 2198
    _globals['_COMPOSITEFILTER_OPERATOR']._serialized_start = 2145
    _globals['_COMPOSITEFILTER_OPERATOR']._serialized_end = 2198
    _globals['_PROPERTYFILTER']._serialized_start = 2201
    _globals['_PROPERTYFILTER']._serialized_end = 2563
    _globals['_PROPERTYFILTER_OPERATOR']._serialized_start = 2379
    _globals['_PROPERTYFILTER_OPERATOR']._serialized_end = 2563
    _globals['_FINDNEAREST']._serialized_start = 2566
    _globals['_FINDNEAREST']._serialized_end = 3033
    _globals['_FINDNEAREST_DISTANCEMEASURE']._serialized_start = 2938
    _globals['_FINDNEAREST_DISTANCEMEASURE']._serialized_end = 3033
    _globals['_GQLQUERY']._serialized_start = 3036
    _globals['_GQLQUERY']._serialized_end = 3329
    _globals['_GQLQUERY_NAMEDBINDINGSENTRY']._serialized_start = 3237
    _globals['_GQLQUERY_NAMEDBINDINGSENTRY']._serialized_end = 3329
    _globals['_GQLQUERYPARAMETER']._serialized_start = 3331
    _globals['_GQLQUERYPARAMETER']._serialized_end = 3431
    _globals['_QUERYRESULTBATCH']._serialized_start = 3434
    _globals['_QUERYRESULTBATCH']._serialized_end = 3959
    _globals['_QUERYRESULTBATCH_MORERESULTSTYPE']._serialized_start = 3807
    _globals['_QUERYRESULTBATCH_MORERESULTSTYPE']._serialized_end = 3959