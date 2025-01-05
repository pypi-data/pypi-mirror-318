"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1beta1/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.automl.v1beta1 import annotation_payload_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_annotation__payload__pb2
from .....google.cloud.automl.v1beta1 import annotation_spec_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_annotation__spec__pb2
from .....google.cloud.automl.v1beta1 import column_spec_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_column__spec__pb2
from .....google.cloud.automl.v1beta1 import dataset_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_dataset__pb2
from .....google.cloud.automl.v1beta1 import image_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_image__pb2
from .....google.cloud.automl.v1beta1 import io_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_io__pb2
from .....google.cloud.automl.v1beta1 import model_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_model__pb2
from .....google.cloud.automl.v1beta1 import model_evaluation_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_model__evaluation__pb2
from .....google.cloud.automl.v1beta1 import operations_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_operations__pb2
from .....google.cloud.automl.v1beta1 import table_spec_pb2 as google_dot_cloud_dot_automl_dot_v1beta1_dot_table__spec__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/automl/v1beta1/service.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a4google/cloud/automl/v1beta1/annotation_payload.proto\x1a1google/cloud/automl/v1beta1/annotation_spec.proto\x1a-google/cloud/automl/v1beta1/column_spec.proto\x1a)google/cloud/automl/v1beta1/dataset.proto\x1a\'google/cloud/automl/v1beta1/image.proto\x1a$google/cloud/automl/v1beta1/io.proto\x1a\'google/cloud/automl/v1beta1/model.proto\x1a2google/cloud/automl/v1beta1/model_evaluation.proto\x1a,google/cloud/automl/v1beta1/operations.proto\x1a,google/cloud/automl/v1beta1/table_spec.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto"\x8d\x01\n\x14CreateDatasetRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12:\n\x07dataset\x18\x02 \x01(\x0b2$.google.cloud.automl.v1beta1.DatasetB\x03\xe0A\x02"H\n\x11GetDatasetRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dautoml.googleapis.com/Dataset"\x87\x01\n\x13ListDatasetsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x0e\n\x06filter\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t"g\n\x14ListDatasetsResponse\x126\n\x08datasets\x18\x01 \x03(\x0b2$.google.cloud.automl.v1beta1.Dataset\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x83\x01\n\x14UpdateDatasetRequest\x12:\n\x07dataset\x18\x01 \x01(\x0b2$.google.cloud.automl.v1beta1.DatasetB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"K\n\x14DeleteDatasetRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dautoml.googleapis.com/Dataset"\x8d\x01\n\x11ImportDataRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dautoml.googleapis.com/Dataset\x12C\n\x0cinput_config\x18\x03 \x01(\x0b2(.google.cloud.automl.v1beta1.InputConfigB\x03\xe0A\x02"\x8f\x01\n\x11ExportDataRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dautoml.googleapis.com/Dataset\x12E\n\routput_config\x18\x03 \x01(\x0b2).google.cloud.automl.v1beta1.OutputConfigB\x03\xe0A\x02"V\n\x18GetAnnotationSpecRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$automl.googleapis.com/AnnotationSpec"|\n\x13GetTableSpecRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fautoml.googleapis.com/TableSpec\x12.\n\nfield_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xb5\x01\n\x15ListTableSpecsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dautoml.googleapis.com/Dataset\x12.\n\nfield_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x0e\n\x06filter\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t"n\n\x16ListTableSpecsResponse\x12;\n\x0btable_specs\x18\x01 \x03(\x0b2&.google.cloud.automl.v1beta1.TableSpec\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x8a\x01\n\x16UpdateTableSpecRequest\x12?\n\ntable_spec\x18\x01 \x01(\x0b2&.google.cloud.automl.v1beta1.TableSpecB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"~\n\x14GetColumnSpecRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n automl.googleapis.com/ColumnSpec\x12.\n\nfield_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xb8\x01\n\x16ListColumnSpecsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fautoml.googleapis.com/TableSpec\x12.\n\nfield_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x0e\n\x06filter\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t"q\n\x17ListColumnSpecsResponse\x12=\n\x0ccolumn_specs\x18\x01 \x03(\x0b2\'.google.cloud.automl.v1beta1.ColumnSpec\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x8d\x01\n\x17UpdateColumnSpecRequest\x12A\n\x0bcolumn_spec\x18\x01 \x01(\x0b2\'.google.cloud.automl.v1beta1.ColumnSpecB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x87\x01\n\x12CreateModelRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x126\n\x05model\x18\x04 \x01(\x0b2".google.cloud.automl.v1beta1.ModelB\x03\xe0A\x02"D\n\x0fGetModelRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model"\x85\x01\n\x11ListModelsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x0e\n\x06filter\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t"`\n\x12ListModelsResponse\x121\n\x05model\x18\x01 \x03(\x0b2".google.cloud.automl.v1beta1.Model\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"G\n\x12DeleteModelRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model"\xef\x02\n\x12DeployModelRequest\x12\x84\x01\n0image_object_detection_model_deployment_metadata\x18\x02 \x01(\x0b2H.google.cloud.automl.v1beta1.ImageObjectDetectionModelDeploymentMetadataH\x00\x12\x81\x01\n.image_classification_model_deployment_metadata\x18\x04 \x01(\x0b2G.google.cloud.automl.v1beta1.ImageClassificationModelDeploymentMetadataH\x00\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/ModelB\x1b\n\x19model_deployment_metadata"I\n\x14UndeployModelRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model"\x99\x01\n\x12ExportModelRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model\x12P\n\routput_config\x18\x03 \x01(\x0b24.google.cloud.automl.v1beta1.ModelExportOutputConfigB\x03\xe0A\x02"\xb1\x01\n\x1eExportEvaluatedExamplesRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model\x12\\\n\routput_config\x18\x03 \x01(\x0b2@.google.cloud.automl.v1beta1.ExportEvaluatedExamplesOutputConfigB\x03\xe0A\x02"X\n\x19GetModelEvaluationRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%automl.googleapis.com/ModelEvaluation"\x89\x01\n\x1bListModelEvaluationsRequest\x123\n\x06parent\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model\x12\x0e\n\x06filter\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t"\x7f\n\x1cListModelEvaluationsResponse\x12F\n\x10model_evaluation\x18\x01 \x03(\x0b2,.google.cloud.automl.v1beta1.ModelEvaluation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xed\'\n\x06AutoMl\x12\xbd\x01\n\rCreateDataset\x121.google.cloud.automl.v1beta1.CreateDatasetRequest\x1a$.google.cloud.automl.v1beta1.Dataset"S\xdaA\x0eparent,dataset\x82\xd3\xe4\x93\x02<"1/v1beta1/{parent=projects/*/locations/*}/datasets:\x07dataset\x12\xa4\x01\n\nGetDataset\x12..google.cloud.automl.v1beta1.GetDatasetRequest\x1a$.google.cloud.automl.v1beta1.Dataset"@\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1beta1/{name=projects/*/locations/*/datasets/*}\x12\xb7\x01\n\x0cListDatasets\x120.google.cloud.automl.v1beta1.ListDatasetsRequest\x1a1.google.cloud.automl.v1beta1.ListDatasetsResponse"B\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1beta1/{parent=projects/*/locations/*}/datasets\x12\xbe\x01\n\rUpdateDataset\x121.google.cloud.automl.v1beta1.UpdateDatasetRequest\x1a$.google.cloud.automl.v1beta1.Dataset"T\xdaA\x07dataset\x82\xd3\xe4\x93\x02D29/v1beta1/{dataset.name=projects/*/locations/*/datasets/*}:\x07dataset\x12\xd0\x01\n\rDeleteDataset\x121.google.cloud.automl.v1beta1.DeleteDatasetRequest\x1a\x1d.google.longrunning.Operation"m\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x023*1/v1beta1/{name=projects/*/locations/*/datasets/*}\x12\xe6\x01\n\nImportData\x12..google.cloud.automl.v1beta1.ImportDataRequest\x1a\x1d.google.longrunning.Operation"\x88\x01\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x11name,input_config\x82\xd3\xe4\x93\x02A"</v1beta1/{name=projects/*/locations/*/datasets/*}:importData:\x01*\x12\xe7\x01\n\nExportData\x12..google.cloud.automl.v1beta1.ExportDataRequest\x1a\x1d.google.longrunning.Operation"\x89\x01\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x12name,output_config\x82\xd3\xe4\x93\x02A"</v1beta1/{name=projects/*/locations/*/datasets/*}:exportData:\x01*\x12\xcb\x01\n\x11GetAnnotationSpec\x125.google.cloud.automl.v1beta1.GetAnnotationSpecRequest\x1a+.google.cloud.automl.v1beta1.AnnotationSpec"R\xdaA\x04name\x82\xd3\xe4\x93\x02E\x12C/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*}\x12\xb7\x01\n\x0cGetTableSpec\x120.google.cloud.automl.v1beta1.GetTableSpecRequest\x1a&.google.cloud.automl.v1beta1.TableSpec"M\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1beta1/{name=projects/*/locations/*/datasets/*/tableSpecs/*}\x12\xca\x01\n\x0eListTableSpecs\x122.google.cloud.automl.v1beta1.ListTableSpecsRequest\x1a3.google.cloud.automl.v1beta1.ListTableSpecsResponse"O\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v1beta1/{parent=projects/*/locations/*/datasets/*}/tableSpecs\x12\xda\x01\n\x0fUpdateTableSpec\x123.google.cloud.automl.v1beta1.UpdateTableSpecRequest\x1a&.google.cloud.automl.v1beta1.TableSpec"j\xdaA\ntable_spec\x82\xd3\xe4\x93\x02W2I/v1beta1/{table_spec.name=projects/*/locations/*/datasets/*/tableSpecs/*}:\ntable_spec\x12\xc8\x01\n\rGetColumnSpec\x121.google.cloud.automl.v1beta1.GetColumnSpecRequest\x1a\'.google.cloud.automl.v1beta1.ColumnSpec"[\xdaA\x04name\x82\xd3\xe4\x93\x02N\x12L/v1beta1/{name=projects/*/locations/*/datasets/*/tableSpecs/*/columnSpecs/*}\x12\xdb\x01\n\x0fListColumnSpecs\x123.google.cloud.automl.v1beta1.ListColumnSpecsRequest\x1a4.google.cloud.automl.v1beta1.ListColumnSpecsResponse"]\xdaA\x06parent\x82\xd3\xe4\x93\x02N\x12L/v1beta1/{parent=projects/*/locations/*/datasets/*/tableSpecs/*}/columnSpecs\x12\xee\x01\n\x10UpdateColumnSpec\x124.google.cloud.automl.v1beta1.UpdateColumnSpecRequest\x1a\'.google.cloud.automl.v1beta1.ColumnSpec"{\xdaA\x0bcolumn_spec\x82\xd3\xe4\x93\x02g2X/v1beta1/{column_spec.name=projects/*/locations/*/datasets/*/tableSpecs/*/columnSpecs/*}:\x0bcolumn_spec\x12\xc9\x01\n\x0bCreateModel\x12/.google.cloud.automl.v1beta1.CreateModelRequest\x1a\x1d.google.longrunning.Operation"j\xcaA\x1a\n\x05Model\x12\x11OperationMetadata\xdaA\x0cparent,model\x82\xd3\xe4\x93\x028"//v1beta1/{parent=projects/*/locations/*}/models:\x05model\x12\x9c\x01\n\x08GetModel\x12,.google.cloud.automl.v1beta1.GetModelRequest\x1a".google.cloud.automl.v1beta1.Model">\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1beta1/{name=projects/*/locations/*/models/*}\x12\xaf\x01\n\nListModels\x12..google.cloud.automl.v1beta1.ListModelsRequest\x1a/.google.cloud.automl.v1beta1.ListModelsResponse"@\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1beta1/{parent=projects/*/locations/*}/models\x12\xca\x01\n\x0bDeleteModel\x12/.google.cloud.automl.v1beta1.DeleteModelRequest\x1a\x1d.google.longrunning.Operation"k\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1beta1/{name=projects/*/locations/*/models/*}\x12\xd4\x01\n\x0bDeployModel\x12/.google.cloud.automl.v1beta1.DeployModelRequest\x1a\x1d.google.longrunning.Operation"u\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02;"6/v1beta1/{name=projects/*/locations/*/models/*}:deploy:\x01*\x12\xda\x01\n\rUndeployModel\x121.google.cloud.automl.v1beta1.UndeployModelRequest\x1a\x1d.google.longrunning.Operation"w\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02="8/v1beta1/{name=projects/*/locations/*/models/*}:undeploy:\x01*\x12\xe3\x01\n\x0bExportModel\x12/.google.cloud.automl.v1beta1.ExportModelRequest\x1a\x1d.google.longrunning.Operation"\x83\x01\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x12name,output_config\x82\xd3\xe4\x93\x02;"6/v1beta1/{name=projects/*/locations/*/models/*}:export:\x01*\x12\x8c\x02\n\x17ExportEvaluatedExamples\x12;.google.cloud.automl.v1beta1.ExportEvaluatedExamplesRequest\x1a\x1d.google.longrunning.Operation"\x94\x01\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x12name,output_config\x82\xd3\xe4\x93\x02L"G/v1beta1/{name=projects/*/locations/*/models/*}:exportEvaluatedExamples:\x01*\x12\xcd\x01\n\x12GetModelEvaluation\x126.google.cloud.automl.v1beta1.GetModelEvaluationRequest\x1a,.google.cloud.automl.v1beta1.ModelEvaluation"Q\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/v1beta1/{name=projects/*/locations/*/models/*/modelEvaluations/*}\x12\xe0\x01\n\x14ListModelEvaluations\x128.google.cloud.automl.v1beta1.ListModelEvaluationsRequest\x1a9.google.cloud.automl.v1beta1.ListModelEvaluationsResponse"S\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/v1beta1/{parent=projects/*/locations/*/models/*}/modelEvaluations\x1aI\xcaA\x15automl.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa8\x01\n\x1fcom.google.cloud.automl.v1beta1B\x0bAutoMlProtoP\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1beta1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.automl.v1beta1B\x0bAutoMlProtoP\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1'
    _globals['_CREATEDATASETREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDATASETREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEDATASETREQUEST'].fields_by_name['dataset']._loaded_options = None
    _globals['_CREATEDATASETREQUEST'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02'
    _globals['_GETDATASETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATASETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dautoml.googleapis.com/Dataset'
    _globals['_LISTDATASETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATASETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_UPDATEDATASETREQUEST'].fields_by_name['dataset']._loaded_options = None
    _globals['_UPDATEDATASETREQUEST'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEDATASETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDATASETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dautoml.googleapis.com/Dataset'
    _globals['_IMPORTDATAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_IMPORTDATAREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dautoml.googleapis.com/Dataset'
    _globals['_IMPORTDATAREQUEST'].fields_by_name['input_config']._loaded_options = None
    _globals['_IMPORTDATAREQUEST'].fields_by_name['input_config']._serialized_options = b'\xe0A\x02'
    _globals['_EXPORTDATAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_EXPORTDATAREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dautoml.googleapis.com/Dataset'
    _globals['_EXPORTDATAREQUEST'].fields_by_name['output_config']._loaded_options = None
    _globals['_EXPORTDATAREQUEST'].fields_by_name['output_config']._serialized_options = b'\xe0A\x02'
    _globals['_GETANNOTATIONSPECREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETANNOTATIONSPECREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$automl.googleapis.com/AnnotationSpec'
    _globals['_GETTABLESPECREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTABLESPECREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fautoml.googleapis.com/TableSpec'
    _globals['_LISTTABLESPECSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTABLESPECSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dautoml.googleapis.com/Dataset'
    _globals['_UPDATETABLESPECREQUEST'].fields_by_name['table_spec']._loaded_options = None
    _globals['_UPDATETABLESPECREQUEST'].fields_by_name['table_spec']._serialized_options = b'\xe0A\x02'
    _globals['_GETCOLUMNSPECREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCOLUMNSPECREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n automl.googleapis.com/ColumnSpec'
    _globals['_LISTCOLUMNSPECSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCOLUMNSPECSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fautoml.googleapis.com/TableSpec'
    _globals['_UPDATECOLUMNSPECREQUEST'].fields_by_name['column_spec']._loaded_options = None
    _globals['_UPDATECOLUMNSPECREQUEST'].fields_by_name['column_spec']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEMODELREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEMODELREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEMODELREQUEST'].fields_by_name['model']._loaded_options = None
    _globals['_CREATEMODELREQUEST'].fields_by_name['model']._serialized_options = b'\xe0A\x02'
    _globals['_GETMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMODELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model'
    _globals['_LISTMODELSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMODELSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_DELETEMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEMODELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model'
    _globals['_DEPLOYMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DEPLOYMODELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model'
    _globals['_UNDEPLOYMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UNDEPLOYMODELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model'
    _globals['_EXPORTMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_EXPORTMODELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model'
    _globals['_EXPORTMODELREQUEST'].fields_by_name['output_config']._loaded_options = None
    _globals['_EXPORTMODELREQUEST'].fields_by_name['output_config']._serialized_options = b'\xe0A\x02'
    _globals['_EXPORTEVALUATEDEXAMPLESREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_EXPORTEVALUATEDEXAMPLESREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model'
    _globals['_EXPORTEVALUATEDEXAMPLESREQUEST'].fields_by_name['output_config']._loaded_options = None
    _globals['_EXPORTEVALUATEDEXAMPLESREQUEST'].fields_by_name['output_config']._serialized_options = b'\xe0A\x02'
    _globals['_GETMODELEVALUATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMODELEVALUATIONREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%automl.googleapis.com/ModelEvaluation"
    _globals['_LISTMODELEVALUATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMODELEVALUATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model'
    _globals['_AUTOML']._loaded_options = None
    _globals['_AUTOML']._serialized_options = b'\xcaA\x15automl.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_AUTOML'].methods_by_name['CreateDataset']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['CreateDataset']._serialized_options = b'\xdaA\x0eparent,dataset\x82\xd3\xe4\x93\x02<"1/v1beta1/{parent=projects/*/locations/*}/datasets:\x07dataset'
    _globals['_AUTOML'].methods_by_name['GetDataset']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['GetDataset']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1beta1/{name=projects/*/locations/*/datasets/*}'
    _globals['_AUTOML'].methods_by_name['ListDatasets']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['ListDatasets']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1beta1/{parent=projects/*/locations/*}/datasets'
    _globals['_AUTOML'].methods_by_name['UpdateDataset']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['UpdateDataset']._serialized_options = b'\xdaA\x07dataset\x82\xd3\xe4\x93\x02D29/v1beta1/{dataset.name=projects/*/locations/*/datasets/*}:\x07dataset'
    _globals['_AUTOML'].methods_by_name['DeleteDataset']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['DeleteDataset']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x023*1/v1beta1/{name=projects/*/locations/*/datasets/*}'
    _globals['_AUTOML'].methods_by_name['ImportData']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['ImportData']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x11name,input_config\x82\xd3\xe4\x93\x02A"</v1beta1/{name=projects/*/locations/*/datasets/*}:importData:\x01*'
    _globals['_AUTOML'].methods_by_name['ExportData']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['ExportData']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x12name,output_config\x82\xd3\xe4\x93\x02A"</v1beta1/{name=projects/*/locations/*/datasets/*}:exportData:\x01*'
    _globals['_AUTOML'].methods_by_name['GetAnnotationSpec']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['GetAnnotationSpec']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02E\x12C/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*}'
    _globals['_AUTOML'].methods_by_name['GetTableSpec']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['GetTableSpec']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1beta1/{name=projects/*/locations/*/datasets/*/tableSpecs/*}'
    _globals['_AUTOML'].methods_by_name['ListTableSpecs']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['ListTableSpecs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v1beta1/{parent=projects/*/locations/*/datasets/*}/tableSpecs'
    _globals['_AUTOML'].methods_by_name['UpdateTableSpec']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['UpdateTableSpec']._serialized_options = b'\xdaA\ntable_spec\x82\xd3\xe4\x93\x02W2I/v1beta1/{table_spec.name=projects/*/locations/*/datasets/*/tableSpecs/*}:\ntable_spec'
    _globals['_AUTOML'].methods_by_name['GetColumnSpec']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['GetColumnSpec']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02N\x12L/v1beta1/{name=projects/*/locations/*/datasets/*/tableSpecs/*/columnSpecs/*}'
    _globals['_AUTOML'].methods_by_name['ListColumnSpecs']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['ListColumnSpecs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02N\x12L/v1beta1/{parent=projects/*/locations/*/datasets/*/tableSpecs/*}/columnSpecs'
    _globals['_AUTOML'].methods_by_name['UpdateColumnSpec']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['UpdateColumnSpec']._serialized_options = b'\xdaA\x0bcolumn_spec\x82\xd3\xe4\x93\x02g2X/v1beta1/{column_spec.name=projects/*/locations/*/datasets/*/tableSpecs/*/columnSpecs/*}:\x0bcolumn_spec'
    _globals['_AUTOML'].methods_by_name['CreateModel']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['CreateModel']._serialized_options = b'\xcaA\x1a\n\x05Model\x12\x11OperationMetadata\xdaA\x0cparent,model\x82\xd3\xe4\x93\x028"//v1beta1/{parent=projects/*/locations/*}/models:\x05model'
    _globals['_AUTOML'].methods_by_name['GetModel']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['GetModel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1beta1/{name=projects/*/locations/*/models/*}'
    _globals['_AUTOML'].methods_by_name['ListModels']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['ListModels']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1beta1/{parent=projects/*/locations/*}/models'
    _globals['_AUTOML'].methods_by_name['DeleteModel']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['DeleteModel']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1beta1/{name=projects/*/locations/*/models/*}'
    _globals['_AUTOML'].methods_by_name['DeployModel']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['DeployModel']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02;"6/v1beta1/{name=projects/*/locations/*/models/*}:deploy:\x01*'
    _globals['_AUTOML'].methods_by_name['UndeployModel']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['UndeployModel']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02="8/v1beta1/{name=projects/*/locations/*/models/*}:undeploy:\x01*'
    _globals['_AUTOML'].methods_by_name['ExportModel']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['ExportModel']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x12name,output_config\x82\xd3\xe4\x93\x02;"6/v1beta1/{name=projects/*/locations/*/models/*}:export:\x01*'
    _globals['_AUTOML'].methods_by_name['ExportEvaluatedExamples']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['ExportEvaluatedExamples']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x12name,output_config\x82\xd3\xe4\x93\x02L"G/v1beta1/{name=projects/*/locations/*/models/*}:exportEvaluatedExamples:\x01*'
    _globals['_AUTOML'].methods_by_name['GetModelEvaluation']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['GetModelEvaluation']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/v1beta1/{name=projects/*/locations/*/models/*/modelEvaluations/*}'
    _globals['_AUTOML'].methods_by_name['ListModelEvaluations']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['ListModelEvaluations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/v1beta1/{parent=projects/*/locations/*/models/*}/modelEvaluations'
    _globals['_CREATEDATASETREQUEST']._serialized_start = 720
    _globals['_CREATEDATASETREQUEST']._serialized_end = 861
    _globals['_GETDATASETREQUEST']._serialized_start = 863
    _globals['_GETDATASETREQUEST']._serialized_end = 935
    _globals['_LISTDATASETSREQUEST']._serialized_start = 938
    _globals['_LISTDATASETSREQUEST']._serialized_end = 1073
    _globals['_LISTDATASETSRESPONSE']._serialized_start = 1075
    _globals['_LISTDATASETSRESPONSE']._serialized_end = 1178
    _globals['_UPDATEDATASETREQUEST']._serialized_start = 1181
    _globals['_UPDATEDATASETREQUEST']._serialized_end = 1312
    _globals['_DELETEDATASETREQUEST']._serialized_start = 1314
    _globals['_DELETEDATASETREQUEST']._serialized_end = 1389
    _globals['_IMPORTDATAREQUEST']._serialized_start = 1392
    _globals['_IMPORTDATAREQUEST']._serialized_end = 1533
    _globals['_EXPORTDATAREQUEST']._serialized_start = 1536
    _globals['_EXPORTDATAREQUEST']._serialized_end = 1679
    _globals['_GETANNOTATIONSPECREQUEST']._serialized_start = 1681
    _globals['_GETANNOTATIONSPECREQUEST']._serialized_end = 1767
    _globals['_GETTABLESPECREQUEST']._serialized_start = 1769
    _globals['_GETTABLESPECREQUEST']._serialized_end = 1893
    _globals['_LISTTABLESPECSREQUEST']._serialized_start = 1896
    _globals['_LISTTABLESPECSREQUEST']._serialized_end = 2077
    _globals['_LISTTABLESPECSRESPONSE']._serialized_start = 2079
    _globals['_LISTTABLESPECSRESPONSE']._serialized_end = 2189
    _globals['_UPDATETABLESPECREQUEST']._serialized_start = 2192
    _globals['_UPDATETABLESPECREQUEST']._serialized_end = 2330
    _globals['_GETCOLUMNSPECREQUEST']._serialized_start = 2332
    _globals['_GETCOLUMNSPECREQUEST']._serialized_end = 2458
    _globals['_LISTCOLUMNSPECSREQUEST']._serialized_start = 2461
    _globals['_LISTCOLUMNSPECSREQUEST']._serialized_end = 2645
    _globals['_LISTCOLUMNSPECSRESPONSE']._serialized_start = 2647
    _globals['_LISTCOLUMNSPECSRESPONSE']._serialized_end = 2760
    _globals['_UPDATECOLUMNSPECREQUEST']._serialized_start = 2763
    _globals['_UPDATECOLUMNSPECREQUEST']._serialized_end = 2904
    _globals['_CREATEMODELREQUEST']._serialized_start = 2907
    _globals['_CREATEMODELREQUEST']._serialized_end = 3042
    _globals['_GETMODELREQUEST']._serialized_start = 3044
    _globals['_GETMODELREQUEST']._serialized_end = 3112
    _globals['_LISTMODELSREQUEST']._serialized_start = 3115
    _globals['_LISTMODELSREQUEST']._serialized_end = 3248
    _globals['_LISTMODELSRESPONSE']._serialized_start = 3250
    _globals['_LISTMODELSRESPONSE']._serialized_end = 3346
    _globals['_DELETEMODELREQUEST']._serialized_start = 3348
    _globals['_DELETEMODELREQUEST']._serialized_end = 3419
    _globals['_DEPLOYMODELREQUEST']._serialized_start = 3422
    _globals['_DEPLOYMODELREQUEST']._serialized_end = 3789
    _globals['_UNDEPLOYMODELREQUEST']._serialized_start = 3791
    _globals['_UNDEPLOYMODELREQUEST']._serialized_end = 3864
    _globals['_EXPORTMODELREQUEST']._serialized_start = 3867
    _globals['_EXPORTMODELREQUEST']._serialized_end = 4020
    _globals['_EXPORTEVALUATEDEXAMPLESREQUEST']._serialized_start = 4023
    _globals['_EXPORTEVALUATEDEXAMPLESREQUEST']._serialized_end = 4200
    _globals['_GETMODELEVALUATIONREQUEST']._serialized_start = 4202
    _globals['_GETMODELEVALUATIONREQUEST']._serialized_end = 4290
    _globals['_LISTMODELEVALUATIONSREQUEST']._serialized_start = 4293
    _globals['_LISTMODELEVALUATIONSREQUEST']._serialized_end = 4430
    _globals['_LISTMODELEVALUATIONSRESPONSE']._serialized_start = 4432
    _globals['_LISTMODELEVALUATIONSRESPONSE']._serialized_end = 4559
    _globals['_AUTOML']._serialized_start = 4562
    _globals['_AUTOML']._serialized_end = 9663