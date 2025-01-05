"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1alpha/data_store_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1alpha import data_store_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_data__store__pb2
from .....google.cloud.discoveryengine.v1alpha import document_processing_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_document__processing__config__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/discoveryengine/v1alpha/data_store_service.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/discoveryengine/v1alpha/data_store.proto\x1aEgoogle/cloud/discoveryengine/v1alpha/document_processing_config.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8c\x02\n\x16CreateDataStoreRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/Collection\x12H\n\ndata_store\x18\x02 \x01(\x0b2/.google.cloud.discoveryengine.v1alpha.DataStoreB\x03\xe0A\x02\x12\x1a\n\rdata_store_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12#\n\x1bcreate_advanced_site_search\x18\x04 \x01(\x08\x12$\n\x1cskip_default_schema_creation\x18\x07 \x01(\x08"U\n\x13GetDataStoreRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore"{\n\x17CreateDataStoreMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x91\x01\n\x15ListDataStoresRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/Collection\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"w\n\x16ListDataStoresResponse\x12D\n\x0bdata_stores\x18\x01 \x03(\x0b2/.google.cloud.discoveryengine.v1alpha.DataStore\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"X\n\x16DeleteDataStoreRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore"\x93\x01\n\x16UpdateDataStoreRequest\x12H\n\ndata_store\x18\x01 \x01(\x0b2/.google.cloud.discoveryengine.v1alpha.DataStoreB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"{\n\x17DeleteDataStoreMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"s\n"GetDocumentProcessingConfigRequest\x12M\n\x04name\x18\x01 \x01(\tB?\xe0A\x02\xfaA9\n7discoveryengine.googleapis.com/DocumentProcessingConfig"\xc1\x01\n%UpdateDocumentProcessingConfigRequest\x12g\n\x1adocument_processing_config\x18\x01 \x01(\x0b2>.google.cloud.discoveryengine.v1alpha.DocumentProcessingConfigB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask2\xad\x14\n\x10DataStoreService\x12\x9d\x03\n\x0fCreateDataStore\x12<.google.cloud.discoveryengine.v1alpha.CreateDataStoreRequest\x1a\x1d.google.longrunning.Operation"\xac\x02\xcaAn\n.google.cloud.discoveryengine.v1alpha.DataStore\x12<google.cloud.discoveryengine.v1alpha.CreateDataStoreMetadata\xdaA\x1fparent,data_store,data_store_id\x82\xd3\xe4\x93\x02\x92\x01"3/v1alpha/{parent=projects/*/locations/*}/dataStores:\ndata_storeZO"A/v1alpha/{parent=projects/*/locations/*/collections/*}/dataStores:\ndata_store\x12\x84\x02\n\x0cGetDataStore\x129.google.cloud.discoveryengine.v1alpha.GetDataStoreRequest\x1a/.google.cloud.discoveryengine.v1alpha.DataStore"\x87\x01\xdaA\x04name\x82\xd3\xe4\x93\x02z\x123/v1alpha/{name=projects/*/locations/*/dataStores/*}ZC\x12A/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*}\x12\x97\x02\n\x0eListDataStores\x12;.google.cloud.discoveryengine.v1alpha.ListDataStoresRequest\x1a<.google.cloud.discoveryengine.v1alpha.ListDataStoresResponse"\x89\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02z\x123/v1alpha/{parent=projects/*/locations/*}/dataStoresZC\x12A/v1alpha/{parent=projects/*/locations/*/collections/*}/dataStores\x12\xd0\x02\n\x0fDeleteDataStore\x12<.google.cloud.discoveryengine.v1alpha.DeleteDataStoreRequest\x1a\x1d.google.longrunning.Operation"\xdf\x01\xcaAU\n\x15google.protobuf.Empty\x12<google.cloud.discoveryengine.v1alpha.DeleteDataStoreMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02z*3/v1alpha/{name=projects/*/locations/*/dataStores/*}ZC*A/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*}\x12\xcb\x02\n\x0fUpdateDataStore\x12<.google.cloud.discoveryengine.v1alpha.UpdateDataStoreRequest\x1a/.google.cloud.discoveryengine.v1alpha.DataStore"\xc8\x01\xdaA\x16data_store,update_mask\x82\xd3\xe4\x93\x02\xa8\x012>/v1alpha/{data_store.name=projects/*/locations/*/dataStores/*}:\ndata_storeZZ2L/v1alpha/{data_store.name=projects/*/locations/*/collections/*/dataStores/*}:\ndata_store\x12\xe4\x02\n\x1bGetDocumentProcessingConfig\x12H.google.cloud.discoveryengine.v1alpha.GetDocumentProcessingConfigRequest\x1a>.google.cloud.discoveryengine.v1alpha.DocumentProcessingConfig"\xba\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xac\x01\x12L/v1alpha/{name=projects/*/locations/*/dataStores/*/documentProcessingConfig}Z\\\x12Z/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*/documentProcessingConfig}\x12\xfb\x03\n\x1eUpdateDocumentProcessingConfig\x12K.google.cloud.discoveryengine.v1alpha.UpdateDocumentProcessingConfigRequest\x1a>.google.cloud.discoveryengine.v1alpha.DocumentProcessingConfig"\xcb\x02\xdaA&document_processing_config,update_mask\x82\xd3\xe4\x93\x02\x9b\x022g/v1alpha/{document_processing_config.name=projects/*/locations/*/dataStores/*/documentProcessingConfig}:\x1adocument_processing_configZ\x93\x012u/v1alpha/{document_processing_config.name=projects/*/locations/*/collections/*/dataStores/*/documentProcessingConfig}:\x1adocument_processing_config\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa1\x02\n(com.google.cloud.discoveryengine.v1alphaB\x15DataStoreServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.data_store_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x15DataStoreServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
    _globals['_CREATEDATASTOREREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDATASTOREREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/Collection'
    _globals['_CREATEDATASTOREREQUEST'].fields_by_name['data_store']._loaded_options = None
    _globals['_CREATEDATASTOREREQUEST'].fields_by_name['data_store']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDATASTOREREQUEST'].fields_by_name['data_store_id']._loaded_options = None
    _globals['_CREATEDATASTOREREQUEST'].fields_by_name['data_store_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETDATASTOREREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATASTOREREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_LISTDATASTORESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATASTORESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/Collection'
    _globals['_DELETEDATASTOREREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDATASTOREREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_UPDATEDATASTOREREQUEST'].fields_by_name['data_store']._loaded_options = None
    _globals['_UPDATEDATASTOREREQUEST'].fields_by_name['data_store']._serialized_options = b'\xe0A\x02'
    _globals['_GETDOCUMENTPROCESSINGCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDOCUMENTPROCESSINGCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA9\n7discoveryengine.googleapis.com/DocumentProcessingConfig'
    _globals['_UPDATEDOCUMENTPROCESSINGCONFIGREQUEST'].fields_by_name['document_processing_config']._loaded_options = None
    _globals['_UPDATEDOCUMENTPROCESSINGCONFIGREQUEST'].fields_by_name['document_processing_config']._serialized_options = b'\xe0A\x02'
    _globals['_DATASTORESERVICE']._loaded_options = None
    _globals['_DATASTORESERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DATASTORESERVICE'].methods_by_name['CreateDataStore']._loaded_options = None
    _globals['_DATASTORESERVICE'].methods_by_name['CreateDataStore']._serialized_options = b'\xcaAn\n.google.cloud.discoveryengine.v1alpha.DataStore\x12<google.cloud.discoveryengine.v1alpha.CreateDataStoreMetadata\xdaA\x1fparent,data_store,data_store_id\x82\xd3\xe4\x93\x02\x92\x01"3/v1alpha/{parent=projects/*/locations/*}/dataStores:\ndata_storeZO"A/v1alpha/{parent=projects/*/locations/*/collections/*}/dataStores:\ndata_store'
    _globals['_DATASTORESERVICE'].methods_by_name['GetDataStore']._loaded_options = None
    _globals['_DATASTORESERVICE'].methods_by_name['GetDataStore']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02z\x123/v1alpha/{name=projects/*/locations/*/dataStores/*}ZC\x12A/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*}'
    _globals['_DATASTORESERVICE'].methods_by_name['ListDataStores']._loaded_options = None
    _globals['_DATASTORESERVICE'].methods_by_name['ListDataStores']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02z\x123/v1alpha/{parent=projects/*/locations/*}/dataStoresZC\x12A/v1alpha/{parent=projects/*/locations/*/collections/*}/dataStores'
    _globals['_DATASTORESERVICE'].methods_by_name['DeleteDataStore']._loaded_options = None
    _globals['_DATASTORESERVICE'].methods_by_name['DeleteDataStore']._serialized_options = b'\xcaAU\n\x15google.protobuf.Empty\x12<google.cloud.discoveryengine.v1alpha.DeleteDataStoreMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02z*3/v1alpha/{name=projects/*/locations/*/dataStores/*}ZC*A/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*}'
    _globals['_DATASTORESERVICE'].methods_by_name['UpdateDataStore']._loaded_options = None
    _globals['_DATASTORESERVICE'].methods_by_name['UpdateDataStore']._serialized_options = b'\xdaA\x16data_store,update_mask\x82\xd3\xe4\x93\x02\xa8\x012>/v1alpha/{data_store.name=projects/*/locations/*/dataStores/*}:\ndata_storeZZ2L/v1alpha/{data_store.name=projects/*/locations/*/collections/*/dataStores/*}:\ndata_store'
    _globals['_DATASTORESERVICE'].methods_by_name['GetDocumentProcessingConfig']._loaded_options = None
    _globals['_DATASTORESERVICE'].methods_by_name['GetDocumentProcessingConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xac\x01\x12L/v1alpha/{name=projects/*/locations/*/dataStores/*/documentProcessingConfig}Z\\\x12Z/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*/documentProcessingConfig}'
    _globals['_DATASTORESERVICE'].methods_by_name['UpdateDocumentProcessingConfig']._loaded_options = None
    _globals['_DATASTORESERVICE'].methods_by_name['UpdateDocumentProcessingConfig']._serialized_options = b'\xdaA&document_processing_config,update_mask\x82\xd3\xe4\x93\x02\x9b\x022g/v1alpha/{document_processing_config.name=projects/*/locations/*/dataStores/*/documentProcessingConfig}:\x1adocument_processing_configZ\x93\x012u/v1alpha/{document_processing_config.name=projects/*/locations/*/collections/*/dataStores/*/documentProcessingConfig}:\x1adocument_processing_config'
    _globals['_CREATEDATASTOREREQUEST']._serialized_start = 478
    _globals['_CREATEDATASTOREREQUEST']._serialized_end = 746
    _globals['_GETDATASTOREREQUEST']._serialized_start = 748
    _globals['_GETDATASTOREREQUEST']._serialized_end = 833
    _globals['_CREATEDATASTOREMETADATA']._serialized_start = 835
    _globals['_CREATEDATASTOREMETADATA']._serialized_end = 958
    _globals['_LISTDATASTORESREQUEST']._serialized_start = 961
    _globals['_LISTDATASTORESREQUEST']._serialized_end = 1106
    _globals['_LISTDATASTORESRESPONSE']._serialized_start = 1108
    _globals['_LISTDATASTORESRESPONSE']._serialized_end = 1227
    _globals['_DELETEDATASTOREREQUEST']._serialized_start = 1229
    _globals['_DELETEDATASTOREREQUEST']._serialized_end = 1317
    _globals['_UPDATEDATASTOREREQUEST']._serialized_start = 1320
    _globals['_UPDATEDATASTOREREQUEST']._serialized_end = 1467
    _globals['_DELETEDATASTOREMETADATA']._serialized_start = 1469
    _globals['_DELETEDATASTOREMETADATA']._serialized_end = 1592
    _globals['_GETDOCUMENTPROCESSINGCONFIGREQUEST']._serialized_start = 1594
    _globals['_GETDOCUMENTPROCESSINGCONFIGREQUEST']._serialized_end = 1709
    _globals['_UPDATEDOCUMENTPROCESSINGCONFIGREQUEST']._serialized_start = 1712
    _globals['_UPDATEDOCUMENTPROCESSINGCONFIGREQUEST']._serialized_end = 1905
    _globals['_DATASTORESERVICE']._serialized_start = 1908
    _globals['_DATASTORESERVICE']._serialized_end = 4513