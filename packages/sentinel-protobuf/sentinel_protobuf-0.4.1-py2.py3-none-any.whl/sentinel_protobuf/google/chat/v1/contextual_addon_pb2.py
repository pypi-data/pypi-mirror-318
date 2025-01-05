"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/chat/v1/contextual_addon.proto')
_sym_db = _symbol_database.Default()
from ....google.chat.v1 import widgets_pb2 as google_dot_chat_dot_v1_dot_widgets__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/chat/v1/contextual_addon.proto\x12\x0egoogle.chat.v1\x1a\x1cgoogle/chat/v1/widgets.proto"\x8a\x05\n\x15ContextualAddOnMarkup\x1a\xf0\x04\n\x04Card\x12E\n\x06header\x18\x01 \x01(\x0b25.google.chat.v1.ContextualAddOnMarkup.Card.CardHeader\x12D\n\x08sections\x18\x02 \x03(\x0b22.google.chat.v1.ContextualAddOnMarkup.Card.Section\x12K\n\x0ccard_actions\x18\x03 \x03(\x0b25.google.chat.v1.ContextualAddOnMarkup.Card.CardAction\x12\x0c\n\x04name\x18\x04 \x01(\t\x1a\xd9\x01\n\nCardHeader\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08subtitle\x18\x02 \x01(\t\x12U\n\x0bimage_style\x18\x03 \x01(\x0e2@.google.chat.v1.ContextualAddOnMarkup.Card.CardHeader.ImageStyle\x12\x11\n\timage_url\x18\x04 \x01(\t"@\n\nImageStyle\x12\x1b\n\x17IMAGE_STYLE_UNSPECIFIED\x10\x00\x12\t\n\x05IMAGE\x10\x01\x12\n\n\x06AVATAR\x10\x02\x1aH\n\x07Section\x12\x0e\n\x06header\x18\x01 \x01(\t\x12-\n\x07widgets\x18\x02 \x03(\x0b2\x1c.google.chat.v1.WidgetMarkup\x1aZ\n\nCardAction\x12\x14\n\x0caction_label\x18\x01 \x01(\t\x126\n\x08on_click\x18\x02 \x01(\x0b2$.google.chat.v1.WidgetMarkup.OnClickB\xad\x01\n\x12com.google.chat.v1B\x14ContextualAddOnProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.chat.v1.contextual_addon_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x12com.google.chat.v1B\x14ContextualAddOnProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1'
    _globals['_CONTEXTUALADDONMARKUP']._serialized_start = 88
    _globals['_CONTEXTUALADDONMARKUP']._serialized_end = 738
    _globals['_CONTEXTUALADDONMARKUP_CARD']._serialized_start = 114
    _globals['_CONTEXTUALADDONMARKUP_CARD']._serialized_end = 738
    _globals['_CONTEXTUALADDONMARKUP_CARD_CARDHEADER']._serialized_start = 355
    _globals['_CONTEXTUALADDONMARKUP_CARD_CARDHEADER']._serialized_end = 572
    _globals['_CONTEXTUALADDONMARKUP_CARD_CARDHEADER_IMAGESTYLE']._serialized_start = 508
    _globals['_CONTEXTUALADDONMARKUP_CARD_CARDHEADER_IMAGESTYLE']._serialized_end = 572
    _globals['_CONTEXTUALADDONMARKUP_CARD_SECTION']._serialized_start = 574
    _globals['_CONTEXTUALADDONMARKUP_CARD_SECTION']._serialized_end = 646
    _globals['_CONTEXTUALADDONMARKUP_CARD_CARDACTION']._serialized_start = 648
    _globals['_CONTEXTUALADDONMARKUP_CARD_CARDACTION']._serialized_end = 738