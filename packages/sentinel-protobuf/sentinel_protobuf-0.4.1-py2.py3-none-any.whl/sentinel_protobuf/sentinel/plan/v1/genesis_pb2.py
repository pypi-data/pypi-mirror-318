"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/plan/v1/genesis.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.plan.v1 import plan_pb2 as sentinel_dot_plan_dot_v1_dot_plan__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esentinel/plan/v1/genesis.proto\x12\x10sentinel.plan.v1\x1a\x14gogoproto/gogo.proto\x1a\x1bsentinel/plan/v1/plan.proto"W\n\x0bGenesisPlan\x129\n\x04plan\x18\x01 \x01(\x0b2\x16.sentinel.plan.v1.PlanB\x13\xc8\xde\x1f\x00\xea\xde\x1f\x0b_,omitempty\x12\r\n\x05nodes\x18\x02 \x03(\tB>Z4github.com/sentinel-official/hub/v12/x/plan/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.plan.v1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/plan/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_GENESISPLAN'].fields_by_name['plan']._loaded_options = None
    _globals['_GENESISPLAN'].fields_by_name['plan']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x0b_,omitempty'
    _globals['_GENESISPLAN']._serialized_start = 103
    _globals['_GENESISPLAN']._serialized_end = 190