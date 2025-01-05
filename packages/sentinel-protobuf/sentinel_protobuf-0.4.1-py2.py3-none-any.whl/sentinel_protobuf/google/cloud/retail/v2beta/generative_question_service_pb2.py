"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/retail/v2beta/generative_question_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2beta import generative_question_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_generative__question__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/retail/v2beta/generative_question_service.proto\x12\x1agoogle.cloud.retail.v2beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a4google/cloud/retail/v2beta/generative_question.proto\x1a google/protobuf/field_mask.proto"\xd5\x01\n-UpdateGenerativeQuestionsFeatureConfigRequest\x12n\n#generative_questions_feature_config\x18\x02 \x01(\x0b2<.google.cloud.retail.v2beta.GenerativeQuestionsFeatureConfigB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"d\n*GetGenerativeQuestionsFeatureConfigRequest\x126\n\x07catalog\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog"]\n$ListGenerativeQuestionConfigsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog"\x82\x01\n%ListGenerativeQuestionConfigsResponse\x12Y\n\x1bgenerative_question_configs\x18\x01 \x03(\x0b24.google.cloud.retail.v2beta.GenerativeQuestionConfig"\xbc\x01\n%UpdateGenerativeQuestionConfigRequest\x12]\n\x1agenerative_question_config\x18\x03 \x01(\x0b24.google.cloud.retail.v2beta.GenerativeQuestionConfigB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\xbe\x01\n+BatchUpdateGenerativeQuestionConfigsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x01\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12X\n\x08requests\x18\x02 \x03(\x0b2A.google.cloud.retail.v2beta.UpdateGenerativeQuestionConfigRequestB\x03\xe0A\x02"\x8e\x01\n,BatchUpdateGenerativeQuestionConfigsResponse\x12^\n\x1bgenerative_question_configs\x18\x01 \x03(\x0b24.google.cloud.retail.v2beta.GenerativeQuestionConfigB\x03\xe0A\x012\xf6\x0c\n\x19GenerativeQuestionService\x12\x85\x03\n&UpdateGenerativeQuestionsFeatureConfig\x12I.google.cloud.retail.v2beta.UpdateGenerativeQuestionsFeatureConfigRequest\x1a<.google.cloud.retail.v2beta.GenerativeQuestionsFeatureConfig"\xd1\x01\xdaA/generative_questions_feature_config,update_mask\x82\xd3\xe4\x93\x02\x98\x012q/v2beta/{generative_questions_feature_config.catalog=projects/*/locations/*/catalogs/*}/generativeQuestionFeature:#generative_questions_feature_config\x12\x8c\x02\n#GetGenerativeQuestionsFeatureConfig\x12F.google.cloud.retail.v2beta.GetGenerativeQuestionsFeatureConfigRequest\x1a<.google.cloud.retail.v2beta.GenerativeQuestionsFeatureConfig"_\xdaA\x07catalog\x82\xd3\xe4\x93\x02O\x12M/v2beta/{catalog=projects/*/locations/*/catalogs/*}/generativeQuestionFeature\x12\xfd\x01\n\x1dListGenerativeQuestionConfigs\x12@.google.cloud.retail.v2beta.ListGenerativeQuestionConfigsRequest\x1aA.google.cloud.retail.v2beta.ListGenerativeQuestionConfigsResponse"W\xdaA\x06parent\x82\xd3\xe4\x93\x02H\x12F/v2beta/{parent=projects/*/locations/*/catalogs/*}/generativeQuestions\x12\xca\x02\n\x1eUpdateGenerativeQuestionConfig\x12A.google.cloud.retail.v2beta.UpdateGenerativeQuestionConfigRequest\x1a4.google.cloud.retail.v2beta.GenerativeQuestionConfig"\xae\x01\xdaA&generative_question_config,update_mask\x82\xd3\xe4\x93\x02\x7f2a/v2beta/{generative_question_config.catalog=projects/*/locations/*/catalogs/*}/generativeQuestion:\x1agenerative_question_config\x12\xa9\x02\n$BatchUpdateGenerativeQuestionConfigs\x12G.google.cloud.retail.v2beta.BatchUpdateGenerativeQuestionConfigsRequest\x1aH.google.cloud.retail.v2beta.BatchUpdateGenerativeQuestionConfigsResponse"n\xdaA\x0fparent,requests\x82\xd3\xe4\x93\x02V"Q/v2beta/{parent=projects/*/locations/*/catalogs/*}/generativeQuestion:batchUpdate:\x01*\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xdd\x01\n\x1ecom.google.cloud.retail.v2betaB\x1eGenerativeQuestionServiceProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2beta.generative_question_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.retail.v2betaB\x1eGenerativeQuestionServiceProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2beta'
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
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['UpdateGenerativeQuestionsFeatureConfig']._serialized_options = b'\xdaA/generative_questions_feature_config,update_mask\x82\xd3\xe4\x93\x02\x98\x012q/v2beta/{generative_questions_feature_config.catalog=projects/*/locations/*/catalogs/*}/generativeQuestionFeature:#generative_questions_feature_config'
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['GetGenerativeQuestionsFeatureConfig']._loaded_options = None
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['GetGenerativeQuestionsFeatureConfig']._serialized_options = b'\xdaA\x07catalog\x82\xd3\xe4\x93\x02O\x12M/v2beta/{catalog=projects/*/locations/*/catalogs/*}/generativeQuestionFeature'
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['ListGenerativeQuestionConfigs']._loaded_options = None
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['ListGenerativeQuestionConfigs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02H\x12F/v2beta/{parent=projects/*/locations/*/catalogs/*}/generativeQuestions'
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['UpdateGenerativeQuestionConfig']._loaded_options = None
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['UpdateGenerativeQuestionConfig']._serialized_options = b'\xdaA&generative_question_config,update_mask\x82\xd3\xe4\x93\x02\x7f2a/v2beta/{generative_question_config.catalog=projects/*/locations/*/catalogs/*}/generativeQuestion:\x1agenerative_question_config'
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['BatchUpdateGenerativeQuestionConfigs']._loaded_options = None
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['BatchUpdateGenerativeQuestionConfigs']._serialized_options = b'\xdaA\x0fparent,requests\x82\xd3\xe4\x93\x02V"Q/v2beta/{parent=projects/*/locations/*/catalogs/*}/generativeQuestion:batchUpdate:\x01*'
    _globals['_UPDATEGENERATIVEQUESTIONSFEATURECONFIGREQUEST']._serialized_start = 296
    _globals['_UPDATEGENERATIVEQUESTIONSFEATURECONFIGREQUEST']._serialized_end = 509
    _globals['_GETGENERATIVEQUESTIONSFEATURECONFIGREQUEST']._serialized_start = 511
    _globals['_GETGENERATIVEQUESTIONSFEATURECONFIGREQUEST']._serialized_end = 611
    _globals['_LISTGENERATIVEQUESTIONCONFIGSREQUEST']._serialized_start = 613
    _globals['_LISTGENERATIVEQUESTIONCONFIGSREQUEST']._serialized_end = 706
    _globals['_LISTGENERATIVEQUESTIONCONFIGSRESPONSE']._serialized_start = 709
    _globals['_LISTGENERATIVEQUESTIONCONFIGSRESPONSE']._serialized_end = 839
    _globals['_UPDATEGENERATIVEQUESTIONCONFIGREQUEST']._serialized_start = 842
    _globals['_UPDATEGENERATIVEQUESTIONCONFIGREQUEST']._serialized_end = 1030
    _globals['_BATCHUPDATEGENERATIVEQUESTIONCONFIGSREQUEST']._serialized_start = 1033
    _globals['_BATCHUPDATEGENERATIVEQUESTIONCONFIGSREQUEST']._serialized_end = 1223
    _globals['_BATCHUPDATEGENERATIVEQUESTIONCONFIGSRESPONSE']._serialized_start = 1226
    _globals['_BATCHUPDATEGENERATIVEQUESTIONCONFIGSRESPONSE']._serialized_end = 1368
    _globals['_GENERATIVEQUESTIONSERVICE']._serialized_start = 1371
    _globals['_GENERATIVEQUESTIONSERVICE']._serialized_end = 3025