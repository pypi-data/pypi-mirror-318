"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3beta1/fulfillment.proto')
_sym_db = _symbol_database.Default()
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import advanced_settings_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_advanced__settings__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import response_message_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_response__message__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/dialogflow/cx/v3beta1/fulfillment.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x19google/api/resource.proto\x1a:google/cloud/dialogflow/cx/v3beta1/advanced_settings.proto\x1a9google/cloud/dialogflow/cx/v3beta1/response_message.proto\x1a\x1cgoogle/protobuf/struct.proto"\xfb\x07\n\x0bFulfillment\x12E\n\x08messages\x18\x01 \x03(\x0b23.google.cloud.dialogflow.cx.v3beta1.ResponseMessage\x127\n\x07webhook\x18\x02 \x01(\tB&\xfaA#\n!dialogflow.googleapis.com/Webhook\x12 \n\x18return_partial_responses\x18\x08 \x01(\x08\x12\x0b\n\x03tag\x18\x03 \x01(\t\x12a\n\x15set_parameter_actions\x18\x04 \x03(\x0b2B.google.cloud.dialogflow.cx.v3beta1.Fulfillment.SetParameterAction\x12[\n\x11conditional_cases\x18\x05 \x03(\x0b2@.google.cloud.dialogflow.cx.v3beta1.Fulfillment.ConditionalCases\x12O\n\x11advanced_settings\x18\x07 \x01(\x0b24.google.cloud.dialogflow.cx.v3beta1.AdvancedSettings\x12"\n\x1aenable_generative_fallback\x18\x0c \x01(\x08\x1aN\n\x12SetParameterAction\x12\x11\n\tparameter\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x1a\xb7\x03\n\x10ConditionalCases\x12T\n\x05cases\x18\x01 \x03(\x0b2E.google.cloud.dialogflow.cx.v3beta1.Fulfillment.ConditionalCases.Case\x1a\xcc\x02\n\x04Case\x12\x11\n\tcondition\x18\x01 \x01(\t\x12g\n\x0ccase_content\x18\x02 \x03(\x0b2Q.google.cloud.dialogflow.cx.v3beta1.Fulfillment.ConditionalCases.Case.CaseContent\x1a\xc7\x01\n\x0bCaseContent\x12F\n\x07message\x18\x01 \x01(\x0b23.google.cloud.dialogflow.cx.v3beta1.ResponseMessageH\x00\x12\\\n\x10additional_cases\x18\x02 \x01(\x0b2@.google.cloud.dialogflow.cx.v3beta1.Fulfillment.ConditionalCasesH\x00B\x12\n\x10cases_or_messageB\xca\x01\n&com.google.cloud.dialogflow.cx.v3beta1B\x10FulfillmentProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.fulfillment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\x10FulfillmentProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1'
    _globals['_FULFILLMENT'].fields_by_name['webhook']._loaded_options = None
    _globals['_FULFILLMENT'].fields_by_name['webhook']._serialized_options = b'\xfaA#\n!dialogflow.googleapis.com/Webhook'
    _globals['_FULFILLMENT']._serialized_start = 269
    _globals['_FULFILLMENT']._serialized_end = 1288
    _globals['_FULFILLMENT_SETPARAMETERACTION']._serialized_start = 768
    _globals['_FULFILLMENT_SETPARAMETERACTION']._serialized_end = 846
    _globals['_FULFILLMENT_CONDITIONALCASES']._serialized_start = 849
    _globals['_FULFILLMENT_CONDITIONALCASES']._serialized_end = 1288
    _globals['_FULFILLMENT_CONDITIONALCASES_CASE']._serialized_start = 956
    _globals['_FULFILLMENT_CONDITIONALCASES_CASE']._serialized_end = 1288
    _globals['_FULFILLMENT_CONDITIONALCASES_CASE_CASECONTENT']._serialized_start = 1089
    _globals['_FULFILLMENT_CONDITIONALCASES_CASE_CASECONTENT']._serialized_end = 1288