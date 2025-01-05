"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/contentwarehouse/v1/document_schema_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.contentwarehouse.v1 import document_schema_pb2 as google_dot_cloud_dot_contentwarehouse_dot_v1_dot_document__schema__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/contentwarehouse/v1/document_schema_service.proto\x12 google.cloud.contentwarehouse.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a6google/cloud/contentwarehouse/v1/document_schema.proto\x1a\x1bgoogle/protobuf/empty.proto"\xaf\x01\n\x1bCreateDocumentSchemaRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Location\x12N\n\x0fdocument_schema\x18\x02 \x01(\x0b20.google.cloud.contentwarehouse.v1.DocumentSchemaB\x03\xe0A\x02"`\n\x18GetDocumentSchemaRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.contentwarehouse.googleapis.com/DocumentSchema"\xb3\x01\n\x1bUpdateDocumentSchemaRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.contentwarehouse.googleapis.com/DocumentSchema\x12N\n\x0fdocument_schema\x18\x02 \x01(\x0b20.google.cloud.contentwarehouse.v1.DocumentSchemaB\x03\xe0A\x02"c\n\x1bDeleteDocumentSchemaRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.contentwarehouse.googleapis.com/DocumentSchema"\x85\x01\n\x1aListDocumentSchemasRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x82\x01\n\x1bListDocumentSchemasResponse\x12J\n\x10document_schemas\x18\x01 \x03(\x0b20.google.cloud.contentwarehouse.v1.DocumentSchema\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x95\t\n\x15DocumentSchemaService\x12\xee\x01\n\x14CreateDocumentSchema\x12=.google.cloud.contentwarehouse.v1.CreateDocumentSchemaRequest\x1a0.google.cloud.contentwarehouse.v1.DocumentSchema"e\xdaA\x16parent,document_schema\x82\xd3\xe4\x93\x02F"3/v1/{parent=projects/*/locations/*}/documentSchemas:\x0fdocument_schema\x12\xde\x01\n\x14UpdateDocumentSchema\x12=.google.cloud.contentwarehouse.v1.UpdateDocumentSchemaRequest\x1a0.google.cloud.contentwarehouse.v1.DocumentSchema"U\xdaA\x14name,document_schema\x82\xd3\xe4\x93\x02823/v1/{name=projects/*/locations/*/documentSchemas/*}:\x01*\x12\xc5\x01\n\x11GetDocumentSchema\x12:.google.cloud.contentwarehouse.v1.GetDocumentSchemaRequest\x1a0.google.cloud.contentwarehouse.v1.DocumentSchema"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1/{name=projects/*/locations/*/documentSchemas/*}\x12\xb1\x01\n\x14DeleteDocumentSchema\x12=.google.cloud.contentwarehouse.v1.DeleteDocumentSchemaRequest\x1a\x16.google.protobuf.Empty"B\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1/{name=projects/*/locations/*/documentSchemas/*}\x12\xd8\x01\n\x13ListDocumentSchemas\x12<.google.cloud.contentwarehouse.v1.ListDocumentSchemasRequest\x1a=.google.cloud.contentwarehouse.v1.ListDocumentSchemasResponse"D\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1/{parent=projects/*/locations/*}/documentSchemas\x1aS\xcaA\x1fcontentwarehouse.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x82\x02\n$com.google.cloud.contentwarehouse.v1B\x1aDocumentSchemaServiceProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.contentwarehouse.v1.document_schema_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.contentwarehouse.v1B\x1aDocumentSchemaServiceProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1'
    _globals['_CREATEDOCUMENTSCHEMAREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDOCUMENTSCHEMAREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Location'
    _globals['_CREATEDOCUMENTSCHEMAREQUEST'].fields_by_name['document_schema']._loaded_options = None
    _globals['_CREATEDOCUMENTSCHEMAREQUEST'].fields_by_name['document_schema']._serialized_options = b'\xe0A\x02'
    _globals['_GETDOCUMENTSCHEMAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDOCUMENTSCHEMAREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.contentwarehouse.googleapis.com/DocumentSchema'
    _globals['_UPDATEDOCUMENTSCHEMAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATEDOCUMENTSCHEMAREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.contentwarehouse.googleapis.com/DocumentSchema'
    _globals['_UPDATEDOCUMENTSCHEMAREQUEST'].fields_by_name['document_schema']._loaded_options = None
    _globals['_UPDATEDOCUMENTSCHEMAREQUEST'].fields_by_name['document_schema']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEDOCUMENTSCHEMAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDOCUMENTSCHEMAREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.contentwarehouse.googleapis.com/DocumentSchema'
    _globals['_LISTDOCUMENTSCHEMASREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDOCUMENTSCHEMASREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Location'
    _globals['_DOCUMENTSCHEMASERVICE']._loaded_options = None
    _globals['_DOCUMENTSCHEMASERVICE']._serialized_options = b'\xcaA\x1fcontentwarehouse.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DOCUMENTSCHEMASERVICE'].methods_by_name['CreateDocumentSchema']._loaded_options = None
    _globals['_DOCUMENTSCHEMASERVICE'].methods_by_name['CreateDocumentSchema']._serialized_options = b'\xdaA\x16parent,document_schema\x82\xd3\xe4\x93\x02F"3/v1/{parent=projects/*/locations/*}/documentSchemas:\x0fdocument_schema'
    _globals['_DOCUMENTSCHEMASERVICE'].methods_by_name['UpdateDocumentSchema']._loaded_options = None
    _globals['_DOCUMENTSCHEMASERVICE'].methods_by_name['UpdateDocumentSchema']._serialized_options = b'\xdaA\x14name,document_schema\x82\xd3\xe4\x93\x02823/v1/{name=projects/*/locations/*/documentSchemas/*}:\x01*'
    _globals['_DOCUMENTSCHEMASERVICE'].methods_by_name['GetDocumentSchema']._loaded_options = None
    _globals['_DOCUMENTSCHEMASERVICE'].methods_by_name['GetDocumentSchema']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1/{name=projects/*/locations/*/documentSchemas/*}'
    _globals['_DOCUMENTSCHEMASERVICE'].methods_by_name['DeleteDocumentSchema']._loaded_options = None
    _globals['_DOCUMENTSCHEMASERVICE'].methods_by_name['DeleteDocumentSchema']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1/{name=projects/*/locations/*/documentSchemas/*}'
    _globals['_DOCUMENTSCHEMASERVICE'].methods_by_name['ListDocumentSchemas']._loaded_options = None
    _globals['_DOCUMENTSCHEMASERVICE'].methods_by_name['ListDocumentSchemas']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1/{parent=projects/*/locations/*}/documentSchemas'
    _globals['_CREATEDOCUMENTSCHEMAREQUEST']._serialized_start = 301
    _globals['_CREATEDOCUMENTSCHEMAREQUEST']._serialized_end = 476
    _globals['_GETDOCUMENTSCHEMAREQUEST']._serialized_start = 478
    _globals['_GETDOCUMENTSCHEMAREQUEST']._serialized_end = 574
    _globals['_UPDATEDOCUMENTSCHEMAREQUEST']._serialized_start = 577
    _globals['_UPDATEDOCUMENTSCHEMAREQUEST']._serialized_end = 756
    _globals['_DELETEDOCUMENTSCHEMAREQUEST']._serialized_start = 758
    _globals['_DELETEDOCUMENTSCHEMAREQUEST']._serialized_end = 857
    _globals['_LISTDOCUMENTSCHEMASREQUEST']._serialized_start = 860
    _globals['_LISTDOCUMENTSCHEMASREQUEST']._serialized_end = 993
    _globals['_LISTDOCUMENTSCHEMASRESPONSE']._serialized_start = 996
    _globals['_LISTDOCUMENTSCHEMASRESPONSE']._serialized_end = 1126
    _globals['_DOCUMENTSCHEMASERVICE']._serialized_start = 1129
    _globals['_DOCUMENTSCHEMASERVICE']._serialized_end = 2302