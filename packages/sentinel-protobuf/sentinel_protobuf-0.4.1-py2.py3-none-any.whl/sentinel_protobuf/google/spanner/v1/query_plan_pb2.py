"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/spanner/v1/query_plan.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/spanner/v1/query_plan.proto\x12\x11google.spanner.v1\x1a\x1cgoogle/protobuf/struct.proto"\xf8\x04\n\x08PlanNode\x12\r\n\x05index\x18\x01 \x01(\x05\x12.\n\x04kind\x18\x02 \x01(\x0e2 .google.spanner.v1.PlanNode.Kind\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12:\n\x0bchild_links\x18\x04 \x03(\x0b2%.google.spanner.v1.PlanNode.ChildLink\x12M\n\x14short_representation\x18\x05 \x01(\x0b2/.google.spanner.v1.PlanNode.ShortRepresentation\x12)\n\x08metadata\x18\x06 \x01(\x0b2\x17.google.protobuf.Struct\x120\n\x0fexecution_stats\x18\x07 \x01(\x0b2\x17.google.protobuf.Struct\x1a@\n\tChildLink\x12\x13\n\x0bchild_index\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x10\n\x08variable\x18\x03 \x01(\t\x1a\xb2\x01\n\x13ShortRepresentation\x12\x13\n\x0bdescription\x18\x01 \x01(\t\x12S\n\nsubqueries\x18\x02 \x03(\x0b2?.google.spanner.v1.PlanNode.ShortRepresentation.SubqueriesEntry\x1a1\n\x0fSubqueriesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x028\x01"8\n\x04Kind\x12\x14\n\x10KIND_UNSPECIFIED\x10\x00\x12\x0e\n\nRELATIONAL\x10\x01\x12\n\n\x06SCALAR\x10\x02"<\n\tQueryPlan\x12/\n\nplan_nodes\x18\x01 \x03(\x0b2\x1b.google.spanner.v1.PlanNodeB\xb1\x01\n\x15com.google.spanner.v1B\x0eQueryPlanProtoP\x01Z5cloud.google.com/go/spanner/apiv1/spannerpb;spannerpb\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1\xea\x02\x1aGoogle::Cloud::Spanner::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.spanner.v1.query_plan_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x15com.google.spanner.v1B\x0eQueryPlanProtoP\x01Z5cloud.google.com/go/spanner/apiv1/spannerpb;spannerpb\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1\xea\x02\x1aGoogle::Cloud::Spanner::V1'
    _globals['_PLANNODE_SHORTREPRESENTATION_SUBQUERIESENTRY']._loaded_options = None
    _globals['_PLANNODE_SHORTREPRESENTATION_SUBQUERIESENTRY']._serialized_options = b'8\x01'
    _globals['_PLANNODE']._serialized_start = 88
    _globals['_PLANNODE']._serialized_end = 720
    _globals['_PLANNODE_CHILDLINK']._serialized_start = 417
    _globals['_PLANNODE_CHILDLINK']._serialized_end = 481
    _globals['_PLANNODE_SHORTREPRESENTATION']._serialized_start = 484
    _globals['_PLANNODE_SHORTREPRESENTATION']._serialized_end = 662
    _globals['_PLANNODE_SHORTREPRESENTATION_SUBQUERIESENTRY']._serialized_start = 613
    _globals['_PLANNODE_SHORTREPRESENTATION_SUBQUERIESENTRY']._serialized_end = 662
    _globals['_PLANNODE_KIND']._serialized_start = 664
    _globals['_PLANNODE_KIND']._serialized_end = 720
    _globals['_QUERYPLAN']._serialized_start = 722
    _globals['_QUERYPLAN']._serialized_end = 782