"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/speech/v1p1beta1/cloud_speech_adaptation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.speech.v1p1beta1 import resource_pb2 as google_dot_cloud_dot_speech_dot_v1p1beta1_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/cloud/speech/v1p1beta1/cloud_speech_adaptation.proto\x12\x1dgoogle.cloud.speech.v1p1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/speech/v1p1beta1/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xb0\x01\n\x16CreatePhraseSetRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fspeech.googleapis.com/PhraseSet\x12\x1a\n\rphrase_set_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12A\n\nphrase_set\x18\x03 \x01(\x0b2(.google.cloud.speech.v1p1beta1.PhraseSetB\x03\xe0A\x02"\x8c\x01\n\x16UpdatePhraseSetRequest\x12A\n\nphrase_set\x18\x01 \x01(\x0b2(.google.cloud.speech.v1p1beta1.PhraseSetB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"L\n\x13GetPhraseSetRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspeech.googleapis.com/PhraseSet"v\n\x14ListPhraseSetRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fspeech.googleapis.com/PhraseSet\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"o\n\x15ListPhraseSetResponse\x12=\n\x0bphrase_sets\x18\x01 \x03(\x0b2(.google.cloud.speech.v1p1beta1.PhraseSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"O\n\x16DeletePhraseSetRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspeech.googleapis.com/PhraseSet"\xba\x01\n\x18CreateCustomClassRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!speech.googleapis.com/CustomClass\x12\x1c\n\x0fcustom_class_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12E\n\x0ccustom_class\x18\x03 \x01(\x0b2*.google.cloud.speech.v1p1beta1.CustomClassB\x03\xe0A\x02"\x92\x01\n\x18UpdateCustomClassRequest\x12E\n\x0ccustom_class\x18\x01 \x01(\x0b2*.google.cloud.speech.v1p1beta1.CustomClassB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"P\n\x15GetCustomClassRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!speech.googleapis.com/CustomClass"|\n\x18ListCustomClassesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!speech.googleapis.com/CustomClass\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"x\n\x19ListCustomClassesResponse\x12B\n\x0ecustom_classes\x18\x01 \x03(\x0b2*.google.cloud.speech.v1p1beta1.CustomClass\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"S\n\x18DeleteCustomClassRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!speech.googleapis.com/CustomClass2\xd2\x10\n\nAdaptation\x12\xd6\x01\n\x0fCreatePhraseSet\x125.google.cloud.speech.v1p1beta1.CreatePhraseSetRequest\x1a(.google.cloud.speech.v1p1beta1.PhraseSet"b\xdaA\x1fparent,phrase_set,phrase_set_id\x82\xd3\xe4\x93\x02:"5/v1p1beta1/{parent=projects/*/locations/*}/phraseSets:\x01*\x12\xb2\x01\n\x0cGetPhraseSet\x122.google.cloud.speech.v1p1beta1.GetPhraseSetRequest\x1a(.google.cloud.speech.v1p1beta1.PhraseSet"D\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v1p1beta1/{name=projects/*/locations/*/phraseSets/*}\x12\xc2\x01\n\rListPhraseSet\x123.google.cloud.speech.v1p1beta1.ListPhraseSetRequest\x1a4.google.cloud.speech.v1p1beta1.ListPhraseSetResponse"F\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v1p1beta1/{parent=projects/*/locations/*}/phraseSets\x12\xe1\x01\n\x0fUpdatePhraseSet\x125.google.cloud.speech.v1p1beta1.UpdatePhraseSetRequest\x1a(.google.cloud.speech.v1p1beta1.PhraseSet"m\xdaA\x16phrase_set,update_mask\x82\xd3\xe4\x93\x02N2@/v1p1beta1/{phrase_set.name=projects/*/locations/*/phraseSets/*}:\nphrase_set\x12\xa6\x01\n\x0fDeletePhraseSet\x125.google.cloud.speech.v1p1beta1.DeletePhraseSetRequest\x1a\x16.google.protobuf.Empty"D\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v1p1beta1/{name=projects/*/locations/*/phraseSets/*}\x12\xe3\x01\n\x11CreateCustomClass\x127.google.cloud.speech.v1p1beta1.CreateCustomClassRequest\x1a*.google.cloud.speech.v1p1beta1.CustomClass"i\xdaA#parent,custom_class,custom_class_id\x82\xd3\xe4\x93\x02="8/v1p1beta1/{parent=projects/*/locations/*}/customClasses:\x01*\x12\xbb\x01\n\x0eGetCustomClass\x124.google.cloud.speech.v1p1beta1.GetCustomClassRequest\x1a*.google.cloud.speech.v1p1beta1.CustomClass"G\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/v1p1beta1/{name=projects/*/locations/*/customClasses/*}\x12\xd1\x01\n\x11ListCustomClasses\x127.google.cloud.speech.v1p1beta1.ListCustomClassesRequest\x1a8.google.cloud.speech.v1p1beta1.ListCustomClassesResponse"I\xdaA\x06parent\x82\xd3\xe4\x93\x02:\x128/v1p1beta1/{parent=projects/*/locations/*}/customClasses\x12\xf0\x01\n\x11UpdateCustomClass\x127.google.cloud.speech.v1p1beta1.UpdateCustomClassRequest\x1a*.google.cloud.speech.v1p1beta1.CustomClass"v\xdaA\x18custom_class,update_mask\x82\xd3\xe4\x93\x02U2E/v1p1beta1/{custom_class.name=projects/*/locations/*/customClasses/*}:\x0ccustom_class\x12\xad\x01\n\x11DeleteCustomClass\x127.google.cloud.speech.v1p1beta1.DeleteCustomClassRequest\x1a\x16.google.protobuf.Empty"G\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v1p1beta1/{name=projects/*/locations/*/customClasses/*}\x1aI\xcaA\x15speech.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x80\x01\n!com.google.cloud.speech.v1p1beta1B\x15SpeechAdaptationProtoP\x01Z9cloud.google.com/go/speech/apiv1p1beta1/speechpb;speechpb\xf8\x01\x01\xa2\x02\x03GCSb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.speech.v1p1beta1.cloud_speech_adaptation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.speech.v1p1beta1B\x15SpeechAdaptationProtoP\x01Z9cloud.google.com/go/speech/apiv1p1beta1/speechpb;speechpb\xf8\x01\x01\xa2\x02\x03GCS'
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
    _globals['_ADAPTATION'].methods_by_name['CreatePhraseSet']._serialized_options = b'\xdaA\x1fparent,phrase_set,phrase_set_id\x82\xd3\xe4\x93\x02:"5/v1p1beta1/{parent=projects/*/locations/*}/phraseSets:\x01*'
    _globals['_ADAPTATION'].methods_by_name['GetPhraseSet']._loaded_options = None
    _globals['_ADAPTATION'].methods_by_name['GetPhraseSet']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v1p1beta1/{name=projects/*/locations/*/phraseSets/*}'
    _globals['_ADAPTATION'].methods_by_name['ListPhraseSet']._loaded_options = None
    _globals['_ADAPTATION'].methods_by_name['ListPhraseSet']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v1p1beta1/{parent=projects/*/locations/*}/phraseSets'
    _globals['_ADAPTATION'].methods_by_name['UpdatePhraseSet']._loaded_options = None
    _globals['_ADAPTATION'].methods_by_name['UpdatePhraseSet']._serialized_options = b'\xdaA\x16phrase_set,update_mask\x82\xd3\xe4\x93\x02N2@/v1p1beta1/{phrase_set.name=projects/*/locations/*/phraseSets/*}:\nphrase_set'
    _globals['_ADAPTATION'].methods_by_name['DeletePhraseSet']._loaded_options = None
    _globals['_ADAPTATION'].methods_by_name['DeletePhraseSet']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v1p1beta1/{name=projects/*/locations/*/phraseSets/*}'
    _globals['_ADAPTATION'].methods_by_name['CreateCustomClass']._loaded_options = None
    _globals['_ADAPTATION'].methods_by_name['CreateCustomClass']._serialized_options = b'\xdaA#parent,custom_class,custom_class_id\x82\xd3\xe4\x93\x02="8/v1p1beta1/{parent=projects/*/locations/*}/customClasses:\x01*'
    _globals['_ADAPTATION'].methods_by_name['GetCustomClass']._loaded_options = None
    _globals['_ADAPTATION'].methods_by_name['GetCustomClass']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/v1p1beta1/{name=projects/*/locations/*/customClasses/*}'
    _globals['_ADAPTATION'].methods_by_name['ListCustomClasses']._loaded_options = None
    _globals['_ADAPTATION'].methods_by_name['ListCustomClasses']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02:\x128/v1p1beta1/{parent=projects/*/locations/*}/customClasses'
    _globals['_ADAPTATION'].methods_by_name['UpdateCustomClass']._loaded_options = None
    _globals['_ADAPTATION'].methods_by_name['UpdateCustomClass']._serialized_options = b'\xdaA\x18custom_class,update_mask\x82\xd3\xe4\x93\x02U2E/v1p1beta1/{custom_class.name=projects/*/locations/*/customClasses/*}:\x0ccustom_class'
    _globals['_ADAPTATION'].methods_by_name['DeleteCustomClass']._loaded_options = None
    _globals['_ADAPTATION'].methods_by_name['DeleteCustomClass']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v1p1beta1/{name=projects/*/locations/*/customClasses/*}'
    _globals['_CREATEPHRASESETREQUEST']._serialized_start = 319
    _globals['_CREATEPHRASESETREQUEST']._serialized_end = 495
    _globals['_UPDATEPHRASESETREQUEST']._serialized_start = 498
    _globals['_UPDATEPHRASESETREQUEST']._serialized_end = 638
    _globals['_GETPHRASESETREQUEST']._serialized_start = 640
    _globals['_GETPHRASESETREQUEST']._serialized_end = 716
    _globals['_LISTPHRASESETREQUEST']._serialized_start = 718
    _globals['_LISTPHRASESETREQUEST']._serialized_end = 836
    _globals['_LISTPHRASESETRESPONSE']._serialized_start = 838
    _globals['_LISTPHRASESETRESPONSE']._serialized_end = 949
    _globals['_DELETEPHRASESETREQUEST']._serialized_start = 951
    _globals['_DELETEPHRASESETREQUEST']._serialized_end = 1030
    _globals['_CREATECUSTOMCLASSREQUEST']._serialized_start = 1033
    _globals['_CREATECUSTOMCLASSREQUEST']._serialized_end = 1219
    _globals['_UPDATECUSTOMCLASSREQUEST']._serialized_start = 1222
    _globals['_UPDATECUSTOMCLASSREQUEST']._serialized_end = 1368
    _globals['_GETCUSTOMCLASSREQUEST']._serialized_start = 1370
    _globals['_GETCUSTOMCLASSREQUEST']._serialized_end = 1450
    _globals['_LISTCUSTOMCLASSESREQUEST']._serialized_start = 1452
    _globals['_LISTCUSTOMCLASSESREQUEST']._serialized_end = 1576
    _globals['_LISTCUSTOMCLASSESRESPONSE']._serialized_start = 1578
    _globals['_LISTCUSTOMCLASSESRESPONSE']._serialized_end = 1698
    _globals['_DELETECUSTOMCLASSREQUEST']._serialized_start = 1700
    _globals['_DELETECUSTOMCLASSREQUEST']._serialized_end = 1783
    _globals['_ADAPTATION']._serialized_start = 1786
    _globals['_ADAPTATION']._serialized_end = 3916