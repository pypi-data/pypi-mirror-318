"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1alpha/rank_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/discoveryengine/v1alpha/rank_service.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"J\n\rRankingRecord\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07content\x18\x03 \x01(\t\x12\r\n\x05score\x18\x04 \x01(\x02"\x89\x03\n\x0bRankRequest\x12L\n\x0eranking_config\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,discoveryengine.googleapis.com/RankingConfig\x12\r\n\x05model\x18\x02 \x01(\t\x12\r\n\x05top_n\x18\x03 \x01(\x05\x12\r\n\x05query\x18\x04 \x01(\t\x12I\n\x07records\x18\x05 \x03(\x0b23.google.cloud.discoveryengine.v1alpha.RankingRecordB\x03\xe0A\x02\x12)\n!ignore_record_details_in_response\x18\x06 \x01(\x08\x12V\n\x0buser_labels\x18\x07 \x03(\x0b2A.google.cloud.discoveryengine.v1alpha.RankRequest.UserLabelsEntry\x1a1\n\x0fUserLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"T\n\x0cRankResponse\x12D\n\x07records\x18\x05 \x03(\x0b23.google.cloud.discoveryengine.v1alpha.RankingRecord2\xa4\x02\n\x0bRankService\x12\xc0\x01\n\x04Rank\x121.google.cloud.discoveryengine.v1alpha.RankRequest\x1a2.google.cloud.discoveryengine.v1alpha.RankResponse"Q\x82\xd3\xe4\x93\x02K"F/v1alpha/{ranking_config=projects/*/locations/*/rankingConfigs/*}:rank:\x01*\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x9c\x02\n(com.google.cloud.discoveryengine.v1alphaB\x10RankServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.rank_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x10RankServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
    _globals['_RANKREQUEST_USERLABELSENTRY']._loaded_options = None
    _globals['_RANKREQUEST_USERLABELSENTRY']._serialized_options = b'8\x01'
    _globals['_RANKREQUEST'].fields_by_name['ranking_config']._loaded_options = None
    _globals['_RANKREQUEST'].fields_by_name['ranking_config']._serialized_options = b'\xe0A\x02\xfaA.\n,discoveryengine.googleapis.com/RankingConfig'
    _globals['_RANKREQUEST'].fields_by_name['records']._loaded_options = None
    _globals['_RANKREQUEST'].fields_by_name['records']._serialized_options = b'\xe0A\x02'
    _globals['_RANKSERVICE']._loaded_options = None
    _globals['_RANKSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_RANKSERVICE'].methods_by_name['Rank']._loaded_options = None
    _globals['_RANKSERVICE'].methods_by_name['Rank']._serialized_options = b'\x82\xd3\xe4\x93\x02K"F/v1alpha/{ranking_config=projects/*/locations/*/rankingConfigs/*}:rank:\x01*'
    _globals['_RANKINGRECORD']._serialized_start = 212
    _globals['_RANKINGRECORD']._serialized_end = 286
    _globals['_RANKREQUEST']._serialized_start = 289
    _globals['_RANKREQUEST']._serialized_end = 682
    _globals['_RANKREQUEST_USERLABELSENTRY']._serialized_start = 633
    _globals['_RANKREQUEST_USERLABELSENTRY']._serialized_end = 682
    _globals['_RANKRESPONSE']._serialized_start = 684
    _globals['_RANKRESPONSE']._serialized_end = 768
    _globals['_RANKSERVICE']._serialized_start = 771
    _globals['_RANKSERVICE']._serialized_end = 1063