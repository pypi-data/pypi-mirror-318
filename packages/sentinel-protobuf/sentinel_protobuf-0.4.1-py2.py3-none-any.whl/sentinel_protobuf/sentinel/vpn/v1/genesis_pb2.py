"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/vpn/v1/genesis.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.deposit.v1 import genesis_pb2 as sentinel_dot_deposit_dot_v1_dot_genesis__pb2
from ....sentinel.lease.v1 import genesis_pb2 as sentinel_dot_lease_dot_v1_dot_genesis__pb2
from ....sentinel.node.v3 import genesis_pb2 as sentinel_dot_node_dot_v3_dot_genesis__pb2
from ....sentinel.plan.v3 import genesis_pb2 as sentinel_dot_plan_dot_v3_dot_genesis__pb2
from ....sentinel.provider.v2 import genesis_pb2 as sentinel_dot_provider_dot_v2_dot_genesis__pb2
from ....sentinel.session.v3 import genesis_pb2 as sentinel_dot_session_dot_v3_dot_genesis__pb2
from ....sentinel.subscription.v3 import genesis_pb2 as sentinel_dot_subscription_dot_v3_dot_genesis__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsentinel/vpn/v1/genesis.proto\x12\x0fsentinel.vpn.v1\x1a\x14gogoproto/gogo.proto\x1a!sentinel/deposit/v1/genesis.proto\x1a\x1fsentinel/lease/v1/genesis.proto\x1a\x1esentinel/node/v3/genesis.proto\x1a\x1esentinel/plan/v3/genesis.proto\x1a"sentinel/provider/v2/genesis.proto\x1a!sentinel/session/v3/genesis.proto\x1a&sentinel/subscription/v3/genesis.proto"\xf6\x02\n\x0cGenesisState\x122\n\x07deposit\x18\x01 \x01(\x0b2!.sentinel.deposit.v1.GenesisState\x12.\n\x05lease\x18\x02 \x01(\x0b2\x1f.sentinel.lease.v1.GenesisState\x12,\n\x04node\x18\x03 \x01(\x0b2\x1e.sentinel.node.v3.GenesisState\x12,\n\x04plan\x18\x04 \x01(\x0b2\x1e.sentinel.plan.v3.GenesisState\x124\n\x08provider\x18\x05 \x01(\x0b2".sentinel.provider.v2.GenesisState\x122\n\x07session\x18\x06 \x01(\x0b2!.sentinel.session.v3.GenesisState\x12<\n\x0csubscription\x18\x07 \x01(\x0b2&.sentinel.subscription.v3.GenesisStateB=Z3github.com/sentinel-official/hub/v12/x/vpn/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.vpn.v1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z3github.com/sentinel-official/hub/v12/x/vpn/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_GENESISSTATE']._serialized_start = 316
    _globals['_GENESISSTATE']._serialized_end = 690