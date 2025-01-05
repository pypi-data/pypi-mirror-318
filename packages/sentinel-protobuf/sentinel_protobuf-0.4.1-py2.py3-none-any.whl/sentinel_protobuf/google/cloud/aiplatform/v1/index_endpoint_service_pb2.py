"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/index_endpoint_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import index_endpoint_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_index__endpoint__pb2
from .....google.cloud.aiplatform.v1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_operation__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/aiplatform/v1/index_endpoint_service.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/aiplatform/v1/index_endpoint.proto\x1a*google/cloud/aiplatform/v1/operation.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x9f\x01\n\x1aCreateIndexEndpointRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12F\n\x0eindex_endpoint\x18\x02 \x01(\x0b2).google.cloud.aiplatform.v1.IndexEndpointB\x03\xe0A\x02"v\n$CreateIndexEndpointOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata"X\n\x17GetIndexEndpointRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'aiplatform.googleapis.com/IndexEndpoint"\xd0\x01\n\x19ListIndexEndpointsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01\x122\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"y\n\x1aListIndexEndpointsResponse\x12B\n\x0findex_endpoints\x18\x01 \x03(\x0b2).google.cloud.aiplatform.v1.IndexEndpoint\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x9a\x01\n\x1aUpdateIndexEndpointRequest\x12F\n\x0eindex_endpoint\x18\x01 \x01(\x0b2).google.cloud.aiplatform.v1.IndexEndpointB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"[\n\x1aDeleteIndexEndpointRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'aiplatform.googleapis.com/IndexEndpoint"\xa5\x01\n\x12DeployIndexRequest\x12G\n\x0eindex_endpoint\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'aiplatform.googleapis.com/IndexEndpoint\x12F\n\x0edeployed_index\x18\x02 \x01(\x0b2).google.cloud.aiplatform.v1.DeployedIndexB\x03\xe0A\x02"X\n\x13DeployIndexResponse\x12A\n\x0edeployed_index\x18\x01 \x01(\x0b2).google.cloud.aiplatform.v1.DeployedIndex"\x89\x01\n\x1cDeployIndexOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata\x12\x19\n\x11deployed_index_id\x18\x02 \x01(\t"\x7f\n\x14UndeployIndexRequest\x12G\n\x0eindex_endpoint\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'aiplatform.googleapis.com/IndexEndpoint\x12\x1e\n\x11deployed_index_id\x18\x02 \x01(\tB\x03\xe0A\x02"\x17\n\x15UndeployIndexResponse"p\n\x1eUndeployIndexOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata"\xad\x01\n\x1aMutateDeployedIndexRequest\x12G\n\x0eindex_endpoint\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'aiplatform.googleapis.com/IndexEndpoint\x12F\n\x0edeployed_index\x18\x02 \x01(\x0b2).google.cloud.aiplatform.v1.DeployedIndexB\x03\xe0A\x02"`\n\x1bMutateDeployedIndexResponse\x12A\n\x0edeployed_index\x18\x01 \x01(\x0b2).google.cloud.aiplatform.v1.DeployedIndex"\x91\x01\n$MutateDeployedIndexOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata\x12\x19\n\x11deployed_index_id\x18\x02 \x01(\t2\xaf\x10\n\x14IndexEndpointService\x12\x89\x02\n\x13CreateIndexEndpoint\x126.google.cloud.aiplatform.v1.CreateIndexEndpointRequest\x1a\x1d.google.longrunning.Operation"\x9a\x01\xcaA5\n\rIndexEndpoint\x12$CreateIndexEndpointOperationMetadata\xdaA\x15parent,index_endpoint\x82\xd3\xe4\x93\x02D"2/v1/{parent=projects/*/locations/*}/indexEndpoints:\x0eindex_endpoint\x12\xb5\x01\n\x10GetIndexEndpoint\x123.google.cloud.aiplatform.v1.GetIndexEndpointRequest\x1a).google.cloud.aiplatform.v1.IndexEndpoint"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1/{name=projects/*/locations/*/indexEndpoints/*}\x12\xc8\x01\n\x12ListIndexEndpoints\x125.google.cloud.aiplatform.v1.ListIndexEndpointsRequest\x1a6.google.cloud.aiplatform.v1.ListIndexEndpointsResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1/{parent=projects/*/locations/*}/indexEndpoints\x12\xf0\x01\n\x13UpdateIndexEndpoint\x126.google.cloud.aiplatform.v1.UpdateIndexEndpointRequest\x1a).google.cloud.aiplatform.v1.IndexEndpoint"v\xdaA\x1aindex_endpoint,update_mask\x82\xd3\xe4\x93\x02S2A/v1/{index_endpoint.name=projects/*/locations/*/indexEndpoints/*}:\x0eindex_endpoint\x12\xe2\x01\n\x13DeleteIndexEndpoint\x126.google.cloud.aiplatform.v1.DeleteIndexEndpointRequest\x1a\x1d.google.longrunning.Operation"t\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1/{name=projects/*/locations/*/indexEndpoints/*}\x12\x88\x02\n\x0bDeployIndex\x12..google.cloud.aiplatform.v1.DeployIndexRequest\x1a\x1d.google.longrunning.Operation"\xa9\x01\xcaA3\n\x13DeployIndexResponse\x12\x1cDeployIndexOperationMetadata\xdaA\x1dindex_endpoint,deployed_index\x82\xd3\xe4\x93\x02M"H/v1/{index_endpoint=projects/*/locations/*/indexEndpoints/*}:deployIndex:\x01*\x12\x95\x02\n\rUndeployIndex\x120.google.cloud.aiplatform.v1.UndeployIndexRequest\x1a\x1d.google.longrunning.Operation"\xb2\x01\xcaA7\n\x15UndeployIndexResponse\x12\x1eUndeployIndexOperationMetadata\xdaA index_endpoint,deployed_index_id\x82\xd3\xe4\x93\x02O"J/v1/{index_endpoint=projects/*/locations/*/indexEndpoints/*}:undeployIndex:\x01*\x12\xbd\x02\n\x13MutateDeployedIndex\x126.google.cloud.aiplatform.v1.MutateDeployedIndexRequest\x1a\x1d.google.longrunning.Operation"\xce\x01\xcaAC\n\x1bMutateDeployedIndexResponse\x12$MutateDeployedIndexOperationMetadata\xdaA\x1dindex_endpoint,deployed_index\x82\xd3\xe4\x93\x02b"P/v1/{index_endpoint=projects/*/locations/*/indexEndpoints/*}:mutateDeployedIndex:\x0edeployed_index\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd7\x01\n\x1ecom.google.cloud.aiplatform.v1B\x19IndexEndpointServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.index_endpoint_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x19IndexEndpointServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
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
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['CreateIndexEndpoint']._serialized_options = b'\xcaA5\n\rIndexEndpoint\x12$CreateIndexEndpointOperationMetadata\xdaA\x15parent,index_endpoint\x82\xd3\xe4\x93\x02D"2/v1/{parent=projects/*/locations/*}/indexEndpoints:\x0eindex_endpoint'
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['GetIndexEndpoint']._loaded_options = None
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['GetIndexEndpoint']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1/{name=projects/*/locations/*/indexEndpoints/*}'
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['ListIndexEndpoints']._loaded_options = None
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['ListIndexEndpoints']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1/{parent=projects/*/locations/*}/indexEndpoints'
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['UpdateIndexEndpoint']._loaded_options = None
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['UpdateIndexEndpoint']._serialized_options = b'\xdaA\x1aindex_endpoint,update_mask\x82\xd3\xe4\x93\x02S2A/v1/{index_endpoint.name=projects/*/locations/*/indexEndpoints/*}:\x0eindex_endpoint'
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['DeleteIndexEndpoint']._loaded_options = None
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['DeleteIndexEndpoint']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1/{name=projects/*/locations/*/indexEndpoints/*}'
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['DeployIndex']._loaded_options = None
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['DeployIndex']._serialized_options = b'\xcaA3\n\x13DeployIndexResponse\x12\x1cDeployIndexOperationMetadata\xdaA\x1dindex_endpoint,deployed_index\x82\xd3\xe4\x93\x02M"H/v1/{index_endpoint=projects/*/locations/*/indexEndpoints/*}:deployIndex:\x01*'
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['UndeployIndex']._loaded_options = None
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['UndeployIndex']._serialized_options = b'\xcaA7\n\x15UndeployIndexResponse\x12\x1eUndeployIndexOperationMetadata\xdaA index_endpoint,deployed_index_id\x82\xd3\xe4\x93\x02O"J/v1/{index_endpoint=projects/*/locations/*/indexEndpoints/*}:undeployIndex:\x01*'
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['MutateDeployedIndex']._loaded_options = None
    _globals['_INDEXENDPOINTSERVICE'].methods_by_name['MutateDeployedIndex']._serialized_options = b'\xcaAC\n\x1bMutateDeployedIndexResponse\x12$MutateDeployedIndexOperationMetadata\xdaA\x1dindex_endpoint,deployed_index\x82\xd3\xe4\x93\x02b"P/v1/{index_endpoint=projects/*/locations/*/indexEndpoints/*}:mutateDeployedIndex:\x0edeployed_index'
    _globals['_CREATEINDEXENDPOINTREQUEST']._serialized_start = 396
    _globals['_CREATEINDEXENDPOINTREQUEST']._serialized_end = 555
    _globals['_CREATEINDEXENDPOINTOPERATIONMETADATA']._serialized_start = 557
    _globals['_CREATEINDEXENDPOINTOPERATIONMETADATA']._serialized_end = 675
    _globals['_GETINDEXENDPOINTREQUEST']._serialized_start = 677
    _globals['_GETINDEXENDPOINTREQUEST']._serialized_end = 765
    _globals['_LISTINDEXENDPOINTSREQUEST']._serialized_start = 768
    _globals['_LISTINDEXENDPOINTSREQUEST']._serialized_end = 976
    _globals['_LISTINDEXENDPOINTSRESPONSE']._serialized_start = 978
    _globals['_LISTINDEXENDPOINTSRESPONSE']._serialized_end = 1099
    _globals['_UPDATEINDEXENDPOINTREQUEST']._serialized_start = 1102
    _globals['_UPDATEINDEXENDPOINTREQUEST']._serialized_end = 1256
    _globals['_DELETEINDEXENDPOINTREQUEST']._serialized_start = 1258
    _globals['_DELETEINDEXENDPOINTREQUEST']._serialized_end = 1349
    _globals['_DEPLOYINDEXREQUEST']._serialized_start = 1352
    _globals['_DEPLOYINDEXREQUEST']._serialized_end = 1517
    _globals['_DEPLOYINDEXRESPONSE']._serialized_start = 1519
    _globals['_DEPLOYINDEXRESPONSE']._serialized_end = 1607
    _globals['_DEPLOYINDEXOPERATIONMETADATA']._serialized_start = 1610
    _globals['_DEPLOYINDEXOPERATIONMETADATA']._serialized_end = 1747
    _globals['_UNDEPLOYINDEXREQUEST']._serialized_start = 1749
    _globals['_UNDEPLOYINDEXREQUEST']._serialized_end = 1876
    _globals['_UNDEPLOYINDEXRESPONSE']._serialized_start = 1878
    _globals['_UNDEPLOYINDEXRESPONSE']._serialized_end = 1901
    _globals['_UNDEPLOYINDEXOPERATIONMETADATA']._serialized_start = 1903
    _globals['_UNDEPLOYINDEXOPERATIONMETADATA']._serialized_end = 2015
    _globals['_MUTATEDEPLOYEDINDEXREQUEST']._serialized_start = 2018
    _globals['_MUTATEDEPLOYEDINDEXREQUEST']._serialized_end = 2191
    _globals['_MUTATEDEPLOYEDINDEXRESPONSE']._serialized_start = 2193
    _globals['_MUTATEDEPLOYEDINDEXRESPONSE']._serialized_end = 2289
    _globals['_MUTATEDEPLOYEDINDEXOPERATIONMETADATA']._serialized_start = 2292
    _globals['_MUTATEDEPLOYEDINDEXOPERATIONMETADATA']._serialized_end = 2437
    _globals['_INDEXENDPOINTSERVICE']._serialized_start = 2440
    _globals['_INDEXENDPOINTSERVICE']._serialized_end = 4535