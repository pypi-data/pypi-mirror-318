"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/subscription/v2/querier.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....sentinel.subscription.v2 import allocation_pb2 as sentinel_dot_subscription_dot_v2_dot_allocation__pb2
from ....sentinel.subscription.v2 import params_pb2 as sentinel_dot_subscription_dot_v2_dot_params__pb2
from ....sentinel.subscription.v2 import payout_pb2 as sentinel_dot_subscription_dot_v2_dot_payout__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&sentinel/subscription/v2/querier.proto\x12\x18sentinel.subscription.v2\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a)sentinel/subscription/v2/allocation.proto\x1a%sentinel/subscription/v2/params.proto\x1a%sentinel/subscription/v2/payout.proto"a\n\x17QueryAllocationsRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"5\n\x16QueryAllocationRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0f\n\x07address\x18\x02 \x01(\t"Q\n\x13QueryPayoutsRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"l\n\x1dQueryPayoutsForAccountRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"i\n\x1aQueryPayoutsForNodeRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest" \n\x12QueryPayoutRequest\x12\n\n\x02id\x18\x01 \x01(\x04"W\n\x19QuerySubscriptionsRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"r\n#QuerySubscriptionsForAccountRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"o\n QuerySubscriptionsForNodeRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"j\n QuerySubscriptionsForPlanRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"&\n\x18QuerySubscriptionRequest\x12\n\n\x02id\x18\x01 \x01(\x04"\x14\n\x12QueryParamsRequest"\x98\x01\n\x18QueryAllocationsResponse\x12?\n\x0ballocations\x18\x01 \x03(\x0b2$.sentinel.subscription.v2.AllocationB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"Y\n\x17QueryAllocationResponse\x12>\n\nallocation\x18\x01 \x01(\x0b2$.sentinel.subscription.v2.AllocationB\x04\xc8\xde\x1f\x00"\x8c\x01\n\x14QueryPayoutsResponse\x127\n\x07payouts\x18\x01 \x03(\x0b2 .sentinel.subscription.v2.PayoutB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x96\x01\n\x1eQueryPayoutsForAccountResponse\x127\n\x07payouts\x18\x01 \x03(\x0b2 .sentinel.subscription.v2.PayoutB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x93\x01\n\x1bQueryPayoutsForNodeResponse\x127\n\x07payouts\x18\x01 \x03(\x0b2 .sentinel.subscription.v2.PayoutB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"M\n\x13QueryPayoutResponse\x126\n\x06payout\x18\x01 \x01(\x0b2 .sentinel.subscription.v2.PayoutB\x04\xc8\xde\x1f\x00"\x86\x01\n\x1aQuerySubscriptionsResponse\x12+\n\rsubscriptions\x18\x01 \x03(\x0b2\x14.google.protobuf.Any\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x90\x01\n$QuerySubscriptionsForAccountResponse\x12+\n\rsubscriptions\x18\x01 \x03(\x0b2\x14.google.protobuf.Any\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x8d\x01\n!QuerySubscriptionsForNodeResponse\x12+\n\rsubscriptions\x18\x01 \x03(\x0b2\x14.google.protobuf.Any\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x8d\x01\n!QuerySubscriptionsForPlanResponse\x12+\n\rsubscriptions\x18\x01 \x03(\x0b2\x14.google.protobuf.Any\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"G\n\x19QuerySubscriptionResponse\x12*\n\x0csubscription\x18\x01 \x01(\x0b2\x14.google.protobuf.Any"M\n\x13QueryParamsResponse\x126\n\x06params\x18\x01 \x01(\x0b2 .sentinel.subscription.v2.ParamsB\x04\xc8\xde\x1f\x002\xe3\x11\n\x0cQueryService\x12\xc2\x01\n\x0fQueryAllocation\x120.sentinel.subscription.v2.QueryAllocationRequest\x1a1.sentinel.subscription.v2.QueryAllocationResponse"J\x82\xd3\xe4\x93\x02D\x12B/sentinel/subscription/v2/subscriptions/{id}/allocations/{address}\x12\xbb\x01\n\x10QueryAllocations\x121.sentinel.subscription.v2.QueryAllocationsRequest\x1a2.sentinel.subscription.v2.QueryAllocationsResponse"@\x82\xd3\xe4\x93\x02:\x128/sentinel/subscription/v2/subscriptions/{id}/allocations\x12\x98\x01\n\x0cQueryPayouts\x12-.sentinel.subscription.v2.QueryPayoutsRequest\x1a..sentinel.subscription.v2.QueryPayoutsResponse")\x82\xd3\xe4\x93\x02#\x12!/sentinel/subscription/v2/payouts\x12\xc9\x01\n\x16QueryPayoutsForAccount\x127.sentinel.subscription.v2.QueryPayoutsForAccountRequest\x1a8.sentinel.subscription.v2.QueryPayoutsForAccountResponse"<\x82\xd3\xe4\x93\x026\x124/sentinel/subscription/v2/accounts/{address}/payouts\x12\xbd\x01\n\x13QueryPayoutsForNode\x124.sentinel.subscription.v2.QueryPayoutsForNodeRequest\x1a5.sentinel.subscription.v2.QueryPayoutsForNodeResponse"9\x82\xd3\xe4\x93\x023\x121/sentinel/subscription/v2/nodes/{address}/payouts\x12\x9a\x01\n\x0bQueryPayout\x12,.sentinel.subscription.v2.QueryPayoutRequest\x1a-.sentinel.subscription.v2.QueryPayoutResponse".\x82\xd3\xe4\x93\x02(\x12&/sentinel/subscription/v2/payouts/{id}\x12\xb0\x01\n\x12QuerySubscriptions\x123.sentinel.subscription.v2.QuerySubscriptionsRequest\x1a4.sentinel.subscription.v2.QuerySubscriptionsResponse"/\x82\xd3\xe4\x93\x02)\x12\'/sentinel/subscription/v2/subscriptions\x12\xe1\x01\n\x1cQuerySubscriptionsForAccount\x12=.sentinel.subscription.v2.QuerySubscriptionsForAccountRequest\x1a>.sentinel.subscription.v2.QuerySubscriptionsForAccountResponse"B\x82\xd3\xe4\x93\x02<\x12:/sentinel/subscription/v2/accounts/{address}/subscriptions\x12\xd5\x01\n\x19QuerySubscriptionsForNode\x12:.sentinel.subscription.v2.QuerySubscriptionsForNodeRequest\x1a;.sentinel.subscription.v2.QuerySubscriptionsForNodeResponse"?\x82\xd3\xe4\x93\x029\x127/sentinel/subscription/v2/nodes/{address}/subscriptions\x12\xd0\x01\n\x19QuerySubscriptionsForPlan\x12:.sentinel.subscription.v2.QuerySubscriptionsForPlanRequest\x1a;.sentinel.subscription.v2.QuerySubscriptionsForPlanResponse":\x82\xd3\xe4\x93\x024\x122/sentinel/subscription/v2/plans/{id}/subscriptions\x12\xb2\x01\n\x11QuerySubscription\x122.sentinel.subscription.v2.QuerySubscriptionRequest\x1a3.sentinel.subscription.v2.QuerySubscriptionResponse"4\x82\xd3\xe4\x93\x02.\x12,/sentinel/subscription/v2/subscriptions/{id}\x12\x94\x01\n\x0bQueryParams\x12,.sentinel.subscription.v2.QueryParamsRequest\x1a-.sentinel.subscription.v2.QueryParamsResponse"(\x82\xd3\xe4\x93\x02"\x12 /sentinel/subscription/v2/paramsBFZ<github.com/sentinel-official/hub/v12/x/subscription/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.subscription.v2.querier_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/sentinel-official/hub/v12/x/subscription/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_QUERYALLOCATIONSRESPONSE'].fields_by_name['allocations']._loaded_options = None
    _globals['_QUERYALLOCATIONSRESPONSE'].fields_by_name['allocations']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYALLOCATIONRESPONSE'].fields_by_name['allocation']._loaded_options = None
    _globals['_QUERYALLOCATIONRESPONSE'].fields_by_name['allocation']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYPAYOUTSRESPONSE'].fields_by_name['payouts']._loaded_options = None
    _globals['_QUERYPAYOUTSRESPONSE'].fields_by_name['payouts']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYPAYOUTSFORACCOUNTRESPONSE'].fields_by_name['payouts']._loaded_options = None
    _globals['_QUERYPAYOUTSFORACCOUNTRESPONSE'].fields_by_name['payouts']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYPAYOUTSFORNODERESPONSE'].fields_by_name['payouts']._loaded_options = None
    _globals['_QUERYPAYOUTSFORNODERESPONSE'].fields_by_name['payouts']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYPAYOUTRESPONSE'].fields_by_name['payout']._loaded_options = None
    _globals['_QUERYPAYOUTRESPONSE'].fields_by_name['payout']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYSERVICE'].methods_by_name['QueryAllocation']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryAllocation']._serialized_options = b'\x82\xd3\xe4\x93\x02D\x12B/sentinel/subscription/v2/subscriptions/{id}/allocations/{address}'
    _globals['_QUERYSERVICE'].methods_by_name['QueryAllocations']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryAllocations']._serialized_options = b'\x82\xd3\xe4\x93\x02:\x128/sentinel/subscription/v2/subscriptions/{id}/allocations'
    _globals['_QUERYSERVICE'].methods_by_name['QueryPayouts']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryPayouts']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/sentinel/subscription/v2/payouts'
    _globals['_QUERYSERVICE'].methods_by_name['QueryPayoutsForAccount']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryPayoutsForAccount']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/sentinel/subscription/v2/accounts/{address}/payouts'
    _globals['_QUERYSERVICE'].methods_by_name['QueryPayoutsForNode']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryPayoutsForNode']._serialized_options = b'\x82\xd3\xe4\x93\x023\x121/sentinel/subscription/v2/nodes/{address}/payouts'
    _globals['_QUERYSERVICE'].methods_by_name['QueryPayout']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryPayout']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/sentinel/subscription/v2/payouts/{id}'
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscriptions']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscriptions']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/sentinel/subscription/v2/subscriptions"
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscriptionsForAccount']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscriptionsForAccount']._serialized_options = b'\x82\xd3\xe4\x93\x02<\x12:/sentinel/subscription/v2/accounts/{address}/subscriptions'
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscriptionsForNode']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscriptionsForNode']._serialized_options = b'\x82\xd3\xe4\x93\x029\x127/sentinel/subscription/v2/nodes/{address}/subscriptions'
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscriptionsForPlan']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscriptionsForPlan']._serialized_options = b'\x82\xd3\xe4\x93\x024\x122/sentinel/subscription/v2/plans/{id}/subscriptions'
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscription']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscription']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/sentinel/subscription/v2/subscriptions/{id}'
    _globals['_QUERYSERVICE'].methods_by_name['QueryParams']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryParams']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /sentinel/subscription/v2/params'
    _globals['_QUERYALLOCATIONSREQUEST']._serialized_start = 312
    _globals['_QUERYALLOCATIONSREQUEST']._serialized_end = 409
    _globals['_QUERYALLOCATIONREQUEST']._serialized_start = 411
    _globals['_QUERYALLOCATIONREQUEST']._serialized_end = 464
    _globals['_QUERYPAYOUTSREQUEST']._serialized_start = 466
    _globals['_QUERYPAYOUTSREQUEST']._serialized_end = 547
    _globals['_QUERYPAYOUTSFORACCOUNTREQUEST']._serialized_start = 549
    _globals['_QUERYPAYOUTSFORACCOUNTREQUEST']._serialized_end = 657
    _globals['_QUERYPAYOUTSFORNODEREQUEST']._serialized_start = 659
    _globals['_QUERYPAYOUTSFORNODEREQUEST']._serialized_end = 764
    _globals['_QUERYPAYOUTREQUEST']._serialized_start = 766
    _globals['_QUERYPAYOUTREQUEST']._serialized_end = 798
    _globals['_QUERYSUBSCRIPTIONSREQUEST']._serialized_start = 800
    _globals['_QUERYSUBSCRIPTIONSREQUEST']._serialized_end = 887
    _globals['_QUERYSUBSCRIPTIONSFORACCOUNTREQUEST']._serialized_start = 889
    _globals['_QUERYSUBSCRIPTIONSFORACCOUNTREQUEST']._serialized_end = 1003
    _globals['_QUERYSUBSCRIPTIONSFORNODEREQUEST']._serialized_start = 1005
    _globals['_QUERYSUBSCRIPTIONSFORNODEREQUEST']._serialized_end = 1116
    _globals['_QUERYSUBSCRIPTIONSFORPLANREQUEST']._serialized_start = 1118
    _globals['_QUERYSUBSCRIPTIONSFORPLANREQUEST']._serialized_end = 1224
    _globals['_QUERYSUBSCRIPTIONREQUEST']._serialized_start = 1226
    _globals['_QUERYSUBSCRIPTIONREQUEST']._serialized_end = 1264
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 1266
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 1286
    _globals['_QUERYALLOCATIONSRESPONSE']._serialized_start = 1289
    _globals['_QUERYALLOCATIONSRESPONSE']._serialized_end = 1441
    _globals['_QUERYALLOCATIONRESPONSE']._serialized_start = 1443
    _globals['_QUERYALLOCATIONRESPONSE']._serialized_end = 1532
    _globals['_QUERYPAYOUTSRESPONSE']._serialized_start = 1535
    _globals['_QUERYPAYOUTSRESPONSE']._serialized_end = 1675
    _globals['_QUERYPAYOUTSFORACCOUNTRESPONSE']._serialized_start = 1678
    _globals['_QUERYPAYOUTSFORACCOUNTRESPONSE']._serialized_end = 1828
    _globals['_QUERYPAYOUTSFORNODERESPONSE']._serialized_start = 1831
    _globals['_QUERYPAYOUTSFORNODERESPONSE']._serialized_end = 1978
    _globals['_QUERYPAYOUTRESPONSE']._serialized_start = 1980
    _globals['_QUERYPAYOUTRESPONSE']._serialized_end = 2057
    _globals['_QUERYSUBSCRIPTIONSRESPONSE']._serialized_start = 2060
    _globals['_QUERYSUBSCRIPTIONSRESPONSE']._serialized_end = 2194
    _globals['_QUERYSUBSCRIPTIONSFORACCOUNTRESPONSE']._serialized_start = 2197
    _globals['_QUERYSUBSCRIPTIONSFORACCOUNTRESPONSE']._serialized_end = 2341
    _globals['_QUERYSUBSCRIPTIONSFORNODERESPONSE']._serialized_start = 2344
    _globals['_QUERYSUBSCRIPTIONSFORNODERESPONSE']._serialized_end = 2485
    _globals['_QUERYSUBSCRIPTIONSFORPLANRESPONSE']._serialized_start = 2488
    _globals['_QUERYSUBSCRIPTIONSFORPLANRESPONSE']._serialized_end = 2629
    _globals['_QUERYSUBSCRIPTIONRESPONSE']._serialized_start = 2631
    _globals['_QUERYSUBSCRIPTIONRESPONSE']._serialized_end = 2702
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 2704
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 2781
    _globals['_QUERYSERVICE']._serialized_start = 2784
    _globals['_QUERYSERVICE']._serialized_end = 5059