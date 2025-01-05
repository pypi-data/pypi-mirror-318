"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/spanner/v1/result_set.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ....google.spanner.v1 import query_plan_pb2 as google_dot_spanner_dot_v1_dot_query__plan__pb2
from ....google.spanner.v1 import transaction_pb2 as google_dot_spanner_dot_v1_dot_transaction__pb2
from ....google.spanner.v1 import type_pb2 as google_dot_spanner_dot_v1_dot_type__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/spanner/v1/result_set.proto\x12\x11google.spanner.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a"google/spanner/v1/query_plan.proto\x1a#google/spanner/v1/transaction.proto\x1a\x1cgoogle/spanner/v1/type.proto"\xf2\x01\n\tResultSet\x126\n\x08metadata\x18\x01 \x01(\x0b2$.google.spanner.v1.ResultSetMetadata\x12(\n\x04rows\x18\x02 \x03(\x0b2\x1a.google.protobuf.ListValue\x120\n\x05stats\x18\x03 \x01(\x0b2!.google.spanner.v1.ResultSetStats\x12Q\n\x0fprecommit_token\x18\x05 \x01(\x0b23.google.spanner.v1.MultiplexedSessionPrecommitTokenB\x03\xe0A\x01"\xa4\x02\n\x10PartialResultSet\x126\n\x08metadata\x18\x01 \x01(\x0b2$.google.spanner.v1.ResultSetMetadata\x12&\n\x06values\x18\x02 \x03(\x0b2\x16.google.protobuf.Value\x12\x15\n\rchunked_value\x18\x03 \x01(\x08\x12\x14\n\x0cresume_token\x18\x04 \x01(\x0c\x120\n\x05stats\x18\x05 \x01(\x0b2!.google.spanner.v1.ResultSetStats\x12Q\n\x0fprecommit_token\x18\x08 \x01(\x0b23.google.spanner.v1.MultiplexedSessionPrecommitTokenB\x03\xe0A\x01"\xb7\x01\n\x11ResultSetMetadata\x12/\n\x08row_type\x18\x01 \x01(\x0b2\x1d.google.spanner.v1.StructType\x123\n\x0btransaction\x18\x02 \x01(\x0b2\x1e.google.spanner.v1.Transaction\x12<\n\x15undeclared_parameters\x18\x03 \x01(\x0b2\x1d.google.spanner.v1.StructType"\xb9\x01\n\x0eResultSetStats\x120\n\nquery_plan\x18\x01 \x01(\x0b2\x1c.google.spanner.v1.QueryPlan\x12,\n\x0bquery_stats\x18\x02 \x01(\x0b2\x17.google.protobuf.Struct\x12\x19\n\x0frow_count_exact\x18\x03 \x01(\x03H\x00\x12\x1f\n\x15row_count_lower_bound\x18\x04 \x01(\x03H\x00B\x0b\n\trow_countB\xb4\x01\n\x15com.google.spanner.v1B\x0eResultSetProtoP\x01Z5cloud.google.com/go/spanner/apiv1/spannerpb;spannerpb\xf8\x01\x01\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1\xea\x02\x1aGoogle::Cloud::Spanner::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.spanner.v1.result_set_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x15com.google.spanner.v1B\x0eResultSetProtoP\x01Z5cloud.google.com/go/spanner/apiv1/spannerpb;spannerpb\xf8\x01\x01\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1\xea\x02\x1aGoogle::Cloud::Spanner::V1'
    _globals['_RESULTSET'].fields_by_name['precommit_token']._loaded_options = None
    _globals['_RESULTSET'].fields_by_name['precommit_token']._serialized_options = b'\xe0A\x01'
    _globals['_PARTIALRESULTSET'].fields_by_name['precommit_token']._loaded_options = None
    _globals['_PARTIALRESULTSET'].fields_by_name['precommit_token']._serialized_options = b'\xe0A\x01'
    _globals['_RESULTSET']._serialized_start = 224
    _globals['_RESULTSET']._serialized_end = 466
    _globals['_PARTIALRESULTSET']._serialized_start = 469
    _globals['_PARTIALRESULTSET']._serialized_end = 761
    _globals['_RESULTSETMETADATA']._serialized_start = 764
    _globals['_RESULTSETMETADATA']._serialized_end = 947
    _globals['_RESULTSETSTATS']._serialized_start = 950
    _globals['_RESULTSETSTATS']._serialized_end = 1135