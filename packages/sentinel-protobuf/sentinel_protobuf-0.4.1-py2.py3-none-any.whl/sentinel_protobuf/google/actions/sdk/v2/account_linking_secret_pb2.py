"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/account_linking_secret.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/actions/sdk/v2/account_linking_secret.proto\x12\x15google.actions.sdk.v2"W\n\x14AccountLinkingSecret\x12\x1f\n\x17encrypted_client_secret\x18\x01 \x01(\x0c\x12\x1e\n\x16encryption_key_version\x18\x02 \x01(\tBr\n\x19com.google.actions.sdk.v2B\x19AccountLinkingSecretProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdkb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.account_linking_secret_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.actions.sdk.v2B\x19AccountLinkingSecretProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdk'
    _globals['_ACCOUNTLINKINGSECRET']._serialized_start = 77
    _globals['_ACCOUNTLINKINGSECRET']._serialized_end = 164