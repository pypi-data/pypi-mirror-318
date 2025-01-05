"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/swap/v1/swap.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bsentinel/swap/v1/swap.proto\x12\x10sentinel.swap.v1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto"Z\n\x04Swap\x12\x0f\n\x07tx_hash\x18\x01 \x01(\x0c\x12\x10\n\x08receiver\x18\x02 \x01(\t\x12/\n\x06amount\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00B>Z4github.com/sentinel-official/hub/v12/x/swap/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.swap.v1.swap_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/swap/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_SWAP'].fields_by_name['amount']._loaded_options = None
    _globals['_SWAP'].fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_SWAP']._serialized_start = 103
    _globals['_SWAP']._serialized_end = 193