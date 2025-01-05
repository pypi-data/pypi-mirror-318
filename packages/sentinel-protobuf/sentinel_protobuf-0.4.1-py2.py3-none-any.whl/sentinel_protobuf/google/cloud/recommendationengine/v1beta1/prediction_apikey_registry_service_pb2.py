"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/recommendationengine/v1beta1/prediction_apikey_registry_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.cloud.recommendationengine.v1beta1 import recommendationengine_resources_pb2 as google_dot_cloud_dot_recommendationengine_dot_v1beta1_dot_recommendationengine__resources__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nRgoogle/cloud/recommendationengine/v1beta1/prediction_apikey_registry_service.proto\x12)google.cloud.recommendationengine.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x17google/api/client.proto\x1aNgoogle/cloud/recommendationengine/v1beta1/recommendationengine_resources.proto"/\n\x1cPredictionApiKeyRegistration\x12\x0f\n\x07api_key\x18\x01 \x01(\t"\xea\x01\n)CreatePredictionApiKeyRegistrationRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.recommendationengine.googleapis.com/EventStore\x12u\n\x1fprediction_api_key_registration\x18\x02 \x01(\x0b2G.google.cloud.recommendationengine.v1beta1.PredictionApiKeyRegistrationB\x03\xe0A\x02"\xa3\x01\n(ListPredictionApiKeyRegistrationsRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.recommendationengine.googleapis.com/EventStore\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\xb7\x01\n)ListPredictionApiKeyRegistrationsResponse\x12q\n prediction_api_key_registrations\x18\x01 \x03(\x0b2G.google.cloud.recommendationengine.v1beta1.PredictionApiKeyRegistration\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x83\x01\n)DeletePredictionApiKeyRegistrationRequest\x12V\n\x04name\x18\x01 \x01(\tBH\xe0A\x02\xfaAB\n@recommendationengine.googleapis.com/PredictionApiKeyRegistration2\x97\x08\n\x18PredictionApiKeyRegistry\x12\xd9\x02\n"CreatePredictionApiKeyRegistration\x12T.google.cloud.recommendationengine.v1beta1.CreatePredictionApiKeyRegistrationRequest\x1aG.google.cloud.recommendationengine.v1beta1.PredictionApiKeyRegistration"\x93\x01\xdaA&parent,prediction_api_key_registration\x82\xd3\xe4\x93\x02d"_/v1beta1/{parent=projects/*/locations/*/catalogs/*/eventStores/*}/predictionApiKeyRegistrations:\x01*\x12\xc0\x02\n!ListPredictionApiKeyRegistrations\x12S.google.cloud.recommendationengine.v1beta1.ListPredictionApiKeyRegistrationsRequest\x1aT.google.cloud.recommendationengine.v1beta1.ListPredictionApiKeyRegistrationsResponse"p\xdaA\x06parent\x82\xd3\xe4\x93\x02a\x12_/v1beta1/{parent=projects/*/locations/*/catalogs/*/eventStores/*}/predictionApiKeyRegistrations\x12\x82\x02\n"DeletePredictionApiKeyRegistration\x12T.google.cloud.recommendationengine.v1beta1.DeletePredictionApiKeyRegistrationRequest\x1a\x16.google.protobuf.Empty"n\xdaA\x04name\x82\xd3\xe4\x93\x02a*_/v1beta1/{name=projects/*/locations/*/catalogs/*/eventStores/*/predictionApiKeyRegistrations/*}\x1aW\xcaA#recommendationengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa3\x02\n-com.google.cloud.recommendationengine.v1beta1P\x01Zacloud.google.com/go/recommendationengine/apiv1beta1/recommendationenginepb;recommendationenginepb\xa2\x02\x05RECAI\xaa\x02)Google.Cloud.RecommendationEngine.V1Beta1\xca\x02)Google\\Cloud\\RecommendationEngine\\V1beta1\xea\x02,Google::Cloud::RecommendationEngine::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.recommendationengine.v1beta1.prediction_apikey_registry_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n-com.google.cloud.recommendationengine.v1beta1P\x01Zacloud.google.com/go/recommendationengine/apiv1beta1/recommendationenginepb;recommendationenginepb\xa2\x02\x05RECAI\xaa\x02)Google.Cloud.RecommendationEngine.V1Beta1\xca\x02)Google\\Cloud\\RecommendationEngine\\V1beta1\xea\x02,Google::Cloud::RecommendationEngine::V1beta1'
    _globals['_CREATEPREDICTIONAPIKEYREGISTRATIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPREDICTIONAPIKEYREGISTRATIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\n.recommendationengine.googleapis.com/EventStore'
    _globals['_CREATEPREDICTIONAPIKEYREGISTRATIONREQUEST'].fields_by_name['prediction_api_key_registration']._loaded_options = None
    _globals['_CREATEPREDICTIONAPIKEYREGISTRATIONREQUEST'].fields_by_name['prediction_api_key_registration']._serialized_options = b'\xe0A\x02'
    _globals['_LISTPREDICTIONAPIKEYREGISTRATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPREDICTIONAPIKEYREGISTRATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\n.recommendationengine.googleapis.com/EventStore'
    _globals['_LISTPREDICTIONAPIKEYREGISTRATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTPREDICTIONAPIKEYREGISTRATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPREDICTIONAPIKEYREGISTRATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTPREDICTIONAPIKEYREGISTRATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEPREDICTIONAPIKEYREGISTRATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPREDICTIONAPIKEYREGISTRATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaAB\n@recommendationengine.googleapis.com/PredictionApiKeyRegistration'
    _globals['_PREDICTIONAPIKEYREGISTRY']._loaded_options = None
    _globals['_PREDICTIONAPIKEYREGISTRY']._serialized_options = b'\xcaA#recommendationengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PREDICTIONAPIKEYREGISTRY'].methods_by_name['CreatePredictionApiKeyRegistration']._loaded_options = None
    _globals['_PREDICTIONAPIKEYREGISTRY'].methods_by_name['CreatePredictionApiKeyRegistration']._serialized_options = b'\xdaA&parent,prediction_api_key_registration\x82\xd3\xe4\x93\x02d"_/v1beta1/{parent=projects/*/locations/*/catalogs/*/eventStores/*}/predictionApiKeyRegistrations:\x01*'
    _globals['_PREDICTIONAPIKEYREGISTRY'].methods_by_name['ListPredictionApiKeyRegistrations']._loaded_options = None
    _globals['_PREDICTIONAPIKEYREGISTRY'].methods_by_name['ListPredictionApiKeyRegistrations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02a\x12_/v1beta1/{parent=projects/*/locations/*/catalogs/*/eventStores/*}/predictionApiKeyRegistrations'
    _globals['_PREDICTIONAPIKEYREGISTRY'].methods_by_name['DeletePredictionApiKeyRegistration']._loaded_options = None
    _globals['_PREDICTIONAPIKEYREGISTRY'].methods_by_name['DeletePredictionApiKeyRegistration']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02a*_/v1beta1/{name=projects/*/locations/*/catalogs/*/eventStores/*/predictionApiKeyRegistrations/*}'
    _globals['_PREDICTIONAPIKEYREGISTRATION']._serialized_start = 353
    _globals['_PREDICTIONAPIKEYREGISTRATION']._serialized_end = 400
    _globals['_CREATEPREDICTIONAPIKEYREGISTRATIONREQUEST']._serialized_start = 403
    _globals['_CREATEPREDICTIONAPIKEYREGISTRATIONREQUEST']._serialized_end = 637
    _globals['_LISTPREDICTIONAPIKEYREGISTRATIONSREQUEST']._serialized_start = 640
    _globals['_LISTPREDICTIONAPIKEYREGISTRATIONSREQUEST']._serialized_end = 803
    _globals['_LISTPREDICTIONAPIKEYREGISTRATIONSRESPONSE']._serialized_start = 806
    _globals['_LISTPREDICTIONAPIKEYREGISTRATIONSRESPONSE']._serialized_end = 989
    _globals['_DELETEPREDICTIONAPIKEYREGISTRATIONREQUEST']._serialized_start = 992
    _globals['_DELETEPREDICTIONAPIKEYREGISTRATIONREQUEST']._serialized_end = 1123
    _globals['_PREDICTIONAPIKEYREGISTRY']._serialized_start = 1126
    _globals['_PREDICTIONAPIKEYREGISTRY']._serialized_end = 2173