"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3/safety_settings.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/dialogflow/cx/v3/safety_settings.proto\x12\x1dgoogle.cloud.dialogflow.cx.v3\x1a\x1fgoogle/api/field_behavior.proto"\x97\x01\n\x0eSafetySettings\x12L\n\x0ebanned_phrases\x18\x01 \x03(\x0b24.google.cloud.dialogflow.cx.v3.SafetySettings.Phrase\x1a7\n\x06Phrase\x12\x11\n\x04text\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rlanguage_code\x18\x02 \x01(\tB\x03\xe0A\x02B\xb6\x01\n!com.google.cloud.dialogflow.cx.v3B\x13SafetySettingsProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3.safety_settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.dialogflow.cx.v3B\x13SafetySettingsProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3'
    _globals['_SAFETYSETTINGS_PHRASE'].fields_by_name['text']._loaded_options = None
    _globals['_SAFETYSETTINGS_PHRASE'].fields_by_name['text']._serialized_options = b'\xe0A\x02'
    _globals['_SAFETYSETTINGS_PHRASE'].fields_by_name['language_code']._loaded_options = None
    _globals['_SAFETYSETTINGS_PHRASE'].fields_by_name['language_code']._serialized_options = b'\xe0A\x02'
    _globals['_SAFETYSETTINGS']._serialized_start = 120
    _globals['_SAFETYSETTINGS']._serialized_end = 271
    _globals['_SAFETYSETTINGS_PHRASE']._serialized_start = 216
    _globals['_SAFETYSETTINGS_PHRASE']._serialized_end = 271