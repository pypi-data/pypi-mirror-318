"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/deposit/v1/genesis.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.deposit.v1 import deposit_pb2 as sentinel_dot_deposit_dot_v1_dot_deposit__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!sentinel/deposit/v1/genesis.proto\x12\x13sentinel.deposit.v1\x1a\x14gogoproto/gogo.proto\x1a!sentinel/deposit/v1/deposit.proto"W\n\x0cGenesisState\x12G\n\x08deposits\x18\x01 \x03(\x0b2\x1c.sentinel.deposit.v1.DepositB\x17\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"deposits"BAZ7github.com/sentinel-official/hub/v12/x/deposit/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.deposit.v1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/sentinel-official/hub/v12/x/deposit/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_GENESISSTATE'].fields_by_name['deposits']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['deposits']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"deposits"'
    _globals['_GENESISSTATE']._serialized_start = 115
    _globals['_GENESISSTATE']._serialized_end = 202