"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2/document.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dialogflow.v2 import gcs_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_gcs__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/dialogflow/v2/document.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a$google/cloud/dialogflow/v2/gcs.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xa6\x08\n\x08Document\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x16\n\tmime_type\x18\x03 \x01(\tB\x03\xe0A\x02\x12P\n\x0fknowledge_types\x18\x04 \x03(\x0e22.google.cloud.dialogflow.v2.Document.KnowledgeTypeB\x03\xe0A\x02\x12\x15\n\x0bcontent_uri\x18\x05 \x01(\tH\x00\x12\x15\n\x0braw_content\x18\t \x01(\x0cH\x00\x12\x1f\n\x12enable_auto_reload\x18\x0b \x01(\x08B\x03\xe0A\x01\x12T\n\x14latest_reload_status\x18\x0c \x01(\x0b21.google.cloud.dialogflow.v2.Document.ReloadStatusB\x03\xe0A\x03\x12I\n\x08metadata\x18\x07 \x03(\x0b22.google.cloud.dialogflow.v2.Document.MetadataEntryB\x03\xe0A\x01\x12>\n\x05state\x18\r \x01(\x0e2*.google.cloud.dialogflow.v2.Document.StateB\x03\xe0A\x03\x1a\\\n\x0cReloadStatus\x12(\n\x04time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12"\n\x06status\x18\x02 \x01(\x0b2\x12.google.rpc.Status\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x81\x01\n\rKnowledgeType\x12\x1e\n\x1aKNOWLEDGE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03FAQ\x10\x01\x12\x11\n\rEXTRACTIVE_QA\x10\x02\x12\x16\n\x12ARTICLE_SUGGESTION\x10\x03\x12\x1c\n\x18AGENT_FACING_SMART_REPLY\x10\x04"c\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\r\n\tRELOADING\x10\x04\x12\x0c\n\x08DELETING\x10\x05:\xcf\x01\xeaA\xcb\x01\n"dialogflow.googleapis.com/Document\x12Gprojects/{project}/knowledgeBases/{knowledge_base}/documents/{document}\x12\\projects/{project}/locations/{location}/knowledgeBases/{knowledge_base}/documents/{document}B\x08\n\x06source"N\n\x12GetDocumentRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/Document"\x89\x01\n\x14ListDocumentsRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/Document\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"i\n\x15ListDocumentsResponse\x127\n\tdocuments\x18\x01 \x03(\x0b2$.google.cloud.dialogflow.v2.Document\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x90\x01\n\x15CreateDocumentRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/Document\x12;\n\x08document\x18\x02 \x01(\x0b2$.google.cloud.dialogflow.v2.DocumentB\x03\xe0A\x02"\x99\x02\n\x16ImportDocumentsRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/Document\x12A\n\ngcs_source\x18\x02 \x01(\x0b2&.google.cloud.dialogflow.v2.GcsSourcesB\x03\xe0A\x01H\x00\x12R\n\x11document_template\x18\x03 \x01(\x0b22.google.cloud.dialogflow.v2.ImportDocumentTemplateB\x03\xe0A\x02\x12"\n\x1aimport_gcs_custom_metadata\x18\x04 \x01(\x08B\x08\n\x06source"\x87\x02\n\x16ImportDocumentTemplate\x12\x16\n\tmime_type\x18\x01 \x01(\tB\x03\xe0A\x02\x12P\n\x0fknowledge_types\x18\x02 \x03(\x0e22.google.cloud.dialogflow.v2.Document.KnowledgeTypeB\x03\xe0A\x02\x12R\n\x08metadata\x18\x03 \x03(\x0b2@.google.cloud.dialogflow.v2.ImportDocumentTemplate.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"?\n\x17ImportDocumentsResponse\x12$\n\x08warnings\x18\x01 \x03(\x0b2\x12.google.rpc.Status"Q\n\x15DeleteDocumentRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/Document"\x8a\x01\n\x15UpdateDocumentRequest\x12;\n\x08document\x18\x01 \x01(\x0b2$.google.cloud.dialogflow.v2.DocumentB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\xcd\x01\n\x15ReloadDocumentRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/Document\x12\x1a\n\x0bcontent_uri\x18\x03 \x01(\tB\x03\xe0A\x01H\x00\x12\'\n\x1aimport_gcs_custom_metadata\x18\x04 \x01(\x08B\x03\xe0A\x01\x12+\n\x1esmart_messaging_partial_update\x18\x05 \x01(\x08B\x03\xe0A\x01B\x08\n\x06source"\xec\x01\n\x15ExportDocumentRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/Document\x12E\n\x0fgcs_destination\x18\x02 \x01(\x0b2*.google.cloud.dialogflow.v2.GcsDestinationH\x00\x12\x1b\n\x13export_full_content\x18\x03 \x01(\x08\x12&\n\x1esmart_messaging_partial_update\x18\x05 \x01(\x08B\r\n\x0bdestination"g\n\x17ExportOperationMetadata\x12L\n\x18exported_gcs_destination\x18\x01 \x01(\x0b2*.google.cloud.dialogflow.v2.GcsDestination"\xba\x02\n\x1aKnowledgeOperationMetadata\x12P\n\x05state\x18\x01 \x01(\x0e2<.google.cloud.dialogflow.v2.KnowledgeOperationMetadata.StateB\x03\xe0A\x03\x12\x16\n\x0eknowledge_base\x18\x03 \x01(\t\x12X\n\x19export_operation_metadata\x18\x04 \x01(\x0b23.google.cloud.dialogflow.v2.ExportOperationMetadataH\x00"B\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x08\n\x04DONE\x10\x03B\x14\n\x12operation_metadata2\xac\x16\n\tDocuments\x12\xb9\x02\n\rListDocuments\x120.google.cloud.dialogflow.v2.ListDocumentsRequest\x1a1.google.cloud.dialogflow.v2.ListDocumentsResponse"\xc2\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xb2\x01\x122/v2/{parent=projects/*/knowledgeBases/*}/documentsZ@\x12>/v2/{parent=projects/*/locations/*/knowledgeBases/*}/documentsZ:\x128/v2/{parent=projects/*/agent/knowledgeBases/*}/documents\x12\xa6\x02\n\x0bGetDocument\x12..google.cloud.dialogflow.v2.GetDocumentRequest\x1a$.google.cloud.dialogflow.v2.Document"\xc0\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xb2\x01\x122/v2/{name=projects/*/knowledgeBases/*/documents/*}Z@\x12>/v2/{name=projects/*/locations/*/knowledgeBases/*/documents/*}Z:\x128/v2/{name=projects/*/agent/knowledgeBases/*/documents/*}\x12\xf7\x02\n\x0eCreateDocument\x121.google.cloud.dialogflow.v2.CreateDocumentRequest\x1a\x1d.google.longrunning.Operation"\x92\x02\xcaA&\n\x08Document\x12\x1aKnowledgeOperationMetadata\xdaA\x0fparent,document\x82\xd3\xe4\x93\x02\xd0\x01"2/v2/{parent=projects/*/knowledgeBases/*}/documents:\x08documentZJ">/v2/{parent=projects/*/locations/*/knowledgeBases/*}/documents:\x08documentZD"8/v2/{parent=projects/*/agent/knowledgeBases/*}/documents:\x08document\x12\xb0\x02\n\x0fImportDocuments\x122.google.cloud.dialogflow.v2.ImportDocumentsRequest\x1a\x1d.google.longrunning.Operation"\xc9\x01\xcaA5\n\x17ImportDocumentsResponse\x12\x1aKnowledgeOperationMetadata\x82\xd3\xe4\x93\x02\x8a\x01"9/v2/{parent=projects/*/knowledgeBases/*}/documents:import:\x01*ZJ"E/v2/{parent=projects/*/locations/*/knowledgeBases/*}/documents:import:\x01*\x12\xdb\x02\n\x0eDeleteDocument\x121.google.cloud.dialogflow.v2.DeleteDocumentRequest\x1a\x1d.google.longrunning.Operation"\xf6\x01\xcaA3\n\x15google.protobuf.Empty\x12\x1aKnowledgeOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\xb2\x01*2/v2/{name=projects/*/knowledgeBases/*/documents/*}Z@*>/v2/{name=projects/*/locations/*/knowledgeBases/*/documents/*}Z:*8/v2/{name=projects/*/agent/knowledgeBases/*/documents/*}\x12\x97\x03\n\x0eUpdateDocument\x121.google.cloud.dialogflow.v2.UpdateDocumentRequest\x1a\x1d.google.longrunning.Operation"\xb2\x02\xcaA&\n\x08Document\x12\x1aKnowledgeOperationMetadata\xdaA\x14document,update_mask\x82\xd3\xe4\x93\x02\xeb\x012;/v2/{document.name=projects/*/knowledgeBases/*/documents/*}:\x08documentZS2G/v2/{document.name=projects/*/locations/*/knowledgeBases/*/documents/*}:\x08documentZM2A/v2/{document.name=projects/*/agent/knowledgeBases/*/documents/*}:\x08document\x12\xf8\x02\n\x0eReloadDocument\x121.google.cloud.dialogflow.v2.ReloadDocumentRequest\x1a\x1d.google.longrunning.Operation"\x93\x02\xcaA&\n\x08Document\x12\x1aKnowledgeOperationMetadata\xdaA\x10name,content_uri\x82\xd3\xe4\x93\x02\xd0\x01"9/v2/{name=projects/*/knowledgeBases/*/documents/*}:reload:\x01*ZJ"E/v2/{name=projects/*/locations/*/knowledgeBases/*/documents/*}:reload:\x01*ZD"?/v2/{name=projects/*/agent/knowledgeBases/*/documents/*}:reload:\x01*\x12\x9f\x02\n\x0eExportDocument\x121.google.cloud.dialogflow.v2.ExportDocumentRequest\x1a\x1d.google.longrunning.Operation"\xba\x01\xcaA&\n\x08Document\x12\x1aKnowledgeOperationMetadata\x82\xd3\xe4\x93\x02\x8a\x01"9/v2/{name=projects/*/knowledgeBases/*/documents/*}:export:\x01*ZJ"E/v2/{name=projects/*/locations/*/knowledgeBases/*/documents/*}:export:\x01*\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\x96\x01\n\x1ecom.google.cloud.dialogflow.v2B\rDocumentProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2.document_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.dialogflow.v2B\rDocumentProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2'
    _globals['_DOCUMENT_METADATAENTRY']._loaded_options = None
    _globals['_DOCUMENT_METADATAENTRY']._serialized_options = b'8\x01'
    _globals['_DOCUMENT'].fields_by_name['name']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['name']._serialized_options = b'\xe0A\x01'
    _globals['_DOCUMENT'].fields_by_name['display_name']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_DOCUMENT'].fields_by_name['mime_type']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['mime_type']._serialized_options = b'\xe0A\x02'
    _globals['_DOCUMENT'].fields_by_name['knowledge_types']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['knowledge_types']._serialized_options = b'\xe0A\x02'
    _globals['_DOCUMENT'].fields_by_name['enable_auto_reload']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['enable_auto_reload']._serialized_options = b'\xe0A\x01'
    _globals['_DOCUMENT'].fields_by_name['latest_reload_status']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['latest_reload_status']._serialized_options = b'\xe0A\x03'
    _globals['_DOCUMENT'].fields_by_name['metadata']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['metadata']._serialized_options = b'\xe0A\x01'
    _globals['_DOCUMENT'].fields_by_name['state']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_DOCUMENT']._loaded_options = None
    _globals['_DOCUMENT']._serialized_options = b'\xeaA\xcb\x01\n"dialogflow.googleapis.com/Document\x12Gprojects/{project}/knowledgeBases/{knowledge_base}/documents/{document}\x12\\projects/{project}/locations/{location}/knowledgeBases/{knowledge_base}/documents/{document}'
    _globals['_GETDOCUMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDOCUMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/Document'
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/Document'
    _globals['_CREATEDOCUMENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDOCUMENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/Document'
    _globals['_CREATEDOCUMENTREQUEST'].fields_by_name['document']._loaded_options = None
    _globals['_CREATEDOCUMENTREQUEST'].fields_by_name['document']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTDOCUMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTDOCUMENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/Document'
    _globals['_IMPORTDOCUMENTSREQUEST'].fields_by_name['gcs_source']._loaded_options = None
    _globals['_IMPORTDOCUMENTSREQUEST'].fields_by_name['gcs_source']._serialized_options = b'\xe0A\x01'
    _globals['_IMPORTDOCUMENTSREQUEST'].fields_by_name['document_template']._loaded_options = None
    _globals['_IMPORTDOCUMENTSREQUEST'].fields_by_name['document_template']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTDOCUMENTTEMPLATE_METADATAENTRY']._loaded_options = None
    _globals['_IMPORTDOCUMENTTEMPLATE_METADATAENTRY']._serialized_options = b'8\x01'
    _globals['_IMPORTDOCUMENTTEMPLATE'].fields_by_name['mime_type']._loaded_options = None
    _globals['_IMPORTDOCUMENTTEMPLATE'].fields_by_name['mime_type']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTDOCUMENTTEMPLATE'].fields_by_name['knowledge_types']._loaded_options = None
    _globals['_IMPORTDOCUMENTTEMPLATE'].fields_by_name['knowledge_types']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEDOCUMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDOCUMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/Document'
    _globals['_UPDATEDOCUMENTREQUEST'].fields_by_name['document']._loaded_options = None
    _globals['_UPDATEDOCUMENTREQUEST'].fields_by_name['document']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDOCUMENTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEDOCUMENTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_RELOADDOCUMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RELOADDOCUMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/Document'
    _globals['_RELOADDOCUMENTREQUEST'].fields_by_name['content_uri']._loaded_options = None
    _globals['_RELOADDOCUMENTREQUEST'].fields_by_name['content_uri']._serialized_options = b'\xe0A\x01'
    _globals['_RELOADDOCUMENTREQUEST'].fields_by_name['import_gcs_custom_metadata']._loaded_options = None
    _globals['_RELOADDOCUMENTREQUEST'].fields_by_name['import_gcs_custom_metadata']._serialized_options = b'\xe0A\x01'
    _globals['_RELOADDOCUMENTREQUEST'].fields_by_name['smart_messaging_partial_update']._loaded_options = None
    _globals['_RELOADDOCUMENTREQUEST'].fields_by_name['smart_messaging_partial_update']._serialized_options = b'\xe0A\x01'
    _globals['_EXPORTDOCUMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_EXPORTDOCUMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/Document'
    _globals['_KNOWLEDGEOPERATIONMETADATA'].fields_by_name['state']._loaded_options = None
    _globals['_KNOWLEDGEOPERATIONMETADATA'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_DOCUMENTS']._loaded_options = None
    _globals['_DOCUMENTS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_DOCUMENTS'].methods_by_name['ListDocuments']._loaded_options = None
    _globals['_DOCUMENTS'].methods_by_name['ListDocuments']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xb2\x01\x122/v2/{parent=projects/*/knowledgeBases/*}/documentsZ@\x12>/v2/{parent=projects/*/locations/*/knowledgeBases/*}/documentsZ:\x128/v2/{parent=projects/*/agent/knowledgeBases/*}/documents'
    _globals['_DOCUMENTS'].methods_by_name['GetDocument']._loaded_options = None
    _globals['_DOCUMENTS'].methods_by_name['GetDocument']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xb2\x01\x122/v2/{name=projects/*/knowledgeBases/*/documents/*}Z@\x12>/v2/{name=projects/*/locations/*/knowledgeBases/*/documents/*}Z:\x128/v2/{name=projects/*/agent/knowledgeBases/*/documents/*}'
    _globals['_DOCUMENTS'].methods_by_name['CreateDocument']._loaded_options = None
    _globals['_DOCUMENTS'].methods_by_name['CreateDocument']._serialized_options = b'\xcaA&\n\x08Document\x12\x1aKnowledgeOperationMetadata\xdaA\x0fparent,document\x82\xd3\xe4\x93\x02\xd0\x01"2/v2/{parent=projects/*/knowledgeBases/*}/documents:\x08documentZJ">/v2/{parent=projects/*/locations/*/knowledgeBases/*}/documents:\x08documentZD"8/v2/{parent=projects/*/agent/knowledgeBases/*}/documents:\x08document'
    _globals['_DOCUMENTS'].methods_by_name['ImportDocuments']._loaded_options = None
    _globals['_DOCUMENTS'].methods_by_name['ImportDocuments']._serialized_options = b'\xcaA5\n\x17ImportDocumentsResponse\x12\x1aKnowledgeOperationMetadata\x82\xd3\xe4\x93\x02\x8a\x01"9/v2/{parent=projects/*/knowledgeBases/*}/documents:import:\x01*ZJ"E/v2/{parent=projects/*/locations/*/knowledgeBases/*}/documents:import:\x01*'
    _globals['_DOCUMENTS'].methods_by_name['DeleteDocument']._loaded_options = None
    _globals['_DOCUMENTS'].methods_by_name['DeleteDocument']._serialized_options = b'\xcaA3\n\x15google.protobuf.Empty\x12\x1aKnowledgeOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\xb2\x01*2/v2/{name=projects/*/knowledgeBases/*/documents/*}Z@*>/v2/{name=projects/*/locations/*/knowledgeBases/*/documents/*}Z:*8/v2/{name=projects/*/agent/knowledgeBases/*/documents/*}'
    _globals['_DOCUMENTS'].methods_by_name['UpdateDocument']._loaded_options = None
    _globals['_DOCUMENTS'].methods_by_name['UpdateDocument']._serialized_options = b'\xcaA&\n\x08Document\x12\x1aKnowledgeOperationMetadata\xdaA\x14document,update_mask\x82\xd3\xe4\x93\x02\xeb\x012;/v2/{document.name=projects/*/knowledgeBases/*/documents/*}:\x08documentZS2G/v2/{document.name=projects/*/locations/*/knowledgeBases/*/documents/*}:\x08documentZM2A/v2/{document.name=projects/*/agent/knowledgeBases/*/documents/*}:\x08document'
    _globals['_DOCUMENTS'].methods_by_name['ReloadDocument']._loaded_options = None
    _globals['_DOCUMENTS'].methods_by_name['ReloadDocument']._serialized_options = b'\xcaA&\n\x08Document\x12\x1aKnowledgeOperationMetadata\xdaA\x10name,content_uri\x82\xd3\xe4\x93\x02\xd0\x01"9/v2/{name=projects/*/knowledgeBases/*/documents/*}:reload:\x01*ZJ"E/v2/{name=projects/*/locations/*/knowledgeBases/*/documents/*}:reload:\x01*ZD"?/v2/{name=projects/*/agent/knowledgeBases/*/documents/*}:reload:\x01*'
    _globals['_DOCUMENTS'].methods_by_name['ExportDocument']._loaded_options = None
    _globals['_DOCUMENTS'].methods_by_name['ExportDocument']._serialized_options = b'\xcaA&\n\x08Document\x12\x1aKnowledgeOperationMetadata\x82\xd3\xe4\x93\x02\x8a\x01"9/v2/{name=projects/*/knowledgeBases/*/documents/*}:export:\x01*ZJ"E/v2/{name=projects/*/locations/*/knowledgeBases/*/documents/*}:export:\x01*'
    _globals['_DOCUMENT']._serialized_start = 385
    _globals['_DOCUMENT']._serialized_end = 1447
    _globals['_DOCUMENT_RELOADSTATUS']._serialized_start = 853
    _globals['_DOCUMENT_RELOADSTATUS']._serialized_end = 945
    _globals['_DOCUMENT_METADATAENTRY']._serialized_start = 947
    _globals['_DOCUMENT_METADATAENTRY']._serialized_end = 994
    _globals['_DOCUMENT_KNOWLEDGETYPE']._serialized_start = 997
    _globals['_DOCUMENT_KNOWLEDGETYPE']._serialized_end = 1126
    _globals['_DOCUMENT_STATE']._serialized_start = 1128
    _globals['_DOCUMENT_STATE']._serialized_end = 1227
    _globals['_GETDOCUMENTREQUEST']._serialized_start = 1449
    _globals['_GETDOCUMENTREQUEST']._serialized_end = 1527
    _globals['_LISTDOCUMENTSREQUEST']._serialized_start = 1530
    _globals['_LISTDOCUMENTSREQUEST']._serialized_end = 1667
    _globals['_LISTDOCUMENTSRESPONSE']._serialized_start = 1669
    _globals['_LISTDOCUMENTSRESPONSE']._serialized_end = 1774
    _globals['_CREATEDOCUMENTREQUEST']._serialized_start = 1777
    _globals['_CREATEDOCUMENTREQUEST']._serialized_end = 1921
    _globals['_IMPORTDOCUMENTSREQUEST']._serialized_start = 1924
    _globals['_IMPORTDOCUMENTSREQUEST']._serialized_end = 2205
    _globals['_IMPORTDOCUMENTTEMPLATE']._serialized_start = 2208
    _globals['_IMPORTDOCUMENTTEMPLATE']._serialized_end = 2471
    _globals['_IMPORTDOCUMENTTEMPLATE_METADATAENTRY']._serialized_start = 947
    _globals['_IMPORTDOCUMENTTEMPLATE_METADATAENTRY']._serialized_end = 994
    _globals['_IMPORTDOCUMENTSRESPONSE']._serialized_start = 2473
    _globals['_IMPORTDOCUMENTSRESPONSE']._serialized_end = 2536
    _globals['_DELETEDOCUMENTREQUEST']._serialized_start = 2538
    _globals['_DELETEDOCUMENTREQUEST']._serialized_end = 2619
    _globals['_UPDATEDOCUMENTREQUEST']._serialized_start = 2622
    _globals['_UPDATEDOCUMENTREQUEST']._serialized_end = 2760
    _globals['_RELOADDOCUMENTREQUEST']._serialized_start = 2763
    _globals['_RELOADDOCUMENTREQUEST']._serialized_end = 2968
    _globals['_EXPORTDOCUMENTREQUEST']._serialized_start = 2971
    _globals['_EXPORTDOCUMENTREQUEST']._serialized_end = 3207
    _globals['_EXPORTOPERATIONMETADATA']._serialized_start = 3209
    _globals['_EXPORTOPERATIONMETADATA']._serialized_end = 3312
    _globals['_KNOWLEDGEOPERATIONMETADATA']._serialized_start = 3315
    _globals['_KNOWLEDGEOPERATIONMETADATA']._serialized_end = 3629
    _globals['_KNOWLEDGEOPERATIONMETADATA_STATE']._serialized_start = 3541
    _globals['_KNOWLEDGEOPERATIONMETADATA_STATE']._serialized_end = 3607
    _globals['_DOCUMENTS']._serialized_start = 3632
    _globals['_DOCUMENTS']._serialized_end = 6492