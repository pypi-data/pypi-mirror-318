"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/artifactregistry/v1/attachment.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/devtools/artifactregistry/v1/attachment.proto\x12#google.devtools.artifactregistry.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc2\x04\n\nAttachment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x06target\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x1c\n\x14attachment_namespace\x18\x04 \x01(\t\x12Z\n\x0bannotations\x18\x05 \x03(\x0b2@.google.devtools.artifactregistry.v1.Attachment.AnnotationsEntryB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12;\n\x05files\x18\x08 \x03(\tB,\xe0A\x02\xfaA&\n$artifactregistry.googleapis.com/File\x12\x1d\n\x10oci_version_name\x18\t \x01(\tB\x03\xe0A\x03\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x8c\x01\xeaA\x88\x01\n*artifactregistry.googleapis.com/Attachment\x12Zprojects/{project}/locations/{location}/repositories/{repository}/attachments/{attachment}"\x98\x01\n\x16ListAttachmentsRequest\x12B\n\x06parent\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\x12*artifactregistry.googleapis.com/Attachment\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"x\n\x17ListAttachmentsResponse\x12D\n\x0battachments\x18\x01 \x03(\x0b2/.google.devtools.artifactregistry.v1.Attachment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"X\n\x14GetAttachmentRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*artifactregistry.googleapis.com/Attachment"\xc3\x01\n\x17CreateAttachmentRequest\x12B\n\x06parent\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\x12*artifactregistry.googleapis.com/Attachment\x12\x1a\n\rattachment_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12H\n\nattachment\x18\x03 \x01(\x0b2/.google.devtools.artifactregistry.v1.AttachmentB\x03\xe0A\x02"[\n\x17DeleteAttachmentRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*artifactregistry.googleapis.com/AttachmentB\xfa\x01\n\'com.google.devtools.artifactregistry.v1B\x0fAttachmentProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.artifactregistry.v1.attachment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.devtools.artifactregistry.v1B\x0fAttachmentProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1"
    _globals['_ATTACHMENT_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_ATTACHMENT_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_ATTACHMENT'].fields_by_name['target']._loaded_options = None
    _globals['_ATTACHMENT'].fields_by_name['target']._serialized_options = b'\xe0A\x02'
    _globals['_ATTACHMENT'].fields_by_name['annotations']._loaded_options = None
    _globals['_ATTACHMENT'].fields_by_name['annotations']._serialized_options = b'\xe0A\x01'
    _globals['_ATTACHMENT'].fields_by_name['create_time']._loaded_options = None
    _globals['_ATTACHMENT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ATTACHMENT'].fields_by_name['update_time']._loaded_options = None
    _globals['_ATTACHMENT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ATTACHMENT'].fields_by_name['files']._loaded_options = None
    _globals['_ATTACHMENT'].fields_by_name['files']._serialized_options = b'\xe0A\x02\xfaA&\n$artifactregistry.googleapis.com/File'
    _globals['_ATTACHMENT'].fields_by_name['oci_version_name']._loaded_options = None
    _globals['_ATTACHMENT'].fields_by_name['oci_version_name']._serialized_options = b'\xe0A\x03'
    _globals['_ATTACHMENT']._loaded_options = None
    _globals['_ATTACHMENT']._serialized_options = b'\xeaA\x88\x01\n*artifactregistry.googleapis.com/Attachment\x12Zprojects/{project}/locations/{location}/repositories/{repository}/attachments/{attachment}'
    _globals['_LISTATTACHMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTATTACHMENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA,\x12*artifactregistry.googleapis.com/Attachment'
    _globals['_LISTATTACHMENTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTATTACHMENTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_GETATTACHMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETATTACHMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*artifactregistry.googleapis.com/Attachment'
    _globals['_CREATEATTACHMENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEATTACHMENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA,\x12*artifactregistry.googleapis.com/Attachment'
    _globals['_CREATEATTACHMENTREQUEST'].fields_by_name['attachment_id']._loaded_options = None
    _globals['_CREATEATTACHMENTREQUEST'].fields_by_name['attachment_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEATTACHMENTREQUEST'].fields_by_name['attachment']._loaded_options = None
    _globals['_CREATEATTACHMENTREQUEST'].fields_by_name['attachment']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEATTACHMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEATTACHMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*artifactregistry.googleapis.com/Attachment'
    _globals['_ATTACHMENT']._serialized_start = 187
    _globals['_ATTACHMENT']._serialized_end = 765
    _globals['_ATTACHMENT_ANNOTATIONSENTRY']._serialized_start = 572
    _globals['_ATTACHMENT_ANNOTATIONSENTRY']._serialized_end = 622
    _globals['_LISTATTACHMENTSREQUEST']._serialized_start = 768
    _globals['_LISTATTACHMENTSREQUEST']._serialized_end = 920
    _globals['_LISTATTACHMENTSRESPONSE']._serialized_start = 922
    _globals['_LISTATTACHMENTSRESPONSE']._serialized_end = 1042
    _globals['_GETATTACHMENTREQUEST']._serialized_start = 1044
    _globals['_GETATTACHMENTREQUEST']._serialized_end = 1132
    _globals['_CREATEATTACHMENTREQUEST']._serialized_start = 1135
    _globals['_CREATEATTACHMENTREQUEST']._serialized_end = 1330
    _globals['_DELETEATTACHMENTREQUEST']._serialized_start = 1332
    _globals['_DELETEATTACHMENTREQUEST']._serialized_end = 1423