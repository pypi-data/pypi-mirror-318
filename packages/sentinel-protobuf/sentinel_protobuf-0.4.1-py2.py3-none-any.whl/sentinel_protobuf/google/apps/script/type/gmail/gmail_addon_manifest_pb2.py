"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/script/type/gmail/gmail_addon_manifest.proto')
_sym_db = _symbol_database.Default()
from ......google.apps.script.type import addon_widget_set_pb2 as google_dot_apps_dot_script_dot_type_dot_addon__widget__set__pb2
from ......google.apps.script.type import extension_point_pb2 as google_dot_apps_dot_script_dot_type_dot_extension__point__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/apps/script/type/gmail/gmail_addon_manifest.proto\x12\x1dgoogle.apps.script.type.gmail\x1a.google/apps/script/type/addon_widget_set.proto\x1a-google/apps/script/type/extension_point.proto"\xe7\x02\n\x12GmailAddOnManifest\x12I\n\x10homepage_trigger\x18\x0e \x01(\x0b2/.google.apps.script.type.HomepageExtensionPoint\x12M\n\x13contextual_triggers\x18\x03 \x03(\x0b20.google.apps.script.type.gmail.ContextualTrigger\x12I\n\x11universal_actions\x18\x04 \x03(\x0b2..google.apps.script.type.gmail.UniversalAction\x12F\n\x0fcompose_trigger\x18\x0c \x01(\x0b2-.google.apps.script.type.gmail.ComposeTrigger\x12$\n\x1cauthorization_check_function\x18\x07 \x01(\t"[\n\x0fUniversalAction\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x13\n\topen_link\x18\x02 \x01(\tH\x00\x12\x16\n\x0crun_function\x18\x03 \x01(\tH\x00B\r\n\x0baction_type"\xdb\x01\n\x0eComposeTrigger\x12@\n\x07actions\x18\x05 \x03(\x0b2/.google.apps.script.type.MenuItemExtensionPoint\x12O\n\x0cdraft_access\x18\x04 \x01(\x0e29.google.apps.script.type.gmail.ComposeTrigger.DraftAccess"6\n\x0bDraftAccess\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\x0c\n\x08METADATA\x10\x02"\x89\x01\n\x11ContextualTrigger\x12L\n\runconditional\x18\x01 \x01(\x0b23.google.apps.script.type.gmail.UnconditionalTriggerH\x00\x12\x1b\n\x13on_trigger_function\x18\x04 \x01(\tB\t\n\x07trigger"\x16\n\x14UnconditionalTriggerB\xe0\x01\n!com.google.apps.script.type.gmailB\x17GmailAddOnManifestProtoP\x01Z<google.golang.org/genproto/googleapis/apps/script/type/gmail\xaa\x02\x1dGoogle.Apps.Script.Type.Gmail\xca\x02\x1dGoogle\\Apps\\Script\\Type\\Gmail\xea\x02!Google::Apps::Script::Type::Gmailb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.script.type.gmail.gmail_addon_manifest_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.apps.script.type.gmailB\x17GmailAddOnManifestProtoP\x01Z<google.golang.org/genproto/googleapis/apps/script/type/gmail\xaa\x02\x1dGoogle.Apps.Script.Type.Gmail\xca\x02\x1dGoogle\\Apps\\Script\\Type\\Gmail\xea\x02!Google::Apps::Script::Type::Gmail'
    _globals['_GMAILADDONMANIFEST']._serialized_start = 187
    _globals['_GMAILADDONMANIFEST']._serialized_end = 546
    _globals['_UNIVERSALACTION']._serialized_start = 548
    _globals['_UNIVERSALACTION']._serialized_end = 639
    _globals['_COMPOSETRIGGER']._serialized_start = 642
    _globals['_COMPOSETRIGGER']._serialized_end = 861
    _globals['_COMPOSETRIGGER_DRAFTACCESS']._serialized_start = 807
    _globals['_COMPOSETRIGGER_DRAFTACCESS']._serialized_end = 861
    _globals['_CONTEXTUALTRIGGER']._serialized_start = 864
    _globals['_CONTEXTUALTRIGGER']._serialized_end = 1001
    _globals['_UNCONDITIONALTRIGGER']._serialized_start = 1003
    _globals['_UNCONDITIONALTRIGGER']._serialized_end = 1025