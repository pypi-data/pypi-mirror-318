"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/deposit/v1/deposit.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!sentinel/deposit/v1/deposit.proto\x12\x13sentinel.deposit.v1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto"v\n\x07Deposit\x12\x0f\n\x07address\x18\x01 \x01(\t\x12Z\n\x05coins\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsBAZ7github.com/sentinel-official/hub/v12/x/deposit/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.deposit.v1.deposit_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/sentinel-official/hub/v12/x/deposit/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_DEPOSIT'].fields_by_name['coins']._loaded_options = None
    _globals['_DEPOSIT'].fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_DEPOSIT']._serialized_start = 112
    _globals['_DEPOSIT']._serialized_end = 230