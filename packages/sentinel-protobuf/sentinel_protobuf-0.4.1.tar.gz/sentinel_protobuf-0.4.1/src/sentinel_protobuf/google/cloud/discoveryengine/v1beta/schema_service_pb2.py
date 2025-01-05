"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1beta/schema_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1beta import schema_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_schema__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/discoveryengine/v1beta/schema_service.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/discoveryengine/v1beta/schema.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"O\n\x10GetSchemaRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Schema"}\n\x12ListSchemasRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"l\n\x13ListSchemasResponse\x12<\n\x07schemas\x18\x01 \x03(\x0b2+.google.cloud.discoveryengine.v1beta.Schema\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xb1\x01\n\x13CreateSchemaRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x12@\n\x06schema\x18\x02 \x01(\x0b2+.google.cloud.discoveryengine.v1beta.SchemaB\x03\xe0A\x02\x12\x16\n\tschema_id\x18\x03 \x01(\tB\x03\xe0A\x02"n\n\x13UpdateSchemaRequest\x12@\n\x06schema\x18\x01 \x01(\x0b2+.google.cloud.discoveryengine.v1beta.SchemaB\x03\xe0A\x02\x12\x15\n\rallow_missing\x18\x03 \x01(\x08"R\n\x13DeleteSchemaRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Schema"x\n\x14CreateSchemaMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"x\n\x14UpdateSchemaMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"x\n\x14DeleteSchemaMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp2\x89\x0e\n\rSchemaService\x12\x8c\x02\n\tGetSchema\x125.google.cloud.discoveryengine.v1beta.GetSchemaRequest\x1a+.google.cloud.discoveryengine.v1beta.Schema"\x9a\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x8c\x01\x12</v1beta/{name=projects/*/locations/*/dataStores/*/schemas/*}ZL\x12J/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/schemas/*}\x12\x9f\x02\n\x0bListSchemas\x127.google.cloud.discoveryengine.v1beta.ListSchemasRequest\x1a8.google.cloud.discoveryengine.v1beta.ListSchemasResponse"\x9c\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\x8c\x01\x12</v1beta/{parent=projects/*/locations/*/dataStores/*}/schemasZL\x12J/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*}/schemas\x12\x90\x03\n\x0cCreateSchema\x128.google.cloud.discoveryengine.v1beta.CreateSchemaRequest\x1a\x1d.google.longrunning.Operation"\xa6\x02\xcaAf\n*google.cloud.discoveryengine.v1beta.Schema\x128google.cloud.discoveryengine.v1beta.CreateSchemaMetadata\xdaA\x17parent,schema,schema_id\x82\xd3\xe4\x93\x02\x9c\x01"</v1beta/{parent=projects/*/locations/*/dataStores/*}/schemas:\x06schemaZT"J/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*}/schemas:\x06schema\x12\x84\x03\n\x0cUpdateSchema\x128.google.cloud.discoveryengine.v1beta.UpdateSchemaRequest\x1a\x1d.google.longrunning.Operation"\x9a\x02\xcaAf\n*google.cloud.discoveryengine.v1beta.Schema\x128google.cloud.discoveryengine.v1beta.UpdateSchemaMetadata\x82\xd3\xe4\x93\x02\xaa\x012C/v1beta/{schema.name=projects/*/locations/*/dataStores/*/schemas/*}:\x06schemaZ[2Q/v1beta/{schema.name=projects/*/locations/*/collections/*/dataStores/*/schemas/*}:\x06schema\x12\xd8\x02\n\x0cDeleteSchema\x128.google.cloud.discoveryengine.v1beta.DeleteSchemaRequest\x1a\x1d.google.longrunning.Operation"\xee\x01\xcaAQ\n\x15google.protobuf.Empty\x128google.cloud.discoveryengine.v1beta.DeleteSchemaMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x8c\x01*</v1beta/{name=projects/*/locations/*/dataStores/*/schemas/*}ZL*J/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/schemas/*}\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x99\x02\n\'com.google.cloud.discoveryengine.v1betaB\x12SchemaServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.schema_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x12SchemaServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
    _globals['_GETSCHEMAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSCHEMAREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%discoveryengine.googleapis.com/Schema"
    _globals['_LISTSCHEMASREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSCHEMASREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_CREATESCHEMAREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESCHEMAREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_CREATESCHEMAREQUEST'].fields_by_name['schema']._loaded_options = None
    _globals['_CREATESCHEMAREQUEST'].fields_by_name['schema']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESCHEMAREQUEST'].fields_by_name['schema_id']._loaded_options = None
    _globals['_CREATESCHEMAREQUEST'].fields_by_name['schema_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESCHEMAREQUEST'].fields_by_name['schema']._loaded_options = None
    _globals['_UPDATESCHEMAREQUEST'].fields_by_name['schema']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESCHEMAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESCHEMAREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%discoveryengine.googleapis.com/Schema"
    _globals['_SCHEMASERVICE']._loaded_options = None
    _globals['_SCHEMASERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SCHEMASERVICE'].methods_by_name['GetSchema']._loaded_options = None
    _globals['_SCHEMASERVICE'].methods_by_name['GetSchema']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x8c\x01\x12</v1beta/{name=projects/*/locations/*/dataStores/*/schemas/*}ZL\x12J/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/schemas/*}'
    _globals['_SCHEMASERVICE'].methods_by_name['ListSchemas']._loaded_options = None
    _globals['_SCHEMASERVICE'].methods_by_name['ListSchemas']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x8c\x01\x12</v1beta/{parent=projects/*/locations/*/dataStores/*}/schemasZL\x12J/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*}/schemas'
    _globals['_SCHEMASERVICE'].methods_by_name['CreateSchema']._loaded_options = None
    _globals['_SCHEMASERVICE'].methods_by_name['CreateSchema']._serialized_options = b'\xcaAf\n*google.cloud.discoveryengine.v1beta.Schema\x128google.cloud.discoveryengine.v1beta.CreateSchemaMetadata\xdaA\x17parent,schema,schema_id\x82\xd3\xe4\x93\x02\x9c\x01"</v1beta/{parent=projects/*/locations/*/dataStores/*}/schemas:\x06schemaZT"J/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*}/schemas:\x06schema'
    _globals['_SCHEMASERVICE'].methods_by_name['UpdateSchema']._loaded_options = None
    _globals['_SCHEMASERVICE'].methods_by_name['UpdateSchema']._serialized_options = b'\xcaAf\n*google.cloud.discoveryengine.v1beta.Schema\x128google.cloud.discoveryengine.v1beta.UpdateSchemaMetadata\x82\xd3\xe4\x93\x02\xaa\x012C/v1beta/{schema.name=projects/*/locations/*/dataStores/*/schemas/*}:\x06schemaZ[2Q/v1beta/{schema.name=projects/*/locations/*/collections/*/dataStores/*/schemas/*}:\x06schema'
    _globals['_SCHEMASERVICE'].methods_by_name['DeleteSchema']._loaded_options = None
    _globals['_SCHEMASERVICE'].methods_by_name['DeleteSchema']._serialized_options = b'\xcaAQ\n\x15google.protobuf.Empty\x128google.cloud.discoveryengine.v1beta.DeleteSchemaMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x8c\x01*</v1beta/{name=projects/*/locations/*/dataStores/*/schemas/*}ZL*J/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/schemas/*}'
    _globals['_GETSCHEMAREQUEST']._serialized_start = 361
    _globals['_GETSCHEMAREQUEST']._serialized_end = 440
    _globals['_LISTSCHEMASREQUEST']._serialized_start = 442
    _globals['_LISTSCHEMASREQUEST']._serialized_end = 567
    _globals['_LISTSCHEMASRESPONSE']._serialized_start = 569
    _globals['_LISTSCHEMASRESPONSE']._serialized_end = 677
    _globals['_CREATESCHEMAREQUEST']._serialized_start = 680
    _globals['_CREATESCHEMAREQUEST']._serialized_end = 857
    _globals['_UPDATESCHEMAREQUEST']._serialized_start = 859
    _globals['_UPDATESCHEMAREQUEST']._serialized_end = 969
    _globals['_DELETESCHEMAREQUEST']._serialized_start = 971
    _globals['_DELETESCHEMAREQUEST']._serialized_end = 1053
    _globals['_CREATESCHEMAMETADATA']._serialized_start = 1055
    _globals['_CREATESCHEMAMETADATA']._serialized_end = 1175
    _globals['_UPDATESCHEMAMETADATA']._serialized_start = 1177
    _globals['_UPDATESCHEMAMETADATA']._serialized_end = 1297
    _globals['_DELETESCHEMAMETADATA']._serialized_start = 1299
    _globals['_DELETESCHEMAMETADATA']._serialized_end = 1419
    _globals['_SCHEMASERVICE']._serialized_start = 1422
    _globals['_SCHEMASERVICE']._serialized_end = 3223