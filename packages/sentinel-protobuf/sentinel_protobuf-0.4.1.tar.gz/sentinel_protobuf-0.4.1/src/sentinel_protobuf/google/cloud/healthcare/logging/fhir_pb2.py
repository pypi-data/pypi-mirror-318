"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/healthcare/logging/fhir.proto')
_sym_db = _symbol_database.Default()
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/healthcare/logging/fhir.proto\x12\x1fgoogle.cloud.healthcare.logging\x1a\x17google/rpc/status.proto"\\\n\x12ImportFhirLogEntry\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x13\n\x0bresource_id\x18\x02 \x01(\t\x12!\n\x05error\x18\x03 \x01(\x0b2\x12.google.rpc.Status"c\n\x12ExportFhirLogEntry\x12\x13\n\x0bdestination\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x03 \x01(\t\x12!\n\x05error\x18\x04 \x01(\x0b2\x12.google.rpc.Status"U\n\x1bFhirConfigureSearchLogEntry\x12\x13\n\x0bresource_id\x18\x01 \x01(\t\x12!\n\x05error\x18\x02 \x01(\x0b2\x12.google.rpc.Status"j\n\x18FhirNotificationLogEntry\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x14\n\x0cpubsub_topic\x18\x02 \x01(\t\x12!\n\x05error\x18\x03 \x01(\x0b2\x12.google.rpc.Status"c\n\x12FhirStreamLogEntry\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x13\n\x0bdestination\x18\x02 \x01(\t\x12!\n\x05error\x18\x03 \x01(\x0b2\x12.google.rpc.Status"t\n#FhirDeidentifyStreamToStoreLogEntry\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x13\n\x0bdestination\x18\x02 \x01(\t\x12!\n\x05error\x18\x03 \x01(\x0b2\x12.google.rpc.StatusBa\n#com.google.cloud.healthcare.loggingZ:cloud.google.com/go/healthcare/logging/loggingpb;loggingpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.healthcare.logging.fhir_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.healthcare.loggingZ:cloud.google.com/go/healthcare/logging/loggingpb;loggingpb'
    _globals['_IMPORTFHIRLOGENTRY']._serialized_start = 104
    _globals['_IMPORTFHIRLOGENTRY']._serialized_end = 196
    _globals['_EXPORTFHIRLOGENTRY']._serialized_start = 198
    _globals['_EXPORTFHIRLOGENTRY']._serialized_end = 297
    _globals['_FHIRCONFIGURESEARCHLOGENTRY']._serialized_start = 299
    _globals['_FHIRCONFIGURESEARCHLOGENTRY']._serialized_end = 384
    _globals['_FHIRNOTIFICATIONLOGENTRY']._serialized_start = 386
    _globals['_FHIRNOTIFICATIONLOGENTRY']._serialized_end = 492
    _globals['_FHIRSTREAMLOGENTRY']._serialized_start = 494
    _globals['_FHIRSTREAMLOGENTRY']._serialized_end = 593
    _globals['_FHIRDEIDENTIFYSTREAMTOSTORELOGENTRY']._serialized_start = 595
    _globals['_FHIRDEIDENTIFYSTREAMTOSTORELOGENTRY']._serialized_end = 711