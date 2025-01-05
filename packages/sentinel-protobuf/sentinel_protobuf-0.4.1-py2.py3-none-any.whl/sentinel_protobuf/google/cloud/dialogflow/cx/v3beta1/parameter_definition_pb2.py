"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3beta1/parameter_definition.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/dialogflow/cx/v3beta1/parameter_definition.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x1fgoogle/api/field_behavior.proto"\x8d\x02\n\x13ParameterDefinition\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12X\n\x04type\x18\x02 \x01(\x0e2E.google.cloud.dialogflow.cx.v3beta1.ParameterDefinition.ParameterTypeB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x03 \x01(\t"t\n\rParameterType\x12\x1e\n\x1aPARAMETER_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06STRING\x10\x01\x12\n\n\x06NUMBER\x10\x02\x12\x0b\n\x07BOOLEAN\x10\x03\x12\x08\n\x04NULL\x10\x04\x12\n\n\x06OBJECT\x10\x05\x12\x08\n\x04LIST\x10\x06B\xd2\x01\n&com.google.cloud.dialogflow.cx.v3beta1B\x18ParameterDefinitionProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.parameter_definition_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\x18ParameterDefinitionProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1'
    _globals['_PARAMETERDEFINITION'].fields_by_name['name']._loaded_options = None
    _globals['_PARAMETERDEFINITION'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_PARAMETERDEFINITION'].fields_by_name['type']._loaded_options = None
    _globals['_PARAMETERDEFINITION'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_PARAMETERDEFINITION']._serialized_start = 135
    _globals['_PARAMETERDEFINITION']._serialized_end = 404
    _globals['_PARAMETERDEFINITION_PARAMETERTYPE']._serialized_start = 288
    _globals['_PARAMETERDEFINITION_PARAMETERTYPE']._serialized_end = 404