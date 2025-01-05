"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dataproc/v1/autoscaling_policies.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/dataproc/v1/autoscaling_policies.proto\x12\x18google.cloud.dataproc.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto"\xa5\x05\n\x11AutoscalingPolicy\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\x04name\x18\x02 \x01(\tB\x03\xe0A\x03\x12S\n\x0fbasic_algorithm\x18\x03 \x01(\x0b23.google.cloud.dataproc.v1.BasicAutoscalingAlgorithmB\x03\xe0A\x02H\x00\x12Z\n\rworker_config\x18\x04 \x01(\x0b2>.google.cloud.dataproc.v1.InstanceGroupAutoscalingPolicyConfigB\x03\xe0A\x02\x12d\n\x17secondary_worker_config\x18\x05 \x01(\x0b2>.google.cloud.dataproc.v1.InstanceGroupAutoscalingPolicyConfigB\x03\xe0A\x01\x12L\n\x06labels\x18\x06 \x03(\x0b27.google.cloud.dataproc.v1.AutoscalingPolicy.LabelsEntryB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\xcf\x01\xeaA\xcb\x01\n)dataproc.googleapis.com/AutoscalingPolicy\x12Pprojects/{project}/locations/{location}/autoscalingPolicies/{autoscaling_policy}\x12Lprojects/{project}/regions/{region}/autoscalingPolicies/{autoscaling_policy}B\x0b\n\talgorithm"\xb0\x01\n\x19BasicAutoscalingAlgorithm\x12P\n\x0byarn_config\x18\x01 \x01(\x0b24.google.cloud.dataproc.v1.BasicYarnAutoscalingConfigB\x03\xe0A\x02H\x00\x127\n\x0fcooldown_period\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01B\x08\n\x06config"\xf9\x01\n\x1aBasicYarnAutoscalingConfig\x12E\n\x1dgraceful_decommission_timeout\x18\x05 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x02\x12\x1c\n\x0fscale_up_factor\x18\x01 \x01(\x01B\x03\xe0A\x02\x12\x1e\n\x11scale_down_factor\x18\x02 \x01(\x01B\x03\xe0A\x02\x12)\n\x1cscale_up_min_worker_fraction\x18\x03 \x01(\x01B\x03\xe0A\x01\x12+\n\x1escale_down_min_worker_fraction\x18\x04 \x01(\x01B\x03\xe0A\x01"s\n$InstanceGroupAutoscalingPolicyConfig\x12\x1a\n\rmin_instances\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x1a\n\rmax_instances\x18\x02 \x01(\x05B\x03\xe0A\x02\x12\x13\n\x06weight\x18\x03 \x01(\x05B\x03\xe0A\x01"\xa5\x01\n\x1eCreateAutoscalingPolicyRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\x12)dataproc.googleapis.com/AutoscalingPolicy\x12@\n\x06policy\x18\x02 \x01(\x0b2+.google.cloud.dataproc.v1.AutoscalingPolicyB\x03\xe0A\x02"^\n\x1bGetAutoscalingPolicyRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)dataproc.googleapis.com/AutoscalingPolicy"b\n\x1eUpdateAutoscalingPolicyRequest\x12@\n\x06policy\x18\x01 \x01(\x0b2+.google.cloud.dataproc.v1.AutoscalingPolicyB\x03\xe0A\x02"a\n\x1eDeleteAutoscalingPolicyRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)dataproc.googleapis.com/AutoscalingPolicy"\x94\x01\n\x1eListAutoscalingPoliciesRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\x12)dataproc.googleapis.com/AutoscalingPolicy\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x83\x01\n\x1fListAutoscalingPoliciesResponse\x12B\n\x08policies\x18\x01 \x03(\x0b2+.google.cloud.dataproc.v1.AutoscalingPolicyB\x03\xe0A\x03\x12\x1c\n\x0fnext_page_token\x18\x02 \x01(\tB\x03\xe0A\x032\xae\x0b\n\x18AutoscalingPolicyService\x12\x9c\x02\n\x17CreateAutoscalingPolicy\x128.google.cloud.dataproc.v1.CreateAutoscalingPolicyRequest\x1a+.google.cloud.dataproc.v1.AutoscalingPolicy"\x99\x01\xdaA\rparent,policy\x82\xd3\xe4\x93\x02\x82\x01"7/v1/{parent=projects/*/locations/*}/autoscalingPolicies:\x06policyZ?"5/v1/{parent=projects/*/regions/*}/autoscalingPolicies:\x06policy\x12\xa3\x02\n\x17UpdateAutoscalingPolicy\x128.google.cloud.dataproc.v1.UpdateAutoscalingPolicyRequest\x1a+.google.cloud.dataproc.v1.AutoscalingPolicy"\xa0\x01\xdaA\x06policy\x82\xd3\xe4\x93\x02\x90\x01\x1a>/v1/{policy.name=projects/*/locations/*/autoscalingPolicies/*}:\x06policyZF\x1a</v1/{policy.name=projects/*/regions/*/autoscalingPolicies/*}:\x06policy\x12\xfb\x01\n\x14GetAutoscalingPolicy\x125.google.cloud.dataproc.v1.GetAutoscalingPolicyRequest\x1a+.google.cloud.dataproc.v1.AutoscalingPolicy"\x7f\xdaA\x04name\x82\xd3\xe4\x93\x02r\x127/v1/{name=projects/*/locations/*/autoscalingPolicies/*}Z7\x125/v1/{name=projects/*/regions/*/autoscalingPolicies/*}\x12\x92\x02\n\x17ListAutoscalingPolicies\x128.google.cloud.dataproc.v1.ListAutoscalingPoliciesRequest\x1a9.google.cloud.dataproc.v1.ListAutoscalingPoliciesResponse"\x81\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02r\x127/v1/{parent=projects/*/locations/*}/autoscalingPoliciesZ7\x125/v1/{parent=projects/*/regions/*}/autoscalingPolicies\x12\xec\x01\n\x17DeleteAutoscalingPolicy\x128.google.cloud.dataproc.v1.DeleteAutoscalingPolicyRequest\x1a\x16.google.protobuf.Empty"\x7f\xdaA\x04name\x82\xd3\xe4\x93\x02r*7/v1/{name=projects/*/locations/*/autoscalingPolicies/*}Z7*5/v1/{name=projects/*/regions/*/autoscalingPolicies/*}\x1aK\xcaA\x17dataproc.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xbf\x01\n\x1ccom.google.cloud.dataproc.v1B\x18AutoscalingPoliciesProtoP\x01Z;cloud.google.com/go/dataproc/v2/apiv1/dataprocpb;dataprocpb\xeaAE\n\x1edataproc.googleapis.com/Region\x12#projects/{project}/regions/{region}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataproc.v1.autoscaling_policies_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.dataproc.v1B\x18AutoscalingPoliciesProtoP\x01Z;cloud.google.com/go/dataproc/v2/apiv1/dataprocpb;dataprocpb\xeaAE\n\x1edataproc.googleapis.com/Region\x12#projects/{project}/regions/{region}'
    _globals['_AUTOSCALINGPOLICY_LABELSENTRY']._loaded_options = None
    _globals['_AUTOSCALINGPOLICY_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_AUTOSCALINGPOLICY'].fields_by_name['name']._loaded_options = None
    _globals['_AUTOSCALINGPOLICY'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_AUTOSCALINGPOLICY'].fields_by_name['basic_algorithm']._loaded_options = None
    _globals['_AUTOSCALINGPOLICY'].fields_by_name['basic_algorithm']._serialized_options = b'\xe0A\x02'
    _globals['_AUTOSCALINGPOLICY'].fields_by_name['worker_config']._loaded_options = None
    _globals['_AUTOSCALINGPOLICY'].fields_by_name['worker_config']._serialized_options = b'\xe0A\x02'
    _globals['_AUTOSCALINGPOLICY'].fields_by_name['secondary_worker_config']._loaded_options = None
    _globals['_AUTOSCALINGPOLICY'].fields_by_name['secondary_worker_config']._serialized_options = b'\xe0A\x01'
    _globals['_AUTOSCALINGPOLICY'].fields_by_name['labels']._loaded_options = None
    _globals['_AUTOSCALINGPOLICY'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_AUTOSCALINGPOLICY']._loaded_options = None
    _globals['_AUTOSCALINGPOLICY']._serialized_options = b'\xeaA\xcb\x01\n)dataproc.googleapis.com/AutoscalingPolicy\x12Pprojects/{project}/locations/{location}/autoscalingPolicies/{autoscaling_policy}\x12Lprojects/{project}/regions/{region}/autoscalingPolicies/{autoscaling_policy}'
    _globals['_BASICAUTOSCALINGALGORITHM'].fields_by_name['yarn_config']._loaded_options = None
    _globals['_BASICAUTOSCALINGALGORITHM'].fields_by_name['yarn_config']._serialized_options = b'\xe0A\x02'
    _globals['_BASICAUTOSCALINGALGORITHM'].fields_by_name['cooldown_period']._loaded_options = None
    _globals['_BASICAUTOSCALINGALGORITHM'].fields_by_name['cooldown_period']._serialized_options = b'\xe0A\x01'
    _globals['_BASICYARNAUTOSCALINGCONFIG'].fields_by_name['graceful_decommission_timeout']._loaded_options = None
    _globals['_BASICYARNAUTOSCALINGCONFIG'].fields_by_name['graceful_decommission_timeout']._serialized_options = b'\xe0A\x02'
    _globals['_BASICYARNAUTOSCALINGCONFIG'].fields_by_name['scale_up_factor']._loaded_options = None
    _globals['_BASICYARNAUTOSCALINGCONFIG'].fields_by_name['scale_up_factor']._serialized_options = b'\xe0A\x02'
    _globals['_BASICYARNAUTOSCALINGCONFIG'].fields_by_name['scale_down_factor']._loaded_options = None
    _globals['_BASICYARNAUTOSCALINGCONFIG'].fields_by_name['scale_down_factor']._serialized_options = b'\xe0A\x02'
    _globals['_BASICYARNAUTOSCALINGCONFIG'].fields_by_name['scale_up_min_worker_fraction']._loaded_options = None
    _globals['_BASICYARNAUTOSCALINGCONFIG'].fields_by_name['scale_up_min_worker_fraction']._serialized_options = b'\xe0A\x01'
    _globals['_BASICYARNAUTOSCALINGCONFIG'].fields_by_name['scale_down_min_worker_fraction']._loaded_options = None
    _globals['_BASICYARNAUTOSCALINGCONFIG'].fields_by_name['scale_down_min_worker_fraction']._serialized_options = b'\xe0A\x01'
    _globals['_INSTANCEGROUPAUTOSCALINGPOLICYCONFIG'].fields_by_name['min_instances']._loaded_options = None
    _globals['_INSTANCEGROUPAUTOSCALINGPOLICYCONFIG'].fields_by_name['min_instances']._serialized_options = b'\xe0A\x01'
    _globals['_INSTANCEGROUPAUTOSCALINGPOLICYCONFIG'].fields_by_name['max_instances']._loaded_options = None
    _globals['_INSTANCEGROUPAUTOSCALINGPOLICYCONFIG'].fields_by_name['max_instances']._serialized_options = b'\xe0A\x02'
    _globals['_INSTANCEGROUPAUTOSCALINGPOLICYCONFIG'].fields_by_name['weight']._loaded_options = None
    _globals['_INSTANCEGROUPAUTOSCALINGPOLICYCONFIG'].fields_by_name['weight']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEAUTOSCALINGPOLICYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEAUTOSCALINGPOLICYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\x12)dataproc.googleapis.com/AutoscalingPolicy'
    _globals['_CREATEAUTOSCALINGPOLICYREQUEST'].fields_by_name['policy']._loaded_options = None
    _globals['_CREATEAUTOSCALINGPOLICYREQUEST'].fields_by_name['policy']._serialized_options = b'\xe0A\x02'
    _globals['_GETAUTOSCALINGPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETAUTOSCALINGPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)dataproc.googleapis.com/AutoscalingPolicy'
    _globals['_UPDATEAUTOSCALINGPOLICYREQUEST'].fields_by_name['policy']._loaded_options = None
    _globals['_UPDATEAUTOSCALINGPOLICYREQUEST'].fields_by_name['policy']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEAUTOSCALINGPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEAUTOSCALINGPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)dataproc.googleapis.com/AutoscalingPolicy'
    _globals['_LISTAUTOSCALINGPOLICIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTAUTOSCALINGPOLICIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\x12)dataproc.googleapis.com/AutoscalingPolicy'
    _globals['_LISTAUTOSCALINGPOLICIESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTAUTOSCALINGPOLICIESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTAUTOSCALINGPOLICIESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTAUTOSCALINGPOLICIESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTAUTOSCALINGPOLICIESRESPONSE'].fields_by_name['policies']._loaded_options = None
    _globals['_LISTAUTOSCALINGPOLICIESRESPONSE'].fields_by_name['policies']._serialized_options = b'\xe0A\x03'
    _globals['_LISTAUTOSCALINGPOLICIESRESPONSE'].fields_by_name['next_page_token']._loaded_options = None
    _globals['_LISTAUTOSCALINGPOLICIESRESPONSE'].fields_by_name['next_page_token']._serialized_options = b'\xe0A\x03'
    _globals['_AUTOSCALINGPOLICYSERVICE']._loaded_options = None
    _globals['_AUTOSCALINGPOLICYSERVICE']._serialized_options = b'\xcaA\x17dataproc.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_AUTOSCALINGPOLICYSERVICE'].methods_by_name['CreateAutoscalingPolicy']._loaded_options = None
    _globals['_AUTOSCALINGPOLICYSERVICE'].methods_by_name['CreateAutoscalingPolicy']._serialized_options = b'\xdaA\rparent,policy\x82\xd3\xe4\x93\x02\x82\x01"7/v1/{parent=projects/*/locations/*}/autoscalingPolicies:\x06policyZ?"5/v1/{parent=projects/*/regions/*}/autoscalingPolicies:\x06policy'
    _globals['_AUTOSCALINGPOLICYSERVICE'].methods_by_name['UpdateAutoscalingPolicy']._loaded_options = None
    _globals['_AUTOSCALINGPOLICYSERVICE'].methods_by_name['UpdateAutoscalingPolicy']._serialized_options = b'\xdaA\x06policy\x82\xd3\xe4\x93\x02\x90\x01\x1a>/v1/{policy.name=projects/*/locations/*/autoscalingPolicies/*}:\x06policyZF\x1a</v1/{policy.name=projects/*/regions/*/autoscalingPolicies/*}:\x06policy'
    _globals['_AUTOSCALINGPOLICYSERVICE'].methods_by_name['GetAutoscalingPolicy']._loaded_options = None
    _globals['_AUTOSCALINGPOLICYSERVICE'].methods_by_name['GetAutoscalingPolicy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02r\x127/v1/{name=projects/*/locations/*/autoscalingPolicies/*}Z7\x125/v1/{name=projects/*/regions/*/autoscalingPolicies/*}'
    _globals['_AUTOSCALINGPOLICYSERVICE'].methods_by_name['ListAutoscalingPolicies']._loaded_options = None
    _globals['_AUTOSCALINGPOLICYSERVICE'].methods_by_name['ListAutoscalingPolicies']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02r\x127/v1/{parent=projects/*/locations/*}/autoscalingPoliciesZ7\x125/v1/{parent=projects/*/regions/*}/autoscalingPolicies'
    _globals['_AUTOSCALINGPOLICYSERVICE'].methods_by_name['DeleteAutoscalingPolicy']._loaded_options = None
    _globals['_AUTOSCALINGPOLICYSERVICE'].methods_by_name['DeleteAutoscalingPolicy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02r*7/v1/{name=projects/*/locations/*/autoscalingPolicies/*}Z7*5/v1/{name=projects/*/regions/*/autoscalingPolicies/*}'
    _globals['_AUTOSCALINGPOLICY']._serialized_start = 258
    _globals['_AUTOSCALINGPOLICY']._serialized_end = 935
    _globals['_AUTOSCALINGPOLICY_LABELSENTRY']._serialized_start = 667
    _globals['_AUTOSCALINGPOLICY_LABELSENTRY']._serialized_end = 712
    _globals['_BASICAUTOSCALINGALGORITHM']._serialized_start = 938
    _globals['_BASICAUTOSCALINGALGORITHM']._serialized_end = 1114
    _globals['_BASICYARNAUTOSCALINGCONFIG']._serialized_start = 1117
    _globals['_BASICYARNAUTOSCALINGCONFIG']._serialized_end = 1366
    _globals['_INSTANCEGROUPAUTOSCALINGPOLICYCONFIG']._serialized_start = 1368
    _globals['_INSTANCEGROUPAUTOSCALINGPOLICYCONFIG']._serialized_end = 1483
    _globals['_CREATEAUTOSCALINGPOLICYREQUEST']._serialized_start = 1486
    _globals['_CREATEAUTOSCALINGPOLICYREQUEST']._serialized_end = 1651
    _globals['_GETAUTOSCALINGPOLICYREQUEST']._serialized_start = 1653
    _globals['_GETAUTOSCALINGPOLICYREQUEST']._serialized_end = 1747
    _globals['_UPDATEAUTOSCALINGPOLICYREQUEST']._serialized_start = 1749
    _globals['_UPDATEAUTOSCALINGPOLICYREQUEST']._serialized_end = 1847
    _globals['_DELETEAUTOSCALINGPOLICYREQUEST']._serialized_start = 1849
    _globals['_DELETEAUTOSCALINGPOLICYREQUEST']._serialized_end = 1946
    _globals['_LISTAUTOSCALINGPOLICIESREQUEST']._serialized_start = 1949
    _globals['_LISTAUTOSCALINGPOLICIESREQUEST']._serialized_end = 2097
    _globals['_LISTAUTOSCALINGPOLICIESRESPONSE']._serialized_start = 2100
    _globals['_LISTAUTOSCALINGPOLICIESRESPONSE']._serialized_end = 2231
    _globals['_AUTOSCALINGPOLICYSERVICE']._serialized_start = 2234
    _globals['_AUTOSCALINGPOLICYSERVICE']._serialized_end = 3688