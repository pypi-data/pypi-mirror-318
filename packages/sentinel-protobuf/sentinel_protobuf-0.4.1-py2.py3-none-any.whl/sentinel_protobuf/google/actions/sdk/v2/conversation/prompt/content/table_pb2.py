"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/conversation/prompt/content/table.proto')
_sym_db = _symbol_database.Default()
from ........google.actions.sdk.v2.conversation.prompt.content import image_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_prompt_dot_content_dot_image__pb2
from ........google.actions.sdk.v2.conversation.prompt.content import link_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_prompt_dot_content_dot_link__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/actions/sdk/v2/conversation/prompt/content/table.proto\x12"google.actions.sdk.v2.conversation\x1a=google/actions/sdk/v2/conversation/prompt/content/image.proto\x1a<google/actions/sdk/v2/conversation/prompt/content/link.proto"\x9a\x02\n\x05Table\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08subtitle\x18\x02 \x01(\t\x128\n\x05image\x18\x04 \x01(\x0b2).google.actions.sdk.v2.conversation.Image\x12@\n\x07columns\x18\x05 \x03(\x0b2/.google.actions.sdk.v2.conversation.TableColumn\x12:\n\x04rows\x18\x06 \x03(\x0b2,.google.actions.sdk.v2.conversation.TableRow\x128\n\x06button\x18\x07 \x01(\x0b2(.google.actions.sdk.v2.conversation.Link"\xc0\x01\n\x0bTableColumn\x12\x0e\n\x06header\x18\x01 \x01(\t\x12R\n\x05align\x18\x02 \x01(\x0e2C.google.actions.sdk.v2.conversation.TableColumn.HorizontalAlignment"M\n\x13HorizontalAlignment\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07LEADING\x10\x01\x12\n\n\x06CENTER\x10\x02\x12\x0c\n\x08TRAILING\x10\x03"\x19\n\tTableCell\x12\x0c\n\x04text\x18\x01 \x01(\t"Y\n\x08TableRow\x12<\n\x05cells\x18\x01 \x03(\x0b2-.google.actions.sdk.v2.conversation.TableCell\x12\x0f\n\x07divider\x18\x02 \x01(\x08B\x86\x01\n&com.google.actions.sdk.v2.conversationB\nTableProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversationb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.conversation.prompt.content.table_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.actions.sdk.v2.conversationB\nTableProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversation'
    _globals['_TABLE']._serialized_start = 227
    _globals['_TABLE']._serialized_end = 509
    _globals['_TABLECOLUMN']._serialized_start = 512
    _globals['_TABLECOLUMN']._serialized_end = 704
    _globals['_TABLECOLUMN_HORIZONTALALIGNMENT']._serialized_start = 627
    _globals['_TABLECOLUMN_HORIZONTALALIGNMENT']._serialized_end = 704
    _globals['_TABLECELL']._serialized_start = 706
    _globals['_TABLECELL']._serialized_end = 731
    _globals['_TABLEROW']._serialized_start = 733
    _globals['_TABLEROW']._serialized_end = 822