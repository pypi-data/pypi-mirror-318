"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/subscription/v1/genesis.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.subscription.v1 import params_pb2 as sentinel_dot_subscription_dot_v1_dot_params__pb2
from ....sentinel.subscription.v1 import quota_pb2 as sentinel_dot_subscription_dot_v1_dot_quota__pb2
from ....sentinel.subscription.v1 import subscription_pb2 as sentinel_dot_subscription_dot_v1_dot_subscription__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&sentinel/subscription/v1/genesis.proto\x12\x18sentinel.subscription.v1\x1a\x14gogoproto/gogo.proto\x1a%sentinel/subscription/v1/params.proto\x1a$sentinel/subscription/v1/quota.proto\x1a+sentinel/subscription/v1/subscription.proto"\x95\x01\n\x13GenesisSubscription\x12G\n\x0csubscription\x18\x01 \x01(\x0b2&.sentinel.subscription.v1.SubscriptionB\t\xc8\xde\x1f\x00\xea\xde\x1f\x01_\x125\n\x06quotas\x18\x02 \x03(\x0b2\x1f.sentinel.subscription.v1.QuotaB\x04\xc8\xde\x1f\x00"\xa1\x01\n\x0cGenesisState\x12Y\n\rsubscriptions\x18\x01 \x03(\x0b2-.sentinel.subscription.v1.GenesisSubscriptionB\x13\xc8\xde\x1f\x00\xea\xde\x1f\x0b_,omitempty\x126\n\x06params\x18\x02 \x01(\x0b2 .sentinel.subscription.v1.ParamsB\x04\xc8\xde\x1f\x00BFZ<github.com/sentinel-official/hub/v12/x/subscription/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.subscription.v1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/sentinel-official/hub/v12/x/subscription/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_GENESISSUBSCRIPTION'].fields_by_name['subscription']._loaded_options = None
    _globals['_GENESISSUBSCRIPTION'].fields_by_name['subscription']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x01_'
    _globals['_GENESISSUBSCRIPTION'].fields_by_name['quotas']._loaded_options = None
    _globals['_GENESISSUBSCRIPTION'].fields_by_name['quotas']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE'].fields_by_name['subscriptions']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['subscriptions']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x0b_,omitempty'
    _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSUBSCRIPTION']._serialized_start = 213
    _globals['_GENESISSUBSCRIPTION']._serialized_end = 362
    _globals['_GENESISSTATE']._serialized_start = 365
    _globals['_GENESISSTATE']._serialized_end = 526