"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/featurestore_online_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import feature_selector_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_feature__selector__pb2
from .....google.cloud.aiplatform.v1 import types_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_types__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/aiplatform/v1/featurestore_online_service.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/aiplatform/v1/feature_selector.proto\x1a&google/cloud/aiplatform/v1/types.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xac\x01\n\x19WriteFeatureValuesRequest\x12A\n\x0bentity_type\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$aiplatform.googleapis.com/EntityType\x12L\n\x08payloads\x18\x02 \x03(\x0b25.google.cloud.aiplatform.v1.WriteFeatureValuesPayloadB\x03\xe0A\x02"\xfa\x01\n\x19WriteFeatureValuesPayload\x12\x16\n\tentity_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12e\n\x0efeature_values\x18\x02 \x03(\x0b2H.google.cloud.aiplatform.v1.WriteFeatureValuesPayload.FeatureValuesEntryB\x03\xe0A\x02\x1a^\n\x12FeatureValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x127\n\x05value\x18\x02 \x01(\x0b2(.google.cloud.aiplatform.v1.FeatureValue:\x028\x01"\x1c\n\x1aWriteFeatureValuesResponse"\xc1\x01\n\x18ReadFeatureValuesRequest\x12A\n\x0bentity_type\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$aiplatform.googleapis.com/EntityType\x12\x16\n\tentity_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12J\n\x10feature_selector\x18\x03 \x01(\x0b2+.google.cloud.aiplatform.v1.FeatureSelectorB\x03\xe0A\x02"\x95\x05\n\x19ReadFeatureValuesResponse\x12L\n\x06header\x18\x01 \x01(\x0b2<.google.cloud.aiplatform.v1.ReadFeatureValuesResponse.Header\x12U\n\x0bentity_view\x18\x02 \x01(\x0b2@.google.cloud.aiplatform.v1.ReadFeatureValuesResponse.EntityView\x1a\x1f\n\x11FeatureDescriptor\x12\n\n\x02id\x18\x01 \x01(\t\x1a\xae\x01\n\x06Header\x12>\n\x0bentity_type\x18\x01 \x01(\tB)\xfaA&\n$aiplatform.googleapis.com/EntityType\x12d\n\x13feature_descriptors\x18\x02 \x03(\x0b2G.google.cloud.aiplatform.v1.ReadFeatureValuesResponse.FeatureDescriptor\x1a\x80\x02\n\nEntityView\x12\x11\n\tentity_id\x18\x01 \x01(\t\x12S\n\x04data\x18\x02 \x03(\x0b2E.google.cloud.aiplatform.v1.ReadFeatureValuesResponse.EntityView.Data\x1a\x89\x01\n\x04Data\x129\n\x05value\x18\x01 \x01(\x0b2(.google.cloud.aiplatform.v1.FeatureValueH\x00\x12>\n\x06values\x18\x02 \x01(\x0b2,.google.cloud.aiplatform.v1.FeatureValueListH\x00B\x06\n\x04data"\xcb\x01\n!StreamingReadFeatureValuesRequest\x12A\n\x0bentity_type\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$aiplatform.googleapis.com/EntityType\x12\x17\n\nentity_ids\x18\x02 \x03(\tB\x03\xe0A\x02\x12J\n\x10feature_selector\x18\x03 \x01(\x0b2+.google.cloud.aiplatform.v1.FeatureSelectorB\x03\xe0A\x02"\xe6\x04\n\x0cFeatureValue\x12\x14\n\nbool_value\x18\x01 \x01(\x08H\x00\x12\x16\n\x0cdouble_value\x18\x02 \x01(\x01H\x00\x12\x15\n\x0bint64_value\x18\x05 \x01(\x03H\x00\x12\x16\n\x0cstring_value\x18\x06 \x01(\tH\x00\x12A\n\x10bool_array_value\x18\x07 \x01(\x0b2%.google.cloud.aiplatform.v1.BoolArrayH\x00\x12E\n\x12double_array_value\x18\x08 \x01(\x0b2\'.google.cloud.aiplatform.v1.DoubleArrayH\x00\x12C\n\x11int64_array_value\x18\x0b \x01(\x0b2&.google.cloud.aiplatform.v1.Int64ArrayH\x00\x12E\n\x12string_array_value\x18\x0c \x01(\x0b2\'.google.cloud.aiplatform.v1.StringArrayH\x00\x12\x15\n\x0bbytes_value\x18\r \x01(\x0cH\x00\x12?\n\x0cstruct_value\x18\x0f \x01(\x0b2\'.google.cloud.aiplatform.v1.StructValueH\x00\x12C\n\x08metadata\x18\x0e \x01(\x0b21.google.cloud.aiplatform.v1.FeatureValue.Metadata\x1a=\n\x08Metadata\x121\n\rgenerate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x07\n\x05value"K\n\x0bStructValue\x12<\n\x06values\x18\x01 \x03(\x0b2,.google.cloud.aiplatform.v1.StructFieldValue"Y\n\x10StructFieldValue\x12\x0c\n\x04name\x18\x01 \x01(\t\x127\n\x05value\x18\x02 \x01(\x0b2(.google.cloud.aiplatform.v1.FeatureValue"L\n\x10FeatureValueList\x128\n\x06values\x18\x01 \x03(\x0b2(.google.cloud.aiplatform.v1.FeatureValue2\xfd\x06\n FeaturestoreOnlineServingService\x12\xf3\x01\n\x11ReadFeatureValues\x124.google.cloud.aiplatform.v1.ReadFeatureValuesRequest\x1a5.google.cloud.aiplatform.v1.ReadFeatureValuesResponse"q\xdaA\x0bentity_type\x82\xd3\xe4\x93\x02]"X/v1/{entity_type=projects/*/locations/*/featurestores/*/entityTypes/*}:readFeatureValues:\x01*\x12\x90\x02\n\x1aStreamingReadFeatureValues\x12=.google.cloud.aiplatform.v1.StreamingReadFeatureValuesRequest\x1a5.google.cloud.aiplatform.v1.ReadFeatureValuesResponse"z\xdaA\x0bentity_type\x82\xd3\xe4\x93\x02f"a/v1/{entity_type=projects/*/locations/*/featurestores/*/entityTypes/*}:streamingReadFeatureValues:\x01*0\x01\x12\x80\x02\n\x12WriteFeatureValues\x125.google.cloud.aiplatform.v1.WriteFeatureValuesRequest\x1a6.google.cloud.aiplatform.v1.WriteFeatureValuesResponse"{\xdaA\x14entity_type,payloads\x82\xd3\xe4\x93\x02^"Y/v1/{entity_type=projects/*/locations/*/featurestores/*/entityTypes/*}:writeFeatureValues:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xdc\x01\n\x1ecom.google.cloud.aiplatform.v1B\x1eFeaturestoreOnlineServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.featurestore_online_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x1eFeaturestoreOnlineServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_WRITEFEATUREVALUESREQUEST'].fields_by_name['entity_type']._loaded_options = None
    _globals['_WRITEFEATUREVALUESREQUEST'].fields_by_name['entity_type']._serialized_options = b'\xe0A\x02\xfaA&\n$aiplatform.googleapis.com/EntityType'
    _globals['_WRITEFEATUREVALUESREQUEST'].fields_by_name['payloads']._loaded_options = None
    _globals['_WRITEFEATUREVALUESREQUEST'].fields_by_name['payloads']._serialized_options = b'\xe0A\x02'
    _globals['_WRITEFEATUREVALUESPAYLOAD_FEATUREVALUESENTRY']._loaded_options = None
    _globals['_WRITEFEATUREVALUESPAYLOAD_FEATUREVALUESENTRY']._serialized_options = b'8\x01'
    _globals['_WRITEFEATUREVALUESPAYLOAD'].fields_by_name['entity_id']._loaded_options = None
    _globals['_WRITEFEATUREVALUESPAYLOAD'].fields_by_name['entity_id']._serialized_options = b'\xe0A\x02'
    _globals['_WRITEFEATUREVALUESPAYLOAD'].fields_by_name['feature_values']._loaded_options = None
    _globals['_WRITEFEATUREVALUESPAYLOAD'].fields_by_name['feature_values']._serialized_options = b'\xe0A\x02'
    _globals['_READFEATUREVALUESREQUEST'].fields_by_name['entity_type']._loaded_options = None
    _globals['_READFEATUREVALUESREQUEST'].fields_by_name['entity_type']._serialized_options = b'\xe0A\x02\xfaA&\n$aiplatform.googleapis.com/EntityType'
    _globals['_READFEATUREVALUESREQUEST'].fields_by_name['entity_id']._loaded_options = None
    _globals['_READFEATUREVALUESREQUEST'].fields_by_name['entity_id']._serialized_options = b'\xe0A\x02'
    _globals['_READFEATUREVALUESREQUEST'].fields_by_name['feature_selector']._loaded_options = None
    _globals['_READFEATUREVALUESREQUEST'].fields_by_name['feature_selector']._serialized_options = b'\xe0A\x02'
    _globals['_READFEATUREVALUESRESPONSE_HEADER'].fields_by_name['entity_type']._loaded_options = None
    _globals['_READFEATUREVALUESRESPONSE_HEADER'].fields_by_name['entity_type']._serialized_options = b'\xfaA&\n$aiplatform.googleapis.com/EntityType'
    _globals['_STREAMINGREADFEATUREVALUESREQUEST'].fields_by_name['entity_type']._loaded_options = None
    _globals['_STREAMINGREADFEATUREVALUESREQUEST'].fields_by_name['entity_type']._serialized_options = b'\xe0A\x02\xfaA&\n$aiplatform.googleapis.com/EntityType'
    _globals['_STREAMINGREADFEATUREVALUESREQUEST'].fields_by_name['entity_ids']._loaded_options = None
    _globals['_STREAMINGREADFEATUREVALUESREQUEST'].fields_by_name['entity_ids']._serialized_options = b'\xe0A\x02'
    _globals['_STREAMINGREADFEATUREVALUESREQUEST'].fields_by_name['feature_selector']._loaded_options = None
    _globals['_STREAMINGREADFEATUREVALUESREQUEST'].fields_by_name['feature_selector']._serialized_options = b'\xe0A\x02'
    _globals['_FEATURESTOREONLINESERVINGSERVICE']._loaded_options = None
    _globals['_FEATURESTOREONLINESERVINGSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_FEATURESTOREONLINESERVINGSERVICE'].methods_by_name['ReadFeatureValues']._loaded_options = None
    _globals['_FEATURESTOREONLINESERVINGSERVICE'].methods_by_name['ReadFeatureValues']._serialized_options = b'\xdaA\x0bentity_type\x82\xd3\xe4\x93\x02]"X/v1/{entity_type=projects/*/locations/*/featurestores/*/entityTypes/*}:readFeatureValues:\x01*'
    _globals['_FEATURESTOREONLINESERVINGSERVICE'].methods_by_name['StreamingReadFeatureValues']._loaded_options = None
    _globals['_FEATURESTOREONLINESERVINGSERVICE'].methods_by_name['StreamingReadFeatureValues']._serialized_options = b'\xdaA\x0bentity_type\x82\xd3\xe4\x93\x02f"a/v1/{entity_type=projects/*/locations/*/featurestores/*/entityTypes/*}:streamingReadFeatureValues:\x01*'
    _globals['_FEATURESTOREONLINESERVINGSERVICE'].methods_by_name['WriteFeatureValues']._loaded_options = None
    _globals['_FEATURESTOREONLINESERVINGSERVICE'].methods_by_name['WriteFeatureValues']._serialized_options = b'\xdaA\x14entity_type,payloads\x82\xd3\xe4\x93\x02^"Y/v1/{entity_type=projects/*/locations/*/featurestores/*/entityTypes/*}:writeFeatureValues:\x01*'
    _globals['_WRITEFEATUREVALUESREQUEST']._serialized_start = 332
    _globals['_WRITEFEATUREVALUESREQUEST']._serialized_end = 504
    _globals['_WRITEFEATUREVALUESPAYLOAD']._serialized_start = 507
    _globals['_WRITEFEATUREVALUESPAYLOAD']._serialized_end = 757
    _globals['_WRITEFEATUREVALUESPAYLOAD_FEATUREVALUESENTRY']._serialized_start = 663
    _globals['_WRITEFEATUREVALUESPAYLOAD_FEATUREVALUESENTRY']._serialized_end = 757
    _globals['_WRITEFEATUREVALUESRESPONSE']._serialized_start = 759
    _globals['_WRITEFEATUREVALUESRESPONSE']._serialized_end = 787
    _globals['_READFEATUREVALUESREQUEST']._serialized_start = 790
    _globals['_READFEATUREVALUESREQUEST']._serialized_end = 983
    _globals['_READFEATUREVALUESRESPONSE']._serialized_start = 986
    _globals['_READFEATUREVALUESRESPONSE']._serialized_end = 1647
    _globals['_READFEATUREVALUESRESPONSE_FEATUREDESCRIPTOR']._serialized_start = 1180
    _globals['_READFEATUREVALUESRESPONSE_FEATUREDESCRIPTOR']._serialized_end = 1211
    _globals['_READFEATUREVALUESRESPONSE_HEADER']._serialized_start = 1214
    _globals['_READFEATUREVALUESRESPONSE_HEADER']._serialized_end = 1388
    _globals['_READFEATUREVALUESRESPONSE_ENTITYVIEW']._serialized_start = 1391
    _globals['_READFEATUREVALUESRESPONSE_ENTITYVIEW']._serialized_end = 1647
    _globals['_READFEATUREVALUESRESPONSE_ENTITYVIEW_DATA']._serialized_start = 1510
    _globals['_READFEATUREVALUESRESPONSE_ENTITYVIEW_DATA']._serialized_end = 1647
    _globals['_STREAMINGREADFEATUREVALUESREQUEST']._serialized_start = 1650
    _globals['_STREAMINGREADFEATUREVALUESREQUEST']._serialized_end = 1853
    _globals['_FEATUREVALUE']._serialized_start = 1856
    _globals['_FEATUREVALUE']._serialized_end = 2470
    _globals['_FEATUREVALUE_METADATA']._serialized_start = 2400
    _globals['_FEATUREVALUE_METADATA']._serialized_end = 2461
    _globals['_STRUCTVALUE']._serialized_start = 2472
    _globals['_STRUCTVALUE']._serialized_end = 2547
    _globals['_STRUCTFIELDVALUE']._serialized_start = 2549
    _globals['_STRUCTFIELDVALUE']._serialized_end = 2638
    _globals['_FEATUREVALUELIST']._serialized_start = 2640
    _globals['_FEATUREVALUELIST']._serialized_end = 2716
    _globals['_FEATURESTOREONLINESERVINGSERVICE']._serialized_start = 2719
    _globals['_FEATURESTOREONLINESERVINGSERVICE']._serialized_end = 3612