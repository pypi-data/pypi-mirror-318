
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.mint.v1 import inflation_pb2 as sentinel_dot_mint_dot_v1_dot_inflation__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esentinel/mint/v1/genesis.proto\x12\x10sentinel.mint.v1\x1a\x14gogoproto/gogo.proto\x1a sentinel/mint/v1/inflation.proto"Z\n\x0cGenesisState\x12J\n\ninflations\x18\x01 \x03(\x0b2\x1b.sentinel.mint.v1.InflationB\x19\xf2\xde\x1f\x11yaml:"inflations"\xc8\xde\x1f\x00B>Z4github.com/sentinel-official/hub/v12/x/mint/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.mint.v1.genesis_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/mint/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _GENESISSTATE.fields_by_name['inflations']._options = None
    _GENESISSTATE.fields_by_name['inflations']._serialized_options = b'\xf2\xde\x1f\x11yaml:"inflations"\xc8\xde\x1f\x00'
    _GENESISSTATE._serialized_start = 108
    _GENESISSTATE._serialized_end = 198
