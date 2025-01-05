"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/migration_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import migratable_resource_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_migratable__resource__pb2
from .....google.cloud.aiplatform.v1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_operation__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/aiplatform/v1/migration_service.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a4google/cloud/aiplatform/v1/migratable_resource.proto\x1a*google/cloud/aiplatform/v1/operation.proto\x1a#google/longrunning/operations.proto\x1a\x17google/rpc/status.proto"\x94\x01\n SearchMigratableResourcesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"\x8a\x01\n!SearchMigratableResourcesResponse\x12L\n\x14migratable_resources\x18\x01 \x03(\x0b2..google.cloud.aiplatform.v1.MigratableResource\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xb5\x01\n\x1cBatchMigrateResourcesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12Z\n\x19migrate_resource_requests\x18\x02 \x03(\x0b22.google.cloud.aiplatform.v1.MigrateResourceRequestB\x03\xe0A\x02"\xe2\n\n\x16MigrateResourceRequest\x12\x86\x01\n&migrate_ml_engine_model_version_config\x18\x01 \x01(\x0b2T.google.cloud.aiplatform.v1.MigrateResourceRequest.MigrateMlEngineModelVersionConfigH\x00\x12r\n\x1bmigrate_automl_model_config\x18\x02 \x01(\x0b2K.google.cloud.aiplatform.v1.MigrateResourceRequest.MigrateAutomlModelConfigH\x00\x12v\n\x1dmigrate_automl_dataset_config\x18\x03 \x01(\x0b2M.google.cloud.aiplatform.v1.MigrateResourceRequest.MigrateAutomlDatasetConfigH\x00\x12\x83\x01\n$migrate_data_labeling_dataset_config\x18\x04 \x01(\x0b2S.google.cloud.aiplatform.v1.MigrateResourceRequest.MigrateDataLabelingDatasetConfigH\x00\x1a\x95\x01\n!MigrateMlEngineModelVersionConfig\x12\x15\n\x08endpoint\x18\x01 \x01(\tB\x03\xe0A\x02\x128\n\rmodel_version\x18\x02 \x01(\tB!\xe0A\x02\xfaA\x1b\n\x19ml.googleapis.com/Version\x12\x1f\n\x12model_display_name\x18\x03 \x01(\tB\x03\xe0A\x02\x1ao\n\x18MigrateAutomlModelConfig\x122\n\x05model\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model\x12\x1f\n\x12model_display_name\x18\x02 \x01(\tB\x03\xe0A\x01\x1aw\n\x1aMigrateAutomlDatasetConfig\x126\n\x07dataset\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dautoml.googleapis.com/Dataset\x12!\n\x14dataset_display_name\x18\x02 \x01(\tB\x03\xe0A\x02\x1a\xbf\x03\n MigrateDataLabelingDatasetConfig\x12<\n\x07dataset\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#datalabeling.googleapis.com/Dataset\x12!\n\x14dataset_display_name\x18\x02 \x01(\tB\x03\xe0A\x01\x12\xbb\x01\n/migrate_data_labeling_annotated_dataset_configs\x18\x03 \x03(\x0b2}.google.cloud.aiplatform.v1.MigrateResourceRequest.MigrateDataLabelingDatasetConfig.MigrateDataLabelingAnnotatedDatasetConfigB\x03\xe0A\x01\x1a|\n)MigrateDataLabelingAnnotatedDatasetConfig\x12O\n\x11annotated_dataset\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,datalabeling.googleapis.com/AnnotatedDatasetB\t\n\x07request"x\n\x1dBatchMigrateResourcesResponse\x12W\n\x1amigrate_resource_responses\x18\x01 \x03(\x0b23.google.cloud.aiplatform.v1.MigrateResourceResponse"\xed\x01\n\x17MigrateResourceResponse\x129\n\x07dataset\x18\x01 \x01(\tB&\xfaA#\n!aiplatform.googleapis.com/DatasetH\x00\x125\n\x05model\x18\x02 \x01(\tB$\xfaA!\n\x1faiplatform.googleapis.com/ModelH\x00\x12K\n\x13migratable_resource\x18\x03 \x01(\x0b2..google.cloud.aiplatform.v1.MigratableResourceB\x13\n\x11migrated_resource"\xdb\x03\n&BatchMigrateResourcesOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata\x12i\n\x0fpartial_results\x18\x02 \x03(\x0b2P.google.cloud.aiplatform.v1.BatchMigrateResourcesOperationMetadata.PartialResult\x1a\xf5\x01\n\rPartialResult\x12#\n\x05error\x18\x02 \x01(\x0b2\x12.google.rpc.StatusH\x00\x125\n\x05model\x18\x03 \x01(\tB$\xfaA!\n\x1faiplatform.googleapis.com/ModelH\x00\x129\n\x07dataset\x18\x04 \x01(\tB&\xfaA#\n!aiplatform.googleapis.com/DatasetH\x00\x12C\n\x07request\x18\x01 \x01(\x0b22.google.cloud.aiplatform.v1.MigrateResourceRequestB\x08\n\x06result2\x82\x05\n\x10MigrationService\x12\xec\x01\n\x19SearchMigratableResources\x12<.google.cloud.aiplatform.v1.SearchMigratableResourcesRequest\x1a=.google.cloud.aiplatform.v1.SearchMigratableResourcesResponse"R\xdaA\x06parent\x82\xd3\xe4\x93\x02C">/v1/{parent=projects/*/locations/*}/migratableResources:search:\x01*\x12\xaf\x02\n\x15BatchMigrateResources\x128.google.cloud.aiplatform.v1.BatchMigrateResourcesRequest\x1a\x1d.google.longrunning.Operation"\xbc\x01\xcaAG\n\x1dBatchMigrateResourcesResponse\x12&BatchMigrateResourcesOperationMetadata\xdaA parent,migrate_resource_requests\x82\xd3\xe4\x93\x02I"D/v1/{parent=projects/*/locations/*}/migratableResources:batchMigrate:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd3\x01\n\x1ecom.google.cloud.aiplatform.v1B\x15MigrationServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.migration_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x15MigrationServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
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
    _globals['_MIGRATIONSERVICE'].methods_by_name['SearchMigratableResources']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02C">/v1/{parent=projects/*/locations/*}/migratableResources:search:\x01*'
    _globals['_MIGRATIONSERVICE'].methods_by_name['BatchMigrateResources']._loaded_options = None
    _globals['_MIGRATIONSERVICE'].methods_by_name['BatchMigrateResources']._serialized_options = b'\xcaAG\n\x1dBatchMigrateResourcesResponse\x12&BatchMigrateResourcesOperationMetadata\xdaA parent,migrate_resource_requests\x82\xd3\xe4\x93\x02I"D/v1/{parent=projects/*/locations/*}/migratableResources:batchMigrate:\x01*'
    _globals['_SEARCHMIGRATABLERESOURCESREQUEST']._serialized_start = 358
    _globals['_SEARCHMIGRATABLERESOURCESREQUEST']._serialized_end = 506
    _globals['_SEARCHMIGRATABLERESOURCESRESPONSE']._serialized_start = 509
    _globals['_SEARCHMIGRATABLERESOURCESRESPONSE']._serialized_end = 647
    _globals['_BATCHMIGRATERESOURCESREQUEST']._serialized_start = 650
    _globals['_BATCHMIGRATERESOURCESREQUEST']._serialized_end = 831
    _globals['_MIGRATERESOURCEREQUEST']._serialized_start = 834
    _globals['_MIGRATERESOURCEREQUEST']._serialized_end = 2212
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEMLENGINEMODELVERSIONCONFIG']._serialized_start = 1368
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEMLENGINEMODELVERSIONCONFIG']._serialized_end = 1517
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEAUTOMLMODELCONFIG']._serialized_start = 1519
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEAUTOMLMODELCONFIG']._serialized_end = 1630
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEAUTOMLDATASETCONFIG']._serialized_start = 1632
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEAUTOMLDATASETCONFIG']._serialized_end = 1751
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEDATALABELINGDATASETCONFIG']._serialized_start = 1754
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEDATALABELINGDATASETCONFIG']._serialized_end = 2201
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEDATALABELINGDATASETCONFIG_MIGRATEDATALABELINGANNOTATEDDATASETCONFIG']._serialized_start = 2077
    _globals['_MIGRATERESOURCEREQUEST_MIGRATEDATALABELINGDATASETCONFIG_MIGRATEDATALABELINGANNOTATEDDATASETCONFIG']._serialized_end = 2201
    _globals['_BATCHMIGRATERESOURCESRESPONSE']._serialized_start = 2214
    _globals['_BATCHMIGRATERESOURCESRESPONSE']._serialized_end = 2334
    _globals['_MIGRATERESOURCERESPONSE']._serialized_start = 2337
    _globals['_MIGRATERESOURCERESPONSE']._serialized_end = 2574
    _globals['_BATCHMIGRATERESOURCESOPERATIONMETADATA']._serialized_start = 2577
    _globals['_BATCHMIGRATERESOURCESOPERATIONMETADATA']._serialized_end = 3052
    _globals['_BATCHMIGRATERESOURCESOPERATIONMETADATA_PARTIALRESULT']._serialized_start = 2807
    _globals['_BATCHMIGRATERESOURCESOPERATIONMETADATA_PARTIALRESULT']._serialized_end = 3052
    _globals['_MIGRATIONSERVICE']._serialized_start = 3055
    _globals['_MIGRATIONSERVICE']._serialized_end = 3697