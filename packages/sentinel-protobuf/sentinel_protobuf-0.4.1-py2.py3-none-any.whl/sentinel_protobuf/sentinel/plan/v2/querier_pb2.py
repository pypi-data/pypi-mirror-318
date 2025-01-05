"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/plan/v2/querier.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....sentinel.plan.v2 import plan_pb2 as sentinel_dot_plan_dot_v2_dot_plan__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esentinel/plan/v2/querier.proto\x12\x10sentinel.plan.v2\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bsentinel/plan/v2/plan.proto\x1a\x1esentinel/types/v1/status.proto"z\n\x11QueryPlansRequest\x12)\n\x06status\x18\x01 \x01(\x0e2\x19.sentinel.types.v1.Status\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x96\x01\n\x1cQueryPlansForProviderRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12)\n\x06status\x18\x02 \x01(\x0e2\x19.sentinel.types.v1.Status\x12:\n\npagination\x18\x03 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x1e\n\x10QueryPlanRequest\x12\n\n\x02id\x18\x01 \x01(\x04"~\n\x12QueryPlansResponse\x12+\n\x05plans\x18\x01 \x03(\x0b2\x16.sentinel.plan.v2.PlanB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x89\x01\n\x1dQueryPlansForProviderResponse\x12+\n\x05plans\x18\x01 \x03(\x0b2\x16.sentinel.plan.v2.PlanB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"?\n\x11QueryPlanResponse\x12*\n\x04plan\x18\x01 \x01(\x0b2\x16.sentinel.plan.v2.PlanB\x04\xc8\xde\x1f\x002\xb4\x03\n\x0cQueryService\x12x\n\nQueryPlans\x12#.sentinel.plan.v2.QueryPlansRequest\x1a$.sentinel.plan.v2.QueryPlansResponse"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/sentinel/plan/v2/plans\x12\xad\x01\n\x15QueryPlansForProvider\x12..sentinel.plan.v2.QueryPlansForProviderRequest\x1a/.sentinel.plan.v2.QueryPlansForProviderResponse"3\x82\xd3\xe4\x93\x02-\x12+/sentinel/plan/v2/providers/{address}/plans\x12z\n\tQueryPlan\x12".sentinel.plan.v2.QueryPlanRequest\x1a#.sentinel.plan.v2.QueryPlanResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/sentinel/plan/v2/plans/{id}B>Z4github.com/sentinel-official/hub/v12/x/plan/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.plan.v2.querier_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/plan/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_QUERYPLANSRESPONSE'].fields_by_name['plans']._loaded_options = None
    _globals['_QUERYPLANSRESPONSE'].fields_by_name['plans']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYPLANSFORPROVIDERRESPONSE'].fields_by_name['plans']._loaded_options = None
    _globals['_QUERYPLANSFORPROVIDERRESPONSE'].fields_by_name['plans']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYPLANRESPONSE'].fields_by_name['plan']._loaded_options = None
    _globals['_QUERYPLANRESPONSE'].fields_by_name['plan']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYSERVICE'].methods_by_name['QueryPlans']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryPlans']._serialized_options = b'\x82\xd3\xe4\x93\x02\x19\x12\x17/sentinel/plan/v2/plans'
    _globals['_QUERYSERVICE'].methods_by_name['QueryPlansForProvider']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryPlansForProvider']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/sentinel/plan/v2/providers/{address}/plans'
    _globals['_QUERYSERVICE'].methods_by_name['QueryPlan']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryPlan']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/sentinel/plan/v2/plans/{id}'
    _globals['_QUERYPLANSREQUEST']._serialized_start = 209
    _globals['_QUERYPLANSREQUEST']._serialized_end = 331
    _globals['_QUERYPLANSFORPROVIDERREQUEST']._serialized_start = 334
    _globals['_QUERYPLANSFORPROVIDERREQUEST']._serialized_end = 484
    _globals['_QUERYPLANREQUEST']._serialized_start = 486
    _globals['_QUERYPLANREQUEST']._serialized_end = 516
    _globals['_QUERYPLANSRESPONSE']._serialized_start = 518
    _globals['_QUERYPLANSRESPONSE']._serialized_end = 644
    _globals['_QUERYPLANSFORPROVIDERRESPONSE']._serialized_start = 647
    _globals['_QUERYPLANSFORPROVIDERRESPONSE']._serialized_end = 784
    _globals['_QUERYPLANRESPONSE']._serialized_start = 786
    _globals['_QUERYPLANRESPONSE']._serialized_end = 849
    _globals['_QUERYSERVICE']._serialized_start = 852
    _globals['_QUERYSERVICE']._serialized_end = 1288