"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3/intent.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3 import inline_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_inline__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/dialogflow/cx/v3/intent.proto\x12\x1dgoogle.cloud.dialogflow.cx.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a*google/cloud/dialogflow/cx/v3/inline.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x9c\x06\n\x06Intent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12N\n\x10training_phrases\x18\x03 \x03(\x0b24.google.cloud.dialogflow.cx.v3.Intent.TrainingPhrase\x12C\n\nparameters\x18\x04 \x03(\x0b2/.google.cloud.dialogflow.cx.v3.Intent.Parameter\x12\x10\n\x08priority\x18\x05 \x01(\x05\x12\x13\n\x0bis_fallback\x18\x06 \x01(\x08\x12A\n\x06labels\x18\x07 \x03(\x0b21.google.cloud.dialogflow.cx.v3.Intent.LabelsEntry\x12\x13\n\x0bdescription\x18\x08 \x01(\t\x1a\xb2\x01\n\x0eTrainingPhrase\x12\n\n\x02id\x18\x01 \x01(\t\x12M\n\x05parts\x18\x02 \x03(\x0b29.google.cloud.dialogflow.cx.v3.Intent.TrainingPhrase.PartB\x03\xe0A\x02\x12\x14\n\x0crepeat_count\x18\x03 \x01(\x05\x1a/\n\x04Part\x12\x11\n\x04text\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x0cparameter_id\x18\x02 \x01(\t\x1a\x80\x01\n\tParameter\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x02\x12A\n\x0bentity_type\x18\x02 \x01(\tB,\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/EntityType\x12\x0f\n\x07is_list\x18\x03 \x01(\x08\x12\x0e\n\x06redact\x18\x04 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:n\xeaAk\n dialogflow.googleapis.com/Intent\x12Gprojects/{project}/locations/{location}/agents/{agent}/intents/{intent}"\xcc\x01\n\x12ListIntentsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 dialogflow.googleapis.com/Intent\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12>\n\x0bintent_view\x18\x05 \x01(\x0e2).google.cloud.dialogflow.cx.v3.IntentView\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"f\n\x13ListIntentsResponse\x126\n\x07intents\x18\x01 \x03(\x0b2%.google.cloud.dialogflow.cx.v3.Intent\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"a\n\x10GetIntentRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n dialogflow.googleapis.com/Intent\x12\x15\n\rlanguage_code\x18\x02 \x01(\t"\xa2\x01\n\x13CreateIntentRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 dialogflow.googleapis.com/Intent\x12:\n\x06intent\x18\x02 \x01(\x0b2%.google.cloud.dialogflow.cx.v3.IntentB\x03\xe0A\x02\x12\x15\n\rlanguage_code\x18\x03 \x01(\t"\x99\x01\n\x13UpdateIntentRequest\x12:\n\x06intent\x18\x01 \x01(\x0b2%.google.cloud.dialogflow.cx.v3.IntentB\x03\xe0A\x02\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"M\n\x13DeleteIntentRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n dialogflow.googleapis.com/Intent"\x91\x03\n\x14ImportIntentsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 dialogflow.googleapis.com/Intent\x12\x15\n\x0bintents_uri\x18\x02 \x01(\tH\x00\x12F\n\x0fintents_content\x18\x03 \x01(\x0b2+.google.cloud.dialogflow.cx.v3.InlineSourceH\x00\x12U\n\x0cmerge_option\x18\x04 \x01(\x0e2?.google.cloud.dialogflow.cx.v3.ImportIntentsRequest.MergeOption"~\n\x0bMergeOption\x12\x1c\n\x18MERGE_OPTION_UNSPECIFIED\x10\x00\x12\x0e\n\x06REJECT\x10\x01\x1a\x02\x08\x01\x12\x0b\n\x07REPLACE\x10\x02\x12\t\n\x05MERGE\x10\x03\x12\n\n\x06RENAME\x10\x04\x12\x13\n\x0fREPORT_CONFLICT\x10\x05\x12\x08\n\x04KEEP\x10\x06B\t\n\x07intents"\x8d\x02\n\x15ImportIntentsResponse\x126\n\x07intents\x18\x01 \x03(\tB%\xfaA"\n dialogflow.googleapis.com/Intent\x12h\n\x15conflicting_resources\x18\x02 \x01(\x0b2I.google.cloud.dialogflow.cx.v3.ImportIntentsResponse.ConflictingResources\x1aR\n\x14ConflictingResources\x12\x1c\n\x14intent_display_names\x18\x01 \x03(\t\x12\x1c\n\x14entity_display_names\x18\x02 \x03(\t"\x17\n\x15ImportIntentsMetadata"\xda\x02\n\x14ExportIntentsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 dialogflow.googleapis.com/Intent\x12\x14\n\x07intents\x18\x02 \x03(\tB\x03\xe0A\x02\x12\x1a\n\x0bintents_uri\x18\x03 \x01(\tB\x03\xe0A\x01H\x00\x12%\n\x16intents_content_inline\x18\x04 \x01(\x08B\x03\xe0A\x01H\x00\x12X\n\x0bdata_format\x18\x05 \x01(\x0e2>.google.cloud.dialogflow.cx.v3.ExportIntentsRequest.DataFormatB\x03\xe0A\x01"F\n\nDataFormat\x12\x1b\n\x17DATA_FORMAT_UNSPECIFIED\x10\x00\x12\x08\n\x04BLOB\x10\x01\x12\x08\n\x04JSON\x10\x02\x12\x07\n\x03CSV\x10\x03B\r\n\x0bdestination"\x86\x01\n\x15ExportIntentsResponse\x12\x15\n\x0bintents_uri\x18\x01 \x01(\tH\x00\x12K\n\x0fintents_content\x18\x02 \x01(\x0b20.google.cloud.dialogflow.cx.v3.InlineDestinationH\x00B\t\n\x07intents"\x17\n\x15ExportIntentsMetadata*X\n\nIntentView\x12\x1b\n\x17INTENT_VIEW_UNSPECIFIED\x10\x00\x12\x17\n\x13INTENT_VIEW_PARTIAL\x10\x01\x12\x14\n\x10INTENT_VIEW_FULL\x10\x022\xdc\x0b\n\x07Intents\x12\xbb\x01\n\x0bListIntents\x121.google.cloud.dialogflow.cx.v3.ListIntentsRequest\x1a2.google.cloud.dialogflow.cx.v3.ListIntentsResponse"E\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v3/{parent=projects/*/locations/*/agents/*}/intents\x12\xa8\x01\n\tGetIntent\x12/.google.cloud.dialogflow.cx.v3.GetIntentRequest\x1a%.google.cloud.dialogflow.cx.v3.Intent"C\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v3/{name=projects/*/locations/*/agents/*/intents/*}\x12\xbf\x01\n\x0cCreateIntent\x122.google.cloud.dialogflow.cx.v3.CreateIntentRequest\x1a%.google.cloud.dialogflow.cx.v3.Intent"T\xdaA\rparent,intent\x82\xd3\xe4\x93\x02>"4/v3/{parent=projects/*/locations/*/agents/*}/intents:\x06intent\x12\xcb\x01\n\x0cUpdateIntent\x122.google.cloud.dialogflow.cx.v3.UpdateIntentRequest\x1a%.google.cloud.dialogflow.cx.v3.Intent"`\xdaA\x12intent,update_mask\x82\xd3\xe4\x93\x02E2;/v3/{intent.name=projects/*/locations/*/agents/*/intents/*}:\x06intent\x12\x9f\x01\n\x0cDeleteIntent\x122.google.cloud.dialogflow.cx.v3.DeleteIntentRequest\x1a\x16.google.protobuf.Empty"C\xdaA\x04name\x82\xd3\xe4\x93\x026*4/v3/{name=projects/*/locations/*/agents/*/intents/*}\x12\xdc\x01\n\rImportIntents\x123.google.cloud.dialogflow.cx.v3.ImportIntentsRequest\x1a\x1d.google.longrunning.Operation"w\xcaA.\n\x15ImportIntentsResponse\x12\x15ImportIntentsMetadata\x82\xd3\xe4\x93\x02@";/v3/{parent=projects/*/locations/*/agents/*}/intents:import:\x01*\x12\xdc\x01\n\rExportIntents\x123.google.cloud.dialogflow.cx.v3.ExportIntentsRequest\x1a\x1d.google.longrunning.Operation"w\xcaA.\n\x15ExportIntentsResponse\x12\x15ExportIntentsMetadata\x82\xd3\xe4\x93\x02@";/v3/{parent=projects/*/locations/*/agents/*}/intents:export:\x01*\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xae\x01\n!com.google.cloud.dialogflow.cx.v3B\x0bIntentProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3.intent_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.dialogflow.cx.v3B\x0bIntentProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3'
    _globals['_INTENT_TRAININGPHRASE_PART'].fields_by_name['text']._loaded_options = None
    _globals['_INTENT_TRAININGPHRASE_PART'].fields_by_name['text']._serialized_options = b'\xe0A\x02'
    _globals['_INTENT_TRAININGPHRASE'].fields_by_name['parts']._loaded_options = None
    _globals['_INTENT_TRAININGPHRASE'].fields_by_name['parts']._serialized_options = b'\xe0A\x02'
    _globals['_INTENT_PARAMETER'].fields_by_name['id']._loaded_options = None
    _globals['_INTENT_PARAMETER'].fields_by_name['id']._serialized_options = b'\xe0A\x02'
    _globals['_INTENT_PARAMETER'].fields_by_name['entity_type']._loaded_options = None
    _globals['_INTENT_PARAMETER'].fields_by_name['entity_type']._serialized_options = b'\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/EntityType'
    _globals['_INTENT_LABELSENTRY']._loaded_options = None
    _globals['_INTENT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_INTENT'].fields_by_name['display_name']._loaded_options = None
    _globals['_INTENT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_INTENT']._loaded_options = None
    _globals['_INTENT']._serialized_options = b'\xeaAk\n dialogflow.googleapis.com/Intent\x12Gprojects/{project}/locations/{location}/agents/{agent}/intents/{intent}'
    _globals['_LISTINTENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTINTENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 dialogflow.googleapis.com/Intent'
    _globals['_GETINTENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINTENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n dialogflow.googleapis.com/Intent'
    _globals['_CREATEINTENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEINTENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 dialogflow.googleapis.com/Intent'
    _globals['_CREATEINTENTREQUEST'].fields_by_name['intent']._loaded_options = None
    _globals['_CREATEINTENTREQUEST'].fields_by_name['intent']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEINTENTREQUEST'].fields_by_name['intent']._loaded_options = None
    _globals['_UPDATEINTENTREQUEST'].fields_by_name['intent']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEINTENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEINTENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n dialogflow.googleapis.com/Intent'
    _globals['_IMPORTINTENTSREQUEST_MERGEOPTION'].values_by_name['REJECT']._loaded_options = None
    _globals['_IMPORTINTENTSREQUEST_MERGEOPTION'].values_by_name['REJECT']._serialized_options = b'\x08\x01'
    _globals['_IMPORTINTENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTINTENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 dialogflow.googleapis.com/Intent'
    _globals['_IMPORTINTENTSRESPONSE'].fields_by_name['intents']._loaded_options = None
    _globals['_IMPORTINTENTSRESPONSE'].fields_by_name['intents']._serialized_options = b'\xfaA"\n dialogflow.googleapis.com/Intent'
    _globals['_EXPORTINTENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_EXPORTINTENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 dialogflow.googleapis.com/Intent'
    _globals['_EXPORTINTENTSREQUEST'].fields_by_name['intents']._loaded_options = None
    _globals['_EXPORTINTENTSREQUEST'].fields_by_name['intents']._serialized_options = b'\xe0A\x02'
    _globals['_EXPORTINTENTSREQUEST'].fields_by_name['intents_uri']._loaded_options = None
    _globals['_EXPORTINTENTSREQUEST'].fields_by_name['intents_uri']._serialized_options = b'\xe0A\x01'
    _globals['_EXPORTINTENTSREQUEST'].fields_by_name['intents_content_inline']._loaded_options = None
    _globals['_EXPORTINTENTSREQUEST'].fields_by_name['intents_content_inline']._serialized_options = b'\xe0A\x01'
    _globals['_EXPORTINTENTSREQUEST'].fields_by_name['data_format']._loaded_options = None
    _globals['_EXPORTINTENTSREQUEST'].fields_by_name['data_format']._serialized_options = b'\xe0A\x01'
    _globals['_INTENTS']._loaded_options = None
    _globals['_INTENTS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_INTENTS'].methods_by_name['ListIntents']._loaded_options = None
    _globals['_INTENTS'].methods_by_name['ListIntents']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v3/{parent=projects/*/locations/*/agents/*}/intents'
    _globals['_INTENTS'].methods_by_name['GetIntent']._loaded_options = None
    _globals['_INTENTS'].methods_by_name['GetIntent']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v3/{name=projects/*/locations/*/agents/*/intents/*}'
    _globals['_INTENTS'].methods_by_name['CreateIntent']._loaded_options = None
    _globals['_INTENTS'].methods_by_name['CreateIntent']._serialized_options = b'\xdaA\rparent,intent\x82\xd3\xe4\x93\x02>"4/v3/{parent=projects/*/locations/*/agents/*}/intents:\x06intent'
    _globals['_INTENTS'].methods_by_name['UpdateIntent']._loaded_options = None
    _globals['_INTENTS'].methods_by_name['UpdateIntent']._serialized_options = b'\xdaA\x12intent,update_mask\x82\xd3\xe4\x93\x02E2;/v3/{intent.name=projects/*/locations/*/agents/*/intents/*}:\x06intent'
    _globals['_INTENTS'].methods_by_name['DeleteIntent']._loaded_options = None
    _globals['_INTENTS'].methods_by_name['DeleteIntent']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026*4/v3/{name=projects/*/locations/*/agents/*/intents/*}'
    _globals['_INTENTS'].methods_by_name['ImportIntents']._loaded_options = None
    _globals['_INTENTS'].methods_by_name['ImportIntents']._serialized_options = b'\xcaA.\n\x15ImportIntentsResponse\x12\x15ImportIntentsMetadata\x82\xd3\xe4\x93\x02@";/v3/{parent=projects/*/locations/*/agents/*}/intents:import:\x01*'
    _globals['_INTENTS'].methods_by_name['ExportIntents']._loaded_options = None
    _globals['_INTENTS'].methods_by_name['ExportIntents']._serialized_options = b'\xcaA.\n\x15ExportIntentsResponse\x12\x15ExportIntentsMetadata\x82\xd3\xe4\x93\x02@";/v3/{parent=projects/*/locations/*/agents/*}/intents:export:\x01*'
    _globals['_INTENTVIEW']._serialized_start = 3157
    _globals['_INTENTVIEW']._serialized_end = 3245
    _globals['_INTENT']._serialized_start = 337
    _globals['_INTENT']._serialized_end = 1133
    _globals['_INTENT_TRAININGPHRASE']._serialized_start = 665
    _globals['_INTENT_TRAININGPHRASE']._serialized_end = 843
    _globals['_INTENT_TRAININGPHRASE_PART']._serialized_start = 796
    _globals['_INTENT_TRAININGPHRASE_PART']._serialized_end = 843
    _globals['_INTENT_PARAMETER']._serialized_start = 846
    _globals['_INTENT_PARAMETER']._serialized_end = 974
    _globals['_INTENT_LABELSENTRY']._serialized_start = 976
    _globals['_INTENT_LABELSENTRY']._serialized_end = 1021
    _globals['_LISTINTENTSREQUEST']._serialized_start = 1136
    _globals['_LISTINTENTSREQUEST']._serialized_end = 1340
    _globals['_LISTINTENTSRESPONSE']._serialized_start = 1342
    _globals['_LISTINTENTSRESPONSE']._serialized_end = 1444
    _globals['_GETINTENTREQUEST']._serialized_start = 1446
    _globals['_GETINTENTREQUEST']._serialized_end = 1543
    _globals['_CREATEINTENTREQUEST']._serialized_start = 1546
    _globals['_CREATEINTENTREQUEST']._serialized_end = 1708
    _globals['_UPDATEINTENTREQUEST']._serialized_start = 1711
    _globals['_UPDATEINTENTREQUEST']._serialized_end = 1864
    _globals['_DELETEINTENTREQUEST']._serialized_start = 1866
    _globals['_DELETEINTENTREQUEST']._serialized_end = 1943
    _globals['_IMPORTINTENTSREQUEST']._serialized_start = 1946
    _globals['_IMPORTINTENTSREQUEST']._serialized_end = 2347
    _globals['_IMPORTINTENTSREQUEST_MERGEOPTION']._serialized_start = 2210
    _globals['_IMPORTINTENTSREQUEST_MERGEOPTION']._serialized_end = 2336
    _globals['_IMPORTINTENTSRESPONSE']._serialized_start = 2350
    _globals['_IMPORTINTENTSRESPONSE']._serialized_end = 2619
    _globals['_IMPORTINTENTSRESPONSE_CONFLICTINGRESOURCES']._serialized_start = 2537
    _globals['_IMPORTINTENTSRESPONSE_CONFLICTINGRESOURCES']._serialized_end = 2619
    _globals['_IMPORTINTENTSMETADATA']._serialized_start = 2621
    _globals['_IMPORTINTENTSMETADATA']._serialized_end = 2644
    _globals['_EXPORTINTENTSREQUEST']._serialized_start = 2647
    _globals['_EXPORTINTENTSREQUEST']._serialized_end = 2993
    _globals['_EXPORTINTENTSREQUEST_DATAFORMAT']._serialized_start = 2908
    _globals['_EXPORTINTENTSREQUEST_DATAFORMAT']._serialized_end = 2978
    _globals['_EXPORTINTENTSRESPONSE']._serialized_start = 2996
    _globals['_EXPORTINTENTSRESPONSE']._serialized_end = 3130
    _globals['_EXPORTINTENTSMETADATA']._serialized_start = 3132
    _globals['_EXPORTINTENTSMETADATA']._serialized_end = 3155
    _globals['_INTENTS']._serialized_start = 3248
    _globals['_INTENTS']._serialized_end = 4748