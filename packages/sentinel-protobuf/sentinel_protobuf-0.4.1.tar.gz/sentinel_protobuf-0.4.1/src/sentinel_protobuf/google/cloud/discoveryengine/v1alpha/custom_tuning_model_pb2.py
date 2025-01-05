"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/discoveryengine/v1alpha/custom_tuning_model.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/discoveryengine/v1alpha/custom_tuning_model.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc0\x07\n\x11CustomTuningModel\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0discoveryengine.googleapis.com/CustomTuningModel\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x15\n\rmodel_version\x18\x03 \x01(\x03\x12W\n\x0bmodel_state\x18\x04 \x01(\x0e2B.google.cloud.discoveryengine.v1alpha.CustomTuningModel.ModelState\x123\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x02\x18\x01\x127\n\x13training_start_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12U\n\x07metrics\x18\x07 \x03(\x0b2D.google.cloud.discoveryengine.v1alpha.CustomTuningModel.MetricsEntry\x1a.\n\x0cMetricsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x028\x01"\xc0\x01\n\nModelState\x12\x1b\n\x17MODEL_STATE_UNSPECIFIED\x10\x00\x12\x13\n\x0fTRAINING_PAUSED\x10\x01\x12\x0c\n\x08TRAINING\x10\x02\x12\x15\n\x11TRAINING_COMPLETE\x10\x03\x12\x15\n\x11READY_FOR_SERVING\x10\x04\x12\x13\n\x0fTRAINING_FAILED\x10\x05\x12\x12\n\x0eNO_IMPROVEMENT\x10\x06\x12\x1b\n\x17INPUT_VALIDATION_FAILED\x10\x07:\xa4\x02\xeaA\xa0\x02\n0discoveryengine.googleapis.com/CustomTuningModel\x12hprojects/{project}/locations/{location}/dataStores/{data_store}/customTuningModels/{custom_tuning_model}\x12\x81\x01projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/customTuningModels/{custom_tuning_model}B\xa2\x02\n(com.google.cloud.discoveryengine.v1alphaB\x16CustomTuningModelProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.custom_tuning_model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x16CustomTuningModelProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
    _globals['_CUSTOMTUNINGMODEL_METRICSENTRY']._loaded_options = None
    _globals['_CUSTOMTUNINGMODEL_METRICSENTRY']._serialized_options = b'8\x01'
    _globals['_CUSTOMTUNINGMODEL'].fields_by_name['name']._loaded_options = None
    _globals['_CUSTOMTUNINGMODEL'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0discoveryengine.googleapis.com/CustomTuningModel'
    _globals['_CUSTOMTUNINGMODEL'].fields_by_name['create_time']._loaded_options = None
    _globals['_CUSTOMTUNINGMODEL'].fields_by_name['create_time']._serialized_options = b'\x18\x01'
    _globals['_CUSTOMTUNINGMODEL']._loaded_options = None
    _globals['_CUSTOMTUNINGMODEL']._serialized_options = b'\xeaA\xa0\x02\n0discoveryengine.googleapis.com/CustomTuningModel\x12hprojects/{project}/locations/{location}/dataStores/{data_store}/customTuningModels/{custom_tuning_model}\x12\x81\x01projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/customTuningModels/{custom_tuning_model}'
    _globals['_CUSTOMTUNINGMODEL']._serialized_start = 198
    _globals['_CUSTOMTUNINGMODEL']._serialized_end = 1158
    _globals['_CUSTOMTUNINGMODEL_METRICSENTRY']._serialized_start = 622
    _globals['_CUSTOMTUNINGMODEL_METRICSENTRY']._serialized_end = 668
    _globals['_CUSTOMTUNINGMODEL_MODELSTATE']._serialized_start = 671
    _globals['_CUSTOMTUNINGMODEL_MODELSTATE']._serialized_end = 863