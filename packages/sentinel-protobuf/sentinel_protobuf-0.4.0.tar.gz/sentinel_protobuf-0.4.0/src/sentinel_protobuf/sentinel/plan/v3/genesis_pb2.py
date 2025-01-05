
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.plan.v3 import plan_pb2 as sentinel_dot_plan_dot_v3_dot_plan__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esentinel/plan/v3/genesis.proto\x12\x10sentinel.plan.v3\x1a\x14gogoproto/gogo.proto\x1a\x1bsentinel/plan/v3/plan.proto"H\n\x0bGenesisPlan\x12*\n\x04plan\x18\x01 \x01(\x0b2\x16.sentinel.plan.v3.PlanB\x04\xc8\xde\x1f\x00\x12\r\n\x05nodes\x18\x02 \x03(\t"R\n\x0cGenesisState\x12B\n\x05plans\x18\x01 \x03(\x0b2\x1d.sentinel.plan.v3.GenesisPlanB\x14\xf2\xde\x1f\x0cyaml:"plans"\xc8\xde\x1f\x00B>Z4github.com/sentinel-official/hub/v12/x/plan/types/v3\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.plan.v3.genesis_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/plan/types/v3\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _GENESISPLAN.fields_by_name['plan']._options = None
    _GENESISPLAN.fields_by_name['plan']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['plans']._options = None
    _GENESISSTATE.fields_by_name['plans']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"plans"\xc8\xde\x1f\x00'
    _GENESISPLAN._serialized_start = 103
    _GENESISPLAN._serialized_end = 175
    _GENESISSTATE._serialized_start = 177
    _GENESISSTATE._serialized_end = 259
