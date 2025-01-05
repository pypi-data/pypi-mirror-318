"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/channel/v1/billing_accounts.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/channel/v1/billing_accounts.proto\x12\x17google.cloud.channel.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8c\x02\n\x0eBillingAccount\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1a\n\rcurrency_code\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bregion_code\x18\x05 \x01(\tB\x03\xe0A\x03:e\xeaAb\n*cloudchannel.googleapis.com/BillingAccount\x124accounts/{account}/billingAccounts/{billing_account}Bl\n\x1bcom.google.cloud.channel.v1B\x14BillingAccountsProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.channel.v1.billing_accounts_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.channel.v1B\x14BillingAccountsProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpb'
    _globals['_BILLINGACCOUNT'].fields_by_name['name']._loaded_options = None
    _globals['_BILLINGACCOUNT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_BILLINGACCOUNT'].fields_by_name['create_time']._loaded_options = None
    _globals['_BILLINGACCOUNT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_BILLINGACCOUNT'].fields_by_name['currency_code']._loaded_options = None
    _globals['_BILLINGACCOUNT'].fields_by_name['currency_code']._serialized_options = b'\xe0A\x03'
    _globals['_BILLINGACCOUNT'].fields_by_name['region_code']._loaded_options = None
    _globals['_BILLINGACCOUNT'].fields_by_name['region_code']._serialized_options = b'\xe0A\x03'
    _globals['_BILLINGACCOUNT']._loaded_options = None
    _globals['_BILLINGACCOUNT']._serialized_options = b'\xeaAb\n*cloudchannel.googleapis.com/BillingAccount\x124accounts/{account}/billingAccounts/{billing_account}'
    _globals['_BILLINGACCOUNT']._serialized_start = 169
    _globals['_BILLINGACCOUNT']._serialized_end = 437