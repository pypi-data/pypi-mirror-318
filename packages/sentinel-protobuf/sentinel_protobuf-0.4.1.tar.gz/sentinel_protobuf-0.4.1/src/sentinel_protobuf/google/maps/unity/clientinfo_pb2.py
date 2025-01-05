"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/maps/unity/clientinfo.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/maps/unity/clientinfo.proto\x12\x11google.maps.unity"\xee\x02\n\nClientInfo\x12\x16\n\x0eapplication_id\x18\x01 \x01(\t\x12\x1b\n\x13application_version\x18\x02 \x01(\t\x128\n\x08platform\x18\x03 \x01(\x0e2&.google.maps.unity.ClientInfo.Platform\x12\x18\n\x10operating_system\x18\x04 \x01(\t\x12\x12\n\napi_client\x18\x05 \x01(\t\x12\x14\n\x0cdevice_model\x18\x06 \x01(\t\x12\x15\n\rlanguage_code\x18\x07 \x01(\t\x12\x1e\n\x16operating_system_build\x18\x08 \x01(\t"v\n\x08Platform\x12\x18\n\x14PLATFORM_UNSPECIFIED\x10\x00\x12\n\n\x06EDITOR\x10\x01\x12\n\n\x06MAC_OS\x10\x02\x12\x0b\n\x07WINDOWS\x10\x03\x12\t\n\x05LINUX\x10\x04\x12\x0b\n\x07ANDROID\x10\x05\x12\x07\n\x03IOS\x10\x06\x12\n\n\x06WEB_GL\x10\x07Bt\n\x15com.google.maps.unityB\x0fClientInfoProtoP\x01Z.cloud.google.com/go/maps/unity/unitypb;unitypb\xa2\x02\x03GMU\xaa\x02\x11Google.Maps.Unityb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.unity.clientinfo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x15com.google.maps.unityB\x0fClientInfoProtoP\x01Z.cloud.google.com/go/maps/unity/unitypb;unitypb\xa2\x02\x03GMU\xaa\x02\x11Google.Maps.Unity'
    _globals['_CLIENTINFO']._serialized_start = 58
    _globals['_CLIENTINFO']._serialized_end = 424
    _globals['_CLIENTINFO_PLATFORM']._serialized_start = 306
    _globals['_CLIENTINFO_PLATFORM']._serialized_end = 424