"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/v1beta1/query.proto')
_sym_db = _symbol_database.Default()
from ....google.firestore.v1beta1 import document_pb2 as google_dot_firestore_dot_v1beta1_dot_document__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/firestore/v1beta1/query.proto\x12\x18google.firestore.v1beta1\x1a\'google/firestore/v1beta1/document.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x95\x10\n\x0fStructuredQuery\x12D\n\x06select\x18\x01 \x01(\x0b24.google.firestore.v1beta1.StructuredQuery.Projection\x12J\n\x04from\x18\x02 \x03(\x0b2<.google.firestore.v1beta1.StructuredQuery.CollectionSelector\x12?\n\x05where\x18\x03 \x01(\x0b20.google.firestore.v1beta1.StructuredQuery.Filter\x12A\n\x08order_by\x18\x04 \x03(\x0b2/.google.firestore.v1beta1.StructuredQuery.Order\x122\n\x08start_at\x18\x07 \x01(\x0b2 .google.firestore.v1beta1.Cursor\x120\n\x06end_at\x18\x08 \x01(\x0b2 .google.firestore.v1beta1.Cursor\x12\x0e\n\x06offset\x18\x06 \x01(\x05\x12*\n\x05limit\x18\x05 \x01(\x0b2\x1b.google.protobuf.Int32Value\x1aD\n\x12CollectionSelector\x12\x15\n\rcollection_id\x18\x02 \x01(\t\x12\x17\n\x0fall_descendants\x18\x03 \x01(\x08\x1a\x8c\x02\n\x06Filter\x12U\n\x10composite_filter\x18\x01 \x01(\x0b29.google.firestore.v1beta1.StructuredQuery.CompositeFilterH\x00\x12M\n\x0cfield_filter\x18\x02 \x01(\x0b25.google.firestore.v1beta1.StructuredQuery.FieldFilterH\x00\x12M\n\x0cunary_filter\x18\x03 \x01(\x0b25.google.firestore.v1beta1.StructuredQuery.UnaryFilterH\x00B\r\n\x0bfilter_type\x1a\xd3\x01\n\x0fCompositeFilter\x12N\n\x02op\x18\x01 \x01(\x0e2B.google.firestore.v1beta1.StructuredQuery.CompositeFilter.Operator\x12A\n\x07filters\x18\x02 \x03(\x0b20.google.firestore.v1beta1.StructuredQuery.Filter"-\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\x07\n\x03AND\x10\x01\x1a\xa7\x03\n\x0bFieldFilter\x12G\n\x05field\x18\x01 \x01(\x0b28.google.firestore.v1beta1.StructuredQuery.FieldReference\x12J\n\x02op\x18\x02 \x01(\x0e2>.google.firestore.v1beta1.StructuredQuery.FieldFilter.Operator\x12.\n\x05value\x18\x03 \x01(\x0b2\x1f.google.firestore.v1beta1.Value"\xd2\x01\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\r\n\tLESS_THAN\x10\x01\x12\x16\n\x12LESS_THAN_OR_EQUAL\x10\x02\x12\x10\n\x0cGREATER_THAN\x10\x03\x12\x19\n\x15GREATER_THAN_OR_EQUAL\x10\x04\x12\t\n\x05EQUAL\x10\x05\x12\r\n\tNOT_EQUAL\x10\x06\x12\x12\n\x0eARRAY_CONTAINS\x10\x07\x12\x06\n\x02IN\x10\x08\x12\x16\n\x12ARRAY_CONTAINS_ANY\x10\t\x12\n\n\x06NOT_IN\x10\n\x1a\x94\x02\n\x0bUnaryFilter\x12J\n\x02op\x18\x01 \x01(\x0e2>.google.firestore.v1beta1.StructuredQuery.UnaryFilter.Operator\x12I\n\x05field\x18\x02 \x01(\x0b28.google.firestore.v1beta1.StructuredQuery.FieldReferenceH\x00"^\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\n\n\x06IS_NAN\x10\x02\x12\x0b\n\x07IS_NULL\x10\x03\x12\x0e\n\nIS_NOT_NAN\x10\x04\x12\x0f\n\x0bIS_NOT_NULL\x10\x05B\x0e\n\x0coperand_type\x1a$\n\x0eFieldReference\x12\x12\n\nfield_path\x18\x02 \x01(\t\x1a\x98\x01\n\x05Order\x12G\n\x05field\x18\x01 \x01(\x0b28.google.firestore.v1beta1.StructuredQuery.FieldReference\x12F\n\tdirection\x18\x02 \x01(\x0e23.google.firestore.v1beta1.StructuredQuery.Direction\x1aV\n\nProjection\x12H\n\x06fields\x18\x02 \x03(\x0b28.google.firestore.v1beta1.StructuredQuery.FieldReference"E\n\tDirection\x12\x19\n\x15DIRECTION_UNSPECIFIED\x10\x00\x12\r\n\tASCENDING\x10\x01\x12\x0e\n\nDESCENDING\x10\x02"I\n\x06Cursor\x12/\n\x06values\x18\x01 \x03(\x0b2\x1f.google.firestore.v1beta1.Value\x12\x0e\n\x06before\x18\x02 \x01(\x08B\xdb\x01\n\x1ccom.google.firestore.v1beta1B\nQueryProtoP\x01Z@cloud.google.com/go/firestore/apiv1beta1/firestorepb;firestorepb\xa2\x02\x04GCFS\xaa\x02\x1eGoogle.Cloud.Firestore.V1Beta1\xca\x02\x1eGoogle\\Cloud\\Firestore\\V1beta1\xea\x02!Google::Cloud::Firestore::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.v1beta1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.firestore.v1beta1B\nQueryProtoP\x01Z@cloud.google.com/go/firestore/apiv1beta1/firestorepb;firestorepb\xa2\x02\x04GCFS\xaa\x02\x1eGoogle.Cloud.Firestore.V1Beta1\xca\x02\x1eGoogle\\Cloud\\Firestore\\V1beta1\xea\x02!Google::Cloud::Firestore::V1beta1'
    _globals['_STRUCTUREDQUERY']._serialized_start = 140
    _globals['_STRUCTUREDQUERY']._serialized_end = 2209
    _globals['_STRUCTUREDQUERY_COLLECTIONSELECTOR']._serialized_start = 599
    _globals['_STRUCTUREDQUERY_COLLECTIONSELECTOR']._serialized_end = 667
    _globals['_STRUCTUREDQUERY_FILTER']._serialized_start = 670
    _globals['_STRUCTUREDQUERY_FILTER']._serialized_end = 938
    _globals['_STRUCTUREDQUERY_COMPOSITEFILTER']._serialized_start = 941
    _globals['_STRUCTUREDQUERY_COMPOSITEFILTER']._serialized_end = 1152
    _globals['_STRUCTUREDQUERY_COMPOSITEFILTER_OPERATOR']._serialized_start = 1107
    _globals['_STRUCTUREDQUERY_COMPOSITEFILTER_OPERATOR']._serialized_end = 1152
    _globals['_STRUCTUREDQUERY_FIELDFILTER']._serialized_start = 1155
    _globals['_STRUCTUREDQUERY_FIELDFILTER']._serialized_end = 1578
    _globals['_STRUCTUREDQUERY_FIELDFILTER_OPERATOR']._serialized_start = 1368
    _globals['_STRUCTUREDQUERY_FIELDFILTER_OPERATOR']._serialized_end = 1578
    _globals['_STRUCTUREDQUERY_UNARYFILTER']._serialized_start = 1581
    _globals['_STRUCTUREDQUERY_UNARYFILTER']._serialized_end = 1857
    _globals['_STRUCTUREDQUERY_UNARYFILTER_OPERATOR']._serialized_start = 1747
    _globals['_STRUCTUREDQUERY_UNARYFILTER_OPERATOR']._serialized_end = 1841
    _globals['_STRUCTUREDQUERY_FIELDREFERENCE']._serialized_start = 1859
    _globals['_STRUCTUREDQUERY_FIELDREFERENCE']._serialized_end = 1895
    _globals['_STRUCTUREDQUERY_ORDER']._serialized_start = 1898
    _globals['_STRUCTUREDQUERY_ORDER']._serialized_end = 2050
    _globals['_STRUCTUREDQUERY_PROJECTION']._serialized_start = 2052
    _globals['_STRUCTUREDQUERY_PROJECTION']._serialized_end = 2138
    _globals['_STRUCTUREDQUERY_DIRECTION']._serialized_start = 2140
    _globals['_STRUCTUREDQUERY_DIRECTION']._serialized_end = 2209
    _globals['_CURSOR']._serialized_start = 2211
    _globals['_CURSOR']._serialized_end = 2284