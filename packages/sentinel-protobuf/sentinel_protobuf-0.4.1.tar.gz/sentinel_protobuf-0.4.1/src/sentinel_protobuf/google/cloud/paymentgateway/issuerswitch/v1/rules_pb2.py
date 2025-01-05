"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/paymentgateway/issuerswitch/v1/rules.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.paymentgateway.issuerswitch.v1 import common_fields_pb2 as google_dot_cloud_dot_paymentgateway_dot_issuerswitch_dot_v1_dot_common__fields__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/paymentgateway/issuerswitch/v1/rules.proto\x12+google.cloud.paymentgateway.issuerswitch.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a?google/cloud/paymentgateway/issuerswitch/v1/common_fields.proto\x1a\x1bgoogle/protobuf/empty.proto"\x96\x02\n\x04Rule\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10rule_description\x18\x02 \x01(\t\x12F\n\x08api_type\x18\x03 \x01(\x0e24.google.cloud.paymentgateway.issuerswitch.v1.ApiType\x12V\n\x10transaction_type\x18\x04 \x01(\x0e2<.google.cloud.paymentgateway.issuerswitch.v1.TransactionType:F\xeaAC\n issuerswitch.googleapis.com/Rule\x12\x1fprojects/{project}/rules/{rule}"\x8b\x02\n\x0cRuleMetadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12L\n\x04type\x18\x03 \x01(\x0e2>.google.cloud.paymentgateway.issuerswitch.v1.RuleMetadata.Type"&\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04LIST\x10\x01:b\xeaA_\n(issuerswitch.googleapis.com/RuleMetadata\x123projects/{project}/rules/{rule}/metadata/{metadata}"\x91\x02\n\x11RuleMetadataValue\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x0c\n\x02id\x18\x02 \x01(\tH\x00\x12Z\n\x11account_reference\x18\x03 \x01(\x0b2=.google.cloud.paymentgateway.issuerswitch.v1.AccountReferenceH\x00:v\xeaAs\n-issuerswitch.googleapis.com/RuleMetadataValue\x12Bprojects/{project}/rules/{rule}/metadata/{metadata}/values/{value}B\x07\n\x05value"s\n\x10ListRulesRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 issuerswitch.googleapis.com/Rule\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x82\x01\n\x11ListRulesResponse\x12@\n\x05rules\x18\x01 \x03(\x0b21.google.cloud.paymentgateway.issuerswitch.v1.Rule\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x03"\x82\x01\n\x17ListRuleMetadataRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(issuerswitch.googleapis.com/RuleMetadata\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x99\x01\n\x18ListRuleMetadataResponse\x12P\n\rrule_metadata\x18\x01 \x03(\x0b29.google.cloud.paymentgateway.issuerswitch.v1.RuleMetadata\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x03"\x8d\x01\n\x1dListRuleMetadataValuesRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\x12-issuerswitch.googleapis.com/RuleMetadataValue\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x97\x01\n\x1eListRuleMetadataValuesResponse\x12\\\n\x14rule_metadata_values\x18\x01 \x03(\x0b2>.google.cloud.paymentgateway.issuerswitch.v1.RuleMetadataValue\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xce\x01\n$BatchCreateRuleMetadataValuesRequest\x12B\n\x06parent\x18\x01 \x01(\tB2\xfaA/\x12-issuerswitch.googleapis.com/RuleMetadataValue\x12b\n\x08requests\x18\x02 \x03(\x0b2K.google.cloud.paymentgateway.issuerswitch.v1.CreateRuleMetadataValueRequestB\x03\xe0A\x02"\x84\x01\n%BatchCreateRuleMetadataValuesResponse\x12[\n\x13rule_metadata_value\x18\x01 \x03(\x0b2>.google.cloud.paymentgateway.issuerswitch.v1.RuleMetadataValue"\xc9\x01\n\x1eCreateRuleMetadataValueRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\x12-issuerswitch.googleapis.com/RuleMetadataValue\x12`\n\x13rule_metadata_value\x18\x02 \x01(\x0b2>.google.cloud.paymentgateway.issuerswitch.v1.RuleMetadataValueB\x03\xe0A\x02"\xb0\x01\n$BatchDeleteRuleMetadataValuesRequest\x12B\n\x06parent\x18\x01 \x01(\tB2\xfaA/\x12-issuerswitch.googleapis.com/RuleMetadataValue\x12D\n\x05names\x18\x02 \x03(\tB5\xe0A\x02\xfaA/\n-issuerswitch.googleapis.com/RuleMetadataValue2\xf2\t\n\x11IssuerSwitchRules\x12\xba\x01\n\tListRules\x12=.google.cloud.paymentgateway.issuerswitch.v1.ListRulesRequest\x1a>.google.cloud.paymentgateway.issuerswitch.v1.ListRulesResponse".\xdaA\x06parent\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1/{parent=projects/*}/rules\x12\xda\x01\n\x10ListRuleMetadata\x12D.google.cloud.paymentgateway.issuerswitch.v1.ListRuleMetadataRequest\x1aE.google.cloud.paymentgateway.issuerswitch.v1.ListRuleMetadataResponse"9\xdaA\x06parent\x82\xd3\xe4\x93\x02*\x12(/v1/{parent=projects/*/rules/*}/metadata\x12\xf5\x01\n\x16ListRuleMetadataValues\x12J.google.cloud.paymentgateway.issuerswitch.v1.ListRuleMetadataValuesRequest\x1aK.google.cloud.paymentgateway.issuerswitch.v1.ListRuleMetadataValuesResponse"B\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1/{parent=projects/*/rules/*/metadata/*}/values\x12\x99\x02\n\x1dBatchCreateRuleMetadataValues\x12Q.google.cloud.paymentgateway.issuerswitch.v1.BatchCreateRuleMetadataValuesRequest\x1aR.google.cloud.paymentgateway.issuerswitch.v1.BatchCreateRuleMetadataValuesResponse"Q\xdaA\x06parent\x82\xd3\xe4\x93\x02B"=/v1/{parent=projects/*/rules/*/metadata/*}/values:batchCreate:\x01*\x12\xdd\x01\n\x1dBatchDeleteRuleMetadataValues\x12Q.google.cloud.paymentgateway.issuerswitch.v1.BatchDeleteRuleMetadataValuesRequest\x1a\x16.google.protobuf.Empty"Q\xdaA\x06parent\x82\xd3\xe4\x93\x02B"=/v1/{parent=projects/*/rules/*/metadata/*}/values:batchDelete:\x01*\x1aO\xcaA\x1bissuerswitch.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa2\x02\n/com.google.cloud.paymentgateway.issuerswitch.v1B\nRulesProtoP\x01ZScloud.google.com/go/paymentgateway/issuerswitch/apiv1/issuerswitchpb;issuerswitchpb\xaa\x02+Google.Cloud.PaymentGateway.IssuerSwitch.V1\xca\x02+Google\\Cloud\\PaymentGateway\\IssuerSwitch\\V1\xea\x02/Google::Cloud::PaymentGateway::IssuerSwitch::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.paymentgateway.issuerswitch.v1.rules_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.cloud.paymentgateway.issuerswitch.v1B\nRulesProtoP\x01ZScloud.google.com/go/paymentgateway/issuerswitch/apiv1/issuerswitchpb;issuerswitchpb\xaa\x02+Google.Cloud.PaymentGateway.IssuerSwitch.V1\xca\x02+Google\\Cloud\\PaymentGateway\\IssuerSwitch\\V1\xea\x02/Google::Cloud::PaymentGateway::IssuerSwitch::V1'
    _globals['_RULE']._loaded_options = None
    _globals['_RULE']._serialized_options = b'\xeaAC\n issuerswitch.googleapis.com/Rule\x12\x1fprojects/{project}/rules/{rule}'
    _globals['_RULEMETADATA']._loaded_options = None
    _globals['_RULEMETADATA']._serialized_options = b'\xeaA_\n(issuerswitch.googleapis.com/RuleMetadata\x123projects/{project}/rules/{rule}/metadata/{metadata}'
    _globals['_RULEMETADATAVALUE'].fields_by_name['name']._loaded_options = None
    _globals['_RULEMETADATAVALUE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_RULEMETADATAVALUE']._loaded_options = None
    _globals['_RULEMETADATAVALUE']._serialized_options = b'\xeaAs\n-issuerswitch.googleapis.com/RuleMetadataValue\x12Bprojects/{project}/rules/{rule}/metadata/{metadata}/values/{value}'
    _globals['_LISTRULESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTRULESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 issuerswitch.googleapis.com/Rule'
    _globals['_LISTRULEMETADATAREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTRULEMETADATAREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(issuerswitch.googleapis.com/RuleMetadata'
    _globals['_LISTRULEMETADATAVALUESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTRULEMETADATAVALUESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\x12-issuerswitch.googleapis.com/RuleMetadataValue'
    _globals['_BATCHCREATERULEMETADATAVALUESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHCREATERULEMETADATAVALUESREQUEST'].fields_by_name['parent']._serialized_options = b'\xfaA/\x12-issuerswitch.googleapis.com/RuleMetadataValue'
    _globals['_BATCHCREATERULEMETADATAVALUESREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_BATCHCREATERULEMETADATAVALUESREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_CREATERULEMETADATAVALUEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATERULEMETADATAVALUEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\x12-issuerswitch.googleapis.com/RuleMetadataValue'
    _globals['_CREATERULEMETADATAVALUEREQUEST'].fields_by_name['rule_metadata_value']._loaded_options = None
    _globals['_CREATERULEMETADATAVALUEREQUEST'].fields_by_name['rule_metadata_value']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHDELETERULEMETADATAVALUESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHDELETERULEMETADATAVALUESREQUEST'].fields_by_name['parent']._serialized_options = b'\xfaA/\x12-issuerswitch.googleapis.com/RuleMetadataValue'
    _globals['_BATCHDELETERULEMETADATAVALUESREQUEST'].fields_by_name['names']._loaded_options = None
    _globals['_BATCHDELETERULEMETADATAVALUESREQUEST'].fields_by_name['names']._serialized_options = b'\xe0A\x02\xfaA/\n-issuerswitch.googleapis.com/RuleMetadataValue'
    _globals['_ISSUERSWITCHRULES']._loaded_options = None
    _globals['_ISSUERSWITCHRULES']._serialized_options = b'\xcaA\x1bissuerswitch.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ISSUERSWITCHRULES'].methods_by_name['ListRules']._loaded_options = None
    _globals['_ISSUERSWITCHRULES'].methods_by_name['ListRules']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1/{parent=projects/*}/rules'
    _globals['_ISSUERSWITCHRULES'].methods_by_name['ListRuleMetadata']._loaded_options = None
    _globals['_ISSUERSWITCHRULES'].methods_by_name['ListRuleMetadata']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02*\x12(/v1/{parent=projects/*/rules/*}/metadata'
    _globals['_ISSUERSWITCHRULES'].methods_by_name['ListRuleMetadataValues']._loaded_options = None
    _globals['_ISSUERSWITCHRULES'].methods_by_name['ListRuleMetadataValues']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1/{parent=projects/*/rules/*/metadata/*}/values'
    _globals['_ISSUERSWITCHRULES'].methods_by_name['BatchCreateRuleMetadataValues']._loaded_options = None
    _globals['_ISSUERSWITCHRULES'].methods_by_name['BatchCreateRuleMetadataValues']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02B"=/v1/{parent=projects/*/rules/*/metadata/*}/values:batchCreate:\x01*'
    _globals['_ISSUERSWITCHRULES'].methods_by_name['BatchDeleteRuleMetadataValues']._loaded_options = None
    _globals['_ISSUERSWITCHRULES'].methods_by_name['BatchDeleteRuleMetadataValues']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02B"=/v1/{parent=projects/*/rules/*/metadata/*}/values:batchDelete:\x01*'
    _globals['_RULE']._serialized_start = 314
    _globals['_RULE']._serialized_end = 592
    _globals['_RULEMETADATA']._serialized_start = 595
    _globals['_RULEMETADATA']._serialized_end = 862
    _globals['_RULEMETADATA_TYPE']._serialized_start = 724
    _globals['_RULEMETADATA_TYPE']._serialized_end = 762
    _globals['_RULEMETADATAVALUE']._serialized_start = 865
    _globals['_RULEMETADATAVALUE']._serialized_end = 1138
    _globals['_LISTRULESREQUEST']._serialized_start = 1140
    _globals['_LISTRULESREQUEST']._serialized_end = 1255
    _globals['_LISTRULESRESPONSE']._serialized_start = 1258
    _globals['_LISTRULESRESPONSE']._serialized_end = 1388
    _globals['_LISTRULEMETADATAREQUEST']._serialized_start = 1391
    _globals['_LISTRULEMETADATAREQUEST']._serialized_end = 1521
    _globals['_LISTRULEMETADATARESPONSE']._serialized_start = 1524
    _globals['_LISTRULEMETADATARESPONSE']._serialized_end = 1677
    _globals['_LISTRULEMETADATAVALUESREQUEST']._serialized_start = 1680
    _globals['_LISTRULEMETADATAVALUESREQUEST']._serialized_end = 1821
    _globals['_LISTRULEMETADATAVALUESRESPONSE']._serialized_start = 1824
    _globals['_LISTRULEMETADATAVALUESRESPONSE']._serialized_end = 1975
    _globals['_BATCHCREATERULEMETADATAVALUESREQUEST']._serialized_start = 1978
    _globals['_BATCHCREATERULEMETADATAVALUESREQUEST']._serialized_end = 2184
    _globals['_BATCHCREATERULEMETADATAVALUESRESPONSE']._serialized_start = 2187
    _globals['_BATCHCREATERULEMETADATAVALUESRESPONSE']._serialized_end = 2319
    _globals['_CREATERULEMETADATAVALUEREQUEST']._serialized_start = 2322
    _globals['_CREATERULEMETADATAVALUEREQUEST']._serialized_end = 2523
    _globals['_BATCHDELETERULEMETADATAVALUESREQUEST']._serialized_start = 2526
    _globals['_BATCHDELETERULEMETADATAVALUESREQUEST']._serialized_end = 2702
    _globals['_ISSUERSWITCHRULES']._serialized_start = 2705
    _globals['_ISSUERSWITCHRULES']._serialized_end = 3971