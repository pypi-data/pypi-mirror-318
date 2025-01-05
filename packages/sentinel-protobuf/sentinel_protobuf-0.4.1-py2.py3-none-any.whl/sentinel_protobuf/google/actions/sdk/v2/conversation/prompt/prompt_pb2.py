"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/conversation/prompt/prompt.proto')
_sym_db = _symbol_database.Default()
from .......google.actions.sdk.v2.conversation.prompt.content import canvas_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_prompt_dot_content_dot_canvas__pb2
from .......google.actions.sdk.v2.conversation.prompt.content import content_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_prompt_dot_content_dot_content__pb2
from .......google.actions.sdk.v2.conversation.prompt.content import link_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_prompt_dot_content_dot_link__pb2
from .......google.actions.sdk.v2.conversation.prompt import simple_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_prompt_dot_simple__pb2
from .......google.actions.sdk.v2.conversation.prompt import suggestion_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_prompt_dot_suggestion__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/actions/sdk/v2/conversation/prompt/prompt.proto\x12"google.actions.sdk.v2.conversation\x1a>google/actions/sdk/v2/conversation/prompt/content/canvas.proto\x1a?google/actions/sdk/v2/conversation/prompt/content/content.proto\x1a<google/actions/sdk/v2/conversation/prompt/content/link.proto\x1a6google/actions/sdk/v2/conversation/prompt/simple.proto\x1a:google/actions/sdk/v2/conversation/prompt/suggestion.proto"\xa8\x03\n\x06Prompt\x12\x12\n\x06append\x18\x01 \x01(\x08B\x02\x18\x01\x12\x10\n\x08override\x18\x08 \x01(\x08\x12@\n\x0cfirst_simple\x18\x02 \x01(\x0b2*.google.actions.sdk.v2.conversation.Simple\x12<\n\x07content\x18\x03 \x01(\x0b2+.google.actions.sdk.v2.conversation.Content\x12?\n\x0blast_simple\x18\x04 \x01(\x0b2*.google.actions.sdk.v2.conversation.Simple\x12C\n\x0bsuggestions\x18\x05 \x03(\x0b2..google.actions.sdk.v2.conversation.Suggestion\x126\n\x04link\x18\x06 \x01(\x0b2(.google.actions.sdk.v2.conversation.Link\x12:\n\x06canvas\x18\t \x01(\x0b2*.google.actions.sdk.v2.conversation.CanvasB\x87\x01\n&com.google.actions.sdk.v2.conversationB\x0bPromptProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversationb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.conversation.prompt.prompt_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.actions.sdk.v2.conversationB\x0bPromptProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversation'
    _globals['_PROMPT'].fields_by_name['append']._loaded_options = None
    _globals['_PROMPT'].fields_by_name['append']._serialized_options = b'\x18\x01'
    _globals['_PROMPT']._serialized_start = 402
    _globals['_PROMPT']._serialized_end = 826