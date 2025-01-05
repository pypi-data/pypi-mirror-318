"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/chat/v1/user.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19google/chat/v1/user.proto\x12\x0egoogle.chat.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xb8\x01\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x11\n\tdomain_id\x18\x06 \x01(\t\x12\'\n\x04type\x18\x05 \x01(\x0e2\x19.google.chat.v1.User.Type\x12\x19\n\x0cis_anonymous\x18\x07 \x01(\x08B\x03\xe0A\x03"0\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05HUMAN\x10\x01\x12\x07\n\x03BOT\x10\x02B\xa2\x01\n\x12com.google.chat.v1B\tUserProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.chat.v1.user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x12com.google.chat.v1B\tUserProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1'
    _globals['_USER'].fields_by_name['display_name']._loaded_options = None
    _globals['_USER'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_USER'].fields_by_name['is_anonymous']._loaded_options = None
    _globals['_USER'].fields_by_name['is_anonymous']._serialized_options = b'\xe0A\x03'
    _globals['_USER']._serialized_start = 106
    _globals['_USER']._serialized_end = 290
    _globals['_USER_TYPE']._serialized_start = 242
    _globals['_USER_TYPE']._serialized_end = 290