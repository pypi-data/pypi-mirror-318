"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/feature_registry_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import feature_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_feature__pb2
from .....google.cloud.aiplatform.v1 import feature_group_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_feature__group__pb2
from .....google.cloud.aiplatform.v1 import featurestore_service_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_featurestore__service__pb2
from .....google.cloud.aiplatform.v1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_operation__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/aiplatform/v1/feature_registry_service.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/aiplatform/v1/feature.proto\x1a.google/cloud/aiplatform/v1/feature_group.proto\x1a5google/cloud/aiplatform/v1/featurestore_service.proto\x1a*google/cloud/aiplatform/v1/operation.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xc0\x01\n\x19CreateFeatureGroupRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&aiplatform.googleapis.com/FeatureGroup\x12D\n\rfeature_group\x18\x02 \x01(\x0b2(.google.cloud.aiplatform.v1.FeatureGroupB\x03\xe0A\x02\x12\x1d\n\x10feature_group_id\x18\x03 \x01(\tB\x03\xe0A\x02"V\n\x16GetFeatureGroupRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/FeatureGroup"\xa3\x01\n\x18ListFeatureGroupsRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&aiplatform.googleapis.com/FeatureGroup\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"v\n\x19ListFeatureGroupsResponse\x12@\n\x0efeature_groups\x18\x01 \x03(\x0b2(.google.cloud.aiplatform.v1.FeatureGroup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x92\x01\n\x19UpdateFeatureGroupRequest\x12D\n\rfeature_group\x18\x01 \x01(\x0b2(.google.cloud.aiplatform.v1.FeatureGroupB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"h\n\x19DeleteFeatureGroupRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/FeatureGroup\x12\r\n\x05force\x18\x02 \x01(\x08"u\n#CreateFeatureGroupOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata"u\n#UpdateFeatureGroupOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata"x\n&CreateRegistryFeatureOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata"p\n\x1eUpdateFeatureOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata2\xe3\x14\n\x16FeatureRegistryService\x12\x93\x02\n\x12CreateFeatureGroup\x125.google.cloud.aiplatform.v1.CreateFeatureGroupRequest\x1a\x1d.google.longrunning.Operation"\xa6\x01\xcaA3\n\x0cFeatureGroup\x12#CreateFeatureGroupOperationMetadata\xdaA%parent,feature_group,feature_group_id\x82\xd3\xe4\x93\x02B"1/v1/{parent=projects/*/locations/*}/featureGroups:\rfeature_group\x12\xb1\x01\n\x0fGetFeatureGroup\x122.google.cloud.aiplatform.v1.GetFeatureGroupRequest\x1a(.google.cloud.aiplatform.v1.FeatureGroup"@\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1/{name=projects/*/locations/*/featureGroups/*}\x12\xc4\x01\n\x11ListFeatureGroups\x124.google.cloud.aiplatform.v1.ListFeatureGroupsRequest\x1a5.google.cloud.aiplatform.v1.ListFeatureGroupsResponse"B\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1/{parent=projects/*/locations/*}/featureGroups\x12\x95\x02\n\x12UpdateFeatureGroup\x125.google.cloud.aiplatform.v1.UpdateFeatureGroupRequest\x1a\x1d.google.longrunning.Operation"\xa8\x01\xcaA3\n\x0cFeatureGroup\x12#UpdateFeatureGroupOperationMetadata\xdaA\x19feature_group,update_mask\x82\xd3\xe4\x93\x02P2?/v1/{feature_group.name=projects/*/locations/*/featureGroups/*}:\rfeature_group\x12\xe5\x01\n\x12DeleteFeatureGroup\x125.google.cloud.aiplatform.v1.DeleteFeatureGroupRequest\x1a\x1d.google.longrunning.Operation"y\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\nname,force\x82\xd3\xe4\x93\x023*1/v1/{name=projects/*/locations/*/featureGroups/*}\x12\xf8\x01\n\rCreateFeature\x120.google.cloud.aiplatform.v1.CreateFeatureRequest\x1a\x1d.google.longrunning.Operation"\x95\x01\xcaA)\n\x07Feature\x12\x1eCreateFeatureOperationMetadata\xdaA\x19parent,feature,feature_id\x82\xd3\xe4\x93\x02G"</v1/{parent=projects/*/locations/*/featureGroups/*}/features:\x07feature\x12\x9a\x02\n\x13BatchCreateFeatures\x126.google.cloud.aiplatform.v1.BatchCreateFeaturesRequest\x1a\x1d.google.longrunning.Operation"\xab\x01\xcaAC\n\x1bBatchCreateFeaturesResponse\x12$BatchCreateFeaturesOperationMetadata\xdaA\x0fparent,requests\x82\xd3\xe4\x93\x02M"H/v1/{parent=projects/*/locations/*/featureGroups/*}/features:batchCreate:\x01*\x12\xad\x01\n\nGetFeature\x12-.google.cloud.aiplatform.v1.GetFeatureRequest\x1a#.google.cloud.aiplatform.v1.Feature"K\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1/{name=projects/*/locations/*/featureGroups/*/features/*}\x12\xc0\x01\n\x0cListFeatures\x12/.google.cloud.aiplatform.v1.ListFeaturesRequest\x1a0.google.cloud.aiplatform.v1.ListFeaturesResponse"M\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1/{parent=projects/*/locations/*/featureGroups/*}/features\x12\xfa\x01\n\rUpdateFeature\x120.google.cloud.aiplatform.v1.UpdateFeatureRequest\x1a\x1d.google.longrunning.Operation"\x97\x01\xcaA)\n\x07Feature\x12\x1eUpdateFeatureOperationMetadata\xdaA\x13feature,update_mask\x82\xd3\xe4\x93\x02O2D/v1/{feature.name=projects/*/locations/*/featureGroups/*/features/*}:\x07feature\x12\xe0\x01\n\rDeleteFeature\x120.google.cloud.aiplatform.v1.DeleteFeatureRequest\x1a\x1d.google.longrunning.Operation"~\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02>*</v1/{name=projects/*/locations/*/featureGroups/*/features/*}\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd9\x01\n\x1ecom.google.cloud.aiplatform.v1B\x1bFeatureRegistryServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.feature_registry_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x1bFeatureRegistryServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_CREATEFEATUREGROUPREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEFEATUREGROUPREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&aiplatform.googleapis.com/FeatureGroup'
    _globals['_CREATEFEATUREGROUPREQUEST'].fields_by_name['feature_group']._loaded_options = None
    _globals['_CREATEFEATUREGROUPREQUEST'].fields_by_name['feature_group']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEFEATUREGROUPREQUEST'].fields_by_name['feature_group_id']._loaded_options = None
    _globals['_CREATEFEATUREGROUPREQUEST'].fields_by_name['feature_group_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETFEATUREGROUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFEATUREGROUPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/FeatureGroup'
    _globals['_LISTFEATUREGROUPSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFEATUREGROUPSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&aiplatform.googleapis.com/FeatureGroup'
    _globals['_UPDATEFEATUREGROUPREQUEST'].fields_by_name['feature_group']._loaded_options = None
    _globals['_UPDATEFEATUREGROUPREQUEST'].fields_by_name['feature_group']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEFEATUREGROUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEFEATUREGROUPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/FeatureGroup'
    _globals['_FEATUREREGISTRYSERVICE']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['CreateFeatureGroup']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['CreateFeatureGroup']._serialized_options = b'\xcaA3\n\x0cFeatureGroup\x12#CreateFeatureGroupOperationMetadata\xdaA%parent,feature_group,feature_group_id\x82\xd3\xe4\x93\x02B"1/v1/{parent=projects/*/locations/*}/featureGroups:\rfeature_group'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['GetFeatureGroup']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['GetFeatureGroup']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1/{name=projects/*/locations/*/featureGroups/*}'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['ListFeatureGroups']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['ListFeatureGroups']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1/{parent=projects/*/locations/*}/featureGroups'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['UpdateFeatureGroup']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['UpdateFeatureGroup']._serialized_options = b'\xcaA3\n\x0cFeatureGroup\x12#UpdateFeatureGroupOperationMetadata\xdaA\x19feature_group,update_mask\x82\xd3\xe4\x93\x02P2?/v1/{feature_group.name=projects/*/locations/*/featureGroups/*}:\rfeature_group'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['DeleteFeatureGroup']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['DeleteFeatureGroup']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\nname,force\x82\xd3\xe4\x93\x023*1/v1/{name=projects/*/locations/*/featureGroups/*}'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['CreateFeature']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['CreateFeature']._serialized_options = b'\xcaA)\n\x07Feature\x12\x1eCreateFeatureOperationMetadata\xdaA\x19parent,feature,feature_id\x82\xd3\xe4\x93\x02G"</v1/{parent=projects/*/locations/*/featureGroups/*}/features:\x07feature'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['BatchCreateFeatures']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['BatchCreateFeatures']._serialized_options = b'\xcaAC\n\x1bBatchCreateFeaturesResponse\x12$BatchCreateFeaturesOperationMetadata\xdaA\x0fparent,requests\x82\xd3\xe4\x93\x02M"H/v1/{parent=projects/*/locations/*/featureGroups/*}/features:batchCreate:\x01*'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['GetFeature']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['GetFeature']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1/{name=projects/*/locations/*/featureGroups/*/features/*}'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['ListFeatures']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['ListFeatures']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1/{parent=projects/*/locations/*/featureGroups/*}/features'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['UpdateFeature']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['UpdateFeature']._serialized_options = b'\xcaA)\n\x07Feature\x12\x1eUpdateFeatureOperationMetadata\xdaA\x13feature,update_mask\x82\xd3\xe4\x93\x02O2D/v1/{feature.name=projects/*/locations/*/featureGroups/*/features/*}:\x07feature'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['DeleteFeature']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['DeleteFeature']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02>*</v1/{name=projects/*/locations/*/featureGroups/*/features/*}'
    _globals['_CREATEFEATUREGROUPREQUEST']._serialized_start = 494
    _globals['_CREATEFEATUREGROUPREQUEST']._serialized_end = 686
    _globals['_GETFEATUREGROUPREQUEST']._serialized_start = 688
    _globals['_GETFEATUREGROUPREQUEST']._serialized_end = 774
    _globals['_LISTFEATUREGROUPSREQUEST']._serialized_start = 777
    _globals['_LISTFEATUREGROUPSREQUEST']._serialized_end = 940
    _globals['_LISTFEATUREGROUPSRESPONSE']._serialized_start = 942
    _globals['_LISTFEATUREGROUPSRESPONSE']._serialized_end = 1060
    _globals['_UPDATEFEATUREGROUPREQUEST']._serialized_start = 1063
    _globals['_UPDATEFEATUREGROUPREQUEST']._serialized_end = 1209
    _globals['_DELETEFEATUREGROUPREQUEST']._serialized_start = 1211
    _globals['_DELETEFEATUREGROUPREQUEST']._serialized_end = 1315
    _globals['_CREATEFEATUREGROUPOPERATIONMETADATA']._serialized_start = 1317
    _globals['_CREATEFEATUREGROUPOPERATIONMETADATA']._serialized_end = 1434
    _globals['_UPDATEFEATUREGROUPOPERATIONMETADATA']._serialized_start = 1436
    _globals['_UPDATEFEATUREGROUPOPERATIONMETADATA']._serialized_end = 1553
    _globals['_CREATEREGISTRYFEATUREOPERATIONMETADATA']._serialized_start = 1555
    _globals['_CREATEREGISTRYFEATUREOPERATIONMETADATA']._serialized_end = 1675
    _globals['_UPDATEFEATUREOPERATIONMETADATA']._serialized_start = 1677
    _globals['_UPDATEFEATUREOPERATIONMETADATA']._serialized_end = 1789
    _globals['_FEATUREREGISTRYSERVICE']._serialized_start = 1792
    _globals['_FEATUREREGISTRYSERVICE']._serialized_end = 4451