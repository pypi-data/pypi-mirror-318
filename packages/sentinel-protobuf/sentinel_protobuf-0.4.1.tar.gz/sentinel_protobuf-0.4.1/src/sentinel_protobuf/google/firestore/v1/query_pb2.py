"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/v1/query.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.firestore.v1 import document_pb2 as google_dot_firestore_dot_v1_dot_document__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fgoogle/firestore/v1/query.proto\x12\x13google.firestore.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a"google/firestore/v1/document.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xf8\x13\n\x0fStructuredQuery\x12?\n\x06select\x18\x01 \x01(\x0b2/.google.firestore.v1.StructuredQuery.Projection\x12E\n\x04from\x18\x02 \x03(\x0b27.google.firestore.v1.StructuredQuery.CollectionSelector\x12:\n\x05where\x18\x03 \x01(\x0b2+.google.firestore.v1.StructuredQuery.Filter\x12<\n\x08order_by\x18\x04 \x03(\x0b2*.google.firestore.v1.StructuredQuery.Order\x12-\n\x08start_at\x18\x07 \x01(\x0b2\x1b.google.firestore.v1.Cursor\x12+\n\x06end_at\x18\x08 \x01(\x0b2\x1b.google.firestore.v1.Cursor\x12\x0e\n\x06offset\x18\x06 \x01(\x05\x12*\n\x05limit\x18\x05 \x01(\x0b2\x1b.google.protobuf.Int32Value\x12K\n\x0cfind_nearest\x18\t \x01(\x0b20.google.firestore.v1.StructuredQuery.FindNearestB\x03\xe0A\x01\x1aD\n\x12CollectionSelector\x12\x15\n\rcollection_id\x18\x02 \x01(\t\x12\x17\n\x0fall_descendants\x18\x03 \x01(\x08\x1a\xfd\x01\n\x06Filter\x12P\n\x10composite_filter\x18\x01 \x01(\x0b24.google.firestore.v1.StructuredQuery.CompositeFilterH\x00\x12H\n\x0cfield_filter\x18\x02 \x01(\x0b20.google.firestore.v1.StructuredQuery.FieldFilterH\x00\x12H\n\x0cunary_filter\x18\x03 \x01(\x0b20.google.firestore.v1.StructuredQuery.UnaryFilterH\x00B\r\n\x0bfilter_type\x1a\xd1\x01\n\x0fCompositeFilter\x12I\n\x02op\x18\x01 \x01(\x0e2=.google.firestore.v1.StructuredQuery.CompositeFilter.Operator\x12<\n\x07filters\x18\x02 \x03(\x0b2+.google.firestore.v1.StructuredQuery.Filter"5\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\x07\n\x03AND\x10\x01\x12\x06\n\x02OR\x10\x02\x1a\x98\x03\n\x0bFieldFilter\x12B\n\x05field\x18\x01 \x01(\x0b23.google.firestore.v1.StructuredQuery.FieldReference\x12E\n\x02op\x18\x02 \x01(\x0e29.google.firestore.v1.StructuredQuery.FieldFilter.Operator\x12)\n\x05value\x18\x03 \x01(\x0b2\x1a.google.firestore.v1.Value"\xd2\x01\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\r\n\tLESS_THAN\x10\x01\x12\x16\n\x12LESS_THAN_OR_EQUAL\x10\x02\x12\x10\n\x0cGREATER_THAN\x10\x03\x12\x19\n\x15GREATER_THAN_OR_EQUAL\x10\x04\x12\t\n\x05EQUAL\x10\x05\x12\r\n\tNOT_EQUAL\x10\x06\x12\x12\n\x0eARRAY_CONTAINS\x10\x07\x12\x06\n\x02IN\x10\x08\x12\x16\n\x12ARRAY_CONTAINS_ANY\x10\t\x12\n\n\x06NOT_IN\x10\n\x1a\x8a\x02\n\x0bUnaryFilter\x12E\n\x02op\x18\x01 \x01(\x0e29.google.firestore.v1.StructuredQuery.UnaryFilter.Operator\x12D\n\x05field\x18\x02 \x01(\x0b23.google.firestore.v1.StructuredQuery.FieldReferenceH\x00"^\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\n\n\x06IS_NAN\x10\x02\x12\x0b\n\x07IS_NULL\x10\x03\x12\x0e\n\nIS_NOT_NAN\x10\x04\x12\x0f\n\x0bIS_NOT_NULL\x10\x05B\x0e\n\x0coperand_type\x1a\x8e\x01\n\x05Order\x12B\n\x05field\x18\x01 \x01(\x0b23.google.firestore.v1.StructuredQuery.FieldReference\x12A\n\tdirection\x18\x02 \x01(\x0e2..google.firestore.v1.StructuredQuery.Direction\x1a$\n\x0eFieldReference\x12\x12\n\nfield_path\x18\x02 \x01(\t\x1aQ\n\nProjection\x12C\n\x06fields\x18\x02 \x03(\x0b23.google.firestore.v1.StructuredQuery.FieldReference\x1a\xea\x03\n\x0bFindNearest\x12N\n\x0cvector_field\x18\x01 \x01(\x0b23.google.firestore.v1.StructuredQuery.FieldReferenceB\x03\xe0A\x02\x125\n\x0cquery_vector\x18\x02 \x01(\x0b2\x1a.google.firestore.v1.ValueB\x03\xe0A\x02\x12_\n\x10distance_measure\x18\x03 \x01(\x0e2@.google.firestore.v1.StructuredQuery.FindNearest.DistanceMeasureB\x03\xe0A\x02\x12/\n\x05limit\x18\x04 \x01(\x0b2\x1b.google.protobuf.Int32ValueB\x03\xe0A\x02\x12"\n\x15distance_result_field\x18\x05 \x01(\tB\x03\xe0A\x01\x12=\n\x12distance_threshold\x18\x06 \x01(\x0b2\x1c.google.protobuf.DoubleValueB\x03\xe0A\x01"_\n\x0fDistanceMeasure\x12 \n\x1cDISTANCE_MEASURE_UNSPECIFIED\x10\x00\x12\r\n\tEUCLIDEAN\x10\x01\x12\n\n\x06COSINE\x10\x02\x12\x0f\n\x0bDOT_PRODUCT\x10\x03"E\n\tDirection\x12\x19\n\x15DIRECTION_UNSPECIFIED\x10\x00\x12\r\n\tASCENDING\x10\x01\x12\x0e\n\nDESCENDING\x10\x02"\xb8\x05\n\x1aStructuredAggregationQuery\x12@\n\x10structured_query\x18\x01 \x01(\x0b2$.google.firestore.v1.StructuredQueryH\x00\x12V\n\x0caggregations\x18\x03 \x03(\x0b2;.google.firestore.v1.StructuredAggregationQuery.AggregationB\x03\xe0A\x01\x1a\xf1\x03\n\x0bAggregation\x12R\n\x05count\x18\x01 \x01(\x0b2A.google.firestore.v1.StructuredAggregationQuery.Aggregation.CountH\x00\x12N\n\x03sum\x18\x02 \x01(\x0b2?.google.firestore.v1.StructuredAggregationQuery.Aggregation.SumH\x00\x12N\n\x03avg\x18\x03 \x01(\x0b2?.google.firestore.v1.StructuredAggregationQuery.Aggregation.AvgH\x00\x12\x12\n\x05alias\x18\x07 \x01(\tB\x03\xe0A\x01\x1a8\n\x05Count\x12/\n\x05up_to\x18\x01 \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x01\x1aI\n\x03Sum\x12B\n\x05field\x18\x01 \x01(\x0b23.google.firestore.v1.StructuredQuery.FieldReference\x1aI\n\x03Avg\x12B\n\x05field\x18\x01 \x01(\x0b23.google.firestore.v1.StructuredQuery.FieldReferenceB\n\n\x08operatorB\x0c\n\nquery_type"D\n\x06Cursor\x12*\n\x06values\x18\x01 \x03(\x0b2\x1a.google.firestore.v1.Value\x12\x0e\n\x06before\x18\x02 \x01(\x08B\xc2\x01\n\x17com.google.firestore.v1B\nQueryProtoP\x01Z;cloud.google.com/go/firestore/apiv1/firestorepb;firestorepb\xa2\x02\x04GCFS\xaa\x02\x19Google.Cloud.Firestore.V1\xca\x02\x19Google\\Cloud\\Firestore\\V1\xea\x02\x1cGoogle::Cloud::Firestore::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.v1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.firestore.v1B\nQueryProtoP\x01Z;cloud.google.com/go/firestore/apiv1/firestorepb;firestorepb\xa2\x02\x04GCFS\xaa\x02\x19Google.Cloud.Firestore.V1\xca\x02\x19Google\\Cloud\\Firestore\\V1\xea\x02\x1cGoogle::Cloud::Firestore::V1'
    _globals['_STRUCTUREDQUERY_FINDNEAREST'].fields_by_name['vector_field']._loaded_options = None
    _globals['_STRUCTUREDQUERY_FINDNEAREST'].fields_by_name['vector_field']._serialized_options = b'\xe0A\x02'
    _globals['_STRUCTUREDQUERY_FINDNEAREST'].fields_by_name['query_vector']._loaded_options = None
    _globals['_STRUCTUREDQUERY_FINDNEAREST'].fields_by_name['query_vector']._serialized_options = b'\xe0A\x02'
    _globals['_STRUCTUREDQUERY_FINDNEAREST'].fields_by_name['distance_measure']._loaded_options = None
    _globals['_STRUCTUREDQUERY_FINDNEAREST'].fields_by_name['distance_measure']._serialized_options = b'\xe0A\x02'
    _globals['_STRUCTUREDQUERY_FINDNEAREST'].fields_by_name['limit']._loaded_options = None
    _globals['_STRUCTUREDQUERY_FINDNEAREST'].fields_by_name['limit']._serialized_options = b'\xe0A\x02'
    _globals['_STRUCTUREDQUERY_FINDNEAREST'].fields_by_name['distance_result_field']._loaded_options = None
    _globals['_STRUCTUREDQUERY_FINDNEAREST'].fields_by_name['distance_result_field']._serialized_options = b'\xe0A\x01'
    _globals['_STRUCTUREDQUERY_FINDNEAREST'].fields_by_name['distance_threshold']._loaded_options = None
    _globals['_STRUCTUREDQUERY_FINDNEAREST'].fields_by_name['distance_threshold']._serialized_options = b'\xe0A\x01'
    _globals['_STRUCTUREDQUERY'].fields_by_name['find_nearest']._loaded_options = None
    _globals['_STRUCTUREDQUERY'].fields_by_name['find_nearest']._serialized_options = b'\xe0A\x01'
    _globals['_STRUCTUREDAGGREGATIONQUERY_AGGREGATION_COUNT'].fields_by_name['up_to']._loaded_options = None
    _globals['_STRUCTUREDAGGREGATIONQUERY_AGGREGATION_COUNT'].fields_by_name['up_to']._serialized_options = b'\xe0A\x01'
    _globals['_STRUCTUREDAGGREGATIONQUERY_AGGREGATION'].fields_by_name['alias']._loaded_options = None
    _globals['_STRUCTUREDAGGREGATIONQUERY_AGGREGATION'].fields_by_name['alias']._serialized_options = b'\xe0A\x01'
    _globals['_STRUCTUREDAGGREGATIONQUERY'].fields_by_name['aggregations']._loaded_options = None
    _globals['_STRUCTUREDAGGREGATIONQUERY'].fields_by_name['aggregations']._serialized_options = b'\xe0A\x01'
    _globals['_STRUCTUREDQUERY']._serialized_start = 158
    _globals['_STRUCTUREDQUERY']._serialized_end = 2710
    _globals['_STRUCTUREDQUERY_COLLECTIONSELECTOR']._serialized_start = 664
    _globals['_STRUCTUREDQUERY_COLLECTIONSELECTOR']._serialized_end = 732
    _globals['_STRUCTUREDQUERY_FILTER']._serialized_start = 735
    _globals['_STRUCTUREDQUERY_FILTER']._serialized_end = 988
    _globals['_STRUCTUREDQUERY_COMPOSITEFILTER']._serialized_start = 991
    _globals['_STRUCTUREDQUERY_COMPOSITEFILTER']._serialized_end = 1200
    _globals['_STRUCTUREDQUERY_COMPOSITEFILTER_OPERATOR']._serialized_start = 1147
    _globals['_STRUCTUREDQUERY_COMPOSITEFILTER_OPERATOR']._serialized_end = 1200
    _globals['_STRUCTUREDQUERY_FIELDFILTER']._serialized_start = 1203
    _globals['_STRUCTUREDQUERY_FIELDFILTER']._serialized_end = 1611
    _globals['_STRUCTUREDQUERY_FIELDFILTER_OPERATOR']._serialized_start = 1401
    _globals['_STRUCTUREDQUERY_FIELDFILTER_OPERATOR']._serialized_end = 1611
    _globals['_STRUCTUREDQUERY_UNARYFILTER']._serialized_start = 1614
    _globals['_STRUCTUREDQUERY_UNARYFILTER']._serialized_end = 1880
    _globals['_STRUCTUREDQUERY_UNARYFILTER_OPERATOR']._serialized_start = 1770
    _globals['_STRUCTUREDQUERY_UNARYFILTER_OPERATOR']._serialized_end = 1864
    _globals['_STRUCTUREDQUERY_ORDER']._serialized_start = 1883
    _globals['_STRUCTUREDQUERY_ORDER']._serialized_end = 2025
    _globals['_STRUCTUREDQUERY_FIELDREFERENCE']._serialized_start = 2027
    _globals['_STRUCTUREDQUERY_FIELDREFERENCE']._serialized_end = 2063
    _globals['_STRUCTUREDQUERY_PROJECTION']._serialized_start = 2065
    _globals['_STRUCTUREDQUERY_PROJECTION']._serialized_end = 2146
    _globals['_STRUCTUREDQUERY_FINDNEAREST']._serialized_start = 2149
    _globals['_STRUCTUREDQUERY_FINDNEAREST']._serialized_end = 2639
    _globals['_STRUCTUREDQUERY_FINDNEAREST_DISTANCEMEASURE']._serialized_start = 2544
    _globals['_STRUCTUREDQUERY_FINDNEAREST_DISTANCEMEASURE']._serialized_end = 2639
    _globals['_STRUCTUREDQUERY_DIRECTION']._serialized_start = 2641
    _globals['_STRUCTUREDQUERY_DIRECTION']._serialized_end = 2710
    _globals['_STRUCTUREDAGGREGATIONQUERY']._serialized_start = 2713
    _globals['_STRUCTUREDAGGREGATIONQUERY']._serialized_end = 3409
    _globals['_STRUCTUREDAGGREGATIONQUERY_AGGREGATION']._serialized_start = 2898
    _globals['_STRUCTUREDAGGREGATIONQUERY_AGGREGATION']._serialized_end = 3395
    _globals['_STRUCTUREDAGGREGATIONQUERY_AGGREGATION_COUNT']._serialized_start = 3177
    _globals['_STRUCTUREDAGGREGATIONQUERY_AGGREGATION_COUNT']._serialized_end = 3233
    _globals['_STRUCTUREDAGGREGATIONQUERY_AGGREGATION_SUM']._serialized_start = 3235
    _globals['_STRUCTUREDAGGREGATIONQUERY_AGGREGATION_SUM']._serialized_end = 3308
    _globals['_STRUCTUREDAGGREGATIONQUERY_AGGREGATION_AVG']._serialized_start = 3310
    _globals['_STRUCTUREDAGGREGATIONQUERY_AGGREGATION_AVG']._serialized_end = 3383
    _globals['_CURSOR']._serialized_start = 3411
    _globals['_CURSOR']._serialized_end = 3479