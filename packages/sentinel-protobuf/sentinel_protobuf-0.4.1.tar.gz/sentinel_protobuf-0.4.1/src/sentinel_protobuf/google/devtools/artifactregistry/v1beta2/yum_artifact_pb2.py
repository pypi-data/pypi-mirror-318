"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/artifactregistry/v1beta2/yum_artifact.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/devtools/artifactregistry/v1beta2/yum_artifact.proto\x12(google.devtools.artifactregistry.v1beta2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto"\x8c\x03\n\x0bYumArtifact\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cpackage_name\x18\x02 \x01(\tB\x03\xe0A\x03\x12\\\n\x0cpackage_type\x18\x03 \x01(\x0e2A.google.devtools.artifactregistry.v1beta2.YumArtifact.PackageTypeB\x03\xe0A\x03\x12\x19\n\x0carchitecture\x18\x04 \x01(\tB\x03\xe0A\x03"C\n\x0bPackageType\x12\x1c\n\x18PACKAGE_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06BINARY\x10\x01\x12\n\n\x06SOURCE\x10\x02:\x90\x01\xeaA\x8c\x01\n+artifactregistry.googleapis.com/YumArtifact\x12]projects/{project}/locations/{location}/repositories/{repository}/yumArtifacts/{yum_artifact}"B\n\x1bImportYumArtifactsGcsSource\x12\x0c\n\x04uris\x18\x01 \x03(\t\x12\x15\n\ruse_wildcards\x18\x02 \x01(\x08"\x92\x01\n\x19ImportYumArtifactsRequest\x12[\n\ngcs_source\x18\x02 \x01(\x0b2E.google.devtools.artifactregistry.v1beta2.ImportYumArtifactsGcsSourceH\x00\x12\x0e\n\x06parent\x18\x01 \x01(\tB\x08\n\x06source"\xa7\x01\n\x1bImportYumArtifactsErrorInfo\x12[\n\ngcs_source\x18\x01 \x01(\x0b2E.google.devtools.artifactregistry.v1beta2.ImportYumArtifactsGcsSourceH\x00\x12!\n\x05error\x18\x02 \x01(\x0b2\x12.google.rpc.StatusB\x08\n\x06source"\xc1\x01\n\x1aImportYumArtifactsResponse\x12L\n\ryum_artifacts\x18\x01 \x03(\x0b25.google.devtools.artifactregistry.v1beta2.YumArtifact\x12U\n\x06errors\x18\x02 \x03(\x0b2E.google.devtools.artifactregistry.v1beta2.ImportYumArtifactsErrorInfo"\x1c\n\x1aImportYumArtifactsMetadataB\x94\x02\n,com.google.devtools.artifactregistry.v1beta2B\x10YumArtifactProtoP\x01ZUcloud.google.com/go/artifactregistry/apiv1beta2/artifactregistrypb;artifactregistrypb\xaa\x02%Google.Cloud.ArtifactRegistry.V1Beta2\xca\x02%Google\\Cloud\\ArtifactRegistry\\V1beta2\xea\x02(Google::Cloud::ArtifactRegistry::V1beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.artifactregistry.v1beta2.yum_artifact_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.devtools.artifactregistry.v1beta2B\x10YumArtifactProtoP\x01ZUcloud.google.com/go/artifactregistry/apiv1beta2/artifactregistrypb;artifactregistrypb\xaa\x02%Google.Cloud.ArtifactRegistry.V1Beta2\xca\x02%Google\\Cloud\\ArtifactRegistry\\V1beta2\xea\x02(Google::Cloud::ArtifactRegistry::V1beta2'
    _globals['_YUMARTIFACT'].fields_by_name['name']._loaded_options = None
    _globals['_YUMARTIFACT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_YUMARTIFACT'].fields_by_name['package_name']._loaded_options = None
    _globals['_YUMARTIFACT'].fields_by_name['package_name']._serialized_options = b'\xe0A\x03'
    _globals['_YUMARTIFACT'].fields_by_name['package_type']._loaded_options = None
    _globals['_YUMARTIFACT'].fields_by_name['package_type']._serialized_options = b'\xe0A\x03'
    _globals['_YUMARTIFACT'].fields_by_name['architecture']._loaded_options = None
    _globals['_YUMARTIFACT'].fields_by_name['architecture']._serialized_options = b'\xe0A\x03'
    _globals['_YUMARTIFACT']._loaded_options = None
    _globals['_YUMARTIFACT']._serialized_options = b'\xeaA\x8c\x01\n+artifactregistry.googleapis.com/YumArtifact\x12]projects/{project}/locations/{location}/repositories/{repository}/yumArtifacts/{yum_artifact}'
    _globals['_YUMARTIFACT']._serialized_start = 191
    _globals['_YUMARTIFACT']._serialized_end = 587
    _globals['_YUMARTIFACT_PACKAGETYPE']._serialized_start = 373
    _globals['_YUMARTIFACT_PACKAGETYPE']._serialized_end = 440
    _globals['_IMPORTYUMARTIFACTSGCSSOURCE']._serialized_start = 589
    _globals['_IMPORTYUMARTIFACTSGCSSOURCE']._serialized_end = 655
    _globals['_IMPORTYUMARTIFACTSREQUEST']._serialized_start = 658
    _globals['_IMPORTYUMARTIFACTSREQUEST']._serialized_end = 804
    _globals['_IMPORTYUMARTIFACTSERRORINFO']._serialized_start = 807
    _globals['_IMPORTYUMARTIFACTSERRORINFO']._serialized_end = 974
    _globals['_IMPORTYUMARTIFACTSRESPONSE']._serialized_start = 977
    _globals['_IMPORTYUMARTIFACTSRESPONSE']._serialized_end = 1170
    _globals['_IMPORTYUMARTIFACTSMETADATA']._serialized_start = 1172
    _globals['_IMPORTYUMARTIFACTSMETADATA']._serialized_end = 1200