"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/contentwarehouse/v1/ruleset_service_request.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.contentwarehouse.v1 import rule_engine_pb2 as google_dot_cloud_dot_contentwarehouse_dot_v1_dot_rule__engine__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/contentwarehouse/v1/ruleset_service_request.proto\x12 google.cloud.contentwarehouse.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a2google/cloud/contentwarehouse/v1/rule_engine.proto"\x9a\x01\n\x14CreateRuleSetRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Location\x12@\n\x08rule_set\x18\x02 \x01(\x0b2).google.cloud.contentwarehouse.v1.RuleSetB\x03\xe0A\x02"R\n\x11GetRuleSetRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'contentwarehouse.googleapis.com/RuleSet"\x97\x01\n\x14UpdateRuleSetRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'contentwarehouse.googleapis.com/RuleSet\x12@\n\x08rule_set\x18\x02 \x01(\x0b2).google.cloud.contentwarehouse.v1.RuleSetB\x03\xe0A\x02"U\n\x14DeleteRuleSetRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'contentwarehouse.googleapis.com/RuleSet"~\n\x13ListRuleSetsRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"m\n\x14ListRuleSetsResponse\x12<\n\trule_sets\x18\x01 \x03(\x0b2).google.cloud.contentwarehouse.v1.RuleSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\tB\x82\x02\n$com.google.cloud.contentwarehouse.v1B\x1aRuleSetServiceRequestProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.contentwarehouse.v1.ruleset_service_request_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.contentwarehouse.v1B\x1aRuleSetServiceRequestProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1'
    _globals['_CREATERULESETREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATERULESETREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Location'
    _globals['_CREATERULESETREQUEST'].fields_by_name['rule_set']._loaded_options = None
    _globals['_CREATERULESETREQUEST'].fields_by_name['rule_set']._serialized_options = b'\xe0A\x02'
    _globals['_GETRULESETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETRULESETREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'contentwarehouse.googleapis.com/RuleSet"
    _globals['_UPDATERULESETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATERULESETREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'contentwarehouse.googleapis.com/RuleSet"
    _globals['_UPDATERULESETREQUEST'].fields_by_name['rule_set']._loaded_options = None
    _globals['_UPDATERULESETREQUEST'].fields_by_name['rule_set']._serialized_options = b'\xe0A\x02'
    _globals['_DELETERULESETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETERULESETREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'contentwarehouse.googleapis.com/RuleSet"
    _globals['_LISTRULESETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTRULESETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Location'
    _globals['_CREATERULESETREQUEST']._serialized_start = 213
    _globals['_CREATERULESETREQUEST']._serialized_end = 367
    _globals['_GETRULESETREQUEST']._serialized_start = 369
    _globals['_GETRULESETREQUEST']._serialized_end = 451
    _globals['_UPDATERULESETREQUEST']._serialized_start = 454
    _globals['_UPDATERULESETREQUEST']._serialized_end = 605
    _globals['_DELETERULESETREQUEST']._serialized_start = 607
    _globals['_DELETERULESETREQUEST']._serialized_end = 692
    _globals['_LISTRULESETSREQUEST']._serialized_start = 694
    _globals['_LISTRULESETSREQUEST']._serialized_end = 820
    _globals['_LISTRULESETSRESPONSE']._serialized_start = 822
    _globals['_LISTRULESETSRESPONSE']._serialized_end = 931