"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/documentai/v1beta3/document_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.documentai.v1beta3 import dataset_pb2 as google_dot_cloud_dot_documentai_dot_v1beta3_dot_dataset__pb2
from .....google.cloud.documentai.v1beta3 import document_pb2 as google_dot_cloud_dot_documentai_dot_v1beta3_dot_document__pb2
from .....google.cloud.documentai.v1beta3 import document_io_pb2 as google_dot_cloud_dot_documentai_dot_v1beta3_dot_document__io__pb2
from .....google.cloud.documentai.v1beta3 import operation_metadata_pb2 as google_dot_cloud_dot_documentai_dot_v1beta3_dot_operation__metadata__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/documentai/v1beta3/document_service.proto\x12\x1fgoogle.cloud.documentai.v1beta3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/documentai/v1beta3/dataset.proto\x1a.google/cloud/documentai/v1beta3/document.proto\x1a1google/cloud/documentai/v1beta3/document_io.proto\x1a8google/cloud/documentai/v1beta3/operation_metadata.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\x87\x01\n\x14UpdateDatasetRequest\x12>\n\x07dataset\x18\x01 \x01(\x0b2(.google.cloud.documentai.v1beta3.DatasetB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"s\n\x1eUpdateDatasetOperationMetadata\x12Q\n\x0fcommon_metadata\x18\x01 \x01(\x0b28.google.cloud.documentai.v1beta3.CommonOperationMetadata"\xdf\x04\n\x16ImportDocumentsRequest\x12:\n\x07dataset\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!documentai.googleapis.com/Dataset\x12\x7f\n\x1ebatch_documents_import_configs\x18\x04 \x03(\x0b2R.google.cloud.documentai.v1beta3.ImportDocumentsRequest.BatchDocumentsImportConfigB\x03\xe0A\x02\x1a\x87\x03\n\x1aBatchDocumentsImportConfig\x12J\n\rdataset_split\x18\x02 \x01(\x0e21.google.cloud.documentai.v1beta3.DatasetSplitTypeH\x00\x12\x7f\n\x11auto_split_config\x18\x03 \x01(\x0b2b.google.cloud.documentai.v1beta3.ImportDocumentsRequest.BatchDocumentsImportConfig.AutoSplitConfigH\x00\x12V\n\x12batch_input_config\x18\x01 \x01(\x0b2:.google.cloud.documentai.v1beta3.BatchDocumentsInputConfig\x1a/\n\x0fAutoSplitConfig\x12\x1c\n\x14training_split_ratio\x18\x01 \x01(\x02B\x13\n\x11split_type_config"\x19\n\x17ImportDocumentsResponse"\x80\x05\n\x17ImportDocumentsMetadata\x12Q\n\x0fcommon_metadata\x18\x01 \x01(\x0b28.google.cloud.documentai.v1beta3.CommonOperationMetadata\x12s\n\x1aindividual_import_statuses\x18\x02 \x03(\x0b2O.google.cloud.documentai.v1beta3.ImportDocumentsMetadata.IndividualImportStatus\x12\x7f\n import_config_validation_results\x18\x04 \x03(\x0b2U.google.cloud.documentai.v1beta3.ImportDocumentsMetadata.ImportConfigValidationResult\x12\x1c\n\x14total_document_count\x18\x03 \x01(\x05\x1a\x9f\x01\n\x16IndividualImportStatus\x12\x18\n\x10input_gcs_source\x18\x01 \x01(\t\x12"\n\x06status\x18\x02 \x01(\x0b2\x12.google.rpc.Status\x12G\n\x12output_document_id\x18\x04 \x01(\x0b2+.google.cloud.documentai.v1beta3.DocumentId\x1a\\\n\x1cImportConfigValidationResult\x12\x18\n\x10input_gcs_source\x18\x01 \x01(\t\x12"\n\x06status\x18\x02 \x01(\x0b2\x12.google.rpc.Status"\x8e\x02\n\x12GetDocumentRequest\x12:\n\x07dataset\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!documentai.googleapis.com/Dataset\x12E\n\x0bdocument_id\x18\x02 \x01(\x0b2+.google.cloud.documentai.v1beta3.DocumentIdB\x03\xe0A\x02\x12-\n\tread_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12F\n\npage_range\x18\x04 \x01(\x0b22.google.cloud.documentai.v1beta3.DocumentPageRange"R\n\x13GetDocumentResponse\x12;\n\x08document\x18\x01 \x01(\x0b2).google.cloud.documentai.v1beta3.Document"\xc1\x01\n\x14ListDocumentsRequest\x12:\n\x07dataset\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!documentai.googleapis.com/Dataset\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x1e\n\x11return_total_size\x18\x06 \x01(\x08B\x03\xe0A\x01\x12\x11\n\x04skip\x18\x08 \x01(\x05B\x03\xe0A\x01"\x92\x01\n\x15ListDocumentsResponse\x12L\n\x11document_metadata\x18\x01 \x03(\x0b21.google.cloud.documentai.v1beta3.DocumentMetadata\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"\x8b\x01\n\x1bBatchDeleteDocumentsRequest\x12\x14\n\x07dataset\x18\x01 \x01(\tB\x03\xe0A\x02\x12V\n\x11dataset_documents\x18\x03 \x01(\x0b26.google.cloud.documentai.v1beta3.BatchDatasetDocumentsB\x03\xe0A\x02"\x1e\n\x1cBatchDeleteDocumentsResponse"\xb9\x03\n\x1cBatchDeleteDocumentsMetadata\x12Q\n\x0fcommon_metadata\x18\x01 \x01(\x0b28.google.cloud.documentai.v1beta3.CommonOperationMetadata\x12\x83\x01\n individual_batch_delete_statuses\x18\x02 \x03(\x0b2Y.google.cloud.documentai.v1beta3.BatchDeleteDocumentsMetadata.IndividualBatchDeleteStatus\x12\x1c\n\x14total_document_count\x18\x03 \x01(\x05\x12\x1c\n\x14error_document_count\x18\x04 \x01(\x05\x1a\x83\x01\n\x1bIndividualBatchDeleteStatus\x12@\n\x0bdocument_id\x18\x01 \x01(\x0b2+.google.cloud.documentai.v1beta3.DocumentId\x12"\n\x06status\x18\x02 \x01(\x0b2\x12.google.rpc.Status"u\n\x17GetDatasetSchemaRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'documentai.googleapis.com/DatasetSchema\x12\x1b\n\x13visible_fields_only\x18\x02 \x01(\x08"\x9a\x01\n\x1aUpdateDatasetSchemaRequest\x12K\n\x0edataset_schema\x18\x01 \x01(\x0b2..google.cloud.documentai.v1beta3.DatasetSchemaB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"/\n\x11DocumentPageRange\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03end\x18\x02 \x01(\x05"\x97\x02\n\x10DocumentMetadata\x12@\n\x0bdocument_id\x18\x01 \x01(\x0b2+.google.cloud.documentai.v1beta3.DocumentId\x12\x12\n\npage_count\x18\x02 \x01(\x05\x12G\n\x0cdataset_type\x18\x03 \x01(\x0e21.google.cloud.documentai.v1beta3.DatasetSplitType\x12N\n\x0elabeling_state\x18\x05 \x01(\x0e26.google.cloud.documentai.v1beta3.DocumentLabelingState\x12\x14\n\x0cdisplay_name\x18\x06 \x01(\t*\x85\x01\n\x10DatasetSplitType\x12"\n\x1eDATASET_SPLIT_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13DATASET_SPLIT_TRAIN\x10\x01\x12\x16\n\x12DATASET_SPLIT_TEST\x10\x02\x12\x1c\n\x18DATASET_SPLIT_UNASSIGNED\x10\x03*\x89\x01\n\x15DocumentLabelingState\x12\'\n#DOCUMENT_LABELING_STATE_UNSPECIFIED\x10\x00\x12\x14\n\x10DOCUMENT_LABELED\x10\x01\x12\x16\n\x12DOCUMENT_UNLABELED\x10\x02\x12\x19\n\x15DOCUMENT_AUTO_LABELED\x10\x032\xb3\x0e\n\x0fDocumentService\x12\xfe\x01\n\rUpdateDataset\x125.google.cloud.documentai.v1beta3.UpdateDatasetRequest\x1a\x1d.google.longrunning.Operation"\x96\x01\xcaA)\n\x07Dataset\x12\x1eUpdateDatasetOperationMetadata\xdaA\x13dataset,update_mask\x82\xd3\xe4\x93\x02N2C/v1beta3/{dataset.name=projects/*/locations/*/processors/*/dataset}:\x07dataset\x12\x84\x02\n\x0fImportDocuments\x127.google.cloud.documentai.v1beta3.ImportDocumentsRequest\x1a\x1d.google.longrunning.Operation"\x98\x01\xcaA2\n\x17ImportDocumentsResponse\x12\x17ImportDocumentsMetadata\xdaA\x07dataset\x82\xd3\xe4\x93\x02S"N/v1beta3/{dataset=projects/*/locations/*/processors/*/dataset}:importDocuments:\x01*\x12\xd6\x01\n\x0bGetDocument\x123.google.cloud.documentai.v1beta3.GetDocumentRequest\x1a4.google.cloud.documentai.v1beta3.GetDocumentResponse"\\\xdaA\x07dataset\x82\xd3\xe4\x93\x02L\x12J/v1beta3/{dataset=projects/*/locations/*/processors/*/dataset}:getDocument\x12\xe1\x01\n\rListDocuments\x125.google.cloud.documentai.v1beta3.ListDocumentsRequest\x1a6.google.cloud.documentai.v1beta3.ListDocumentsResponse"a\xdaA\x07dataset\x82\xd3\xe4\x93\x02Q"L/v1beta3/{dataset=projects/*/locations/*/processors/*/dataset}:listDocuments:\x01*\x12\x9d\x02\n\x14BatchDeleteDocuments\x12<.google.cloud.documentai.v1beta3.BatchDeleteDocumentsRequest\x1a\x1d.google.longrunning.Operation"\xa7\x01\xcaA<\n\x1cBatchDeleteDocumentsResponse\x12\x1cBatchDeleteDocumentsMetadata\xdaA\x07dataset\x82\xd3\xe4\x93\x02X"S/v1beta3/{dataset=projects/*/locations/*/processors/*/dataset}:batchDeleteDocuments:\x01*\x12\xd6\x01\n\x10GetDatasetSchema\x128.google.cloud.documentai.v1beta3.GetDatasetSchemaRequest\x1a..google.cloud.documentai.v1beta3.DatasetSchema"X\xdaA\x04name\x82\xd3\xe4\x93\x02K\x12I/v1beta3/{name=projects/*/locations/*/processors/*/dataset/datasetSchema}\x12\x92\x02\n\x13UpdateDatasetSchema\x12;.google.cloud.documentai.v1beta3.UpdateDatasetSchemaRequest\x1a..google.cloud.documentai.v1beta3.DatasetSchema"\x8d\x01\xdaA\x1adataset_schema,update_mask\x82\xd3\xe4\x93\x02j2X/v1beta3/{dataset_schema.name=projects/*/locations/*/processors/*/dataset/datasetSchema}:\x0edataset_schema\x1aM\xcaA\x19documentai.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf0\x01\n#com.google.cloud.documentai.v1beta3B\x19DocumentAiDocumentServiceP\x01ZCcloud.google.com/go/documentai/apiv1beta3/documentaipb;documentaipb\xaa\x02\x1fGoogle.Cloud.DocumentAI.V1Beta3\xca\x02\x1fGoogle\\Cloud\\DocumentAI\\V1beta3\xea\x02"Google::Cloud::DocumentAI::V1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.documentai.v1beta3.document_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.documentai.v1beta3B\x19DocumentAiDocumentServiceP\x01ZCcloud.google.com/go/documentai/apiv1beta3/documentaipb;documentaipb\xaa\x02\x1fGoogle.Cloud.DocumentAI.V1Beta3\xca\x02\x1fGoogle\\Cloud\\DocumentAI\\V1beta3\xea\x02"Google::Cloud::DocumentAI::V1beta3'
    _globals['_UPDATEDATASETREQUEST'].fields_by_name['dataset']._loaded_options = None
    _globals['_UPDATEDATASETREQUEST'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTDOCUMENTSREQUEST'].fields_by_name['dataset']._loaded_options = None
    _globals['_IMPORTDOCUMENTSREQUEST'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02\xfaA#\n!documentai.googleapis.com/Dataset'
    _globals['_IMPORTDOCUMENTSREQUEST'].fields_by_name['batch_documents_import_configs']._loaded_options = None
    _globals['_IMPORTDOCUMENTSREQUEST'].fields_by_name['batch_documents_import_configs']._serialized_options = b'\xe0A\x02'
    _globals['_GETDOCUMENTREQUEST'].fields_by_name['dataset']._loaded_options = None
    _globals['_GETDOCUMENTREQUEST'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02\xfaA#\n!documentai.googleapis.com/Dataset'
    _globals['_GETDOCUMENTREQUEST'].fields_by_name['document_id']._loaded_options = None
    _globals['_GETDOCUMENTREQUEST'].fields_by_name['document_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['dataset']._loaded_options = None
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02\xfaA#\n!documentai.googleapis.com/Dataset'
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['return_total_size']._loaded_options = None
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['return_total_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['skip']._loaded_options = None
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['skip']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHDELETEDOCUMENTSREQUEST'].fields_by_name['dataset']._loaded_options = None
    _globals['_BATCHDELETEDOCUMENTSREQUEST'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHDELETEDOCUMENTSREQUEST'].fields_by_name['dataset_documents']._loaded_options = None
    _globals['_BATCHDELETEDOCUMENTSREQUEST'].fields_by_name['dataset_documents']._serialized_options = b'\xe0A\x02'
    _globals['_GETDATASETSCHEMAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATASETSCHEMAREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'documentai.googleapis.com/DatasetSchema"
    _globals['_UPDATEDATASETSCHEMAREQUEST'].fields_by_name['dataset_schema']._loaded_options = None
    _globals['_UPDATEDATASETSCHEMAREQUEST'].fields_by_name['dataset_schema']._serialized_options = b'\xe0A\x02'
    _globals['_DOCUMENTSERVICE']._loaded_options = None
    _globals['_DOCUMENTSERVICE']._serialized_options = b'\xcaA\x19documentai.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DOCUMENTSERVICE'].methods_by_name['UpdateDataset']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['UpdateDataset']._serialized_options = b'\xcaA)\n\x07Dataset\x12\x1eUpdateDatasetOperationMetadata\xdaA\x13dataset,update_mask\x82\xd3\xe4\x93\x02N2C/v1beta3/{dataset.name=projects/*/locations/*/processors/*/dataset}:\x07dataset'
    _globals['_DOCUMENTSERVICE'].methods_by_name['ImportDocuments']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['ImportDocuments']._serialized_options = b'\xcaA2\n\x17ImportDocumentsResponse\x12\x17ImportDocumentsMetadata\xdaA\x07dataset\x82\xd3\xe4\x93\x02S"N/v1beta3/{dataset=projects/*/locations/*/processors/*/dataset}:importDocuments:\x01*'
    _globals['_DOCUMENTSERVICE'].methods_by_name['GetDocument']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['GetDocument']._serialized_options = b'\xdaA\x07dataset\x82\xd3\xe4\x93\x02L\x12J/v1beta3/{dataset=projects/*/locations/*/processors/*/dataset}:getDocument'
    _globals['_DOCUMENTSERVICE'].methods_by_name['ListDocuments']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['ListDocuments']._serialized_options = b'\xdaA\x07dataset\x82\xd3\xe4\x93\x02Q"L/v1beta3/{dataset=projects/*/locations/*/processors/*/dataset}:listDocuments:\x01*'
    _globals['_DOCUMENTSERVICE'].methods_by_name['BatchDeleteDocuments']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['BatchDeleteDocuments']._serialized_options = b'\xcaA<\n\x1cBatchDeleteDocumentsResponse\x12\x1cBatchDeleteDocumentsMetadata\xdaA\x07dataset\x82\xd3\xe4\x93\x02X"S/v1beta3/{dataset=projects/*/locations/*/processors/*/dataset}:batchDeleteDocuments:\x01*'
    _globals['_DOCUMENTSERVICE'].methods_by_name['GetDatasetSchema']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['GetDatasetSchema']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02K\x12I/v1beta3/{name=projects/*/locations/*/processors/*/dataset/datasetSchema}'
    _globals['_DOCUMENTSERVICE'].methods_by_name['UpdateDatasetSchema']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['UpdateDatasetSchema']._serialized_options = b'\xdaA\x1adataset_schema,update_mask\x82\xd3\xe4\x93\x02j2X/v1beta3/{dataset_schema.name=projects/*/locations/*/processors/*/dataset/datasetSchema}:\x0edataset_schema'
    _globals['_DATASETSPLITTYPE']._serialized_start = 3969
    _globals['_DATASETSPLITTYPE']._serialized_end = 4102
    _globals['_DOCUMENTLABELINGSTATE']._serialized_start = 4105
    _globals['_DOCUMENTLABELINGSTATE']._serialized_end = 4242
    _globals['_UPDATEDATASETREQUEST']._serialized_start = 507
    _globals['_UPDATEDATASETREQUEST']._serialized_end = 642
    _globals['_UPDATEDATASETOPERATIONMETADATA']._serialized_start = 644
    _globals['_UPDATEDATASETOPERATIONMETADATA']._serialized_end = 759
    _globals['_IMPORTDOCUMENTSREQUEST']._serialized_start = 762
    _globals['_IMPORTDOCUMENTSREQUEST']._serialized_end = 1369
    _globals['_IMPORTDOCUMENTSREQUEST_BATCHDOCUMENTSIMPORTCONFIG']._serialized_start = 978
    _globals['_IMPORTDOCUMENTSREQUEST_BATCHDOCUMENTSIMPORTCONFIG']._serialized_end = 1369
    _globals['_IMPORTDOCUMENTSREQUEST_BATCHDOCUMENTSIMPORTCONFIG_AUTOSPLITCONFIG']._serialized_start = 1301
    _globals['_IMPORTDOCUMENTSREQUEST_BATCHDOCUMENTSIMPORTCONFIG_AUTOSPLITCONFIG']._serialized_end = 1348
    _globals['_IMPORTDOCUMENTSRESPONSE']._serialized_start = 1371
    _globals['_IMPORTDOCUMENTSRESPONSE']._serialized_end = 1396
    _globals['_IMPORTDOCUMENTSMETADATA']._serialized_start = 1399
    _globals['_IMPORTDOCUMENTSMETADATA']._serialized_end = 2039
    _globals['_IMPORTDOCUMENTSMETADATA_INDIVIDUALIMPORTSTATUS']._serialized_start = 1786
    _globals['_IMPORTDOCUMENTSMETADATA_INDIVIDUALIMPORTSTATUS']._serialized_end = 1945
    _globals['_IMPORTDOCUMENTSMETADATA_IMPORTCONFIGVALIDATIONRESULT']._serialized_start = 1947
    _globals['_IMPORTDOCUMENTSMETADATA_IMPORTCONFIGVALIDATIONRESULT']._serialized_end = 2039
    _globals['_GETDOCUMENTREQUEST']._serialized_start = 2042
    _globals['_GETDOCUMENTREQUEST']._serialized_end = 2312
    _globals['_GETDOCUMENTRESPONSE']._serialized_start = 2314
    _globals['_GETDOCUMENTRESPONSE']._serialized_end = 2396
    _globals['_LISTDOCUMENTSREQUEST']._serialized_start = 2399
    _globals['_LISTDOCUMENTSREQUEST']._serialized_end = 2592
    _globals['_LISTDOCUMENTSRESPONSE']._serialized_start = 2595
    _globals['_LISTDOCUMENTSRESPONSE']._serialized_end = 2741
    _globals['_BATCHDELETEDOCUMENTSREQUEST']._serialized_start = 2744
    _globals['_BATCHDELETEDOCUMENTSREQUEST']._serialized_end = 2883
    _globals['_BATCHDELETEDOCUMENTSRESPONSE']._serialized_start = 2885
    _globals['_BATCHDELETEDOCUMENTSRESPONSE']._serialized_end = 2915
    _globals['_BATCHDELETEDOCUMENTSMETADATA']._serialized_start = 2918
    _globals['_BATCHDELETEDOCUMENTSMETADATA']._serialized_end = 3359
    _globals['_BATCHDELETEDOCUMENTSMETADATA_INDIVIDUALBATCHDELETESTATUS']._serialized_start = 3228
    _globals['_BATCHDELETEDOCUMENTSMETADATA_INDIVIDUALBATCHDELETESTATUS']._serialized_end = 3359
    _globals['_GETDATASETSCHEMAREQUEST']._serialized_start = 3361
    _globals['_GETDATASETSCHEMAREQUEST']._serialized_end = 3478
    _globals['_UPDATEDATASETSCHEMAREQUEST']._serialized_start = 3481
    _globals['_UPDATEDATASETSCHEMAREQUEST']._serialized_end = 3635
    _globals['_DOCUMENTPAGERANGE']._serialized_start = 3637
    _globals['_DOCUMENTPAGERANGE']._serialized_end = 3684
    _globals['_DOCUMENTMETADATA']._serialized_start = 3687
    _globals['_DOCUMENTMETADATA']._serialized_end = 3966
    _globals['_DOCUMENTSERVICE']._serialized_start = 4245
    _globals['_DOCUMENTSERVICE']._serialized_end = 6088