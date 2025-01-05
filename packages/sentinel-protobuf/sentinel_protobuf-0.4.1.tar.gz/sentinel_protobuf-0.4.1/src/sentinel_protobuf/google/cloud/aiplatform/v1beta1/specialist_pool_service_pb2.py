"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/specialist_pool_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.cloud.aiplatform.v1beta1 import specialist_pool_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_specialist__pool__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/aiplatform/v1beta1/specialist_pool_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a5google/cloud/aiplatform/v1beta1/specialist_pool.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xa7\x01\n\x1bCreateSpecialistPoolRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12M\n\x0fspecialist_pool\x18\x02 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.SpecialistPoolB\x03\xe0A\x02"|\n%CreateSpecialistPoolOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"Z\n\x18GetSpecialistPoolRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/SpecialistPool"\xad\x01\n\x1aListSpecialistPoolsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12-\n\tread_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x81\x01\n\x1bListSpecialistPoolsResponse\x12I\n\x10specialist_pools\x18\x01 \x03(\x0b2/.google.cloud.aiplatform.v1beta1.SpecialistPool\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"l\n\x1bDeleteSpecialistPoolRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/SpecialistPool\x12\r\n\x05force\x18\x02 \x01(\x08"\xa2\x01\n\x1bUpdateSpecialistPoolRequest\x12M\n\x0fspecialist_pool\x18\x01 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.SpecialistPoolB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\xc7\x01\n%UpdateSpecialistPoolOperationMetadata\x12I\n\x0fspecialist_pool\x18\x01 \x01(\tB0\xe0A\x03\xfaA*\n(aiplatform.googleapis.com/SpecialistPool\x12S\n\x10generic_metadata\x18\x02 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata2\xd0\n\n\x15SpecialistPoolService\x12\x9a\x02\n\x14CreateSpecialistPool\x12<.google.cloud.aiplatform.v1beta1.CreateSpecialistPoolRequest\x1a\x1d.google.longrunning.Operation"\xa4\x01\xcaA7\n\x0eSpecialistPool\x12%CreateSpecialistPoolOperationMetadata\xdaA\x16parent,specialist_pool\x82\xd3\xe4\x93\x02K"8/v1beta1/{parent=projects/*/locations/*}/specialistPools:\x0fspecialist_pool\x12\xc8\x01\n\x11GetSpecialistPool\x129.google.cloud.aiplatform.v1beta1.GetSpecialistPoolRequest\x1a/.google.cloud.aiplatform.v1beta1.SpecialistPool"G\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/v1beta1/{name=projects/*/locations/*/specialistPools/*}\x12\xdb\x01\n\x13ListSpecialistPools\x12;.google.cloud.aiplatform.v1beta1.ListSpecialistPoolsRequest\x1a<.google.cloud.aiplatform.v1beta1.ListSpecialistPoolsResponse"I\xdaA\x06parent\x82\xd3\xe4\x93\x02:\x128/v1beta1/{parent=projects/*/locations/*}/specialistPools\x12\xef\x01\n\x14DeleteSpecialistPool\x12<.google.cloud.aiplatform.v1beta1.DeleteSpecialistPoolRequest\x1a\x1d.google.longrunning.Operation"z\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v1beta1/{name=projects/*/locations/*/specialistPools/*}\x12\xaf\x02\n\x14UpdateSpecialistPool\x12<.google.cloud.aiplatform.v1beta1.UpdateSpecialistPoolRequest\x1a\x1d.google.longrunning.Operation"\xb9\x01\xcaA7\n\x0eSpecialistPool\x12%UpdateSpecialistPoolOperationMetadata\xdaA\x1bspecialist_pool,update_mask\x82\xd3\xe4\x93\x02[2H/v1beta1/{specialist_pool.name=projects/*/locations/*/specialistPools/*}:\x0fspecialist_pool\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf1\x01\n#com.google.cloud.aiplatform.v1beta1B\x1aSpecialistPoolServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.specialist_pool_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x1aSpecialistPoolServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_CREATESPECIALISTPOOLREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESPECIALISTPOOLREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATESPECIALISTPOOLREQUEST'].fields_by_name['specialist_pool']._loaded_options = None
    _globals['_CREATESPECIALISTPOOLREQUEST'].fields_by_name['specialist_pool']._serialized_options = b'\xe0A\x02'
    _globals['_GETSPECIALISTPOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSPECIALISTPOOLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/SpecialistPool'
    _globals['_LISTSPECIALISTPOOLSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSPECIALISTPOOLSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_DELETESPECIALISTPOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESPECIALISTPOOLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/SpecialistPool'
    _globals['_UPDATESPECIALISTPOOLREQUEST'].fields_by_name['specialist_pool']._loaded_options = None
    _globals['_UPDATESPECIALISTPOOLREQUEST'].fields_by_name['specialist_pool']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESPECIALISTPOOLREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESPECIALISTPOOLREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESPECIALISTPOOLOPERATIONMETADATA'].fields_by_name['specialist_pool']._loaded_options = None
    _globals['_UPDATESPECIALISTPOOLOPERATIONMETADATA'].fields_by_name['specialist_pool']._serialized_options = b'\xe0A\x03\xfaA*\n(aiplatform.googleapis.com/SpecialistPool'
    _globals['_SPECIALISTPOOLSERVICE']._loaded_options = None
    _globals['_SPECIALISTPOOLSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SPECIALISTPOOLSERVICE'].methods_by_name['CreateSpecialistPool']._loaded_options = None
    _globals['_SPECIALISTPOOLSERVICE'].methods_by_name['CreateSpecialistPool']._serialized_options = b'\xcaA7\n\x0eSpecialistPool\x12%CreateSpecialistPoolOperationMetadata\xdaA\x16parent,specialist_pool\x82\xd3\xe4\x93\x02K"8/v1beta1/{parent=projects/*/locations/*}/specialistPools:\x0fspecialist_pool'
    _globals['_SPECIALISTPOOLSERVICE'].methods_by_name['GetSpecialistPool']._loaded_options = None
    _globals['_SPECIALISTPOOLSERVICE'].methods_by_name['GetSpecialistPool']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/v1beta1/{name=projects/*/locations/*/specialistPools/*}'
    _globals['_SPECIALISTPOOLSERVICE'].methods_by_name['ListSpecialistPools']._loaded_options = None
    _globals['_SPECIALISTPOOLSERVICE'].methods_by_name['ListSpecialistPools']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02:\x128/v1beta1/{parent=projects/*/locations/*}/specialistPools'
    _globals['_SPECIALISTPOOLSERVICE'].methods_by_name['DeleteSpecialistPool']._loaded_options = None
    _globals['_SPECIALISTPOOLSERVICE'].methods_by_name['DeleteSpecialistPool']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v1beta1/{name=projects/*/locations/*/specialistPools/*}'
    _globals['_SPECIALISTPOOLSERVICE'].methods_by_name['UpdateSpecialistPool']._loaded_options = None
    _globals['_SPECIALISTPOOLSERVICE'].methods_by_name['UpdateSpecialistPool']._serialized_options = b'\xcaA7\n\x0eSpecialistPool\x12%UpdateSpecialistPoolOperationMetadata\xdaA\x1bspecialist_pool,update_mask\x82\xd3\xe4\x93\x02[2H/v1beta1/{specialist_pool.name=projects/*/locations/*/specialistPools/*}:\x0fspecialist_pool'
    _globals['_CREATESPECIALISTPOOLREQUEST']._serialized_start = 418
    _globals['_CREATESPECIALISTPOOLREQUEST']._serialized_end = 585
    _globals['_CREATESPECIALISTPOOLOPERATIONMETADATA']._serialized_start = 587
    _globals['_CREATESPECIALISTPOOLOPERATIONMETADATA']._serialized_end = 711
    _globals['_GETSPECIALISTPOOLREQUEST']._serialized_start = 713
    _globals['_GETSPECIALISTPOOLREQUEST']._serialized_end = 803
    _globals['_LISTSPECIALISTPOOLSREQUEST']._serialized_start = 806
    _globals['_LISTSPECIALISTPOOLSREQUEST']._serialized_end = 979
    _globals['_LISTSPECIALISTPOOLSRESPONSE']._serialized_start = 982
    _globals['_LISTSPECIALISTPOOLSRESPONSE']._serialized_end = 1111
    _globals['_DELETESPECIALISTPOOLREQUEST']._serialized_start = 1113
    _globals['_DELETESPECIALISTPOOLREQUEST']._serialized_end = 1221
    _globals['_UPDATESPECIALISTPOOLREQUEST']._serialized_start = 1224
    _globals['_UPDATESPECIALISTPOOLREQUEST']._serialized_end = 1386
    _globals['_UPDATESPECIALISTPOOLOPERATIONMETADATA']._serialized_start = 1389
    _globals['_UPDATESPECIALISTPOOLOPERATIONMETADATA']._serialized_end = 1588
    _globals['_SPECIALISTPOOLSERVICE']._serialized_start = 1591
    _globals['_SPECIALISTPOOLSERVICE']._serialized_end = 2951