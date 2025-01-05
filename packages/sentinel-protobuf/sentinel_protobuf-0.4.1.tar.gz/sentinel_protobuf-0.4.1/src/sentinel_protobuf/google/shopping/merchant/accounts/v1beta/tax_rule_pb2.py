"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/shopping/merchant/accounts/v1beta/tax_rule.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.type import interval_pb2 as google_dot_type_dot_interval__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/shopping/merchant/accounts/v1beta/tax_rule.proto\x12(google.shopping.merchant.accounts.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1agoogle/type/interval.proto"\x81\x03\n\x07TaxRule\x12\x15\n\x0blocation_id\x18\x02 \x01(\x03H\x00\x12_\n\x0fpost_code_range\x18\x03 \x01(\x0b2D.google.shopping.merchant.accounts.v1beta.TaxRule.TaxPostalCodeRangeH\x00\x12\x19\n\x0fuse_google_rate\x18\x04 \x01(\x08H\x01\x12$\n\x1aself_specified_rate_micros\x18\x05 \x01(\x03H\x01\x12\x13\n\x0bregion_code\x18\x01 \x01(\t\x12\x16\n\x0eshipping_taxed\x18\x06 \x01(\x08\x129\n\x15effective_time_period\x18\x07 \x01(\x0b2\x15.google.type.IntervalB\x03\xe0A\x02\x1a5\n\x12TaxPostalCodeRange\x12\x12\n\x05start\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x0b\n\x03end\x18\x02 \x01(\tB\n\n\x08locationB\x12\n\x10rate_calculationB\x8e\x01\n,com.google.shopping.merchant.accounts.v1betaB\x0cTaxRuleProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1beta.tax_rule_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.shopping.merchant.accounts.v1betaB\x0cTaxRuleProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspb'
    _globals['_TAXRULE_TAXPOSTALCODERANGE'].fields_by_name['start']._loaded_options = None
    _globals['_TAXRULE_TAXPOSTALCODERANGE'].fields_by_name['start']._serialized_options = b'\xe0A\x02'
    _globals['_TAXRULE'].fields_by_name['effective_time_period']._loaded_options = None
    _globals['_TAXRULE'].fields_by_name['effective_time_period']._serialized_options = b'\xe0A\x02'
    _globals['_TAXRULE']._serialized_start = 163
    _globals['_TAXRULE']._serialized_end = 548
    _globals['_TAXRULE_TAXPOSTALCODERANGE']._serialized_start = 463
    _globals['_TAXRULE_TAXPOSTALCODERANGE']._serialized_end = 516