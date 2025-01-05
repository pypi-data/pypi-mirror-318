"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/conversation/prompt/content/content.proto')
_sym_db = _symbol_database.Default()
from ........google.actions.sdk.v2.conversation.prompt.content import canvas_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_prompt_dot_content_dot_canvas__pb2
from ........google.actions.sdk.v2.conversation.prompt.content import card_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_prompt_dot_content_dot_card__pb2
from ........google.actions.sdk.v2.conversation.prompt.content import collection_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_prompt_dot_content_dot_collection__pb2
from ........google.actions.sdk.v2.conversation.prompt.content import image_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_prompt_dot_content_dot_image__pb2
from ........google.actions.sdk.v2.conversation.prompt.content import list_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_prompt_dot_content_dot_list__pb2
from ........google.actions.sdk.v2.conversation.prompt.content import media_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_prompt_dot_content_dot_media__pb2
from ........google.actions.sdk.v2.conversation.prompt.content import table_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_prompt_dot_content_dot_table__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/actions/sdk/v2/conversation/prompt/content/content.proto\x12"google.actions.sdk.v2.conversation\x1a>google/actions/sdk/v2/conversation/prompt/content/canvas.proto\x1a<google/actions/sdk/v2/conversation/prompt/content/card.proto\x1aBgoogle/actions/sdk/v2/conversation/prompt/content/collection.proto\x1a=google/actions/sdk/v2/conversation/prompt/content/image.proto\x1a<google/actions/sdk/v2/conversation/prompt/content/list.proto\x1a=google/actions/sdk/v2/conversation/prompt/content/media.proto\x1a=google/actions/sdk/v2/conversation/prompt/content/table.proto"\xc4\x03\n\x07Content\x128\n\x04card\x18\x01 \x01(\x0b2(.google.actions.sdk.v2.conversation.CardH\x00\x12:\n\x05image\x18\x02 \x01(\x0b2).google.actions.sdk.v2.conversation.ImageH\x00\x12:\n\x05table\x18\x03 \x01(\x0b2).google.actions.sdk.v2.conversation.TableH\x00\x12:\n\x05media\x18\x04 \x01(\x0b2).google.actions.sdk.v2.conversation.MediaH\x00\x12@\n\x06canvas\x18\x05 \x01(\x0b2*.google.actions.sdk.v2.conversation.CanvasB\x02\x18\x01H\x00\x12D\n\ncollection\x18\x06 \x01(\x0b2..google.actions.sdk.v2.conversation.CollectionH\x00\x128\n\x04list\x18\x07 \x01(\x0b2(.google.actions.sdk.v2.conversation.ListH\x00B\t\n\x07contentB\x88\x01\n&com.google.actions.sdk.v2.conversationB\x0cContentProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversationb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.conversation.prompt.content.content_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.actions.sdk.v2.conversationB\x0cContentProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversation'
    _globals['_CONTENT'].fields_by_name['canvas']._loaded_options = None
    _globals['_CONTENT'].fields_by_name['canvas']._serialized_options = b'\x18\x01'
    _globals['_CONTENT']._serialized_start = 549
    _globals['_CONTENT']._serialized_end = 1001