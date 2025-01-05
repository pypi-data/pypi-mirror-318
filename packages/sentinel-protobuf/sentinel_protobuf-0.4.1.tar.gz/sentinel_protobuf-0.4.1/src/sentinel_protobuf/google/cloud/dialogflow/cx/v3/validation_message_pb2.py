"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3/validation_message.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/dialogflow/cx/v3/validation_message.proto\x12\x1dgoogle.cloud.dialogflow.cx.v3"\x9a\x05\n\x11ValidationMessage\x12T\n\rresource_type\x18\x01 \x01(\x0e2=.google.cloud.dialogflow.cx.v3.ValidationMessage.ResourceType\x12\x15\n\tresources\x18\x02 \x03(\tB\x02\x18\x01\x12C\n\x0eresource_names\x18\x06 \x03(\x0b2+.google.cloud.dialogflow.cx.v3.ResourceName\x12K\n\x08severity\x18\x03 \x01(\x0e29.google.cloud.dialogflow.cx.v3.ValidationMessage.Severity\x12\x0e\n\x06detail\x18\x04 \x01(\t"\xad\x02\n\x0cResourceType\x12\x1d\n\x19RESOURCE_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05AGENT\x10\x01\x12\n\n\x06INTENT\x10\x02\x12\x1a\n\x16INTENT_TRAINING_PHRASE\x10\x08\x12\x14\n\x10INTENT_PARAMETER\x10\t\x12\x0b\n\x07INTENTS\x10\n\x12\x1b\n\x17INTENT_TRAINING_PHRASES\x10\x0b\x12\x0f\n\x0bENTITY_TYPE\x10\x03\x12\x10\n\x0cENTITY_TYPES\x10\x0c\x12\x0b\n\x07WEBHOOK\x10\x04\x12\x08\n\x04FLOW\x10\x05\x12\x08\n\x04PAGE\x10\x06\x12\t\n\x05PAGES\x10\r\x12\x1a\n\x16TRANSITION_ROUTE_GROUP\x10\x07\x12 \n\x1cAGENT_TRANSITION_ROUTE_GROUP\x10\x0e"F\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x08\n\x04INFO\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\t\n\x05ERROR\x10\x03"2\n\x0cResourceName\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\tB\xb9\x01\n!com.google.cloud.dialogflow.cx.v3B\x16ValidationMessageProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3.validation_message_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.dialogflow.cx.v3B\x16ValidationMessageProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3'
    _globals['_VALIDATIONMESSAGE'].fields_by_name['resources']._loaded_options = None
    _globals['_VALIDATIONMESSAGE'].fields_by_name['resources']._serialized_options = b'\x18\x01'
    _globals['_VALIDATIONMESSAGE']._serialized_start = 90
    _globals['_VALIDATIONMESSAGE']._serialized_end = 756
    _globals['_VALIDATIONMESSAGE_RESOURCETYPE']._serialized_start = 383
    _globals['_VALIDATIONMESSAGE_RESOURCETYPE']._serialized_end = 684
    _globals['_VALIDATIONMESSAGE_SEVERITY']._serialized_start = 686
    _globals['_VALIDATIONMESSAGE_SEVERITY']._serialized_end = 756
    _globals['_RESOURCENAME']._serialized_start = 758
    _globals['_RESOURCENAME']._serialized_end = 808