
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.session.v1 import params_pb2 as sentinel_dot_session_dot_v1_dot_params__pb2
from ....sentinel.session.v1 import session_pb2 as sentinel_dot_session_dot_v1_dot_session__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!sentinel/session/v1/genesis.proto\x12\x13sentinel.session.v1\x1a\x14gogoproto/gogo.proto\x1a sentinel/session/v1/params.proto\x1a!sentinel/session/v1/session.proto"\x86\x01\n\x0cGenesisState\x12C\n\x08sessions\x18\x01 \x03(\x0b2\x1c.sentinel.session.v1.SessionB\x13\xea\xde\x1f\x0b_,omitempty\xc8\xde\x1f\x00\x121\n\x06params\x18\x02 \x01(\x0b2\x1b.sentinel.session.v1.ParamsB\x04\xc8\xde\x1f\x00BAZ7github.com/sentinel-official/hub/v12/x/session/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.session.v1.genesis_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/sentinel-official/hub/v12/x/session/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _GENESISSTATE.fields_by_name['sessions']._options = None
    _GENESISSTATE.fields_by_name['sessions']._serialized_options = b'\xea\xde\x1f\x0b_,omitempty\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE._serialized_start = 150
    _GENESISSTATE._serialized_end = 284
