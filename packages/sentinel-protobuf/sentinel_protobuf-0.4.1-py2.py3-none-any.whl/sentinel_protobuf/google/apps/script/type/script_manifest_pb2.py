"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/script/type/script_manifest.proto')
_sym_db = _symbol_database.Default()
from .....google.apps.script.type import addon_widget_set_pb2 as google_dot_apps_dot_script_dot_type_dot_addon__widget__set__pb2
from .....google.apps.script.type import extension_point_pb2 as google_dot_apps_dot_script_dot_type_dot_extension__point__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/apps/script/type/script_manifest.proto\x12\x17google.apps.script.type\x1a.google/apps/script/type/addon_widget_set.proto\x1a-google/apps/script/type/extension_point.proto\x1a\x1cgoogle/protobuf/struct.proto"\xb6\x03\n\x13CommonAddOnManifest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08logo_url\x18\x02 \x01(\t\x12D\n\x11layout_properties\x18\x03 \x01(\x0b2).google.apps.script.type.LayoutProperties\x12B\n\x11add_on_widget_set\x18\x04 \x01(\x0b2\'.google.apps.script.type.AddOnWidgetSet\x12\x1b\n\x13use_locale_from_app\x18\x05 \x01(\x08\x12I\n\x10homepage_trigger\x18\x06 \x01(\x0b2/.google.apps.script.type.HomepageExtensionPoint\x12Q\n\x11universal_actions\x18\x07 \x03(\x0b26.google.apps.script.type.UniversalActionExtensionPoint\x12:\n\x16open_link_url_prefixes\x18\x08 \x01(\x0b2\x1a.google.protobuf.ListValue"B\n\x10LayoutProperties\x12\x15\n\rprimary_color\x18\x01 \x01(\t\x12\x17\n\x0fsecondary_color\x18\x02 \x01(\t"]\n\x0bHttpOptions\x12N\n\x14authorization_header\x18\x01 \x01(\x0e20.google.apps.script.type.HttpAuthorizationHeader*v\n\x17HttpAuthorizationHeader\x12)\n%HTTP_AUTHORIZATION_HEADER_UNSPECIFIED\x10\x00\x12\x13\n\x0fSYSTEM_ID_TOKEN\x10\x01\x12\x11\n\rUSER_ID_TOKEN\x10\x02\x12\x08\n\x04NONE\x10\x03B\xa8\x01\n\x1bcom.google.apps.script.typeP\x01Z6google.golang.org/genproto/googleapis/apps/script/type\xaa\x02\x17Google.Apps.Script.Type\xca\x02\x17Google\\Apps\\Script\\Type\xea\x02\x1aGoogle::Apps::Script::Typeb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.script.type.script_manifest_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.apps.script.typeP\x01Z6google.golang.org/genproto/googleapis/apps/script/type\xaa\x02\x17Google.Apps.Script.Type\xca\x02\x17Google\\Apps\\Script\\Type\xea\x02\x1aGoogle::Apps::Script::Type'
    _globals['_HTTPAUTHORIZATIONHEADER']._serialized_start = 803
    _globals['_HTTPAUTHORIZATIONHEADER']._serialized_end = 921
    _globals['_COMMONADDONMANIFEST']._serialized_start = 200
    _globals['_COMMONADDONMANIFEST']._serialized_end = 638
    _globals['_LAYOUTPROPERTIES']._serialized_start = 640
    _globals['_LAYOUTPROPERTIES']._serialized_end = 706
    _globals['_HTTPOPTIONS']._serialized_start = 708
    _globals['_HTTPOPTIONS']._serialized_end = 801