"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/feature_online_store.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1beta1 import service_networking_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_service__networking__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/aiplatform/v1beta1/feature_online_store.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/aiplatform/v1beta1/encryption_spec.proto\x1a8google/cloud/aiplatform/v1beta1/service_networking.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd3\x0c\n\x12FeatureOnlineStore\x12P\n\x08bigtable\x18\x08 \x01(\x0b2<.google.cloud.aiplatform.v1beta1.FeatureOnlineStore.BigtableH\x00\x12R\n\toptimized\x18\x0c \x01(\x0b2=.google.cloud.aiplatform.v1beta1.FeatureOnlineStore.OptimizedH\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x05 \x01(\tB\x03\xe0A\x01\x12T\n\x06labels\x18\x06 \x03(\x0b2?.google.cloud.aiplatform.v1beta1.FeatureOnlineStore.LabelsEntryB\x03\xe0A\x01\x12M\n\x05state\x18\x07 \x01(\x0e29.google.cloud.aiplatform.v1beta1.FeatureOnlineStore.StateB\x03\xe0A\x03\x12u\n\x1adedicated_serving_endpoint\x18\n \x01(\x0b2L.google.cloud.aiplatform.v1beta1.FeatureOnlineStore.DedicatedServingEndpointB\x03\xe0A\x01\x12l\n\x14embedding_management\x18\x0b \x01(\x0b2G.google.cloud.aiplatform.v1beta1.FeatureOnlineStore.EmbeddingManagementB\x05\x18\x01\xe0A\x01\x12M\n\x0fencryption_spec\x18\r \x01(\x0b2/.google.cloud.aiplatform.v1beta1.EncryptionSpecB\x03\xe0A\x01\x12\x1a\n\rsatisfies_pzs\x18\x0f \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x10 \x01(\x08B\x03\xe0A\x03\x1a\xdd\x01\n\x08Bigtable\x12c\n\x0cauto_scaling\x18\x01 \x01(\x0b2H.google.cloud.aiplatform.v1beta1.FeatureOnlineStore.Bigtable.AutoScalingB\x03\xe0A\x02\x1al\n\x0bAutoScaling\x12\x1b\n\x0emin_node_count\x18\x01 \x01(\x05B\x03\xe0A\x02\x12\x1b\n\x0emax_node_count\x18\x02 \x01(\x05B\x03\xe0A\x02\x12#\n\x16cpu_utilization_target\x18\x03 \x01(\x05B\x03\xe0A\x01\x1a\x0b\n\tOptimized\x1a\xd0\x01\n\x18DedicatedServingEndpoint\x12(\n\x1bpublic_endpoint_domain_name\x18\x02 \x01(\tB\x03\xe0A\x03\x12i\n\x1eprivate_service_connect_config\x18\x03 \x01(\x0b2<.google.cloud.aiplatform.v1beta1.PrivateServiceConnectConfigB\x03\xe0A\x01\x12\x1f\n\x12service_attachment\x18\x04 \x01(\tB\x03\xe0A\x03\x1a2\n\x13EmbeddingManagement\x12\x17\n\x07enabled\x18\x01 \x01(\x08B\x06\xe0A\x01\xe0A\x05:\x02\x18\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"8\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06STABLE\x10\x01\x12\x0c\n\x08UPDATING\x10\x02:\x86\x01\xeaA\x82\x01\n,aiplatform.googleapis.com/FeatureOnlineStore\x12Rprojects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}B\x0e\n\x0cstorage_typeB\xee\x01\n#com.google.cloud.aiplatform.v1beta1B\x17FeatureOnlineStoreProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.feature_online_store_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x17FeatureOnlineStoreProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_FEATUREONLINESTORE_BIGTABLE_AUTOSCALING'].fields_by_name['min_node_count']._loaded_options = None
    _globals['_FEATUREONLINESTORE_BIGTABLE_AUTOSCALING'].fields_by_name['min_node_count']._serialized_options = b'\xe0A\x02'
    _globals['_FEATUREONLINESTORE_BIGTABLE_AUTOSCALING'].fields_by_name['max_node_count']._loaded_options = None
    _globals['_FEATUREONLINESTORE_BIGTABLE_AUTOSCALING'].fields_by_name['max_node_count']._serialized_options = b'\xe0A\x02'
    _globals['_FEATUREONLINESTORE_BIGTABLE_AUTOSCALING'].fields_by_name['cpu_utilization_target']._loaded_options = None
    _globals['_FEATUREONLINESTORE_BIGTABLE_AUTOSCALING'].fields_by_name['cpu_utilization_target']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREONLINESTORE_BIGTABLE'].fields_by_name['auto_scaling']._loaded_options = None
    _globals['_FEATUREONLINESTORE_BIGTABLE'].fields_by_name['auto_scaling']._serialized_options = b'\xe0A\x02'
    _globals['_FEATUREONLINESTORE_DEDICATEDSERVINGENDPOINT'].fields_by_name['public_endpoint_domain_name']._loaded_options = None
    _globals['_FEATUREONLINESTORE_DEDICATEDSERVINGENDPOINT'].fields_by_name['public_endpoint_domain_name']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREONLINESTORE_DEDICATEDSERVINGENDPOINT'].fields_by_name['private_service_connect_config']._loaded_options = None
    _globals['_FEATUREONLINESTORE_DEDICATEDSERVINGENDPOINT'].fields_by_name['private_service_connect_config']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREONLINESTORE_DEDICATEDSERVINGENDPOINT'].fields_by_name['service_attachment']._loaded_options = None
    _globals['_FEATUREONLINESTORE_DEDICATEDSERVINGENDPOINT'].fields_by_name['service_attachment']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREONLINESTORE_EMBEDDINGMANAGEMENT'].fields_by_name['enabled']._loaded_options = None
    _globals['_FEATUREONLINESTORE_EMBEDDINGMANAGEMENT'].fields_by_name['enabled']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_FEATUREONLINESTORE_EMBEDDINGMANAGEMENT']._loaded_options = None
    _globals['_FEATUREONLINESTORE_EMBEDDINGMANAGEMENT']._serialized_options = b'\x18\x01'
    _globals['_FEATUREONLINESTORE_LABELSENTRY']._loaded_options = None
    _globals['_FEATUREONLINESTORE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_FEATUREONLINESTORE'].fields_by_name['name']._loaded_options = None
    _globals['_FEATUREONLINESTORE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_FEATUREONLINESTORE'].fields_by_name['create_time']._loaded_options = None
    _globals['_FEATUREONLINESTORE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREONLINESTORE'].fields_by_name['update_time']._loaded_options = None
    _globals['_FEATUREONLINESTORE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREONLINESTORE'].fields_by_name['etag']._loaded_options = None
    _globals['_FEATUREONLINESTORE'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREONLINESTORE'].fields_by_name['labels']._loaded_options = None
    _globals['_FEATUREONLINESTORE'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREONLINESTORE'].fields_by_name['state']._loaded_options = None
    _globals['_FEATUREONLINESTORE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREONLINESTORE'].fields_by_name['dedicated_serving_endpoint']._loaded_options = None
    _globals['_FEATUREONLINESTORE'].fields_by_name['dedicated_serving_endpoint']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREONLINESTORE'].fields_by_name['embedding_management']._loaded_options = None
    _globals['_FEATUREONLINESTORE'].fields_by_name['embedding_management']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_FEATUREONLINESTORE'].fields_by_name['encryption_spec']._loaded_options = None
    _globals['_FEATUREONLINESTORE'].fields_by_name['encryption_spec']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREONLINESTORE'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_FEATUREONLINESTORE'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREONLINESTORE'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_FEATUREONLINESTORE'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREONLINESTORE']._loaded_options = None
    _globals['_FEATUREONLINESTORE']._serialized_options = b'\xeaA\x82\x01\n,aiplatform.googleapis.com/FeatureOnlineStore\x12Rprojects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}'
    _globals['_FEATUREONLINESTORE']._serialized_start = 302
    _globals['_FEATUREONLINESTORE']._serialized_end = 1921
    _globals['_FEATUREONLINESTORE_BIGTABLE']._serialized_start = 1166
    _globals['_FEATUREONLINESTORE_BIGTABLE']._serialized_end = 1387
    _globals['_FEATUREONLINESTORE_BIGTABLE_AUTOSCALING']._serialized_start = 1279
    _globals['_FEATUREONLINESTORE_BIGTABLE_AUTOSCALING']._serialized_end = 1387
    _globals['_FEATUREONLINESTORE_OPTIMIZED']._serialized_start = 1389
    _globals['_FEATUREONLINESTORE_OPTIMIZED']._serialized_end = 1400
    _globals['_FEATUREONLINESTORE_DEDICATEDSERVINGENDPOINT']._serialized_start = 1403
    _globals['_FEATUREONLINESTORE_DEDICATEDSERVINGENDPOINT']._serialized_end = 1611
    _globals['_FEATUREONLINESTORE_EMBEDDINGMANAGEMENT']._serialized_start = 1613
    _globals['_FEATUREONLINESTORE_EMBEDDINGMANAGEMENT']._serialized_end = 1663
    _globals['_FEATUREONLINESTORE_LABELSENTRY']._serialized_start = 1665
    _globals['_FEATUREONLINESTORE_LABELSENTRY']._serialized_end = 1710
    _globals['_FEATUREONLINESTORE_STATE']._serialized_start = 1712
    _globals['_FEATUREONLINESTORE_STATE']._serialized_end = 1768