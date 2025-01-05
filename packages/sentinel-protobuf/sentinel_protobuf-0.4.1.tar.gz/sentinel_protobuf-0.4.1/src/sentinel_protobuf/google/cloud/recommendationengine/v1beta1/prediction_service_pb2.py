"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/recommendationengine/v1beta1/prediction_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.recommendationengine.v1beta1 import user_event_pb2 as google_dot_cloud_dot_recommendationengine_dot_v1beta1_dot_user__event__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgoogle/cloud/recommendationengine/v1beta1/prediction_service.proto\x12)google.cloud.recommendationengine.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a:google/cloud/recommendationengine/v1beta1/user_event.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x17google/api/client.proto"\xae\x04\n\x0ePredictRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-recommendationengine.googleapis.com/Placement\x12M\n\nuser_event\x18\x02 \x01(\x0b24.google.cloud.recommendationengine.v1beta1.UserEventB\x03\xe0A\x02\x12\x16\n\tpage_size\x18\x07 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x08 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x14\n\x07dry_run\x18\x04 \x01(\x08B\x03\xe0A\x01\x12Z\n\x06params\x18\x06 \x03(\x0b2E.google.cloud.recommendationengine.v1beta1.PredictRequest.ParamsEntryB\x03\xe0A\x01\x12Z\n\x06labels\x18\t \x03(\x0b2E.google.cloud.recommendationengine.v1beta1.PredictRequest.LabelsEntryB\x03\xe0A\x01\x1aE\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value:\x028\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xe2\x04\n\x0fPredictResponse\x12\\\n\x07results\x18\x01 \x03(\x0b2K.google.cloud.recommendationengine.v1beta1.PredictResponse.PredictionResult\x12\x1c\n\x14recommendation_token\x18\x02 \x01(\t\x12 \n\x18items_missing_in_catalog\x18\x03 \x03(\t\x12\x0f\n\x07dry_run\x18\x04 \x01(\x08\x12Z\n\x08metadata\x18\x05 \x03(\x0b2H.google.cloud.recommendationengine.v1beta1.PredictResponse.MetadataEntry\x12\x17\n\x0fnext_page_token\x18\x06 \x01(\t\x1a\xe1\x01\n\x10PredictionResult\x12\n\n\x02id\x18\x01 \x01(\t\x12t\n\ritem_metadata\x18\x02 \x03(\x0b2].google.cloud.recommendationengine.v1beta1.PredictResponse.PredictionResult.ItemMetadataEntry\x1aK\n\x11ItemMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value:\x028\x01\x1aG\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value:\x028\x012\xe2\x02\n\x11PredictionService\x12\xf3\x01\n\x07Predict\x129.google.cloud.recommendationengine.v1beta1.PredictRequest\x1a:.google.cloud.recommendationengine.v1beta1.PredictResponse"q\xdaA\x0fname,user_event\x82\xd3\xe4\x93\x02Y"T/v1beta1/{name=projects/*/locations/*/catalogs/*/eventStores/*/placements/*}:predict:\x01*\x1aW\xcaA#recommendationengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa3\x02\n-com.google.cloud.recommendationengine.v1beta1P\x01Zacloud.google.com/go/recommendationengine/apiv1beta1/recommendationenginepb;recommendationenginepb\xa2\x02\x05RECAI\xaa\x02)Google.Cloud.RecommendationEngine.V1Beta1\xca\x02)Google\\Cloud\\RecommendationEngine\\V1beta1\xea\x02,Google::Cloud::RecommendationEngine::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.recommendationengine.v1beta1.prediction_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n-com.google.cloud.recommendationengine.v1beta1P\x01Zacloud.google.com/go/recommendationengine/apiv1beta1/recommendationenginepb;recommendationenginepb\xa2\x02\x05RECAI\xaa\x02)Google.Cloud.RecommendationEngine.V1Beta1\xca\x02)Google\\Cloud\\RecommendationEngine\\V1beta1\xea\x02,Google::Cloud::RecommendationEngine::V1beta1'
    _globals['_PREDICTREQUEST_PARAMSENTRY']._loaded_options = None
    _globals['_PREDICTREQUEST_PARAMSENTRY']._serialized_options = b'8\x01'
    _globals['_PREDICTREQUEST_LABELSENTRY']._loaded_options = None
    _globals['_PREDICTREQUEST_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_PREDICTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_PREDICTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-recommendationengine.googleapis.com/Placement'
    _globals['_PREDICTREQUEST'].fields_by_name['user_event']._loaded_options = None
    _globals['_PREDICTREQUEST'].fields_by_name['user_event']._serialized_options = b'\xe0A\x02'
    _globals['_PREDICTREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_PREDICTREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_PREDICTREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_PREDICTREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_PREDICTREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_PREDICTREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_PREDICTREQUEST'].fields_by_name['dry_run']._loaded_options = None
    _globals['_PREDICTREQUEST'].fields_by_name['dry_run']._serialized_options = b'\xe0A\x01'
    _globals['_PREDICTREQUEST'].fields_by_name['params']._loaded_options = None
    _globals['_PREDICTREQUEST'].fields_by_name['params']._serialized_options = b'\xe0A\x01'
    _globals['_PREDICTREQUEST'].fields_by_name['labels']._loaded_options = None
    _globals['_PREDICTREQUEST'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_PREDICTRESPONSE_PREDICTIONRESULT_ITEMMETADATAENTRY']._loaded_options = None
    _globals['_PREDICTRESPONSE_PREDICTIONRESULT_ITEMMETADATAENTRY']._serialized_options = b'8\x01'
    _globals['_PREDICTRESPONSE_METADATAENTRY']._loaded_options = None
    _globals['_PREDICTRESPONSE_METADATAENTRY']._serialized_options = b'8\x01'
    _globals['_PREDICTIONSERVICE']._loaded_options = None
    _globals['_PREDICTIONSERVICE']._serialized_options = b'\xcaA#recommendationengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PREDICTIONSERVICE'].methods_by_name['Predict']._loaded_options = None
    _globals['_PREDICTIONSERVICE'].methods_by_name['Predict']._serialized_options = b'\xdaA\x0fname,user_event\x82\xd3\xe4\x93\x02Y"T/v1beta1/{name=projects/*/locations/*/catalogs/*/eventStores/*/placements/*}:predict:\x01*'
    _globals['_PREDICTREQUEST']._serialized_start = 319
    _globals['_PREDICTREQUEST']._serialized_end = 877
    _globals['_PREDICTREQUEST_PARAMSENTRY']._serialized_start = 761
    _globals['_PREDICTREQUEST_PARAMSENTRY']._serialized_end = 830
    _globals['_PREDICTREQUEST_LABELSENTRY']._serialized_start = 832
    _globals['_PREDICTREQUEST_LABELSENTRY']._serialized_end = 877
    _globals['_PREDICTRESPONSE']._serialized_start = 880
    _globals['_PREDICTRESPONSE']._serialized_end = 1490
    _globals['_PREDICTRESPONSE_PREDICTIONRESULT']._serialized_start = 1192
    _globals['_PREDICTRESPONSE_PREDICTIONRESULT']._serialized_end = 1417
    _globals['_PREDICTRESPONSE_PREDICTIONRESULT_ITEMMETADATAENTRY']._serialized_start = 1342
    _globals['_PREDICTRESPONSE_PREDICTIONRESULT_ITEMMETADATAENTRY']._serialized_end = 1417
    _globals['_PREDICTRESPONSE_METADATAENTRY']._serialized_start = 1419
    _globals['_PREDICTRESPONSE_METADATAENTRY']._serialized_end = 1490
    _globals['_PREDICTIONSERVICE']._serialized_start = 1493
    _globals['_PREDICTIONSERVICE']._serialized_end = 1847