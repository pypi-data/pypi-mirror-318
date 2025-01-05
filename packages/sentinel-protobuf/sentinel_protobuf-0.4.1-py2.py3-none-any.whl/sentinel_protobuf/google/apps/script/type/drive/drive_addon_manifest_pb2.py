"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/script/type/drive/drive_addon_manifest.proto')
_sym_db = _symbol_database.Default()
from ......google.apps.script.type import extension_point_pb2 as google_dot_apps_dot_script_dot_type_dot_extension__point__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/apps/script/type/drive/drive_addon_manifest.proto\x12\x1dgoogle.apps.script.type.drive\x1a-google/apps/script/type/extension_point.proto"\xb6\x01\n\x12DriveAddOnManifest\x12I\n\x10homepage_trigger\x18\x01 \x01(\x0b2/.google.apps.script.type.HomepageExtensionPoint\x12U\n\x19on_items_selected_trigger\x18\x02 \x01(\x0b22.google.apps.script.type.drive.DriveExtensionPoint"+\n\x13DriveExtensionPoint\x12\x14\n\x0crun_function\x18\x01 \x01(\tB\xe0\x01\n!com.google.apps.script.type.driveB\x17DriveAddOnManifestProtoP\x01Z<google.golang.org/genproto/googleapis/apps/script/type/drive\xaa\x02\x1dGoogle.Apps.Script.Type.Drive\xca\x02\x1dGoogle\\Apps\\Script\\Type\\Drive\xea\x02!Google::Apps::Script::Type::Driveb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.script.type.drive.drive_addon_manifest_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.apps.script.type.driveB\x17DriveAddOnManifestProtoP\x01Z<google.golang.org/genproto/googleapis/apps/script/type/drive\xaa\x02\x1dGoogle.Apps.Script.Type.Drive\xca\x02\x1dGoogle\\Apps\\Script\\Type\\Drive\xea\x02!Google::Apps::Script::Type::Drive'
    _globals['_DRIVEADDONMANIFEST']._serialized_start = 139
    _globals['_DRIVEADDONMANIFEST']._serialized_end = 321
    _globals['_DRIVEEXTENSIONPOINT']._serialized_start = 323
    _globals['_DRIVEEXTENSIONPOINT']._serialized_end = 366