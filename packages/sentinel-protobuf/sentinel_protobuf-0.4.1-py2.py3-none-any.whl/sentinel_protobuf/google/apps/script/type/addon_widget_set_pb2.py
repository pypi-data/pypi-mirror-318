"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/script/type/addon_widget_set.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/apps/script/type/addon_widget_set.proto\x12\x17google.apps.script.type"\xa4\x02\n\x0eAddOnWidgetSet\x12H\n\x0cused_widgets\x18\x01 \x03(\x0e22.google.apps.script.type.AddOnWidgetSet.WidgetType"\xc7\x01\n\nWidgetType\x12\x1b\n\x17WIDGET_TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bDATE_PICKER\x10\x01\x12\x12\n\x0eSTYLED_BUTTONS\x10\x02\x12\x14\n\x10PERSISTENT_FORMS\x10\x03\x12\x10\n\x0cFIXED_FOOTER\x10\x04\x12!\n\x1dUPDATE_SUBJECT_AND_RECIPIENTS\x10\x05\x12\x0f\n\x0bGRID_WIDGET\x10\x06\x12\x1b\n\x17ADDON_COMPOSE_UI_ACTION\x10\x07B\xbd\x01\n\x1bcom.google.apps.script.typeB\x13AddOnWidgetSetProtoP\x01Z6google.golang.org/genproto/googleapis/apps/script/type\xaa\x02\x17Google.Apps.Script.Type\xca\x02\x17Google\\Apps\\Script\\Type\xea\x02\x1aGoogle::Apps::Script::Typeb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.script.type.addon_widget_set_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.apps.script.typeB\x13AddOnWidgetSetProtoP\x01Z6google.golang.org/genproto/googleapis/apps/script/type\xaa\x02\x17Google.Apps.Script.Type\xca\x02\x17Google\\Apps\\Script\\Type\xea\x02\x1aGoogle::Apps::Script::Type'
    _globals['_ADDONWIDGETSET']._serialized_start = 76
    _globals['_ADDONWIDGETSET']._serialized_end = 368
    _globals['_ADDONWIDGETSET_WIDGETTYPE']._serialized_start = 169
    _globals['_ADDONWIDGETSET_WIDGETTYPE']._serialized_end = 368