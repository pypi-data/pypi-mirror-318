"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2beta1/environment.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dialogflow.v2beta1 import audio_config_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_audio__config__pb2
from .....google.cloud.dialogflow.v2beta1 import fulfillment_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_fulfillment__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/dialogflow/v2beta1/environment.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a2google/cloud/dialogflow/v2beta1/audio_config.proto\x1a1google/cloud/dialogflow/v2beta1/fulfillment.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x93\x05\n\x0bEnvironment\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01\x12@\n\ragent_version\x18\x03 \x01(\tB)\xe0A\x01\xfaA#\n!dialogflow.googleapis.com/Version\x12F\n\x05state\x18\x04 \x01(\x0e22.google.cloud.dialogflow.v2beta1.Environment.StateB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12[\n\x17text_to_speech_settings\x18\x07 \x01(\x0b25.google.cloud.dialogflow.v2beta1.TextToSpeechSettingsB\x03\xe0A\x01\x12F\n\x0bfulfillment\x18\x08 \x01(\x0b2,.google.cloud.dialogflow.v2beta1.FulfillmentB\x03\xe0A\x01"E\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07STOPPED\x10\x01\x12\x0b\n\x07LOADING\x10\x02\x12\x0b\n\x07RUNNING\x10\x03:\xaa\x01\xeaA\xa6\x01\n%dialogflow.googleapis.com/Environment\x123projects/{project}/agent/environments/{environment}\x12Hprojects/{project}/locations/{location}/agent/environments/{environment}"\xa9\x03\n\x14TextToSpeechSettings\x12"\n\x15enable_text_to_speech\x18\x01 \x01(\x08B\x03\xe0A\x01\x12X\n\x15output_audio_encoding\x18\x02 \x01(\x0e24.google.cloud.dialogflow.v2beta1.OutputAudioEncodingB\x03\xe0A\x02\x12\x1e\n\x11sample_rate_hertz\x18\x03 \x01(\x05B\x03\xe0A\x01\x12z\n\x19synthesize_speech_configs\x18\x04 \x03(\x0b2R.google.cloud.dialogflow.v2beta1.TextToSpeechSettings.SynthesizeSpeechConfigsEntryB\x03\xe0A\x01\x1aw\n\x1cSynthesizeSpeechConfigsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12F\n\x05value\x18\x02 \x01(\x0b27.google.cloud.dialogflow.v2beta1.SynthesizeSpeechConfig:\x028\x01"\x89\x01\n\x17ListEnvironmentsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%dialogflow.googleapis.com/Environment\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"w\n\x18ListEnvironmentsResponse\x12B\n\x0cenvironments\x18\x01 \x03(\x0b2,.google.cloud.dialogflow.v2beta1.Environment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"T\n\x15GetEnvironmentRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/Environment"\xbe\x01\n\x18CreateEnvironmentRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%dialogflow.googleapis.com/Environment\x12F\n\x0benvironment\x18\x02 \x01(\x0b2,.google.cloud.dialogflow.v2beta1.EnvironmentB\x03\xe0A\x02\x12\x1b\n\x0eenvironment_id\x18\x03 \x01(\tB\x03\xe0A\x02"\xce\x01\n\x18UpdateEnvironmentRequest\x12F\n\x0benvironment\x18\x01 \x01(\x0b2,.google.cloud.dialogflow.v2beta1.EnvironmentB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x124\n\'allow_load_to_draft_and_discard_changes\x18\x03 \x01(\x08B\x03\xe0A\x01"W\n\x18DeleteEnvironmentRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/Environment"\x8e\x01\n\x1cGetEnvironmentHistoryRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/Environment\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\xfe\x01\n\x12EnvironmentHistory\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x03\x12O\n\x07entries\x18\x02 \x03(\x0b29.google.cloud.dialogflow.v2beta1.EnvironmentHistory.EntryB\x03\xe0A\x03\x12\x1c\n\x0fnext_page_token\x18\x03 \x01(\tB\x03\xe0A\x03\x1ad\n\x05Entry\x12\x15\n\ragent_version\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12/\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp2\xbf\r\n\x0cEnvironments\x12\x88\x02\n\x10ListEnvironments\x128.google.cloud.dialogflow.v2beta1.ListEnvironmentsRequest\x1a9.google.cloud.dialogflow.v2beta1.ListEnvironmentsResponse"\x7f\xdaA\x06parent\x82\xd3\xe4\x93\x02p\x12//v2beta1/{parent=projects/*/agent}/environmentsZ=\x12;/v2beta1/{parent=projects/*/locations/*/agent}/environments\x12\xee\x01\n\x0eGetEnvironment\x126.google.cloud.dialogflow.v2beta1.GetEnvironmentRequest\x1a,.google.cloud.dialogflow.v2beta1.Environment"v\x82\xd3\xe4\x93\x02p\x12//v2beta1/{name=projects/*/agent/environments/*}Z=\x12;/v2beta1/{name=projects/*/locations/*/agent/environments/*}\x12\x90\x02\n\x11CreateEnvironment\x129.google.cloud.dialogflow.v2beta1.CreateEnvironmentRequest\x1a,.google.cloud.dialogflow.v2beta1.Environment"\x91\x01\x82\xd3\xe4\x93\x02\x8a\x01"//v2beta1/{parent=projects/*/agent}/environments:\x0benvironmentZJ";/v2beta1/{parent=projects/*/locations/*/agent}/environments:\x0benvironment\x12\xa8\x02\n\x11UpdateEnvironment\x129.google.cloud.dialogflow.v2beta1.UpdateEnvironmentRequest\x1a,.google.cloud.dialogflow.v2beta1.Environment"\xa9\x01\x82\xd3\xe4\x93\x02\xa2\x012;/v2beta1/{environment.name=projects/*/agent/environments/*}:\x0benvironmentZV2G/v2beta1/{environment.name=projects/*/locations/*/agent/environments/*}:\x0benvironment\x12\xde\x01\n\x11DeleteEnvironment\x129.google.cloud.dialogflow.v2beta1.DeleteEnvironmentRequest\x1a\x16.google.protobuf.Empty"v\x82\xd3\xe4\x93\x02p*//v2beta1/{name=projects/*/agent/environments/*}Z=*;/v2beta1/{name=projects/*/locations/*/agent/environments/*}\x12\x99\x02\n\x15GetEnvironmentHistory\x12=.google.cloud.dialogflow.v2beta1.GetEnvironmentHistoryRequest\x1a3.google.cloud.dialogflow.v2beta1.EnvironmentHistory"\x8b\x01\x82\xd3\xe4\x93\x02\x84\x01\x129/v2beta1/{parent=projects/*/agent/environments/*}/historyZG\x12E/v2beta1/{parent=projects/*/locations/*/agent/environments/*}/history\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xa8\x01\n#com.google.cloud.dialogflow.v2beta1B\x10EnvironmentProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2beta1.environment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.dialogflow.v2beta1B\x10EnvironmentProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1'
    _globals['_ENVIRONMENT'].fields_by_name['name']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT'].fields_by_name['description']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_ENVIRONMENT'].fields_by_name['agent_version']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['agent_version']._serialized_options = b'\xe0A\x01\xfaA#\n!dialogflow.googleapis.com/Version'
    _globals['_ENVIRONMENT'].fields_by_name['state']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT'].fields_by_name['update_time']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT'].fields_by_name['text_to_speech_settings']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['text_to_speech_settings']._serialized_options = b'\xe0A\x01'
    _globals['_ENVIRONMENT'].fields_by_name['fulfillment']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['fulfillment']._serialized_options = b'\xe0A\x01'
    _globals['_ENVIRONMENT']._loaded_options = None
    _globals['_ENVIRONMENT']._serialized_options = b'\xeaA\xa6\x01\n%dialogflow.googleapis.com/Environment\x123projects/{project}/agent/environments/{environment}\x12Hprojects/{project}/locations/{location}/agent/environments/{environment}'
    _globals['_TEXTTOSPEECHSETTINGS_SYNTHESIZESPEECHCONFIGSENTRY']._loaded_options = None
    _globals['_TEXTTOSPEECHSETTINGS_SYNTHESIZESPEECHCONFIGSENTRY']._serialized_options = b'8\x01'
    _globals['_TEXTTOSPEECHSETTINGS'].fields_by_name['enable_text_to_speech']._loaded_options = None
    _globals['_TEXTTOSPEECHSETTINGS'].fields_by_name['enable_text_to_speech']._serialized_options = b'\xe0A\x01'
    _globals['_TEXTTOSPEECHSETTINGS'].fields_by_name['output_audio_encoding']._loaded_options = None
    _globals['_TEXTTOSPEECHSETTINGS'].fields_by_name['output_audio_encoding']._serialized_options = b'\xe0A\x02'
    _globals['_TEXTTOSPEECHSETTINGS'].fields_by_name['sample_rate_hertz']._loaded_options = None
    _globals['_TEXTTOSPEECHSETTINGS'].fields_by_name['sample_rate_hertz']._serialized_options = b'\xe0A\x01'
    _globals['_TEXTTOSPEECHSETTINGS'].fields_by_name['synthesize_speech_configs']._loaded_options = None
    _globals['_TEXTTOSPEECHSETTINGS'].fields_by_name['synthesize_speech_configs']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENVIRONMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTENVIRONMENTSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%dialogflow.googleapis.com/Environment"
    _globals['_LISTENVIRONMENTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTENVIRONMENTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENVIRONMENTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTENVIRONMENTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETENVIRONMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENVIRONMENTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%dialogflow.googleapis.com/Environment"
    _globals['_CREATEENVIRONMENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEENVIRONMENTREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%dialogflow.googleapis.com/Environment"
    _globals['_CREATEENVIRONMENTREQUEST'].fields_by_name['environment']._loaded_options = None
    _globals['_CREATEENVIRONMENTREQUEST'].fields_by_name['environment']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEENVIRONMENTREQUEST'].fields_by_name['environment_id']._loaded_options = None
    _globals['_CREATEENVIRONMENTREQUEST'].fields_by_name['environment_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEENVIRONMENTREQUEST'].fields_by_name['environment']._loaded_options = None
    _globals['_UPDATEENVIRONMENTREQUEST'].fields_by_name['environment']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEENVIRONMENTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEENVIRONMENTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEENVIRONMENTREQUEST'].fields_by_name['allow_load_to_draft_and_discard_changes']._loaded_options = None
    _globals['_UPDATEENVIRONMENTREQUEST'].fields_by_name['allow_load_to_draft_and_discard_changes']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEENVIRONMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEENVIRONMENTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%dialogflow.googleapis.com/Environment"
    _globals['_GETENVIRONMENTHISTORYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_GETENVIRONMENTHISTORYREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\n%dialogflow.googleapis.com/Environment"
    _globals['_GETENVIRONMENTHISTORYREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_GETENVIRONMENTHISTORYREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_GETENVIRONMENTHISTORYREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_GETENVIRONMENTHISTORYREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_ENVIRONMENTHISTORY'].fields_by_name['parent']._loaded_options = None
    _globals['_ENVIRONMENTHISTORY'].fields_by_name['parent']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENTHISTORY'].fields_by_name['entries']._loaded_options = None
    _globals['_ENVIRONMENTHISTORY'].fields_by_name['entries']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENTHISTORY'].fields_by_name['next_page_token']._loaded_options = None
    _globals['_ENVIRONMENTHISTORY'].fields_by_name['next_page_token']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENTS']._loaded_options = None
    _globals['_ENVIRONMENTS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_ENVIRONMENTS'].methods_by_name['ListEnvironments']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['ListEnvironments']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02p\x12//v2beta1/{parent=projects/*/agent}/environmentsZ=\x12;/v2beta1/{parent=projects/*/locations/*/agent}/environments'
    _globals['_ENVIRONMENTS'].methods_by_name['GetEnvironment']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['GetEnvironment']._serialized_options = b'\x82\xd3\xe4\x93\x02p\x12//v2beta1/{name=projects/*/agent/environments/*}Z=\x12;/v2beta1/{name=projects/*/locations/*/agent/environments/*}'
    _globals['_ENVIRONMENTS'].methods_by_name['CreateEnvironment']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['CreateEnvironment']._serialized_options = b'\x82\xd3\xe4\x93\x02\x8a\x01"//v2beta1/{parent=projects/*/agent}/environments:\x0benvironmentZJ";/v2beta1/{parent=projects/*/locations/*/agent}/environments:\x0benvironment'
    _globals['_ENVIRONMENTS'].methods_by_name['UpdateEnvironment']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['UpdateEnvironment']._serialized_options = b'\x82\xd3\xe4\x93\x02\xa2\x012;/v2beta1/{environment.name=projects/*/agent/environments/*}:\x0benvironmentZV2G/v2beta1/{environment.name=projects/*/locations/*/agent/environments/*}:\x0benvironment'
    _globals['_ENVIRONMENTS'].methods_by_name['DeleteEnvironment']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['DeleteEnvironment']._serialized_options = b'\x82\xd3\xe4\x93\x02p*//v2beta1/{name=projects/*/agent/environments/*}Z=*;/v2beta1/{name=projects/*/locations/*/agent/environments/*}'
    _globals['_ENVIRONMENTS'].methods_by_name['GetEnvironmentHistory']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['GetEnvironmentHistory']._serialized_options = b'\x82\xd3\xe4\x93\x02\x84\x01\x129/v2beta1/{parent=projects/*/agent/environments/*}/historyZG\x12E/v2beta1/{parent=projects/*/locations/*/agent/environments/*}/history'
    _globals['_ENVIRONMENT']._serialized_start = 401
    _globals['_ENVIRONMENT']._serialized_end = 1060
    _globals['_ENVIRONMENT_STATE']._serialized_start = 818
    _globals['_ENVIRONMENT_STATE']._serialized_end = 887
    _globals['_TEXTTOSPEECHSETTINGS']._serialized_start = 1063
    _globals['_TEXTTOSPEECHSETTINGS']._serialized_end = 1488
    _globals['_TEXTTOSPEECHSETTINGS_SYNTHESIZESPEECHCONFIGSENTRY']._serialized_start = 1369
    _globals['_TEXTTOSPEECHSETTINGS_SYNTHESIZESPEECHCONFIGSENTRY']._serialized_end = 1488
    _globals['_LISTENVIRONMENTSREQUEST']._serialized_start = 1491
    _globals['_LISTENVIRONMENTSREQUEST']._serialized_end = 1628
    _globals['_LISTENVIRONMENTSRESPONSE']._serialized_start = 1630
    _globals['_LISTENVIRONMENTSRESPONSE']._serialized_end = 1749
    _globals['_GETENVIRONMENTREQUEST']._serialized_start = 1751
    _globals['_GETENVIRONMENTREQUEST']._serialized_end = 1835
    _globals['_CREATEENVIRONMENTREQUEST']._serialized_start = 1838
    _globals['_CREATEENVIRONMENTREQUEST']._serialized_end = 2028
    _globals['_UPDATEENVIRONMENTREQUEST']._serialized_start = 2031
    _globals['_UPDATEENVIRONMENTREQUEST']._serialized_end = 2237
    _globals['_DELETEENVIRONMENTREQUEST']._serialized_start = 2239
    _globals['_DELETEENVIRONMENTREQUEST']._serialized_end = 2326
    _globals['_GETENVIRONMENTHISTORYREQUEST']._serialized_start = 2329
    _globals['_GETENVIRONMENTHISTORYREQUEST']._serialized_end = 2471
    _globals['_ENVIRONMENTHISTORY']._serialized_start = 2474
    _globals['_ENVIRONMENTHISTORY']._serialized_end = 2728
    _globals['_ENVIRONMENTHISTORY_ENTRY']._serialized_start = 2628
    _globals['_ENVIRONMENTHISTORY_ENTRY']._serialized_end = 2728
    _globals['_ENVIRONMENTS']._serialized_start = 2731
    _globals['_ENVIRONMENTS']._serialized_end = 4458