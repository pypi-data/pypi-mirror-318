"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/subscription/v3/querier.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....sentinel.subscription.v3 import subscription_pb2 as sentinel_dot_subscription_dot_v3_dot_subscription__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&sentinel/subscription/v3/querier.proto\x12\x18sentinel.subscription.v3\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a+sentinel/subscription/v3/subscription.proto"W\n\x19QuerySubscriptionsRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"r\n#QuerySubscriptionsForAccountRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"j\n QuerySubscriptionsForPlanRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"&\n\x18QuerySubscriptionRequest\x12\n\n\x02id\x18\x01 \x01(\x04"\x9e\x01\n\x1aQuerySubscriptionsResponse\x12C\n\rsubscriptions\x18\x01 \x03(\x0b2&.sentinel.subscription.v3.SubscriptionB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\xa8\x01\n$QuerySubscriptionsForAccountResponse\x12C\n\rsubscriptions\x18\x01 \x03(\x0b2&.sentinel.subscription.v3.SubscriptionB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\xa5\x01\n!QuerySubscriptionsForPlanResponse\x12C\n\rsubscriptions\x18\x01 \x03(\x0b2&.sentinel.subscription.v3.SubscriptionB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"_\n\x19QuerySubscriptionResponse\x12B\n\x0csubscription\x18\x01 \x01(\x0b2&.sentinel.subscription.v3.SubscriptionB\x04\xc8\xde\x1f\x002\xad\x06\n\x0cQueryService\x12\xb0\x01\n\x12QuerySubscriptions\x123.sentinel.subscription.v3.QuerySubscriptionsRequest\x1a4.sentinel.subscription.v3.QuerySubscriptionsResponse"/\x82\xd3\xe4\x93\x02)\x12\'/sentinel/subscription/v3/subscriptions\x12\xe1\x01\n\x1cQuerySubscriptionsForAccount\x12=.sentinel.subscription.v3.QuerySubscriptionsForAccountRequest\x1a>.sentinel.subscription.v3.QuerySubscriptionsForAccountResponse"B\x82\xd3\xe4\x93\x02<\x12:/sentinel/subscription/v3/accounts/{address}/subscriptions\x12\xd0\x01\n\x19QuerySubscriptionsForPlan\x12:.sentinel.subscription.v3.QuerySubscriptionsForPlanRequest\x1a;.sentinel.subscription.v3.QuerySubscriptionsForPlanResponse":\x82\xd3\xe4\x93\x024\x122/sentinel/subscription/v3/plans/{id}/subscriptions\x12\xb2\x01\n\x11QuerySubscription\x122.sentinel.subscription.v3.QuerySubscriptionRequest\x1a3.sentinel.subscription.v3.QuerySubscriptionResponse"4\x82\xd3\xe4\x93\x02.\x12,/sentinel/subscription/v3/subscriptions/{id}BFZ<github.com/sentinel-official/hub/v12/x/subscription/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.subscription.v3.querier_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/sentinel-official/hub/v12/x/subscription/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_QUERYSUBSCRIPTIONSRESPONSE'].fields_by_name['subscriptions']._loaded_options = None
    _globals['_QUERYSUBSCRIPTIONSRESPONSE'].fields_by_name['subscriptions']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYSUBSCRIPTIONSFORACCOUNTRESPONSE'].fields_by_name['subscriptions']._loaded_options = None
    _globals['_QUERYSUBSCRIPTIONSFORACCOUNTRESPONSE'].fields_by_name['subscriptions']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYSUBSCRIPTIONSFORPLANRESPONSE'].fields_by_name['subscriptions']._loaded_options = None
    _globals['_QUERYSUBSCRIPTIONSFORPLANRESPONSE'].fields_by_name['subscriptions']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYSUBSCRIPTIONRESPONSE'].fields_by_name['subscription']._loaded_options = None
    _globals['_QUERYSUBSCRIPTIONRESPONSE'].fields_by_name['subscription']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscriptions']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscriptions']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/sentinel/subscription/v3/subscriptions"
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscriptionsForAccount']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscriptionsForAccount']._serialized_options = b'\x82\xd3\xe4\x93\x02<\x12:/sentinel/subscription/v3/accounts/{address}/subscriptions'
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscriptionsForPlan']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscriptionsForPlan']._serialized_options = b'\x82\xd3\xe4\x93\x024\x122/sentinel/subscription/v3/plans/{id}/subscriptions'
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscription']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscription']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/sentinel/subscription/v3/subscriptions/{id}'
    _globals['_QUERYSUBSCRIPTIONSREQUEST']._serialized_start = 209
    _globals['_QUERYSUBSCRIPTIONSREQUEST']._serialized_end = 296
    _globals['_QUERYSUBSCRIPTIONSFORACCOUNTREQUEST']._serialized_start = 298
    _globals['_QUERYSUBSCRIPTIONSFORACCOUNTREQUEST']._serialized_end = 412
    _globals['_QUERYSUBSCRIPTIONSFORPLANREQUEST']._serialized_start = 414
    _globals['_QUERYSUBSCRIPTIONSFORPLANREQUEST']._serialized_end = 520
    _globals['_QUERYSUBSCRIPTIONREQUEST']._serialized_start = 522
    _globals['_QUERYSUBSCRIPTIONREQUEST']._serialized_end = 560
    _globals['_QUERYSUBSCRIPTIONSRESPONSE']._serialized_start = 563
    _globals['_QUERYSUBSCRIPTIONSRESPONSE']._serialized_end = 721
    _globals['_QUERYSUBSCRIPTIONSFORACCOUNTRESPONSE']._serialized_start = 724
    _globals['_QUERYSUBSCRIPTIONSFORACCOUNTRESPONSE']._serialized_end = 892
    _globals['_QUERYSUBSCRIPTIONSFORPLANRESPONSE']._serialized_start = 895
    _globals['_QUERYSUBSCRIPTIONSFORPLANRESPONSE']._serialized_end = 1060
    _globals['_QUERYSUBSCRIPTIONRESPONSE']._serialized_start = 1062
    _globals['_QUERYSUBSCRIPTIONRESPONSE']._serialized_end = 1157
    _globals['_QUERYSERVICE']._serialized_start = 1160
    _globals['_QUERYSERVICE']._serialized_end = 1973