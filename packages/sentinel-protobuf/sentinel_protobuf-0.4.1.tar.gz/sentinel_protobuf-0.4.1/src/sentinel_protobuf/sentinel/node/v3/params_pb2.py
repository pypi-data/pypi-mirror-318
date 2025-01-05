"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/node/v3/params.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ....sentinel.types.v1 import price_pb2 as sentinel_dot_types_dot_v1_dot_price__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsentinel/node/v3/params.proto\x12\x10sentinel.node.v3\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1dsentinel/types/v1/price.proto"\xa0\x03\n\x06Params\x120\n\x07deposit\x18\x01 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12<\n\x0factive_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12;\n\x13min_gigabyte_prices\x18\x03 \x03(\x0b2\x18.sentinel.types.v1.PriceB\x04\xc8\xde\x1f\x00\x129\n\x11min_hourly_prices\x18\x04 \x03(\x0b2\x18.sentinel.types.v1.PriceB\x04\xc8\xde\x1f\x00\x12\x1d\n\x15max_session_gigabytes\x18\x05 \x01(\x03\x12\x1d\n\x15min_session_gigabytes\x18\x06 \x01(\x03\x12\x19\n\x11max_session_hours\x18\x07 \x01(\x03\x12\x19\n\x11min_session_hours\x18\x08 \x01(\x03\x12:\n\rstaking_share\x18\t \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDecB>Z4github.com/sentinel-official/hub/v12/x/node/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.node.v3.params_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/node/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_PARAMS'].fields_by_name['deposit']._loaded_options = None
    _globals['_PARAMS'].fields_by_name['deposit']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_PARAMS'].fields_by_name['active_duration']._loaded_options = None
    _globals['_PARAMS'].fields_by_name['active_duration']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _globals['_PARAMS'].fields_by_name['min_gigabyte_prices']._loaded_options = None
    _globals['_PARAMS'].fields_by_name['min_gigabyte_prices']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_PARAMS'].fields_by_name['min_hourly_prices']._loaded_options = None
    _globals['_PARAMS'].fields_by_name['min_hourly_prices']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_PARAMS'].fields_by_name['staking_share']._loaded_options = None
    _globals['_PARAMS'].fields_by_name['staking_share']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec'
    _globals['_PARAMS']._serialized_start = 169
    _globals['_PARAMS']._serialized_end = 585