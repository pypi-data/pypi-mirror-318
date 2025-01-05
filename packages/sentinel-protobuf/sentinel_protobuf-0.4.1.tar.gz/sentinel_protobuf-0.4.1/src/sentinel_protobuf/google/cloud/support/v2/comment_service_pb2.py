"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/support/v2/comment_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.support.v2 import comment_pb2 as google_dot_cloud_dot_support_dot_v2_dot_comment__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/support/v2/comment_service.proto\x12\x17google.cloud.support.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a%google/cloud/support/v2/comment.proto"v\n\x13ListCommentsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t"c\n\x14ListCommentsResponse\x122\n\x08comments\x18\x01 \x03(\x0b2 .google.cloud.support.v2.Comment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x88\x01\n\x14CreateCommentRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case\x126\n\x07comment\x18\x02 \x01(\x0b2 .google.cloud.support.v2.CommentB\x03\xe0A\x022\xa5\x04\n\x0eCommentService\x12\xd7\x01\n\x0cListComments\x12,.google.cloud.support.v2.ListCommentsRequest\x1a-.google.cloud.support.v2.ListCommentsResponse"j\xdaA\x06parent\x82\xd3\xe4\x93\x02[\x12(/v2/{parent=projects/*/cases/*}/commentsZ/\x12-/v2/{parent=organizations/*/cases/*}/comments\x12\xe7\x01\n\rCreateComment\x12-.google.cloud.support.v2.CreateCommentRequest\x1a .google.cloud.support.v2.Comment"\x84\x01\xdaA\x0eparent,comment\x82\xd3\xe4\x93\x02m"(/v2/{parent=projects/*/cases/*}/comments:\x07commentZ8"-/v2/{parent=organizations/*/cases/*}/comments:\x07comment\x1aO\xcaA\x1bcloudsupport.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xbc\x01\n\x1bcom.google.cloud.support.v2B\x13CommentServiceProtoP\x01Z5cloud.google.com/go/support/apiv2/supportpb;supportpb\xaa\x02\x17Google.Cloud.Support.V2\xca\x02\x17Google\\Cloud\\Support\\V2\xea\x02\x1aGoogle::Cloud::Support::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.support.v2.comment_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.support.v2B\x13CommentServiceProtoP\x01Z5cloud.google.com/go/support/apiv2/supportpb;supportpb\xaa\x02\x17Google.Cloud.Support.V2\xca\x02\x17Google\\Cloud\\Support\\V2\xea\x02\x1aGoogle::Cloud::Support::V2'
    _globals['_LISTCOMMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCOMMENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case'
    _globals['_CREATECOMMENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECOMMENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case'
    _globals['_CREATECOMMENTREQUEST'].fields_by_name['comment']._loaded_options = None
    _globals['_CREATECOMMENTREQUEST'].fields_by_name['comment']._serialized_options = b'\xe0A\x02'
    _globals['_COMMENTSERVICE']._loaded_options = None
    _globals['_COMMENTSERVICE']._serialized_options = b'\xcaA\x1bcloudsupport.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_COMMENTSERVICE'].methods_by_name['ListComments']._loaded_options = None
    _globals['_COMMENTSERVICE'].methods_by_name['ListComments']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02[\x12(/v2/{parent=projects/*/cases/*}/commentsZ/\x12-/v2/{parent=organizations/*/cases/*}/comments'
    _globals['_COMMENTSERVICE'].methods_by_name['CreateComment']._loaded_options = None
    _globals['_COMMENTSERVICE'].methods_by_name['CreateComment']._serialized_options = b'\xdaA\x0eparent,comment\x82\xd3\xe4\x93\x02m"(/v2/{parent=projects/*/cases/*}/comments:\x07commentZ8"-/v2/{parent=organizations/*/cases/*}/comments:\x07comment'
    _globals['_LISTCOMMENTSREQUEST']._serialized_start = 228
    _globals['_LISTCOMMENTSREQUEST']._serialized_end = 346
    _globals['_LISTCOMMENTSRESPONSE']._serialized_start = 348
    _globals['_LISTCOMMENTSRESPONSE']._serialized_end = 447
    _globals['_CREATECOMMENTREQUEST']._serialized_start = 450
    _globals['_CREATECOMMENTREQUEST']._serialized_end = 586
    _globals['_COMMENTSERVICE']._serialized_start = 589
    _globals['_COMMENTSERVICE']._serialized_end = 1138