"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/oracle/v1/querier.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....sentinel.oracle.v1 import asset_pb2 as sentinel_dot_oracle_dot_v1_dot_asset__pb2
from ....sentinel.oracle.v1 import params_pb2 as sentinel_dot_oracle_dot_v1_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n sentinel/oracle/v1/querier.proto\x12\x12sentinel.oracle.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1esentinel/oracle/v1/asset.proto\x1a\x1fsentinel/oracle/v1/params.proto"P\n\x12QueryAssetsRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest""\n\x11QueryAssetRequest\x12\r\n\x05denom\x18\x01 \x01(\t"\x14\n\x12QueryParamsRequest"\x83\x01\n\x13QueryAssetsResponse\x12/\n\x06assets\x18\x01 \x03(\x0b2\x19.sentinel.oracle.v1.AssetB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"D\n\x12QueryAssetResponse\x12.\n\x05asset\x18\x01 \x01(\x0b2\x19.sentinel.oracle.v1.AssetB\x04\xc8\xde\x1f\x00"G\n\x13QueryParamsResponse\x120\n\x06params\x18\x01 \x01(\x0b2\x1a.sentinel.oracle.v1.ParamsB\x04\xc8\xde\x1f\x002\xa2\x03\n\x0cQueryService\x12\x82\x01\n\x0bQueryAssets\x12&.sentinel.oracle.v1.QueryAssetsRequest\x1a\'.sentinel.oracle.v1.QueryAssetsResponse""\x82\xd3\xe4\x93\x02\x1c\x12\x1a/sentinel/oracle/v1/assets\x12\x87\x01\n\nQueryAsset\x12%.sentinel.oracle.v1.QueryAssetRequest\x1a&.sentinel.oracle.v1.QueryAssetResponse"*\x82\xd3\xe4\x93\x02$\x12"/sentinel/oracle/v1/assets/{denom}\x12\x82\x01\n\x0bQueryParams\x12&.sentinel.oracle.v1.QueryParamsRequest\x1a\'.sentinel.oracle.v1.QueryParamsResponse""\x82\xd3\xe4\x93\x02\x1c\x12\x1a/sentinel/oracle/v1/paramsB@Z6github.com/sentinel-official/hub/v12/x/oracle/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.oracle.v1.querier_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z6github.com/sentinel-official/hub/v12/x/oracle/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_QUERYASSETSRESPONSE'].fields_by_name['assets']._loaded_options = None
    _globals['_QUERYASSETSRESPONSE'].fields_by_name['assets']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYASSETRESPONSE'].fields_by_name['asset']._loaded_options = None
    _globals['_QUERYASSETRESPONSE'].fields_by_name['asset']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYSERVICE'].methods_by_name['QueryAssets']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryAssets']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x12\x1a/sentinel/oracle/v1/assets'
    _globals['_QUERYSERVICE'].methods_by_name['QueryAsset']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryAsset']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/sentinel/oracle/v1/assets/{denom}'
    _globals['_QUERYSERVICE'].methods_by_name['QueryParams']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryParams']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x12\x1a/sentinel/oracle/v1/params'
    _globals['_QUERYASSETSREQUEST']._serialized_start = 217
    _globals['_QUERYASSETSREQUEST']._serialized_end = 297
    _globals['_QUERYASSETREQUEST']._serialized_start = 299
    _globals['_QUERYASSETREQUEST']._serialized_end = 333
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 335
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 355
    _globals['_QUERYASSETSRESPONSE']._serialized_start = 358
    _globals['_QUERYASSETSRESPONSE']._serialized_end = 489
    _globals['_QUERYASSETRESPONSE']._serialized_start = 491
    _globals['_QUERYASSETRESPONSE']._serialized_end = 559
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 561
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 632
    _globals['_QUERYSERVICE']._serialized_start = 635
    _globals['_QUERYSERVICE']._serialized_end = 1053