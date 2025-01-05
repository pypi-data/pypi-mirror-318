"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/node/v3/querier.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....sentinel.node.v3 import node_pb2 as sentinel_dot_node_dot_v3_dot_node__pb2
from ....sentinel.node.v3 import params_pb2 as sentinel_dot_node_dot_v3_dot_params__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esentinel/node/v3/querier.proto\x12\x10sentinel.node.v3\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bsentinel/node/v3/node.proto\x1a\x1dsentinel/node/v3/params.proto\x1a\x1esentinel/types/v1/status.proto"z\n\x11QueryNodesRequest\x12)\n\x06status\x18\x01 \x01(\x0e2\x19.sentinel.types.v1.Status\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x8d\x01\n\x18QueryNodesForPlanRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12)\n\x06status\x18\x02 \x01(\x0e2\x19.sentinel.types.v1.Status\x12:\n\npagination\x18\x03 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"#\n\x10QueryNodeRequest\x12\x0f\n\x07address\x18\x01 \x01(\t"~\n\x12QueryNodesResponse\x12+\n\x05nodes\x18\x01 \x03(\x0b2\x16.sentinel.node.v3.NodeB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x85\x01\n\x19QueryNodesForPlanResponse\x12+\n\x05nodes\x18\x01 \x03(\x0b2\x16.sentinel.node.v3.NodeB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"?\n\x11QueryNodeResponse\x12*\n\x04node\x18\x01 \x01(\x0b2\x16.sentinel.node.v3.NodeB\x04\xc8\xde\x1f\x00"\x14\n\x12QueryParamsRequest"E\n\x13QueryParamsResponse\x12.\n\x06params\x18\x01 \x01(\x0b2\x18.sentinel.node.v3.ParamsB\x04\xc8\xde\x1f\x002\xa2\x04\n\x0cQueryService\x12x\n\nQueryNodes\x12#.sentinel.node.v3.QueryNodesRequest\x1a$.sentinel.node.v3.QueryNodesResponse"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/sentinel/node/v3/nodes\x12\x98\x01\n\x11QueryNodesForPlan\x12*.sentinel.node.v3.QueryNodesForPlanRequest\x1a+.sentinel.node.v3.QueryNodesForPlanResponse"*\x82\xd3\xe4\x93\x02$\x12"/sentinel/node/v3/plans/{id}/nodes\x12\x7f\n\tQueryNode\x12".sentinel.node.v3.QueryNodeRequest\x1a#.sentinel.node.v3.QueryNodeResponse")\x82\xd3\xe4\x93\x02#\x12!/sentinel/node/v3/nodes/{address}\x12|\n\x0bQueryParams\x12$.sentinel.node.v3.QueryParamsRequest\x1a%.sentinel.node.v3.QueryParamsResponse" \x82\xd3\xe4\x93\x02\x1a\x12\x18/sentinel/node/v3/paramsB>Z4github.com/sentinel-official/hub/v12/x/node/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.node.v3.querier_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/node/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_QUERYNODESRESPONSE'].fields_by_name['nodes']._loaded_options = None
    _globals['_QUERYNODESRESPONSE'].fields_by_name['nodes']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYNODESFORPLANRESPONSE'].fields_by_name['nodes']._loaded_options = None
    _globals['_QUERYNODESFORPLANRESPONSE'].fields_by_name['nodes']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYNODERESPONSE'].fields_by_name['node']._loaded_options = None
    _globals['_QUERYNODERESPONSE'].fields_by_name['node']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYSERVICE'].methods_by_name['QueryNodes']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryNodes']._serialized_options = b'\x82\xd3\xe4\x93\x02\x19\x12\x17/sentinel/node/v3/nodes'
    _globals['_QUERYSERVICE'].methods_by_name['QueryNodesForPlan']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryNodesForPlan']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/sentinel/node/v3/plans/{id}/nodes'
    _globals['_QUERYSERVICE'].methods_by_name['QueryNode']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryNode']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/sentinel/node/v3/nodes/{address}'
    _globals['_QUERYSERVICE'].methods_by_name['QueryParams']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryParams']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a\x12\x18/sentinel/node/v3/params'
    _globals['_QUERYNODESREQUEST']._serialized_start = 240
    _globals['_QUERYNODESREQUEST']._serialized_end = 362
    _globals['_QUERYNODESFORPLANREQUEST']._serialized_start = 365
    _globals['_QUERYNODESFORPLANREQUEST']._serialized_end = 506
    _globals['_QUERYNODEREQUEST']._serialized_start = 508
    _globals['_QUERYNODEREQUEST']._serialized_end = 543
    _globals['_QUERYNODESRESPONSE']._serialized_start = 545
    _globals['_QUERYNODESRESPONSE']._serialized_end = 671
    _globals['_QUERYNODESFORPLANRESPONSE']._serialized_start = 674
    _globals['_QUERYNODESFORPLANRESPONSE']._serialized_end = 807
    _globals['_QUERYNODERESPONSE']._serialized_start = 809
    _globals['_QUERYNODERESPONSE']._serialized_end = 872
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 874
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 894
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 896
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 965
    _globals['_QUERYSERVICE']._serialized_start = 968
    _globals['_QUERYSERVICE']._serialized_end = 1514