"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/match_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import index_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_index__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/aiplatform/v1beta1/match_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a+google/cloud/aiplatform/v1beta1/index.proto"\xd0\x04\n\x14FindNeighborsRequest\x12G\n\x0eindex_endpoint\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'aiplatform.googleapis.com/IndexEndpoint\x12\x19\n\x11deployed_index_id\x18\x02 \x01(\t\x12L\n\x07queries\x18\x03 \x03(\x0b2;.google.cloud.aiplatform.v1beta1.FindNeighborsRequest.Query\x12\x1d\n\x15return_full_datapoint\x18\x04 \x01(\x08\x1a\xe6\x02\n\x05Query\x12S\n\x03rrf\x18\x06 \x01(\x0b2?.google.cloud.aiplatform.v1beta1.FindNeighborsRequest.Query.RRFB\x03\xe0A\x01H\x00\x12G\n\tdatapoint\x18\x01 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.IndexDatapointB\x03\xe0A\x02\x12\x16\n\x0eneighbor_count\x18\x02 \x01(\x05\x12-\n%per_crowding_attribute_neighbor_count\x18\x03 \x01(\x05\x12"\n\x1aapproximate_neighbor_count\x18\x04 \x01(\x05\x12.\n&fraction_leaf_nodes_to_search_override\x18\x05 \x01(\x01\x1a\x19\n\x03RRF\x12\x12\n\x05alpha\x18\x01 \x01(\x02B\x03\xe0A\x02B\t\n\x07ranking"\xea\x02\n\x15FindNeighborsResponse\x12b\n\x11nearest_neighbors\x18\x01 \x03(\x0b2G.google.cloud.aiplatform.v1beta1.FindNeighborsResponse.NearestNeighbors\x1ay\n\x08Neighbor\x12B\n\tdatapoint\x18\x01 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.IndexDatapoint\x12\x10\n\x08distance\x18\x02 \x01(\x01\x12\x17\n\x0fsparse_distance\x18\x03 \x01(\x01\x1ar\n\x10NearestNeighbors\x12\n\n\x02id\x18\x01 \x01(\t\x12R\n\tneighbors\x18\x02 \x03(\x0b2?.google.cloud.aiplatform.v1beta1.FindNeighborsResponse.Neighbor"\x8d\x01\n\x1aReadIndexDatapointsRequest\x12G\n\x0eindex_endpoint\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'aiplatform.googleapis.com/IndexEndpoint\x12\x19\n\x11deployed_index_id\x18\x02 \x01(\t\x12\x0b\n\x03ids\x18\x03 \x03(\t"b\n\x1bReadIndexDatapointsResponse\x12C\n\ndatapoints\x18\x01 \x03(\x0b2/.google.cloud.aiplatform.v1beta1.IndexDatapoint2\xaf\x04\n\x0cMatchService\x12\xda\x01\n\rFindNeighbors\x125.google.cloud.aiplatform.v1beta1.FindNeighborsRequest\x1a6.google.cloud.aiplatform.v1beta1.FindNeighborsResponse"Z\x82\xd3\xe4\x93\x02T"O/v1beta1/{index_endpoint=projects/*/locations/*/indexEndpoints/*}:findNeighbors:\x01*\x12\xf2\x01\n\x13ReadIndexDatapoints\x12;.google.cloud.aiplatform.v1beta1.ReadIndexDatapointsRequest\x1a<.google.cloud.aiplatform.v1beta1.ReadIndexDatapointsResponse"`\x82\xd3\xe4\x93\x02Z"U/v1beta1/{index_endpoint=projects/*/locations/*/indexEndpoints/*}:readIndexDatapoints:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe8\x01\n#com.google.cloud.aiplatform.v1beta1B\x11MatchServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.match_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x11MatchServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_FINDNEIGHBORSREQUEST_QUERY_RRF'].fields_by_name['alpha']._loaded_options = None
    _globals['_FINDNEIGHBORSREQUEST_QUERY_RRF'].fields_by_name['alpha']._serialized_options = b'\xe0A\x02'
    _globals['_FINDNEIGHBORSREQUEST_QUERY'].fields_by_name['rrf']._loaded_options = None
    _globals['_FINDNEIGHBORSREQUEST_QUERY'].fields_by_name['rrf']._serialized_options = b'\xe0A\x01'
    _globals['_FINDNEIGHBORSREQUEST_QUERY'].fields_by_name['datapoint']._loaded_options = None
    _globals['_FINDNEIGHBORSREQUEST_QUERY'].fields_by_name['datapoint']._serialized_options = b'\xe0A\x02'
    _globals['_FINDNEIGHBORSREQUEST'].fields_by_name['index_endpoint']._loaded_options = None
    _globals['_FINDNEIGHBORSREQUEST'].fields_by_name['index_endpoint']._serialized_options = b"\xe0A\x02\xfaA)\n'aiplatform.googleapis.com/IndexEndpoint"
    _globals['_READINDEXDATAPOINTSREQUEST'].fields_by_name['index_endpoint']._loaded_options = None
    _globals['_READINDEXDATAPOINTSREQUEST'].fields_by_name['index_endpoint']._serialized_options = b"\xe0A\x02\xfaA)\n'aiplatform.googleapis.com/IndexEndpoint"
    _globals['_MATCHSERVICE']._loaded_options = None
    _globals['_MATCHSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_MATCHSERVICE'].methods_by_name['FindNeighbors']._loaded_options = None
    _globals['_MATCHSERVICE'].methods_by_name['FindNeighbors']._serialized_options = b'\x82\xd3\xe4\x93\x02T"O/v1beta1/{index_endpoint=projects/*/locations/*/indexEndpoints/*}:findNeighbors:\x01*'
    _globals['_MATCHSERVICE'].methods_by_name['ReadIndexDatapoints']._loaded_options = None
    _globals['_MATCHSERVICE'].methods_by_name['ReadIndexDatapoints']._serialized_options = b'\x82\xd3\xe4\x93\x02Z"U/v1beta1/{index_endpoint=projects/*/locations/*/indexEndpoints/*}:readIndexDatapoints:\x01*'
    _globals['_FINDNEIGHBORSREQUEST']._serialized_start = 249
    _globals['_FINDNEIGHBORSREQUEST']._serialized_end = 841
    _globals['_FINDNEIGHBORSREQUEST_QUERY']._serialized_start = 483
    _globals['_FINDNEIGHBORSREQUEST_QUERY']._serialized_end = 841
    _globals['_FINDNEIGHBORSREQUEST_QUERY_RRF']._serialized_start = 805
    _globals['_FINDNEIGHBORSREQUEST_QUERY_RRF']._serialized_end = 830
    _globals['_FINDNEIGHBORSRESPONSE']._serialized_start = 844
    _globals['_FINDNEIGHBORSRESPONSE']._serialized_end = 1206
    _globals['_FINDNEIGHBORSRESPONSE_NEIGHBOR']._serialized_start = 969
    _globals['_FINDNEIGHBORSRESPONSE_NEIGHBOR']._serialized_end = 1090
    _globals['_FINDNEIGHBORSRESPONSE_NEARESTNEIGHBORS']._serialized_start = 1092
    _globals['_FINDNEIGHBORSRESPONSE_NEARESTNEIGHBORS']._serialized_end = 1206
    _globals['_READINDEXDATAPOINTSREQUEST']._serialized_start = 1209
    _globals['_READINDEXDATAPOINTSREQUEST']._serialized_end = 1350
    _globals['_READINDEXDATAPOINTSRESPONSE']._serialized_start = 1352
    _globals['_READINDEXDATAPOINTSRESPONSE']._serialized_end = 1450
    _globals['_MATCHSERVICE']._serialized_start = 1453
    _globals['_MATCHSERVICE']._serialized_end = 2012