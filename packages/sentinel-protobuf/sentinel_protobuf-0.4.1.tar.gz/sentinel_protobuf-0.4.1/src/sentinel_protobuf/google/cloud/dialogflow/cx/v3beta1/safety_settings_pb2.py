"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3beta1/safety_settings.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/dialogflow/cx/v3beta1/safety_settings.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x1fgoogle/api/field_behavior.proto"\xf8\x02\n\x0eSafetySettings\x12y\n$default_banned_phrase_match_strategy\x18\x04 \x01(\x0e2F.google.cloud.dialogflow.cx.v3beta1.SafetySettings.PhraseMatchStrategyB\x03\xe0A\x01\x12Q\n\x0ebanned_phrases\x18\x01 \x03(\x0b29.google.cloud.dialogflow.cx.v3beta1.SafetySettings.Phrase\x1a7\n\x06Phrase\x12\x11\n\x04text\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rlanguage_code\x18\x02 \x01(\tB\x03\xe0A\x02"_\n\x13PhraseMatchStrategy\x12%\n!PHRASE_MATCH_STRATEGY_UNSPECIFIED\x10\x00\x12\x11\n\rPARTIAL_MATCH\x10\x01\x12\x0e\n\nWORD_MATCH\x10\x02B\xca\x01\n&com.google.cloud.dialogflow.cx.v3beta1B\x13SafetySettingsProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.safety_settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\x13SafetySettingsProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1'
    _globals['_SAFETYSETTINGS_PHRASE'].fields_by_name['text']._loaded_options = None
    _globals['_SAFETYSETTINGS_PHRASE'].fields_by_name['text']._serialized_options = b'\xe0A\x02'
    _globals['_SAFETYSETTINGS_PHRASE'].fields_by_name['language_code']._loaded_options = None
    _globals['_SAFETYSETTINGS_PHRASE'].fields_by_name['language_code']._serialized_options = b'\xe0A\x02'
    _globals['_SAFETYSETTINGS'].fields_by_name['default_banned_phrase_match_strategy']._loaded_options = None
    _globals['_SAFETYSETTINGS'].fields_by_name['default_banned_phrase_match_strategy']._serialized_options = b'\xe0A\x01'
    _globals['_SAFETYSETTINGS']._serialized_start = 130
    _globals['_SAFETYSETTINGS']._serialized_end = 506
    _globals['_SAFETYSETTINGS_PHRASE']._serialized_start = 354
    _globals['_SAFETYSETTINGS_PHRASE']._serialized_end = 409
    _globals['_SAFETYSETTINGS_PHRASEMATCHSTRATEGY']._serialized_start = 411
    _globals['_SAFETYSETTINGS_PHRASEMATCHSTRATEGY']._serialized_end = 506