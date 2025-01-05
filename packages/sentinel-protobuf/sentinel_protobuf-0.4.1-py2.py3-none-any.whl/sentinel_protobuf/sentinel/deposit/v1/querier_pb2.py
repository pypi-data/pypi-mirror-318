"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/deposit/v1/querier.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....sentinel.deposit.v1 import deposit_pb2 as sentinel_dot_deposit_dot_v1_dot_deposit__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!sentinel/deposit/v1/querier.proto\x12\x13sentinel.deposit.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a!sentinel/deposit/v1/deposit.proto"R\n\x14QueryDepositsRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"&\n\x13QueryDepositRequest\x12\x0f\n\x07address\x18\x01 \x01(\t"\x8a\x01\n\x15QueryDepositsResponse\x124\n\x08deposits\x18\x01 \x03(\x0b2\x1c.sentinel.deposit.v1.DepositB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"K\n\x14QueryDepositResponse\x123\n\x07deposit\x18\x01 \x01(\x0b2\x1c.sentinel.deposit.v1.DepositB\x04\xc8\xde\x1f\x002\xb5\x02\n\x0cQueryService\x12\x8d\x01\n\rQueryDeposits\x12).sentinel.deposit.v1.QueryDepositsRequest\x1a*.sentinel.deposit.v1.QueryDepositsResponse"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/sentinel/deposit/v1/deposits\x12\x94\x01\n\x0cQueryDeposit\x12(.sentinel.deposit.v1.QueryDepositRequest\x1a).sentinel.deposit.v1.QueryDepositResponse"/\x82\xd3\xe4\x93\x02)\x12\'/sentinel/deposit/v1/deposits/{address}BAZ7github.com/sentinel-official/hub/v12/x/deposit/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.deposit.v1.querier_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/sentinel-official/hub/v12/x/deposit/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_QUERYDEPOSITSRESPONSE'].fields_by_name['deposits']._loaded_options = None
    _globals['_QUERYDEPOSITSRESPONSE'].fields_by_name['deposits']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYDEPOSITRESPONSE'].fields_by_name['deposit']._loaded_options = None
    _globals['_QUERYDEPOSITRESPONSE'].fields_by_name['deposit']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYSERVICE'].methods_by_name['QueryDeposits']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryDeposits']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f\x12\x1d/sentinel/deposit/v1/deposits'
    _globals['_QUERYSERVICE'].methods_by_name['QueryDeposit']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryDeposit']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/sentinel/deposit/v1/deposits/{address}"
    _globals['_QUERYDEPOSITSREQUEST']._serialized_start = 189
    _globals['_QUERYDEPOSITSREQUEST']._serialized_end = 271
    _globals['_QUERYDEPOSITREQUEST']._serialized_start = 273
    _globals['_QUERYDEPOSITREQUEST']._serialized_end = 311
    _globals['_QUERYDEPOSITSRESPONSE']._serialized_start = 314
    _globals['_QUERYDEPOSITSRESPONSE']._serialized_end = 452
    _globals['_QUERYDEPOSITRESPONSE']._serialized_start = 454
    _globals['_QUERYDEPOSITRESPONSE']._serialized_end = 529
    _globals['_QUERYSERVICE']._serialized_start = 532
    _globals['_QUERYSERVICE']._serialized_end = 841