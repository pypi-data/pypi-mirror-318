"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/datastore/admin/v1/datastore_admin.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.datastore.admin.v1 import index_pb2 as google_dot_datastore_dot_admin_dot_v1_dot_index__pb2
from .....google.datastore.admin.v1 import migration_pb2 as google_dot_datastore_dot_admin_dot_v1_dot_migration__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/datastore/admin/v1/datastore_admin.proto\x12\x19google.datastore.admin.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a%google/datastore/admin/v1/index.proto\x1a)google/datastore/admin/v1/migration.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf4\x03\n\x0eCommonMetadata\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12@\n\x0eoperation_type\x18\x03 \x01(\x0e2(.google.datastore.admin.v1.OperationType\x12E\n\x06labels\x18\x04 \x03(\x0b25.google.datastore.admin.v1.CommonMetadata.LabelsEntry\x12>\n\x05state\x18\x05 \x01(\x0e2/.google.datastore.admin.v1.CommonMetadata.State\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x8b\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cINITIALIZING\x10\x01\x12\x0e\n\nPROCESSING\x10\x02\x12\x0e\n\nCANCELLING\x10\x03\x12\x0e\n\nFINALIZING\x10\x04\x12\x0e\n\nSUCCESSFUL\x10\x05\x12\n\n\x06FAILED\x10\x06\x12\r\n\tCANCELLED\x10\x07":\n\x08Progress\x12\x16\n\x0ework_completed\x18\x01 \x01(\x03\x12\x16\n\x0ework_estimated\x18\x02 \x01(\x03"\x8d\x02\n\x15ExportEntitiesRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12L\n\x06labels\x18\x02 \x03(\x0b2<.google.datastore.admin.v1.ExportEntitiesRequest.LabelsEntry\x12>\n\rentity_filter\x18\x03 \x01(\x0b2\'.google.datastore.admin.v1.EntityFilter\x12\x1e\n\x11output_url_prefix\x18\x04 \x01(\tB\x03\xe0A\x02\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x85\x02\n\x15ImportEntitiesRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12L\n\x06labels\x18\x02 \x03(\x0b2<.google.datastore.admin.v1.ImportEntitiesRequest.LabelsEntry\x12\x16\n\tinput_url\x18\x03 \x01(\tB\x03\xe0A\x02\x12>\n\rentity_filter\x18\x04 \x01(\x0b2\'.google.datastore.admin.v1.EntityFilter\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01",\n\x16ExportEntitiesResponse\x12\x12\n\noutput_url\x18\x01 \x01(\t"\xab\x02\n\x16ExportEntitiesMetadata\x129\n\x06common\x18\x01 \x01(\x0b2).google.datastore.admin.v1.CommonMetadata\x12>\n\x11progress_entities\x18\x02 \x01(\x0b2#.google.datastore.admin.v1.Progress\x12;\n\x0eprogress_bytes\x18\x03 \x01(\x0b2#.google.datastore.admin.v1.Progress\x12>\n\rentity_filter\x18\x04 \x01(\x0b2\'.google.datastore.admin.v1.EntityFilter\x12\x19\n\x11output_url_prefix\x18\x05 \x01(\t"\xa3\x02\n\x16ImportEntitiesMetadata\x129\n\x06common\x18\x01 \x01(\x0b2).google.datastore.admin.v1.CommonMetadata\x12>\n\x11progress_entities\x18\x02 \x01(\x0b2#.google.datastore.admin.v1.Progress\x12;\n\x0eprogress_bytes\x18\x03 \x01(\x0b2#.google.datastore.admin.v1.Progress\x12>\n\rentity_filter\x18\x04 \x01(\x0b2\'.google.datastore.admin.v1.EntityFilter\x12\x11\n\tinput_url\x18\x05 \x01(\t"4\n\x0cEntityFilter\x12\r\n\x05kinds\x18\x01 \x03(\t\x12\x15\n\rnamespace_ids\x18\x02 \x03(\t"Y\n\x12CreateIndexRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12/\n\x05index\x18\x03 \x01(\x0b2 .google.datastore.admin.v1.Index":\n\x12DeleteIndexRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x10\n\x08index_id\x18\x03 \x01(\t"7\n\x0fGetIndexRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x10\n\x08index_id\x18\x03 \x01(\t"_\n\x12ListIndexesRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0e\n\x06filter\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t"a\n\x13ListIndexesResponse\x121\n\x07indexes\x18\x01 \x03(\x0b2 .google.datastore.admin.v1.Index\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xa5\x01\n\x16IndexOperationMetadata\x129\n\x06common\x18\x01 \x01(\x0b2).google.datastore.admin.v1.CommonMetadata\x12>\n\x11progress_entities\x18\x02 \x01(\x0b2#.google.datastore.admin.v1.Progress\x12\x10\n\x08index_id\x18\x03 \x01(\t"\xab\x01\n#DatastoreFirestoreMigrationMetadata\x12B\n\x0fmigration_state\x18\x01 \x01(\x0e2).google.datastore.admin.v1.MigrationState\x12@\n\x0emigration_step\x18\x02 \x01(\x0e2(.google.datastore.admin.v1.MigrationStep*}\n\rOperationType\x12\x1e\n\x1aOPERATION_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fEXPORT_ENTITIES\x10\x01\x12\x13\n\x0fIMPORT_ENTITIES\x10\x02\x12\x10\n\x0cCREATE_INDEX\x10\x03\x12\x10\n\x0cDELETE_INDEX\x10\x042\x84\n\n\x0eDatastoreAdmin\x12\xf6\x01\n\x0eExportEntities\x120.google.datastore.admin.v1.ExportEntitiesRequest\x1a\x1d.google.longrunning.Operation"\x92\x01\xcaA0\n\x16ExportEntitiesResponse\x12\x16ExportEntitiesMetadata\xdaA1project_id,labels,entity_filter,output_url_prefix\x82\xd3\xe4\x93\x02%" /v1/projects/{project_id}:export:\x01*\x12\xed\x01\n\x0eImportEntities\x120.google.datastore.admin.v1.ImportEntitiesRequest\x1a\x1d.google.longrunning.Operation"\x89\x01\xcaA/\n\x15google.protobuf.Empty\x12\x16ImportEntitiesMetadata\xdaA)project_id,labels,input_url,entity_filter\x82\xd3\xe4\x93\x02%" /v1/projects/{project_id}:import:\x01*\x12\xaf\x01\n\x0bCreateIndex\x12-.google.datastore.admin.v1.CreateIndexRequest\x1a\x1d.google.longrunning.Operation"R\xcaA\x1f\n\x05Index\x12\x16IndexOperationMetadata\x82\xd3\xe4\x93\x02*"!/v1/projects/{project_id}/indexes:\x05index\x12\xb3\x01\n\x0bDeleteIndex\x12-.google.datastore.admin.v1.DeleteIndexRequest\x1a\x1d.google.longrunning.Operation"V\xcaA\x1f\n\x05Index\x12\x16IndexOperationMetadata\x82\xd3\xe4\x93\x02.*,/v1/projects/{project_id}/indexes/{index_id}\x12\x8e\x01\n\x08GetIndex\x12*.google.datastore.admin.v1.GetIndexRequest\x1a .google.datastore.admin.v1.Index"4\x82\xd3\xe4\x93\x02.\x12,/v1/projects/{project_id}/indexes/{index_id}\x12\x97\x01\n\x0bListIndexes\x12-.google.datastore.admin.v1.ListIndexesRequest\x1a..google.datastore.admin.v1.ListIndexesResponse")\x82\xd3\xe4\x93\x02#\x12!/v1/projects/{project_id}/indexes\x1av\xcaA\x18datastore.googleapis.com\xd2AXhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/datastoreB\xdb\x01\n\x1dcom.google.datastore.admin.v1B\x13DatastoreAdminProtoP\x01Z9cloud.google.com/go/datastore/admin/apiv1/adminpb;adminpb\xaa\x02\x1fGoogle.Cloud.Datastore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Datastore\\Admin\\V1\xea\x02#Google::Cloud::Datastore::Admin::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.datastore.admin.v1.datastore_admin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.datastore.admin.v1B\x13DatastoreAdminProtoP\x01Z9cloud.google.com/go/datastore/admin/apiv1/adminpb;adminpb\xaa\x02\x1fGoogle.Cloud.Datastore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Datastore\\Admin\\V1\xea\x02#Google::Cloud::Datastore::Admin::V1'
    _globals['_COMMONMETADATA_LABELSENTRY']._loaded_options = None
    _globals['_COMMONMETADATA_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_EXPORTENTITIESREQUEST_LABELSENTRY']._loaded_options = None
    _globals['_EXPORTENTITIESREQUEST_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_EXPORTENTITIESREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_EXPORTENTITIESREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_EXPORTENTITIESREQUEST'].fields_by_name['output_url_prefix']._loaded_options = None
    _globals['_EXPORTENTITIESREQUEST'].fields_by_name['output_url_prefix']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTENTITIESREQUEST_LABELSENTRY']._loaded_options = None
    _globals['_IMPORTENTITIESREQUEST_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_IMPORTENTITIESREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_IMPORTENTITIESREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTENTITIESREQUEST'].fields_by_name['input_url']._loaded_options = None
    _globals['_IMPORTENTITIESREQUEST'].fields_by_name['input_url']._serialized_options = b'\xe0A\x02'
    _globals['_DATASTOREADMIN']._loaded_options = None
    _globals['_DATASTOREADMIN']._serialized_options = b'\xcaA\x18datastore.googleapis.com\xd2AXhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/datastore'
    _globals['_DATASTOREADMIN'].methods_by_name['ExportEntities']._loaded_options = None
    _globals['_DATASTOREADMIN'].methods_by_name['ExportEntities']._serialized_options = b'\xcaA0\n\x16ExportEntitiesResponse\x12\x16ExportEntitiesMetadata\xdaA1project_id,labels,entity_filter,output_url_prefix\x82\xd3\xe4\x93\x02%" /v1/projects/{project_id}:export:\x01*'
    _globals['_DATASTOREADMIN'].methods_by_name['ImportEntities']._loaded_options = None
    _globals['_DATASTOREADMIN'].methods_by_name['ImportEntities']._serialized_options = b'\xcaA/\n\x15google.protobuf.Empty\x12\x16ImportEntitiesMetadata\xdaA)project_id,labels,input_url,entity_filter\x82\xd3\xe4\x93\x02%" /v1/projects/{project_id}:import:\x01*'
    _globals['_DATASTOREADMIN'].methods_by_name['CreateIndex']._loaded_options = None
    _globals['_DATASTOREADMIN'].methods_by_name['CreateIndex']._serialized_options = b'\xcaA\x1f\n\x05Index\x12\x16IndexOperationMetadata\x82\xd3\xe4\x93\x02*"!/v1/projects/{project_id}/indexes:\x05index'
    _globals['_DATASTOREADMIN'].methods_by_name['DeleteIndex']._loaded_options = None
    _globals['_DATASTOREADMIN'].methods_by_name['DeleteIndex']._serialized_options = b'\xcaA\x1f\n\x05Index\x12\x16IndexOperationMetadata\x82\xd3\xe4\x93\x02.*,/v1/projects/{project_id}/indexes/{index_id}'
    _globals['_DATASTOREADMIN'].methods_by_name['GetIndex']._loaded_options = None
    _globals['_DATASTOREADMIN'].methods_by_name['GetIndex']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/v1/projects/{project_id}/indexes/{index_id}'
    _globals['_DATASTOREADMIN'].methods_by_name['ListIndexes']._loaded_options = None
    _globals['_DATASTOREADMIN'].methods_by_name['ListIndexes']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/v1/projects/{project_id}/indexes'
    _globals['_OPERATIONTYPE']._serialized_start = 2859
    _globals['_OPERATIONTYPE']._serialized_end = 2984
    _globals['_COMMONMETADATA']._serialized_start = 319
    _globals['_COMMONMETADATA']._serialized_end = 819
    _globals['_COMMONMETADATA_LABELSENTRY']._serialized_start = 632
    _globals['_COMMONMETADATA_LABELSENTRY']._serialized_end = 677
    _globals['_COMMONMETADATA_STATE']._serialized_start = 680
    _globals['_COMMONMETADATA_STATE']._serialized_end = 819
    _globals['_PROGRESS']._serialized_start = 821
    _globals['_PROGRESS']._serialized_end = 879
    _globals['_EXPORTENTITIESREQUEST']._serialized_start = 882
    _globals['_EXPORTENTITIESREQUEST']._serialized_end = 1151
    _globals['_EXPORTENTITIESREQUEST_LABELSENTRY']._serialized_start = 632
    _globals['_EXPORTENTITIESREQUEST_LABELSENTRY']._serialized_end = 677
    _globals['_IMPORTENTITIESREQUEST']._serialized_start = 1154
    _globals['_IMPORTENTITIESREQUEST']._serialized_end = 1415
    _globals['_IMPORTENTITIESREQUEST_LABELSENTRY']._serialized_start = 632
    _globals['_IMPORTENTITIESREQUEST_LABELSENTRY']._serialized_end = 677
    _globals['_EXPORTENTITIESRESPONSE']._serialized_start = 1417
    _globals['_EXPORTENTITIESRESPONSE']._serialized_end = 1461
    _globals['_EXPORTENTITIESMETADATA']._serialized_start = 1464
    _globals['_EXPORTENTITIESMETADATA']._serialized_end = 1763
    _globals['_IMPORTENTITIESMETADATA']._serialized_start = 1766
    _globals['_IMPORTENTITIESMETADATA']._serialized_end = 2057
    _globals['_ENTITYFILTER']._serialized_start = 2059
    _globals['_ENTITYFILTER']._serialized_end = 2111
    _globals['_CREATEINDEXREQUEST']._serialized_start = 2113
    _globals['_CREATEINDEXREQUEST']._serialized_end = 2202
    _globals['_DELETEINDEXREQUEST']._serialized_start = 2204
    _globals['_DELETEINDEXREQUEST']._serialized_end = 2262
    _globals['_GETINDEXREQUEST']._serialized_start = 2264
    _globals['_GETINDEXREQUEST']._serialized_end = 2319
    _globals['_LISTINDEXESREQUEST']._serialized_start = 2321
    _globals['_LISTINDEXESREQUEST']._serialized_end = 2416
    _globals['_LISTINDEXESRESPONSE']._serialized_start = 2418
    _globals['_LISTINDEXESRESPONSE']._serialized_end = 2515
    _globals['_INDEXOPERATIONMETADATA']._serialized_start = 2518
    _globals['_INDEXOPERATIONMETADATA']._serialized_end = 2683
    _globals['_DATASTOREFIRESTOREMIGRATIONMETADATA']._serialized_start = 2686
    _globals['_DATASTOREFIRESTOREMIGRATIONMETADATA']._serialized_end = 2857
    _globals['_DATASTOREADMIN']._serialized_start = 2987
    _globals['_DATASTOREADMIN']._serialized_end = 4271