"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3/advanced_settings.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.cloud.dialogflow.cx.v3 import gcs_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_gcs__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/dialogflow/cx/v3/advanced_settings.proto\x12\x1dgoogle.cloud.dialogflow.cx.v3\x1a\x1fgoogle/api/field_behavior.proto\x1a\'google/cloud/dialogflow/cx/v3/gcs.proto\x1a\x1egoogle/protobuf/duration.proto"\xdc\x07\n\x10AdvancedSettings\x12S\n\x1caudio_export_gcs_destination\x18\x02 \x01(\x0b2-.google.cloud.dialogflow.cx.v3.GcsDestination\x12W\n\x0fspeech_settings\x18\x03 \x01(\x0b2>.google.cloud.dialogflow.cx.v3.AdvancedSettings.SpeechSettings\x12S\n\rdtmf_settings\x18\x05 \x01(\x0b2<.google.cloud.dialogflow.cx.v3.AdvancedSettings.DtmfSettings\x12Y\n\x10logging_settings\x18\x06 \x01(\x0b2?.google.cloud.dialogflow.cx.v3.AdvancedSettings.LoggingSettings\x1a\x98\x02\n\x0eSpeechSettings\x12\x1e\n\x16endpointer_sensitivity\x18\x01 \x01(\x05\x124\n\x11no_speech_timeout\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x12%\n\x1duse_timeout_based_endpointing\x18\x03 \x01(\x08\x12Z\n\x06models\x18\x05 \x03(\x0b2J.google.cloud.dialogflow.cx.v3.AdvancedSettings.SpeechSettings.ModelsEntry\x1a-\n\x0bModelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a\xca\x01\n\x0cDtmfSettings\x12\x0f\n\x07enabled\x18\x01 \x01(\x08\x12\x12\n\nmax_digits\x18\x02 \x01(\x05\x12\x14\n\x0cfinish_digit\x18\x03 \x01(\t\x12>\n\x1binterdigit_timeout_duration\x18\x06 \x01(\x0b2\x19.google.protobuf.Duration\x12?\n\x1cendpointing_timeout_duration\x18\x07 \x01(\x0b2\x19.google.protobuf.Duration\x1a\x81\x01\n\x0fLoggingSettings\x12"\n\x1aenable_stackdriver_logging\x18\x02 \x01(\x08\x12"\n\x1aenable_interaction_logging\x18\x03 \x01(\x08\x12&\n\x1eenable_consent_based_redaction\x18\x04 \x01(\x08B\xb8\x01\n!com.google.cloud.dialogflow.cx.v3B\x15AdvancedSettingsProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3.advanced_settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.dialogflow.cx.v3B\x15AdvancedSettingsProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3'
    _globals['_ADVANCEDSETTINGS_SPEECHSETTINGS_MODELSENTRY']._loaded_options = None
    _globals['_ADVANCEDSETTINGS_SPEECHSETTINGS_MODELSENTRY']._serialized_options = b'8\x01'
    _globals['_ADVANCEDSETTINGS']._serialized_start = 195
    _globals['_ADVANCEDSETTINGS']._serialized_end = 1183
    _globals['_ADVANCEDSETTINGS_SPEECHSETTINGS']._serialized_start = 566
    _globals['_ADVANCEDSETTINGS_SPEECHSETTINGS']._serialized_end = 846
    _globals['_ADVANCEDSETTINGS_SPEECHSETTINGS_MODELSENTRY']._serialized_start = 801
    _globals['_ADVANCEDSETTINGS_SPEECHSETTINGS_MODELSENTRY']._serialized_end = 846
    _globals['_ADVANCEDSETTINGS_DTMFSETTINGS']._serialized_start = 849
    _globals['_ADVANCEDSETTINGS_DTMFSETTINGS']._serialized_end = 1051
    _globals['_ADVANCEDSETTINGS_LOGGINGSETTINGS']._serialized_start = 1054
    _globals['_ADVANCEDSETTINGS_LOGGINGSETTINGS']._serialized_end = 1183