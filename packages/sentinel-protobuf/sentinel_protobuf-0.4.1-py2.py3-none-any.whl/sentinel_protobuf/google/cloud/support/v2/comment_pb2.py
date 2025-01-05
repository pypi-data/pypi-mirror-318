"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/support/v2/comment.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.support.v2 import actor_pb2 as google_dot_cloud_dot_support_dot_v2_dot_actor__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/cloud/support/v2/comment.proto\x12\x17google.cloud.support.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/cloud/support/v2/actor.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd2\x02\n\x07Comment\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x07creator\x18\x03 \x01(\x0b2\x1e.google.cloud.support.v2.ActorB\x03\xe0A\x03\x12\x0c\n\x04body\x18\x04 \x01(\t\x12\x1c\n\x0fplain_text_body\x18\x05 \x01(\tB\x03\xe0A\x03:\x9b\x01\xeaA\x97\x01\n#cloudsupport.googleapis.com/Comment\x12<organizations/{organization}/cases/{case}/comments/{comment}\x122projects/{project}/cases/{case}/comments/{comment}B\xb5\x01\n\x1bcom.google.cloud.support.v2B\x0cCommentProtoP\x01Z5cloud.google.com/go/support/apiv2/supportpb;supportpb\xaa\x02\x17Google.Cloud.Support.V2\xca\x02\x17Google\\Cloud\\Support\\V2\xea\x02\x1aGoogle::Cloud::Support::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.support.v2.comment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.support.v2B\x0cCommentProtoP\x01Z5cloud.google.com/go/support/apiv2/supportpb;supportpb\xaa\x02\x17Google.Cloud.Support.V2\xca\x02\x17Google\\Cloud\\Support\\V2\xea\x02\x1aGoogle::Cloud::Support::V2'
    _globals['_COMMENT'].fields_by_name['name']._loaded_options = None
    _globals['_COMMENT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_COMMENT'].fields_by_name['create_time']._loaded_options = None
    _globals['_COMMENT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_COMMENT'].fields_by_name['creator']._loaded_options = None
    _globals['_COMMENT'].fields_by_name['creator']._serialized_options = b'\xe0A\x03'
    _globals['_COMMENT'].fields_by_name['plain_text_body']._loaded_options = None
    _globals['_COMMENT'].fields_by_name['plain_text_body']._serialized_options = b'\xe0A\x03'
    _globals['_COMMENT']._loaded_options = None
    _globals['_COMMENT']._serialized_options = b'\xeaA\x97\x01\n#cloudsupport.googleapis.com/Comment\x12<organizations/{organization}/cases/{case}/comments/{comment}\x122projects/{project}/cases/{case}/comments/{comment}'
    _globals['_COMMENT']._serialized_start = 197
    _globals['_COMMENT']._serialized_end = 535