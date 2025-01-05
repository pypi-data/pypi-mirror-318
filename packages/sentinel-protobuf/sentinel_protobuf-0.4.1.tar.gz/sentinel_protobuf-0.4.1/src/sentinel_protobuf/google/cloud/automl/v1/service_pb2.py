"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.automl.v1 import annotation_payload_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_annotation__payload__pb2
from .....google.cloud.automl.v1 import annotation_spec_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_annotation__spec__pb2
from .....google.cloud.automl.v1 import dataset_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_dataset__pb2
from .....google.cloud.automl.v1 import image_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_image__pb2
from .....google.cloud.automl.v1 import io_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_io__pb2
from .....google.cloud.automl.v1 import model_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_model__pb2
from .....google.cloud.automl.v1 import model_evaluation_pb2 as google_dot_cloud_dot_automl_dot_v1_dot_model__evaluation__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/cloud/automl/v1/service.proto\x12\x16google.cloud.automl.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/automl/v1/annotation_payload.proto\x1a,google/cloud/automl/v1/annotation_spec.proto\x1a$google/cloud/automl/v1/dataset.proto\x1a"google/cloud/automl/v1/image.proto\x1a\x1fgoogle/cloud/automl/v1/io.proto\x1a"google/cloud/automl/v1/model.proto\x1a-google/cloud/automl/v1/model_evaluation.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto"\x88\x01\n\x14CreateDatasetRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x125\n\x07dataset\x18\x02 \x01(\x0b2\x1f.google.cloud.automl.v1.DatasetB\x03\xe0A\x02"H\n\x11GetDatasetRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dautoml.googleapis.com/Dataset"\x87\x01\n\x13ListDatasetsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x0e\n\x06filter\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t"b\n\x14ListDatasetsResponse\x121\n\x08datasets\x18\x01 \x03(\x0b2\x1f.google.cloud.automl.v1.Dataset\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x83\x01\n\x14UpdateDatasetRequest\x125\n\x07dataset\x18\x01 \x01(\x0b2\x1f.google.cloud.automl.v1.DatasetB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"K\n\x14DeleteDatasetRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dautoml.googleapis.com/Dataset"\x88\x01\n\x11ImportDataRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dautoml.googleapis.com/Dataset\x12>\n\x0cinput_config\x18\x03 \x01(\x0b2#.google.cloud.automl.v1.InputConfigB\x03\xe0A\x02"\x8a\x01\n\x11ExportDataRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dautoml.googleapis.com/Dataset\x12@\n\routput_config\x18\x03 \x01(\x0b2$.google.cloud.automl.v1.OutputConfigB\x03\xe0A\x02"V\n\x18GetAnnotationSpecRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$automl.googleapis.com/AnnotationSpec"\x82\x01\n\x12CreateModelRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x121\n\x05model\x18\x04 \x01(\x0b2\x1d.google.cloud.automl.v1.ModelB\x03\xe0A\x02"D\n\x0fGetModelRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model"\x85\x01\n\x11ListModelsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x0e\n\x06filter\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t"[\n\x12ListModelsResponse\x12,\n\x05model\x18\x01 \x03(\x0b2\x1d.google.cloud.automl.v1.Model\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"G\n\x12DeleteModelRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model"}\n\x12UpdateModelRequest\x121\n\x05model\x18\x01 \x01(\x0b2\x1d.google.cloud.automl.v1.ModelB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\xe3\x02\n\x12DeployModelRequest\x12\x7f\n0image_object_detection_model_deployment_metadata\x18\x02 \x01(\x0b2C.google.cloud.automl.v1.ImageObjectDetectionModelDeploymentMetadataH\x00\x12|\n.image_classification_model_deployment_metadata\x18\x04 \x01(\x0b2B.google.cloud.automl.v1.ImageClassificationModelDeploymentMetadataH\x00\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/ModelB\x1b\n\x19model_deployment_metadata"I\n\x14UndeployModelRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model"\x94\x01\n\x12ExportModelRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model\x12K\n\routput_config\x18\x03 \x01(\x0b2/.google.cloud.automl.v1.ModelExportOutputConfigB\x03\xe0A\x02"X\n\x19GetModelEvaluationRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%automl.googleapis.com/ModelEvaluation"\x8e\x01\n\x1bListModelEvaluationsRequest\x123\n\x06parent\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model\x12\x13\n\x06filter\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t"z\n\x1cListModelEvaluationsResponse\x12A\n\x10model_evaluation\x18\x01 \x03(\x0b2\'.google.cloud.automl.v1.ModelEvaluation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xe8\x1b\n\x06AutoMl\x12\xcb\x01\n\rCreateDataset\x12,.google.cloud.automl.v1.CreateDatasetRequest\x1a\x1d.google.longrunning.Operation"m\xcaA\x1c\n\x07Dataset\x12\x11OperationMetadata\xdaA\x0eparent,dataset\x82\xd3\xe4\x93\x027",/v1/{parent=projects/*/locations/*}/datasets:\x07dataset\x12\x95\x01\n\nGetDataset\x12).google.cloud.automl.v1.GetDatasetRequest\x1a\x1f.google.cloud.automl.v1.Dataset";\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/locations/*/datasets/*}\x12\xa8\x01\n\x0cListDatasets\x12+.google.cloud.automl.v1.ListDatasetsRequest\x1a,.google.cloud.automl.v1.ListDatasetsResponse"=\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/datasets\x12\xbb\x01\n\rUpdateDataset\x12,.google.cloud.automl.v1.UpdateDatasetRequest\x1a\x1f.google.cloud.automl.v1.Dataset"[\xdaA\x13dataset,update_mask\x82\xd3\xe4\x93\x02?24/v1/{dataset.name=projects/*/locations/*/datasets/*}:\x07dataset\x12\xc6\x01\n\rDeleteDataset\x12,.google.cloud.automl.v1.DeleteDatasetRequest\x1a\x1d.google.longrunning.Operation"h\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02.*,/v1/{name=projects/*/locations/*/datasets/*}\x12\xdc\x01\n\nImportData\x12).google.cloud.automl.v1.ImportDataRequest\x1a\x1d.google.longrunning.Operation"\x83\x01\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x11name,input_config\x82\xd3\xe4\x93\x02<"7/v1/{name=projects/*/locations/*/datasets/*}:importData:\x01*\x12\xdd\x01\n\nExportData\x12).google.cloud.automl.v1.ExportDataRequest\x1a\x1d.google.longrunning.Operation"\x84\x01\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x12name,output_config\x82\xd3\xe4\x93\x02<"7/v1/{name=projects/*/locations/*/datasets/*}:exportData:\x01*\x12\xbc\x01\n\x11GetAnnotationSpec\x120.google.cloud.automl.v1.GetAnnotationSpecRequest\x1a&.google.cloud.automl.v1.AnnotationSpec"M\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*}\x12\xbf\x01\n\x0bCreateModel\x12*.google.cloud.automl.v1.CreateModelRequest\x1a\x1d.google.longrunning.Operation"e\xcaA\x1a\n\x05Model\x12\x11OperationMetadata\xdaA\x0cparent,model\x82\xd3\xe4\x93\x023"*/v1/{parent=projects/*/locations/*}/models:\x05model\x12\x8d\x01\n\x08GetModel\x12\'.google.cloud.automl.v1.GetModelRequest\x1a\x1d.google.cloud.automl.v1.Model"9\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/v1/{name=projects/*/locations/*/models/*}\x12\xa0\x01\n\nListModels\x12).google.cloud.automl.v1.ListModelsRequest\x1a*.google.cloud.automl.v1.ListModelsResponse";\xdaA\x06parent\x82\xd3\xe4\x93\x02,\x12*/v1/{parent=projects/*/locations/*}/models\x12\xc0\x01\n\x0bDeleteModel\x12*.google.cloud.automl.v1.DeleteModelRequest\x1a\x1d.google.longrunning.Operation"f\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02,**/v1/{name=projects/*/locations/*/models/*}\x12\xad\x01\n\x0bUpdateModel\x12*.google.cloud.automl.v1.UpdateModelRequest\x1a\x1d.google.cloud.automl.v1.Model"S\xdaA\x11model,update_mask\x82\xd3\xe4\x93\x02920/v1/{model.name=projects/*/locations/*/models/*}:\x05model\x12\xca\x01\n\x0bDeployModel\x12*.google.cloud.automl.v1.DeployModelRequest\x1a\x1d.google.longrunning.Operation"p\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x026"1/v1/{name=projects/*/locations/*/models/*}:deploy:\x01*\x12\xd0\x01\n\rUndeployModel\x12,.google.cloud.automl.v1.UndeployModelRequest\x1a\x1d.google.longrunning.Operation"r\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x028"3/v1/{name=projects/*/locations/*/models/*}:undeploy:\x01*\x12\xd8\x01\n\x0bExportModel\x12*.google.cloud.automl.v1.ExportModelRequest\x1a\x1d.google.longrunning.Operation"~\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x12name,output_config\x82\xd3\xe4\x93\x026"1/v1/{name=projects/*/locations/*/models/*}:export:\x01*\x12\xbe\x01\n\x12GetModelEvaluation\x121.google.cloud.automl.v1.GetModelEvaluationRequest\x1a\'.google.cloud.automl.v1.ModelEvaluation"L\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1/{name=projects/*/locations/*/models/*/modelEvaluations/*}\x12\xd8\x01\n\x14ListModelEvaluations\x123.google.cloud.automl.v1.ListModelEvaluationsRequest\x1a4.google.cloud.automl.v1.ListModelEvaluationsResponse"U\xdaA\rparent,filter\x82\xd3\xe4\x93\x02?\x12=/v1/{parent=projects/*/locations/*/models/*}/modelEvaluations\x1aI\xcaA\x15automl.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xad\x01\n\x1acom.google.cloud.automl.v1B\x0bAutoMlProtoP\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.automl.v1B\x0bAutoMlProtoP\x01Z2cloud.google.com/go/automl/apiv1/automlpb;automlpb\xaa\x02\x16Google.Cloud.AutoML.V1\xca\x02\x16Google\\Cloud\\AutoMl\\V1\xea\x02\x19Google::Cloud::AutoML::V1'
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
    _globals['_UPDATEDATASETREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEDATASETREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
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
    _globals['_UPDATEMODELREQUEST'].fields_by_name['model']._loaded_options = None
    _globals['_UPDATEMODELREQUEST'].fields_by_name['model']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEMODELREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEMODELREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DEPLOYMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DEPLOYMODELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model'
    _globals['_UNDEPLOYMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UNDEPLOYMODELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model'
    _globals['_EXPORTMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_EXPORTMODELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model'
    _globals['_EXPORTMODELREQUEST'].fields_by_name['output_config']._loaded_options = None
    _globals['_EXPORTMODELREQUEST'].fields_by_name['output_config']._serialized_options = b'\xe0A\x02'
    _globals['_GETMODELEVALUATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMODELEVALUATIONREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%automl.googleapis.com/ModelEvaluation"
    _globals['_LISTMODELEVALUATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMODELEVALUATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model'
    _globals['_LISTMODELEVALUATIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTMODELEVALUATIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_AUTOML']._loaded_options = None
    _globals['_AUTOML']._serialized_options = b'\xcaA\x15automl.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_AUTOML'].methods_by_name['CreateDataset']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['CreateDataset']._serialized_options = b'\xcaA\x1c\n\x07Dataset\x12\x11OperationMetadata\xdaA\x0eparent,dataset\x82\xd3\xe4\x93\x027",/v1/{parent=projects/*/locations/*}/datasets:\x07dataset'
    _globals['_AUTOML'].methods_by_name['GetDataset']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['GetDataset']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/locations/*/datasets/*}'
    _globals['_AUTOML'].methods_by_name['ListDatasets']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['ListDatasets']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/datasets'
    _globals['_AUTOML'].methods_by_name['UpdateDataset']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['UpdateDataset']._serialized_options = b'\xdaA\x13dataset,update_mask\x82\xd3\xe4\x93\x02?24/v1/{dataset.name=projects/*/locations/*/datasets/*}:\x07dataset'
    _globals['_AUTOML'].methods_by_name['DeleteDataset']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['DeleteDataset']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02.*,/v1/{name=projects/*/locations/*/datasets/*}'
    _globals['_AUTOML'].methods_by_name['ImportData']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['ImportData']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x11name,input_config\x82\xd3\xe4\x93\x02<"7/v1/{name=projects/*/locations/*/datasets/*}:importData:\x01*'
    _globals['_AUTOML'].methods_by_name['ExportData']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['ExportData']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x12name,output_config\x82\xd3\xe4\x93\x02<"7/v1/{name=projects/*/locations/*/datasets/*}:exportData:\x01*'
    _globals['_AUTOML'].methods_by_name['GetAnnotationSpec']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['GetAnnotationSpec']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*}'
    _globals['_AUTOML'].methods_by_name['CreateModel']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['CreateModel']._serialized_options = b'\xcaA\x1a\n\x05Model\x12\x11OperationMetadata\xdaA\x0cparent,model\x82\xd3\xe4\x93\x023"*/v1/{parent=projects/*/locations/*}/models:\x05model'
    _globals['_AUTOML'].methods_by_name['GetModel']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['GetModel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/v1/{name=projects/*/locations/*/models/*}'
    _globals['_AUTOML'].methods_by_name['ListModels']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['ListModels']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02,\x12*/v1/{parent=projects/*/locations/*}/models'
    _globals['_AUTOML'].methods_by_name['DeleteModel']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['DeleteModel']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02,**/v1/{name=projects/*/locations/*/models/*}'
    _globals['_AUTOML'].methods_by_name['UpdateModel']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['UpdateModel']._serialized_options = b'\xdaA\x11model,update_mask\x82\xd3\xe4\x93\x02920/v1/{model.name=projects/*/locations/*/models/*}:\x05model'
    _globals['_AUTOML'].methods_by_name['DeployModel']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['DeployModel']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x026"1/v1/{name=projects/*/locations/*/models/*}:deploy:\x01*'
    _globals['_AUTOML'].methods_by_name['UndeployModel']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['UndeployModel']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x028"3/v1/{name=projects/*/locations/*/models/*}:undeploy:\x01*'
    _globals['_AUTOML'].methods_by_name['ExportModel']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['ExportModel']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x12name,output_config\x82\xd3\xe4\x93\x026"1/v1/{name=projects/*/locations/*/models/*}:export:\x01*'
    _globals['_AUTOML'].methods_by_name['GetModelEvaluation']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['GetModelEvaluation']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1/{name=projects/*/locations/*/models/*/modelEvaluations/*}'
    _globals['_AUTOML'].methods_by_name['ListModelEvaluations']._loaded_options = None
    _globals['_AUTOML'].methods_by_name['ListModelEvaluations']._serialized_options = b'\xdaA\rparent,filter\x82\xd3\xe4\x93\x02?\x12=/v1/{parent=projects/*/locations/*/models/*}/modelEvaluations'
    _globals['_CREATEDATASETREQUEST']._serialized_start = 536
    _globals['_CREATEDATASETREQUEST']._serialized_end = 672
    _globals['_GETDATASETREQUEST']._serialized_start = 674
    _globals['_GETDATASETREQUEST']._serialized_end = 746
    _globals['_LISTDATASETSREQUEST']._serialized_start = 749
    _globals['_LISTDATASETSREQUEST']._serialized_end = 884
    _globals['_LISTDATASETSRESPONSE']._serialized_start = 886
    _globals['_LISTDATASETSRESPONSE']._serialized_end = 984
    _globals['_UPDATEDATASETREQUEST']._serialized_start = 987
    _globals['_UPDATEDATASETREQUEST']._serialized_end = 1118
    _globals['_DELETEDATASETREQUEST']._serialized_start = 1120
    _globals['_DELETEDATASETREQUEST']._serialized_end = 1195
    _globals['_IMPORTDATAREQUEST']._serialized_start = 1198
    _globals['_IMPORTDATAREQUEST']._serialized_end = 1334
    _globals['_EXPORTDATAREQUEST']._serialized_start = 1337
    _globals['_EXPORTDATAREQUEST']._serialized_end = 1475
    _globals['_GETANNOTATIONSPECREQUEST']._serialized_start = 1477
    _globals['_GETANNOTATIONSPECREQUEST']._serialized_end = 1563
    _globals['_CREATEMODELREQUEST']._serialized_start = 1566
    _globals['_CREATEMODELREQUEST']._serialized_end = 1696
    _globals['_GETMODELREQUEST']._serialized_start = 1698
    _globals['_GETMODELREQUEST']._serialized_end = 1766
    _globals['_LISTMODELSREQUEST']._serialized_start = 1769
    _globals['_LISTMODELSREQUEST']._serialized_end = 1902
    _globals['_LISTMODELSRESPONSE']._serialized_start = 1904
    _globals['_LISTMODELSRESPONSE']._serialized_end = 1995
    _globals['_DELETEMODELREQUEST']._serialized_start = 1997
    _globals['_DELETEMODELREQUEST']._serialized_end = 2068
    _globals['_UPDATEMODELREQUEST']._serialized_start = 2070
    _globals['_UPDATEMODELREQUEST']._serialized_end = 2195
    _globals['_DEPLOYMODELREQUEST']._serialized_start = 2198
    _globals['_DEPLOYMODELREQUEST']._serialized_end = 2553
    _globals['_UNDEPLOYMODELREQUEST']._serialized_start = 2555
    _globals['_UNDEPLOYMODELREQUEST']._serialized_end = 2628
    _globals['_EXPORTMODELREQUEST']._serialized_start = 2631
    _globals['_EXPORTMODELREQUEST']._serialized_end = 2779
    _globals['_GETMODELEVALUATIONREQUEST']._serialized_start = 2781
    _globals['_GETMODELEVALUATIONREQUEST']._serialized_end = 2869
    _globals['_LISTMODELEVALUATIONSREQUEST']._serialized_start = 2872
    _globals['_LISTMODELEVALUATIONSREQUEST']._serialized_end = 3014
    _globals['_LISTMODELEVALUATIONSRESPONSE']._serialized_start = 3016
    _globals['_LISTMODELEVALUATIONSRESPONSE']._serialized_end = 3138
    _globals['_AUTOML']._serialized_start = 3141
    _globals['_AUTOML']._serialized_end = 6701