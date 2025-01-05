"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/identity/accesscontextmanager/type/device_resources.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/identity/accesscontextmanager/type/device_resources.proto\x12)google.identity.accesscontextmanager.type*p\n\x16DeviceEncryptionStatus\x12\x1a\n\x16ENCRYPTION_UNSPECIFIED\x10\x00\x12\x1a\n\x16ENCRYPTION_UNSUPPORTED\x10\x01\x12\x0f\n\x0bUNENCRYPTED\x10\x02\x12\r\n\tENCRYPTED\x10\x03*\x82\x01\n\x06OsType\x12\x12\n\x0eOS_UNSPECIFIED\x10\x00\x12\x0f\n\x0bDESKTOP_MAC\x10\x01\x12\x13\n\x0fDESKTOP_WINDOWS\x10\x02\x12\x11\n\rDESKTOP_LINUX\x10\x03\x12\x15\n\x11DESKTOP_CHROME_OS\x10\x06\x12\x0b\n\x07ANDROID\x10\x04\x12\x07\n\x03IOS\x10\x05*V\n\x15DeviceManagementLevel\x12\x1a\n\x16MANAGEMENT_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\t\n\x05BASIC\x10\x02\x12\x0c\n\x08COMPLETE\x10\x03B\x8d\x02\n-com.google.identity.accesscontextmanager.typeB\tTypeProtoP\x01ZHgoogle.golang.org/genproto/googleapis/identity/accesscontextmanager/type\xaa\x02)Google.Identity.AccessContextManager.Type\xca\x02)Google\\Identity\\AccessContextManager\\Type\xea\x02,Google::Identity::AccessContextManager::Typeb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.identity.accesscontextmanager.type.device_resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n-com.google.identity.accesscontextmanager.typeB\tTypeProtoP\x01ZHgoogle.golang.org/genproto/googleapis/identity/accesscontextmanager/type\xaa\x02)Google.Identity.AccessContextManager.Type\xca\x02)Google\\Identity\\AccessContextManager\\Type\xea\x02,Google::Identity::AccessContextManager::Type'
    _globals['_DEVICEENCRYPTIONSTATUS']._serialized_start = 111
    _globals['_DEVICEENCRYPTIONSTATUS']._serialized_end = 223
    _globals['_OSTYPE']._serialized_start = 226
    _globals['_OSTYPE']._serialized_end = 356
    _globals['_DEVICEMANAGEMENTLEVEL']._serialized_start = 358
    _globals['_DEVICEMANAGEMENTLEVEL']._serialized_end = 444