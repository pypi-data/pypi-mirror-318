"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/chat/v1/space_read_state.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/chat/v1/space_read_state.proto\x12\x0egoogle.chat.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbc\x01\n\x0eSpaceReadState\x12\x0c\n\x04name\x18\x01 \x01(\t\x127\n\x0elast_read_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01:c\xeaA`\n"chat.googleapis.com/SpaceReadState\x12*users/{user}/spaces/{space}/spaceReadState2\x0espaceReadState"T\n\x18GetSpaceReadStateRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"chat.googleapis.com/SpaceReadState"\x92\x01\n\x1bUpdateSpaceReadStateRequest\x12=\n\x10space_read_state\x18\x01 \x01(\x0b2\x1e.google.chat.v1.SpaceReadStateB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02B\xac\x01\n\x12com.google.chat.v1B\x13SpaceReadStateProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.chat.v1.space_read_state_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x12com.google.chat.v1B\x13SpaceReadStateProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1'
    _globals['_SPACEREADSTATE'].fields_by_name['last_read_time']._loaded_options = None
    _globals['_SPACEREADSTATE'].fields_by_name['last_read_time']._serialized_options = b'\xe0A\x01'
    _globals['_SPACEREADSTATE']._loaded_options = None
    _globals['_SPACEREADSTATE']._serialized_options = b'\xeaA`\n"chat.googleapis.com/SpaceReadState\x12*users/{user}/spaces/{space}/spaceReadState2\x0espaceReadState'
    _globals['_GETSPACEREADSTATEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSPACEREADSTATEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"chat.googleapis.com/SpaceReadState'
    _globals['_UPDATESPACEREADSTATEREQUEST'].fields_by_name['space_read_state']._loaded_options = None
    _globals['_UPDATESPACEREADSTATEREQUEST'].fields_by_name['space_read_state']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESPACEREADSTATEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESPACEREADSTATEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_SPACEREADSTATE']._serialized_start = 185
    _globals['_SPACEREADSTATE']._serialized_end = 373
    _globals['_GETSPACEREADSTATEREQUEST']._serialized_start = 375
    _globals['_GETSPACEREADSTATEREQUEST']._serialized_end = 459
    _globals['_UPDATESPACEREADSTATEREQUEST']._serialized_start = 462
    _globals['_UPDATESPACEREADSTATEREQUEST']._serialized_end = 608