"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/firestore/v1/aggregation_result.proto')
_sym_db = _symbol_database.Default()
from ....google.firestore.v1 import document_pb2 as google_dot_firestore_dot_v1_dot_document__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/firestore/v1/aggregation_result.proto\x12\x13google.firestore.v1\x1a"google/firestore/v1/document.proto"\xbe\x01\n\x11AggregationResult\x12U\n\x10aggregate_fields\x18\x02 \x03(\x0b2;.google.firestore.v1.AggregationResult.AggregateFieldsEntry\x1aR\n\x14AggregateFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b2\x1a.google.firestore.v1.Value:\x028\x01B\xce\x01\n\x17com.google.firestore.v1B\x16AggregationResultProtoP\x01Z;cloud.google.com/go/firestore/apiv1/firestorepb;firestorepb\xa2\x02\x04GCFS\xaa\x02\x19Google.Cloud.Firestore.V1\xca\x02\x19Google\\Cloud\\Firestore\\V1\xea\x02\x1cGoogle::Cloud::Firestore::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.v1.aggregation_result_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.firestore.v1B\x16AggregationResultProtoP\x01Z;cloud.google.com/go/firestore/apiv1/firestorepb;firestorepb\xa2\x02\x04GCFS\xaa\x02\x19Google.Cloud.Firestore.V1\xca\x02\x19Google\\Cloud\\Firestore\\V1\xea\x02\x1cGoogle::Cloud::Firestore::V1'
    _globals['_AGGREGATIONRESULT_AGGREGATEFIELDSENTRY']._loaded_options = None
    _globals['_AGGREGATIONRESULT_AGGREGATEFIELDSENTRY']._serialized_options = b'8\x01'
    _globals['_AGGREGATIONRESULT']._serialized_start = 106
    _globals['_AGGREGATIONRESULT']._serialized_end = 296
    _globals['_AGGREGATIONRESULT_AGGREGATEFIELDSENTRY']._serialized_start = 214
    _globals['_AGGREGATIONRESULT_AGGREGATEFIELDSENTRY']._serialized_end = 296