"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3beta1/tool_call.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/dialogflow/cx/v3beta1/tool_call.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto"\x8d\x01\n\x08ToolCall\x124\n\x04tool\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Tool\x12\x13\n\x06action\x18\x02 \x01(\tB\x03\xe0A\x02\x126\n\x10input_parameters\x18\x03 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01"\x85\x02\n\x0eToolCallResult\x124\n\x04tool\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Tool\x12\x13\n\x06action\x18\x02 \x01(\tB\x03\xe0A\x02\x12I\n\x05error\x18\x03 \x01(\x0b28.google.cloud.dialogflow.cx.v3beta1.ToolCallResult.ErrorH\x00\x124\n\x11output_parameters\x18\x04 \x01(\x0b2\x17.google.protobuf.StructH\x00\x1a\x1d\n\x05Error\x12\x14\n\x07message\x18\x01 \x01(\tB\x03\xe0A\x01B\x08\n\x06resultB\xc7\x01\n&com.google.cloud.dialogflow.cx.v3beta1B\rToolCallProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.tool_call_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\rToolCallProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1'
    _globals['_TOOLCALL'].fields_by_name['tool']._loaded_options = None
    _globals['_TOOLCALL'].fields_by_name['tool']._serialized_options = b'\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Tool'
    _globals['_TOOLCALL'].fields_by_name['action']._loaded_options = None
    _globals['_TOOLCALL'].fields_by_name['action']._serialized_options = b'\xe0A\x02'
    _globals['_TOOLCALL'].fields_by_name['input_parameters']._loaded_options = None
    _globals['_TOOLCALL'].fields_by_name['input_parameters']._serialized_options = b'\xe0A\x01'
    _globals['_TOOLCALLRESULT_ERROR'].fields_by_name['message']._loaded_options = None
    _globals['_TOOLCALLRESULT_ERROR'].fields_by_name['message']._serialized_options = b'\xe0A\x01'
    _globals['_TOOLCALLRESULT'].fields_by_name['tool']._loaded_options = None
    _globals['_TOOLCALLRESULT'].fields_by_name['tool']._serialized_options = b'\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Tool'
    _globals['_TOOLCALLRESULT'].fields_by_name['action']._loaded_options = None
    _globals['_TOOLCALLRESULT'].fields_by_name['action']._serialized_options = b'\xe0A\x02'
    _globals['_TOOLCALL']._serialized_start = 236
    _globals['_TOOLCALL']._serialized_end = 377
    _globals['_TOOLCALLRESULT']._serialized_start = 380
    _globals['_TOOLCALLRESULT']._serialized_end = 641
    _globals['_TOOLCALLRESULT_ERROR']._serialized_start = 602
    _globals['_TOOLCALLRESULT_ERROR']._serialized_end = 631