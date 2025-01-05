"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/release_channel.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/actions/sdk/v2/release_channel.proto\x12\x15google.actions.sdk.v2\x1a\x19google/api/resource.proto"\xb2\x01\n\x0eReleaseChannel\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0fcurrent_version\x18\x02 \x01(\t\x12\x17\n\x0fpending_version\x18\x03 \x01(\t:`\xeaA]\n%actions.googleapis.com/ReleaseChannel\x124projects/{project}/releaseChannels/{release_channel}Bl\n\x19com.google.actions.sdk.v2B\x13ReleaseChannelProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdkb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.release_channel_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.actions.sdk.v2B\x13ReleaseChannelProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdk'
    _globals['_RELEASECHANNEL']._loaded_options = None
    _globals['_RELEASECHANNEL']._serialized_options = b'\xeaA]\n%actions.googleapis.com/ReleaseChannel\x124projects/{project}/releaseChannels/{release_channel}'
    _globals['_RELEASECHANNEL']._serialized_start = 98
    _globals['_RELEASECHANNEL']._serialized_end = 276