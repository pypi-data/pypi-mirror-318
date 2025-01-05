"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/contentwarehouse/v1/ruleset_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.cloud.contentwarehouse.v1 import rule_engine_pb2 as google_dot_cloud_dot_contentwarehouse_dot_v1_dot_rule__engine__pb2
from .....google.cloud.contentwarehouse.v1 import ruleset_service_request_pb2 as google_dot_cloud_dot_contentwarehouse_dot_v1_dot_ruleset__service__request__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/contentwarehouse/v1/ruleset_service.proto\x12 google.cloud.contentwarehouse.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a2google/cloud/contentwarehouse/v1/rule_engine.proto\x1a>google/cloud/contentwarehouse/v1/ruleset_service_request.proto\x1a\x1bgoogle/protobuf/empty.proto2\xf4\x07\n\x0eRuleSetService\x12\xc4\x01\n\rCreateRuleSet\x126.google.cloud.contentwarehouse.v1.CreateRuleSetRequest\x1a).google.cloud.contentwarehouse.v1.RuleSet"P\xdaA\x0fparent,rule_set\x82\xd3\xe4\x93\x028",/v1/{parent=projects/*/locations/*}/ruleSets:\x08rule_set\x12\xa9\x01\n\nGetRuleSet\x123.google.cloud.contentwarehouse.v1.GetRuleSetRequest\x1a).google.cloud.contentwarehouse.v1.RuleSet";\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/locations/*/ruleSets/*}\x12\xbb\x01\n\rUpdateRuleSet\x126.google.cloud.contentwarehouse.v1.UpdateRuleSetRequest\x1a).google.cloud.contentwarehouse.v1.RuleSet"G\xdaA\rname,rule_set\x82\xd3\xe4\x93\x0212,/v1/{name=projects/*/locations/*/ruleSets/*}:\x01*\x12\x9c\x01\n\rDeleteRuleSet\x126.google.cloud.contentwarehouse.v1.DeleteRuleSetRequest\x1a\x16.google.protobuf.Empty";\xdaA\x04name\x82\xd3\xe4\x93\x02.*,/v1/{name=projects/*/locations/*/ruleSets/*}\x12\xbc\x01\n\x0cListRuleSets\x125.google.cloud.contentwarehouse.v1.ListRuleSetsRequest\x1a6.google.cloud.contentwarehouse.v1.ListRuleSetsResponse"=\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/ruleSets\x1aS\xcaA\x1fcontentwarehouse.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xfb\x01\n$com.google.cloud.contentwarehouse.v1B\x13RuleSetServiceProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.contentwarehouse.v1.ruleset_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.contentwarehouse.v1B\x13RuleSetServiceProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1'
    _globals['_RULESETSERVICE']._loaded_options = None
    _globals['_RULESETSERVICE']._serialized_options = b'\xcaA\x1fcontentwarehouse.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_RULESETSERVICE'].methods_by_name['CreateRuleSet']._loaded_options = None
    _globals['_RULESETSERVICE'].methods_by_name['CreateRuleSet']._serialized_options = b'\xdaA\x0fparent,rule_set\x82\xd3\xe4\x93\x028",/v1/{parent=projects/*/locations/*}/ruleSets:\x08rule_set'
    _globals['_RULESETSERVICE'].methods_by_name['GetRuleSet']._loaded_options = None
    _globals['_RULESETSERVICE'].methods_by_name['GetRuleSet']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/locations/*/ruleSets/*}'
    _globals['_RULESETSERVICE'].methods_by_name['UpdateRuleSet']._loaded_options = None
    _globals['_RULESETSERVICE'].methods_by_name['UpdateRuleSet']._serialized_options = b'\xdaA\rname,rule_set\x82\xd3\xe4\x93\x0212,/v1/{name=projects/*/locations/*/ruleSets/*}:\x01*'
    _globals['_RULESETSERVICE'].methods_by_name['DeleteRuleSet']._loaded_options = None
    _globals['_RULESETSERVICE'].methods_by_name['DeleteRuleSet']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02.*,/v1/{name=projects/*/locations/*/ruleSets/*}'
    _globals['_RULESETSERVICE'].methods_by_name['ListRuleSets']._loaded_options = None
    _globals['_RULESETSERVICE'].methods_by_name['ListRuleSets']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/ruleSets'
    _globals['_RULESETSERVICE']._serialized_start = 293
    _globals['_RULESETSERVICE']._serialized_end = 1305