"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/datastore/v1beta3/query.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.datastore.v1beta3 import entity_pb2 as google_dot_datastore_dot_v1beta3_dot_entity__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from ....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/datastore/v1beta3/query.proto\x12\x18google.datastore.v1beta3\x1a\x1cgoogle/api/annotations.proto\x1a%google/datastore/v1beta3/entity.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x18google/type/latlng.proto"\xb4\x01\n\x0cEntityResult\x120\n\x06entity\x18\x01 \x01(\x0b2 .google.datastore.v1beta3.Entity\x12\x0f\n\x07version\x18\x04 \x01(\x03\x12\x0e\n\x06cursor\x18\x03 \x01(\x0c"Q\n\nResultType\x12\x1b\n\x17RESULT_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04FULL\x10\x01\x12\x0e\n\nPROJECTION\x10\x02\x12\x0c\n\x08KEY_ONLY\x10\x03"\x8b\x03\n\x05Query\x128\n\nprojection\x18\x02 \x03(\x0b2$.google.datastore.v1beta3.Projection\x126\n\x04kind\x18\x03 \x03(\x0b2(.google.datastore.v1beta3.KindExpression\x120\n\x06filter\x18\x04 \x01(\x0b2 .google.datastore.v1beta3.Filter\x126\n\x05order\x18\x05 \x03(\x0b2\'.google.datastore.v1beta3.PropertyOrder\x12@\n\x0bdistinct_on\x18\x06 \x03(\x0b2+.google.datastore.v1beta3.PropertyReference\x12\x14\n\x0cstart_cursor\x18\x07 \x01(\x0c\x12\x12\n\nend_cursor\x18\x08 \x01(\x0c\x12\x0e\n\x06offset\x18\n \x01(\x05\x12*\n\x05limit\x18\x0c \x01(\x0b2\x1b.google.protobuf.Int32Value"\x1e\n\x0eKindExpression\x12\x0c\n\x04name\x18\x01 \x01(\t"!\n\x11PropertyReference\x12\x0c\n\x04name\x18\x02 \x01(\t"K\n\nProjection\x12=\n\x08property\x18\x01 \x01(\x0b2+.google.datastore.v1beta3.PropertyReference"\xdb\x01\n\rPropertyOrder\x12=\n\x08property\x18\x01 \x01(\x0b2+.google.datastore.v1beta3.PropertyReference\x12D\n\tdirection\x18\x02 \x01(\x0e21.google.datastore.v1beta3.PropertyOrder.Direction"E\n\tDirection\x12\x19\n\x15DIRECTION_UNSPECIFIED\x10\x00\x12\r\n\tASCENDING\x10\x01\x12\x0e\n\nDESCENDING\x10\x02"\xa3\x01\n\x06Filter\x12E\n\x10composite_filter\x18\x01 \x01(\x0b2).google.datastore.v1beta3.CompositeFilterH\x00\x12C\n\x0fproperty_filter\x18\x02 \x01(\x0b2(.google.datastore.v1beta3.PropertyFilterH\x00B\r\n\x0bfilter_type"\xb3\x01\n\x0fCompositeFilter\x12>\n\x02op\x18\x01 \x01(\x0e22.google.datastore.v1beta3.CompositeFilter.Operator\x121\n\x07filters\x18\x02 \x03(\x0b2 .google.datastore.v1beta3.Filter"-\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\x07\n\x03AND\x10\x01"\xd6\x02\n\x0ePropertyFilter\x12=\n\x08property\x18\x01 \x01(\x0b2+.google.datastore.v1beta3.PropertyReference\x12=\n\x02op\x18\x02 \x01(\x0e21.google.datastore.v1beta3.PropertyFilter.Operator\x12.\n\x05value\x18\x03 \x01(\x0b2\x1f.google.datastore.v1beta3.Value"\x95\x01\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\r\n\tLESS_THAN\x10\x01\x12\x16\n\x12LESS_THAN_OR_EQUAL\x10\x02\x12\x10\n\x0cGREATER_THAN\x10\x03\x12\x19\n\x15GREATER_THAN_OR_EQUAL\x10\x04\x12\t\n\x05EQUAL\x10\x05\x12\x10\n\x0cHAS_ANCESTOR\x10\x0b"\xb4\x02\n\x08GqlQuery\x12\x14\n\x0cquery_string\x18\x01 \x01(\t\x12\x16\n\x0eallow_literals\x18\x02 \x01(\x08\x12M\n\x0enamed_bindings\x18\x05 \x03(\x0b25.google.datastore.v1beta3.GqlQuery.NamedBindingsEntry\x12H\n\x13positional_bindings\x18\x04 \x03(\x0b2+.google.datastore.v1beta3.GqlQueryParameter\x1aa\n\x12NamedBindingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b2+.google.datastore.v1beta3.GqlQueryParameter:\x028\x01"i\n\x11GqlQueryParameter\x120\n\x05value\x18\x02 \x01(\x0b2\x1f.google.datastore.v1beta3.ValueH\x00\x12\x10\n\x06cursor\x18\x03 \x01(\x0cH\x00B\x10\n\x0eparameter_type"\xed\x03\n\x10QueryResultBatch\x12\x17\n\x0fskipped_results\x18\x06 \x01(\x05\x12\x16\n\x0eskipped_cursor\x18\x03 \x01(\x0c\x12M\n\x12entity_result_type\x18\x01 \x01(\x0e21.google.datastore.v1beta3.EntityResult.ResultType\x12>\n\x0eentity_results\x18\x02 \x03(\x0b2&.google.datastore.v1beta3.EntityResult\x12\x12\n\nend_cursor\x18\x04 \x01(\x0c\x12P\n\x0cmore_results\x18\x05 \x01(\x0e2:.google.datastore.v1beta3.QueryResultBatch.MoreResultsType\x12\x18\n\x10snapshot_version\x18\x07 \x01(\x03"\x98\x01\n\x0fMoreResultsType\x12!\n\x1dMORE_RESULTS_TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cNOT_FINISHED\x10\x01\x12\x1c\n\x18MORE_RESULTS_AFTER_LIMIT\x10\x02\x12\x1d\n\x19MORE_RESULTS_AFTER_CURSOR\x10\x04\x12\x13\n\x0fNO_MORE_RESULTS\x10\x03B\xd4\x01\n\x1ccom.google.datastore.v1beta3B\nQueryProtoP\x01Z@cloud.google.com/go/datastore/apiv1beta3/datastorepb;datastorepb\xaa\x02\x1eGoogle.Cloud.Datastore.V1Beta3\xca\x02\x1eGoogle\\Cloud\\Datastore\\V1beta3\xea\x02!Google::Cloud::Datastore::V1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.datastore.v1beta3.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.datastore.v1beta3B\nQueryProtoP\x01Z@cloud.google.com/go/datastore/apiv1beta3/datastorepb;datastorepb\xaa\x02\x1eGoogle.Cloud.Datastore.V1Beta3\xca\x02\x1eGoogle\\Cloud\\Datastore\\V1beta3\xea\x02!Google::Cloud::Datastore::V1beta3'
    _globals['_GQLQUERY_NAMEDBINDINGSENTRY']._loaded_options = None
    _globals['_GQLQUERY_NAMEDBINDINGSENTRY']._serialized_options = b'8\x01'
    _globals['_ENTITYRESULT']._serialized_start = 194
    _globals['_ENTITYRESULT']._serialized_end = 374
    _globals['_ENTITYRESULT_RESULTTYPE']._serialized_start = 293
    _globals['_ENTITYRESULT_RESULTTYPE']._serialized_end = 374
    _globals['_QUERY']._serialized_start = 377
    _globals['_QUERY']._serialized_end = 772
    _globals['_KINDEXPRESSION']._serialized_start = 774
    _globals['_KINDEXPRESSION']._serialized_end = 804
    _globals['_PROPERTYREFERENCE']._serialized_start = 806
    _globals['_PROPERTYREFERENCE']._serialized_end = 839
    _globals['_PROJECTION']._serialized_start = 841
    _globals['_PROJECTION']._serialized_end = 916
    _globals['_PROPERTYORDER']._serialized_start = 919
    _globals['_PROPERTYORDER']._serialized_end = 1138
    _globals['_PROPERTYORDER_DIRECTION']._serialized_start = 1069
    _globals['_PROPERTYORDER_DIRECTION']._serialized_end = 1138
    _globals['_FILTER']._serialized_start = 1141
    _globals['_FILTER']._serialized_end = 1304
    _globals['_COMPOSITEFILTER']._serialized_start = 1307
    _globals['_COMPOSITEFILTER']._serialized_end = 1486
    _globals['_COMPOSITEFILTER_OPERATOR']._serialized_start = 1441
    _globals['_COMPOSITEFILTER_OPERATOR']._serialized_end = 1486
    _globals['_PROPERTYFILTER']._serialized_start = 1489
    _globals['_PROPERTYFILTER']._serialized_end = 1831
    _globals['_PROPERTYFILTER_OPERATOR']._serialized_start = 1682
    _globals['_PROPERTYFILTER_OPERATOR']._serialized_end = 1831
    _globals['_GQLQUERY']._serialized_start = 1834
    _globals['_GQLQUERY']._serialized_end = 2142
    _globals['_GQLQUERY_NAMEDBINDINGSENTRY']._serialized_start = 2045
    _globals['_GQLQUERY_NAMEDBINDINGSENTRY']._serialized_end = 2142
    _globals['_GQLQUERYPARAMETER']._serialized_start = 2144
    _globals['_GQLQUERYPARAMETER']._serialized_end = 2249
    _globals['_QUERYRESULTBATCH']._serialized_start = 2252
    _globals['_QUERYRESULTBATCH']._serialized_end = 2745
    _globals['_QUERYRESULTBATCH_MORERESULTSTYPE']._serialized_start = 2593
    _globals['_QUERYRESULTBATCH_MORERESULTSTYPE']._serialized_end = 2745