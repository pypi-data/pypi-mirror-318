"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/kubernetes/security/containersecurity_logging/logging.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHgoogle/cloud/kubernetes/security/containersecurity_logging/logging.proto\x123cloud.kubernetes.security.containersecurity_logging\x1a\x1fgoogle/protobuf/timestamp.proto"\x89\x03\n\rVulnerability\x12\x14\n\x0cpackage_name\x18\x01 \x01(\t\x12 \n\x18affected_package_version\x18\x02 \x01(\t\x12\x0e\n\x06cve_id\x18\x03 \x01(\t\x12\x0f\n\x07cpe_uri\x18\x04 \x01(\t\x12O\n\x08severity\x18\x05 \x01(\x0e2=.cloud.kubernetes.security.containersecurity_logging.Severity\x12\x12\n\ncvss_score\x18\x06 \x01(\x02\x12\x13\n\x0bcvss_vector\x18\x07 \x01(\t\x12\x15\n\rfixed_cpe_uri\x18\x08 \x01(\t\x12\x14\n\x0cpackage_type\x18\t \x01(\t\x12\x15\n\rfixed_package\x18\n \x01(\t\x12\x1d\n\x15fixed_package_version\x18\x0b \x01(\t\x12\x13\n\x0bdescription\x18\x0c \x01(\t\x12\x14\n\x0crelated_urls\x18\r \x03(\t\x12\x17\n\x0faffected_images\x18\x0e \x03(\t"\xf9\x03\n\x07Finding\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12N\n\x04type\x18\x02 \x01(\x0e2@.cloud.kubernetes.security.containersecurity_logging.FindingType\x12Q\n\x05state\x18\x03 \x01(\x0e2B.cloud.kubernetes.security.containersecurity_logging.Finding.State\x12\x0f\n\x07finding\x18\x04 \x01(\t\x12O\n\x08severity\x18\x05 \x01(\x0e2=.cloud.kubernetes.security.containersecurity_logging.Severity\x12.\n\nevent_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12[\n\rvulnerability\x18\x07 \x01(\x0b2B.cloud.kubernetes.security.containersecurity_logging.VulnerabilityH\x00":\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x0e\n\nREMEDIATED\x10\x02B\t\n\x07details*g\n\x0bFindingType\x12\x1c\n\x18FINDING_TYPE_UNSPECIFIED\x10\x00\x12\x1a\n\x16FINDING_TYPE_MISCONFIG\x10\x01\x12\x1e\n\x1aFINDING_TYPE_VULNERABILITY\x10\x02*u\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x15\n\x11SEVERITY_CRITICAL\x10\x01\x12\x11\n\rSEVERITY_HIGH\x10\x02\x12\x13\n\x0fSEVERITY_MEDIUM\x10\x03\x12\x10\n\x0cSEVERITY_LOW\x10\x04B\x9e\x03\n>com.google.cloud.kubernetes.security.containersecurity.loggingB\x1dContainerSecurityLoggingProtoP\x01Z\x7fcloud.google.com/go/cloud/kubernetes/security/containersecurity_logging/containersecurity_loggingpb;containersecurity_loggingpb\xaa\x02:Google.Cloud.Kubernetes.Security.ContainerSecurity.Logging\xca\x02:Google\\Cloud\\Kubernetes\\Security\\ContainerSecurity\\Logging\xea\x02?Google::Cloud::Kubernetes::Security::ContainerSecurity::Loggingb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.kubernetes.security.containersecurity_logging.logging_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n>com.google.cloud.kubernetes.security.containersecurity.loggingB\x1dContainerSecurityLoggingProtoP\x01Z\x7fcloud.google.com/go/cloud/kubernetes/security/containersecurity_logging/containersecurity_loggingpb;containersecurity_loggingpb\xaa\x02:Google.Cloud.Kubernetes.Security.ContainerSecurity.Logging\xca\x02:Google\\Cloud\\Kubernetes\\Security\\ContainerSecurity\\Logging\xea\x02?Google::Cloud::Kubernetes::Security::ContainerSecurity::Logging'
    _globals['_FINDINGTYPE']._serialized_start = 1066
    _globals['_FINDINGTYPE']._serialized_end = 1169
    _globals['_SEVERITY']._serialized_start = 1171
    _globals['_SEVERITY']._serialized_end = 1288
    _globals['_VULNERABILITY']._serialized_start = 163
    _globals['_VULNERABILITY']._serialized_end = 556
    _globals['_FINDING']._serialized_start = 559
    _globals['_FINDING']._serialized_end = 1064
    _globals['_FINDING_STATE']._serialized_start = 995
    _globals['_FINDING_STATE']._serialized_end = 1053