"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/recommender/v1beta1/recommender_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.recommender.v1beta1 import insight_pb2 as google_dot_cloud_dot_recommender_dot_v1beta1_dot_insight__pb2
from .....google.cloud.recommender.v1beta1 import insight_type_config_pb2 as google_dot_cloud_dot_recommender_dot_v1beta1_dot_insight__type__config__pb2
from .....google.cloud.recommender.v1beta1 import recommendation_pb2 as google_dot_cloud_dot_recommender_dot_v1beta1_dot_recommendation__pb2
from .....google.cloud.recommender.v1beta1 import recommender_config_pb2 as google_dot_cloud_dot_recommender_dot_v1beta1_dot_recommender__config__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/recommender/v1beta1/recommender_service.proto\x12 google.cloud.recommender.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a.google/cloud/recommender/v1beta1/insight.proto\x1a:google/cloud/recommender/v1beta1/insight_type_config.proto\x1a5google/cloud/recommender/v1beta1/recommendation.proto\x1a9google/cloud/recommender/v1beta1/recommender_config.proto\x1a google/protobuf/field_mask.proto"\x9b\x01\n\x13ListInsightsRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&recommender.googleapis.com/InsightType\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"l\n\x14ListInsightsResponse\x12;\n\x08insights\x18\x01 \x03(\x0b2).google.cloud.recommender.v1beta1.Insight\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"M\n\x11GetInsightRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"recommender.googleapis.com/Insight"\x8d\x02\n\x1aMarkInsightAcceptedRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"recommender.googleapis.com/Insight\x12l\n\x0estate_metadata\x18\x02 \x03(\x0b2O.google.cloud.recommender.v1beta1.MarkInsightAcceptedRequest.StateMetadataEntryB\x03\xe0A\x01\x12\x11\n\x04etag\x18\x03 \x01(\tB\x03\xe0A\x02\x1a4\n\x12StateMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x9d\x01\n\x1aListRecommendationsRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&recommender.googleapis.com/Recommender\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x0e\n\x06filter\x18\x05 \x01(\t"\x81\x01\n\x1bListRecommendationsResponse\x12I\n\x0frecommendations\x18\x01 \x03(\x0b20.google.cloud.recommender.v1beta1.Recommendation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"[\n\x18GetRecommendationRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)recommender.googleapis.com/Recommendation"\x9b\x02\n MarkRecommendationClaimedRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)recommender.googleapis.com/Recommendation\x12m\n\x0estate_metadata\x18\x02 \x03(\x0b2U.google.cloud.recommender.v1beta1.MarkRecommendationClaimedRequest.StateMetadataEntry\x12\x11\n\x04etag\x18\x03 \x01(\tB\x03\xe0A\x02\x1a4\n\x12StateMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x9f\x02\n"MarkRecommendationSucceededRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)recommender.googleapis.com/Recommendation\x12o\n\x0estate_metadata\x18\x02 \x03(\x0b2W.google.cloud.recommender.v1beta1.MarkRecommendationSucceededRequest.StateMetadataEntry\x12\x11\n\x04etag\x18\x03 \x01(\tB\x03\xe0A\x02\x1a4\n\x12StateMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x99\x02\n\x1fMarkRecommendationFailedRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)recommender.googleapis.com/Recommendation\x12l\n\x0estate_metadata\x18\x02 \x03(\x0b2T.google.cloud.recommender.v1beta1.MarkRecommendationFailedRequest.StateMetadataEntry\x12\x11\n\x04etag\x18\x03 \x01(\tB\x03\xe0A\x02\x1a4\n\x12StateMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"a\n\x1bGetRecommenderConfigRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,recommender.googleapis.com/RecommenderConfig"\xbe\x01\n\x1eUpdateRecommenderConfigRequest\x12T\n\x12recommender_config\x18\x01 \x01(\x0b23.google.cloud.recommender.v1beta1.RecommenderConfigB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08"a\n\x1bGetInsightTypeConfigRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,recommender.googleapis.com/InsightTypeConfig"\xbf\x01\n\x1eUpdateInsightTypeConfigRequest\x12U\n\x13insight_type_config\x18\x01 \x01(\x0b23.google.cloud.recommender.v1beta1.InsightTypeConfigB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08"J\n\x17ListRecommendersRequest\x12\x16\n\tpage_size\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01"|\n\x18ListRecommendersResponse\x12G\n\x0crecommenders\x18\x01 \x03(\x0b21.google.cloud.recommender.v1beta1.RecommenderType\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"J\n\x17ListInsightTypesRequest\x12\x16\n\tpage_size\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01"y\n\x18ListInsightTypesResponse\x12D\n\rinsight_types\x18\x01 \x03(\x0b2-.google.cloud.recommender.v1beta1.InsightType\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x8e-\n\x0bRecommender\x12\xa9\x03\n\x0cListInsights\x125.google.cloud.recommender.v1beta1.ListInsightsRequest\x1a6.google.cloud.recommender.v1beta1.ListInsightsResponse"\xa9\x02\xdaA\x06parent\x82\xd3\xe4\x93\x02\x99\x02\x12@/v1beta1/{parent=projects/*/locations/*/insightTypes/*}/insightsZI\x12G/v1beta1/{parent=billingAccounts/*/locations/*/insightTypes/*}/insightsZA\x12?/v1beta1/{parent=folders/*/locations/*/insightTypes/*}/insightsZG\x12E/v1beta1/{parent=organizations/*/locations/*/insightTypes/*}/insights\x12\x96\x03\n\nGetInsight\x123.google.cloud.recommender.v1beta1.GetInsightRequest\x1a).google.cloud.recommender.v1beta1.Insight"\xa7\x02\xdaA\x04name\x82\xd3\xe4\x93\x02\x99\x02\x12@/v1beta1/{name=projects/*/locations/*/insightTypes/*/insights/*}ZI\x12G/v1beta1/{name=billingAccounts/*/locations/*/insightTypes/*/insights/*}ZA\x12?/v1beta1/{name=folders/*/locations/*/insightTypes/*/insights/*}ZG\x12E/v1beta1/{name=organizations/*/locations/*/insightTypes/*/insights/*}\x12\xfc\x03\n\x13MarkInsightAccepted\x12<.google.cloud.recommender.v1beta1.MarkInsightAcceptedRequest\x1a).google.cloud.recommender.v1beta1.Insight"\xfb\x02\xdaA\x18name,state_metadata,etag\x82\xd3\xe4\x93\x02\xd9\x02"M/v1beta1/{name=projects/*/locations/*/insightTypes/*/insights/*}:markAccepted:\x01*ZY"T/v1beta1/{name=billingAccounts/*/locations/*/insightTypes/*/insights/*}:markAccepted:\x01*ZQ"L/v1beta1/{name=folders/*/locations/*/insightTypes/*/insights/*}:markAccepted:\x01*ZW"R/v1beta1/{name=organizations/*/locations/*/insightTypes/*/insights/*}:markAccepted:\x01*\x12\xe1\x03\n\x13ListRecommendations\x12<.google.cloud.recommender.v1beta1.ListRecommendationsRequest\x1a=.google.cloud.recommender.v1beta1.ListRecommendationsResponse"\xcc\x02\xdaA\rparent,filter\x82\xd3\xe4\x93\x02\xb5\x02\x12G/v1beta1/{parent=projects/*/locations/*/recommenders/*}/recommendationsZP\x12N/v1beta1/{parent=billingAccounts/*/locations/*/recommenders/*}/recommendationsZH\x12F/v1beta1/{parent=folders/*/locations/*/recommenders/*}/recommendationsZN\x12L/v1beta1/{parent=organizations/*/locations/*/recommenders/*}/recommendations\x12\xc7\x03\n\x11GetRecommendation\x12:.google.cloud.recommender.v1beta1.GetRecommendationRequest\x1a0.google.cloud.recommender.v1beta1.Recommendation"\xc3\x02\xdaA\x04name\x82\xd3\xe4\x93\x02\xb5\x02\x12G/v1beta1/{name=projects/*/locations/*/recommenders/*/recommendations/*}ZP\x12N/v1beta1/{name=billingAccounts/*/locations/*/recommenders/*/recommendations/*}ZH\x12F/v1beta1/{name=folders/*/locations/*/recommenders/*/recommendations/*}ZN\x12L/v1beta1/{name=organizations/*/locations/*/recommenders/*/recommendations/*}\x12\xa7\x04\n\x19MarkRecommendationClaimed\x12B.google.cloud.recommender.v1beta1.MarkRecommendationClaimedRequest\x1a0.google.cloud.recommender.v1beta1.Recommendation"\x93\x03\xdaA\x18name,state_metadata,etag\x82\xd3\xe4\x93\x02\xf1\x02"S/v1beta1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markClaimed:\x01*Z_"Z/v1beta1/{name=billingAccounts/*/locations/*/recommenders/*/recommendations/*}:markClaimed:\x01*ZW"R/v1beta1/{name=folders/*/locations/*/recommenders/*/recommendations/*}:markClaimed:\x01*Z]"X/v1beta1/{name=organizations/*/locations/*/recommenders/*/recommendations/*}:markClaimed:\x01*\x12\xb3\x04\n\x1bMarkRecommendationSucceeded\x12D.google.cloud.recommender.v1beta1.MarkRecommendationSucceededRequest\x1a0.google.cloud.recommender.v1beta1.Recommendation"\x9b\x03\xdaA\x18name,state_metadata,etag\x82\xd3\xe4\x93\x02\xf9\x02"U/v1beta1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markSucceeded:\x01*Za"\\/v1beta1/{name=billingAccounts/*/locations/*/recommenders/*/recommendations/*}:markSucceeded:\x01*ZY"T/v1beta1/{name=folders/*/locations/*/recommenders/*/recommendations/*}:markSucceeded:\x01*Z_"Z/v1beta1/{name=organizations/*/locations/*/recommenders/*/recommendations/*}:markSucceeded:\x01*\x12\xa1\x04\n\x18MarkRecommendationFailed\x12A.google.cloud.recommender.v1beta1.MarkRecommendationFailedRequest\x1a0.google.cloud.recommender.v1beta1.Recommendation"\x8f\x03\xdaA\x18name,state_metadata,etag\x82\xd3\xe4\x93\x02\xed\x02"R/v1beta1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markFailed:\x01*Z^"Y/v1beta1/{name=billingAccounts/*/locations/*/recommenders/*/recommendations/*}:markFailed:\x01*ZV"Q/v1beta1/{name=folders/*/locations/*/recommenders/*/recommendations/*}:markFailed:\x01*Z\\"W/v1beta1/{name=organizations/*/locations/*/recommenders/*/recommendations/*}:markFailed:\x01*\x12\x9e\x02\n\x14GetRecommenderConfig\x12=.google.cloud.recommender.v1beta1.GetRecommenderConfigRequest\x1a3.google.cloud.recommender.v1beta1.RecommenderConfig"\x91\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x83\x01\x12</v1beta1/{name=projects/*/locations/*/recommenders/*/config}ZC\x12A/v1beta1/{name=organizations/*/locations/*/recommenders/*/config}\x12\x8c\x03\n\x17UpdateRecommenderConfig\x12@.google.cloud.recommender.v1beta1.UpdateRecommenderConfigRequest\x1a3.google.cloud.recommender.v1beta1.RecommenderConfig"\xf9\x01\xdaA\x1erecommender_config,update_mask\x82\xd3\xe4\x93\x02\xd1\x012O/v1beta1/{recommender_config.name=projects/*/locations/*/recommenders/*/config}:\x12recommender_configZj"T/v1beta1/{recommender_config.name=organizations/*/locations/*/recommenders/*/config}:\x12recommender_config\x12\x9e\x02\n\x14GetInsightTypeConfig\x12=.google.cloud.recommender.v1beta1.GetInsightTypeConfigRequest\x1a3.google.cloud.recommender.v1beta1.InsightTypeConfig"\x91\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x83\x01\x12</v1beta1/{name=projects/*/locations/*/insightTypes/*/config}ZC\x12A/v1beta1/{name=organizations/*/locations/*/insightTypes/*/config}\x12\x91\x03\n\x17UpdateInsightTypeConfig\x12@.google.cloud.recommender.v1beta1.UpdateInsightTypeConfigRequest\x1a3.google.cloud.recommender.v1beta1.InsightTypeConfig"\xfe\x01\xdaA\x1finsight_type_config,update_mask\x82\xd3\xe4\x93\x02\xd5\x012P/v1beta1/{insight_type_config.name=projects/*/locations/*/insightTypes/*/config}:\x13insight_type_configZl"U/v1beta1/{insight_type_config.name=organizations/*/locations/*/insightTypes/*/config}:\x13insight_type_config\x12\xa8\x01\n\x10ListRecommenders\x129.google.cloud.recommender.v1beta1.ListRecommendersRequest\x1a:.google.cloud.recommender.v1beta1.ListRecommendersResponse"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v1beta1/recommenders\x12\xa8\x01\n\x10ListInsightTypes\x129.google.cloud.recommender.v1beta1.ListInsightTypesRequest\x1a:.google.cloud.recommender.v1beta1.ListInsightTypesResponse"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v1beta1/insightTypes\x1aN\xcaA\x1arecommender.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xac\x01\n$com.google.cloud.recommender.v1beta1B\x10RecommenderProtoP\x01ZFcloud.google.com/go/recommender/apiv1beta1/recommenderpb;recommenderpb\xa2\x02\x04CREC\xaa\x02 Google.Cloud.Recommender.V1Beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.recommender.v1beta1.recommender_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.recommender.v1beta1B\x10RecommenderProtoP\x01ZFcloud.google.com/go/recommender/apiv1beta1/recommenderpb;recommenderpb\xa2\x02\x04CREC\xaa\x02 Google.Cloud.Recommender.V1Beta1'
    _globals['_LISTINSIGHTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTINSIGHTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\n&recommender.googleapis.com/InsightType'
    _globals['_LISTINSIGHTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTINSIGHTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINSIGHTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTINSIGHTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINSIGHTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTINSIGHTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_GETINSIGHTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINSIGHTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"recommender.googleapis.com/Insight'
    _globals['_MARKINSIGHTACCEPTEDREQUEST_STATEMETADATAENTRY']._loaded_options = None
    _globals['_MARKINSIGHTACCEPTEDREQUEST_STATEMETADATAENTRY']._serialized_options = b'8\x01'
    _globals['_MARKINSIGHTACCEPTEDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_MARKINSIGHTACCEPTEDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"recommender.googleapis.com/Insight'
    _globals['_MARKINSIGHTACCEPTEDREQUEST'].fields_by_name['state_metadata']._loaded_options = None
    _globals['_MARKINSIGHTACCEPTEDREQUEST'].fields_by_name['state_metadata']._serialized_options = b'\xe0A\x01'
    _globals['_MARKINSIGHTACCEPTEDREQUEST'].fields_by_name['etag']._loaded_options = None
    _globals['_MARKINSIGHTACCEPTEDREQUEST'].fields_by_name['etag']._serialized_options = b'\xe0A\x02'
    _globals['_LISTRECOMMENDATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTRECOMMENDATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\n&recommender.googleapis.com/Recommender'
    _globals['_LISTRECOMMENDATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTRECOMMENDATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTRECOMMENDATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTRECOMMENDATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETRECOMMENDATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETRECOMMENDATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)recommender.googleapis.com/Recommendation'
    _globals['_MARKRECOMMENDATIONCLAIMEDREQUEST_STATEMETADATAENTRY']._loaded_options = None
    _globals['_MARKRECOMMENDATIONCLAIMEDREQUEST_STATEMETADATAENTRY']._serialized_options = b'8\x01'
    _globals['_MARKRECOMMENDATIONCLAIMEDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_MARKRECOMMENDATIONCLAIMEDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)recommender.googleapis.com/Recommendation'
    _globals['_MARKRECOMMENDATIONCLAIMEDREQUEST'].fields_by_name['etag']._loaded_options = None
    _globals['_MARKRECOMMENDATIONCLAIMEDREQUEST'].fields_by_name['etag']._serialized_options = b'\xe0A\x02'
    _globals['_MARKRECOMMENDATIONSUCCEEDEDREQUEST_STATEMETADATAENTRY']._loaded_options = None
    _globals['_MARKRECOMMENDATIONSUCCEEDEDREQUEST_STATEMETADATAENTRY']._serialized_options = b'8\x01'
    _globals['_MARKRECOMMENDATIONSUCCEEDEDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_MARKRECOMMENDATIONSUCCEEDEDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)recommender.googleapis.com/Recommendation'
    _globals['_MARKRECOMMENDATIONSUCCEEDEDREQUEST'].fields_by_name['etag']._loaded_options = None
    _globals['_MARKRECOMMENDATIONSUCCEEDEDREQUEST'].fields_by_name['etag']._serialized_options = b'\xe0A\x02'
    _globals['_MARKRECOMMENDATIONFAILEDREQUEST_STATEMETADATAENTRY']._loaded_options = None
    _globals['_MARKRECOMMENDATIONFAILEDREQUEST_STATEMETADATAENTRY']._serialized_options = b'8\x01'
    _globals['_MARKRECOMMENDATIONFAILEDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_MARKRECOMMENDATIONFAILEDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)recommender.googleapis.com/Recommendation'
    _globals['_MARKRECOMMENDATIONFAILEDREQUEST'].fields_by_name['etag']._loaded_options = None
    _globals['_MARKRECOMMENDATIONFAILEDREQUEST'].fields_by_name['etag']._serialized_options = b'\xe0A\x02'
    _globals['_GETRECOMMENDERCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETRECOMMENDERCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,recommender.googleapis.com/RecommenderConfig'
    _globals['_UPDATERECOMMENDERCONFIGREQUEST'].fields_by_name['recommender_config']._loaded_options = None
    _globals['_UPDATERECOMMENDERCONFIGREQUEST'].fields_by_name['recommender_config']._serialized_options = b'\xe0A\x02'
    _globals['_GETINSIGHTTYPECONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINSIGHTTYPECONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,recommender.googleapis.com/InsightTypeConfig'
    _globals['_UPDATEINSIGHTTYPECONFIGREQUEST'].fields_by_name['insight_type_config']._loaded_options = None
    _globals['_UPDATEINSIGHTTYPECONFIGREQUEST'].fields_by_name['insight_type_config']._serialized_options = b'\xe0A\x02'
    _globals['_LISTRECOMMENDERSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTRECOMMENDERSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTRECOMMENDERSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTRECOMMENDERSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINSIGHTTYPESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTINSIGHTTYPESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINSIGHTTYPESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTINSIGHTTYPESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_RECOMMENDER']._loaded_options = None
    _globals['_RECOMMENDER']._serialized_options = b'\xcaA\x1arecommender.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_RECOMMENDER'].methods_by_name['ListInsights']._loaded_options = None
    _globals['_RECOMMENDER'].methods_by_name['ListInsights']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x99\x02\x12@/v1beta1/{parent=projects/*/locations/*/insightTypes/*}/insightsZI\x12G/v1beta1/{parent=billingAccounts/*/locations/*/insightTypes/*}/insightsZA\x12?/v1beta1/{parent=folders/*/locations/*/insightTypes/*}/insightsZG\x12E/v1beta1/{parent=organizations/*/locations/*/insightTypes/*}/insights'
    _globals['_RECOMMENDER'].methods_by_name['GetInsight']._loaded_options = None
    _globals['_RECOMMENDER'].methods_by_name['GetInsight']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x99\x02\x12@/v1beta1/{name=projects/*/locations/*/insightTypes/*/insights/*}ZI\x12G/v1beta1/{name=billingAccounts/*/locations/*/insightTypes/*/insights/*}ZA\x12?/v1beta1/{name=folders/*/locations/*/insightTypes/*/insights/*}ZG\x12E/v1beta1/{name=organizations/*/locations/*/insightTypes/*/insights/*}'
    _globals['_RECOMMENDER'].methods_by_name['MarkInsightAccepted']._loaded_options = None
    _globals['_RECOMMENDER'].methods_by_name['MarkInsightAccepted']._serialized_options = b'\xdaA\x18name,state_metadata,etag\x82\xd3\xe4\x93\x02\xd9\x02"M/v1beta1/{name=projects/*/locations/*/insightTypes/*/insights/*}:markAccepted:\x01*ZY"T/v1beta1/{name=billingAccounts/*/locations/*/insightTypes/*/insights/*}:markAccepted:\x01*ZQ"L/v1beta1/{name=folders/*/locations/*/insightTypes/*/insights/*}:markAccepted:\x01*ZW"R/v1beta1/{name=organizations/*/locations/*/insightTypes/*/insights/*}:markAccepted:\x01*'
    _globals['_RECOMMENDER'].methods_by_name['ListRecommendations']._loaded_options = None
    _globals['_RECOMMENDER'].methods_by_name['ListRecommendations']._serialized_options = b'\xdaA\rparent,filter\x82\xd3\xe4\x93\x02\xb5\x02\x12G/v1beta1/{parent=projects/*/locations/*/recommenders/*}/recommendationsZP\x12N/v1beta1/{parent=billingAccounts/*/locations/*/recommenders/*}/recommendationsZH\x12F/v1beta1/{parent=folders/*/locations/*/recommenders/*}/recommendationsZN\x12L/v1beta1/{parent=organizations/*/locations/*/recommenders/*}/recommendations'
    _globals['_RECOMMENDER'].methods_by_name['GetRecommendation']._loaded_options = None
    _globals['_RECOMMENDER'].methods_by_name['GetRecommendation']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xb5\x02\x12G/v1beta1/{name=projects/*/locations/*/recommenders/*/recommendations/*}ZP\x12N/v1beta1/{name=billingAccounts/*/locations/*/recommenders/*/recommendations/*}ZH\x12F/v1beta1/{name=folders/*/locations/*/recommenders/*/recommendations/*}ZN\x12L/v1beta1/{name=organizations/*/locations/*/recommenders/*/recommendations/*}'
    _globals['_RECOMMENDER'].methods_by_name['MarkRecommendationClaimed']._loaded_options = None
    _globals['_RECOMMENDER'].methods_by_name['MarkRecommendationClaimed']._serialized_options = b'\xdaA\x18name,state_metadata,etag\x82\xd3\xe4\x93\x02\xf1\x02"S/v1beta1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markClaimed:\x01*Z_"Z/v1beta1/{name=billingAccounts/*/locations/*/recommenders/*/recommendations/*}:markClaimed:\x01*ZW"R/v1beta1/{name=folders/*/locations/*/recommenders/*/recommendations/*}:markClaimed:\x01*Z]"X/v1beta1/{name=organizations/*/locations/*/recommenders/*/recommendations/*}:markClaimed:\x01*'
    _globals['_RECOMMENDER'].methods_by_name['MarkRecommendationSucceeded']._loaded_options = None
    _globals['_RECOMMENDER'].methods_by_name['MarkRecommendationSucceeded']._serialized_options = b'\xdaA\x18name,state_metadata,etag\x82\xd3\xe4\x93\x02\xf9\x02"U/v1beta1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markSucceeded:\x01*Za"\\/v1beta1/{name=billingAccounts/*/locations/*/recommenders/*/recommendations/*}:markSucceeded:\x01*ZY"T/v1beta1/{name=folders/*/locations/*/recommenders/*/recommendations/*}:markSucceeded:\x01*Z_"Z/v1beta1/{name=organizations/*/locations/*/recommenders/*/recommendations/*}:markSucceeded:\x01*'
    _globals['_RECOMMENDER'].methods_by_name['MarkRecommendationFailed']._loaded_options = None
    _globals['_RECOMMENDER'].methods_by_name['MarkRecommendationFailed']._serialized_options = b'\xdaA\x18name,state_metadata,etag\x82\xd3\xe4\x93\x02\xed\x02"R/v1beta1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markFailed:\x01*Z^"Y/v1beta1/{name=billingAccounts/*/locations/*/recommenders/*/recommendations/*}:markFailed:\x01*ZV"Q/v1beta1/{name=folders/*/locations/*/recommenders/*/recommendations/*}:markFailed:\x01*Z\\"W/v1beta1/{name=organizations/*/locations/*/recommenders/*/recommendations/*}:markFailed:\x01*'
    _globals['_RECOMMENDER'].methods_by_name['GetRecommenderConfig']._loaded_options = None
    _globals['_RECOMMENDER'].methods_by_name['GetRecommenderConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x83\x01\x12</v1beta1/{name=projects/*/locations/*/recommenders/*/config}ZC\x12A/v1beta1/{name=organizations/*/locations/*/recommenders/*/config}'
    _globals['_RECOMMENDER'].methods_by_name['UpdateRecommenderConfig']._loaded_options = None
    _globals['_RECOMMENDER'].methods_by_name['UpdateRecommenderConfig']._serialized_options = b'\xdaA\x1erecommender_config,update_mask\x82\xd3\xe4\x93\x02\xd1\x012O/v1beta1/{recommender_config.name=projects/*/locations/*/recommenders/*/config}:\x12recommender_configZj"T/v1beta1/{recommender_config.name=organizations/*/locations/*/recommenders/*/config}:\x12recommender_config'
    _globals['_RECOMMENDER'].methods_by_name['GetInsightTypeConfig']._loaded_options = None
    _globals['_RECOMMENDER'].methods_by_name['GetInsightTypeConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x83\x01\x12</v1beta1/{name=projects/*/locations/*/insightTypes/*/config}ZC\x12A/v1beta1/{name=organizations/*/locations/*/insightTypes/*/config}'
    _globals['_RECOMMENDER'].methods_by_name['UpdateInsightTypeConfig']._loaded_options = None
    _globals['_RECOMMENDER'].methods_by_name['UpdateInsightTypeConfig']._serialized_options = b'\xdaA\x1finsight_type_config,update_mask\x82\xd3\xe4\x93\x02\xd5\x012P/v1beta1/{insight_type_config.name=projects/*/locations/*/insightTypes/*/config}:\x13insight_type_configZl"U/v1beta1/{insight_type_config.name=organizations/*/locations/*/insightTypes/*/config}:\x13insight_type_config'
    _globals['_RECOMMENDER'].methods_by_name['ListRecommenders']._loaded_options = None
    _globals['_RECOMMENDER'].methods_by_name['ListRecommenders']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17\x12\x15/v1beta1/recommenders'
    _globals['_RECOMMENDER'].methods_by_name['ListInsightTypes']._loaded_options = None
    _globals['_RECOMMENDER'].methods_by_name['ListInsightTypes']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17\x12\x15/v1beta1/insightTypes'
    _globals['_LISTINSIGHTSREQUEST']._serialized_start = 468
    _globals['_LISTINSIGHTSREQUEST']._serialized_end = 623
    _globals['_LISTINSIGHTSRESPONSE']._serialized_start = 625
    _globals['_LISTINSIGHTSRESPONSE']._serialized_end = 733
    _globals['_GETINSIGHTREQUEST']._serialized_start = 735
    _globals['_GETINSIGHTREQUEST']._serialized_end = 812
    _globals['_MARKINSIGHTACCEPTEDREQUEST']._serialized_start = 815
    _globals['_MARKINSIGHTACCEPTEDREQUEST']._serialized_end = 1084
    _globals['_MARKINSIGHTACCEPTEDREQUEST_STATEMETADATAENTRY']._serialized_start = 1032
    _globals['_MARKINSIGHTACCEPTEDREQUEST_STATEMETADATAENTRY']._serialized_end = 1084
    _globals['_LISTRECOMMENDATIONSREQUEST']._serialized_start = 1087
    _globals['_LISTRECOMMENDATIONSREQUEST']._serialized_end = 1244
    _globals['_LISTRECOMMENDATIONSRESPONSE']._serialized_start = 1247
    _globals['_LISTRECOMMENDATIONSRESPONSE']._serialized_end = 1376
    _globals['_GETRECOMMENDATIONREQUEST']._serialized_start = 1378
    _globals['_GETRECOMMENDATIONREQUEST']._serialized_end = 1469
    _globals['_MARKRECOMMENDATIONCLAIMEDREQUEST']._serialized_start = 1472
    _globals['_MARKRECOMMENDATIONCLAIMEDREQUEST']._serialized_end = 1755
    _globals['_MARKRECOMMENDATIONCLAIMEDREQUEST_STATEMETADATAENTRY']._serialized_start = 1032
    _globals['_MARKRECOMMENDATIONCLAIMEDREQUEST_STATEMETADATAENTRY']._serialized_end = 1084
    _globals['_MARKRECOMMENDATIONSUCCEEDEDREQUEST']._serialized_start = 1758
    _globals['_MARKRECOMMENDATIONSUCCEEDEDREQUEST']._serialized_end = 2045
    _globals['_MARKRECOMMENDATIONSUCCEEDEDREQUEST_STATEMETADATAENTRY']._serialized_start = 1032
    _globals['_MARKRECOMMENDATIONSUCCEEDEDREQUEST_STATEMETADATAENTRY']._serialized_end = 1084
    _globals['_MARKRECOMMENDATIONFAILEDREQUEST']._serialized_start = 2048
    _globals['_MARKRECOMMENDATIONFAILEDREQUEST']._serialized_end = 2329
    _globals['_MARKRECOMMENDATIONFAILEDREQUEST_STATEMETADATAENTRY']._serialized_start = 1032
    _globals['_MARKRECOMMENDATIONFAILEDREQUEST_STATEMETADATAENTRY']._serialized_end = 1084
    _globals['_GETRECOMMENDERCONFIGREQUEST']._serialized_start = 2331
    _globals['_GETRECOMMENDERCONFIGREQUEST']._serialized_end = 2428
    _globals['_UPDATERECOMMENDERCONFIGREQUEST']._serialized_start = 2431
    _globals['_UPDATERECOMMENDERCONFIGREQUEST']._serialized_end = 2621
    _globals['_GETINSIGHTTYPECONFIGREQUEST']._serialized_start = 2623
    _globals['_GETINSIGHTTYPECONFIGREQUEST']._serialized_end = 2720
    _globals['_UPDATEINSIGHTTYPECONFIGREQUEST']._serialized_start = 2723
    _globals['_UPDATEINSIGHTTYPECONFIGREQUEST']._serialized_end = 2914
    _globals['_LISTRECOMMENDERSREQUEST']._serialized_start = 2916
    _globals['_LISTRECOMMENDERSREQUEST']._serialized_end = 2990
    _globals['_LISTRECOMMENDERSRESPONSE']._serialized_start = 2992
    _globals['_LISTRECOMMENDERSRESPONSE']._serialized_end = 3116
    _globals['_LISTINSIGHTTYPESREQUEST']._serialized_start = 3118
    _globals['_LISTINSIGHTTYPESREQUEST']._serialized_end = 3192
    _globals['_LISTINSIGHTTYPESRESPONSE']._serialized_start = 3194
    _globals['_LISTINSIGHTTYPESRESPONSE']._serialized_end = 3315
    _globals['_RECOMMENDER']._serialized_start = 3318
    _globals['_RECOMMENDER']._serialized_end = 9092