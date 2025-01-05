"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1/schema.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/discoveryengine/v1/schema.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto"\xd9\x02\n\x06Schema\x120\n\rstruct_schema\x18\x02 \x01(\x0b2\x17.google.protobuf.StructH\x00\x12\x15\n\x0bjson_schema\x18\x03 \x01(\tH\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05:\xe8\x01\xeaA\xe4\x01\n%discoveryengine.googleapis.com/Schema\x12Pprojects/{project}/locations/{location}/dataStores/{data_store}/schemas/{schema}\x12iprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/schemas/{schema}B\x08\n\x06schemaB\xfe\x01\n#com.google.cloud.discoveryengine.v1B\x0bSchemaProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.schema_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x0bSchemaProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_SCHEMA'].fields_by_name['name']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_SCHEMA']._loaded_options = None
    _globals['_SCHEMA']._serialized_options = b'\xeaA\xe4\x01\n%discoveryengine.googleapis.com/Schema\x12Pprojects/{project}/locations/{location}/dataStores/{data_store}/schemas/{schema}\x12iprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/schemas/{schema}'
    _globals['_SCHEMA']._serialized_start = 172
    _globals['_SCHEMA']._serialized_end = 517