"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/channel/v1/offers.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.channel.v1 import common_pb2 as google_dot_cloud_dot_channel_dot_v1_dot_common__pb2
from .....google.cloud.channel.v1 import products_pb2 as google_dot_cloud_dot_channel_dot_v1_dot_products__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import money_pb2 as google_dot_type_dot_money__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/cloud/channel/v1/offers.proto\x12\x17google.cloud.channel.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a$google/cloud/channel/v1/common.proto\x1a&google/cloud/channel/v1/products.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/type/money.proto"\xbc\x04\n\x05Offer\x12\x0c\n\x04name\x18\x01 \x01(\t\x12>\n\x0emarketing_info\x18\x02 \x01(\x0b2&.google.cloud.channel.v1.MarketingInfo\x12)\n\x03sku\x18\x03 \x01(\x0b2\x1c.google.cloud.channel.v1.Sku\x12+\n\x04plan\x18\x04 \x01(\x0b2\x1d.google.cloud.channel.v1.Plan\x129\n\x0bconstraints\x18\x05 \x01(\x0b2$.google.cloud.channel.v1.Constraints\x12D\n\x12price_by_resources\x18\x06 \x03(\x0b2(.google.cloud.channel.v1.PriceByResource\x12.\n\nstart_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x121\n\x08end_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12K\n\x15parameter_definitions\x18\t \x03(\x0b2,.google.cloud.channel.v1.ParameterDefinition\x12\x11\n\tdeal_code\x18\x0c \x01(\t:I\xeaAF\n!cloudchannel.googleapis.com/Offer\x12!accounts/{account}/offers/{offer}"\x88\x03\n\x13ParameterDefinition\x12\x0c\n\x04name\x18\x01 \x01(\t\x12R\n\x0eparameter_type\x18\x02 \x01(\x0e2:.google.cloud.channel.v1.ParameterDefinition.ParameterType\x121\n\tmin_value\x18\x03 \x01(\x0b2\x1e.google.cloud.channel.v1.Value\x121\n\tmax_value\x18\x04 \x01(\x0b2\x1e.google.cloud.channel.v1.Value\x126\n\x0eallowed_values\x18\x05 \x03(\x0b2\x1e.google.cloud.channel.v1.Value\x12\x10\n\x08optional\x18\x06 \x01(\x08"_\n\rParameterType\x12\x1e\n\x1aPARAMETER_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05INT64\x10\x01\x12\n\n\x06STRING\x10\x02\x12\n\n\x06DOUBLE\x10\x03\x12\x0b\n\x07BOOLEAN\x10\x04"Y\n\x0bConstraints\x12J\n\x14customer_constraints\x18\x01 \x01(\x0b2,.google.cloud.channel.v1.CustomerConstraints"\xd7\x01\n\x13CustomerConstraints\x12\x17\n\x0fallowed_regions\x18\x01 \x03(\t\x12W\n\x16allowed_customer_types\x18\x02 \x03(\x0e27.google.cloud.channel.v1.CloudIdentityInfo.CustomerType\x12N\n\x17promotional_order_types\x18\x03 \x03(\x0e2-.google.cloud.channel.v1.PromotionalOrderType"\x86\x02\n\x04Plan\x12:\n\x0cpayment_plan\x18\x01 \x01(\x0e2$.google.cloud.channel.v1.PaymentPlan\x12:\n\x0cpayment_type\x18\x02 \x01(\x0e2$.google.cloud.channel.v1.PaymentType\x126\n\rpayment_cycle\x18\x03 \x01(\x0b2\x1f.google.cloud.channel.v1.Period\x125\n\x0ctrial_period\x18\x04 \x01(\x0b2\x1f.google.cloud.channel.v1.Period\x12\x17\n\x0fbilling_account\x18\x05 \x01(\t"\xb9\x01\n\x0fPriceByResource\x12<\n\rresource_type\x18\x01 \x01(\x0e2%.google.cloud.channel.v1.ResourceType\x12-\n\x05price\x18\x02 \x01(\x0b2\x1e.google.cloud.channel.v1.Price\x129\n\x0cprice_phases\x18\x03 \x03(\x0b2#.google.cloud.channel.v1.PricePhase"\x8a\x01\n\x05Price\x12&\n\nbase_price\x18\x01 \x01(\x0b2\x12.google.type.Money\x12\x10\n\x08discount\x18\x02 \x01(\x01\x12+\n\x0feffective_price\x18\x03 \x01(\x0b2\x12.google.type.Money\x12\x1a\n\x12external_price_uri\x18\x04 \x01(\t"\xd9\x01\n\nPricePhase\x128\n\x0bperiod_type\x18\x01 \x01(\x0e2#.google.cloud.channel.v1.PeriodType\x12\x14\n\x0cfirst_period\x18\x02 \x01(\x05\x12\x13\n\x0blast_period\x18\x03 \x01(\x05\x12-\n\x05price\x18\x04 \x01(\x0b2\x1e.google.cloud.channel.v1.Price\x127\n\x0bprice_tiers\x18\x05 \x03(\x0b2".google.cloud.channel.v1.PriceTier"i\n\tPriceTier\x12\x16\n\x0efirst_resource\x18\x01 \x01(\x05\x12\x15\n\rlast_resource\x18\x02 \x01(\x05\x12-\n\x05price\x18\x03 \x01(\x0b2\x1e.google.cloud.channel.v1.Price"T\n\x06Period\x12\x10\n\x08duration\x18\x01 \x01(\x05\x128\n\x0bperiod_type\x18\x02 \x01(\x0e2#.google.cloud.channel.v1.PeriodType*m\n\x14PromotionalOrderType\x12 \n\x1cPROMOTIONAL_TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bNEW_UPGRADE\x10\x01\x12\x0c\n\x08TRANSFER\x10\x02\x12\x14\n\x10PROMOTION_SWITCH\x10\x03*k\n\x0bPaymentPlan\x12\x1c\n\x18PAYMENT_PLAN_UNSPECIFIED\x10\x00\x12\x0e\n\nCOMMITMENT\x10\x01\x12\x0c\n\x08FLEXIBLE\x10\x02\x12\x08\n\x04FREE\x10\x03\x12\t\n\x05TRIAL\x10\x04\x12\x0b\n\x07OFFLINE\x10\x05*D\n\x0bPaymentType\x12\x1c\n\x18PAYMENT_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06PREPAY\x10\x01\x12\x0b\n\x07POSTPAY\x10\x02*\x8a\x01\n\x0cResourceType\x12\x1d\n\x19RESOURCE_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04SEAT\x10\x01\x12\x07\n\x03MAU\x10\x02\x12\x06\n\x02GB\x10\x03\x12\x11\n\rLICENSED_USER\x10\x04\x12\x0b\n\x07MINUTES\x10\x05\x12\x0e\n\nIAAS_USAGE\x10\x06\x12\x10\n\x0cSUBSCRIPTION\x10\x07*G\n\nPeriodType\x12\x1b\n\x17PERIOD_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03DAY\x10\x01\x12\t\n\x05MONTH\x10\x02\x12\x08\n\x04YEAR\x10\x03Bc\n\x1bcom.google.cloud.channel.v1B\x0bOffersProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.channel.v1.offers_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.channel.v1B\x0bOffersProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpb'
    _globals['_OFFER'].fields_by_name['end_time']._loaded_options = None
    _globals['_OFFER'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OFFER']._loaded_options = None
    _globals['_OFFER']._serialized_options = b'\xeaAF\n!cloudchannel.googleapis.com/Offer\x12!accounts/{account}/offers/{offer}'
    _globals['_PROMOTIONALORDERTYPE']._serialized_start = 2547
    _globals['_PROMOTIONALORDERTYPE']._serialized_end = 2656
    _globals['_PAYMENTPLAN']._serialized_start = 2658
    _globals['_PAYMENTPLAN']._serialized_end = 2765
    _globals['_PAYMENTTYPE']._serialized_start = 2767
    _globals['_PAYMENTTYPE']._serialized_end = 2835
    _globals['_RESOURCETYPE']._serialized_start = 2838
    _globals['_RESOURCETYPE']._serialized_end = 2976
    _globals['_PERIODTYPE']._serialized_start = 2978
    _globals['_PERIODTYPE']._serialized_end = 3049
    _globals['_OFFER']._serialized_start = 262
    _globals['_OFFER']._serialized_end = 834
    _globals['_PARAMETERDEFINITION']._serialized_start = 837
    _globals['_PARAMETERDEFINITION']._serialized_end = 1229
    _globals['_PARAMETERDEFINITION_PARAMETERTYPE']._serialized_start = 1134
    _globals['_PARAMETERDEFINITION_PARAMETERTYPE']._serialized_end = 1229
    _globals['_CONSTRAINTS']._serialized_start = 1231
    _globals['_CONSTRAINTS']._serialized_end = 1320
    _globals['_CUSTOMERCONSTRAINTS']._serialized_start = 1323
    _globals['_CUSTOMERCONSTRAINTS']._serialized_end = 1538
    _globals['_PLAN']._serialized_start = 1541
    _globals['_PLAN']._serialized_end = 1803
    _globals['_PRICEBYRESOURCE']._serialized_start = 1806
    _globals['_PRICEBYRESOURCE']._serialized_end = 1991
    _globals['_PRICE']._serialized_start = 1994
    _globals['_PRICE']._serialized_end = 2132
    _globals['_PRICEPHASE']._serialized_start = 2135
    _globals['_PRICEPHASE']._serialized_end = 2352
    _globals['_PRICETIER']._serialized_start = 2354
    _globals['_PRICETIER']._serialized_end = 2459
    _globals['_PERIOD']._serialized_start = 2461
    _globals['_PERIOD']._serialized_end = 2545