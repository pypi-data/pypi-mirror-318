"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/pubsub/v1/schema.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dgoogle/pubsub/v1/schema.proto\x12\x10google.pubsub.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbd\x02\n\x06Schema\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12+\n\x04type\x18\x02 \x01(\x0e2\x1d.google.pubsub.v1.Schema.Type\x12\x12\n\ndefinition\x18\x03 \x01(\t\x12\x1b\n\x0brevision_id\x18\x04 \x01(\tB\x06\xe0A\x05\xe0A\x03\x12=\n\x14revision_create_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03";\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fPROTOCOL_BUFFER\x10\x01\x12\x08\n\x04AVRO\x10\x02:F\xeaAC\n\x1cpubsub.googleapis.com/Schema\x12#projects/{project}/schemas/{schema}"\x8d\x01\n\x13CreateSchemaRequest\x124\n\x06parent\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\x12\x1cpubsub.googleapis.com/Schema\x12-\n\x06schema\x18\x02 \x01(\x0b2\x18.google.pubsub.v1.SchemaB\x03\xe0A\x02\x12\x11\n\tschema_id\x18\x03 \x01(\t"r\n\x10GetSchemaRequest\x122\n\x04name\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cpubsub.googleapis.com/Schema\x12*\n\x04view\x18\x02 \x01(\x0e2\x1c.google.pubsub.v1.SchemaView"\xac\x01\n\x12ListSchemasRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12*\n\x04view\x18\x02 \x01(\x0e2\x1c.google.pubsub.v1.SchemaView\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"Y\n\x13ListSchemasResponse\x12)\n\x07schemas\x18\x01 \x03(\x0b2\x18.google.pubsub.v1.Schema\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xa3\x01\n\x1aListSchemaRevisionsRequest\x122\n\x04name\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cpubsub.googleapis.com/Schema\x12*\n\x04view\x18\x02 \x01(\x0e2\x1c.google.pubsub.v1.SchemaView\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"a\n\x1bListSchemaRevisionsResponse\x12)\n\x07schemas\x18\x01 \x03(\x0b2\x18.google.pubsub.v1.Schema\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"x\n\x13CommitSchemaRequest\x122\n\x04name\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cpubsub.googleapis.com/Schema\x12-\n\x06schema\x18\x02 \x01(\x0b2\x18.google.pubsub.v1.SchemaB\x03\xe0A\x02"e\n\x15RollbackSchemaRequest\x122\n\x04name\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cpubsub.googleapis.com/Schema\x12\x18\n\x0brevision_id\x18\x02 \x01(\tB\x03\xe0A\x02"m\n\x1bDeleteSchemaRevisionRequest\x122\n\x04name\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cpubsub.googleapis.com/Schema\x12\x1a\n\x0brevision_id\x18\x02 \x01(\tB\x05\x18\x01\xe0A\x01"I\n\x13DeleteSchemaRequest\x122\n\x04name\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cpubsub.googleapis.com/Schema"\x8b\x01\n\x15ValidateSchemaRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12-\n\x06schema\x18\x02 \x01(\x0b2\x18.google.pubsub.v1.SchemaB\x03\xe0A\x02"\x18\n\x16ValidateSchemaResponse"\x8a\x02\n\x16ValidateMessageRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x121\n\x04name\x18\x02 \x01(\tB!\xfaA\x1e\n\x1cpubsub.googleapis.com/SchemaH\x00\x12*\n\x06schema\x18\x03 \x01(\x0b2\x18.google.pubsub.v1.SchemaH\x00\x12\x0f\n\x07message\x18\x04 \x01(\x0c\x12,\n\x08encoding\x18\x05 \x01(\x0e2\x1a.google.pubsub.v1.EncodingB\r\n\x0bschema_spec"\x19\n\x17ValidateMessageResponse*>\n\nSchemaView\x12\x1b\n\x17SCHEMA_VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x08\n\x04FULL\x10\x02*:\n\x08Encoding\x12\x18\n\x14ENCODING_UNSPECIFIED\x10\x00\x12\x08\n\x04JSON\x10\x01\x12\n\n\x06BINARY\x10\x022\x88\r\n\rSchemaService\x12\x9a\x01\n\x0cCreateSchema\x12%.google.pubsub.v1.CreateSchemaRequest\x1a\x18.google.pubsub.v1.Schema"I\xdaA\x17parent,schema,schema_id\x82\xd3\xe4\x93\x02)"\x1f/v1/{parent=projects/*}/schemas:\x06schema\x12y\n\tGetSchema\x12".google.pubsub.v1.GetSchemaRequest\x1a\x18.google.pubsub.v1.Schema".\xdaA\x04name\x82\xd3\xe4\x93\x02!\x12\x1f/v1/{name=projects/*/schemas/*}\x12\x8c\x01\n\x0bListSchemas\x12$.google.pubsub.v1.ListSchemasRequest\x1a%.google.pubsub.v1.ListSchemasResponse"0\xdaA\x06parent\x82\xd3\xe4\x93\x02!\x12\x1f/v1/{parent=projects/*}/schemas\x12\xb0\x01\n\x13ListSchemaRevisions\x12,.google.pubsub.v1.ListSchemaRevisionsRequest\x1a-.google.pubsub.v1.ListSchemaRevisionsResponse"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/schemas/*}:listRevisions\x12\x90\x01\n\x0cCommitSchema\x12%.google.pubsub.v1.CommitSchemaRequest\x1a\x18.google.pubsub.v1.Schema"?\xdaA\x0bname,schema\x82\xd3\xe4\x93\x02+"&/v1/{name=projects/*/schemas/*}:commit:\x01*\x12\x9b\x01\n\x0eRollbackSchema\x12\'.google.pubsub.v1.RollbackSchemaRequest\x1a\x18.google.pubsub.v1.Schema"F\xdaA\x10name,revision_id\x82\xd3\xe4\x93\x02-"(/v1/{name=projects/*/schemas/*}:rollback:\x01*\x12\xaa\x01\n\x14DeleteSchemaRevision\x12-.google.pubsub.v1.DeleteSchemaRevisionRequest\x1a\x18.google.pubsub.v1.Schema"I\xdaA\x10name,revision_id\x82\xd3\xe4\x93\x020*./v1/{name=projects/*/schemas/*}:deleteRevision\x12}\n\x0cDeleteSchema\x12%.google.pubsub.v1.DeleteSchemaRequest\x1a\x16.google.protobuf.Empty".\xdaA\x04name\x82\xd3\xe4\x93\x02!*\x1f/v1/{name=projects/*/schemas/*}\x12\xa8\x01\n\x0eValidateSchema\x12\'.google.pubsub.v1.ValidateSchemaRequest\x1a(.google.pubsub.v1.ValidateSchemaResponse"C\xdaA\rparent,schema\x82\xd3\xe4\x93\x02-"(/v1/{parent=projects/*}/schemas:validate:\x01*\x12\xa2\x01\n\x0fValidateMessage\x12(.google.pubsub.v1.ValidateMessageRequest\x1a).google.pubsub.v1.ValidateMessageResponse":\x82\xd3\xe4\x93\x024"//v1/{parent=projects/*}/schemas:validateMessage:\x01*\x1ap\xcaA\x15pubsub.googleapis.com\xd2AUhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/pubsubB\xaa\x01\n\x14com.google.pubsub.v1B\x0bSchemaProtoP\x01Z2cloud.google.com/go/pubsub/apiv1/pubsubpb;pubsubpb\xf8\x01\x01\xaa\x02\x16Google.Cloud.PubSub.V1\xca\x02\x16Google\\Cloud\\PubSub\\V1\xea\x02\x19Google::Cloud::PubSub::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.pubsub.v1.schema_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x14com.google.pubsub.v1B\x0bSchemaProtoP\x01Z2cloud.google.com/go/pubsub/apiv1/pubsubpb;pubsubpb\xf8\x01\x01\xaa\x02\x16Google.Cloud.PubSub.V1\xca\x02\x16Google\\Cloud\\PubSub\\V1\xea\x02\x19Google::Cloud::PubSub::V1'
    _globals['_SCHEMA'].fields_by_name['name']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_SCHEMA'].fields_by_name['revision_id']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['revision_id']._serialized_options = b'\xe0A\x05\xe0A\x03'
    _globals['_SCHEMA'].fields_by_name['revision_create_time']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['revision_create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SCHEMA']._loaded_options = None
    _globals['_SCHEMA']._serialized_options = b'\xeaAC\n\x1cpubsub.googleapis.com/Schema\x12#projects/{project}/schemas/{schema}'
    _globals['_CREATESCHEMAREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESCHEMAREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1e\x12\x1cpubsub.googleapis.com/Schema'
    _globals['_CREATESCHEMAREQUEST'].fields_by_name['schema']._loaded_options = None
    _globals['_CREATESCHEMAREQUEST'].fields_by_name['schema']._serialized_options = b'\xe0A\x02'
    _globals['_GETSCHEMAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSCHEMAREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cpubsub.googleapis.com/Schema'
    _globals['_LISTSCHEMASREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSCHEMASREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_LISTSCHEMAREVISIONSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LISTSCHEMAREVISIONSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cpubsub.googleapis.com/Schema'
    _globals['_COMMITSCHEMAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_COMMITSCHEMAREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cpubsub.googleapis.com/Schema'
    _globals['_COMMITSCHEMAREQUEST'].fields_by_name['schema']._loaded_options = None
    _globals['_COMMITSCHEMAREQUEST'].fields_by_name['schema']._serialized_options = b'\xe0A\x02'
    _globals['_ROLLBACKSCHEMAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_ROLLBACKSCHEMAREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cpubsub.googleapis.com/Schema'
    _globals['_ROLLBACKSCHEMAREQUEST'].fields_by_name['revision_id']._loaded_options = None
    _globals['_ROLLBACKSCHEMAREQUEST'].fields_by_name['revision_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESCHEMAREVISIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESCHEMAREVISIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cpubsub.googleapis.com/Schema'
    _globals['_DELETESCHEMAREVISIONREQUEST'].fields_by_name['revision_id']._loaded_options = None
    _globals['_DELETESCHEMAREVISIONREQUEST'].fields_by_name['revision_id']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_DELETESCHEMAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESCHEMAREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cpubsub.googleapis.com/Schema'
    _globals['_VALIDATESCHEMAREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_VALIDATESCHEMAREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_VALIDATESCHEMAREQUEST'].fields_by_name['schema']._loaded_options = None
    _globals['_VALIDATESCHEMAREQUEST'].fields_by_name['schema']._serialized_options = b'\xe0A\x02'
    _globals['_VALIDATEMESSAGEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_VALIDATEMESSAGEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_VALIDATEMESSAGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_VALIDATEMESSAGEREQUEST'].fields_by_name['name']._serialized_options = b'\xfaA\x1e\n\x1cpubsub.googleapis.com/Schema'
    _globals['_SCHEMASERVICE']._loaded_options = None
    _globals['_SCHEMASERVICE']._serialized_options = b'\xcaA\x15pubsub.googleapis.com\xd2AUhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/pubsub'
    _globals['_SCHEMASERVICE'].methods_by_name['CreateSchema']._loaded_options = None
    _globals['_SCHEMASERVICE'].methods_by_name['CreateSchema']._serialized_options = b'\xdaA\x17parent,schema,schema_id\x82\xd3\xe4\x93\x02)"\x1f/v1/{parent=projects/*}/schemas:\x06schema'
    _globals['_SCHEMASERVICE'].methods_by_name['GetSchema']._loaded_options = None
    _globals['_SCHEMASERVICE'].methods_by_name['GetSchema']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02!\x12\x1f/v1/{name=projects/*/schemas/*}'
    _globals['_SCHEMASERVICE'].methods_by_name['ListSchemas']._loaded_options = None
    _globals['_SCHEMASERVICE'].methods_by_name['ListSchemas']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02!\x12\x1f/v1/{parent=projects/*}/schemas'
    _globals['_SCHEMASERVICE'].methods_by_name['ListSchemaRevisions']._loaded_options = None
    _globals['_SCHEMASERVICE'].methods_by_name['ListSchemaRevisions']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/schemas/*}:listRevisions'
    _globals['_SCHEMASERVICE'].methods_by_name['CommitSchema']._loaded_options = None
    _globals['_SCHEMASERVICE'].methods_by_name['CommitSchema']._serialized_options = b'\xdaA\x0bname,schema\x82\xd3\xe4\x93\x02+"&/v1/{name=projects/*/schemas/*}:commit:\x01*'
    _globals['_SCHEMASERVICE'].methods_by_name['RollbackSchema']._loaded_options = None
    _globals['_SCHEMASERVICE'].methods_by_name['RollbackSchema']._serialized_options = b'\xdaA\x10name,revision_id\x82\xd3\xe4\x93\x02-"(/v1/{name=projects/*/schemas/*}:rollback:\x01*'
    _globals['_SCHEMASERVICE'].methods_by_name['DeleteSchemaRevision']._loaded_options = None
    _globals['_SCHEMASERVICE'].methods_by_name['DeleteSchemaRevision']._serialized_options = b'\xdaA\x10name,revision_id\x82\xd3\xe4\x93\x020*./v1/{name=projects/*/schemas/*}:deleteRevision'
    _globals['_SCHEMASERVICE'].methods_by_name['DeleteSchema']._loaded_options = None
    _globals['_SCHEMASERVICE'].methods_by_name['DeleteSchema']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02!*\x1f/v1/{name=projects/*/schemas/*}'
    _globals['_SCHEMASERVICE'].methods_by_name['ValidateSchema']._loaded_options = None
    _globals['_SCHEMASERVICE'].methods_by_name['ValidateSchema']._serialized_options = b'\xdaA\rparent,schema\x82\xd3\xe4\x93\x02-"(/v1/{parent=projects/*}/schemas:validate:\x01*'
    _globals['_SCHEMASERVICE'].methods_by_name['ValidateMessage']._loaded_options = None
    _globals['_SCHEMASERVICE'].methods_by_name['ValidateMessage']._serialized_options = b'\x82\xd3\xe4\x93\x024"//v1/{parent=projects/*}/schemas:validateMessage:\x01*'
    _globals['_SCHEMAVIEW']._serialized_start = 2214
    _globals['_SCHEMAVIEW']._serialized_end = 2276
    _globals['_ENCODING']._serialized_start = 2278
    _globals['_ENCODING']._serialized_end = 2336
    _globals['_SCHEMA']._serialized_start = 229
    _globals['_SCHEMA']._serialized_end = 546
    _globals['_SCHEMA_TYPE']._serialized_start = 415
    _globals['_SCHEMA_TYPE']._serialized_end = 474
    _globals['_CREATESCHEMAREQUEST']._serialized_start = 549
    _globals['_CREATESCHEMAREQUEST']._serialized_end = 690
    _globals['_GETSCHEMAREQUEST']._serialized_start = 692
    _globals['_GETSCHEMAREQUEST']._serialized_end = 806
    _globals['_LISTSCHEMASREQUEST']._serialized_start = 809
    _globals['_LISTSCHEMASREQUEST']._serialized_end = 981
    _globals['_LISTSCHEMASRESPONSE']._serialized_start = 983
    _globals['_LISTSCHEMASRESPONSE']._serialized_end = 1072
    _globals['_LISTSCHEMAREVISIONSREQUEST']._serialized_start = 1075
    _globals['_LISTSCHEMAREVISIONSREQUEST']._serialized_end = 1238
    _globals['_LISTSCHEMAREVISIONSRESPONSE']._serialized_start = 1240
    _globals['_LISTSCHEMAREVISIONSRESPONSE']._serialized_end = 1337
    _globals['_COMMITSCHEMAREQUEST']._serialized_start = 1339
    _globals['_COMMITSCHEMAREQUEST']._serialized_end = 1459
    _globals['_ROLLBACKSCHEMAREQUEST']._serialized_start = 1461
    _globals['_ROLLBACKSCHEMAREQUEST']._serialized_end = 1562
    _globals['_DELETESCHEMAREVISIONREQUEST']._serialized_start = 1564
    _globals['_DELETESCHEMAREVISIONREQUEST']._serialized_end = 1673
    _globals['_DELETESCHEMAREQUEST']._serialized_start = 1675
    _globals['_DELETESCHEMAREQUEST']._serialized_end = 1748
    _globals['_VALIDATESCHEMAREQUEST']._serialized_start = 1751
    _globals['_VALIDATESCHEMAREQUEST']._serialized_end = 1890
    _globals['_VALIDATESCHEMARESPONSE']._serialized_start = 1892
    _globals['_VALIDATESCHEMARESPONSE']._serialized_end = 1916
    _globals['_VALIDATEMESSAGEREQUEST']._serialized_start = 1919
    _globals['_VALIDATEMESSAGEREQUEST']._serialized_end = 2185
    _globals['_VALIDATEMESSAGERESPONSE']._serialized_start = 2187
    _globals['_VALIDATEMESSAGERESPONSE']._serialized_end = 2212
    _globals['_SCHEMASERVICE']._serialized_start = 2339
    _globals['_SCHEMASERVICE']._serialized_end = 4011