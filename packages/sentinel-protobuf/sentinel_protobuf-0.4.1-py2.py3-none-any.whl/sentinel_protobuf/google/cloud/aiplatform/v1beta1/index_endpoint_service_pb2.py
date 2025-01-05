"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/index_endpoint_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import index_endpoint_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_index__endpoint__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/aiplatform/v1beta1/index_endpoint_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a4google/cloud/aiplatform/v1beta1/index_endpoint.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xa4\x01\n\x1aCreateIndexEndpointRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12K\n\x0eindex_endpoint\x18\x02 \x01(\x0b2..google.cloud.aiplatform.v1beta1.IndexEndpointB\x03\xe0A\x02"{\n$CreateIndexEndpointOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"X\n\x17GetIndexEndpointRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'aiplatform.googleapis.com/IndexEndpoint"\xd0\x01\n\x19ListIndexEndpointsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01\x122\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"~\n\x1aListIndexEndpointsResponse\x12G\n\x0findex_endpoints\x18\x01 \x03(\x0b2..google.cloud.aiplatform.v1beta1.IndexEndpoint\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x9f\x01\n\x1aUpdateIndexEndpointRequest\x12K\n\x0eindex_endpoint\x18\x01 \x01(\x0b2..google.cloud.aiplatform.v1beta1.IndexEndpointB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"[\n\x1aDeleteIndexEndpointRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'aiplatform.googleapis.com/IndexEndpoint"\xaa\x01\n\x12DeployIndexRequest\x12G\n\x0eindex_endpoint\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'aiplatform.googleapis.com/IndexEndpoint\x12K\n\x0edeployed_index\x18\x02 \x01(\x0b2..google.cloud.aiplatform.v1beta1.DeployedIndexB\x03\xe0A\x02"]\n\x13DeployIndexResponse\x12F\n\x0edeployed_index\x18\x01 \x01(\x0b2..google.cloud.aiplatform.v1beta1.DeployedIndex"\x8e\x01\n\x1cDeployIndexOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata\x12\x19\n\x11deployed_index_id\x18\x02 \x01(\t"\x7f\n\x14UndeployIndexRequest\x12G\n\x0eindex_endpoint\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'aiplatform.googleapis.com/IndexEndpoint\x12\x1e\n\x11deployed_index_id\x18\x02 \x01(\tB\x03\xe0A\x02"\x17\n\x15UndeployIndexResponse"u\n\x1eUndeployIndexOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"\xb2\x01\n\x1aMutateDeployedIndexRequest\x12G\n\x0eindex_endpoint\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'aiplatform.googleapis.com/IndexEndpoint\x12K\n\x0edeployed_index\x18\x02 \x01(\x0b2..google.cloud.aiplatform.v1beta1.DeployedIndexB\x03\xe0A\x02"e\n\x1bMutateDeployedIndexResponse\x12F\n\x0edeployed_index\x18\x01 \x01(\x0b2..google.cloud.aiplatform.v1beta1.DeployedIndex"\x96\x01\n$MutateDeployedIndexOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata\x12\x19\n\x11deployed_index_id\x18\x02 \x01(\t2\x8e\x11\n\x14IndexEndpointService\x12\x93\x02\n\x13CreateIndexEndpoint\x12;.google.cloud.aiplatform.v1beta1.CreateIndexEndpointRequest\x1a\x1d.google.longrunning.Operation"\x9f\x01\xcaA5\n\rIndexEndpoint\x12$CreateIndexEndpointOperationMetadata\xdaA\x15parent,index_endpoint\x82\xd3\xe4\x93\x02I"7/v1beta1/{parent=projects/*/locations/*}/indexEndpoints:\x0eindex_endpoint\x12\xc4\x01\n\x10GetIndexEndpoint\x128.google.cloud.aiplatform.v1beta1.GetIndexEndpointRequest\x1a..google.cloud.aiplatform.v1beta1.IndexEndpoint"F\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v1beta1/{name=projects/*/locations/*/indexEndpoints/*}\x12\xd7\x01\n\x12ListIndexEndpoints\x12:.google.cloud.aiplatform.v1beta1.ListIndexEndpointsRequest\x1a;.google.cloud.aiplatform.v1beta1.ListIndexEndpointsResponse"H\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1beta1/{parent=projects/*/locations/*}/indexEndpoints\x12\xff\x01\n\x13UpdateIndexEndpoint\x12;.google.cloud.aiplatform.v1beta1.UpdateIndexEndpointRequest\x1a..google.cloud.aiplatform.v1beta1.IndexEndpoint"{\xdaA\x1aindex_endpoint,update_mask\x82\xd3\xe4\x93\x02X2F/v1beta1/{index_endpoint.name=projects/*/locations/*/indexEndpoints/*}:\x0eindex_endpoint\x12\xec\x01\n\x13DeleteIndexEndpoint\x12;.google.cloud.aiplatform.v1beta1.DeleteIndexEndpointRequest\x1a\x1d.google.longrunning.Operation"y\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v1beta1/{name=projects/*/locations/*/indexEndpoints/*}\x12\x92\x02\n\x0bDeployIndex\x123.google.cloud.aiplatform.v1beta1.DeployIndexRequest\x1a\x1d.google.longrunning.Operation"\xae\x01\xcaA3\n\x13DeployIndexResponse\x12\x1cDeployIndexOperationMetadata\xdaA\x1dindex_endpoint,deployed_index\x82\xd3\xe4\x93\x02R"M/v1beta1/{index_endpoint=projects/*/locations/*/indexEndpoints/*}:deployIndex:\x01*\x12\x9f\x02\n\rUndeployIndex\x125.google.cloud.aiplatform.v1beta1.UndeployIndexRequest\x1a\x1d.google.longrunning.Operation"\xb7\x01\xcaA7\n\x15UndeployIndexResponse\x12\x1eUndeployIndexOperationMetadata\xdaA index_endpoint,deployed_index_id\x82\xd3\xe4\x93\x02T"O/v1beta1/{index_endpoint=projects/*/locations/*/indexEndpoints/*}:undeployIndex:\x01*\x12\xc7\x02\n\x13MutateDeployedIndex\x12;.google.cloud.aiplatform.v1beta1.MutateDeployedIndexRequest\x1a\x1d.google.longrunning.Operation"\xd3\x01\xcaAC\n\x1bMutateDeployedIndexResponse\x12$MutateDeployedIndexOperationMetadata\xdaA\x1dindex_endpoint,deployed_index\x82\xd3\xe4\x93\x02g"U/v1beta1/{index_endpoint=projects/*/locations/*/indexEndpoints/*}:mutateDeployedIndex:\x0edeployed_index\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf0\x01\n#com.google.cloud.aiplatform.v1beta1B\x19IndexEndpointServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.index_endpoint_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x19IndexEndpointServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_CREATEINDEXENDPOINTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEINDEXENDPOINTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEINDEXENDPOINTREQUEST'].fields_by_name['index_endpoint']._loaded_options = None
    _globals['_CREATEINDEXENDPOINTREQUEST'].fields_by_name['index_endpoint']._serialized_options = b'\xe0A\x02'
    _globals['_GETINDEXENDPOINTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINDEXENDPOINTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'aiplatform.googleapis.com/IndexEndpoint"
    _globals['_LISTINDEXENDPOINTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTINDEXENDPOINTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTINDEXENDPOINTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTINDEXENDPOINTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINDEXENDPOINTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTINDEXENDPOINTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINDEXENDPOINTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTINDEXENDPOINTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINDEXENDPOINTSREQUEST'].fields_by_name['read_mask']._loaded_options = None
    _globals['_LISTINDEXENDPOINTSREQUEST'].fields_by_name['read_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEINDEXENDPOINTREQUEST'].fields_by_name['index_endpoint']._loaded_options = None
    _globals['_UPDATEINDEXENDPOINTREQUEST'].fields_by_name['index_endpoint']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEINDEXENDPOINTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEINDEXENDPOINTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEINDEXENDPOINTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEINDEXENDPOINTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'aiplatform.googleapis.com/IndexEndpoint"
    _globals['_DEPLOYINDEXREQUEST'].fields_by_name['index_endpoint']._loaded_options = None
    _globals['_DEPLOYINDEXREQUEST'].fields_by_name['index_endpoint']._serialized_options = b"\xe0A\x02\xfaA)\n'aiplatform.googleapis.com/IndexEndpoint"
    _globals['_DEPLOYINDEXREQUEST'].fields_by_name['deployed_index']._loaded_options = None
    _globals['_DEPLOYINDEXREQUEST'].fields_by_name['deployed_index']._serialized_options = b'\xe0A\x02'
    _globals['_UNDEPLOYINDEXREQUEST'].fields_by_name['index_endpoint']._loaded_options = None
    _globals['_UNDEPLOYINDEXREQUEST'].fields_by_name['index_endpoint']._serialized_options = b"\xe0A\x02\xfaA)\n'aiplatform.googleapis.com/IndexEndpoint"
    _globals['_UNDEPLOYINDEXREQUEST'].fields_by_name['deployed_index_id']._loaded_options = None
    _globals['_UNDEPLOYINDEXREQUEST'].fields_by_name['deployed_index_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEDEPLOYEDINDEXREQUEST'].fields_by_name['index_endpoint']._loaded_options = None
    _globals['_MUTATEDEPLOYEDINDEXREQUEST'].fields_by_name['index_endpoint']._serialized_options = b"\xe0A\x02\xfaA)\n'aiplatform.googleapis.com/IndexEndpoint"
    _globals['_MUTATEDEPLOYEDINDEXREQUEST'].fields_by_name['deployed_index']._loaded_options = None
    _globals['_MUTATEDEPLOYEDINDEXREQUEST'].fields_by_name['deployed_index']._serialized_options = b'\xe0A\x02'
    _globals['_INDEXENDPOINTSERVICE']._loaded_options = None
    _globals['_INDEXENDPOINTSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['CreateIndexEndpoint']._loaded_options = None
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['CreateIndexEndpoint']._serialized_options = b'\xcaA5\n\rIndexEndpoint\x12$CreateIndexEndpointOperationMetadata\xdaA\x15parent,index_endpoint\x82\xd3\xe4\x93\x02I"7/v1beta1/{parent=projects/*/locations/*}/indexEndpoints:\x0eindex_endpoint'
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['GetIndexEndpoint']._loaded_options = None
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['GetIndexEndpoint']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v1beta1/{name=projects/*/locations/*/indexEndpoints/*}'
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['ListIndexEndpoints']._loaded_options = None
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['ListIndexEndpoints']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1beta1/{parent=projects/*/locations/*}/indexEndpoints'
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['UpdateIndexEndpoint']._loaded_options = None
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['UpdateIndexEndpoint']._serialized_options = b'\xdaA\x1aindex_endpoint,update_mask\x82\xd3\xe4\x93\x02X2F/v1beta1/{index_endpoint.name=projects/*/locations/*/indexEndpoints/*}:\x0eindex_endpoint'
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['DeleteIndexEndpoint']._loaded_options = None
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['DeleteIndexEndpoint']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v1beta1/{name=projects/*/locations/*/indexEndpoints/*}'
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['DeployIndex']._loaded_options = None
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['DeployIndex']._serialized_options = b'\xcaA3\n\x13DeployIndexResponse\x12\x1cDeployIndexOperationMetadata\xdaA\x1dindex_endpoint,deployed_index\x82\xd3\xe4\x93\x02R"M/v1beta1/{index_endpoint=projects/*/locations/*/indexEndpoints/*}:deployIndex:\x01*'
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['UndeployIndex']._loaded_options = None
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['UndeployIndex']._serialized_options = b'\xcaA7\n\x15UndeployIndexResponse\x12\x1eUndeployIndexOperationMetadata\xdaA index_endpoint,deployed_index_id\x82\xd3\xe4\x93\x02T"O/v1beta1/{index_endpoint=projects/*/locations/*/indexEndpoints/*}:undeployIndex:\x01*'
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['MutateDeployedIndex']._loaded_options = None
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['MutateDeployedIndex']._serialized_options = b'\xcaAC\n\x1bMutateDeployedIndexResponse\x12$MutateDeployedIndexOperationMetadata\xdaA\x1dindex_endpoint,deployed_index\x82\xd3\xe4\x93\x02g"U/v1beta1/{index_endpoint=projects/*/locations/*/indexEndpoints/*}:mutateDeployedIndex:\x0edeployed_index'
    _globals['_CREATEINDEXENDPOINTREQUEST']._serialized_start = 416
    _globals['_CREATEINDEXENDPOINTREQUEST']._serialized_end = 580
    _globals['_CREATEINDEXENDPOINTOPERATIONMETADATA']._serialized_start = 582
    _globals['_CREATEINDEXENDPOINTOPERATIONMETADATA']._serialized_end = 705
    _globals['_GETINDEXENDPOINTREQUEST']._serialized_start = 707
    _globals['_GETINDEXENDPOINTREQUEST']._serialized_end = 795
    _globals['_LISTINDEXENDPOINTSREQUEST']._serialized_start = 798
    _globals['_LISTINDEXENDPOINTSREQUEST']._serialized_end = 1006
    _globals['_LISTINDEXENDPOINTSRESPONSE']._serialized_start = 1008
    _globals['_LISTINDEXENDPOINTSRESPONSE']._serialized_end = 1134
    _globals['_UPDATEINDEXENDPOINTREQUEST']._serialized_start = 1137
    _globals['_UPDATEINDEXENDPOINTREQUEST']._serialized_end = 1296
    _globals['_DELETEINDEXENDPOINTREQUEST']._serialized_start = 1298
    _globals['_DELETEINDEXENDPOINTREQUEST']._serialized_end = 1389
    _globals['_DEPLOYINDEXREQUEST']._serialized_start = 1392
    _globals['_DEPLOYINDEXREQUEST']._serialized_end = 1562
    _globals['_DEPLOYINDEXRESPONSE']._serialized_start = 1564
    _globals['_DEPLOYINDEXRESPONSE']._serialized_end = 1657
    _globals['_DEPLOYINDEXOPERATIONMETADATA']._serialized_start = 1660
    _globals['_DEPLOYINDEXOPERATIONMETADATA']._serialized_end = 1802
    _globals['_UNDEPLOYINDEXREQUEST']._serialized_start = 1804
    _globals['_UNDEPLOYINDEXREQUEST']._serialized_end = 1931
    _globals['_UNDEPLOYINDEXRESPONSE']._serialized_start = 1933
    _globals['_UNDEPLOYINDEXRESPONSE']._serialized_end = 1956
    _globals['_UNDEPLOYINDEXOPERATIONMETADATA']._serialized_start = 1958
    _globals['_UNDEPLOYINDEXOPERATIONMETADATA']._serialized_end = 2075
    _globals['_MUTATEDEPLOYEDINDEXREQUEST']._serialized_start = 2078
    _globals['_MUTATEDEPLOYEDINDEXREQUEST']._serialized_end = 2256
    _globals['_MUTATEDEPLOYEDINDEXRESPONSE']._serialized_start = 2258
    _globals['_MUTATEDEPLOYEDINDEXRESPONSE']._serialized_end = 2359
    _globals['_MUTATEDEPLOYEDINDEXOPERATIONMETADATA']._serialized_start = 2362
    _globals['_MUTATEDEPLOYEDINDEXOPERATIONMETADATA']._serialized_end = 2512
    _globals['_INDEXENDPOINTSERVICE']._serialized_start = 2515
    _globals['_INDEXENDPOINTSERVICE']._serialized_end = 4705