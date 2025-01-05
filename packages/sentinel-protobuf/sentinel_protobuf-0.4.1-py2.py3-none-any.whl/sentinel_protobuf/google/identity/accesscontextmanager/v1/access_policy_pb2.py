"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/identity/accesscontextmanager/v1/access_policy.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/identity/accesscontextmanager/v1/access_policy.proto\x12\'google.identity.accesscontextmanager.v1\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x92\x02\n\x0cAccessPolicy\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06parent\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0e\n\x06scopes\x18\x07 \x03(\t\x12/\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0c\n\x04etag\x18\x06 \x01(\t:U\xeaAR\n0accesscontextmanager.googleapis.com/AccessPolicy\x12\x1eaccessPolicies/{access_policy}B\xa2\x02\n+com.google.identity.accesscontextmanager.v1B\x0bPolicyProtoP\x01Z\\cloud.google.com/go/accesscontextmanager/apiv1/accesscontextmanagerpb;accesscontextmanagerpb\xa2\x02\x04GACM\xaa\x02\'Google.Identity.AccessContextManager.V1\xca\x02\'Google\\Identity\\AccessContextManager\\V1\xea\x02*Google::Identity::AccessContextManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.identity.accesscontextmanager.v1.access_policy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.identity.accesscontextmanager.v1B\x0bPolicyProtoP\x01Z\\cloud.google.com/go/accesscontextmanager/apiv1/accesscontextmanagerpb;accesscontextmanagerpb\xa2\x02\x04GACM\xaa\x02'Google.Identity.AccessContextManager.V1\xca\x02'Google\\Identity\\AccessContextManager\\V1\xea\x02*Google::Identity::AccessContextManager::V1"
    _globals['_ACCESSPOLICY']._loaded_options = None
    _globals['_ACCESSPOLICY']._serialized_options = b'\xeaAR\n0accesscontextmanager.googleapis.com/AccessPolicy\x12\x1eaccessPolicies/{access_policy}'
    _globals['_ACCESSPOLICY']._serialized_start = 165
    _globals['_ACCESSPOLICY']._serialized_end = 439