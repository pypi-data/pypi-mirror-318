"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/shopping/merchant/accounts/v1beta/account_tax.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.shopping.merchant.accounts.v1beta import tax_rule_pb2 as google_dot_shopping_dot_merchant_dot_accounts_dot_v1beta_dot_tax__rule__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/shopping/merchant/accounts/v1beta/account_tax.proto\x12(google.shopping.merchant.accounts.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a7google/shopping/merchant/accounts/v1beta/tax_rule.proto"\xe6\x01\n\nAccountTax\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x14\n\x07account\x18\x02 \x01(\x03B\x03\xe0A\x03\x12D\n\ttax_rules\x18\x03 \x03(\x0b21.google.shopping.merchant.accounts.v1beta.TaxRule:i\xeaAf\n%merchantapi.googleapis.com/AccountTax\x12#accounts/{account}/accounttax/{tax}*\x0caccountTaxes2\naccountTax"S\n\x14GetAccountTaxRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%merchantapi.googleapis.com/AccountTax"\x9a\x01\n\x17UpdateAccountTaxRequest\x12N\n\x0baccount_tax\x18\x01 \x01(\x0b24.google.shopping.merchant.accounts.v1beta.AccountTaxB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"}\n\x15ListAccountTaxRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%merchantapi.googleapis.com/AccountTax\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"~\n\x16ListAccountTaxResponse\x12K\n\raccount_taxes\x18\x01 \x03(\x0b24.google.shopping.merchant.accounts.v1beta.AccountTax\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x84\x06\n\x11AccountTaxService\x12\xc5\x01\n\rGetAccountTax\x12>.google.shopping.merchant.accounts.v1beta.GetAccountTaxRequest\x1a4.google.shopping.merchant.accounts.v1beta.AccountTax">\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//accounts/v1beta/{name=accounts/*/accounttax/*}\x12\xd5\x01\n\x0eListAccountTax\x12?.google.shopping.merchant.accounts.v1beta.ListAccountTaxRequest\x1a@.google.shopping.merchant.accounts.v1beta.ListAccountTaxResponse"@\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//accounts/v1beta/{parent=accounts/*}/accounttax\x12\x85\x02\n\x10UpdateAccountTax\x12A.google.shopping.merchant.accounts.v1beta.UpdateAccountTaxRequest\x1a4.google.shopping.merchant.accounts.v1beta.AccountTax"x\xdaA\x17account_tax,update_mask\xdaA\x0baccount_tax\x82\xd3\xe4\x93\x02J2;/accounts/v1beta/{account_tax.name=accounts/*/accounttax/*}:\x0baccount_tax\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x91\x01\n,com.google.shopping.merchant.accounts.v1betaB\x0fAccountTaxProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1beta.account_tax_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.shopping.merchant.accounts.v1betaB\x0fAccountTaxProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspb'
    _globals['_ACCOUNTTAX'].fields_by_name['name']._loaded_options = None
    _globals['_ACCOUNTTAX'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ACCOUNTTAX'].fields_by_name['account']._loaded_options = None
    _globals['_ACCOUNTTAX'].fields_by_name['account']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTTAX']._loaded_options = None
    _globals['_ACCOUNTTAX']._serialized_options = b'\xeaAf\n%merchantapi.googleapis.com/AccountTax\x12#accounts/{account}/accounttax/{tax}*\x0caccountTaxes2\naccountTax'
    _globals['_GETACCOUNTTAXREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETACCOUNTTAXREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%merchantapi.googleapis.com/AccountTax"
    _globals['_UPDATEACCOUNTTAXREQUEST'].fields_by_name['account_tax']._loaded_options = None
    _globals['_UPDATEACCOUNTTAXREQUEST'].fields_by_name['account_tax']._serialized_options = b'\xe0A\x02'
    _globals['_LISTACCOUNTTAXREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTACCOUNTTAXREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%merchantapi.googleapis.com/AccountTax"
    _globals['_ACCOUNTTAXSERVICE']._loaded_options = None
    _globals['_ACCOUNTTAXSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_ACCOUNTTAXSERVICE'].methods_by_name['GetAccountTax']._loaded_options = None
    _globals['_ACCOUNTTAXSERVICE'].methods_by_name['GetAccountTax']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//accounts/v1beta/{name=accounts/*/accounttax/*}'
    _globals['_ACCOUNTTAXSERVICE'].methods_by_name['ListAccountTax']._loaded_options = None
    _globals['_ACCOUNTTAXSERVICE'].methods_by_name['ListAccountTax']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//accounts/v1beta/{parent=accounts/*}/accounttax'
    _globals['_ACCOUNTTAXSERVICE'].methods_by_name['UpdateAccountTax']._loaded_options = None
    _globals['_ACCOUNTTAXSERVICE'].methods_by_name['UpdateAccountTax']._serialized_options = b'\xdaA\x17account_tax,update_mask\xdaA\x0baccount_tax\x82\xd3\xe4\x93\x02J2;/accounts/v1beta/{account_tax.name=accounts/*/accounttax/*}:\x0baccount_tax'
    _globals['_ACCOUNTTAX']._serialized_start = 311
    _globals['_ACCOUNTTAX']._serialized_end = 541
    _globals['_GETACCOUNTTAXREQUEST']._serialized_start = 543
    _globals['_GETACCOUNTTAXREQUEST']._serialized_end = 626
    _globals['_UPDATEACCOUNTTAXREQUEST']._serialized_start = 629
    _globals['_UPDATEACCOUNTTAXREQUEST']._serialized_end = 783
    _globals['_LISTACCOUNTTAXREQUEST']._serialized_start = 785
    _globals['_LISTACCOUNTTAXREQUEST']._serialized_end = 910
    _globals['_LISTACCOUNTTAXRESPONSE']._serialized_start = 912
    _globals['_LISTACCOUNTTAXRESPONSE']._serialized_end = 1038
    _globals['_ACCOUNTTAXSERVICE']._serialized_start = 1041
    _globals['_ACCOUNTTAXSERVICE']._serialized_end = 1813