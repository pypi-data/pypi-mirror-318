"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/migration_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import migratable_resource_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_migratable__resource__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/aiplatform/v1beta1/migration_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a9google/cloud/aiplatform/v1beta1/migratable_resource.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a#google/longrunning/operations.proto\x1a\x17google/rpc/status.proto"\x94\x01\n SearchMigratableResourcesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"\x8f\x01\n!SearchMigratableResourcesResponse\x12Q\n\x14migratable_resources\x18\x01 \x03(\x0b23.google.cloud.aiplatform.v1beta1.MigratableResource\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xba\x01\n\x1cBatchMigrateResourcesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12_\n\x19migrate_resource_requests\x18\x02 \x03(\x0b27.google.cloud.aiplatform.v1beta1.MigrateResourceRequestB\x03\xe0A\x02"\xfc\n\n\x16MigrateResourceRequest\x12\x8b\x01\n&migrate_ml_engine_model_version_config\x18\x01 \x01(\x0b2Y.google.cloud.aiplatform.v1beta1.MigrateResourceRequest.MigrateMlEngineModelVersionConfigH\x00\x12w\n\x1bmigrate_automl_model_config\x18\x02 \x01(\x0b2P.google.cloud.aiplatform.v1beta1.MigrateResourceRequest.MigrateAutomlModelConfigH\x00\x12{\n\x1dmigrate_automl_dataset_config\x18\x03 \x01(\x0b2R.google.cloud.aiplatform.v1beta1.MigrateResourceRequest.MigrateAutomlDatasetConfigH\x00\x12\x88\x01\n$migrate_data_labeling_dataset_config\x18\x04 \x01(\x0b2X.google.cloud.aiplatform.v1beta1.MigrateResourceRequest.MigrateDataLabelingDatasetConfigH\x00\x1a\x95\x01\n!MigrateMlEngineModelVersionConfig\x12\x15\n\x08endpoint\x18\x01 \x01(\tB\x03\xe0A\x02\x128\n\rmodel_version\x18\x02 \x01(\tB!\xe0A\x02\xfaA\x1b\n\x19ml.googleapis.com/Version\x12\x1f\n\x12model_display_name\x18\x03 \x01(\tB\x03\xe0A\x02\x1ao\n\x18MigrateAutomlModelConfig\x122\n\x05model\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model\x12\x1f\n\x12model_display_name\x18\x02 \x01(\tB\x03\xe0A\x01\x1aw\n\x1aMigrateAutomlDatasetConfig\x126\n\x07dataset\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dautoml.googleapis.com/Dataset\x12!\n\x14dataset_display_name\x18\x02 \x01(\tB\x03\xe0A\x02\x1a\xc5\x03\n MigrateDataLabelingDatasetConfig\x12<\n\x07dataset\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#datalabeling.googleapis.com/Dataset\x12!\n\x14dataset_display_name\x18\x02 \x01(\tB\x03\xe0A\x01\x12\xc1\x01\n/migrate_data_labeling_annotated_dataset_configs\x18\x03 \x03(\x0b2\x82\x01.google.cloud.aiplatform.v1beta1.MigrateResourceRequest.MigrateDataLabelingDatasetConfig.MigrateDataLabelingAnnotatedDatasetConfigB\x03\xe0A\x01\x1a|\n)MigrateDataLabelingAnnotatedDatasetConfig\x12O\n\x11annotated_dataset\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,datalabeling.googleapis.com/AnnotatedDatasetB\t\n\x07request"}\n\x1dBatchMigrateResourcesResponse\x12\\\n\x1amigrate_resource_responses\x18\x01 \x03(\x0b28.google.cloud.aiplatform.v1beta1.MigrateResourceResponse"\xf2\x01\n\x17MigrateResourceResponse\x129\n\x07dataset\x18\x01 \x01(\tB&\xfaA#\n!aiplatform.googleapis.com/DatasetH\x00\x125\n\x05model\x18\x02 \x01(\tB$\xfaA!\n\x1faiplatform.googleapis.com/ModelH\x00\x12P\n\x13migratable_resource\x18\x03 \x01(\x0b23.google.cloud.aiplatform.v1beta1.MigratableResourceB\x13\n\x11migrated_resource"\xea\x03\n&BatchMigrateResourcesOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata\x12n\n\x0fpartial_results\x18\x02 \x03(\x0b2U.google.cloud.aiplatform.v1beta1.BatchMigrateResourcesOperationMetadata.PartialResult\x1a\xfa\x01\n\rPartialResult\x12#\n\x05error\x18\x02 \x01(\x0b2\x12.google.rpc.StatusH\x00\x125\n\x05model\x18\x03 \x01(\tB$\xfaA!\n\x1faiplatform.googleapis.com/ModelH\x00\x129\n\x07dataset\x18\x04 \x01(\tB&\xfaA#\n!aiplatform.googleapis.com/DatasetH\x00\x12H\n\x07request\x18\x01 \x01(\x0b27.google.cloud.aiplatform.v1beta1.MigrateResourceRequestB\x08\n\x06result2\x9b\x05\n\x10MigrationService\x12\xfb\x01\n\x19SearchMigratableResources\x12A.google.cloud.aiplatform.v1beta1.SearchMigratableResourcesRequest\x1aB.google.cloud.aiplatform.v1beta1.SearchMigratableResourcesResponse"W\xdaA\x06parent\x82\xd3\xe4\x93\x02H"C/v1beta1/{parent=projects/*/locations/*}/migratableResources:search:\x01*\x12\xb9\x02\n\x15BatchMigrateResources\x12=.google.cloud.aiplatform.v1beta1.BatchMigrateResourcesRequest\x1a\x1d.google.longrunning.Operation"\xc1\x01\xcaAG\n\x1dBatchMigrateResourcesResponse\x12&BatchMigrateResourcesOperationMetadata\xdaA parent,migrate_resource_requests\x82\xd3\xe4\x93\x02N"I/v1beta1/{parent=projects/*/locations/*}/migratableResources:batchMigrate:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xec\x01\n#com.google.cloud.aiplatform.v1beta1B\x15MigrationServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.migration_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x15MigrationServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_SEARCHMIGRATABLERESOURCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_SEARCHMIGRATABLERESOURCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_BATCHMIGRATERESOURCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHMIGRATERESOURCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_BATCHMIGRATERESOURCESREQUEST'].fields_by_name['migrate_resource_requests']._loaded_options = None
    _globals['_BATCHMIGRATERESOURCESREQUEST'].fields_by_name['migrate_resource_requests']._serialized_options = b'\xe0A\x02'
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEMLENGINEMODELVERSIONCONFIG'].fields_by_name['endpoint']._loaded_options = None
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEMLENGINEMODELVERSIONCONFIG'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02'
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEMLENGINEMODELVERSIONCONFIG'].fields_by_name['model_version']._loaded_options = None
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEMLENGINEMODELVERSIONCONFIG'].fields_by_name['model_version']._serialized_options = b'\xe0A\x02\xfaA\x1b\n\x19ml.googleapis.com/Version'
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEMLENGINEMODELVERSIONCONFIG'].fields_by_name['model_display_name']._loaded_options = None
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEMLENGINEMODELVERSIONCONFIG'].fields_by_name['model_display_name']._serialized_options = b'\xe0A\x02'
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEAUTOMLMODELCONFIG'].fields_by_name['model']._loaded_options = None
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEAUTOMLMODELCONFIG'].fields_by_name['model']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model'
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEAUTOMLMODELCONFIG'].fields_by_name['model_display_name']._loaded_options = None
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEAUTOMLMODELCONFIG'].fields_by_name['model_display_name']._serialized_options = b'\xe0A\x01'
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEAUTOMLDATASETCONFIG'].fields_by_name['dataset']._loaded_options = None
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEAUTOMLDATASETCONFIG'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dautoml.googleapis.com/Dataset'
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEAUTOMLDATASETCONFIG'].fields_by_name['dataset_display_name']._loaded_options = None
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEAUTOMLDATASETCONFIG'].fields_by_name['dataset_display_name']._serialized_options = b'\xe0A\x02'
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEDATALABELINGDATASETCONFIG_MIGRATEDATALABELINGANNOTATEDDATASETCONFIG'].fields_by_name['annotated_dataset']._loaded_options = None
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEDATALABELINGDATASETCONFIG_MIGRATEDATALABELINGANNOTATEDDATASETCONFIG'].fields_by_name['annotated_dataset']._serialized_options = b'\xe0A\x02\xfaA.\n,datalabeling.googleapis.com/AnnotatedDataset'
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEDATALABELINGDATASETCONFIG'].fields_by_name['dataset']._loaded_options = None
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEDATALABELINGDATASETCONFIG'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02\xfaA%\n#datalabeling.googleapis.com/Dataset'
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEDATALABELINGDATASETCONFIG'].fields_by_name['dataset_display_name']._loaded_options = None
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEDATALABELINGDATASETCONFIG'].fields_by_name['dataset_display_name']._serialized_options = b'\xe0A\x01'
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEDATALABELINGDATASETCONFIG'].fields_by_name['migrate_data_labeling_annotated_dataset_configs']._loaded_options = None
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEDATALABELINGDATASETCONFIG'].fields_by_name['migrate_data_labeling_annotated_dataset_configs']._serialized_options = b'\xe0A\x01'
    _globals['_MIGRATERESOURCERESPONSE'].fields_by_name['dataset']._loaded_options = None
    _globals['_MIGRATERESOURCERESPONSE'].fields_by_name['dataset']._serialized_options = b'\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_MIGRATERESOURCERESPONSE'].fields_by_name['model']._loaded_options = None
    _globals['_MIGRATERESOURCERESPONSE'].fields_by_name['model']._serialized_options = b'\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_BATCHMIGRATERESOURCESOPERATIONMETADATA_PARTIALRESULT'].fields_by_name['model']._loaded_options = None
    _globals['_BATCHMIGRATERESOURCESOPERATIONMETADATA_PARTIALRESULT'].fields_by_name['model']._serialized_options = b'\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_BATCHMIGRATERESOURCESOPERATIONMETADATA_PARTIALRESULT'].fields_by_name['dataset']._loaded_options = None
    _globals['_BATCHMIGRATERESOURCESOPERATIONMETADATA_PARTIALRESULT'].fields_by_name['dataset']._serialized_options = b'\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_MIGRATIONSERVICE']._loaded_options = None
    _globals['_MIGRATIONSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_MIGRATIONSERVICE'].methods_by_name['SearchMigratableResources']._loaded_options = None
    _globals['_MIGRATIONSERVICE'].methods_by_name['SearchMigratableResources']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02H"C/v1beta1/{parent=projects/*/locations/*}/migratableResources:search:\x01*'
    _globals['_MIGRATIONSERVICE'].methods_by_name['BatchMigrateResources']._loaded_options = None
    _globals['_MIGRATIONSERVICE'].methods_by_name['BatchMigrateResources']._serialized_options = b'\xcaAG\n\x1dBatchMigrateResourcesResponse\x12&BatchMigrateResourcesOperationMetadata\xdaA parent,migrate_resource_requests\x82\xd3\xe4\x93\x02N"I/v1beta1/{parent=projects/*/locations/*}/migratableResources:batchMigrate:\x01*'
    _globals['_SEARCHMIGRATABLERESOURCESREQUEST']._serialized_start = 378
    _globals['_SEARCHMIGRATABLERESOURCESREQUEST']._serialized_end = 526
    _globals['_SEARCHMIGRATABLERESOURCESRESPONSE']._serialized_start = 529
    _globals['_SEARCHMIGRATABLERESOURCESRESPONSE']._serialized_end = 672
    _globals['_BATCHMIGRATERESOURCESREQUEST']._serialized_start = 675
    _globals['_BATCHMIGRATERESOURCESREQUEST']._serialized_end = 861
    _globals['_MIGRATERESOURCEREQUEST']._serialized_start = 864
    _globals['_MIGRATERESOURCEREQUEST']._serialized_end = 2268
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEMLENGINEMODELVERSIONCONFIG']._serialized_start = 1418
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEMLENGINEMODELVERSIONCONFIG']._serialized_end = 1567
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEAUTOMLMODELCONFIG']._serialized_start = 1569
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEAUTOMLMODELCONFIG']._serialized_end = 1680
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEAUTOMLDATASETCONFIG']._serialized_start = 1682
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEAUTOMLDATASETCONFIG']._serialized_end = 1801
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEDATALABELINGDATASETCONFIG']._serialized_start = 1804
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEDATALABELINGDATASETCONFIG']._serialized_end = 2257
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEDATALABELINGDATASETCONFIG_MIGRATEDATALABELINGANNOTATEDDATASETCONFIG']._serialized_start = 2133
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEDATALABELINGDATASETCONFIG_MIGRATEDATALABELINGANNOTATEDDATASETCONFIG']._serialized_end = 2257
    _globals['_BATCHMIGRATERESOURCESRESPONSE']._serialized_start = 2270
    _globals['_BATCHMIGRATERESOURCESRESPONSE']._serialized_end = 2395
    _globals['_MIGRATERESOURCERESPONSE']._serialized_start = 2398
    _globals['_MIGRATERESOURCERESPONSE']._serialized_end = 2640
    _globals['_BATCHMIGRATERESOURCESOPERATIONMETADATA']._serialized_start = 2643
    _globals['_BATCHMIGRATERESOURCESOPERATIONMETADATA']._serialized_end = 3133
    _globals['_BATCHMIGRATERESOURCESOPERATIONMETADATA_PARTIALRESULT']._serialized_start = 2883
    _globals['_BATCHMIGRATERESOURCESOPERATIONMETADATA_PARTIALRESULT']._serialized_end = 3133
    _globals['_MIGRATIONSERVICE']._serialized_start = 3136
    _globals['_MIGRATIONSERVICE']._serialized_end = 3803