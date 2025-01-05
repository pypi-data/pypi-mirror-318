"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/retail/v2alpha/generative_question_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2alpha import generative_question_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_generative__question__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/retail/v2alpha/generative_question_service.proto\x12\x1bgoogle.cloud.retail.v2alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/retail/v2alpha/generative_question.proto\x1a google/protobuf/field_mask.proto"\xd6\x01\n-UpdateGenerativeQuestionsFeatureConfigRequest\x12o\n#generative_questions_feature_config\x18\x02 \x01(\x0b2=.google.cloud.retail.v2alpha.GenerativeQuestionsFeatureConfigB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"d\n*GetGenerativeQuestionsFeatureConfigRequest\x126\n\x07catalog\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog"]\n$ListGenerativeQuestionConfigsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog"\x83\x01\n%ListGenerativeQuestionConfigsResponse\x12Z\n\x1bgenerative_question_configs\x18\x01 \x03(\x0b25.google.cloud.retail.v2alpha.GenerativeQuestionConfig"\xbd\x01\n%UpdateGenerativeQuestionConfigRequest\x12^\n\x1agenerative_question_config\x18\x03 \x01(\x0b25.google.cloud.retail.v2alpha.GenerativeQuestionConfigB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\xbf\x01\n+BatchUpdateGenerativeQuestionConfigsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x01\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12Y\n\x08requests\x18\x02 \x03(\x0b2B.google.cloud.retail.v2alpha.UpdateGenerativeQuestionConfigRequestB\x03\xe0A\x02"\x8f\x01\n,BatchUpdateGenerativeQuestionConfigsResponse\x12_\n\x1bgenerative_question_configs\x18\x01 \x03(\x0b25.google.cloud.retail.v2alpha.GenerativeQuestionConfigB\x03\xe0A\x012\x86\r\n\x19GenerativeQuestionService\x12\x88\x03\n&UpdateGenerativeQuestionsFeatureConfig\x12J.google.cloud.retail.v2alpha.UpdateGenerativeQuestionsFeatureConfigRequest\x1a=.google.cloud.retail.v2alpha.GenerativeQuestionsFeatureConfig"\xd2\x01\xdaA/generative_questions_feature_config,update_mask\x82\xd3\xe4\x93\x02\x99\x012r/v2alpha/{generative_questions_feature_config.catalog=projects/*/locations/*/catalogs/*}/generativeQuestionFeature:#generative_questions_feature_config\x12\x8f\x02\n#GetGenerativeQuestionsFeatureConfig\x12G.google.cloud.retail.v2alpha.GetGenerativeQuestionsFeatureConfigRequest\x1a=.google.cloud.retail.v2alpha.GenerativeQuestionsFeatureConfig"`\xdaA\x07catalog\x82\xd3\xe4\x93\x02P\x12N/v2alpha/{catalog=projects/*/locations/*/catalogs/*}/generativeQuestionFeature\x12\x80\x02\n\x1dListGenerativeQuestionConfigs\x12A.google.cloud.retail.v2alpha.ListGenerativeQuestionConfigsRequest\x1aB.google.cloud.retail.v2alpha.ListGenerativeQuestionConfigsResponse"X\xdaA\x06parent\x82\xd3\xe4\x93\x02I\x12G/v2alpha/{parent=projects/*/locations/*/catalogs/*}/generativeQuestions\x12\xce\x02\n\x1eUpdateGenerativeQuestionConfig\x12B.google.cloud.retail.v2alpha.UpdateGenerativeQuestionConfigRequest\x1a5.google.cloud.retail.v2alpha.GenerativeQuestionConfig"\xb0\x01\xdaA&generative_question_config,update_mask\x82\xd3\xe4\x93\x02\x80\x012b/v2alpha/{generative_question_config.catalog=projects/*/locations/*/catalogs/*}/generativeQuestion:\x1agenerative_question_config\x12\xac\x02\n$BatchUpdateGenerativeQuestionConfigs\x12H.google.cloud.retail.v2alpha.BatchUpdateGenerativeQuestionConfigsRequest\x1aI.google.cloud.retail.v2alpha.BatchUpdateGenerativeQuestionConfigsResponse"o\xdaA\x0fparent,requests\x82\xd3\xe4\x93\x02W"R/v2alpha/{parent=projects/*/locations/*/catalogs/*}/generativeQuestion:batchUpdate:\x01*\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe2\x01\n\x1fcom.google.cloud.retail.v2alphaB\x1eGenerativeQuestionServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2alpha.generative_question_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.retail.v2alphaB\x1eGenerativeQuestionServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alpha'
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
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['UpdateGenerativeQuestionsFeatureConfig']._serialized_options = b'\xdaA/generative_questions_feature_config,update_mask\x82\xd3\xe4\x93\x02\x99\x012r/v2alpha/{generative_questions_feature_config.catalog=projects/*/locations/*/catalogs/*}/generativeQuestionFeature:#generative_questions_feature_config'
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['GetGenerativeQuestionsFeatureConfig']._loaded_options = None
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['GetGenerativeQuestionsFeatureConfig']._serialized_options = b'\xdaA\x07catalog\x82\xd3\xe4\x93\x02P\x12N/v2alpha/{catalog=projects/*/locations/*/catalogs/*}/generativeQuestionFeature'
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['ListGenerativeQuestionConfigs']._loaded_options = None
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['ListGenerativeQuestionConfigs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02I\x12G/v2alpha/{parent=projects/*/locations/*/catalogs/*}/generativeQuestions'
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['UpdateGenerativeQuestionConfig']._loaded_options = None
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['UpdateGenerativeQuestionConfig']._serialized_options = b'\xdaA&generative_question_config,update_mask\x82\xd3\xe4\x93\x02\x80\x012b/v2alpha/{generative_question_config.catalog=projects/*/locations/*/catalogs/*}/generativeQuestion:\x1agenerative_question_config'
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['BatchUpdateGenerativeQuestionConfigs']._loaded_options = None
    _globals['_GENERATIVEQUESTIONSERVICE'].methods_by_name['BatchUpdateGenerativeQuestionConfigs']._serialized_options = b'\xdaA\x0fparent,requests\x82\xd3\xe4\x93\x02W"R/v2alpha/{parent=projects/*/locations/*/catalogs/*}/generativeQuestion:batchUpdate:\x01*'
    _globals['_UPDATEGENERATIVEQUESTIONSFEATURECONFIGREQUEST']._serialized_start = 299
    _globals['_UPDATEGENERATIVEQUESTIONSFEATURECONFIGREQUEST']._serialized_end = 513
    _globals['_GETGENERATIVEQUESTIONSFEATURECONFIGREQUEST']._serialized_start = 515
    _globals['_GETGENERATIVEQUESTIONSFEATURECONFIGREQUEST']._serialized_end = 615
    _globals['_LISTGENERATIVEQUESTIONCONFIGSREQUEST']._serialized_start = 617
    _globals['_LISTGENERATIVEQUESTIONCONFIGSREQUEST']._serialized_end = 710
    _globals['_LISTGENERATIVEQUESTIONCONFIGSRESPONSE']._serialized_start = 713
    _globals['_LISTGENERATIVEQUESTIONCONFIGSRESPONSE']._serialized_end = 844
    _globals['_UPDATEGENERATIVEQUESTIONCONFIGREQUEST']._serialized_start = 847
    _globals['_UPDATEGENERATIVEQUESTIONCONFIGREQUEST']._serialized_end = 1036
    _globals['_BATCHUPDATEGENERATIVEQUESTIONCONFIGSREQUEST']._serialized_start = 1039
    _globals['_BATCHUPDATEGENERATIVEQUESTIONCONFIGSREQUEST']._serialized_end = 1230
    _globals['_BATCHUPDATEGENERATIVEQUESTIONCONFIGSRESPONSE']._serialized_start = 1233
    _globals['_BATCHUPDATEGENERATIVEQUESTIONCONFIGSRESPONSE']._serialized_end = 1376
    _globals['_GENERATIVEQUESTIONSERVICE']._serialized_start = 1379
    _globals['_GENERATIVEQUESTIONSERVICE']._serialized_end = 3049