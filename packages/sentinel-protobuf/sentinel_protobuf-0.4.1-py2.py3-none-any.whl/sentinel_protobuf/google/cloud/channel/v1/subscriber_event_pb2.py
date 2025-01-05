"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/channel/v1/subscriber_event.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/channel/v1/subscriber_event.proto\x12\x17google.cloud.channel.v1\x1a\x19google/api/resource.proto"\xe4\x01\n\rCustomerEvent\x12;\n\x08customer\x18\x01 \x01(\tB)\xfaA&\n$cloudchannel.googleapis.com/Customer\x12?\n\nevent_type\x18\x02 \x01(\x0e2+.google.cloud.channel.v1.CustomerEvent.Type"U\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x1a\n\x16PRIMARY_DOMAIN_CHANGED\x10\x01\x12\x1b\n\x17PRIMARY_DOMAIN_VERIFIED\x10\x02"\xb1\x03\n\x10EntitlementEvent\x12A\n\x0bentitlement\x18\x01 \x01(\tB,\xfaA)\n\'cloudchannel.googleapis.com/Entitlement\x12B\n\nevent_type\x18\x02 \x01(\x0e2..google.cloud.channel.v1.EntitlementEvent.Type"\x95\x02\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07CREATED\x10\x01\x12\x17\n\x13PRICE_PLAN_SWITCHED\x10\x03\x12\x16\n\x12COMMITMENT_CHANGED\x10\x04\x12\x0b\n\x07RENEWED\x10\x05\x12\r\n\tSUSPENDED\x10\x06\x12\r\n\tACTIVATED\x10\x07\x12\r\n\tCANCELLED\x10\x08\x12\x0f\n\x0bSKU_CHANGED\x10\t\x12\x1b\n\x17RENEWAL_SETTING_CHANGED\x10\n\x12\x18\n\x14PAID_SERVICE_STARTED\x10\x0b\x12\x1e\n\x1aLICENSE_ASSIGNMENT_CHANGED\x10\x0c\x12\x17\n\x13LICENSE_CAP_CHANGED\x10\r"\xa4\x01\n\x0fSubscriberEvent\x12@\n\x0ecustomer_event\x18\x01 \x01(\x0b2&.google.cloud.channel.v1.CustomerEventH\x00\x12F\n\x11entitlement_event\x18\x02 \x01(\x0b2).google.cloud.channel.v1.EntitlementEventH\x00B\x07\n\x05eventBl\n\x1bcom.google.cloud.channel.v1B\x14SubscriberEventProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.channel.v1.subscriber_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.channel.v1B\x14SubscriberEventProtoP\x01Z5cloud.google.com/go/channel/apiv1/channelpb;channelpb'
    _globals['_CUSTOMEREVENT'].fields_by_name['customer']._loaded_options = None
    _globals['_CUSTOMEREVENT'].fields_by_name['customer']._serialized_options = b'\xfaA&\n$cloudchannel.googleapis.com/Customer'
    _globals['_ENTITLEMENTEVENT'].fields_by_name['entitlement']._loaded_options = None
    _globals['_ENTITLEMENTEVENT'].fields_by_name['entitlement']._serialized_options = b"\xfaA)\n'cloudchannel.googleapis.com/Entitlement"
    _globals['_CUSTOMEREVENT']._serialized_start = 103
    _globals['_CUSTOMEREVENT']._serialized_end = 331
    _globals['_CUSTOMEREVENT_TYPE']._serialized_start = 246
    _globals['_CUSTOMEREVENT_TYPE']._serialized_end = 331
    _globals['_ENTITLEMENTEVENT']._serialized_start = 334
    _globals['_ENTITLEMENTEVENT']._serialized_end = 767
    _globals['_ENTITLEMENTEVENT_TYPE']._serialized_start = 490
    _globals['_ENTITLEMENTEVENT_TYPE']._serialized_end = 767
    _globals['_SUBSCRIBEREVENT']._serialized_start = 770
    _globals['_SUBSCRIBEREVENT']._serialized_end = 934