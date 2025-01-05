"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/mint/v1/genesis.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.mint.v1 import inflation_pb2 as sentinel_dot_mint_dot_v1_dot_inflation__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esentinel/mint/v1/genesis.proto\x12\x10sentinel.mint.v1\x1a\x14gogoproto/gogo.proto\x1a sentinel/mint/v1/inflation.proto"Z\n\x0cGenesisState\x12J\n\ninflations\x18\x01 \x03(\x0b2\x1b.sentinel.mint.v1.InflationB\x19\xc8\xde\x1f\x00\xf2\xde\x1f\x11yaml:"inflations"B>Z4github.com/sentinel-official/hub/v12/x/mint/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.mint.v1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/mint/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_GENESISSTATE'].fields_by_name['inflations']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['inflations']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x11yaml:"inflations"'
    _globals['_GENESISSTATE']._serialized_start = 108
    _globals['_GENESISSTATE']._serialized_end = 198