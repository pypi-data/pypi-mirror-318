"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3beta1/inline.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/dialogflow/cx/v3beta1/inline.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x1fgoogle/api/field_behavior.proto")\n\x11InlineDestination\x12\x14\n\x07content\x18\x01 \x01(\x0cB\x03\xe0A\x03"\x1f\n\x0cInlineSource\x12\x0f\n\x07content\x18\x01 \x01(\x0cB\xc2\x01\n&com.google.cloud.dialogflow.cx.v3beta1B\x0bInlineProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.inline_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\x0bInlineProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1'
    _globals['_INLINEDESTINATION'].fields_by_name['content']._loaded_options = None
    _globals['_INLINEDESTINATION'].fields_by_name['content']._serialized_options = b'\xe0A\x03'
    _globals['_INLINEDESTINATION']._serialized_start = 120
    _globals['_INLINEDESTINATION']._serialized_end = 161
    _globals['_INLINESOURCE']._serialized_start = 163
    _globals['_INLINESOURCE']._serialized_end = 194