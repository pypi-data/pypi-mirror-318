"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/services/experiment_arm_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v17.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v17.resources import experiment_arm_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_resources_dot_experiment__arm__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/ads/googleads/v17/services/experiment_arm_service.proto\x12!google.ads.googleads.v17.services\x1a:google/ads/googleads/v17/enums/response_content_type.proto\x1a7google/ads/googleads/v17/resources/experiment_arm.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\xa7\x02\n\x1bMutateExperimentArmsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12R\n\noperations\x18\x02 \x03(\x0b29.google.ads.googleads.v17.services.ExperimentArmOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12j\n\x15response_content_type\x18\x05 \x01(\x0e2K.google.ads.googleads.v17.enums.ResponseContentTypeEnum.ResponseContentType"\x9f\x02\n\x16ExperimentArmOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12C\n\x06create\x18\x01 \x01(\x0b21.google.ads.googleads.v17.resources.ExperimentArmH\x00\x12C\n\x06update\x18\x02 \x01(\x0b21.google.ads.googleads.v17.resources.ExperimentArmH\x00\x12=\n\x06remove\x18\x03 \x01(\tB+\xfaA(\n&googleads.googleapis.com/ExperimentArmH\x00B\x0b\n\toperation"\xa0\x01\n\x1cMutateExperimentArmsResponse\x121\n\x15partial_failure_error\x18\x01 \x01(\x0b2\x12.google.rpc.Status\x12M\n\x07results\x18\x02 \x03(\x0b2<.google.ads.googleads.v17.services.MutateExperimentArmResult"\xaa\x01\n\x19MutateExperimentArmResult\x12B\n\rresource_name\x18\x01 \x01(\tB+\xfaA(\n&googleads.googleapis.com/ExperimentArm\x12I\n\x0eexperiment_arm\x18\x02 \x01(\x0b21.google.ads.googleads.v17.resources.ExperimentArm2\xd1\x02\n\x14ExperimentArmService\x12\xf1\x01\n\x14MutateExperimentArms\x12>.google.ads.googleads.v17.services.MutateExperimentArmsRequest\x1a?.google.ads.googleads.v17.services.MutateExperimentArmsResponse"X\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x029"4/v17/customers/{customer_id=*}/experimentArms:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x85\x02\n%com.google.ads.googleads.v17.servicesB\x19ExperimentArmServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v17/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V17.Services\xca\x02!Google\\Ads\\GoogleAds\\V17\\Services\xea\x02%Google::Ads::GoogleAds::V17::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.services.experiment_arm_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v17.servicesB\x19ExperimentArmServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v17/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V17.Services\xca\x02!Google\\Ads\\GoogleAds\\V17\\Services\xea\x02%Google::Ads::GoogleAds::V17::Services'
    _globals['_MUTATEEXPERIMENTARMSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEEXPERIMENTARMSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEEXPERIMENTARMSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATEEXPERIMENTARMSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_EXPERIMENTARMOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_EXPERIMENTARMOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA(\n&googleads.googleapis.com/ExperimentArm'
    _globals['_MUTATEEXPERIMENTARMRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEEXPERIMENTARMRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA(\n&googleads.googleapis.com/ExperimentArm'
    _globals['_EXPERIMENTARMSERVICE']._loaded_options = None
    _globals['_EXPERIMENTARMSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_EXPERIMENTARMSERVICE'].methods_by_name['MutateExperimentArms']._loaded_options = None
    _globals['_EXPERIMENTARMSERVICE'].methods_by_name['MutateExperimentArms']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x029"4/v17/customers/{customer_id=*}/experimentArms:mutate:\x01*'
    _globals['_MUTATEEXPERIMENTARMSREQUEST']._serialized_start = 393
    _globals['_MUTATEEXPERIMENTARMSREQUEST']._serialized_end = 688
    _globals['_EXPERIMENTARMOPERATION']._serialized_start = 691
    _globals['_EXPERIMENTARMOPERATION']._serialized_end = 978
    _globals['_MUTATEEXPERIMENTARMSRESPONSE']._serialized_start = 981
    _globals['_MUTATEEXPERIMENTARMSRESPONSE']._serialized_end = 1141
    _globals['_MUTATEEXPERIMENTARMRESULT']._serialized_start = 1144
    _globals['_MUTATEEXPERIMENTARMRESULT']._serialized_end = 1314
    _globals['_EXPERIMENTARMSERVICE']._serialized_start = 1317
    _globals['_EXPERIMENTARMSERVICE']._serialized_end = 1654