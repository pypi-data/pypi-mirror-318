"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/script/type/extension_point.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/apps/script/type/extension_point.proto\x12\x17google.apps.script.type\x1a\x1egoogle/protobuf/wrappers.proto"O\n\x16MenuItemExtensionPoint\x12\x14\n\x0crun_function\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x10\n\x08logo_url\x18\x03 \x01(\t"[\n\x16HomepageExtensionPoint\x12\x14\n\x0crun_function\x18\x01 \x01(\t\x12+\n\x07enabled\x18\x02 \x01(\x0b2\x1a.google.protobuf.BoolValue"j\n\x1dUniversalActionExtensionPoint\x12\r\n\x05label\x18\x01 \x01(\t\x12\x13\n\topen_link\x18\x02 \x01(\tH\x00\x12\x16\n\x0crun_function\x18\x03 \x01(\tH\x00B\r\n\x0baction_typeB\xa8\x01\n\x1bcom.google.apps.script.typeP\x01Z6google.golang.org/genproto/googleapis/apps/script/type\xaa\x02\x17Google.Apps.Script.Type\xca\x02\x17Google\\Apps\\Script\\Type\xea\x02\x1aGoogle::Apps::Script::Typeb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.script.type.extension_point_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.apps.script.typeP\x01Z6google.golang.org/genproto/googleapis/apps/script/type\xaa\x02\x17Google.Apps.Script.Type\xca\x02\x17Google\\Apps\\Script\\Type\xea\x02\x1aGoogle::Apps::Script::Type'
    _globals['_MENUITEMEXTENSIONPOINT']._serialized_start = 106
    _globals['_MENUITEMEXTENSIONPOINT']._serialized_end = 185
    _globals['_HOMEPAGEEXTENSIONPOINT']._serialized_start = 187
    _globals['_HOMEPAGEEXTENSIONPOINT']._serialized_end = 278
    _globals['_UNIVERSALACTIONEXTENSIONPOINT']._serialized_start = 280
    _globals['_UNIVERSALACTIONEXTENSIONPOINT']._serialized_end = 386