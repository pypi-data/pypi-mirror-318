"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/subscription/v1/querier.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....sentinel.subscription.v1 import params_pb2 as sentinel_dot_subscription_dot_v1_dot_params__pb2
from ....sentinel.subscription.v1 import quota_pb2 as sentinel_dot_subscription_dot_v1_dot_quota__pb2
from ....sentinel.subscription.v1 import subscription_pb2 as sentinel_dot_subscription_dot_v1_dot_subscription__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&sentinel/subscription/v1/querier.proto\x12\x18sentinel.subscription.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a%sentinel/subscription/v1/params.proto\x1a$sentinel/subscription/v1/quota.proto\x1a+sentinel/subscription/v1/subscription.proto\x1a\x1esentinel/types/v1/status.proto"\\\n\x12QueryQuotasRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"0\n\x11QueryQuotaRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0f\n\x07address\x18\x02 \x01(\t"W\n\x19QuerySubscriptionsRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x9d\x01\n#QuerySubscriptionsForAddressRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12)\n\x06status\x18\x02 \x01(\x0e2\x19.sentinel.types.v1.Status\x12:\n\npagination\x18\x03 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"&\n\x18QuerySubscriptionRequest\x12\n\n\x02id\x18\x01 \x01(\x04"\x14\n\x12QueryParamsRequest"\x89\x01\n\x13QueryQuotasResponse\x125\n\x06quotas\x18\x01 \x03(\x0b2\x1f.sentinel.subscription.v1.QuotaB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"J\n\x12QueryQuotaResponse\x124\n\x05quota\x18\x01 \x01(\x0b2\x1f.sentinel.subscription.v1.QuotaB\x04\xc8\xde\x1f\x00"\x9e\x01\n\x1aQuerySubscriptionsResponse\x12C\n\rsubscriptions\x18\x01 \x03(\x0b2&.sentinel.subscription.v1.SubscriptionB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\xa8\x01\n$QuerySubscriptionsForAddressResponse\x12C\n\rsubscriptions\x18\x01 \x03(\x0b2&.sentinel.subscription.v1.SubscriptionB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"_\n\x19QuerySubscriptionResponse\x12B\n\x0csubscription\x18\x01 \x01(\x0b2&.sentinel.subscription.v1.SubscriptionB\x04\xc8\xde\x1f\x00"M\n\x13QueryParamsResponse\x126\n\x06params\x18\x01 \x01(\x0b2 .sentinel.subscription.v1.ParamsB\x04\xc8\xde\x1f\x002\xd5\x08\n\x0cQueryService\x12\xa7\x01\n\x0bQueryQuotas\x12,.sentinel.subscription.v1.QueryQuotasRequest\x1a-.sentinel.subscription.v1.QueryQuotasResponse";\x82\xd3\xe4\x93\x025\x123/sentinel/subscription/v1/subscriptions/{id}/quotas\x12\xb7\x01\n\nQueryQuota\x12+.sentinel.subscription.v1.QueryQuotaRequest\x1a,.sentinel.subscription.v1.QueryQuotaResponse"N\x82\xd3\xe4\x93\x02H\x12F/sentinel/subscription/v1/accounts/{address}/subscriptions/{id}/quotas\x12\xb0\x01\n\x12QuerySubscriptions\x123.sentinel.subscription.v1.QuerySubscriptionsRequest\x1a4.sentinel.subscription.v1.QuerySubscriptionsResponse"/\x82\xd3\xe4\x93\x02)\x12\'/sentinel/subscription/v1/subscriptions\x12\xe1\x01\n\x1cQuerySubscriptionsForAddress\x12=.sentinel.subscription.v1.QuerySubscriptionsForAddressRequest\x1a>.sentinel.subscription.v1.QuerySubscriptionsForAddressResponse"B\x82\xd3\xe4\x93\x02<\x12:/sentinel/subscription/v1/accounts/{address}/subscriptions\x12\xb2\x01\n\x11QuerySubscription\x122.sentinel.subscription.v1.QuerySubscriptionRequest\x1a3.sentinel.subscription.v1.QuerySubscriptionResponse"4\x82\xd3\xe4\x93\x02.\x12,/sentinel/subscription/v1/subscriptions/{id}\x12\x94\x01\n\x0bQueryParams\x12,.sentinel.subscription.v1.QueryParamsRequest\x1a-.sentinel.subscription.v1.QueryParamsResponse"(\x82\xd3\xe4\x93\x02"\x12 /sentinel/subscription/v1/paramsBFZ<github.com/sentinel-official/hub/v12/x/subscription/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.subscription.v1.querier_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/sentinel-official/hub/v12/x/subscription/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_QUERYQUOTASRESPONSE'].fields_by_name['quotas']._loaded_options = None
    _globals['_QUERYQUOTASRESPONSE'].fields_by_name['quotas']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYQUOTARESPONSE'].fields_by_name['quota']._loaded_options = None
    _globals['_QUERYQUOTARESPONSE'].fields_by_name['quota']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYSUBSCRIPTIONSRESPONSE'].fields_by_name['subscriptions']._loaded_options = None
    _globals['_QUERYSUBSCRIPTIONSRESPONSE'].fields_by_name['subscriptions']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYSUBSCRIPTIONSFORADDRESSRESPONSE'].fields_by_name['subscriptions']._loaded_options = None
    _globals['_QUERYSUBSCRIPTIONSFORADDRESSRESPONSE'].fields_by_name['subscriptions']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYSUBSCRIPTIONRESPONSE'].fields_by_name['subscription']._loaded_options = None
    _globals['_QUERYSUBSCRIPTIONRESPONSE'].fields_by_name['subscription']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYSERVICE'].methods_by_name['QueryQuotas']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryQuotas']._serialized_options = b'\x82\xd3\xe4\x93\x025\x123/sentinel/subscription/v1/subscriptions/{id}/quotas'
    _globals['_QUERYSERVICE'].methods_by_name['QueryQuota']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryQuota']._serialized_options = b'\x82\xd3\xe4\x93\x02H\x12F/sentinel/subscription/v1/accounts/{address}/subscriptions/{id}/quotas'
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscriptions']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscriptions']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/sentinel/subscription/v1/subscriptions"
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscriptionsForAddress']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscriptionsForAddress']._serialized_options = b'\x82\xd3\xe4\x93\x02<\x12:/sentinel/subscription/v1/accounts/{address}/subscriptions'
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscription']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QuerySubscription']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/sentinel/subscription/v1/subscriptions/{id}'
    _globals['_QUERYSERVICE'].methods_by_name['QueryParams']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryParams']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /sentinel/subscription/v1/params'
    _globals['_QUERYQUOTASREQUEST']._serialized_start = 318
    _globals['_QUERYQUOTASREQUEST']._serialized_end = 410
    _globals['_QUERYQUOTAREQUEST']._serialized_start = 412
    _globals['_QUERYQUOTAREQUEST']._serialized_end = 460
    _globals['_QUERYSUBSCRIPTIONSREQUEST']._serialized_start = 462
    _globals['_QUERYSUBSCRIPTIONSREQUEST']._serialized_end = 549
    _globals['_QUERYSUBSCRIPTIONSFORADDRESSREQUEST']._serialized_start = 552
    _globals['_QUERYSUBSCRIPTIONSFORADDRESSREQUEST']._serialized_end = 709
    _globals['_QUERYSUBSCRIPTIONREQUEST']._serialized_start = 711
    _globals['_QUERYSUBSCRIPTIONREQUEST']._serialized_end = 749
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 751
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 771
    _globals['_QUERYQUOTASRESPONSE']._serialized_start = 774
    _globals['_QUERYQUOTASRESPONSE']._serialized_end = 911
    _globals['_QUERYQUOTARESPONSE']._serialized_start = 913
    _globals['_QUERYQUOTARESPONSE']._serialized_end = 987
    _globals['_QUERYSUBSCRIPTIONSRESPONSE']._serialized_start = 990
    _globals['_QUERYSUBSCRIPTIONSRESPONSE']._serialized_end = 1148
    _globals['_QUERYSUBSCRIPTIONSFORADDRESSRESPONSE']._serialized_start = 1151
    _globals['_QUERYSUBSCRIPTIONSFORADDRESSRESPONSE']._serialized_end = 1319
    _globals['_QUERYSUBSCRIPTIONRESPONSE']._serialized_start = 1321
    _globals['_QUERYSUBSCRIPTIONRESPONSE']._serialized_end = 1416
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 1418
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 1495
    _globals['_QUERYSERVICE']._serialized_start = 1498
    _globals['_QUERYSERVICE']._serialized_end = 2607