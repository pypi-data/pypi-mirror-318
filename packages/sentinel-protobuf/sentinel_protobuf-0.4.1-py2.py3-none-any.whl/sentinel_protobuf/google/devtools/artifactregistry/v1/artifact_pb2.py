"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/artifactregistry/v1/artifact.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/devtools/artifactregistry/v1/artifact.proto\x12#google.devtools.artifactregistry.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x98\x03\n\x0bDockerImage\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x10\n\x03uri\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x0c\n\x04tags\x18\x03 \x03(\t\x12\x18\n\x10image_size_bytes\x18\x04 \x01(\x03\x12/\n\x0bupload_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x12\n\nmedia_type\x18\x06 \x01(\t\x12.\n\nbuild_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x0bupdate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:\x90\x01\xeaA\x8c\x01\n+artifactregistry.googleapis.com/DockerImage\x12]projects/{project}/locations/{location}/repositories/{repository}/dockerImages/{docker_image}"g\n\x17ListDockerImagesRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t"|\n\x18ListDockerImagesResponse\x12G\n\rdocker_images\x18\x01 \x03(\x0b20.google.devtools.artifactregistry.v1.DockerImage\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"Z\n\x15GetDockerImageRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+artifactregistry.googleapis.com/DockerImage"\xf5\x02\n\rMavenArtifact\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07pom_uri\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x10\n\x08group_id\x18\x03 \x01(\t\x12\x13\n\x0bartifact_id\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:\x96\x01\xeaA\x92\x01\n-artifactregistry.googleapis.com/MavenArtifact\x12aprojects/{project}/locations/{location}/repositories/{repository}/mavenArtifacts/{maven_artifact}"\x89\x01\n\x19ListMavenArtifactsRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\x12-artifactregistry.googleapis.com/MavenArtifact\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x82\x01\n\x1aListMavenArtifactsResponse\x12K\n\x0fmaven_artifacts\x18\x01 \x03(\x0b22.google.devtools.artifactregistry.v1.MavenArtifact\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"^\n\x17GetMavenArtifactRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-artifactregistry.googleapis.com/MavenArtifact"\xd0\x02\n\nNpmPackage\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x0cpackage_name\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\x12\x0c\n\x04tags\x18\x05 \x03(\t\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:\x8d\x01\xeaA\x89\x01\n*artifactregistry.googleapis.com/NpmPackage\x12[projects/{project}/locations/{location}/repositories/{repository}/npmPackages/{npm_package}"\x83\x01\n\x16ListNpmPackagesRequest\x12B\n\x06parent\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\x12*artifactregistry.googleapis.com/NpmPackage\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"y\n\x17ListNpmPackagesResponse\x12E\n\x0cnpm_packages\x18\x01 \x03(\x0b2/.google.devtools.artifactregistry.v1.NpmPackage\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"X\n\x14GetNpmPackageRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*artifactregistry.googleapis.com/NpmPackage"\xe0\x02\n\rPythonPackage\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x10\n\x03uri\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x14\n\x0cpackage_name\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:\x96\x01\xeaA\x92\x01\n-artifactregistry.googleapis.com/PythonPackage\x12aprojects/{project}/locations/{location}/repositories/{repository}/pythonPackages/{python_package}"\x89\x01\n\x19ListPythonPackagesRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\x12-artifactregistry.googleapis.com/PythonPackage\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x82\x01\n\x1aListPythonPackagesResponse\x12K\n\x0fpython_packages\x18\x01 \x03(\x0b22.google.devtools.artifactregistry.v1.PythonPackage\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"^\n\x17GetPythonPackageRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-artifactregistry.googleapis.com/PythonPackageB\xf8\x01\n\'com.google.devtools.artifactregistry.v1B\rArtifactProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.artifactregistry.v1.artifact_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.devtools.artifactregistry.v1B\rArtifactProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1"
    _globals['_DOCKERIMAGE'].fields_by_name['name']._loaded_options = None
    _globals['_DOCKERIMAGE'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_DOCKERIMAGE'].fields_by_name['uri']._loaded_options = None
    _globals['_DOCKERIMAGE'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_DOCKERIMAGE'].fields_by_name['update_time']._loaded_options = None
    _globals['_DOCKERIMAGE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_DOCKERIMAGE']._loaded_options = None
    _globals['_DOCKERIMAGE']._serialized_options = b'\xeaA\x8c\x01\n+artifactregistry.googleapis.com/DockerImage\x12]projects/{project}/locations/{location}/repositories/{repository}/dockerImages/{docker_image}'
    _globals['_LISTDOCKERIMAGESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDOCKERIMAGESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_GETDOCKERIMAGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDOCKERIMAGEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+artifactregistry.googleapis.com/DockerImage'
    _globals['_MAVENARTIFACT'].fields_by_name['name']._loaded_options = None
    _globals['_MAVENARTIFACT'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_MAVENARTIFACT'].fields_by_name['pom_uri']._loaded_options = None
    _globals['_MAVENARTIFACT'].fields_by_name['pom_uri']._serialized_options = b'\xe0A\x02'
    _globals['_MAVENARTIFACT'].fields_by_name['create_time']._loaded_options = None
    _globals['_MAVENARTIFACT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_MAVENARTIFACT'].fields_by_name['update_time']._loaded_options = None
    _globals['_MAVENARTIFACT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_MAVENARTIFACT']._loaded_options = None
    _globals['_MAVENARTIFACT']._serialized_options = b'\xeaA\x92\x01\n-artifactregistry.googleapis.com/MavenArtifact\x12aprojects/{project}/locations/{location}/repositories/{repository}/mavenArtifacts/{maven_artifact}'
    _globals['_LISTMAVENARTIFACTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMAVENARTIFACTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\x12-artifactregistry.googleapis.com/MavenArtifact'
    _globals['_GETMAVENARTIFACTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMAVENARTIFACTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-artifactregistry.googleapis.com/MavenArtifact'
    _globals['_NPMPACKAGE'].fields_by_name['name']._loaded_options = None
    _globals['_NPMPACKAGE'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_NPMPACKAGE'].fields_by_name['create_time']._loaded_options = None
    _globals['_NPMPACKAGE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_NPMPACKAGE'].fields_by_name['update_time']._loaded_options = None
    _globals['_NPMPACKAGE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_NPMPACKAGE']._loaded_options = None
    _globals['_NPMPACKAGE']._serialized_options = b'\xeaA\x89\x01\n*artifactregistry.googleapis.com/NpmPackage\x12[projects/{project}/locations/{location}/repositories/{repository}/npmPackages/{npm_package}'
    _globals['_LISTNPMPACKAGESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTNPMPACKAGESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA,\x12*artifactregistry.googleapis.com/NpmPackage'
    _globals['_GETNPMPACKAGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETNPMPACKAGEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*artifactregistry.googleapis.com/NpmPackage'
    _globals['_PYTHONPACKAGE'].fields_by_name['name']._loaded_options = None
    _globals['_PYTHONPACKAGE'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_PYTHONPACKAGE'].fields_by_name['uri']._loaded_options = None
    _globals['_PYTHONPACKAGE'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_PYTHONPACKAGE'].fields_by_name['create_time']._loaded_options = None
    _globals['_PYTHONPACKAGE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_PYTHONPACKAGE'].fields_by_name['update_time']._loaded_options = None
    _globals['_PYTHONPACKAGE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_PYTHONPACKAGE']._loaded_options = None
    _globals['_PYTHONPACKAGE']._serialized_options = b'\xeaA\x92\x01\n-artifactregistry.googleapis.com/PythonPackage\x12aprojects/{project}/locations/{location}/repositories/{repository}/pythonPackages/{python_package}'
    _globals['_LISTPYTHONPACKAGESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPYTHONPACKAGESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\x12-artifactregistry.googleapis.com/PythonPackage'
    _globals['_GETPYTHONPACKAGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPYTHONPACKAGEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-artifactregistry.googleapis.com/PythonPackage'
    _globals['_DOCKERIMAGE']._serialized_start = 185
    _globals['_DOCKERIMAGE']._serialized_end = 593
    _globals['_LISTDOCKERIMAGESREQUEST']._serialized_start = 595
    _globals['_LISTDOCKERIMAGESREQUEST']._serialized_end = 698
    _globals['_LISTDOCKERIMAGESRESPONSE']._serialized_start = 700
    _globals['_LISTDOCKERIMAGESRESPONSE']._serialized_end = 824
    _globals['_GETDOCKERIMAGEREQUEST']._serialized_start = 826
    _globals['_GETDOCKERIMAGEREQUEST']._serialized_end = 916
    _globals['_MAVENARTIFACT']._serialized_start = 919
    _globals['_MAVENARTIFACT']._serialized_end = 1292
    _globals['_LISTMAVENARTIFACTSREQUEST']._serialized_start = 1295
    _globals['_LISTMAVENARTIFACTSREQUEST']._serialized_end = 1432
    _globals['_LISTMAVENARTIFACTSRESPONSE']._serialized_start = 1435
    _globals['_LISTMAVENARTIFACTSRESPONSE']._serialized_end = 1565
    _globals['_GETMAVENARTIFACTREQUEST']._serialized_start = 1567
    _globals['_GETMAVENARTIFACTREQUEST']._serialized_end = 1661
    _globals['_NPMPACKAGE']._serialized_start = 1664
    _globals['_NPMPACKAGE']._serialized_end = 2000
    _globals['_LISTNPMPACKAGESREQUEST']._serialized_start = 2003
    _globals['_LISTNPMPACKAGESREQUEST']._serialized_end = 2134
    _globals['_LISTNPMPACKAGESRESPONSE']._serialized_start = 2136
    _globals['_LISTNPMPACKAGESRESPONSE']._serialized_end = 2257
    _globals['_GETNPMPACKAGEREQUEST']._serialized_start = 2259
    _globals['_GETNPMPACKAGEREQUEST']._serialized_end = 2347
    _globals['_PYTHONPACKAGE']._serialized_start = 2350
    _globals['_PYTHONPACKAGE']._serialized_end = 2702
    _globals['_LISTPYTHONPACKAGESREQUEST']._serialized_start = 2705
    _globals['_LISTPYTHONPACKAGESREQUEST']._serialized_end = 2842
    _globals['_LISTPYTHONPACKAGESRESPONSE']._serialized_start = 2845
    _globals['_LISTPYTHONPACKAGESRESPONSE']._serialized_end = 2975
    _globals['_GETPYTHONPACKAGEREQUEST']._serialized_start = 2977
    _globals['_GETPYTHONPACKAGEREQUEST']._serialized_end = 3071