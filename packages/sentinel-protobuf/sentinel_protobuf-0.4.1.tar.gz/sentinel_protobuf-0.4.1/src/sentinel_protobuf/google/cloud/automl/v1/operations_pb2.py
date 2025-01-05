"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1/operations.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.automl.v1 import io_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_io__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/automl/v1/operations.proto\x12\x16google.cloud.automl.v1\x1a\x1fgoogle/cloud/automl/v1/io.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xc9\x07\n\x11OperationMetadata\x12I\n\x0edelete_details\x18\x08 \x01(\x0b2/.google.cloud.automl.v1.DeleteOperationMetadataH\x00\x12T\n\x14deploy_model_details\x18\x18 \x01(\x0b24.google.cloud.automl.v1.DeployModelOperationMetadataH\x00\x12X\n\x16undeploy_model_details\x18\x19 \x01(\x0b26.google.cloud.automl.v1.UndeployModelOperationMetadataH\x00\x12T\n\x14create_model_details\x18\n \x01(\x0b24.google.cloud.automl.v1.CreateModelOperationMetadataH\x00\x12X\n\x16create_dataset_details\x18\x1e \x01(\x0b26.google.cloud.automl.v1.CreateDatasetOperationMetadataH\x00\x12R\n\x13import_data_details\x18\x0f \x01(\x0b23.google.cloud.automl.v1.ImportDataOperationMetadataH\x00\x12V\n\x15batch_predict_details\x18\x10 \x01(\x0b25.google.cloud.automl.v1.BatchPredictOperationMetadataH\x00\x12R\n\x13export_data_details\x18\x15 \x01(\x0b23.google.cloud.automl.v1.ExportDataOperationMetadataH\x00\x12T\n\x14export_model_details\x18\x16 \x01(\x0b24.google.cloud.automl.v1.ExportModelOperationMetadataH\x00\x12\x18\n\x10progress_percent\x18\r \x01(\x05\x12,\n\x10partial_failures\x18\x02 \x03(\x0b2\x12.google.rpc.Status\x12/\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\t\n\x07details"\x19\n\x17DeleteOperationMetadata"\x1e\n\x1cDeployModelOperationMetadata" \n\x1eUndeployModelOperationMetadata" \n\x1eCreateDatasetOperationMetadata"\x1e\n\x1cCreateModelOperationMetadata"\x1d\n\x1bImportDataOperationMetadata"\xc7\x01\n\x1bExportDataOperationMetadata\x12]\n\x0boutput_info\x18\x01 \x01(\x0b2H.google.cloud.automl.v1.ExportDataOperationMetadata.ExportDataOutputInfo\x1aI\n\x14ExportDataOutputInfo\x12\x1e\n\x14gcs_output_directory\x18\x01 \x01(\tH\x00B\x11\n\x0foutput_location"\x96\x02\n\x1dBatchPredictOperationMetadata\x12E\n\x0cinput_config\x18\x01 \x01(\x0b2/.google.cloud.automl.v1.BatchPredictInputConfig\x12a\n\x0boutput_info\x18\x02 \x01(\x0b2L.google.cloud.automl.v1.BatchPredictOperationMetadata.BatchPredictOutputInfo\x1aK\n\x16BatchPredictOutputInfo\x12\x1e\n\x14gcs_output_directory\x18\x01 \x01(\tH\x00B\x11\n\x0foutput_location"\xb6\x01\n\x1cExportModelOperationMetadata\x12_\n\x0boutput_info\x18\x02 \x01(\x0b2J.google.cloud.automl.v1.ExportModelOperationMetadata.ExportModelOutputInfo\x1a5\n\x15ExportModelOutputInfo\x12\x1c\n\x14gcs_output_directory\x18\x01 \x01(\tB\xa0\x01\n\x1acom.google.cloud.automl.v1P\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1.operations_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.automl.v1P\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1'
    _globals['_OPERATIONMETADATA']._serialized_start = 159
    _globals['_OPERATIONMETADATA']._serialized_end = 1128
    _globals['_DELETEOPERATIONMETADATA']._serialized_start = 1130
    _globals['_DELETEOPERATIONMETADATA']._serialized_end = 1155
    _globals['_DEPLOYMODELOPERATIONMETADATA']._serialized_start = 1157
    _globals['_DEPLOYMODELOPERATIONMETADATA']._serialized_end = 1187
    _globals['_UNDEPLOYMODELOPERATIONMETADATA']._serialized_start = 1189
    _globals['_UNDEPLOYMODELOPERATIONMETADATA']._serialized_end = 1221
    _globals['_CREATEDATASETOPERATIONMETADATA']._serialized_start = 1223
    _globals['_CREATEDATASETOPERATIONMETADATA']._serialized_end = 1255
    _globals['_CREATEMODELOPERATIONMETADATA']._serialized_start = 1257
    _globals['_CREATEMODELOPERATIONMETADATA']._serialized_end = 1287
    _globals['_IMPORTDATAOPERATIONMETADATA']._serialized_start = 1289
    _globals['_IMPORTDATAOPERATIONMETADATA']._serialized_end = 1318
    _globals['_EXPORTDATAOPERATIONMETADATA']._serialized_start = 1321
    _globals['_EXPORTDATAOPERATIONMETADATA']._serialized_end = 1520
    _globals['_EXPORTDATAOPERATIONMETADATA_EXPORTDATAOUTPUTINFO']._serialized_start = 1447
    _globals['_EXPORTDATAOPERATIONMETADATA_EXPORTDATAOUTPUTINFO']._serialized_end = 1520
    _globals['_BATCHPREDICTOPERATIONMETADATA']._serialized_start = 1523
    _globals['_BATCHPREDICTOPERATIONMETADATA']._serialized_end = 1801
    _globals['_BATCHPREDICTOPERATIONMETADATA_BATCHPREDICTOUTPUTINFO']._serialized_start = 1726
    _globals['_BATCHPREDICTOPERATIONMETADATA_BATCHPREDICTOUTPUTINFO']._serialized_end = 1801
    _globals['_EXPORTMODELOPERATIONMETADATA']._serialized_start = 1804
    _globals['_EXPORTMODELOPERATIONMETADATA']._serialized_end = 1986
    _globals['_EXPORTMODELOPERATIONMETADATA_EXPORTMODELOUTPUTINFO']._serialized_start = 1933
    _globals['_EXPORTMODELOPERATIONMETADATA_EXPORTMODELOUTPUTINFO']._serialized_end = 1986