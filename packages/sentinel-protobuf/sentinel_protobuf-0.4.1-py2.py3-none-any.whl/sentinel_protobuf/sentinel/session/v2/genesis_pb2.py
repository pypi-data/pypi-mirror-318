"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/session/v2/genesis.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.session.v2 import params_pb2 as sentinel_dot_session_dot_v2_dot_params__pb2
from ....sentinel.session.v2 import session_pb2 as sentinel_dot_session_dot_v2_dot_session__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!sentinel/session/v2/genesis.proto\x12\x13sentinel.session.v2\x1a\x14gogoproto/gogo.proto\x1a sentinel/session/v2/params.proto\x1a!sentinel/session/v2/session.proto"w\n\x0cGenesisState\x124\n\x08sessions\x18\x01 \x03(\x0b2\x1c.sentinel.session.v2.SessionB\x04\xc8\xde\x1f\x00\x121\n\x06params\x18\x02 \x01(\x0b2\x1b.sentinel.session.v2.ParamsB\x04\xc8\xde\x1f\x00BAZ7github.com/sentinel-official/hub/v12/x/session/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.session.v2.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/sentinel-official/hub/v12/x/session/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_GENESISSTATE'].fields_by_name['sessions']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['sessions']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE']._serialized_start = 149
    _globals['_GENESISSTATE']._serialized_end = 268