"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/dataset_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import annotation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_annotation__pb2
from .....google.cloud.aiplatform.v1beta1 import annotation_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_annotation__spec__pb2
from .....google.cloud.aiplatform.v1beta1 import data_item_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_data__item__pb2
from .....google.cloud.aiplatform.v1beta1 import dataset_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_dataset__pb2
from .....google.cloud.aiplatform.v1beta1 import dataset_version_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_dataset__version__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.cloud.aiplatform.v1beta1 import saved_query_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_saved__query__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/aiplatform/v1beta1/dataset_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/aiplatform/v1beta1/annotation.proto\x1a5google/cloud/aiplatform/v1beta1/annotation_spec.proto\x1a/google/cloud/aiplatform/v1beta1/data_item.proto\x1a-google/cloud/aiplatform/v1beta1/dataset.proto\x1a5google/cloud/aiplatform/v1beta1/dataset_version.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a1google/cloud/aiplatform/v1beta1/saved_query.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x91\x01\n\x14CreateDatasetRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12>\n\x07dataset\x18\x02 \x01(\x0b2(.google.cloud.aiplatform.v1beta1.DatasetB\x03\xe0A\x02"u\n\x1eCreateDatasetOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"{\n\x11GetDatasetRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset\x12-\n\tread_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x8c\x01\n\x14UpdateDatasetRequest\x12>\n\x07dataset\x18\x01 \x01(\x0b2(.google.cloud.aiplatform.v1beta1.DatasetB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\xa2\x01\n\x1bUpdateDatasetVersionRequest\x12M\n\x0fdataset_version\x18\x01 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.DatasetVersionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\xc8\x01\n\x13ListDatasetsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x10\n\x08order_by\x18\x06 \x01(\t"k\n\x14ListDatasetsResponse\x12:\n\x08datasets\x18\x01 \x03(\x0b2(.google.cloud.aiplatform.v1beta1.Dataset\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"O\n\x14DeleteDatasetRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset"\x9c\x01\n\x11ImportDataRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset\x12N\n\x0eimport_configs\x18\x02 \x03(\x0b21.google.cloud.aiplatform.v1beta1.ImportDataConfigB\x03\xe0A\x02"\x14\n\x12ImportDataResponse"r\n\x1bImportDataOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"\x9b\x01\n\x11ExportDataRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset\x12M\n\rexport_config\x18\x02 \x01(\x0b21.google.cloud.aiplatform.v1beta1.ExportDataConfigB\x03\xe0A\x02",\n\x12ExportDataResponse\x12\x16\n\x0eexported_files\x18\x01 \x03(\t"\x90\x01\n\x1bExportDataOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata\x12\x1c\n\x14gcs_output_directory\x18\x02 \x01(\t"\xa7\x01\n\x1bCreateDatasetVersionRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset\x12M\n\x0fdataset_version\x18\x02 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.DatasetVersionB\x03\xe0A\x02"|\n%CreateDatasetVersionOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"]\n\x1bDeleteDatasetVersionRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/DatasetVersion"\x89\x01\n\x18GetDatasetVersionRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/DatasetVersion\x12-\n\tread_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xe8\x01\n\x1aListDatasetVersionsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01\x122\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x06 \x01(\tB\x03\xe0A\x01"\x81\x01\n\x1bListDatasetVersionsResponse\x12I\n\x10dataset_versions\x18\x01 \x03(\x0b2/.google.cloud.aiplatform.v1beta1.DatasetVersion\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"^\n\x1cRestoreDatasetVersionRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/DatasetVersion"}\n&RestoreDatasetVersionOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"\xc9\x01\n\x14ListDataItemsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x10\n\x08order_by\x18\x06 \x01(\t"o\n\x15ListDataItemsResponse\x12=\n\ndata_items\x18\x01 \x03(\x0b2).google.cloud.aiplatform.v1beta1.DataItem\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xe1\x04\n\x16SearchDataItemsRequest\x12\x1c\n\x12order_by_data_item\x18\x0c \x01(\tH\x00\x12h\n\x13order_by_annotation\x18\r \x01(\x0b2I.google.cloud.aiplatform.v1beta1.SearchDataItemsRequest.OrderByAnnotationH\x00\x12:\n\x07dataset\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset\x12@\n\x0bsaved_query\x18\x02 \x01(\tB+\x18\x01\xfaA&\n$aiplatform.googleapis.com/SavedQuery\x12\x19\n\x11data_labeling_job\x18\x03 \x01(\t\x12\x18\n\x10data_item_filter\x18\x04 \x01(\t\x12\x1e\n\x12annotations_filter\x18\x05 \x01(\tB\x02\x18\x01\x12\x1a\n\x12annotation_filters\x18\x0b \x03(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x19\n\x11annotations_limit\x18\x07 \x01(\x05\x12\x11\n\tpage_size\x18\x08 \x01(\x05\x12\x14\n\x08order_by\x18\t \x01(\tB\x02\x18\x01\x12\x12\n\npage_token\x18\n \x01(\t\x1a?\n\x11OrderByAnnotation\x12\x18\n\x0bsaved_query\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x10\n\x08order_by\x18\x02 \x01(\tB\x07\n\x05order"z\n\x17SearchDataItemsResponse\x12F\n\x0fdata_item_views\x18\x01 \x03(\x0b2-.google.cloud.aiplatform.v1beta1.DataItemView\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xb1\x01\n\x0cDataItemView\x12<\n\tdata_item\x18\x01 \x01(\x0b2).google.cloud.aiplatform.v1beta1.DataItem\x12@\n\x0bannotations\x18\x02 \x03(\x0b2+.google.cloud.aiplatform.v1beta1.Annotation\x12!\n\x19has_truncated_annotations\x18\x03 \x01(\x08"\xcc\x01\n\x17ListSavedQueriesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x10\n\x08order_by\x18\x06 \x01(\t"w\n\x18ListSavedQueriesResponse\x12B\n\rsaved_queries\x18\x01 \x03(\x0b2+.google.cloud.aiplatform.v1beta1.SavedQuery\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"U\n\x17DeleteSavedQueryRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$aiplatform.googleapis.com/SavedQuery"\x89\x01\n\x18GetAnnotationSpecRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/AnnotationSpec\x12-\n\tread_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xcc\x01\n\x16ListAnnotationsRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/DataItem\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x10\n\x08order_by\x18\x06 \x01(\t"t\n\x17ListAnnotationsResponse\x12@\n\x0bannotations\x18\x01 \x03(\x0b2+.google.cloud.aiplatform.v1beta1.Annotation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x89\'\n\x0eDatasetService\x12\x85\x02\n\rCreateDataset\x125.google.cloud.aiplatform.v1beta1.CreateDatasetRequest\x1a\x1d.google.longrunning.Operation"\x9d\x01\xcaA)\n\x07Dataset\x12\x1eCreateDatasetOperationMetadata\xdaA\x0eparent,dataset\x82\xd3\xe4\x93\x02Z"1/v1beta1/{parent=projects/*/locations/*}/datasets:\x07datasetZ\x1c"\x11/v1beta1/datasets:\x07dataset\x12\xca\x01\n\nGetDataset\x122.google.cloud.aiplatform.v1beta1.GetDatasetRequest\x1a(.google.cloud.aiplatform.v1beta1.Dataset"^\xdaA\x04name\x82\xd3\xe4\x93\x02Q\x121/v1beta1/{name=projects/*/locations/*/datasets/*}Z\x1c\x12\x1a/v1beta1/{name=datasets/*}\x12\x82\x02\n\rUpdateDataset\x125.google.cloud.aiplatform.v1beta1.UpdateDatasetRequest\x1a(.google.cloud.aiplatform.v1beta1.Dataset"\x8f\x01\xdaA\x13dataset,update_mask\x82\xd3\xe4\x93\x02s29/v1beta1/{dataset.name=projects/*/locations/*/datasets/*}:\x07datasetZ-2"/v1beta1/{dataset.name=datasets/*}:\x07dataset\x12\xd4\x01\n\x0cListDatasets\x124.google.cloud.aiplatform.v1beta1.ListDatasetsRequest\x1a5.google.cloud.aiplatform.v1beta1.ListDatasetsResponse"W\xdaA\x06parent\x82\xd3\xe4\x93\x02H\x121/v1beta1/{parent=projects/*/locations/*}/datasetsZ\x13\x12\x11/v1beta1/datasets\x12\xf9\x01\n\rDeleteDataset\x125.google.cloud.aiplatform.v1beta1.DeleteDatasetRequest\x1a\x1d.google.longrunning.Operation"\x91\x01\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02Q*1/v1beta1/{name=projects/*/locations/*/datasets/*}Z\x1c*\x1a/v1beta1/{name=datasets/*}\x12\xef\x01\n\nImportData\x122.google.cloud.aiplatform.v1beta1.ImportDataRequest\x1a\x1d.google.longrunning.Operation"\x8d\x01\xcaA1\n\x12ImportDataResponse\x12\x1bImportDataOperationMetadata\xdaA\x13name,import_configs\x82\xd3\xe4\x93\x02="8/v1beta1/{name=projects/*/locations/*/datasets/*}:import:\x01*\x12\xee\x01\n\nExportData\x122.google.cloud.aiplatform.v1beta1.ExportDataRequest\x1a\x1d.google.longrunning.Operation"\x8c\x01\xcaA1\n\x12ExportDataResponse\x12\x1bExportDataOperationMetadata\xdaA\x12name,export_config\x82\xd3\xe4\x93\x02="8/v1beta1/{name=projects/*/locations/*/datasets/*}:export:\x01*\x12\xe7\x02\n\x14CreateDatasetVersion\x12<.google.cloud.aiplatform.v1beta1.CreateDatasetVersionRequest\x1a\x1d.google.longrunning.Operation"\xf1\x01\xcaA7\n\x0eDatasetVersion\x12%CreateDatasetVersionOperationMetadata\xdaA\x16parent,dataset_version\x82\xd3\xe4\x93\x02\x97\x01"C/v1beta1/{parent=projects/*/locations/*/datasets/*}/datasetVersions:\x0fdataset_versionZ?",/v1beta1/{parent=datasets/*}/datasetVersions:\x0fdataset_version\x12\xe4\x02\n\x14UpdateDatasetVersion\x12<.google.cloud.aiplatform.v1beta1.UpdateDatasetVersionRequest\x1a/.google.cloud.aiplatform.v1beta1.DatasetVersion"\xdc\x01\xdaA\x1bdataset_version,update_mask\x82\xd3\xe4\x93\x02\xb7\x012S/v1beta1/{dataset_version.name=projects/*/locations/*/datasets/*/datasetVersions/*}:\x0fdataset_versionZO2</v1beta1/{dataset_version.name=datasets/*/datasetVersions/*}:\x0fdataset_version\x12\xab\x02\n\x14DeleteDatasetVersion\x12<.google.cloud.aiplatform.v1beta1.DeleteDatasetVersionRequest\x1a\x1d.google.longrunning.Operation"\xb5\x01\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02u*C/v1beta1/{name=projects/*/locations/*/datasets/*/datasetVersions/*}Z.*,/v1beta1/{name=datasets/*/datasetVersions/*}\x12\x84\x02\n\x11GetDatasetVersion\x129.google.cloud.aiplatform.v1beta1.GetDatasetVersionRequest\x1a/.google.cloud.aiplatform.v1beta1.DatasetVersion"\x82\x01\xdaA\x04name\x82\xd3\xe4\x93\x02u\x12C/v1beta1/{name=projects/*/locations/*/datasets/*/datasetVersions/*}Z.\x12,/v1beta1/{name=datasets/*/datasetVersions/*}\x12\x97\x02\n\x13ListDatasetVersions\x12;.google.cloud.aiplatform.v1beta1.ListDatasetVersionsRequest\x1a<.google.cloud.aiplatform.v1beta1.ListDatasetVersionsResponse"\x84\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02u\x12C/v1beta1/{parent=projects/*/locations/*/datasets/*}/datasetVersionsZ.\x12,/v1beta1/{parent=datasets/*}/datasetVersions\x12\xc6\x02\n\x15RestoreDatasetVersion\x12=.google.cloud.aiplatform.v1beta1.RestoreDatasetVersionRequest\x1a\x1d.google.longrunning.Operation"\xce\x01\xcaA8\n\x0eDatasetVersion\x12&RestoreDatasetVersionOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x85\x01\x12K/v1beta1/{name=projects/*/locations/*/datasets/*/datasetVersions/*}:restoreZ6\x124/v1beta1/{name=datasets/*/datasetVersions/*}:restore\x12\xce\x01\n\rListDataItems\x125.google.cloud.aiplatform.v1beta1.ListDataItemsRequest\x1a6.google.cloud.aiplatform.v1beta1.ListDataItemsResponse"N\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1beta1/{parent=projects/*/locations/*/datasets/*}/dataItems\x12\xd2\x01\n\x0fSearchDataItems\x127.google.cloud.aiplatform.v1beta1.SearchDataItemsRequest\x1a8.google.cloud.aiplatform.v1beta1.SearchDataItemsResponse"L\x82\xd3\xe4\x93\x02F\x12D/v1beta1/{dataset=projects/*/locations/*/datasets/*}:searchDataItems\x12\xda\x01\n\x10ListSavedQueries\x128.google.cloud.aiplatform.v1beta1.ListSavedQueriesRequest\x1a9.google.cloud.aiplatform.v1beta1.ListSavedQueriesResponse"Q\xdaA\x06parent\x82\xd3\xe4\x93\x02B\x12@/v1beta1/{parent=projects/*/locations/*/datasets/*}/savedQueries\x12\xf0\x01\n\x10DeleteSavedQuery\x128.google.cloud.aiplatform.v1beta1.DeleteSavedQueryRequest\x1a\x1d.google.longrunning.Operation"\x82\x01\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02B*@/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*}\x12\xd3\x01\n\x11GetAnnotationSpec\x129.google.cloud.aiplatform.v1beta1.GetAnnotationSpecRequest\x1a/.google.cloud.aiplatform.v1beta1.AnnotationSpec"R\xdaA\x04name\x82\xd3\xe4\x93\x02E\x12C/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*}\x12\xe2\x01\n\x0fListAnnotations\x127.google.cloud.aiplatform.v1beta1.ListAnnotationsRequest\x1a8.google.cloud.aiplatform.v1beta1.ListAnnotationsResponse"\\\xdaA\x06parent\x82\xd3\xe4\x93\x02M\x12K/v1beta1/{parent=projects/*/locations/*/datasets/*/dataItems/*}/annotations\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xea\x01\n#com.google.cloud.aiplatform.v1beta1B\x13DatasetServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.dataset_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x13DatasetServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_CREATEDATASETREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDATASETREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEDATASETREQUEST'].fields_by_name['dataset']._loaded_options = None
    _globals['_CREATEDATASETREQUEST'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02'
    _globals['_GETDATASETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATASETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_UPDATEDATASETREQUEST'].fields_by_name['dataset']._loaded_options = None
    _globals['_UPDATEDATASETREQUEST'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDATASETREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEDATASETREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDATASETVERSIONREQUEST'].fields_by_name['dataset_version']._loaded_options = None
    _globals['_UPDATEDATASETVERSIONREQUEST'].fields_by_name['dataset_version']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDATASETVERSIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEDATASETVERSIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_LISTDATASETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATASETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_DELETEDATASETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDATASETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_IMPORTDATAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_IMPORTDATAREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_IMPORTDATAREQUEST'].fields_by_name['import_configs']._loaded_options = None
    _globals['_IMPORTDATAREQUEST'].fields_by_name['import_configs']._serialized_options = b'\xe0A\x02'
    _globals['_EXPORTDATAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_EXPORTDATAREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_EXPORTDATAREQUEST'].fields_by_name['export_config']._loaded_options = None
    _globals['_EXPORTDATAREQUEST'].fields_by_name['export_config']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDATASETVERSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDATASETVERSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_CREATEDATASETVERSIONREQUEST'].fields_by_name['dataset_version']._loaded_options = None
    _globals['_CREATEDATASETVERSIONREQUEST'].fields_by_name['dataset_version']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEDATASETVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDATASETVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/DatasetVersion'
    _globals['_GETDATASETVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATASETVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/DatasetVersion'
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['read_mask']._loaded_options = None
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['read_mask']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_RESTOREDATASETVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESTOREDATASETVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/DatasetVersion'
    _globals['_LISTDATAITEMSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATAITEMSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_SEARCHDATAITEMSREQUEST_ORDERBYANNOTATION'].fields_by_name['saved_query']._loaded_options = None
    _globals['_SEARCHDATAITEMSREQUEST_ORDERBYANNOTATION'].fields_by_name['saved_query']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHDATAITEMSREQUEST'].fields_by_name['dataset']._loaded_options = None
    _globals['_SEARCHDATAITEMSREQUEST'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_SEARCHDATAITEMSREQUEST'].fields_by_name['saved_query']._loaded_options = None
    _globals['_SEARCHDATAITEMSREQUEST'].fields_by_name['saved_query']._serialized_options = b'\x18\x01\xfaA&\n$aiplatform.googleapis.com/SavedQuery'
    _globals['_SEARCHDATAITEMSREQUEST'].fields_by_name['annotations_filter']._loaded_options = None
    _globals['_SEARCHDATAITEMSREQUEST'].fields_by_name['annotations_filter']._serialized_options = b'\x18\x01'
    _globals['_SEARCHDATAITEMSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_SEARCHDATAITEMSREQUEST'].fields_by_name['order_by']._serialized_options = b'\x18\x01'
    _globals['_LISTSAVEDQUERIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSAVEDQUERIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_DELETESAVEDQUERYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESAVEDQUERYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$aiplatform.googleapis.com/SavedQuery'
    _globals['_GETANNOTATIONSPECREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETANNOTATIONSPECREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/AnnotationSpec'
    _globals['_LISTANNOTATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTANNOTATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/DataItem'
    _globals['_DATASETSERVICE']._loaded_options = None
    _globals['_DATASETSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DATASETSERVICE'].methods_by_name['CreateDataset']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['CreateDataset']._serialized_options = b'\xcaA)\n\x07Dataset\x12\x1eCreateDatasetOperationMetadata\xdaA\x0eparent,dataset\x82\xd3\xe4\x93\x02Z"1/v1beta1/{parent=projects/*/locations/*}/datasets:\x07datasetZ\x1c"\x11/v1beta1/datasets:\x07dataset'
    _globals['_DATASETSERVICE'].methods_by_name['GetDataset']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['GetDataset']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02Q\x121/v1beta1/{name=projects/*/locations/*/datasets/*}Z\x1c\x12\x1a/v1beta1/{name=datasets/*}'
    _globals['_DATASETSERVICE'].methods_by_name['UpdateDataset']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['UpdateDataset']._serialized_options = b'\xdaA\x13dataset,update_mask\x82\xd3\xe4\x93\x02s29/v1beta1/{dataset.name=projects/*/locations/*/datasets/*}:\x07datasetZ-2"/v1beta1/{dataset.name=datasets/*}:\x07dataset'
    _globals['_DATASETSERVICE'].methods_by_name['ListDatasets']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['ListDatasets']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02H\x121/v1beta1/{parent=projects/*/locations/*}/datasetsZ\x13\x12\x11/v1beta1/datasets'
    _globals['_DATASETSERVICE'].methods_by_name['DeleteDataset']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['DeleteDataset']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02Q*1/v1beta1/{name=projects/*/locations/*/datasets/*}Z\x1c*\x1a/v1beta1/{name=datasets/*}'
    _globals['_DATASETSERVICE'].methods_by_name['ImportData']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['ImportData']._serialized_options = b'\xcaA1\n\x12ImportDataResponse\x12\x1bImportDataOperationMetadata\xdaA\x13name,import_configs\x82\xd3\xe4\x93\x02="8/v1beta1/{name=projects/*/locations/*/datasets/*}:import:\x01*'
    _globals['_DATASETSERVICE'].methods_by_name['ExportData']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['ExportData']._serialized_options = b'\xcaA1\n\x12ExportDataResponse\x12\x1bExportDataOperationMetadata\xdaA\x12name,export_config\x82\xd3\xe4\x93\x02="8/v1beta1/{name=projects/*/locations/*/datasets/*}:export:\x01*'
    _globals['_DATASETSERVICE'].methods_by_name['CreateDatasetVersion']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['CreateDatasetVersion']._serialized_options = b'\xcaA7\n\x0eDatasetVersion\x12%CreateDatasetVersionOperationMetadata\xdaA\x16parent,dataset_version\x82\xd3\xe4\x93\x02\x97\x01"C/v1beta1/{parent=projects/*/locations/*/datasets/*}/datasetVersions:\x0fdataset_versionZ?",/v1beta1/{parent=datasets/*}/datasetVersions:\x0fdataset_version'
    _globals['_DATASETSERVICE'].methods_by_name['UpdateDatasetVersion']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['UpdateDatasetVersion']._serialized_options = b'\xdaA\x1bdataset_version,update_mask\x82\xd3\xe4\x93\x02\xb7\x012S/v1beta1/{dataset_version.name=projects/*/locations/*/datasets/*/datasetVersions/*}:\x0fdataset_versionZO2</v1beta1/{dataset_version.name=datasets/*/datasetVersions/*}:\x0fdataset_version'
    _globals['_DATASETSERVICE'].methods_by_name['DeleteDatasetVersion']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['DeleteDatasetVersion']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02u*C/v1beta1/{name=projects/*/locations/*/datasets/*/datasetVersions/*}Z.*,/v1beta1/{name=datasets/*/datasetVersions/*}'
    _globals['_DATASETSERVICE'].methods_by_name['GetDatasetVersion']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['GetDatasetVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02u\x12C/v1beta1/{name=projects/*/locations/*/datasets/*/datasetVersions/*}Z.\x12,/v1beta1/{name=datasets/*/datasetVersions/*}'
    _globals['_DATASETSERVICE'].methods_by_name['ListDatasetVersions']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['ListDatasetVersions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02u\x12C/v1beta1/{parent=projects/*/locations/*/datasets/*}/datasetVersionsZ.\x12,/v1beta1/{parent=datasets/*}/datasetVersions'
    _globals['_DATASETSERVICE'].methods_by_name['RestoreDatasetVersion']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['RestoreDatasetVersion']._serialized_options = b'\xcaA8\n\x0eDatasetVersion\x12&RestoreDatasetVersionOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x85\x01\x12K/v1beta1/{name=projects/*/locations/*/datasets/*/datasetVersions/*}:restoreZ6\x124/v1beta1/{name=datasets/*/datasetVersions/*}:restore'
    _globals['_DATASETSERVICE'].methods_by_name['ListDataItems']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['ListDataItems']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1beta1/{parent=projects/*/locations/*/datasets/*}/dataItems'
    _globals['_DATASETSERVICE'].methods_by_name['SearchDataItems']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['SearchDataItems']._serialized_options = b'\x82\xd3\xe4\x93\x02F\x12D/v1beta1/{dataset=projects/*/locations/*/datasets/*}:searchDataItems'
    _globals['_DATASETSERVICE'].methods_by_name['ListSavedQueries']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['ListSavedQueries']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02B\x12@/v1beta1/{parent=projects/*/locations/*/datasets/*}/savedQueries'
    _globals['_DATASETSERVICE'].methods_by_name['DeleteSavedQuery']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['DeleteSavedQuery']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02B*@/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*}'
    _globals['_DATASETSERVICE'].methods_by_name['GetAnnotationSpec']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['GetAnnotationSpec']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02E\x12C/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*}'
    _globals['_DATASETSERVICE'].methods_by_name['ListAnnotations']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['ListAnnotations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02M\x12K/v1beta1/{parent=projects/*/locations/*/datasets/*/dataItems/*}/annotations'
    _globals['_CREATEDATASETREQUEST']._serialized_start = 662
    _globals['_CREATEDATASETREQUEST']._serialized_end = 807
    _globals['_CREATEDATASETOPERATIONMETADATA']._serialized_start = 809
    _globals['_CREATEDATASETOPERATIONMETADATA']._serialized_end = 926
    _globals['_GETDATASETREQUEST']._serialized_start = 928
    _globals['_GETDATASETREQUEST']._serialized_end = 1051
    _globals['_UPDATEDATASETREQUEST']._serialized_start = 1054
    _globals['_UPDATEDATASETREQUEST']._serialized_end = 1194
    _globals['_UPDATEDATASETVERSIONREQUEST']._serialized_start = 1197
    _globals['_UPDATEDATASETVERSIONREQUEST']._serialized_end = 1359
    _globals['_LISTDATASETSREQUEST']._serialized_start = 1362
    _globals['_LISTDATASETSREQUEST']._serialized_end = 1562
    _globals['_LISTDATASETSRESPONSE']._serialized_start = 1564
    _globals['_LISTDATASETSRESPONSE']._serialized_end = 1671
    _globals['_DELETEDATASETREQUEST']._serialized_start = 1673
    _globals['_DELETEDATASETREQUEST']._serialized_end = 1752
    _globals['_IMPORTDATAREQUEST']._serialized_start = 1755
    _globals['_IMPORTDATAREQUEST']._serialized_end = 1911
    _globals['_IMPORTDATARESPONSE']._serialized_start = 1913
    _globals['_IMPORTDATARESPONSE']._serialized_end = 1933
    _globals['_IMPORTDATAOPERATIONMETADATA']._serialized_start = 1935
    _globals['_IMPORTDATAOPERATIONMETADATA']._serialized_end = 2049
    _globals['_EXPORTDATAREQUEST']._serialized_start = 2052
    _globals['_EXPORTDATAREQUEST']._serialized_end = 2207
    _globals['_EXPORTDATARESPONSE']._serialized_start = 2209
    _globals['_EXPORTDATARESPONSE']._serialized_end = 2253
    _globals['_EXPORTDATAOPERATIONMETADATA']._serialized_start = 2256
    _globals['_EXPORTDATAOPERATIONMETADATA']._serialized_end = 2400
    _globals['_CREATEDATASETVERSIONREQUEST']._serialized_start = 2403
    _globals['_CREATEDATASETVERSIONREQUEST']._serialized_end = 2570
    _globals['_CREATEDATASETVERSIONOPERATIONMETADATA']._serialized_start = 2572
    _globals['_CREATEDATASETVERSIONOPERATIONMETADATA']._serialized_end = 2696
    _globals['_DELETEDATASETVERSIONREQUEST']._serialized_start = 2698
    _globals['_DELETEDATASETVERSIONREQUEST']._serialized_end = 2791
    _globals['_GETDATASETVERSIONREQUEST']._serialized_start = 2794
    _globals['_GETDATASETVERSIONREQUEST']._serialized_end = 2931
    _globals['_LISTDATASETVERSIONSREQUEST']._serialized_start = 2934
    _globals['_LISTDATASETVERSIONSREQUEST']._serialized_end = 3166
    _globals['_LISTDATASETVERSIONSRESPONSE']._serialized_start = 3169
    _globals['_LISTDATASETVERSIONSRESPONSE']._serialized_end = 3298
    _globals['_RESTOREDATASETVERSIONREQUEST']._serialized_start = 3300
    _globals['_RESTOREDATASETVERSIONREQUEST']._serialized_end = 3394
    _globals['_RESTOREDATASETVERSIONOPERATIONMETADATA']._serialized_start = 3396
    _globals['_RESTOREDATASETVERSIONOPERATIONMETADATA']._serialized_end = 3521
    _globals['_LISTDATAITEMSREQUEST']._serialized_start = 3524
    _globals['_LISTDATAITEMSREQUEST']._serialized_end = 3725
    _globals['_LISTDATAITEMSRESPONSE']._serialized_start = 3727
    _globals['_LISTDATAITEMSRESPONSE']._serialized_end = 3838
    _globals['_SEARCHDATAITEMSREQUEST']._serialized_start = 3841
    _globals['_SEARCHDATAITEMSREQUEST']._serialized_end = 4450
    _globals['_SEARCHDATAITEMSREQUEST_ORDERBYANNOTATION']._serialized_start = 4378
    _globals['_SEARCHDATAITEMSREQUEST_ORDERBYANNOTATION']._serialized_end = 4441
    _globals['_SEARCHDATAITEMSRESPONSE']._serialized_start = 4452
    _globals['_SEARCHDATAITEMSRESPONSE']._serialized_end = 4574
    _globals['_DATAITEMVIEW']._serialized_start = 4577
    _globals['_DATAITEMVIEW']._serialized_end = 4754
    _globals['_LISTSAVEDQUERIESREQUEST']._serialized_start = 4757
    _globals['_LISTSAVEDQUERIESREQUEST']._serialized_end = 4961
    _globals['_LISTSAVEDQUERIESRESPONSE']._serialized_start = 4963
    _globals['_LISTSAVEDQUERIESRESPONSE']._serialized_end = 5082
    _globals['_DELETESAVEDQUERYREQUEST']._serialized_start = 5084
    _globals['_DELETESAVEDQUERYREQUEST']._serialized_end = 5169
    _globals['_GETANNOTATIONSPECREQUEST']._serialized_start = 5172
    _globals['_GETANNOTATIONSPECREQUEST']._serialized_end = 5309
    _globals['_LISTANNOTATIONSREQUEST']._serialized_start = 5312
    _globals['_LISTANNOTATIONSREQUEST']._serialized_end = 5516
    _globals['_LISTANNOTATIONSRESPONSE']._serialized_start = 5518
    _globals['_LISTANNOTATIONSRESPONSE']._serialized_end = 5634
    _globals['_DATASETSERVICE']._serialized_start = 5637
    _globals['_DATASETSERVICE']._serialized_end = 10638