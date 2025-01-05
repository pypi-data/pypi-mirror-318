"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/featurestore_online_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import feature_selector_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_feature__selector__pb2
from .....google.cloud.aiplatform.v1beta1 import types_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_types__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/cloud/aiplatform/v1beta1/featurestore_online_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a6google/cloud/aiplatform/v1beta1/feature_selector.proto\x1a+google/cloud/aiplatform/v1beta1/types.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb1\x01\n\x19WriteFeatureValuesRequest\x12A\n\x0bentity_type\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$aiplatform.googleapis.com/EntityType\x12Q\n\x08payloads\x18\x02 \x03(\x0b2:.google.cloud.aiplatform.v1beta1.WriteFeatureValuesPayloadB\x03\xe0A\x02"\x84\x02\n\x19WriteFeatureValuesPayload\x12\x16\n\tentity_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12j\n\x0efeature_values\x18\x02 \x03(\x0b2M.google.cloud.aiplatform.v1beta1.WriteFeatureValuesPayload.FeatureValuesEntryB\x03\xe0A\x02\x1ac\n\x12FeatureValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12<\n\x05value\x18\x02 \x01(\x0b2-.google.cloud.aiplatform.v1beta1.FeatureValue:\x028\x01"\x1c\n\x1aWriteFeatureValuesResponse"\xc6\x01\n\x18ReadFeatureValuesRequest\x12A\n\x0bentity_type\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$aiplatform.googleapis.com/EntityType\x12\x16\n\tentity_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12O\n\x10feature_selector\x18\x03 \x01(\x0b20.google.cloud.aiplatform.v1beta1.FeatureSelectorB\x03\xe0A\x02"\xb3\x05\n\x19ReadFeatureValuesResponse\x12Q\n\x06header\x18\x01 \x01(\x0b2A.google.cloud.aiplatform.v1beta1.ReadFeatureValuesResponse.Header\x12Z\n\x0bentity_view\x18\x02 \x01(\x0b2E.google.cloud.aiplatform.v1beta1.ReadFeatureValuesResponse.EntityView\x1a\x1f\n\x11FeatureDescriptor\x12\n\n\x02id\x18\x01 \x01(\t\x1a\xb3\x01\n\x06Header\x12>\n\x0bentity_type\x18\x01 \x01(\tB)\xfaA&\n$aiplatform.googleapis.com/EntityType\x12i\n\x13feature_descriptors\x18\x02 \x03(\x0b2L.google.cloud.aiplatform.v1beta1.ReadFeatureValuesResponse.FeatureDescriptor\x1a\x8f\x02\n\nEntityView\x12\x11\n\tentity_id\x18\x01 \x01(\t\x12X\n\x04data\x18\x02 \x03(\x0b2J.google.cloud.aiplatform.v1beta1.ReadFeatureValuesResponse.EntityView.Data\x1a\x93\x01\n\x04Data\x12>\n\x05value\x18\x01 \x01(\x0b2-.google.cloud.aiplatform.v1beta1.FeatureValueH\x00\x12C\n\x06values\x18\x02 \x01(\x0b21.google.cloud.aiplatform.v1beta1.FeatureValueListH\x00B\x06\n\x04data"\xd0\x01\n!StreamingReadFeatureValuesRequest\x12A\n\x0bentity_type\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$aiplatform.googleapis.com/EntityType\x12\x17\n\nentity_ids\x18\x02 \x03(\tB\x03\xe0A\x02\x12O\n\x10feature_selector\x18\x03 \x01(\x0b20.google.cloud.aiplatform.v1beta1.FeatureSelectorB\x03\xe0A\x02"\x84\x05\n\x0cFeatureValue\x12\x14\n\nbool_value\x18\x01 \x01(\x08H\x00\x12\x16\n\x0cdouble_value\x18\x02 \x01(\x01H\x00\x12\x15\n\x0bint64_value\x18\x05 \x01(\x03H\x00\x12\x16\n\x0cstring_value\x18\x06 \x01(\tH\x00\x12F\n\x10bool_array_value\x18\x07 \x01(\x0b2*.google.cloud.aiplatform.v1beta1.BoolArrayH\x00\x12J\n\x12double_array_value\x18\x08 \x01(\x0b2,.google.cloud.aiplatform.v1beta1.DoubleArrayH\x00\x12H\n\x11int64_array_value\x18\x0b \x01(\x0b2+.google.cloud.aiplatform.v1beta1.Int64ArrayH\x00\x12J\n\x12string_array_value\x18\x0c \x01(\x0b2,.google.cloud.aiplatform.v1beta1.StringArrayH\x00\x12\x15\n\x0bbytes_value\x18\r \x01(\x0cH\x00\x12D\n\x0cstruct_value\x18\x0f \x01(\x0b2,.google.cloud.aiplatform.v1beta1.StructValueH\x00\x12H\n\x08metadata\x18\x0e \x01(\x0b26.google.cloud.aiplatform.v1beta1.FeatureValue.Metadata\x1a=\n\x08Metadata\x121\n\rgenerate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x07\n\x05value"P\n\x0bStructValue\x12A\n\x06values\x18\x01 \x03(\x0b21.google.cloud.aiplatform.v1beta1.StructFieldValue"^\n\x10StructFieldValue\x12\x0c\n\x04name\x18\x01 \x01(\t\x12<\n\x05value\x18\x02 \x01(\x0b2-.google.cloud.aiplatform.v1beta1.FeatureValue"Q\n\x10FeatureValueList\x12=\n\x06values\x18\x01 \x03(\x0b2-.google.cloud.aiplatform.v1beta1.FeatureValue2\xab\x07\n FeaturestoreOnlineServingService\x12\x82\x02\n\x11ReadFeatureValues\x129.google.cloud.aiplatform.v1beta1.ReadFeatureValuesRequest\x1a:.google.cloud.aiplatform.v1beta1.ReadFeatureValuesResponse"v\xdaA\x0bentity_type\x82\xd3\xe4\x93\x02b"]/v1beta1/{entity_type=projects/*/locations/*/featurestores/*/entityTypes/*}:readFeatureValues:\x01*\x12\x9f\x02\n\x1aStreamingReadFeatureValues\x12B.google.cloud.aiplatform.v1beta1.StreamingReadFeatureValuesRequest\x1a:.google.cloud.aiplatform.v1beta1.ReadFeatureValuesResponse"\x7f\xdaA\x0bentity_type\x82\xd3\xe4\x93\x02k"f/v1beta1/{entity_type=projects/*/locations/*/featurestores/*/entityTypes/*}:streamingReadFeatureValues:\x01*0\x01\x12\x90\x02\n\x12WriteFeatureValues\x12:.google.cloud.aiplatform.v1beta1.WriteFeatureValuesRequest\x1a;.google.cloud.aiplatform.v1beta1.WriteFeatureValuesResponse"\x80\x01\xdaA\x14entity_type,payloads\x82\xd3\xe4\x93\x02c"^/v1beta1/{entity_type=projects/*/locations/*/featurestores/*/entityTypes/*}:writeFeatureValues:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf5\x01\n#com.google.cloud.aiplatform.v1beta1B\x1eFeaturestoreOnlineServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.featurestore_online_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x1eFeaturestoreOnlineServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
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
    _globals['_FEATURESTOREONLINESERVINGSERVICE'].methods_by_name['ReadFeatureValues']._serialized_options = b'\xdaA\x0bentity_type\x82\xd3\xe4\x93\x02b"]/v1beta1/{entity_type=projects/*/locations/*/featurestores/*/entityTypes/*}:readFeatureValues:\x01*'
    _globals['_FEATURESTOREONLINESERVINGSERVICE'].methods_by_name['StreamingReadFeatureValues']._loaded_options = None
    _globals['_FEATURESTOREONLINESERVINGSERVICE'].methods_by_name['StreamingReadFeatureValues']._serialized_options = b'\xdaA\x0bentity_type\x82\xd3\xe4\x93\x02k"f/v1beta1/{entity_type=projects/*/locations/*/featurestores/*/entityTypes/*}:streamingReadFeatureValues:\x01*'
    _globals['_FEATURESTOREONLINESERVINGSERVICE'].methods_by_name['WriteFeatureValues']._loaded_options = None
    _globals['_FEATURESTOREONLINESERVINGSERVICE'].methods_by_name['WriteFeatureValues']._serialized_options = b'\xdaA\x14entity_type,payloads\x82\xd3\xe4\x93\x02c"^/v1beta1/{entity_type=projects/*/locations/*/featurestores/*/entityTypes/*}:writeFeatureValues:\x01*'
    _globals['_WRITEFEATUREVALUESREQUEST']._serialized_start = 352
    _globals['_WRITEFEATUREVALUESREQUEST']._serialized_end = 529
    _globals['_WRITEFEATUREVALUESPAYLOAD']._serialized_start = 532
    _globals['_WRITEFEATUREVALUESPAYLOAD']._serialized_end = 792
    _globals['_WRITEFEATUREVALUESPAYLOAD_FEATUREVALUESENTRY']._serialized_start = 693
    _globals['_WRITEFEATUREVALUESPAYLOAD_FEATUREVALUESENTRY']._serialized_end = 792
    _globals['_WRITEFEATUREVALUESRESPONSE']._serialized_start = 794
    _globals['_WRITEFEATUREVALUESRESPONSE']._serialized_end = 822
    _globals['_READFEATUREVALUESREQUEST']._serialized_start = 825
    _globals['_READFEATUREVALUESREQUEST']._serialized_end = 1023
    _globals['_READFEATUREVALUESRESPONSE']._serialized_start = 1026
    _globals['_READFEATUREVALUESRESPONSE']._serialized_end = 1717
    _globals['_READFEATUREVALUESRESPONSE_FEATUREDESCRIPTOR']._serialized_start = 1230
    _globals['_READFEATUREVALUESRESPONSE_FEATUREDESCRIPTOR']._serialized_end = 1261
    _globals['_READFEATUREVALUESRESPONSE_HEADER']._serialized_start = 1264
    _globals['_READFEATUREVALUESRESPONSE_HEADER']._serialized_end = 1443
    _globals['_READFEATUREVALUESRESPONSE_ENTITYVIEW']._serialized_start = 1446
    _globals['_READFEATUREVALUESRESPONSE_ENTITYVIEW']._serialized_end = 1717
    _globals['_READFEATUREVALUESRESPONSE_ENTITYVIEW_DATA']._serialized_start = 1570
    _globals['_READFEATUREVALUESRESPONSE_ENTITYVIEW_DATA']._serialized_end = 1717
    _globals['_STREAMINGREADFEATUREVALUESREQUEST']._serialized_start = 1720
    _globals['_STREAMINGREADFEATUREVALUESREQUEST']._serialized_end = 1928
    _globals['_FEATUREVALUE']._serialized_start = 1931
    _globals['_FEATUREVALUE']._serialized_end = 2575
    _globals['_FEATUREVALUE_METADATA']._serialized_start = 2505
    _globals['_FEATUREVALUE_METADATA']._serialized_end = 2566
    _globals['_STRUCTVALUE']._serialized_start = 2577
    _globals['_STRUCTVALUE']._serialized_end = 2657
    _globals['_STRUCTFIELDVALUE']._serialized_start = 2659
    _globals['_STRUCTFIELDVALUE']._serialized_end = 2753
    _globals['_FEATUREVALUELIST']._serialized_start = 2755
    _globals['_FEATUREVALUELIST']._serialized_end = 2836
    _globals['_FEATURESTOREONLINESERVINGSERVICE']._serialized_start = 2839
    _globals['_FEATURESTOREONLINESERVINGSERVICE']._serialized_end = 3778