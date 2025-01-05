"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1/data_store_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import data_store_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_data__store__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/discoveryengine/v1/data_store_service.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/discoveryengine/v1/data_store.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x87\x02\n\x16CreateDataStoreRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/Collection\x12C\n\ndata_store\x18\x02 \x01(\x0b2*.google.cloud.discoveryengine.v1.DataStoreB\x03\xe0A\x02\x12\x1a\n\rdata_store_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12#\n\x1bcreate_advanced_site_search\x18\x04 \x01(\x08\x12$\n\x1cskip_default_schema_creation\x18\x07 \x01(\x08"U\n\x13GetDataStoreRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore"{\n\x17CreateDataStoreMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x91\x01\n\x15ListDataStoresRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/Collection\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"r\n\x16ListDataStoresResponse\x12?\n\x0bdata_stores\x18\x01 \x03(\x0b2*.google.cloud.discoveryengine.v1.DataStore\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"X\n\x16DeleteDataStoreRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore"\x8e\x01\n\x16UpdateDataStoreRequest\x12C\n\ndata_store\x18\x01 \x01(\x0b2*.google.cloud.discoveryengine.v1.DataStoreB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"{\n\x17DeleteDataStoreMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp2\xdd\x0c\n\x10DataStoreService\x12\x84\x03\n\x0fCreateDataStore\x127.google.cloud.discoveryengine.v1.CreateDataStoreRequest\x1a\x1d.google.longrunning.Operation"\x98\x02\xcaAd\n)google.cloud.discoveryengine.v1.DataStore\x127google.cloud.discoveryengine.v1.CreateDataStoreMetadata\xdaA\x1fparent,data_store,data_store_id\x82\xd3\xe4\x93\x02\x88\x01"./v1/{parent=projects/*/locations/*}/dataStores:\ndata_storeZJ"</v1/{parent=projects/*/locations/*/collections/*}/dataStores:\ndata_store\x12\xef\x01\n\x0cGetDataStore\x124.google.cloud.discoveryengine.v1.GetDataStoreRequest\x1a*.google.cloud.discoveryengine.v1.DataStore"}\xdaA\x04name\x82\xd3\xe4\x93\x02p\x12./v1/{name=projects/*/locations/*/dataStores/*}Z>\x12</v1/{name=projects/*/locations/*/collections/*/dataStores/*}\x12\x82\x02\n\x0eListDataStores\x126.google.cloud.discoveryengine.v1.ListDataStoresRequest\x1a7.google.cloud.discoveryengine.v1.ListDataStoresResponse"\x7f\xdaA\x06parent\x82\xd3\xe4\x93\x02p\x12./v1/{parent=projects/*/locations/*}/dataStoresZ>\x12</v1/{parent=projects/*/locations/*/collections/*}/dataStores\x12\xbc\x02\n\x0fDeleteDataStore\x127.google.cloud.discoveryengine.v1.DeleteDataStoreRequest\x1a\x1d.google.longrunning.Operation"\xd0\x01\xcaAP\n\x15google.protobuf.Empty\x127google.cloud.discoveryengine.v1.DeleteDataStoreMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02p*./v1/{name=projects/*/locations/*/dataStores/*}Z>*</v1/{name=projects/*/locations/*/collections/*/dataStores/*}\x12\xb7\x02\n\x0fUpdateDataStore\x127.google.cloud.discoveryengine.v1.UpdateDataStoreRequest\x1a*.google.cloud.discoveryengine.v1.DataStore"\xbe\x01\xdaA\x16data_store,update_mask\x82\xd3\xe4\x93\x02\x9e\x0129/v1/{data_store.name=projects/*/locations/*/dataStores/*}:\ndata_storeZU2G/v1/{data_store.name=projects/*/locations/*/collections/*/dataStores/*}:\ndata_store\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x88\x02\n#com.google.cloud.discoveryengine.v1B\x15DataStoreServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.data_store_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x15DataStoreServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
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
    _globals['_DATASTORESERVICE']._loaded_options = None
    _globals['_DATASTORESERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DATASTORESERVICE'].methods_by_name['CreateDataStore']._loaded_options = None
    _globals['_DATASTORESERVICE'].methods_by_name['CreateDataStore']._serialized_options = b'\xcaAd\n)google.cloud.discoveryengine.v1.DataStore\x127google.cloud.discoveryengine.v1.CreateDataStoreMetadata\xdaA\x1fparent,data_store,data_store_id\x82\xd3\xe4\x93\x02\x88\x01"./v1/{parent=projects/*/locations/*}/dataStores:\ndata_storeZJ"</v1/{parent=projects/*/locations/*/collections/*}/dataStores:\ndata_store'
    _globals['_DATASTORESERVICE'].methods_by_name['GetDataStore']._loaded_options = None
    _globals['_DATASTORESERVICE'].methods_by_name['GetDataStore']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02p\x12./v1/{name=projects/*/locations/*/dataStores/*}Z>\x12</v1/{name=projects/*/locations/*/collections/*/dataStores/*}'
    _globals['_DATASTORESERVICE'].methods_by_name['ListDataStores']._loaded_options = None
    _globals['_DATASTORESERVICE'].methods_by_name['ListDataStores']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02p\x12./v1/{parent=projects/*/locations/*}/dataStoresZ>\x12</v1/{parent=projects/*/locations/*/collections/*}/dataStores'
    _globals['_DATASTORESERVICE'].methods_by_name['DeleteDataStore']._loaded_options = None
    _globals['_DATASTORESERVICE'].methods_by_name['DeleteDataStore']._serialized_options = b'\xcaAP\n\x15google.protobuf.Empty\x127google.cloud.discoveryengine.v1.DeleteDataStoreMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02p*./v1/{name=projects/*/locations/*/dataStores/*}Z>*</v1/{name=projects/*/locations/*/collections/*/dataStores/*}'
    _globals['_DATASTORESERVICE'].methods_by_name['UpdateDataStore']._loaded_options = None
    _globals['_DATASTORESERVICE'].methods_by_name['UpdateDataStore']._serialized_options = b'\xdaA\x16data_store,update_mask\x82\xd3\xe4\x93\x02\x9e\x0129/v1/{data_store.name=projects/*/locations/*/dataStores/*}:\ndata_storeZU2G/v1/{data_store.name=projects/*/locations/*/collections/*/dataStores/*}:\ndata_store'
    _globals['_CREATEDATASTOREREQUEST']._serialized_start = 392
    _globals['_CREATEDATASTOREREQUEST']._serialized_end = 655
    _globals['_GETDATASTOREREQUEST']._serialized_start = 657
    _globals['_GETDATASTOREREQUEST']._serialized_end = 742
    _globals['_CREATEDATASTOREMETADATA']._serialized_start = 744
    _globals['_CREATEDATASTOREMETADATA']._serialized_end = 867
    _globals['_LISTDATASTORESREQUEST']._serialized_start = 870
    _globals['_LISTDATASTORESREQUEST']._serialized_end = 1015
    _globals['_LISTDATASTORESRESPONSE']._serialized_start = 1017
    _globals['_LISTDATASTORESRESPONSE']._serialized_end = 1131
    _globals['_DELETEDATASTOREREQUEST']._serialized_start = 1133
    _globals['_DELETEDATASTOREREQUEST']._serialized_end = 1221
    _globals['_UPDATEDATASTOREREQUEST']._serialized_start = 1224
    _globals['_UPDATEDATASTOREREQUEST']._serialized_end = 1366
    _globals['_DELETEDATASTOREMETADATA']._serialized_start = 1368
    _globals['_DELETEDATASTOREMETADATA']._serialized_end = 1491
    _globals['_DATASTORESERVICE']._serialized_start = 1494
    _globals['_DATASTORESERVICE']._serialized_end = 3123