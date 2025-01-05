"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2beta1/document.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dialogflow.v2beta1 import gcs_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_gcs__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/dialogflow/v2beta1/document.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a)google/cloud/dialogflow/v2beta1/gcs.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xe6\x08\n\x08Document\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x16\n\tmime_type\x18\x03 \x01(\tB\x03\xe0A\x02\x12U\n\x0fknowledge_types\x18\x04 \x03(\x0e27.google.cloud.dialogflow.v2beta1.Document.KnowledgeTypeB\x03\xe0A\x02\x12\x15\n\x0bcontent_uri\x18\x05 \x01(\tH\x00\x12\x15\n\x07content\x18\x06 \x01(\tB\x02\x18\x01H\x00\x12\x15\n\x0braw_content\x18\t \x01(\x0cH\x00\x12\x1f\n\x12enable_auto_reload\x18\x0b \x01(\x08B\x03\xe0A\x01\x12Y\n\x14latest_reload_status\x18\x0c \x01(\x0b26.google.cloud.dialogflow.v2beta1.Document.ReloadStatusB\x03\xe0A\x03\x12N\n\x08metadata\x18\x07 \x03(\x0b27.google.cloud.dialogflow.v2beta1.Document.MetadataEntryB\x03\xe0A\x01\x12C\n\x05state\x18\r \x01(\x0e2/.google.cloud.dialogflow.v2beta1.Document.StateB\x03\xe0A\x03\x1a\\\n\x0cReloadStatus\x12(\n\x04time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12"\n\x06status\x18\x02 \x01(\x0b2\x12.google.rpc.Status\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x96\x01\n\rKnowledgeType\x12\x1e\n\x1aKNOWLEDGE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03FAQ\x10\x01\x12\x11\n\rEXTRACTIVE_QA\x10\x02\x12\x16\n\x12ARTICLE_SUGGESTION\x10\x03\x12\x1c\n\x18AGENT_FACING_SMART_REPLY\x10\x04\x12\x0f\n\x0bSMART_REPLY\x10\x04\x1a\x02\x10\x01"c\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\r\n\tRELOADING\x10\x04\x12\x0c\n\x08DELETING\x10\x05:\xcf\x01\xeaA\xcb\x01\n"dialogflow.googleapis.com/Document\x12Gprojects/{project}/knowledgeBases/{knowledge_base}/documents/{document}\x12\\projects/{project}/locations/{location}/knowledgeBases/{knowledge_base}/documents/{document}B\x08\n\x06source"N\n\x12GetDocumentRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/Document"\x89\x01\n\x14ListDocumentsRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/Document\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"n\n\x15ListDocumentsResponse\x12<\n\tdocuments\x18\x01 \x03(\x0b2).google.cloud.dialogflow.v2beta1.Document\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xb9\x01\n\x15CreateDocumentRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/Document\x12@\n\x08document\x18\x02 \x01(\x0b2).google.cloud.dialogflow.v2beta1.DocumentB\x03\xe0A\x02\x12"\n\x1aimport_gcs_custom_metadata\x18\x03 \x01(\x08"\xa3\x02\n\x16ImportDocumentsRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/Document\x12F\n\ngcs_source\x18\x02 \x01(\x0b2+.google.cloud.dialogflow.v2beta1.GcsSourcesB\x03\xe0A\x01H\x00\x12W\n\x11document_template\x18\x03 \x01(\x0b27.google.cloud.dialogflow.v2beta1.ImportDocumentTemplateB\x03\xe0A\x02\x12"\n\x1aimport_gcs_custom_metadata\x18\x04 \x01(\x08B\x08\n\x06source"\x91\x02\n\x16ImportDocumentTemplate\x12\x16\n\tmime_type\x18\x01 \x01(\tB\x03\xe0A\x02\x12U\n\x0fknowledge_types\x18\x02 \x03(\x0e27.google.cloud.dialogflow.v2beta1.Document.KnowledgeTypeB\x03\xe0A\x02\x12W\n\x08metadata\x18\x03 \x03(\x0b2E.google.cloud.dialogflow.v2beta1.ImportDocumentTemplate.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"?\n\x17ImportDocumentsResponse\x12$\n\x08warnings\x18\x01 \x03(\x0b2\x12.google.rpc.Status"Q\n\x15DeleteDocumentRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/Document"\x8f\x01\n\x15UpdateDocumentRequest\x12@\n\x08document\x18\x01 \x01(\x0b2).google.cloud.dialogflow.v2beta1.DocumentB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"l\n\x17ExportOperationMetadata\x12Q\n\x18exported_gcs_destination\x18\x01 \x01(\x0b2/.google.cloud.dialogflow.v2beta1.GcsDestination"\xc4\x02\n\x1aKnowledgeOperationMetadata\x12U\n\x05state\x18\x01 \x01(\x0e2A.google.cloud.dialogflow.v2beta1.KnowledgeOperationMetadata.StateB\x03\xe0A\x03\x12\x16\n\x0eknowledge_base\x18\x03 \x01(\t\x12]\n\x19export_operation_metadata\x18\x04 \x01(\x0b28.google.cloud.dialogflow.v2beta1.ExportOperationMetadataH\x00"B\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x08\n\x04DONE\x10\x03B\x14\n\x12operation_metadata"\xc1\x01\n\x15ReloadDocumentRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/Document\x12@\n\ngcs_source\x18\x03 \x01(\x0b2*.google.cloud.dialogflow.v2beta1.GcsSourceH\x00\x12"\n\x1aimport_gcs_custom_metadata\x18\x04 \x01(\x08B\x08\n\x06source2\xa5\x15\n\tDocuments\x12\xd2\x02\n\rListDocuments\x125.google.cloud.dialogflow.v2beta1.ListDocumentsRequest\x1a6.google.cloud.dialogflow.v2beta1.ListDocumentsResponse"\xd1\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xc1\x01\x127/v2beta1/{parent=projects/*/knowledgeBases/*}/documentsZE\x12C/v2beta1/{parent=projects/*/locations/*/knowledgeBases/*}/documentsZ?\x12=/v2beta1/{parent=projects/*/agent/knowledgeBases/*}/documents\x12\xbf\x02\n\x0bGetDocument\x123.google.cloud.dialogflow.v2beta1.GetDocumentRequest\x1a).google.cloud.dialogflow.v2beta1.Document"\xcf\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xc1\x01\x127/v2beta1/{name=projects/*/knowledgeBases/*/documents/*}ZE\x12C/v2beta1/{name=projects/*/locations/*/knowledgeBases/*/documents/*}Z?\x12=/v2beta1/{name=projects/*/agent/knowledgeBases/*/documents/*}\x12\x8b\x03\n\x0eCreateDocument\x126.google.cloud.dialogflow.v2beta1.CreateDocumentRequest\x1a\x1d.google.longrunning.Operation"\xa1\x02\xcaA&\n\x08Document\x12\x1aKnowledgeOperationMetadata\xdaA\x0fparent,document\x82\xd3\xe4\x93\x02\xdf\x01"7/v2beta1/{parent=projects/*/knowledgeBases/*}/documents:\x08documentZO"C/v2beta1/{parent=projects/*/locations/*/knowledgeBases/*}/documents:\x08documentZI"=/v2beta1/{parent=projects/*/agent/knowledgeBases/*}/documents:\x08document\x12\xbf\x02\n\x0fImportDocuments\x127.google.cloud.dialogflow.v2beta1.ImportDocumentsRequest\x1a\x1d.google.longrunning.Operation"\xd3\x01\xcaA5\n\x17ImportDocumentsResponse\x12\x1aKnowledgeOperationMetadata\x82\xd3\xe4\x93\x02\x94\x01">/v2beta1/{parent=projects/*/knowledgeBases/*}/documents:import:\x01*ZO"J/v2beta1/{parent=projects/*/locations/*/knowledgeBases/*}/documents:import:\x01*\x12\xef\x02\n\x0eDeleteDocument\x126.google.cloud.dialogflow.v2beta1.DeleteDocumentRequest\x1a\x1d.google.longrunning.Operation"\x85\x02\xcaA3\n\x15google.protobuf.Empty\x12\x1aKnowledgeOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\xc1\x01*7/v2beta1/{name=projects/*/knowledgeBases/*/documents/*}ZE*C/v2beta1/{name=projects/*/locations/*/knowledgeBases/*/documents/*}Z?*=/v2beta1/{name=projects/*/agent/knowledgeBases/*/documents/*}\x12\xb6\x03\n\x0eUpdateDocument\x126.google.cloud.dialogflow.v2beta1.UpdateDocumentRequest\x1a\x1d.google.longrunning.Operation"\xcc\x02\xcaA&\n\x08Document\x12\x1aKnowledgeOperationMetadata\xdaA\x14document,update_mask\xdaA\x08document\x82\xd3\xe4\x93\x02\xfa\x012@/v2beta1/{document.name=projects/*/knowledgeBases/*/documents/*}:\x08documentZX2L/v2beta1/{document.name=projects/*/locations/*/knowledgeBases/*/documents/*}:\x08documentZR2F/v2beta1/{document.name=projects/*/agent/knowledgeBases/*/documents/*}:\x08document\x12\x8b\x03\n\x0eReloadDocument\x126.google.cloud.dialogflow.v2beta1.ReloadDocumentRequest\x1a\x1d.google.longrunning.Operation"\xa1\x02\xcaA&\n\x08Document\x12\x1aKnowledgeOperationMetadata\xdaA\x0fname,gcs_source\x82\xd3\xe4\x93\x02\xdf\x01">/v2beta1/{name=projects/*/knowledgeBases/*/documents/*}:reload:\x01*ZO"J/v2beta1/{name=projects/*/locations/*/knowledgeBases/*/documents/*}:reload:\x01*ZI"D/v2beta1/{name=projects/*/agent/knowledgeBases/*/documents/*}:reload:\x01*\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xa5\x01\n#com.google.cloud.dialogflow.v2beta1B\rDocumentProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2beta1.document_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.dialogflow.v2beta1B\rDocumentProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1'
    _globals['_DOCUMENT_METADATAENTRY']._loaded_options = None
    _globals['_DOCUMENT_METADATAENTRY']._serialized_options = b'8\x01'
    _globals['_DOCUMENT_KNOWLEDGETYPE']._loaded_options = None
    _globals['_DOCUMENT_KNOWLEDGETYPE']._serialized_options = b'\x10\x01'
    _globals['_DOCUMENT'].fields_by_name['name']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['name']._serialized_options = b'\xe0A\x01'
    _globals['_DOCUMENT'].fields_by_name['display_name']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_DOCUMENT'].fields_by_name['mime_type']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['mime_type']._serialized_options = b'\xe0A\x02'
    _globals['_DOCUMENT'].fields_by_name['knowledge_types']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['knowledge_types']._serialized_options = b'\xe0A\x02'
    _globals['_DOCUMENT'].fields_by_name['content']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['content']._serialized_options = b'\x18\x01'
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
    _globals['_KNOWLEDGEOPERATIONMETADATA'].fields_by_name['state']._loaded_options = None
    _globals['_KNOWLEDGEOPERATIONMETADATA'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_RELOADDOCUMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RELOADDOCUMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/Document'
    _globals['_DOCUMENTS']._loaded_options = None
    _globals['_DOCUMENTS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_DOCUMENTS'].methods_by_name['ListDocuments']._loaded_options = None
    _globals['_DOCUMENTS'].methods_by_name['ListDocuments']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xc1\x01\x127/v2beta1/{parent=projects/*/knowledgeBases/*}/documentsZE\x12C/v2beta1/{parent=projects/*/locations/*/knowledgeBases/*}/documentsZ?\x12=/v2beta1/{parent=projects/*/agent/knowledgeBases/*}/documents'
    _globals['_DOCUMENTS'].methods_by_name['GetDocument']._loaded_options = None
    _globals['_DOCUMENTS'].methods_by_name['GetDocument']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xc1\x01\x127/v2beta1/{name=projects/*/knowledgeBases/*/documents/*}ZE\x12C/v2beta1/{name=projects/*/locations/*/knowledgeBases/*/documents/*}Z?\x12=/v2beta1/{name=projects/*/agent/knowledgeBases/*/documents/*}'
    _globals['_DOCUMENTS'].methods_by_name['CreateDocument']._loaded_options = None
    _globals['_DOCUMENTS'].methods_by_name['CreateDocument']._serialized_options = b'\xcaA&\n\x08Document\x12\x1aKnowledgeOperationMetadata\xdaA\x0fparent,document\x82\xd3\xe4\x93\x02\xdf\x01"7/v2beta1/{parent=projects/*/knowledgeBases/*}/documents:\x08documentZO"C/v2beta1/{parent=projects/*/locations/*/knowledgeBases/*}/documents:\x08documentZI"=/v2beta1/{parent=projects/*/agent/knowledgeBases/*}/documents:\x08document'
    _globals['_DOCUMENTS'].methods_by_name['ImportDocuments']._loaded_options = None
    _globals['_DOCUMENTS'].methods_by_name['ImportDocuments']._serialized_options = b'\xcaA5\n\x17ImportDocumentsResponse\x12\x1aKnowledgeOperationMetadata\x82\xd3\xe4\x93\x02\x94\x01">/v2beta1/{parent=projects/*/knowledgeBases/*}/documents:import:\x01*ZO"J/v2beta1/{parent=projects/*/locations/*/knowledgeBases/*}/documents:import:\x01*'
    _globals['_DOCUMENTS'].methods_by_name['DeleteDocument']._loaded_options = None
    _globals['_DOCUMENTS'].methods_by_name['DeleteDocument']._serialized_options = b'\xcaA3\n\x15google.protobuf.Empty\x12\x1aKnowledgeOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\xc1\x01*7/v2beta1/{name=projects/*/knowledgeBases/*/documents/*}ZE*C/v2beta1/{name=projects/*/locations/*/knowledgeBases/*/documents/*}Z?*=/v2beta1/{name=projects/*/agent/knowledgeBases/*/documents/*}'
    _globals['_DOCUMENTS'].methods_by_name['UpdateDocument']._loaded_options = None
    _globals['_DOCUMENTS'].methods_by_name['UpdateDocument']._serialized_options = b'\xcaA&\n\x08Document\x12\x1aKnowledgeOperationMetadata\xdaA\x14document,update_mask\xdaA\x08document\x82\xd3\xe4\x93\x02\xfa\x012@/v2beta1/{document.name=projects/*/knowledgeBases/*/documents/*}:\x08documentZX2L/v2beta1/{document.name=projects/*/locations/*/knowledgeBases/*/documents/*}:\x08documentZR2F/v2beta1/{document.name=projects/*/agent/knowledgeBases/*/documents/*}:\x08document'
    _globals['_DOCUMENTS'].methods_by_name['ReloadDocument']._loaded_options = None
    _globals['_DOCUMENTS'].methods_by_name['ReloadDocument']._serialized_options = b'\xcaA&\n\x08Document\x12\x1aKnowledgeOperationMetadata\xdaA\x0fname,gcs_source\x82\xd3\xe4\x93\x02\xdf\x01">/v2beta1/{name=projects/*/knowledgeBases/*/documents/*}:reload:\x01*ZO"J/v2beta1/{name=projects/*/locations/*/knowledgeBases/*/documents/*}:reload:\x01*ZI"D/v2beta1/{name=projects/*/agent/knowledgeBases/*/documents/*}:reload:\x01*'
    _globals['_DOCUMENT']._serialized_start = 400
    _globals['_DOCUMENT']._serialized_end = 1526
    _globals['_DOCUMENT_RELOADSTATUS']._serialized_start = 911
    _globals['_DOCUMENT_RELOADSTATUS']._serialized_end = 1003
    _globals['_DOCUMENT_METADATAENTRY']._serialized_start = 1005
    _globals['_DOCUMENT_METADATAENTRY']._serialized_end = 1052
    _globals['_DOCUMENT_KNOWLEDGETYPE']._serialized_start = 1055
    _globals['_DOCUMENT_KNOWLEDGETYPE']._serialized_end = 1205
    _globals['_DOCUMENT_STATE']._serialized_start = 1207
    _globals['_DOCUMENT_STATE']._serialized_end = 1306
    _globals['_GETDOCUMENTREQUEST']._serialized_start = 1528
    _globals['_GETDOCUMENTREQUEST']._serialized_end = 1606
    _globals['_LISTDOCUMENTSREQUEST']._serialized_start = 1609
    _globals['_LISTDOCUMENTSREQUEST']._serialized_end = 1746
    _globals['_LISTDOCUMENTSRESPONSE']._serialized_start = 1748
    _globals['_LISTDOCUMENTSRESPONSE']._serialized_end = 1858
    _globals['_CREATEDOCUMENTREQUEST']._serialized_start = 1861
    _globals['_CREATEDOCUMENTREQUEST']._serialized_end = 2046
    _globals['_IMPORTDOCUMENTSREQUEST']._serialized_start = 2049
    _globals['_IMPORTDOCUMENTSREQUEST']._serialized_end = 2340
    _globals['_IMPORTDOCUMENTTEMPLATE']._serialized_start = 2343
    _globals['_IMPORTDOCUMENTTEMPLATE']._serialized_end = 2616
    _globals['_IMPORTDOCUMENTTEMPLATE_METADATAENTRY']._serialized_start = 1005
    _globals['_IMPORTDOCUMENTTEMPLATE_METADATAENTRY']._serialized_end = 1052
    _globals['_IMPORTDOCUMENTSRESPONSE']._serialized_start = 2618
    _globals['_IMPORTDOCUMENTSRESPONSE']._serialized_end = 2681
    _globals['_DELETEDOCUMENTREQUEST']._serialized_start = 2683
    _globals['_DELETEDOCUMENTREQUEST']._serialized_end = 2764
    _globals['_UPDATEDOCUMENTREQUEST']._serialized_start = 2767
    _globals['_UPDATEDOCUMENTREQUEST']._serialized_end = 2910
    _globals['_EXPORTOPERATIONMETADATA']._serialized_start = 2912
    _globals['_EXPORTOPERATIONMETADATA']._serialized_end = 3020
    _globals['_KNOWLEDGEOPERATIONMETADATA']._serialized_start = 3023
    _globals['_KNOWLEDGEOPERATIONMETADATA']._serialized_end = 3347
    _globals['_KNOWLEDGEOPERATIONMETADATA_STATE']._serialized_start = 3259
    _globals['_KNOWLEDGEOPERATIONMETADATA_STATE']._serialized_end = 3325
    _globals['_RELOADDOCUMENTREQUEST']._serialized_start = 3350
    _globals['_RELOADDOCUMENTREQUEST']._serialized_end = 3543
    _globals['_DOCUMENTS']._serialized_start = 3546
    _globals['_DOCUMENTS']._serialized_end = 6271