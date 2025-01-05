"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/retail/v2/generative_question_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2 import generative_question_pb2 as google_dot_cloud_dot_retail_dot_v2_dot_generative__question__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/retail/v2/generative_question_service.proto\x12\x16google.cloud.retail.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/retail/v2/generative_question.proto\x1a google/protobuf/field_mask.proto"\xd1\x01\n-UpdateGenerativeQuestionsFeatureConfigRequest\x12j\n#generative_questions_feature_config\x18\x02 \x01(\x0b28.google.cloud.retail.v2.GenerativeQuestionsFeatureConfigB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"d\n*GetGenerativeQuestionsFeatureConfigRequest\x126\n\x07catalog\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog"]\n$ListGenerativeQuestionConfigsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog"~\n%ListGenerativeQuestionConfigsResponse\x12U\n\x1bgenerative_question_configs\x18\x01 \x03(\x0b20.google.cloud.retail.v2.GenerativeQuestionConfig"\xb8\x01\n%UpdateGenerativeQuestionConfigRequest\x12Y\n\x1agenerative_question_config\x18\x03 \x01(\x0b20.google.cloud.retail.v2.GenerativeQuestionConfigB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\xba\x01\n+BatchUpdateGenerativeQuestionConfigsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x01\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12T\n\x08requests\x18\x02 \x03(\x0b2=.google.cloud.retail.v2.UpdateGenerativeQuestionConfigRequestB\x03\xe0A\x02"\x8a\x01\n,BatchUpdateGenerativeQuestionConfigsResponse\x12Z\n\x1bgenerative_question_configs\x18\x01 \x03(\x0b20.google.cloud.retail.v2.GenerativeQuestionConfigB\x03\xe0A\x012\xba\x0c\n\x19GenerativeQuestionService\x12\xf9\x02\n&UpdateGenerativeQuestionsFeatureConfig\x12E.google.cloud.retail.v2.UpdateGenerativeQuestionsFeatureConfigRequest\x1a8.google.cloud.retail.v2.GenerativeQuestionsFeatureConfig"\xcd\x01\xdaA/generative_questions_feature_config,update_mask\x82\xd3\xe4\x93\x02\x94\x012m/v2/{generative_questions_feature_config.catalog=projects/*/locations/*/catalogs/*}/generativeQuestionFeature:#generative_questions_feature_config\x12\x80\x02\n#GetGenerativeQuestionsFeatureConfig\x12B.google.cloud.retail.v2.GetGenerativeQuestionsFeatureConfigRequest\x1a8.google.cloud.retail.v2.GenerativeQuestionsFeatureConfig"[\xdaA\x07catalog\x82\xd3\xe4\x93\x02K\x12I/v2/{catalog=projects/*/locations/*/catalogs/*}/generativeQuestionFeature\x12\xf1\x01\n\x1dListGenerativeQuestionConfigs\x12<.google.cloud.retail.v2.ListGenerativeQuestionConfigsRequest\x1a=.google.cloud.retail.v2.ListGenerativeQuestionConfigsResponse"S\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/v2/{parent=projects/*/locations/*/catalogs/*}/generativeQuestions\x12\xbe\x02\n\x1eUpdateGenerativeQuestionConfig\x12=.google.cloud.retail.v2.UpdateGenerativeQuestionConfigRequest\x1a0.google.cloud.retail.v2.GenerativeQuestionConfig"\xaa\x01\xdaA&generative_question_config,update_mask\x82\xd3\xe4\x93\x02{2]/v2/{generative_question_config.catalog=projects/*/locations/*/catalogs/*}/generativeQuestion:\x1agenerative_question_config\x12\x9d\x02\n$BatchUpdateGenerativeQuestionConfigs\x12C.google.cloud.retail.v2.BatchUpdateGenerativeQuestionConfigsRequest\x1aD.google.cloud.retail.v2.BatchUpdateGenerativeQuestionConfigsResponse"j\xdaA\x0fparent,requests\x82\xd3\xe4\x93\x02R"M/v2/{parent=projects/*/locations/*/catalogs/*}/generativeQuestion:batchUpdate:\x01*\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xc9\x01\n\x1acom.google.cloud.retail.v2B\x1eGenerativeQuestionServiceProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2.generative_question_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.retail.v2B\x1eGenerativeQuestionServiceProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2'
    _globals['_UPDATEGENERATIVEQUESTIONSFEATURECONFIGREQUEST'].fields_by_name['generative_questions_feature_config']._loaded_options = None
    _globals['_UPDATEGENERATIVEQUESTIONSFEATURECONFIGREQUEST'].fields_by_name['generative_questions_feature_config']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEGENERATIVEQUESTIONSFEATURECONFIGREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEGENERATIVEQUESTIONSFEATURECONFIGREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_GETGENERATIVEQUESTIONSFEATURECONFIGREQUEST'].fields_by_name['catalog']._loaded_options = None
    _globals['_GETGENERATIVEQUESTIONSFEATURECONFIGREQUEST'].fields_by_name['catalog']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog'
    _globals['_LISTGENERATIVEQUESTIONCONFIGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTGENERATIVEQUESTIONCONFIGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog'
    _globals['_UPDATEGENERATIVEQUESTIONCONFIGREQUEST'].fields_by_name['generative_question_config']._loaded_options = None
    _globals['_UPDATEGENERATIVEQUESTIONCONFIGREQUEST'].fields_by_name['generative_question_config']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEGENERATIVEQUESTIONCONFIGREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEGENERATIVEQUESTIONCONFIGREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHUPDATEGENERATIVEQUESTIONCONFIGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHUPDATEGENERATIVEQUESTIONCONFIGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x01\xfaA\x1f\n\x1dretail.googleapis.com/Catalog'
    _globals['_BATCHUPDATEGENERATIVEQUESTIONCONFIGSREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_BATCHUPDATEGENERATIVEQUESTIONCONFIGSREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHUPDATEGENERATIVEQUESTIONCONFIGSRESPONSE'].fields_by_name['generative_question_configs']._loaded_options = None
    _globals['_BATCHUPDATEGENERATIVEQUESTIONCONFIGSRESPONSE'].fields_by_name['generative_question_configs']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATIVEQUESTIONSERVICE']._loaded_options = None
    _globals['_GENERATIVEQUESTIONSERVICE']._serialized_options = b'\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['UpdateGenerativeQuestionsFeatureConfig']._loaded_options = None
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['UpdateGenerativeQuestionsFeatureConfig']._serialized_options = b'\xdaA/generative_questions_feature_config,update_mask\x82\xd3\xe4\x93\x02\x94\x012m/v2/{generative_questions_feature_config.catalog=projects/*/locations/*/catalogs/*}/generativeQuestionFeature:#generative_questions_feature_config'
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['GetGenerativeQuestionsFeatureConfig']._loaded_options = None
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['GetGenerativeQuestionsFeatureConfig']._serialized_options = b'\xdaA\x07catalog\x82\xd3\xe4\x93\x02K\x12I/v2/{catalog=projects/*/locations/*/catalogs/*}/generativeQuestionFeature'
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['ListGenerativeQuestionConfigs']._loaded_options = None
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['ListGenerativeQuestionConfigs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/v2/{parent=projects/*/locations/*/catalogs/*}/generativeQuestions'
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['UpdateGenerativeQuestionConfig']._loaded_options = None
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['UpdateGenerativeQuestionConfig']._serialized_options = b'\xdaA&generative_question_config,update_mask\x82\xd3\xe4\x93\x02{2]/v2/{generative_question_config.catalog=projects/*/locations/*/catalogs/*}/generativeQuestion:\x1agenerative_question_config'
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['BatchUpdateGenerativeQuestionConfigs']._loaded_options = None
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['BatchUpdateGenerativeQuestionConfigs']._serialized_options = b'\xdaA\x0fparent,requests\x82\xd3\xe4\x93\x02R"M/v2/{parent=projects/*/locations/*/catalogs/*}/generativeQuestion:batchUpdate:\x01*'
    _globals['_UPDATEGENERATIVEQUESTIONSFEATURECONFIGREQUEST']._serialized_start = 284
    _globals['_UPDATEGENERATIVEQUESTIONSFEATURECONFIGREQUEST']._serialized_end = 493
    _globals['_GETGENERATIVEQUESTIONSFEATURECONFIGREQUEST']._serialized_start = 495
    _globals['_GETGENERATIVEQUESTIONSFEATURECONFIGREQUEST']._serialized_end = 595
    _globals['_LISTGENERATIVEQUESTIONCONFIGSREQUEST']._serialized_start = 597
    _globals['_LISTGENERATIVEQUESTIONCONFIGSREQUEST']._serialized_end = 690
    _globals['_LISTGENERATIVEQUESTIONCONFIGSRESPONSE']._serialized_start = 692
    _globals['_LISTGENERATIVEQUESTIONCONFIGSRESPONSE']._serialized_end = 818
    _globals['_UPDATEGENERATIVEQUESTIONCONFIGREQUEST']._serialized_start = 821
    _globals['_UPDATEGENERATIVEQUESTIONCONFIGREQUEST']._serialized_end = 1005
    _globals['_BATCHUPDATEGENERATIVEQUESTIONCONFIGSREQUEST']._serialized_start = 1008
    _globals['_BATCHUPDATEGENERATIVEQUESTIONCONFIGSREQUEST']._serialized_end = 1194
    _globals['_BATCHUPDATEGENERATIVEQUESTIONCONFIGSRESPONSE']._serialized_start = 1197
    _globals['_BATCHUPDATEGENERATIVEQUESTIONCONFIGSRESPONSE']._serialized_end = 1335
    _globals['_GENERATIVEQUESTIONSERVICE']._serialized_start = 1338
    _globals['_GENERATIVEQUESTIONSERVICE']._serialized_end = 2932