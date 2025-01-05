"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/artifactregistry/v1/apt_artifact.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/devtools/artifactregistry/v1/apt_artifact.proto\x12#google.devtools.artifactregistry.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto"\xba\x03\n\x0bAptArtifact\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cpackage_name\x18\x02 \x01(\tB\x03\xe0A\x03\x12W\n\x0cpackage_type\x18\x03 \x01(\x0e2<.google.devtools.artifactregistry.v1.AptArtifact.PackageTypeB\x03\xe0A\x03\x12\x19\n\x0carchitecture\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x16\n\tcomponent\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0ccontrol_file\x18\x06 \x01(\x0cB\x03\xe0A\x03"C\n\x0bPackageType\x12\x1c\n\x18PACKAGE_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06BINARY\x10\x01\x12\n\n\x06SOURCE\x10\x02:\x90\x01\xeaA\x8c\x01\n+artifactregistry.googleapis.com/AptArtifact\x12]projects/{project}/locations/{location}/repositories/{repository}/aptArtifacts/{apt_artifact}"B\n\x1bImportAptArtifactsGcsSource\x12\x0c\n\x04uris\x18\x01 \x03(\t\x12\x15\n\ruse_wildcards\x18\x02 \x01(\x08"\x8d\x01\n\x19ImportAptArtifactsRequest\x12V\n\ngcs_source\x18\x02 \x01(\x0b2@.google.devtools.artifactregistry.v1.ImportAptArtifactsGcsSourceH\x00\x12\x0e\n\x06parent\x18\x01 \x01(\tB\x08\n\x06source"\xa2\x01\n\x1bImportAptArtifactsErrorInfo\x12V\n\ngcs_source\x18\x01 \x01(\x0b2@.google.devtools.artifactregistry.v1.ImportAptArtifactsGcsSourceH\x00\x12!\n\x05error\x18\x02 \x01(\x0b2\x12.google.rpc.StatusB\x08\n\x06source"\xb7\x01\n\x1aImportAptArtifactsResponse\x12G\n\rapt_artifacts\x18\x01 \x03(\x0b20.google.devtools.artifactregistry.v1.AptArtifact\x12P\n\x06errors\x18\x02 \x03(\x0b2@.google.devtools.artifactregistry.v1.ImportAptArtifactsErrorInfo"\x1c\n\x1aImportAptArtifactsMetadataB\xfb\x01\n\'com.google.devtools.artifactregistry.v1B\x10AptArtifactProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.artifactregistry.v1.apt_artifact_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.devtools.artifactregistry.v1B\x10AptArtifactProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1"
    _globals['_APTARTIFACT'].fields_by_name['name']._loaded_options = None
    _globals['_APTARTIFACT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_APTARTIFACT'].fields_by_name['package_name']._loaded_options = None
    _globals['_APTARTIFACT'].fields_by_name['package_name']._serialized_options = b'\xe0A\x03'
    _globals['_APTARTIFACT'].fields_by_name['package_type']._loaded_options = None
    _globals['_APTARTIFACT'].fields_by_name['package_type']._serialized_options = b'\xe0A\x03'
    _globals['_APTARTIFACT'].fields_by_name['architecture']._loaded_options = None
    _globals['_APTARTIFACT'].fields_by_name['architecture']._serialized_options = b'\xe0A\x03'
    _globals['_APTARTIFACT'].fields_by_name['component']._loaded_options = None
    _globals['_APTARTIFACT'].fields_by_name['component']._serialized_options = b'\xe0A\x03'
    _globals['_APTARTIFACT'].fields_by_name['control_file']._loaded_options = None
    _globals['_APTARTIFACT'].fields_by_name['control_file']._serialized_options = b'\xe0A\x03'
    _globals['_APTARTIFACT']._loaded_options = None
    _globals['_APTARTIFACT']._serialized_options = b'\xeaA\x8c\x01\n+artifactregistry.googleapis.com/AptArtifact\x12]projects/{project}/locations/{location}/repositories/{repository}/aptArtifacts/{apt_artifact}'
    _globals['_APTARTIFACT']._serialized_start = 181
    _globals['_APTARTIFACT']._serialized_end = 623
    _globals['_APTARTIFACT_PACKAGETYPE']._serialized_start = 409
    _globals['_APTARTIFACT_PACKAGETYPE']._serialized_end = 476
    _globals['_IMPORTAPTARTIFACTSGCSSOURCE']._serialized_start = 625
    _globals['_IMPORTAPTARTIFACTSGCSSOURCE']._serialized_end = 691
    _globals['_IMPORTAPTARTIFACTSREQUEST']._serialized_start = 694
    _globals['_IMPORTAPTARTIFACTSREQUEST']._serialized_end = 835
    _globals['_IMPORTAPTARTIFACTSERRORINFO']._serialized_start = 838
    _globals['_IMPORTAPTARTIFACTSERRORINFO']._serialized_end = 1000
    _globals['_IMPORTAPTARTIFACTSRESPONSE']._serialized_start = 1003
    _globals['_IMPORTAPTARTIFACTSRESPONSE']._serialized_end = 1186
    _globals['_IMPORTAPTARTIFACTSMETADATA']._serialized_start = 1188
    _globals['_IMPORTAPTARTIFACTSMETADATA']._serialized_end = 1216