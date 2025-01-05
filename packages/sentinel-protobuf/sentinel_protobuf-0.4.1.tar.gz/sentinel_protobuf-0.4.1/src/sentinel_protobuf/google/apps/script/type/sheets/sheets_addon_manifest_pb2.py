"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/script/type/sheets/sheets_addon_manifest.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.apps.script.type import extension_point_pb2 as google_dot_apps_dot_script_dot_type_dot_extension__point__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/apps/script/type/sheets/sheets_addon_manifest.proto\x12\x1egoogle.apps.script.type.sheets\x1a\x1fgoogle/api/field_behavior.proto\x1a-google/apps/script/type/extension_point.proto"\xbd\x01\n\x13SheetsAddOnManifest\x12I\n\x10homepage_trigger\x18\x03 \x01(\x0b2/.google.apps.script.type.HomepageExtensionPoint\x12[\n\x1don_file_scope_granted_trigger\x18\x05 \x01(\x0b24.google.apps.script.type.sheets.SheetsExtensionPoint"1\n\x14SheetsExtensionPoint\x12\x19\n\x0crun_function\x18\x01 \x01(\tB\x03\xe0A\x02B\xe6\x01\n"com.google.apps.script.type.sheetsB\x18SheetsAddOnManifestProtoP\x01Z=google.golang.org/genproto/googleapis/apps/script/type/sheets\xaa\x02\x1eGoogle.Apps.Script.Type.Sheets\xca\x02\x1eGoogle\\Apps\\Script\\Type\\Sheets\xea\x02"Google::Apps::Script::Type::Sheetsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.script.type.sheets.sheets_addon_manifest_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.apps.script.type.sheetsB\x18SheetsAddOnManifestProtoP\x01Z=google.golang.org/genproto/googleapis/apps/script/type/sheets\xaa\x02\x1eGoogle.Apps.Script.Type.Sheets\xca\x02\x1eGoogle\\Apps\\Script\\Type\\Sheets\xea\x02"Google::Apps::Script::Type::Sheets'
    _globals['_SHEETSEXTENSIONPOINT'].fields_by_name['run_function']._loaded_options = None
    _globals['_SHEETSEXTENSIONPOINT'].fields_by_name['run_function']._serialized_options = b'\xe0A\x02'
    _globals['_SHEETSADDONMANIFEST']._serialized_start = 175
    _globals['_SHEETSADDONMANIFEST']._serialized_end = 364
    _globals['_SHEETSEXTENSIONPOINT']._serialized_start = 366
    _globals['_SHEETSEXTENSIONPOINT']._serialized_end = 415