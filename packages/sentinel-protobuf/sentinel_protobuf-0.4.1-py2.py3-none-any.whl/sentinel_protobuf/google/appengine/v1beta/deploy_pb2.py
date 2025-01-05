"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/appengine/v1beta/deploy.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/appengine/v1beta/deploy.proto\x12\x17google.appengine.v1beta\x1a\x1egoogle/protobuf/duration.proto"\x82\x03\n\nDeployment\x12=\n\x05files\x18\x01 \x03(\x0b2..google.appengine.v1beta.Deployment.FilesEntry\x129\n\tcontainer\x18\x02 \x01(\x0b2&.google.appengine.v1beta.ContainerInfo\x12-\n\x03zip\x18\x03 \x01(\x0b2 .google.appengine.v1beta.ZipInfo\x121\n\x05build\x18\x05 \x01(\x0b2".google.appengine.v1beta.BuildInfo\x12G\n\x13cloud_build_options\x18\x06 \x01(\x0b2*.google.appengine.v1beta.CloudBuildOptions\x1aO\n\nFilesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x120\n\x05value\x18\x02 \x01(\x0b2!.google.appengine.v1beta.FileInfo:\x028\x01"C\n\x08FileInfo\x12\x12\n\nsource_url\x18\x01 \x01(\t\x12\x10\n\x08sha1_sum\x18\x02 \x01(\t\x12\x11\n\tmime_type\x18\x03 \x01(\t"\x1e\n\rContainerInfo\x12\r\n\x05image\x18\x01 \x01(\t"#\n\tBuildInfo\x12\x16\n\x0ecloud_build_id\x18\x01 \x01(\t"b\n\x11CloudBuildOptions\x12\x15\n\rapp_yaml_path\x18\x01 \x01(\t\x126\n\x13cloud_build_timeout\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"2\n\x07ZipInfo\x12\x12\n\nsource_url\x18\x03 \x01(\t\x12\x13\n\x0bfiles_count\x18\x04 \x01(\x05B\xd1\x01\n\x1bcom.google.appengine.v1betaB\x0bDeployProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.v1beta.deploy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.appengine.v1betaB\x0bDeployProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1beta'
    _globals['_DEPLOYMENT_FILESENTRY']._loaded_options = None
    _globals['_DEPLOYMENT_FILESENTRY']._serialized_options = b'8\x01'
    _globals['_DEPLOYMENT']._serialized_start = 98
    _globals['_DEPLOYMENT']._serialized_end = 484
    _globals['_DEPLOYMENT_FILESENTRY']._serialized_start = 405
    _globals['_DEPLOYMENT_FILESENTRY']._serialized_end = 484
    _globals['_FILEINFO']._serialized_start = 486
    _globals['_FILEINFO']._serialized_end = 553
    _globals['_CONTAINERINFO']._serialized_start = 555
    _globals['_CONTAINERINFO']._serialized_end = 585
    _globals['_BUILDINFO']._serialized_start = 587
    _globals['_BUILDINFO']._serialized_end = 622
    _globals['_CLOUDBUILDOPTIONS']._serialized_start = 624
    _globals['_CLOUDBUILDOPTIONS']._serialized_end = 722
    _globals['_ZIPINFO']._serialized_start = 724
    _globals['_ZIPINFO']._serialized_end = 774