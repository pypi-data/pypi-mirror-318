"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/kms/logging/v1/logs.proto')
_sym_db = _symbol_database.Default()
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/kms/logging/v1/logs.proto\x12\x1bgoogle.cloud.kms.logging.v1\x1a\x17google/rpc/status.proto"\x98\x01\n\x0eCryptoKeyEvent\x12Q\n\x0erotation_event\x18\x01 \x01(\x0b29.google.cloud.kms.logging.v1.CryptoKeyEvent.RotationEvent\x1a3\n\rRotationEvent\x12"\n\x06status\x18\x01 \x01(\x0b2\x12.google.rpc.Status"\xd4\x04\n\x15CryptoKeyVersionEvent\x12s\n\x1bscheduled_destruction_event\x18\x01 \x01(\x0b2L.google.cloud.kms.logging.v1.CryptoKeyVersionEvent.ScheduledDestructionEventH\x00\x12e\n\x14key_generation_event\x18\x02 \x01(\x0b2E.google.cloud.kms.logging.v1.CryptoKeyVersionEvent.KeyGenerationEventH\x00\x12V\n\x0cimport_event\x18\x03 \x01(\x0b2>.google.cloud.kms.logging.v1.CryptoKeyVersionEvent.ImportEventH\x00\x1ah\n\x19ScheduledDestructionEvent\x12"\n\x06status\x18\x01 \x01(\x0b2\x12.google.rpc.Status\x12\'\n\x1fkey_access_justification_reason\x18\x02 \x01(\t\x1aa\n\x12KeyGenerationEvent\x12"\n\x06status\x18\x01 \x01(\x0b2\x12.google.rpc.Status\x12\'\n\x1fkey_access_justification_reason\x18\x02 \x01(\t\x1a1\n\x0bImportEvent\x12"\n\x06status\x18\x01 \x01(\x0b2\x12.google.rpc.StatusB\x07\n\x05eventBi\n\x1fcom.google.cloud.kms.logging.v1B\tLogsProtoP\x01Z9cloud.google.com/go/kms/logging/apiv1/loggingpb;loggingpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.kms.logging.v1.logs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.kms.logging.v1B\tLogsProtoP\x01Z9cloud.google.com/go/kms/logging/apiv1/loggingpb;loggingpb'
    _globals['_CRYPTOKEYEVENT']._serialized_start = 97
    _globals['_CRYPTOKEYEVENT']._serialized_end = 249
    _globals['_CRYPTOKEYEVENT_ROTATIONEVENT']._serialized_start = 198
    _globals['_CRYPTOKEYEVENT_ROTATIONEVENT']._serialized_end = 249
    _globals['_CRYPTOKEYVERSIONEVENT']._serialized_start = 252
    _globals['_CRYPTOKEYVERSIONEVENT']._serialized_end = 848
    _globals['_CRYPTOKEYVERSIONEVENT_SCHEDULEDDESTRUCTIONEVENT']._serialized_start = 585
    _globals['_CRYPTOKEYVERSIONEVENT_SCHEDULEDDESTRUCTIONEVENT']._serialized_end = 689
    _globals['_CRYPTOKEYVERSIONEVENT_KEYGENERATIONEVENT']._serialized_start = 691
    _globals['_CRYPTOKEYVERSIONEVENT_KEYGENERATIONEVENT']._serialized_end = 788
    _globals['_CRYPTOKEYVERSIONEVENT_IMPORTEVENT']._serialized_start = 790
    _globals['_CRYPTOKEYVERSIONEVENT_IMPORTEVENT']._serialized_end = 839