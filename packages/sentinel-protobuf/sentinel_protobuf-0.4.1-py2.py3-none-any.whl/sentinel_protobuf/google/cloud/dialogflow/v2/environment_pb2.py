"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2/environment.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dialogflow.v2 import audio_config_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_audio__config__pb2
from .....google.cloud.dialogflow.v2 import fulfillment_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_fulfillment__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/dialogflow/v2/environment.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/dialogflow/v2/audio_config.proto\x1a,google/cloud/dialogflow/v2/fulfillment.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x84\x05\n\x0bEnvironment\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01\x12@\n\ragent_version\x18\x03 \x01(\tB)\xe0A\x01\xfaA#\n!dialogflow.googleapis.com/Version\x12A\n\x05state\x18\x04 \x01(\x0e2-.google.cloud.dialogflow.v2.Environment.StateB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12V\n\x17text_to_speech_settings\x18\x07 \x01(\x0b20.google.cloud.dialogflow.v2.TextToSpeechSettingsB\x03\xe0A\x01\x12A\n\x0bfulfillment\x18\x08 \x01(\x0b2\'.google.cloud.dialogflow.v2.FulfillmentB\x03\xe0A\x01"E\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07STOPPED\x10\x01\x12\x0b\n\x07LOADING\x10\x02\x12\x0b\n\x07RUNNING\x10\x03:\xaa\x01\xeaA\xa6\x01\n%dialogflow.googleapis.com/Environment\x123projects/{project}/agent/environments/{environment}\x12Hprojects/{project}/locations/{location}/agent/environments/{environment}"\x9a\x03\n\x14TextToSpeechSettings\x12"\n\x15enable_text_to_speech\x18\x01 \x01(\x08B\x03\xe0A\x01\x12S\n\x15output_audio_encoding\x18\x02 \x01(\x0e2/.google.cloud.dialogflow.v2.OutputAudioEncodingB\x03\xe0A\x02\x12\x1e\n\x11sample_rate_hertz\x18\x03 \x01(\x05B\x03\xe0A\x01\x12u\n\x19synthesize_speech_configs\x18\x04 \x03(\x0b2M.google.cloud.dialogflow.v2.TextToSpeechSettings.SynthesizeSpeechConfigsEntryB\x03\xe0A\x01\x1ar\n\x1cSynthesizeSpeechConfigsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12A\n\x05value\x18\x02 \x01(\x0b22.google.cloud.dialogflow.v2.SynthesizeSpeechConfig:\x028\x01"\x89\x01\n\x17ListEnvironmentsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%dialogflow.googleapis.com/Environment\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"r\n\x18ListEnvironmentsResponse\x12=\n\x0cenvironments\x18\x01 \x03(\x0b2\'.google.cloud.dialogflow.v2.Environment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"T\n\x15GetEnvironmentRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/Environment"\xb9\x01\n\x18CreateEnvironmentRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%dialogflow.googleapis.com/Environment\x12A\n\x0benvironment\x18\x02 \x01(\x0b2\'.google.cloud.dialogflow.v2.EnvironmentB\x03\xe0A\x02\x12\x1b\n\x0eenvironment_id\x18\x03 \x01(\tB\x03\xe0A\x02"\xc9\x01\n\x18UpdateEnvironmentRequest\x12A\n\x0benvironment\x18\x01 \x01(\x0b2\'.google.cloud.dialogflow.v2.EnvironmentB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x124\n\'allow_load_to_draft_and_discard_changes\x18\x03 \x01(\x08B\x03\xe0A\x01"W\n\x18DeleteEnvironmentRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/Environment"\x8e\x01\n\x1cGetEnvironmentHistoryRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/Environment\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\xf9\x01\n\x12EnvironmentHistory\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x03\x12J\n\x07entries\x18\x02 \x03(\x0b24.google.cloud.dialogflow.v2.EnvironmentHistory.EntryB\x03\xe0A\x03\x12\x1c\n\x0fnext_page_token\x18\x03 \x01(\tB\x03\xe0A\x03\x1ad\n\x05Entry\x12\x15\n\ragent_version\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12/\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp2\xcb\x0c\n\x0cEnvironments\x12\xf4\x01\n\x10ListEnvironments\x123.google.cloud.dialogflow.v2.ListEnvironmentsRequest\x1a4.google.cloud.dialogflow.v2.ListEnvironmentsResponse"u\xdaA\x06parent\x82\xd3\xe4\x93\x02f\x12*/v2/{parent=projects/*/agent}/environmentsZ8\x126/v2/{parent=projects/*/locations/*/agent}/environments\x12\xda\x01\n\x0eGetEnvironment\x121.google.cloud.dialogflow.v2.GetEnvironmentRequest\x1a\'.google.cloud.dialogflow.v2.Environment"l\x82\xd3\xe4\x93\x02f\x12*/v2/{name=projects/*/agent/environments/*}Z8\x126/v2/{name=projects/*/locations/*/agent/environments/*}\x12\xfc\x01\n\x11CreateEnvironment\x124.google.cloud.dialogflow.v2.CreateEnvironmentRequest\x1a\'.google.cloud.dialogflow.v2.Environment"\x87\x01\x82\xd3\xe4\x93\x02\x80\x01"*/v2/{parent=projects/*/agent}/environments:\x0benvironmentZE"6/v2/{parent=projects/*/locations/*/agent}/environments:\x0benvironment\x12\x94\x02\n\x11UpdateEnvironment\x124.google.cloud.dialogflow.v2.UpdateEnvironmentRequest\x1a\'.google.cloud.dialogflow.v2.Environment"\x9f\x01\x82\xd3\xe4\x93\x02\x98\x0126/v2/{environment.name=projects/*/agent/environments/*}:\x0benvironmentZQ2B/v2/{environment.name=projects/*/locations/*/agent/environments/*}:\x0benvironment\x12\xcf\x01\n\x11DeleteEnvironment\x124.google.cloud.dialogflow.v2.DeleteEnvironmentRequest\x1a\x16.google.protobuf.Empty"l\x82\xd3\xe4\x93\x02f**/v2/{name=projects/*/agent/environments/*}Z8*6/v2/{name=projects/*/locations/*/agent/environments/*}\x12\x84\x02\n\x15GetEnvironmentHistory\x128.google.cloud.dialogflow.v2.GetEnvironmentHistoryRequest\x1a..google.cloud.dialogflow.v2.EnvironmentHistory"\x80\x01\x82\xd3\xe4\x93\x02z\x124/v2/{parent=projects/*/agent/environments/*}/historyZB\x12@/v2/{parent=projects/*/locations/*/agent/environments/*}/history\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\x96\x01\n\x1ecom.google.cloud.dialogflow.v2B\x10EnvironmentProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2.environment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.dialogflow.v2B\x10EnvironmentProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2'
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
    _globals['_ENVIRONMENTS'].methods_by_name['ListEnvironments']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02f\x12*/v2/{parent=projects/*/agent}/environmentsZ8\x126/v2/{parent=projects/*/locations/*/agent}/environments'
    _globals['_ENVIRONMENTS'].methods_by_name['GetEnvironment']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['GetEnvironment']._serialized_options = b'\x82\xd3\xe4\x93\x02f\x12*/v2/{name=projects/*/agent/environments/*}Z8\x126/v2/{name=projects/*/locations/*/agent/environments/*}'
    _globals['_ENVIRONMENTS'].methods_by_name['CreateEnvironment']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['CreateEnvironment']._serialized_options = b'\x82\xd3\xe4\x93\x02\x80\x01"*/v2/{parent=projects/*/agent}/environments:\x0benvironmentZE"6/v2/{parent=projects/*/locations/*/agent}/environments:\x0benvironment'
    _globals['_ENVIRONMENTS'].methods_by_name['UpdateEnvironment']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['UpdateEnvironment']._serialized_options = b'\x82\xd3\xe4\x93\x02\x98\x0126/v2/{environment.name=projects/*/agent/environments/*}:\x0benvironmentZQ2B/v2/{environment.name=projects/*/locations/*/agent/environments/*}:\x0benvironment'
    _globals['_ENVIRONMENTS'].methods_by_name['DeleteEnvironment']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['DeleteEnvironment']._serialized_options = b'\x82\xd3\xe4\x93\x02f**/v2/{name=projects/*/agent/environments/*}Z8*6/v2/{name=projects/*/locations/*/agent/environments/*}'
    _globals['_ENVIRONMENTS'].methods_by_name['GetEnvironmentHistory']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['GetEnvironmentHistory']._serialized_options = b'\x82\xd3\xe4\x93\x02z\x124/v2/{parent=projects/*/agent/environments/*}/historyZB\x12@/v2/{parent=projects/*/locations/*/agent/environments/*}/history'
    _globals['_ENVIRONMENT']._serialized_start = 381
    _globals['_ENVIRONMENT']._serialized_end = 1025
    _globals['_ENVIRONMENT_STATE']._serialized_start = 783
    _globals['_ENVIRONMENT_STATE']._serialized_end = 852
    _globals['_TEXTTOSPEECHSETTINGS']._serialized_start = 1028
    _globals['_TEXTTOSPEECHSETTINGS']._serialized_end = 1438
    _globals['_TEXTTOSPEECHSETTINGS_SYNTHESIZESPEECHCONFIGSENTRY']._serialized_start = 1324
    _globals['_TEXTTOSPEECHSETTINGS_SYNTHESIZESPEECHCONFIGSENTRY']._serialized_end = 1438
    _globals['_LISTENVIRONMENTSREQUEST']._serialized_start = 1441
    _globals['_LISTENVIRONMENTSREQUEST']._serialized_end = 1578
    _globals['_LISTENVIRONMENTSRESPONSE']._serialized_start = 1580
    _globals['_LISTENVIRONMENTSRESPONSE']._serialized_end = 1694
    _globals['_GETENVIRONMENTREQUEST']._serialized_start = 1696
    _globals['_GETENVIRONMENTREQUEST']._serialized_end = 1780
    _globals['_CREATEENVIRONMENTREQUEST']._serialized_start = 1783
    _globals['_CREATEENVIRONMENTREQUEST']._serialized_end = 1968
    _globals['_UPDATEENVIRONMENTREQUEST']._serialized_start = 1971
    _globals['_UPDATEENVIRONMENTREQUEST']._serialized_end = 2172
    _globals['_DELETEENVIRONMENTREQUEST']._serialized_start = 2174
    _globals['_DELETEENVIRONMENTREQUEST']._serialized_end = 2261
    _globals['_GETENVIRONMENTHISTORYREQUEST']._serialized_start = 2264
    _globals['_GETENVIRONMENTHISTORYREQUEST']._serialized_end = 2406
    _globals['_ENVIRONMENTHISTORY']._serialized_start = 2409
    _globals['_ENVIRONMENTHISTORY']._serialized_end = 2658
    _globals['_ENVIRONMENTHISTORY_ENTRY']._serialized_start = 2558
    _globals['_ENVIRONMENTHISTORY_ENTRY']._serialized_end = 2658
    _globals['_ENVIRONMENTS']._serialized_start = 2661
    _globals['_ENVIRONMENTS']._serialized_end = 4272