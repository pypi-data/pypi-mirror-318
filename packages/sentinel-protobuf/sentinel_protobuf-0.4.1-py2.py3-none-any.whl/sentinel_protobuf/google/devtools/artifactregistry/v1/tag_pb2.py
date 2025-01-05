"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/artifactregistry/v1/tag.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/devtools/artifactregistry/v1/tag.proto\x12#google.devtools.artifactregistry.v1\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xb1\x01\n\x03Tag\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t:\x8a\x01\xeaA\x86\x01\n#artifactregistry.googleapis.com/Tag\x12_projects/{project}/locations/{location}/repositories/{repository}/packages/{package}/tags/{tag}"X\n\x0fListTagsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"c\n\x10ListTagsResponse\x126\n\x04tags\x18\x01 \x03(\x0b2(.google.devtools.artifactregistry.v1.Tag\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x1d\n\rGetTagRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"i\n\x10CreateTagRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0e\n\x06tag_id\x18\x02 \x01(\t\x125\n\x03tag\x18\x03 \x01(\x0b2(.google.devtools.artifactregistry.v1.Tag"z\n\x10UpdateTagRequest\x125\n\x03tag\x18\x01 \x01(\x0b2(.google.devtools.artifactregistry.v1.Tag\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask" \n\x10DeleteTagRequest\x12\x0c\n\x04name\x18\x01 \x01(\tB\xf3\x01\n\'com.google.devtools.artifactregistry.v1B\x08TagProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.artifactregistry.v1.tag_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.devtools.artifactregistry.v1B\x08TagProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1"
    _globals['_TAG']._loaded_options = None
    _globals['_TAG']._serialized_options = b'\xeaA\x86\x01\n#artifactregistry.googleapis.com/Tag\x12_projects/{project}/locations/{location}/repositories/{repository}/packages/{package}/tags/{tag}'
    _globals['_TAG']._serialized_start = 148
    _globals['_TAG']._serialized_end = 325
    _globals['_LISTTAGSREQUEST']._serialized_start = 327
    _globals['_LISTTAGSREQUEST']._serialized_end = 415
    _globals['_LISTTAGSRESPONSE']._serialized_start = 417
    _globals['_LISTTAGSRESPONSE']._serialized_end = 516
    _globals['_GETTAGREQUEST']._serialized_start = 518
    _globals['_GETTAGREQUEST']._serialized_end = 547
    _globals['_CREATETAGREQUEST']._serialized_start = 549
    _globals['_CREATETAGREQUEST']._serialized_end = 654
    _globals['_UPDATETAGREQUEST']._serialized_start = 656
    _globals['_UPDATETAGREQUEST']._serialized_end = 778
    _globals['_DELETETAGREQUEST']._serialized_start = 780
    _globals['_DELETETAGREQUEST']._serialized_end = 812