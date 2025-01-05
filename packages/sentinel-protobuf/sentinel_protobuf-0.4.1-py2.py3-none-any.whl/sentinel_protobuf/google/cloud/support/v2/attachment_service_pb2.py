"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/support/v2/attachment_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.support.v2 import attachment_pb2 as google_dot_cloud_dot_support_dot_v2_dot_attachment__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/support/v2/attachment_service.proto\x12\x17google.cloud.support.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/support/v2/attachment.proto"y\n\x16ListAttachmentsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"l\n\x17ListAttachmentsResponse\x128\n\x0battachments\x18\x01 \x03(\x0b2#.google.cloud.support.v2.Attachment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xd1\x02\n\x15CaseAttachmentService\x12\xe6\x01\n\x0fListAttachments\x12/.google.cloud.support.v2.ListAttachmentsRequest\x1a0.google.cloud.support.v2.ListAttachmentsResponse"p\xdaA\x06parent\x82\xd3\xe4\x93\x02a\x12+/v2/{parent=projects/*/cases/*}/attachmentsZ2\x120/v2/{parent=organizations/*/cases/*}/attachments\x1aO\xcaA\x1bcloudsupport.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xbf\x01\n\x1bcom.google.cloud.support.v2B\x16AttachmentServiceProtoP\x01Z5cloud.google.com/go/support/apiv2/supportpb;supportpb\xaa\x02\x17Google.Cloud.Support.V2\xca\x02\x17Google\\Cloud\\Support\\V2\xea\x02\x1aGoogle::Cloud::Support::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.support.v2.attachment_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.support.v2B\x16AttachmentServiceProtoP\x01Z5cloud.google.com/go/support/apiv2/supportpb;supportpb\xaa\x02\x17Google.Cloud.Support.V2\xca\x02\x17Google\\Cloud\\Support\\V2\xea\x02\x1aGoogle::Cloud::Support::V2'
    _globals['_LISTATTACHMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTATTACHMENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case'
    _globals['_CASEATTACHMENTSERVICE']._loaded_options = None
    _globals['_CASEATTACHMENTSERVICE']._serialized_options = b'\xcaA\x1bcloudsupport.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CASEATTACHMENTSERVICE'].methods_by_name['ListAttachments']._loaded_options = None
    _globals['_CASEATTACHMENTSERVICE'].methods_by_name['ListAttachments']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02a\x12+/v2/{parent=projects/*/cases/*}/attachmentsZ2\x120/v2/{parent=organizations/*/cases/*}/attachments'
    _globals['_LISTATTACHMENTSREQUEST']._serialized_start = 234
    _globals['_LISTATTACHMENTSREQUEST']._serialized_end = 355
    _globals['_LISTATTACHMENTSRESPONSE']._serialized_start = 357
    _globals['_LISTATTACHMENTSRESPONSE']._serialized_end = 465
    _globals['_CASEATTACHMENTSERVICE']._serialized_start = 468
    _globals['_CASEATTACHMENTSERVICE']._serialized_end = 805