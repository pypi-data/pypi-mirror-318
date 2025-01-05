"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/certificatemanager/logging/v1/logs.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/certificatemanager/logging/v1/logs.proto\x12*google.cloud.certificatemanager.logging.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\x81\x02\n\x12CertificatesExpiry\x12\r\n\x05count\x18\x01 \x01(\x03\x12\x14\n\x0ccertificates\x18\x02 \x03(\t\x12S\n\x05state\x18\x03 \x01(\x0e2D.google.cloud.certificatemanager.logging.v1.CertificatesExpiry.State\x12/\n\x0bexpire_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"@\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x13\n\x0fCLOSE_TO_EXPIRY\x10\x01\x12\x0b\n\x07EXPIRED\x10\x02B\x92\x02\n.com.google.cloud.certificatemanager.logging.v1B\tLogsProtoP\x01ZHcloud.google.com/go/certificatemanager/logging/apiv1/loggingpb;loggingpb\xaa\x02*Google.Cloud.CertificateManager.Logging.V1\xca\x02*Google\\Cloud\\CertificateManager\\Logging\\V1\xea\x02.Google::Cloud::CertificateManager::Logging::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.certificatemanager.logging.v1.logs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n.com.google.cloud.certificatemanager.logging.v1B\tLogsProtoP\x01ZHcloud.google.com/go/certificatemanager/logging/apiv1/loggingpb;loggingpb\xaa\x02*Google.Cloud.CertificateManager.Logging.V1\xca\x02*Google\\Cloud\\CertificateManager\\Logging\\V1\xea\x02.Google::Cloud::CertificateManager::Logging::V1'
    _globals['_CERTIFICATESEXPIRY']._serialized_start = 135
    _globals['_CERTIFICATESEXPIRY']._serialized_end = 392
    _globals['_CERTIFICATESEXPIRY_STATE']._serialized_start = 328
    _globals['_CERTIFICATESEXPIRY_STATE']._serialized_end = 392