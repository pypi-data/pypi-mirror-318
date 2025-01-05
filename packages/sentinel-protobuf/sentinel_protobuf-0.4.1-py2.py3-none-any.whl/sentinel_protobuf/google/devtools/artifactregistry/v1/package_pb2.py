"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/artifactregistry/v1/package.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/devtools/artifactregistry/v1/package.proto\x12#google.devtools.artifactregistry.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa1\x03\n\x07Package\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12/\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12W\n\x0bannotations\x18\x07 \x03(\x0b2=.google.devtools.artifactregistry.v1.Package.AnnotationsEntryB\x03\xe0A\x01\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x82\x01\xeaA\x7f\n\'artifactregistry.googleapis.com/Package\x12Tprojects/{project}/locations/{location}/repositories/{repository}/packages/{package}"\xa9\x01\n\x13ListPackagesRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\x12\'artifactregistry.googleapis.com/Package\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"o\n\x14ListPackagesResponse\x12>\n\x08packages\x18\x01 \x03(\x0b2,.google.devtools.artifactregistry.v1.Package\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"R\n\x11GetPackageRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'artifactregistry.googleapis.com/Package"U\n\x14DeletePackageRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'artifactregistry.googleapis.com/Package"\x86\x01\n\x14UpdatePackageRequest\x12=\n\x07package\x18\x01 \x01(\x0b2,.google.devtools.artifactregistry.v1.Package\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\xf7\x01\n\'com.google.devtools.artifactregistry.v1B\x0cPackageProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.artifactregistry.v1.package_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.devtools.artifactregistry.v1B\x0cPackageProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1"
    _globals['_PACKAGE_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_PACKAGE_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_PACKAGE'].fields_by_name['annotations']._loaded_options = None
    _globals['_PACKAGE'].fields_by_name['annotations']._serialized_options = b'\xe0A\x01'
    _globals['_PACKAGE']._loaded_options = None
    _globals['_PACKAGE']._serialized_options = b"\xeaA\x7f\n'artifactregistry.googleapis.com/Package\x12Tprojects/{project}/locations/{location}/repositories/{repository}/packages/{package}"
    _globals['_LISTPACKAGESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPACKAGESREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\x12'artifactregistry.googleapis.com/Package"
    _globals['_LISTPACKAGESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTPACKAGESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPACKAGESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTPACKAGESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETPACKAGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPACKAGEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'artifactregistry.googleapis.com/Package"
    _globals['_DELETEPACKAGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPACKAGEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'artifactregistry.googleapis.com/Package"
    _globals['_PACKAGE']._serialized_start = 218
    _globals['_PACKAGE']._serialized_end = 635
    _globals['_PACKAGE_ANNOTATIONSENTRY']._serialized_start = 452
    _globals['_PACKAGE_ANNOTATIONSENTRY']._serialized_end = 502
    _globals['_LISTPACKAGESREQUEST']._serialized_start = 638
    _globals['_LISTPACKAGESREQUEST']._serialized_end = 807
    _globals['_LISTPACKAGESRESPONSE']._serialized_start = 809
    _globals['_LISTPACKAGESRESPONSE']._serialized_end = 920
    _globals['_GETPACKAGEREQUEST']._serialized_start = 922
    _globals['_GETPACKAGEREQUEST']._serialized_end = 1004
    _globals['_DELETEPACKAGEREQUEST']._serialized_start = 1006
    _globals['_DELETEPACKAGEREQUEST']._serialized_end = 1091
    _globals['_UPDATEPACKAGEREQUEST']._serialized_start = 1094
    _globals['_UPDATEPACKAGEREQUEST']._serialized_end = 1228