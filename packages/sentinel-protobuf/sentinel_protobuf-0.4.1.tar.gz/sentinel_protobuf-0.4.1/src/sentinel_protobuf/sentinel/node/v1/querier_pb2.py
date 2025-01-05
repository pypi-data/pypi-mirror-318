"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/node/v1/querier.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....sentinel.node.v1 import node_pb2 as sentinel_dot_node_dot_v1_dot_node__pb2
from ....sentinel.node.v1 import params_pb2 as sentinel_dot_node_dot_v1_dot_params__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esentinel/node/v1/querier.proto\x12\x10sentinel.node.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bsentinel/node/v1/node.proto\x1a\x1dsentinel/node/v1/params.proto\x1a\x1esentinel/types/v1/status.proto"z\n\x11QueryNodesRequest\x12)\n\x06status\x18\x01 \x01(\x0e2\x19.sentinel.types.v1.Status\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x96\x01\n\x1cQueryNodesForProviderRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12)\n\x06status\x18\x02 \x01(\x0e2\x19.sentinel.types.v1.Status\x12:\n\npagination\x18\x03 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"#\n\x10QueryNodeRequest\x12\x0f\n\x07address\x18\x01 \x01(\t"\x14\n\x12QueryParamsRequest"~\n\x12QueryNodesResponse\x12+\n\x05nodes\x18\x01 \x03(\x0b2\x16.sentinel.node.v1.NodeB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x89\x01\n\x1dQueryNodesForProviderResponse\x12+\n\x05nodes\x18\x01 \x03(\x0b2\x16.sentinel.node.v1.NodeB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"?\n\x11QueryNodeResponse\x12*\n\x04node\x18\x01 \x01(\x0b2\x16.sentinel.node.v1.NodeB\x04\xc8\xde\x1f\x00"E\n\x13QueryParamsResponse\x12.\n\x06params\x18\x01 \x01(\x0b2\x18.sentinel.node.v1.ParamsB\x04\xc8\xde\x1f\x002\xb7\x04\n\x0cQueryService\x12x\n\nQueryNodes\x12#.sentinel.node.v1.QueryNodesRequest\x1a$.sentinel.node.v1.QueryNodesResponse"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/sentinel/node/v1/nodes\x12\xad\x01\n\x15QueryNodesForProvider\x12..sentinel.node.v1.QueryNodesForProviderRequest\x1a/.sentinel.node.v1.QueryNodesForProviderResponse"3\x82\xd3\xe4\x93\x02-\x12+/sentinel/node/v1/providers/{address}/nodes\x12\x7f\n\tQueryNode\x12".sentinel.node.v1.QueryNodeRequest\x1a#.sentinel.node.v1.QueryNodeResponse")\x82\xd3\xe4\x93\x02#\x12!/sentinel/node/v1/nodes/{address}\x12|\n\x0bQueryParams\x12$.sentinel.node.v1.QueryParamsRequest\x1a%.sentinel.node.v1.QueryParamsResponse" \x82\xd3\xe4\x93\x02\x1a\x12\x18/sentinel/node/v1/paramsB>Z4github.com/sentinel-official/hub/v12/x/node/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.node.v1.querier_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/node/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_QUERYNODESRESPONSE'].fields_by_name['nodes']._loaded_options = None
    _globals['_QUERYNODESRESPONSE'].fields_by_name['nodes']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYNODESFORPROVIDERRESPONSE'].fields_by_name['nodes']._loaded_options = None
    _globals['_QUERYNODESFORPROVIDERRESPONSE'].fields_by_name['nodes']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYNODERESPONSE'].fields_by_name['node']._loaded_options = None
    _globals['_QUERYNODERESPONSE'].fields_by_name['node']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYSERVICE'].methods_by_name['QueryNodes']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryNodes']._serialized_options = b'\x82\xd3\xe4\x93\x02\x19\x12\x17/sentinel/node/v1/nodes'
    _globals['_QUERYSERVICE'].methods_by_name['QueryNodesForProvider']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryNodesForProvider']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/sentinel/node/v1/providers/{address}/nodes'
    _globals['_QUERYSERVICE'].methods_by_name['QueryNode']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryNode']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/sentinel/node/v1/nodes/{address}'
    _globals['_QUERYSERVICE'].methods_by_name['QueryParams']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryParams']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a\x12\x18/sentinel/node/v1/params'
    _globals['_QUERYNODESREQUEST']._serialized_start = 240
    _globals['_QUERYNODESREQUEST']._serialized_end = 362
    _globals['_QUERYNODESFORPROVIDERREQUEST']._serialized_start = 365
    _globals['_QUERYNODESFORPROVIDERREQUEST']._serialized_end = 515
    _globals['_QUERYNODEREQUEST']._serialized_start = 517
    _globals['_QUERYNODEREQUEST']._serialized_end = 552
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 554
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 574
    _globals['_QUERYNODESRESPONSE']._serialized_start = 576
    _globals['_QUERYNODESRESPONSE']._serialized_end = 702
    _globals['_QUERYNODESFORPROVIDERRESPONSE']._serialized_start = 705
    _globals['_QUERYNODESFORPROVIDERRESPONSE']._serialized_end = 842
    _globals['_QUERYNODERESPONSE']._serialized_start = 844
    _globals['_QUERYNODERESPONSE']._serialized_end = 907
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 909
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 978
    _globals['_QUERYSERVICE']._serialized_start = 981
    _globals['_QUERYSERVICE']._serialized_end = 1548