"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/migratable_resource.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/aiplatform/v1/migratable_resource.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd3\t\n\x12MigratableResource\x12k\n\x17ml_engine_model_version\x18\x01 \x01(\x0b2C.google.cloud.aiplatform.v1.MigratableResource.MlEngineModelVersionB\x03\xe0A\x03H\x00\x12W\n\x0cautoml_model\x18\x02 \x01(\x0b2:.google.cloud.aiplatform.v1.MigratableResource.AutomlModelB\x03\xe0A\x03H\x00\x12[\n\x0eautoml_dataset\x18\x03 \x01(\x0b2<.google.cloud.aiplatform.v1.MigratableResource.AutomlDatasetB\x03\xe0A\x03H\x00\x12h\n\x15data_labeling_dataset\x18\x04 \x01(\x0b2B.google.cloud.aiplatform.v1.MigratableResource.DataLabelingDatasetB\x03\xe0A\x03H\x00\x12:\n\x11last_migrate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x129\n\x10last_update_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1aY\n\x14MlEngineModelVersion\x12\x10\n\x08endpoint\x18\x01 \x01(\t\x12/\n\x07version\x18\x02 \x01(\tB\x1e\xfaA\x1b\n\x19ml.googleapis.com/Version\x1aZ\n\x0bAutomlModel\x12/\n\x05model\x18\x01 \x01(\tB \xfaA\x1d\n\x1bautoml.googleapis.com/Model\x12\x1a\n\x12model_display_name\x18\x03 \x01(\t\x1ab\n\rAutomlDataset\x123\n\x07dataset\x18\x01 \x01(\tB"\xfaA\x1f\n\x1dautoml.googleapis.com/Dataset\x12\x1c\n\x14dataset_display_name\x18\x04 \x01(\t\x1a\x91\x03\n\x13DataLabelingDataset\x129\n\x07dataset\x18\x01 \x01(\tB(\xfaA%\n#datalabeling.googleapis.com/Dataset\x12\x1c\n\x14dataset_display_name\x18\x04 \x01(\t\x12\x89\x01\n data_labeling_annotated_datasets\x18\x03 \x03(\x0b2_.google.cloud.aiplatform.v1.MigratableResource.DataLabelingDataset.DataLabelingAnnotatedDataset\x1a\x94\x01\n\x1cDataLabelingAnnotatedDataset\x12L\n\x11annotated_dataset\x18\x01 \x01(\tB1\xfaA.\n,datalabeling.googleapis.com/AnnotatedDataset\x12&\n\x1eannotated_dataset_display_name\x18\x03 \x01(\tB\n\n\x08resourceB\xac\x05\n\x1ecom.google.cloud.aiplatform.v1B\x17MigratableResourceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1\xeaAQ\n\x19ml.googleapis.com/Version\x124projects/{project}/models/{model}/versions/{version}\xeaAU\n\x1bautoml.googleapis.com/Model\x126projects/{project}/locations/{location}/models/{model}\xeaA[\n\x1dautoml.googleapis.com/Dataset\x12:projects/{project}/locations/{location}/datasets/{dataset}\xeaAL\n#datalabeling.googleapis.com/Dataset\x12%projects/{project}/datasets/{dataset}\xeaA{\n,datalabeling.googleapis.com/AnnotatedDataset\x12Kprojects/{project}/datasets/{dataset}/annotatedDatasets/{annotated_dataset}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.migratable_resource_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x17MigratableResourceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1\xeaAQ\n\x19ml.googleapis.com/Version\x124projects/{project}/models/{model}/versions/{version}\xeaAU\n\x1bautoml.googleapis.com/Model\x126projects/{project}/locations/{location}/models/{model}\xeaA[\n\x1dautoml.googleapis.com/Dataset\x12:projects/{project}/locations/{location}/datasets/{dataset}\xeaAL\n#datalabeling.googleapis.com/Dataset\x12%projects/{project}/datasets/{dataset}\xeaA{\n,datalabeling.googleapis.com/AnnotatedDataset\x12Kprojects/{project}/datasets/{dataset}/annotatedDatasets/{annotated_dataset}'
    _globals['_MIGRATABLERESOURCE_MLENGINEMODELVERSION'].fields_by_name['version']._loaded_options = None
    _globals['_MIGRATABLERESOURCE_MLENGINEMODELVERSION'].fields_by_name['version']._serialized_options = b'\xfaA\x1b\n\x19ml.googleapis.com/Version'
    _globals['_MIGRATABLERESOURCE_AUTOMLMODEL'].fields_by_name['model']._loaded_options = None
    _globals['_MIGRATABLERESOURCE_AUTOMLMODEL'].fields_by_name['model']._serialized_options = b'\xfaA\x1d\n\x1bautoml.googleapis.com/Model'
    _globals['_MIGRATABLERESOURCE_AUTOMLDATASET'].fields_by_name['dataset']._loaded_options = None
    _globals['_MIGRATABLERESOURCE_AUTOMLDATASET'].fields_by_name['dataset']._serialized_options = b'\xfaA\x1f\n\x1dautoml.googleapis.com/Dataset'
    _globals['_MIGRATABLERESOURCE_DATALABELINGDATASET_DATALABELINGANNOTATEDDATASET'].fields_by_name['annotated_dataset']._loaded_options = None
    _globals['_MIGRATABLERESOURCE_DATALABELINGDATASET_DATALABELINGANNOTATEDDATASET'].fields_by_name['annotated_dataset']._serialized_options = b'\xfaA.\n,datalabeling.googleapis.com/AnnotatedDataset'
    _globals['_MIGRATABLERESOURCE_DATALABELINGDATASET'].fields_by_name['dataset']._loaded_options = None
    _globals['_MIGRATABLERESOURCE_DATALABELINGDATASET'].fields_by_name['dataset']._serialized_options = b'\xfaA%\n#datalabeling.googleapis.com/Dataset'
    _globals['_MIGRATABLERESOURCE'].fields_by_name['ml_engine_model_version']._loaded_options = None
    _globals['_MIGRATABLERESOURCE'].fields_by_name['ml_engine_model_version']._serialized_options = b'\xe0A\x03'
    _globals['_MIGRATABLERESOURCE'].fields_by_name['automl_model']._loaded_options = None
    _globals['_MIGRATABLERESOURCE'].fields_by_name['automl_model']._serialized_options = b'\xe0A\x03'
    _globals['_MIGRATABLERESOURCE'].fields_by_name['automl_dataset']._loaded_options = None
    _globals['_MIGRATABLERESOURCE'].fields_by_name['automl_dataset']._serialized_options = b'\xe0A\x03'
    _globals['_MIGRATABLERESOURCE'].fields_by_name['data_labeling_dataset']._loaded_options = None
    _globals['_MIGRATABLERESOURCE'].fields_by_name['data_labeling_dataset']._serialized_options = b'\xe0A\x03'
    _globals['_MIGRATABLERESOURCE'].fields_by_name['last_migrate_time']._loaded_options = None
    _globals['_MIGRATABLERESOURCE'].fields_by_name['last_migrate_time']._serialized_options = b'\xe0A\x03'
    _globals['_MIGRATABLERESOURCE'].fields_by_name['last_update_time']._loaded_options = None
    _globals['_MIGRATABLERESOURCE'].fields_by_name['last_update_time']._serialized_options = b'\xe0A\x03'
    _globals['_MIGRATABLERESOURCE']._serialized_start = 178
    _globals['_MIGRATABLERESOURCE']._serialized_end = 1413
    _globals['_MIGRATABLERESOURCE_MLENGINEMODELVERSION']._serialized_start = 716
    _globals['_MIGRATABLERESOURCE_MLENGINEMODELVERSION']._serialized_end = 805
    _globals['_MIGRATABLERESOURCE_AUTOMLMODEL']._serialized_start = 807
    _globals['_MIGRATABLERESOURCE_AUTOMLMODEL']._serialized_end = 897
    _globals['_MIGRATABLERESOURCE_AUTOMLDATASET']._serialized_start = 899
    _globals['_MIGRATABLERESOURCE_AUTOMLDATASET']._serialized_end = 997
    _globals['_MIGRATABLERESOURCE_DATALABELINGDATASET']._serialized_start = 1000
    _globals['_MIGRATABLERESOURCE_DATALABELINGDATASET']._serialized_end = 1401
    _globals['_MIGRATABLERESOURCE_DATALABELINGDATASET_DATALABELINGANNOTATEDDATASET']._serialized_start = 1253
    _globals['_MIGRATABLERESOURCE_DATALABELINGDATASET_DATALABELINGANNOTATEDDATASET']._serialized_end = 1401