"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/chat/v1/widgets.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cgoogle/chat/v1/widgets.proto\x12\x0egoogle.chat.v1"\xf5\x0e\n\x0cWidgetMarkup\x12D\n\x0etext_paragraph\x18\x01 \x01(\x0b2*.google.chat.v1.WidgetMarkup.TextParagraphH\x00\x123\n\x05image\x18\x02 \x01(\x0b2".google.chat.v1.WidgetMarkup.ImageH\x00\x12:\n\tkey_value\x18\x03 \x01(\x0b2%.google.chat.v1.WidgetMarkup.KeyValueH\x00\x124\n\x07buttons\x18\x06 \x03(\x0b2#.google.chat.v1.WidgetMarkup.Button\x1a\x1d\n\rTextParagraph\x12\x0c\n\x04text\x18\x01 \x01(\t\x1a\x92\x01\n\x06Button\x12>\n\x0btext_button\x18\x01 \x01(\x0b2\'.google.chat.v1.WidgetMarkup.TextButtonH\x00\x12@\n\x0cimage_button\x18\x02 \x01(\x0b2(.google.chat.v1.WidgetMarkup.ImageButtonH\x00B\x06\n\x04type\x1aR\n\nTextButton\x12\x0c\n\x04text\x18\x01 \x01(\t\x126\n\x08on_click\x18\x02 \x01(\x0b2$.google.chat.v1.WidgetMarkup.OnClick\x1a\xa9\x02\n\x08KeyValue\x121\n\x04icon\x18\x01 \x01(\x0e2!.google.chat.v1.WidgetMarkup.IconH\x00\x12\x12\n\x08icon_url\x18\x02 \x01(\tH\x00\x12\x11\n\ttop_label\x18\x03 \x01(\t\x12\x0f\n\x07content\x18\x04 \x01(\t\x12\x19\n\x11content_multiline\x18\t \x01(\x08\x12\x14\n\x0cbottom_label\x18\x05 \x01(\t\x126\n\x08on_click\x18\x06 \x01(\x0b2$.google.chat.v1.WidgetMarkup.OnClick\x125\n\x06button\x18\x07 \x01(\x0b2#.google.chat.v1.WidgetMarkup.ButtonH\x01B\x07\n\x05iconsB\t\n\x07control\x1ah\n\x05Image\x12\x11\n\timage_url\x18\x01 \x01(\t\x126\n\x08on_click\x18\x02 \x01(\x0b2$.google.chat.v1.WidgetMarkup.OnClick\x12\x14\n\x0caspect_ratio\x18\x03 \x01(\x01\x1a\xa3\x01\n\x0bImageButton\x121\n\x04icon\x18\x01 \x01(\x0e2!.google.chat.v1.WidgetMarkup.IconH\x00\x12\x12\n\x08icon_url\x18\x03 \x01(\tH\x00\x126\n\x08on_click\x18\x02 \x01(\x0b2$.google.chat.v1.WidgetMarkup.OnClick\x12\x0c\n\x04name\x18\x04 \x01(\tB\x07\n\x05icons\x1a\x88\x01\n\x07OnClick\x129\n\x06action\x18\x01 \x01(\x0b2\'.google.chat.v1.WidgetMarkup.FormActionH\x00\x12:\n\topen_link\x18\x02 \x01(\x0b2%.google.chat.v1.WidgetMarkup.OpenLinkH\x00B\x06\n\x04data\x1a\x17\n\x08OpenLink\x12\x0b\n\x03url\x18\x01 \x01(\t\x1a\xa4\x01\n\nFormAction\x12\x1a\n\x12action_method_name\x18\x01 \x01(\t\x12K\n\nparameters\x18\x02 \x03(\x0b27.google.chat.v1.WidgetMarkup.FormAction.ActionParameter\x1a-\n\x0fActionParameter\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t"\xe0\x03\n\x04Icon\x12\x14\n\x10ICON_UNSPECIFIED\x10\x00\x12\x0c\n\x08AIRPLANE\x10\x01\x12\x0c\n\x08BOOKMARK\x10\x1a\x12\x07\n\x03BUS\x10\x19\x12\x07\n\x03CAR\x10\t\x12\t\n\x05CLOCK\x10\x02\x12\x1c\n\x18CONFIRMATION_NUMBER_ICON\x10\x0c\x12\n\n\x06DOLLAR\x10\x0e\x12\x0f\n\x0bDESCRIPTION\x10\x1b\x12\t\n\x05EMAIL\x10\n\x12\x13\n\x0fEVENT_PERFORMER\x10\x14\x12\x0e\n\nEVENT_SEAT\x10\x15\x12\x12\n\x0eFLIGHT_ARRIVAL\x10\x10\x12\x14\n\x10FLIGHT_DEPARTURE\x10\x0f\x12\t\n\x05HOTEL\x10\x06\x12\x13\n\x0fHOTEL_ROOM_TYPE\x10\x11\x12\n\n\x06INVITE\x10\x13\x12\x0b\n\x07MAP_PIN\x10\x03\x12\x0e\n\nMEMBERSHIP\x10\x18\x12\x13\n\x0fMULTIPLE_PEOPLE\x10\x12\x12\t\n\x05OFFER\x10\x1e\x12\n\n\x06PERSON\x10\x0b\x12\t\n\x05PHONE\x10\r\x12\x13\n\x0fRESTAURANT_ICON\x10\x07\x12\x11\n\rSHOPPING_CART\x10\x08\x12\x08\n\x04STAR\x10\x05\x12\t\n\x05STORE\x10\x16\x12\n\n\x06TICKET\x10\x04\x12\t\n\x05TRAIN\x10\x17\x12\x10\n\x0cVIDEO_CAMERA\x10\x1c\x12\x0e\n\nVIDEO_PLAY\x10\x1dB\x06\n\x04dataB\xa5\x01\n\x12com.google.chat.v1B\x0cWidgetsProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.chat.v1.widgets_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x12com.google.chat.v1B\x0cWidgetsProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1'
    _globals['_WIDGETMARKUP']._serialized_start = 49
    _globals['_WIDGETMARKUP']._serialized_end = 1958
    _globals['_WIDGETMARKUP_TEXTPARAGRAPH']._serialized_start = 302
    _globals['_WIDGETMARKUP_TEXTPARAGRAPH']._serialized_end = 331
    _globals['_WIDGETMARKUP_BUTTON']._serialized_start = 334
    _globals['_WIDGETMARKUP_BUTTON']._serialized_end = 480
    _globals['_WIDGETMARKUP_TEXTBUTTON']._serialized_start = 482
    _globals['_WIDGETMARKUP_TEXTBUTTON']._serialized_end = 564
    _globals['_WIDGETMARKUP_KEYVALUE']._serialized_start = 567
    _globals['_WIDGETMARKUP_KEYVALUE']._serialized_end = 864
    _globals['_WIDGETMARKUP_IMAGE']._serialized_start = 866
    _globals['_WIDGETMARKUP_IMAGE']._serialized_end = 970
    _globals['_WIDGETMARKUP_IMAGEBUTTON']._serialized_start = 973
    _globals['_WIDGETMARKUP_IMAGEBUTTON']._serialized_end = 1136
    _globals['_WIDGETMARKUP_ONCLICK']._serialized_start = 1139
    _globals['_WIDGETMARKUP_ONCLICK']._serialized_end = 1275
    _globals['_WIDGETMARKUP_OPENLINK']._serialized_start = 1277
    _globals['_WIDGETMARKUP_OPENLINK']._serialized_end = 1300
    _globals['_WIDGETMARKUP_FORMACTION']._serialized_start = 1303
    _globals['_WIDGETMARKUP_FORMACTION']._serialized_end = 1467
    _globals['_WIDGETMARKUP_FORMACTION_ACTIONPARAMETER']._serialized_start = 1422
    _globals['_WIDGETMARKUP_FORMACTION_ACTIONPARAMETER']._serialized_end = 1467
    _globals['_WIDGETMARKUP_ICON']._serialized_start = 1470
    _globals['_WIDGETMARKUP_ICON']._serialized_end = 1950