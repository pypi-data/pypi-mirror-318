"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1beta1/operations.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.automl.v1beta1 import io_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_io__pb2
from .....google.cloud.automl.v1beta1 import model_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_model__pb2
from .....google.cloud.automl.v1beta1 import model_evaluation_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_model__evaluation__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/automl/v1beta1/operations.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a$google/cloud/automl/v1beta1/io.proto\x1a\'google/cloud/automl/v1beta1/model.proto\x1a2google/cloud/automl/v1beta1/model_evaluation.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\x8b\x08\n\x11OperationMetadata\x12N\n\x0edelete_details\x18\x08 \x01(\x0b24.google.cloud.automl.v1beta1.DeleteOperationMetadataH\x00\x12Y\n\x14deploy_model_details\x18\x18 \x01(\x0b29.google.cloud.automl.v1beta1.DeployModelOperationMetadataH\x00\x12]\n\x16undeploy_model_details\x18\x19 \x01(\x0b2;.google.cloud.automl.v1beta1.UndeployModelOperationMetadataH\x00\x12Y\n\x14create_model_details\x18\n \x01(\x0b29.google.cloud.automl.v1beta1.CreateModelOperationMetadataH\x00\x12W\n\x13import_data_details\x18\x0f \x01(\x0b28.google.cloud.automl.v1beta1.ImportDataOperationMetadataH\x00\x12[\n\x15batch_predict_details\x18\x10 \x01(\x0b2:.google.cloud.automl.v1beta1.BatchPredictOperationMetadataH\x00\x12W\n\x13export_data_details\x18\x15 \x01(\x0b28.google.cloud.automl.v1beta1.ExportDataOperationMetadataH\x00\x12Y\n\x14export_model_details\x18\x16 \x01(\x0b29.google.cloud.automl.v1beta1.ExportModelOperationMetadataH\x00\x12r\n!export_evaluated_examples_details\x18\x1a \x01(\x0b2E.google.cloud.automl.v1beta1.ExportEvaluatedExamplesOperationMetadataH\x00\x12\x18\n\x10progress_percent\x18\r \x01(\x05\x12,\n\x10partial_failures\x18\x02 \x03(\x0b2\x12.google.rpc.Status\x12/\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\t\n\x07details"\x19\n\x17DeleteOperationMetadata"\x1e\n\x1cDeployModelOperationMetadata" \n\x1eUndeployModelOperationMetadata"\x1e\n\x1cCreateModelOperationMetadata"\x1d\n\x1bImportDataOperationMetadata"\xef\x01\n\x1bExportDataOperationMetadata\x12b\n\x0boutput_info\x18\x01 \x01(\x0b2M.google.cloud.automl.v1beta1.ExportDataOperationMetadata.ExportDataOutputInfo\x1al\n\x14ExportDataOutputInfo\x12\x1e\n\x14gcs_output_directory\x18\x01 \x01(\tH\x00\x12!\n\x17bigquery_output_dataset\x18\x02 \x01(\tH\x00B\x11\n\x0foutput_location"\xc3\x02\n\x1dBatchPredictOperationMetadata\x12J\n\x0cinput_config\x18\x01 \x01(\x0b24.google.cloud.automl.v1beta1.BatchPredictInputConfig\x12f\n\x0boutput_info\x18\x02 \x01(\x0b2Q.google.cloud.automl.v1beta1.BatchPredictOperationMetadata.BatchPredictOutputInfo\x1an\n\x16BatchPredictOutputInfo\x12\x1e\n\x14gcs_output_directory\x18\x01 \x01(\tH\x00\x12!\n\x17bigquery_output_dataset\x18\x02 \x01(\tH\x00B\x11\n\x0foutput_location"\xbb\x01\n\x1cExportModelOperationMetadata\x12d\n\x0boutput_info\x18\x02 \x01(\x0b2O.google.cloud.automl.v1beta1.ExportModelOperationMetadata.ExportModelOutputInfo\x1a5\n\x15ExportModelOutputInfo\x12\x1c\n\x14gcs_output_directory\x18\x01 \x01(\t"\xee\x01\n(ExportEvaluatedExamplesOperationMetadata\x12|\n\x0boutput_info\x18\x02 \x01(\x0b2g.google.cloud.automl.v1beta1.ExportEvaluatedExamplesOperationMetadata.ExportEvaluatedExamplesOutputInfo\x1aD\n!ExportEvaluatedExamplesOutputInfo\x12\x1f\n\x17bigquery_output_dataset\x18\x02 \x01(\tB\x9b\x01\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1beta1.operations_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1'
    _globals['_OPERATIONMETADATA']._serialized_start = 267
    _globals['_OPERATIONMETADATA']._serialized_end = 1302
    _globals['_DELETEOPERATIONMETADATA']._serialized_start = 1304
    _globals['_DELETEOPERATIONMETADATA']._serialized_end = 1329
    _globals['_DEPLOYMODELOPERATIONMETADATA']._serialized_start = 1331
    _globals['_DEPLOYMODELOPERATIONMETADATA']._serialized_end = 1361
    _globals['_UNDEPLOYMODELOPERATIONMETADATA']._serialized_start = 1363
    _globals['_UNDEPLOYMODELOPERATIONMETADATA']._serialized_end = 1395
    _globals['_CREATEMODELOPERATIONMETADATA']._serialized_start = 1397
    _globals['_CREATEMODELOPERATIONMETADATA']._serialized_end = 1427
    _globals['_IMPORTDATAOPERATIONMETADATA']._serialized_start = 1429
    _globals['_IMPORTDATAOPERATIONMETADATA']._serialized_end = 1458
    _globals['_EXPORTDATAOPERATIONMETADATA']._serialized_start = 1461
    _globals['_EXPORTDATAOPERATIONMETADATA']._serialized_end = 1700
    _globals['_EXPORTDATAOPERATIONMETADATA_EXPORTDATAOUTPUTINFO']._serialized_start = 1592
    _globals['_EXPORTDATAOPERATIONMETADATA_EXPORTDATAOUTPUTINFO']._serialized_end = 1700
    _globals['_BATCHPREDICTOPERATIONMETADATA']._serialized_start = 1703
    _globals['_BATCHPREDICTOPERATIONMETADATA']._serialized_end = 2026
    _globals['_BATCHPREDICTOPERATIONMETADATA_BATCHPREDICTOUTPUTINFO']._serialized_start = 1916
    _globals['_BATCHPREDICTOPERATIONMETADATA_BATCHPREDICTOUTPUTINFO']._serialized_end = 2026
    _globals['_EXPORTMODELOPERATIONMETADATA']._serialized_start = 2029
    _globals['_EXPORTMODELOPERATIONMETADATA']._serialized_end = 2216
    _globals['_EXPORTMODELOPERATIONMETADATA_EXPORTMODELOUTPUTINFO']._serialized_start = 2163
    _globals['_EXPORTMODELOPERATIONMETADATA_EXPORTMODELOUTPUTINFO']._serialized_end = 2216
    _globals['_EXPORTEVALUATEDEXAMPLESOPERATIONMETADATA']._serialized_start = 2219
    _globals['_EXPORTEVALUATEDEXAMPLESOPERATIONMETADATA']._serialized_end = 2457
    _globals['_EXPORTEVALUATEDEXAMPLESOPERATIONMETADATA_EXPORTEVALUATEDEXAMPLESOUTPUTINFO']._serialized_start = 2389
    _globals['_EXPORTEVALUATEDEXAMPLESOPERATIONMETADATA_EXPORTEVALUATEDEXAMPLESOUTPUTINFO']._serialized_end = 2457