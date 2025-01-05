"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/channel/v1/repricing.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import date_pb2 as google_dot_type_dot_date__pb2
from .....google.type import decimal_pb2 as google_dot_type_dot_decimal__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/channel/v1/repricing.proto\x12\x17google.cloud.channel.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x16google/type/date.proto\x1a\x19google/type/decimal.proto"\xc5\x02\n\x17CustomerRepricingConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12G\n\x10repricing_config\x18\x02 \x01(\x0b2(.google.cloud.channel.v1.RepricingConfigB\x03\xe0A\x02\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:\x97\x01\xeaA\x93\x01\n3cloudchannel.googleapis.com/CustomerRepricingConfig\x12\\accounts/{account}/customers/{customer}/customerRepricingConfigs/{customer_repricing_config}"\xef\x02\n\x1dChannelPartnerRepricingConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12G\n\x10repricing_config\x18\x02 \x01(\x0b2(.google.cloud.channel.v1.RepricingConfigB\x03\xe0A\x02\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:\xbb\x01\xeaA\xb7\x01\n9cloudchannel.googleapis.com/ChannelPartnerRepricingConfig\x12zaccounts/{account}/channelPartnerLinks/{channel_partner}/channelPartnerRepricingConfigs/{channel_partner_repricing_config}"\x85\x05\n\x0fRepricingConfig\x12b\n\x17entitlement_granularity\x18\x04 \x01(\x0b2?.google.cloud.channel.v1.RepricingConfig.EntitlementGranularityH\x00\x12m\n\x1bchannel_partner_granularity\x18\x05 \x01(\x0b2B.google.cloud.channel.v1.RepricingConfig.ChannelPartnerGranularityB\x02\x18\x01H\x00\x127\n\x17effective_invoice_month\x18\x01 \x01(\x0b2\x11.google.type.DateB\x03\xe0A\x02\x12E\n\nadjustment\x18\x02 \x01(\x0b2,.google.cloud.channel.v1.RepricingAdjustmentB\x03\xe0A\x02\x12E\n\x0frebilling_basis\x18\x03 \x01(\x0e2\'.google.cloud.channel.v1.RebillingBasisB\x03\xe0A\x02\x12K\n\x15conditional_overrides\x18\x06 \x03(\x0b2,.google.cloud.channel.v1.ConditionalOverride\x1a[\n\x16EntitlementGranularity\x12A\n\x0bentitlement\x18\x01 \x01(\tB,\xfaA)\n\'cloudchannel.googleapis.com/Entitlement\x1a\x1f\n\x19ChannelPartnerGranularity:\x02\x18\x01B\r\n\x0bgranularity"s\n\x13RepricingAdjustment\x12N\n\x15percentage_adjustment\x18\x02 \x01(\x0b2-.google.cloud.channel.v1.PercentageAdjustmentH\x00B\x0c\n\nadjustment"@\n\x14PercentageAdjustment\x12(\n\npercentage\x18\x02 \x01(\x0b2\x14.google.type.Decimal"\xf2\x01\n\x13ConditionalOverride\x12E\n\nadjustment\x18\x01 \x01(\x0b2,.google.cloud.channel.v1.RepricingAdjustmentB\x03\xe0A\x02\x12E\n\x0frebilling_basis\x18\x02 \x01(\x0e2\'.google.cloud.channel.v1.RebillingBasisB\x03\xe0A\x02\x12M\n\x13repricing_condition\x18\x03 \x01(\x0b2+.google.cloud.channel.v1.RepricingConditionB\x03\xe0A\x02"l\n\x12RepricingCondition\x12I\n\x13sku_group_condition\x18\x01 \x01(\x0b2*.google.cloud.channel.v1.SkuGroupConditionH\x00B\x0b\n\tcondition"&\n\x11SkuGroupCondition\x12\x11\n\tsku_group\x18\x01 \x01(\t*]\n\x0eRebillingBasis\x12\x1f\n\x1bREBILLING_BASIS_UNSPECIFIED\x10\x00\x12\x10\n\x0cCOST_AT_LIST\x10\x01\x12\x18\n\x14DIRECT_CUSTOMER_COST\x10\x02Bf\n\x1bcom.google.cloud.channel.v1B\x0eRepricingProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.channel.v1.repricing_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.channel.v1B\x0eRepricingProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpb'
    _globals['_CUSTOMERREPRICINGCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_CUSTOMERREPRICINGCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERREPRICINGCONFIG'].fields_by_name['repricing_config']._loaded_options = None
    _globals['_CUSTOMERREPRICINGCONFIG'].fields_by_name['repricing_config']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMERREPRICINGCONFIG'].fields_by_name['update_time']._loaded_options = None
    _globals['_CUSTOMERREPRICINGCONFIG'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERREPRICINGCONFIG']._loaded_options = None
    _globals['_CUSTOMERREPRICINGCONFIG']._serialized_options = b'\xeaA\x93\x01\n3cloudchannel.googleapis.com/CustomerRepricingConfig\x12\\accounts/{account}/customers/{customer}/customerRepricingConfigs/{customer_repricing_config}'
    _globals['_CHANNELPARTNERREPRICINGCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_CHANNELPARTNERREPRICINGCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNELPARTNERREPRICINGCONFIG'].fields_by_name['repricing_config']._loaded_options = None
    _globals['_CHANNELPARTNERREPRICINGCONFIG'].fields_by_name['repricing_config']._serialized_options = b'\xe0A\x02'
    _globals['_CHANNELPARTNERREPRICINGCONFIG'].fields_by_name['update_time']._loaded_options = None
    _globals['_CHANNELPARTNERREPRICINGCONFIG'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNELPARTNERREPRICINGCONFIG']._loaded_options = None
    _globals['_CHANNELPARTNERREPRICINGCONFIG']._serialized_options = b'\xeaA\xb7\x01\n9cloudchannel.googleapis.com/ChannelPartnerRepricingConfig\x12zaccounts/{account}/channelPartnerLinks/{channel_partner}/channelPartnerRepricingConfigs/{channel_partner_repricing_config}'
    _globals['_REPRICINGCONFIG_ENTITLEMENTGRANULARITY'].fields_by_name['entitlement']._loaded_options = None
    _globals['_REPRICINGCONFIG_ENTITLEMENTGRANULARITY'].fields_by_name['entitlement']._serialized_options = b"\xfaA)\n'cloudchannel.googleapis.com/Entitlement"
    _globals['_REPRICINGCONFIG_CHANNELPARTNERGRANULARITY']._loaded_options = None
    _globals['_REPRICINGCONFIG_CHANNELPARTNERGRANULARITY']._serialized_options = b'\x18\x01'
    _globals['_REPRICINGCONFIG'].fields_by_name['channel_partner_granularity']._loaded_options = None
    _globals['_REPRICINGCONFIG'].fields_by_name['channel_partner_granularity']._serialized_options = b'\x18\x01'
    _globals['_REPRICINGCONFIG'].fields_by_name['effective_invoice_month']._loaded_options = None
    _globals['_REPRICINGCONFIG'].fields_by_name['effective_invoice_month']._serialized_options = b'\xe0A\x02'
    _globals['_REPRICINGCONFIG'].fields_by_name['adjustment']._loaded_options = None
    _globals['_REPRICINGCONFIG'].fields_by_name['adjustment']._serialized_options = b'\xe0A\x02'
    _globals['_REPRICINGCONFIG'].fields_by_name['rebilling_basis']._loaded_options = None
    _globals['_REPRICINGCONFIG'].fields_by_name['rebilling_basis']._serialized_options = b'\xe0A\x02'
    _globals['_CONDITIONALOVERRIDE'].fields_by_name['adjustment']._loaded_options = None
    _globals['_CONDITIONALOVERRIDE'].fields_by_name['adjustment']._serialized_options = b'\xe0A\x02'
    _globals['_CONDITIONALOVERRIDE'].fields_by_name['rebilling_basis']._loaded_options = None
    _globals['_CONDITIONALOVERRIDE'].fields_by_name['rebilling_basis']._serialized_options = b'\xe0A\x02'
    _globals['_CONDITIONALOVERRIDE'].fields_by_name['repricing_condition']._loaded_options = None
    _globals['_CONDITIONALOVERRIDE'].fields_by_name['repricing_condition']._serialized_options = b'\xe0A\x02'
    _globals['_REBILLINGBASIS']._serialized_start = 2136
    _globals['_REBILLINGBASIS']._serialized_end = 2229
    _globals['_CUSTOMERREPRICINGCONFIG']._serialized_start = 213
    _globals['_CUSTOMERREPRICINGCONFIG']._serialized_end = 538
    _globals['_CHANNELPARTNERREPRICINGCONFIG']._serialized_start = 541
    _globals['_CHANNELPARTNERREPRICINGCONFIG']._serialized_end = 908
    _globals['_REPRICINGCONFIG']._serialized_start = 911
    _globals['_REPRICINGCONFIG']._serialized_end = 1556
    _globals['_REPRICINGCONFIG_ENTITLEMENTGRANULARITY']._serialized_start = 1417
    _globals['_REPRICINGCONFIG_ENTITLEMENTGRANULARITY']._serialized_end = 1508
    _globals['_REPRICINGCONFIG_CHANNELPARTNERGRANULARITY']._serialized_start = 1510
    _globals['_REPRICINGCONFIG_CHANNELPARTNERGRANULARITY']._serialized_end = 1541
    _globals['_REPRICINGADJUSTMENT']._serialized_start = 1558
    _globals['_REPRICINGADJUSTMENT']._serialized_end = 1673
    _globals['_PERCENTAGEADJUSTMENT']._serialized_start = 1675
    _globals['_PERCENTAGEADJUSTMENT']._serialized_end = 1739
    _globals['_CONDITIONALOVERRIDE']._serialized_start = 1742
    _globals['_CONDITIONALOVERRIDE']._serialized_end = 1984
    _globals['_REPRICINGCONDITION']._serialized_start = 1986
    _globals['_REPRICINGCONDITION']._serialized_end = 2094
    _globals['_SKUGROUPCONDITION']._serialized_start = 2096
    _globals['_SKUGROUPCONDITION']._serialized_end = 2134