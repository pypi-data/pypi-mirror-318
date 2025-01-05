"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/appengine/v1beta/certificate.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/appengine/v1beta/certificate.proto\x12\x17google.appengine.v1beta\x1a\x1fgoogle/protobuf/timestamp.proto"\xe3\x02\n\x15AuthorizedCertificate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12\x14\n\x0cdomain_names\x18\x04 \x03(\t\x12/\n\x0bexpire_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12I\n\x14certificate_raw_data\x18\x06 \x01(\x0b2+.google.appengine.v1beta.CertificateRawData\x12H\n\x13managed_certificate\x18\x07 \x01(\x0b2+.google.appengine.v1beta.ManagedCertificate\x12\x1f\n\x17visible_domain_mappings\x18\x08 \x03(\t\x12\x1d\n\x15domain_mappings_count\x18\t \x01(\x05"E\n\x12CertificateRawData\x12\x1a\n\x12public_certificate\x18\x01 \x01(\t\x12\x13\n\x0bprivate_key\x18\x02 \x01(\t"\x86\x01\n\x12ManagedCertificate\x125\n\x11last_renewal_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x129\n\x06status\x18\x02 \x01(\x0e2).google.appengine.v1beta.ManagementStatus*\xc6\x01\n\x10ManagementStatus\x12!\n\x1dMANAGEMENT_STATUS_UNSPECIFIED\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\x1f\n\x1bFAILED_RETRYING_NOT_VISIBLE\x10\x04\x12\x14\n\x10FAILED_PERMANENT\x10\x06\x12!\n\x1dFAILED_RETRYING_CAA_FORBIDDEN\x10\x07\x12 \n\x1cFAILED_RETRYING_CAA_CHECKING\x10\x08B\xd6\x01\n\x1bcom.google.appengine.v1betaB\x10CertificateProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.v1beta.certificate_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.appengine.v1betaB\x10CertificateProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1beta'
    _globals['_MANAGEMENTSTATUS']._serialized_start = 670
    _globals['_MANAGEMENTSTATUS']._serialized_end = 868
    _globals['_AUTHORIZEDCERTIFICATE']._serialized_start = 104
    _globals['_AUTHORIZEDCERTIFICATE']._serialized_end = 459
    _globals['_CERTIFICATERAWDATA']._serialized_start = 461
    _globals['_CERTIFICATERAWDATA']._serialized_end = 530
    _globals['_MANAGEDCERTIFICATE']._serialized_start = 533
    _globals['_MANAGEDCERTIFICATE']._serialized_end = 667