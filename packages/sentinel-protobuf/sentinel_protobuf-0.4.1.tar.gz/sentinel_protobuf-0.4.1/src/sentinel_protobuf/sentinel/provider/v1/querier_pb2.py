"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/provider/v1/querier.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....sentinel.provider.v1 import params_pb2 as sentinel_dot_provider_dot_v1_dot_params__pb2
from ....sentinel.provider.v1 import provider_pb2 as sentinel_dot_provider_dot_v1_dot_provider__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"sentinel/provider/v1/querier.proto\x12\x14sentinel.provider.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a!sentinel/provider/v1/params.proto\x1a#sentinel/provider/v1/provider.proto"S\n\x15QueryProvidersRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\'\n\x14QueryProviderRequest\x12\x0f\n\x07address\x18\x01 \x01(\t"\x14\n\x12QueryParamsRequest"\x8e\x01\n\x16QueryProvidersResponse\x127\n\tproviders\x18\x01 \x03(\x0b2\x1e.sentinel.provider.v1.ProviderB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"O\n\x15QueryProviderResponse\x126\n\x08provider\x18\x01 \x01(\x0b2\x1e.sentinel.provider.v1.ProviderB\x04\xc8\xde\x1f\x00"I\n\x13QueryParamsResponse\x122\n\x06params\x18\x01 \x01(\x0b2\x1c.sentinel.provider.v1.ParamsB\x04\xc8\xde\x1f\x002\xce\x03\n\x0cQueryService\x12\x94\x01\n\x0eQueryProviders\x12+.sentinel.provider.v1.QueryProvidersRequest\x1a,.sentinel.provider.v1.QueryProvidersResponse"\'\x82\xd3\xe4\x93\x02!\x12\x1f/sentinel/provider/v1/providers\x12\x9b\x01\n\rQueryProvider\x12*.sentinel.provider.v1.QueryProviderRequest\x1a+.sentinel.provider.v1.QueryProviderResponse"1\x82\xd3\xe4\x93\x02+\x12)/sentinel/provider/v1/providers/{address}\x12\x88\x01\n\x0bQueryParams\x12(.sentinel.provider.v1.QueryParamsRequest\x1a).sentinel.provider.v1.QueryParamsResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/sentinel/provider/v1/paramsBBZ8github.com/sentinel-official/hub/v12/x/provider/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.provider.v1.querier_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z8github.com/sentinel-official/hub/v12/x/provider/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_QUERYPROVIDERSRESPONSE'].fields_by_name['providers']._loaded_options = None
    _globals['_QUERYPROVIDERSRESPONSE'].fields_by_name['providers']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYPROVIDERRESPONSE'].fields_by_name['provider']._loaded_options = None
    _globals['_QUERYPROVIDERRESPONSE'].fields_by_name['provider']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYSERVICE'].methods_by_name['QueryProviders']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryProviders']._serialized_options = b'\x82\xd3\xe4\x93\x02!\x12\x1f/sentinel/provider/v1/providers'
    _globals['_QUERYSERVICE'].methods_by_name['QueryProvider']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryProvider']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/sentinel/provider/v1/providers/{address}'
    _globals['_QUERYSERVICE'].methods_by_name['QueryParams']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryParams']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/sentinel/provider/v1/params'
    _globals['_QUERYPROVIDERSREQUEST']._serialized_start = 228
    _globals['_QUERYPROVIDERSREQUEST']._serialized_end = 311
    _globals['_QUERYPROVIDERREQUEST']._serialized_start = 313
    _globals['_QUERYPROVIDERREQUEST']._serialized_end = 352
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 354
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 374
    _globals['_QUERYPROVIDERSRESPONSE']._serialized_start = 377
    _globals['_QUERYPROVIDERSRESPONSE']._serialized_end = 519
    _globals['_QUERYPROVIDERRESPONSE']._serialized_start = 521
    _globals['_QUERYPROVIDERRESPONSE']._serialized_end = 600
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 602
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 675
    _globals['_QUERYSERVICE']._serialized_start = 678
    _globals['_QUERYSERVICE']._serialized_end = 1140