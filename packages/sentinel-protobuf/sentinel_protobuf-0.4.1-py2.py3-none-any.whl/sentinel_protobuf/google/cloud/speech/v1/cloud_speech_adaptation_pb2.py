"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/speech/v1/cloud_speech_adaptation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.speech.v1 import resource_pb2 as google_dot_cloud_dot_speech_dot_v1_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/speech/v1/cloud_speech_adaptation.proto\x12\x16google.cloud.speech.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a%google/cloud/speech/v1/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xa9\x01\n\x16CreatePhraseSetRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fspeech.googleapis.com/PhraseSet\x12\x1a\n\rphrase_set_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12:\n\nphrase_set\x18\x03 \x01(\x0b2!.google.cloud.speech.v1.PhraseSetB\x03\xe0A\x02"\x85\x01\n\x16UpdatePhraseSetRequest\x12:\n\nphrase_set\x18\x01 \x01(\x0b2!.google.cloud.speech.v1.PhraseSetB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"L\n\x13GetPhraseSetRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspeech.googleapis.com/PhraseSet"v\n\x14ListPhraseSetRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fspeech.googleapis.com/PhraseSet\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"h\n\x15ListPhraseSetResponse\x126\n\x0bphrase_sets\x18\x01 \x03(\x0b2!.google.cloud.speech.v1.PhraseSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"O\n\x16DeletePhraseSetRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspeech.googleapis.com/PhraseSet"\xb3\x01\n\x18CreateCustomClassRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!speech.googleapis.com/CustomClass\x12\x1c\n\x0fcustom_class_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12>\n\x0ccustom_class\x18\x03 \x01(\x0b2#.google.cloud.speech.v1.CustomClassB\x03\xe0A\x02"\x8b\x01\n\x18UpdateCustomClassRequest\x12>\n\x0ccustom_class\x18\x01 \x01(\x0b2#.google.cloud.speech.v1.CustomClassB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"P\n\x15GetCustomClassRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!speech.googleapis.com/CustomClass"|\n\x18ListCustomClassesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!speech.googleapis.com/CustomClass\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"q\n\x19ListCustomClassesResponse\x12;\n\x0ecustom_classes\x18\x01 \x03(\x0b2#.google.cloud.speech.v1.CustomClass\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"S\n\x18DeleteCustomClassRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!speech.googleapis.com/CustomClass2\x8e\x0f\n\nAdaptation\x12\xc1\x01\n\x0fCreatePhraseSet\x12..google.cloud.speech.v1.CreatePhraseSetRequest\x1a!.google.cloud.speech.v1.PhraseSet"[\xdaA\x1fparent,phrase_set,phrase_set_id\x82\xd3\xe4\x93\x023"./v1/{parent=projects/*/locations/*}/phraseSets:\x01*\x12\x9d\x01\n\x0cGetPhraseSet\x12+.google.cloud.speech.v1.GetPhraseSetRequest\x1a!.google.cloud.speech.v1.PhraseSet"=\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/phraseSets/*}\x12\xad\x01\n\rListPhraseSet\x12,.google.cloud.speech.v1.ListPhraseSetRequest\x1a-.google.cloud.speech.v1.ListPhraseSetResponse"?\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/phraseSets\x12\xcc\x01\n\x0fUpdatePhraseSet\x12..google.cloud.speech.v1.UpdatePhraseSetRequest\x1a!.google.cloud.speech.v1.PhraseSet"f\xdaA\x16phrase_set,update_mask\x82\xd3\xe4\x93\x02G29/v1/{phrase_set.name=projects/*/locations/*/phraseSets/*}:\nphrase_set\x12\x98\x01\n\x0fDeletePhraseSet\x12..google.cloud.speech.v1.DeletePhraseSetRequest\x1a\x16.google.protobuf.Empty"=\xdaA\x04name\x82\xd3\xe4\x93\x020*./v1/{name=projects/*/locations/*/phraseSets/*}\x12\xce\x01\n\x11CreateCustomClass\x120.google.cloud.speech.v1.CreateCustomClassRequest\x1a#.google.cloud.speech.v1.CustomClass"b\xdaA#parent,custom_class,custom_class_id\x82\xd3\xe4\x93\x026"1/v1/{parent=projects/*/locations/*}/customClasses:\x01*\x12\xa6\x01\n\x0eGetCustomClass\x12-.google.cloud.speech.v1.GetCustomClassRequest\x1a#.google.cloud.speech.v1.CustomClass"@\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1/{name=projects/*/locations/*/customClasses/*}\x12\xbc\x01\n\x11ListCustomClasses\x120.google.cloud.speech.v1.ListCustomClassesRequest\x1a1.google.cloud.speech.v1.ListCustomClassesResponse"B\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1/{parent=projects/*/locations/*}/customClasses\x12\xdb\x01\n\x11UpdateCustomClass\x120.google.cloud.speech.v1.UpdateCustomClassRequest\x1a#.google.cloud.speech.v1.CustomClass"o\xdaA\x18custom_class,update_mask\x82\xd3\xe4\x93\x02N2>/v1/{custom_class.name=projects/*/locations/*/customClasses/*}:\x0ccustom_class\x12\x9f\x01\n\x11DeleteCustomClass\x120.google.cloud.speech.v1.DeleteCustomClassRequest\x1a\x16.google.protobuf.Empty"@\xdaA\x04name\x82\xd3\xe4\x93\x023*1/v1/{name=projects/*/locations/*/customClasses/*}\x1aI\xcaA\x15speech.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBr\n\x1acom.google.cloud.speech.v1B\x15SpeechAdaptationProtoP\x01Z2cloud.google.com/go/speech/apiv1/speechpb;speechpb\xf8\x01\x01\xa2\x02\x03GCSb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.speech.v1.cloud_speech_adaptation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.speech.v1B\x15SpeechAdaptationProtoP\x01Z2cloud.google.com/go/speech/apiv1/speechpb;speechpb\xf8\x01\x01\xa2\x02\x03GCS'
    _globals['_CREATEPHRASESETREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPHRASESETREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fspeech.googleapis.com/PhraseSet'
    _globals['_CREATEPHRASESETREQUEST'].fields_by_name['phrase_set_id']._loaded_options = None
    _globals['_CREATEPHRASESETREQUEST'].fields_by_name['phrase_set_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPHRASESETREQUEST'].fields_by_name['phrase_set']._loaded_options = None
    _globals['_CREATEPHRASESETREQUEST'].fields_by_name['phrase_set']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPHRASESETREQUEST'].fields_by_name['phrase_set']._loaded_options = None
    _globals['_UPDATEPHRASESETREQUEST'].fields_by_name['phrase_set']._serialized_options = b'\xe0A\x02'
    _globals['_GETPHRASESETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPHRASESETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fspeech.googleapis.com/PhraseSet'
    _globals['_LISTPHRASESETREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPHRASESETREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fspeech.googleapis.com/PhraseSet'
    _globals['_DELETEPHRASESETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPHRASESETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fspeech.googleapis.com/PhraseSet'
    _globals['_CREATECUSTOMCLASSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECUSTOMCLASSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!speech.googleapis.com/CustomClass'
    _globals['_CREATECUSTOMCLASSREQUEST'].fields_by_name['custom_class_id']._loaded_options = None
    _globals['_CREATECUSTOMCLASSREQUEST'].fields_by_name['custom_class_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECUSTOMCLASSREQUEST'].fields_by_name['custom_class']._loaded_options = None
    _globals['_CREATECUSTOMCLASSREQUEST'].fields_by_name['custom_class']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECUSTOMCLASSREQUEST'].fields_by_name['custom_class']._loaded_options = None
    _globals['_UPDATECUSTOMCLASSREQUEST'].fields_by_name['custom_class']._serialized_options = b'\xe0A\x02'
    _globals['_GETCUSTOMCLASSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCUSTOMCLASSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!speech.googleapis.com/CustomClass'
    _globals['_LISTCUSTOMCLASSESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCUSTOMCLASSESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!speech.googleapis.com/CustomClass'
    _globals['_DELETECUSTOMCLASSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECUSTOMCLASSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!speech.googleapis.com/CustomClass'
    _globals['_ADAPTATION']._loaded_options = None
    _globals['_ADAPTATION']._serialized_options = b'\xcaA\x15speech.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ADAPTATION'].methods_by_name['CreatePhraseSet']._loaded_options = None
    _globals['_ADAPTATION'].methods_by_name['CreatePhraseSet']._serialized_options = b'\xdaA\x1fparent,phrase_set,phrase_set_id\x82\xd3\xe4\x93\x023"./v1/{parent=projects/*/locations/*}/phraseSets:\x01*'
    _globals['_ADAPTATION'].methods_by_name['GetPhraseSet']._loaded_options = None
    _globals['_ADAPTATION'].methods_by_name['GetPhraseSet']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/phraseSets/*}'
    _globals['_ADAPTATION'].methods_by_name['ListPhraseSet']._loaded_options = None
    _globals['_ADAPTATION'].methods_by_name['ListPhraseSet']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/phraseSets'
    _globals['_ADAPTATION'].methods_by_name['UpdatePhraseSet']._loaded_options = None
    _globals['_ADAPTATION'].methods_by_name['UpdatePhraseSet']._serialized_options = b'\xdaA\x16phrase_set,update_mask\x82\xd3\xe4\x93\x02G29/v1/{phrase_set.name=projects/*/locations/*/phraseSets/*}:\nphrase_set'
    _globals['_ADAPTATION'].methods_by_name['DeletePhraseSet']._loaded_options = None
    _globals['_ADAPTATION'].methods_by_name['DeletePhraseSet']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020*./v1/{name=projects/*/locations/*/phraseSets/*}'
    _globals['_ADAPTATION'].methods_by_name['CreateCustomClass']._loaded_options = None
    _globals['_ADAPTATION'].methods_by_name['CreateCustomClass']._serialized_options = b'\xdaA#parent,custom_class,custom_class_id\x82\xd3\xe4\x93\x026"1/v1/{parent=projects/*/locations/*}/customClasses:\x01*'
    _globals['_ADAPTATION'].methods_by_name['GetCustomClass']._loaded_options = None
    _globals['_ADAPTATION'].methods_by_name['GetCustomClass']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1/{name=projects/*/locations/*/customClasses/*}'
    _globals['_ADAPTATION'].methods_by_name['ListCustomClasses']._loaded_options = None
    _globals['_ADAPTATION'].methods_by_name['ListCustomClasses']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1/{parent=projects/*/locations/*}/customClasses'
    _globals['_ADAPTATION'].methods_by_name['UpdateCustomClass']._loaded_options = None
    _globals['_ADAPTATION'].methods_by_name['UpdateCustomClass']._serialized_options = b'\xdaA\x18custom_class,update_mask\x82\xd3\xe4\x93\x02N2>/v1/{custom_class.name=projects/*/locations/*/customClasses/*}:\x0ccustom_class'
    _globals['_ADAPTATION'].methods_by_name['DeleteCustomClass']._loaded_options = None
    _globals['_ADAPTATION'].methods_by_name['DeleteCustomClass']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023*1/v1/{name=projects/*/locations/*/customClasses/*}'
    _globals['_CREATEPHRASESETREQUEST']._serialized_start = 298
    _globals['_CREATEPHRASESETREQUEST']._serialized_end = 467
    _globals['_UPDATEPHRASESETREQUEST']._serialized_start = 470
    _globals['_UPDATEPHRASESETREQUEST']._serialized_end = 603
    _globals['_GETPHRASESETREQUEST']._serialized_start = 605
    _globals['_GETPHRASESETREQUEST']._serialized_end = 681
    _globals['_LISTPHRASESETREQUEST']._serialized_start = 683
    _globals['_LISTPHRASESETREQUEST']._serialized_end = 801
    _globals['_LISTPHRASESETRESPONSE']._serialized_start = 803
    _globals['_LISTPHRASESETRESPONSE']._serialized_end = 907
    _globals['_DELETEPHRASESETREQUEST']._serialized_start = 909
    _globals['_DELETEPHRASESETREQUEST']._serialized_end = 988
    _globals['_CREATECUSTOMCLASSREQUEST']._serialized_start = 991
    _globals['_CREATECUSTOMCLASSREQUEST']._serialized_end = 1170
    _globals['_UPDATECUSTOMCLASSREQUEST']._serialized_start = 1173
    _globals['_UPDATECUSTOMCLASSREQUEST']._serialized_end = 1312
    _globals['_GETCUSTOMCLASSREQUEST']._serialized_start = 1314
    _globals['_GETCUSTOMCLASSREQUEST']._serialized_end = 1394
    _globals['_LISTCUSTOMCLASSESREQUEST']._serialized_start = 1396
    _globals['_LISTCUSTOMCLASSESREQUEST']._serialized_end = 1520
    _globals['_LISTCUSTOMCLASSESRESPONSE']._serialized_start = 1522
    _globals['_LISTCUSTOMCLASSESRESPONSE']._serialized_end = 1635
    _globals['_DELETECUSTOMCLASSREQUEST']._serialized_start = 1637
    _globals['_DELETECUSTOMCLASSREQUEST']._serialized_end = 1720
    _globals['_ADAPTATION']._serialized_start = 1723
    _globals['_ADAPTATION']._serialized_end = 3657