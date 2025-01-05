"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/contentwarehouse/v1/synonymset_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.cloud.contentwarehouse.v1 import synonymset_pb2 as google_dot_cloud_dot_contentwarehouse_dot_v1_dot_synonymset__pb2
from .....google.cloud.contentwarehouse.v1 import synonymset_service_request_pb2 as google_dot_cloud_dot_contentwarehouse_dot_v1_dot_synonymset__service__request__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/contentwarehouse/v1/synonymset_service.proto\x12 google.cloud.contentwarehouse.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a1google/cloud/contentwarehouse/v1/synonymset.proto\x1aAgoogle/cloud/contentwarehouse/v1/synonymset_service_request.proto\x1a\x1bgoogle/protobuf/empty.proto2\xc3\x08\n\x11SynonymSetService\x12\xd6\x01\n\x10CreateSynonymSet\x129.google.cloud.contentwarehouse.v1.CreateSynonymSetRequest\x1a,.google.cloud.contentwarehouse.v1.SynonymSet"Y\xdaA\x12parent,synonym_set\x82\xd3\xe4\x93\x02>"//v1/{parent=projects/*/locations/*}/synonymSets:\x0bsynonym_set\x12\xb5\x01\n\rGetSynonymSet\x126.google.cloud.contentwarehouse.v1.GetSynonymSetRequest\x1a,.google.cloud.contentwarehouse.v1.SynonymSet">\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1/{name=projects/*/locations/*/synonymSets/*}\x12\xd4\x01\n\x10UpdateSynonymSet\x129.google.cloud.contentwarehouse.v1.UpdateSynonymSetRequest\x1a,.google.cloud.contentwarehouse.v1.SynonymSet"W\xdaA\x10name,synonym_set\x82\xd3\xe4\x93\x02>2//v1/{name=projects/*/locations/*/synonymSets/*}:\x0bsynonym_set\x12\xa5\x01\n\x10DeleteSynonymSet\x129.google.cloud.contentwarehouse.v1.DeleteSynonymSetRequest\x1a\x16.google.protobuf.Empty">\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1/{name=projects/*/locations/*/synonymSets/*}\x12\xc8\x01\n\x0fListSynonymSets\x128.google.cloud.contentwarehouse.v1.ListSynonymSetsRequest\x1a9.google.cloud.contentwarehouse.v1.ListSynonymSetsResponse"@\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=projects/*/locations/*}/synonymSets\x1aS\xcaA\x1fcontentwarehouse.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xfe\x01\n$com.google.cloud.contentwarehouse.v1B\x16SynonymSetServiceProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.contentwarehouse.v1.synonymset_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.contentwarehouse.v1B\x16SynonymSetServiceProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1'
    _globals['_SYNONYMSETSERVICE']._loaded_options = None
    _globals['_SYNONYMSETSERVICE']._serialized_options = b'\xcaA\x1fcontentwarehouse.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SYNONYMSETSERVICE'].methods_by_name['CreateSynonymSet']._loaded_options = None
    _globals['_SYNONYMSETSERVICE'].methods_by_name['CreateSynonymSet']._serialized_options = b'\xdaA\x12parent,synonym_set\x82\xd3\xe4\x93\x02>"//v1/{parent=projects/*/locations/*}/synonymSets:\x0bsynonym_set'
    _globals['_SYNONYMSETSERVICE'].methods_by_name['GetSynonymSet']._loaded_options = None
    _globals['_SYNONYMSETSERVICE'].methods_by_name['GetSynonymSet']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1/{name=projects/*/locations/*/synonymSets/*}'
    _globals['_SYNONYMSETSERVICE'].methods_by_name['UpdateSynonymSet']._loaded_options = None
    _globals['_SYNONYMSETSERVICE'].methods_by_name['UpdateSynonymSet']._serialized_options = b'\xdaA\x10name,synonym_set\x82\xd3\xe4\x93\x02>2//v1/{name=projects/*/locations/*/synonymSets/*}:\x0bsynonym_set'
    _globals['_SYNONYMSETSERVICE'].methods_by_name['DeleteSynonymSet']._loaded_options = None
    _globals['_SYNONYMSETSERVICE'].methods_by_name['DeleteSynonymSet']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1/{name=projects/*/locations/*/synonymSets/*}'
    _globals['_SYNONYMSETSERVICE'].methods_by_name['ListSynonymSets']._loaded_options = None
    _globals['_SYNONYMSETSERVICE'].methods_by_name['ListSynonymSets']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=projects/*/locations/*}/synonymSets'
    _globals['_SYNONYMSETSERVICE']._serialized_start = 298
    _globals['_SYNONYMSETSERVICE']._serialized_end = 1389