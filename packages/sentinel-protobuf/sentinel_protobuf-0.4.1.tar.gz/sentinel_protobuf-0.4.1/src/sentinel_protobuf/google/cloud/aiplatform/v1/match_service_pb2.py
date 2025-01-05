"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/match_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import index_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_index__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/aiplatform/v1/match_service.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a&google/cloud/aiplatform/v1/index.proto"\xc1\x04\n\x14FindNeighborsRequest\x12G\n\x0eindex_endpoint\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'aiplatform.googleapis.com/IndexEndpoint\x12\x19\n\x11deployed_index_id\x18\x02 \x01(\t\x12G\n\x07queries\x18\x03 \x03(\x0b26.google.cloud.aiplatform.v1.FindNeighborsRequest.Query\x12\x1d\n\x15return_full_datapoint\x18\x04 \x01(\x08\x1a\xdc\x02\n\x05Query\x12N\n\x03rrf\x18\x06 \x01(\x0b2:.google.cloud.aiplatform.v1.FindNeighborsRequest.Query.RRFB\x03\xe0A\x01H\x00\x12B\n\tdatapoint\x18\x01 \x01(\x0b2*.google.cloud.aiplatform.v1.IndexDatapointB\x03\xe0A\x02\x12\x16\n\x0eneighbor_count\x18\x02 \x01(\x05\x12-\n%per_crowding_attribute_neighbor_count\x18\x03 \x01(\x05\x12"\n\x1aapproximate_neighbor_count\x18\x04 \x01(\x05\x12.\n&fraction_leaf_nodes_to_search_override\x18\x05 \x01(\x01\x1a\x19\n\x03RRF\x12\x12\n\x05alpha\x18\x01 \x01(\x02B\x03\xe0A\x02B\t\n\x07ranking"\xdb\x02\n\x15FindNeighborsResponse\x12]\n\x11nearest_neighbors\x18\x01 \x03(\x0b2B.google.cloud.aiplatform.v1.FindNeighborsResponse.NearestNeighbors\x1at\n\x08Neighbor\x12=\n\tdatapoint\x18\x01 \x01(\x0b2*.google.cloud.aiplatform.v1.IndexDatapoint\x12\x10\n\x08distance\x18\x02 \x01(\x01\x12\x17\n\x0fsparse_distance\x18\x03 \x01(\x01\x1am\n\x10NearestNeighbors\x12\n\n\x02id\x18\x01 \x01(\t\x12M\n\tneighbors\x18\x02 \x03(\x0b2:.google.cloud.aiplatform.v1.FindNeighborsResponse.Neighbor"\x8d\x01\n\x1aReadIndexDatapointsRequest\x12G\n\x0eindex_endpoint\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'aiplatform.googleapis.com/IndexEndpoint\x12\x19\n\x11deployed_index_id\x18\x02 \x01(\t\x12\x0b\n\x03ids\x18\x03 \x03(\t"]\n\x1bReadIndexDatapointsResponse\x12>\n\ndatapoints\x18\x01 \x03(\x0b2*.google.cloud.aiplatform.v1.IndexDatapoint2\x91\x04\n\x0cMatchService\x12\xcb\x01\n\rFindNeighbors\x120.google.cloud.aiplatform.v1.FindNeighborsRequest\x1a1.google.cloud.aiplatform.v1.FindNeighborsResponse"U\x82\xd3\xe4\x93\x02O"J/v1/{index_endpoint=projects/*/locations/*/indexEndpoints/*}:findNeighbors:\x01*\x12\xe3\x01\n\x13ReadIndexDatapoints\x126.google.cloud.aiplatform.v1.ReadIndexDatapointsRequest\x1a7.google.cloud.aiplatform.v1.ReadIndexDatapointsResponse"[\x82\xd3\xe4\x93\x02U"P/v1/{index_endpoint=projects/*/locations/*/indexEndpoints/*}:readIndexDatapoints:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xcf\x01\n\x1ecom.google.cloud.aiplatform.v1B\x11MatchServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.match_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x11MatchServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
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
    _globals['_MATCHSERVICE'].methods_by_name['FindNeighbors']._serialized_options = b'\x82\xd3\xe4\x93\x02O"J/v1/{index_endpoint=projects/*/locations/*/indexEndpoints/*}:findNeighbors:\x01*'
    _globals['_MATCHSERVICE'].methods_by_name['ReadIndexDatapoints']._loaded_options = None
    _globals['_MATCHSERVICE'].methods_by_name['ReadIndexDatapoints']._serialized_options = b'\x82\xd3\xe4\x93\x02U"P/v1/{index_endpoint=projects/*/locations/*/indexEndpoints/*}:readIndexDatapoints:\x01*'
    _globals['_FINDNEIGHBORSREQUEST']._serialized_start = 234
    _globals['_FINDNEIGHBORSREQUEST']._serialized_end = 811
    _globals['_FINDNEIGHBORSREQUEST_QUERY']._serialized_start = 463
    _globals['_FINDNEIGHBORSREQUEST_QUERY']._serialized_end = 811
    _globals['_FINDNEIGHBORSREQUEST_QUERY_RRF']._serialized_start = 775
    _globals['_FINDNEIGHBORSREQUEST_QUERY_RRF']._serialized_end = 800
    _globals['_FINDNEIGHBORSRESPONSE']._serialized_start = 814
    _globals['_FINDNEIGHBORSRESPONSE']._serialized_end = 1161
    _globals['_FINDNEIGHBORSRESPONSE_NEIGHBOR']._serialized_start = 934
    _globals['_FINDNEIGHBORSRESPONSE_NEIGHBOR']._serialized_end = 1050
    _globals['_FINDNEIGHBORSRESPONSE_NEARESTNEIGHBORS']._serialized_start = 1052
    _globals['_FINDNEIGHBORSRESPONSE_NEARESTNEIGHBORS']._serialized_end = 1161
    _globals['_READINDEXDATAPOINTSREQUEST']._serialized_start = 1164
    _globals['_READINDEXDATAPOINTSREQUEST']._serialized_end = 1305
    _globals['_READINDEXDATAPOINTSRESPONSE']._serialized_start = 1307
    _globals['_READINDEXDATAPOINTSRESPONSE']._serialized_end = 1400
    _globals['_MATCHSERVICE']._serialized_start = 1403
    _globals['_MATCHSERVICE']._serialized_end = 1932