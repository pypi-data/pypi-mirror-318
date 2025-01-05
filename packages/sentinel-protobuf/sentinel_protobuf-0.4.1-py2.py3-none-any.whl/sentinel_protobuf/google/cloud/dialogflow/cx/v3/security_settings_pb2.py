"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3/security_settings.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/dialogflow/cx/v3/security_settings.proto\x12\x1dgoogle.cloud.dialogflow.cx.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"^\n\x1aGetSecuritySettingsRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*dialogflow.googleapis.com/SecuritySettings"\xa6\x01\n\x1dUpdateSecuritySettingsRequest\x12O\n\x11security_settings\x18\x01 \x01(\x0b2/.google.cloud.dialogflow.cx.v3.SecuritySettingsB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\x88\x01\n\x1bListSecuritySettingsRequest\x12B\n\x06parent\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\x12*dialogflow.googleapis.com/SecuritySettings\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x83\x01\n\x1cListSecuritySettingsResponse\x12J\n\x11security_settings\x18\x01 \x03(\x0b2/.google.cloud.dialogflow.cx.v3.SecuritySettings\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xb4\x01\n\x1dCreateSecuritySettingsRequest\x12B\n\x06parent\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\x12*dialogflow.googleapis.com/SecuritySettings\x12O\n\x11security_settings\x18\x02 \x01(\x0b2/.google.cloud.dialogflow.cx.v3.SecuritySettingsB\x03\xe0A\x02"a\n\x1dDeleteSecuritySettingsRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*dialogflow.googleapis.com/SecuritySettings"\xe7\x0c\n\x10SecuritySettings\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12]\n\x12redaction_strategy\x18\x03 \x01(\x0e2A.google.cloud.dialogflow.cx.v3.SecuritySettings.RedactionStrategy\x12W\n\x0fredaction_scope\x18\x04 \x01(\x0e2>.google.cloud.dialogflow.cx.v3.SecuritySettings.RedactionScope\x12A\n\x10inspect_template\x18\t \x01(\tB\'\xfaA$\n"dlp.googleapis.com/InspectTemplate\x12G\n\x13deidentify_template\x18\x11 \x01(\tB*\xfaA\'\n%dlp.googleapis.com/DeidentifyTemplate\x12\x1f\n\x15retention_window_days\x18\x06 \x01(\x05H\x00\x12_\n\x12retention_strategy\x18\x07 \x01(\x0e2A.google.cloud.dialogflow.cx.v3.SecuritySettings.RetentionStrategyH\x00\x12W\n\x10purge_data_types\x18\x08 \x03(\x0e2=.google.cloud.dialogflow.cx.v3.SecuritySettings.PurgeDataType\x12b\n\x15audio_export_settings\x18\x0c \x01(\x0b2C.google.cloud.dialogflow.cx.v3.SecuritySettings.AudioExportSettings\x12h\n\x18insights_export_settings\x18\r \x01(\x0b2F.google.cloud.dialogflow.cx.v3.SecuritySettings.InsightsExportSettings\x1a\xb1\x02\n\x13AudioExportSettings\x12\x12\n\ngcs_bucket\x18\x01 \x01(\t\x12\x1c\n\x14audio_export_pattern\x18\x02 \x01(\t\x12\x1e\n\x16enable_audio_redaction\x18\x03 \x01(\x08\x12e\n\x0caudio_format\x18\x04 \x01(\x0e2O.google.cloud.dialogflow.cx.v3.SecuritySettings.AudioExportSettings.AudioFormat\x12\x17\n\x0fstore_tts_audio\x18\x06 \x01(\x08"H\n\x0bAudioFormat\x12\x1c\n\x18AUDIO_FORMAT_UNSPECIFIED\x10\x00\x12\t\n\x05MULAW\x10\x01\x12\x07\n\x03MP3\x10\x02\x12\x07\n\x03OGG\x10\x03\x1a8\n\x16InsightsExportSettings\x12\x1e\n\x16enable_insights_export\x18\x01 \x01(\x08"P\n\x11RedactionStrategy\x12"\n\x1eREDACTION_STRATEGY_UNSPECIFIED\x10\x00\x12\x17\n\x13REDACT_WITH_SERVICE\x10\x01"J\n\x0eRedactionScope\x12\x1f\n\x1bREDACTION_SCOPE_UNSPECIFIED\x10\x00\x12\x17\n\x13REDACT_DISK_STORAGE\x10\x02"V\n\x11RetentionStrategy\x12"\n\x1eRETENTION_STRATEGY_UNSPECIFIED\x10\x00\x12\x1d\n\x19REMOVE_AFTER_CONVERSATION\x10\x01"H\n\rPurgeDataType\x12\x1f\n\x1bPURGE_DATA_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12DIALOGFLOW_HISTORY\x10\x01:}\xeaAz\n*dialogflow.googleapis.com/SecuritySettings\x12Lprojects/{project}/locations/{location}/securitySettings/{security_settings}B\x10\n\x0edata_retention2\xef\t\n\x17SecuritySettingsService\x12\xf3\x01\n\x16CreateSecuritySettings\x12<.google.cloud.dialogflow.cx.v3.CreateSecuritySettingsRequest\x1a/.google.cloud.dialogflow.cx.v3.SecuritySettings"j\xdaA\x18parent,security_settings\x82\xd3\xe4\x93\x02I"4/v3/{parent=projects/*/locations/*}/securitySettings:\x11security_settings\x12\xc6\x01\n\x13GetSecuritySettings\x129.google.cloud.dialogflow.cx.v3.GetSecuritySettingsRequest\x1a/.google.cloud.dialogflow.cx.v3.SecuritySettings"C\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v3/{name=projects/*/locations/*/securitySettings/*}\x12\x8b\x02\n\x16UpdateSecuritySettings\x12<.google.cloud.dialogflow.cx.v3.UpdateSecuritySettingsRequest\x1a/.google.cloud.dialogflow.cx.v3.SecuritySettings"\x81\x01\xdaA\x1dsecurity_settings,update_mask\x82\xd3\xe4\x93\x02[2F/v3/{security_settings.name=projects/*/locations/*/securitySettings/*}:\x11security_settings\x12\xd6\x01\n\x14ListSecuritySettings\x12:.google.cloud.dialogflow.cx.v3.ListSecuritySettingsRequest\x1a;.google.cloud.dialogflow.cx.v3.ListSecuritySettingsResponse"E\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v3/{parent=projects/*/locations/*}/securitySettings\x12\xb3\x01\n\x16DeleteSecuritySettings\x12<.google.cloud.dialogflow.cx.v3.DeleteSecuritySettingsRequest\x1a\x16.google.protobuf.Empty"C\xdaA\x04name\x82\xd3\xe4\x93\x026*4/v3/{name=projects/*/locations/*/securitySettings/*}\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xe2\x04\n!com.google.cloud.dialogflow.cx.v3B\x15SecuritySettingsProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3\xeaA\xc8\x01\n"dlp.googleapis.com/InspectTemplate\x12Uorganizations/{organization}/locations/{location}/inspectTemplates/{inspect_template}\x12Kprojects/{project}/locations/{location}/inspectTemplates/{inspect_template}\xeaA\xd7\x01\n%dlp.googleapis.com/DeidentifyTemplate\x12[organizations/{organization}/locations/{location}/deidentifyTemplates/{deidentify_template}\x12Qprojects/{project}/locations/{location}/deidentifyTemplates/{deidentify_template}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3.security_settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.dialogflow.cx.v3B\x15SecuritySettingsProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3\xeaA\xc8\x01\n"dlp.googleapis.com/InspectTemplate\x12Uorganizations/{organization}/locations/{location}/inspectTemplates/{inspect_template}\x12Kprojects/{project}/locations/{location}/inspectTemplates/{inspect_template}\xeaA\xd7\x01\n%dlp.googleapis.com/DeidentifyTemplate\x12[organizations/{organization}/locations/{location}/deidentifyTemplates/{deidentify_template}\x12Qprojects/{project}/locations/{location}/deidentifyTemplates/{deidentify_template}'
    _globals['_GETSECURITYSETTINGSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSECURITYSETTINGSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*dialogflow.googleapis.com/SecuritySettings'
    _globals['_UPDATESECURITYSETTINGSREQUEST'].fields_by_name['security_settings']._loaded_options = None
    _globals['_UPDATESECURITYSETTINGSREQUEST'].fields_by_name['security_settings']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESECURITYSETTINGSREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESECURITYSETTINGSREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_LISTSECURITYSETTINGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSECURITYSETTINGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA,\x12*dialogflow.googleapis.com/SecuritySettings'
    _globals['_CREATESECURITYSETTINGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESECURITYSETTINGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA,\x12*dialogflow.googleapis.com/SecuritySettings'
    _globals['_CREATESECURITYSETTINGSREQUEST'].fields_by_name['security_settings']._loaded_options = None
    _globals['_CREATESECURITYSETTINGSREQUEST'].fields_by_name['security_settings']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESECURITYSETTINGSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESECURITYSETTINGSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*dialogflow.googleapis.com/SecuritySettings'
    _globals['_SECURITYSETTINGS'].fields_by_name['display_name']._loaded_options = None
    _globals['_SECURITYSETTINGS'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_SECURITYSETTINGS'].fields_by_name['inspect_template']._loaded_options = None
    _globals['_SECURITYSETTINGS'].fields_by_name['inspect_template']._serialized_options = b'\xfaA$\n"dlp.googleapis.com/InspectTemplate'
    _globals['_SECURITYSETTINGS'].fields_by_name['deidentify_template']._loaded_options = None
    _globals['_SECURITYSETTINGS'].fields_by_name['deidentify_template']._serialized_options = b"\xfaA'\n%dlp.googleapis.com/DeidentifyTemplate"
    _globals['_SECURITYSETTINGS']._loaded_options = None
    _globals['_SECURITYSETTINGS']._serialized_options = b'\xeaAz\n*dialogflow.googleapis.com/SecuritySettings\x12Lprojects/{project}/locations/{location}/securitySettings/{security_settings}'
    _globals['_SECURITYSETTINGSSERVICE']._loaded_options = None
    _globals['_SECURITYSETTINGSSERVICE']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_SECURITYSETTINGSSERVICE'].methods_by_name['CreateSecuritySettings']._loaded_options = None
    _globals['_SECURITYSETTINGSSERVICE'].methods_by_name['CreateSecuritySettings']._serialized_options = b'\xdaA\x18parent,security_settings\x82\xd3\xe4\x93\x02I"4/v3/{parent=projects/*/locations/*}/securitySettings:\x11security_settings'
    _globals['_SECURITYSETTINGSSERVICE'].methods_by_name['GetSecuritySettings']._loaded_options = None
    _globals['_SECURITYSETTINGSSERVICE'].methods_by_name['GetSecuritySettings']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v3/{name=projects/*/locations/*/securitySettings/*}'
    _globals['_SECURITYSETTINGSSERVICE'].methods_by_name['UpdateSecuritySettings']._loaded_options = None
    _globals['_SECURITYSETTINGSSERVICE'].methods_by_name['UpdateSecuritySettings']._serialized_options = b'\xdaA\x1dsecurity_settings,update_mask\x82\xd3\xe4\x93\x02[2F/v3/{security_settings.name=projects/*/locations/*/securitySettings/*}:\x11security_settings'
    _globals['_SECURITYSETTINGSSERVICE'].methods_by_name['ListSecuritySettings']._loaded_options = None
    _globals['_SECURITYSETTINGSSERVICE'].methods_by_name['ListSecuritySettings']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v3/{parent=projects/*/locations/*}/securitySettings'
    _globals['_SECURITYSETTINGSSERVICE'].methods_by_name['DeleteSecuritySettings']._loaded_options = None
    _globals['_SECURITYSETTINGSSERVICE'].methods_by_name['DeleteSecuritySettings']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026*4/v3/{name=projects/*/locations/*/securitySettings/*}'
    _globals['_GETSECURITYSETTINGSREQUEST']._serialized_start = 266
    _globals['_GETSECURITYSETTINGSREQUEST']._serialized_end = 360
    _globals['_UPDATESECURITYSETTINGSREQUEST']._serialized_start = 363
    _globals['_UPDATESECURITYSETTINGSREQUEST']._serialized_end = 529
    _globals['_LISTSECURITYSETTINGSREQUEST']._serialized_start = 532
    _globals['_LISTSECURITYSETTINGSREQUEST']._serialized_end = 668
    _globals['_LISTSECURITYSETTINGSRESPONSE']._serialized_start = 671
    _globals['_LISTSECURITYSETTINGSRESPONSE']._serialized_end = 802
    _globals['_CREATESECURITYSETTINGSREQUEST']._serialized_start = 805
    _globals['_CREATESECURITYSETTINGSREQUEST']._serialized_end = 985
    _globals['_DELETESECURITYSETTINGSREQUEST']._serialized_start = 987
    _globals['_DELETESECURITYSETTINGSREQUEST']._serialized_end = 1084
    _globals['_SECURITYSETTINGS']._serialized_start = 1087
    _globals['_SECURITYSETTINGS']._serialized_end = 2726
    _globals['_SECURITYSETTINGS_AUDIOEXPORTSETTINGS']._serialized_start = 1898
    _globals['_SECURITYSETTINGS_AUDIOEXPORTSETTINGS']._serialized_end = 2203
    _globals['_SECURITYSETTINGS_AUDIOEXPORTSETTINGS_AUDIOFORMAT']._serialized_start = 2131
    _globals['_SECURITYSETTINGS_AUDIOEXPORTSETTINGS_AUDIOFORMAT']._serialized_end = 2203
    _globals['_SECURITYSETTINGS_INSIGHTSEXPORTSETTINGS']._serialized_start = 2205
    _globals['_SECURITYSETTINGS_INSIGHTSEXPORTSETTINGS']._serialized_end = 2261
    _globals['_SECURITYSETTINGS_REDACTIONSTRATEGY']._serialized_start = 2263
    _globals['_SECURITYSETTINGS_REDACTIONSTRATEGY']._serialized_end = 2343
    _globals['_SECURITYSETTINGS_REDACTIONSCOPE']._serialized_start = 2345
    _globals['_SECURITYSETTINGS_REDACTIONSCOPE']._serialized_end = 2419
    _globals['_SECURITYSETTINGS_RETENTIONSTRATEGY']._serialized_start = 2421
    _globals['_SECURITYSETTINGS_RETENTIONSTRATEGY']._serialized_end = 2507
    _globals['_SECURITYSETTINGS_PURGEDATATYPE']._serialized_start = 2509
    _globals['_SECURITYSETTINGS_PURGEDATATYPE']._serialized_end = 2581
    _globals['_SECURITYSETTINGSSERVICE']._serialized_start = 2729
    _globals['_SECURITYSETTINGSSERVICE']._serialized_end = 3992