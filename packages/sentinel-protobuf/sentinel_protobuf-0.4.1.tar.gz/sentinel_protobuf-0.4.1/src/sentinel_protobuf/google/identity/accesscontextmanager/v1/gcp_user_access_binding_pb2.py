"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/identity/accesscontextmanager/v1/gcp_user_access_binding.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/identity/accesscontextmanager/v1/gcp_user_access_binding.proto\x12\'google.identity.accesscontextmanager.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa3\x02\n\x14GcpUserAccessBinding\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x19\n\tgroup_key\x18\x02 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12N\n\raccess_levels\x18\x03 \x03(\tB7\xe0A\x02\xfaA1\n/accesscontextmanager.googleapis.com/AccessLevel:\x8c\x01\xeaA\x88\x01\n8accesscontextmanager.googleapis.com/GcpUserAccessBinding\x12Lorganizations/{organization}/gcpUserAccessBindings/{gcp_user_access_binding}B\xb0\x02\n+com.google.identity.accesscontextmanager.v1B\x19GcpUserAccessBindingProtoP\x01Z\\cloud.google.com/go/accesscontextmanager/apiv1/accesscontextmanagerpb;accesscontextmanagerpb\xa2\x02\x04GACM\xaa\x02\'Google.Identity.AccessContextManager.V1\xca\x02\'Google\\Identity\\AccessContextManager\\V1\xea\x02*Google::Identity::AccessContextManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.identity.accesscontextmanager.v1.gcp_user_access_binding_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.identity.accesscontextmanager.v1B\x19GcpUserAccessBindingProtoP\x01Z\\cloud.google.com/go/accesscontextmanager/apiv1/accesscontextmanagerpb;accesscontextmanagerpb\xa2\x02\x04GACM\xaa\x02'Google.Identity.AccessContextManager.V1\xca\x02'Google\\Identity\\AccessContextManager\\V1\xea\x02*Google::Identity::AccessContextManager::V1"
    _globals['_GCPUSERACCESSBINDING'].fields_by_name['name']._loaded_options = None
    _globals['_GCPUSERACCESSBINDING'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_GCPUSERACCESSBINDING'].fields_by_name['group_key']._loaded_options = None
    _globals['_GCPUSERACCESSBINDING'].fields_by_name['group_key']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_GCPUSERACCESSBINDING'].fields_by_name['access_levels']._loaded_options = None
    _globals['_GCPUSERACCESSBINDING'].fields_by_name['access_levels']._serialized_options = b'\xe0A\x02\xfaA1\n/accesscontextmanager.googleapis.com/AccessLevel'
    _globals['_GCPUSERACCESSBINDING']._loaded_options = None
    _globals['_GCPUSERACCESSBINDING']._serialized_options = b'\xeaA\x88\x01\n8accesscontextmanager.googleapis.com/GcpUserAccessBinding\x12Lorganizations/{organization}/gcpUserAccessBindings/{gcp_user_access_binding}'
    _globals['_GCPUSERACCESSBINDING']._serialized_start = 175
    _globals['_GCPUSERACCESSBINDING']._serialized_end = 466