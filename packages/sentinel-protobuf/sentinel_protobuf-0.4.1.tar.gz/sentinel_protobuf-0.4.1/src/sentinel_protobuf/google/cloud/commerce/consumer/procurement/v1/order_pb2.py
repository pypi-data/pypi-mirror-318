"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/commerce/consumer/procurement/v1/order.proto')
_sym_db = _symbol_database.Default()
from .......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/commerce/consumer/procurement/v1/order.proto\x12-google.cloud.commerce.consumer.procurement.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xcb\x03\n\x05Order\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\n \x01(\tB\x03\xe0A\x02\x12P\n\nline_items\x18\x06 \x03(\x0b27.google.cloud.commerce.consumer.procurement.v1.LineItemB\x03\xe0A\x03\x12Z\n\x14cancelled_line_items\x18\x07 \x03(\x0b27.google.cloud.commerce.consumer.procurement.v1.LineItemB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x0c\n\x04etag\x18\x0b \x01(\t:l\xeaAi\n5cloudcommerceconsumerprocurement.googleapis.com/Order\x120billingAccounts/{billing_account}/orders/{order}"\xb7\x02\n\x08LineItem\x12\x19\n\x0cline_item_id\x18\x01 \x01(\tB\x03\xe0A\x03\x12X\n\x0eline_item_info\x18\x02 \x01(\x0b2;.google.cloud.commerce.consumer.procurement.v1.LineItemInfoB\x03\xe0A\x03\x12Z\n\x0epending_change\x18\x03 \x01(\x0b2=.google.cloud.commerce.consumer.procurement.v1.LineItemChangeB\x03\xe0A\x03\x12Z\n\x0echange_history\x18\x04 \x03(\x0b2=.google.cloud.commerce.consumer.procurement.v1.LineItemChangeB\x03\xe0A\x03"\xd7\x05\n\x0eLineItemChange\x12\x16\n\tchange_id\x18\x01 \x01(\tB\x03\xe0A\x03\x12[\n\x0bchange_type\x18\x02 \x01(\x0e2A.google.cloud.commerce.consumer.procurement.v1.LineItemChangeTypeB\x03\xe0A\x02\x12\\\n\x12old_line_item_info\x18\x03 \x01(\x0b2;.google.cloud.commerce.consumer.procurement.v1.LineItemInfoB\x03\xe0A\x03\x12W\n\x12new_line_item_info\x18\x04 \x01(\x0b2;.google.cloud.commerce.consumer.procurement.v1.LineItemInfo\x12]\n\x0cchange_state\x18\x05 \x01(\x0e2B.google.cloud.commerce.consumer.procurement.v1.LineItemChangeStateB\x03\xe0A\x03\x12\x19\n\x0cstate_reason\x18\x06 \x01(\tB\x03\xe0A\x03\x12s\n\x18change_state_reason_type\x18\n \x01(\x0e2L.google.cloud.commerce.consumer.procurement.v1.LineItemChangeStateReasonTypeB\x03\xe0A\x03\x12>\n\x15change_effective_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"\xfb\x01\n\x0cLineItemInfo\x12@\n\x05offer\x18\r \x01(\tB1\xe0A\x01\xfaA+\n)commerceoffercatalog.googleapis.com/Offer\x12Q\n\nparameters\x18\t \x03(\x0b28.google.cloud.commerce.consumer.procurement.v1.ParameterB\x03\xe0A\x01\x12V\n\x0csubscription\x18\n \x01(\x0b2;.google.cloud.commerce.consumer.procurement.v1.SubscriptionB\x03\xe0A\x03"\xc0\x01\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12M\n\x05value\x18\x02 \x01(\x0b2>.google.cloud.commerce.consumer.procurement.v1.Parameter.Value\x1aV\n\x05Value\x12\x15\n\x0bint64_value\x18\x03 \x01(\x03H\x00\x12\x16\n\x0cstring_value\x18\x04 \x01(\tH\x00\x12\x16\n\x0cdouble_value\x18\x05 \x01(\x01H\x00B\x06\n\x04kind"\x8a\x01\n\x0cSubscription\x12.\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x1c\n\x14auto_renewal_enabled\x18\x02 \x01(\x08*\xd0\x01\n\x12LineItemChangeType\x12%\n!LINE_ITEM_CHANGE_TYPE_UNSPECIFIED\x10\x00\x12 \n\x1cLINE_ITEM_CHANGE_TYPE_CREATE\x10\x01\x12 \n\x1cLINE_ITEM_CHANGE_TYPE_UPDATE\x10\x02\x12 \n\x1cLINE_ITEM_CHANGE_TYPE_CANCEL\x10\x03\x12-\n)LINE_ITEM_CHANGE_TYPE_REVERT_CANCELLATION\x10\x04*\xa7\x02\n\x13LineItemChangeState\x12&\n"LINE_ITEM_CHANGE_STATE_UNSPECIFIED\x10\x00\x12+\n\'LINE_ITEM_CHANGE_STATE_PENDING_APPROVAL\x10\x01\x12#\n\x1fLINE_ITEM_CHANGE_STATE_APPROVED\x10\x02\x12$\n LINE_ITEM_CHANGE_STATE_COMPLETED\x10\x03\x12#\n\x1fLINE_ITEM_CHANGE_STATE_REJECTED\x10\x04\x12$\n LINE_ITEM_CHANGE_STATE_ABANDONED\x10\x05\x12%\n!LINE_ITEM_CHANGE_STATE_ACTIVATING\x10\x06*\xf3\x01\n\x1dLineItemChangeStateReasonType\x122\n.LINE_ITEM_CHANGE_STATE_REASON_TYPE_UNSPECIFIED\x10\x00\x12.\n*LINE_ITEM_CHANGE_STATE_REASON_TYPE_EXPIRED\x10\x01\x125\n1LINE_ITEM_CHANGE_STATE_REASON_TYPE_USER_CANCELLED\x10\x02\x127\n3LINE_ITEM_CHANGE_STATE_REASON_TYPE_SYSTEM_CANCELLED\x10\x03B\xb4\x03\n1com.google.cloud.commerce.consumer.procurement.v1P\x01ZScloud.google.com/go/commerce/consumer/procurement/apiv1/procurementpb;procurementpb\xaa\x02-Google.Cloud.Commerce.Consumer.Procurement.V1\xca\x02-Google\\Cloud\\Commerce\\Consumer\\Procurement\\V1\xea\x022Google::Cloud::Commerce::Consumer::Procurement::V1\xeaA\x91\x01\n)commerceoffercatalog.googleapis.com/Offer\x12)services/{service}/standardOffers/{offer}\x129billingAccounts/{consumer_billing_account}/offers/{offer}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.commerce.consumer.procurement.v1.order_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n1com.google.cloud.commerce.consumer.procurement.v1P\x01ZScloud.google.com/go/commerce/consumer/procurement/apiv1/procurementpb;procurementpb\xaa\x02-Google.Cloud.Commerce.Consumer.Procurement.V1\xca\x02-Google\\Cloud\\Commerce\\Consumer\\Procurement\\V1\xea\x022Google::Cloud::Commerce::Consumer::Procurement::V1\xeaA\x91\x01\n)commerceoffercatalog.googleapis.com/Offer\x12)services/{service}/standardOffers/{offer}\x129billingAccounts/{consumer_billing_account}/offers/{offer}'
    _globals['_ORDER'].fields_by_name['name']._loaded_options = None
    _globals['_ORDER'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_ORDER'].fields_by_name['display_name']._loaded_options = None
    _globals['_ORDER'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_ORDER'].fields_by_name['line_items']._loaded_options = None
    _globals['_ORDER'].fields_by_name['line_items']._serialized_options = b'\xe0A\x03'
    _globals['_ORDER'].fields_by_name['cancelled_line_items']._loaded_options = None
    _globals['_ORDER'].fields_by_name['cancelled_line_items']._serialized_options = b'\xe0A\x03'
    _globals['_ORDER'].fields_by_name['create_time']._loaded_options = None
    _globals['_ORDER'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ORDER'].fields_by_name['update_time']._loaded_options = None
    _globals['_ORDER'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ORDER']._loaded_options = None
    _globals['_ORDER']._serialized_options = b'\xeaAi\n5cloudcommerceconsumerprocurement.googleapis.com/Order\x120billingAccounts/{billing_account}/orders/{order}'
    _globals['_LINEITEM'].fields_by_name['line_item_id']._loaded_options = None
    _globals['_LINEITEM'].fields_by_name['line_item_id']._serialized_options = b'\xe0A\x03'
    _globals['_LINEITEM'].fields_by_name['line_item_info']._loaded_options = None
    _globals['_LINEITEM'].fields_by_name['line_item_info']._serialized_options = b'\xe0A\x03'
    _globals['_LINEITEM'].fields_by_name['pending_change']._loaded_options = None
    _globals['_LINEITEM'].fields_by_name['pending_change']._serialized_options = b'\xe0A\x03'
    _globals['_LINEITEM'].fields_by_name['change_history']._loaded_options = None
    _globals['_LINEITEM'].fields_by_name['change_history']._serialized_options = b'\xe0A\x03'
    _globals['_LINEITEMCHANGE'].fields_by_name['change_id']._loaded_options = None
    _globals['_LINEITEMCHANGE'].fields_by_name['change_id']._serialized_options = b'\xe0A\x03'
    _globals['_LINEITEMCHANGE'].fields_by_name['change_type']._loaded_options = None
    _globals['_LINEITEMCHANGE'].fields_by_name['change_type']._serialized_options = b'\xe0A\x02'
    _globals['_LINEITEMCHANGE'].fields_by_name['old_line_item_info']._loaded_options = None
    _globals['_LINEITEMCHANGE'].fields_by_name['old_line_item_info']._serialized_options = b'\xe0A\x03'
    _globals['_LINEITEMCHANGE'].fields_by_name['change_state']._loaded_options = None
    _globals['_LINEITEMCHANGE'].fields_by_name['change_state']._serialized_options = b'\xe0A\x03'
    _globals['_LINEITEMCHANGE'].fields_by_name['state_reason']._loaded_options = None
    _globals['_LINEITEMCHANGE'].fields_by_name['state_reason']._serialized_options = b'\xe0A\x03'
    _globals['_LINEITEMCHANGE'].fields_by_name['change_state_reason_type']._loaded_options = None
    _globals['_LINEITEMCHANGE'].fields_by_name['change_state_reason_type']._serialized_options = b'\xe0A\x03'
    _globals['_LINEITEMCHANGE'].fields_by_name['change_effective_time']._loaded_options = None
    _globals['_LINEITEMCHANGE'].fields_by_name['change_effective_time']._serialized_options = b'\xe0A\x03'
    _globals['_LINEITEMCHANGE'].fields_by_name['create_time']._loaded_options = None
    _globals['_LINEITEMCHANGE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_LINEITEMCHANGE'].fields_by_name['update_time']._loaded_options = None
    _globals['_LINEITEMCHANGE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_LINEITEMINFO'].fields_by_name['offer']._loaded_options = None
    _globals['_LINEITEMINFO'].fields_by_name['offer']._serialized_options = b'\xe0A\x01\xfaA+\n)commerceoffercatalog.googleapis.com/Offer'
    _globals['_LINEITEMINFO'].fields_by_name['parameters']._loaded_options = None
    _globals['_LINEITEMINFO'].fields_by_name['parameters']._serialized_options = b'\xe0A\x01'
    _globals['_LINEITEMINFO'].fields_by_name['subscription']._loaded_options = None
    _globals['_LINEITEMINFO'].fields_by_name['subscription']._serialized_options = b'\xe0A\x03'
    _globals['_LINEITEMCHANGETYPE']._serialized_start = 2298
    _globals['_LINEITEMCHANGETYPE']._serialized_end = 2506
    _globals['_LINEITEMCHANGESTATE']._serialized_start = 2509
    _globals['_LINEITEMCHANGESTATE']._serialized_end = 2804
    _globals['_LINEITEMCHANGESTATEREASONTYPE']._serialized_start = 2807
    _globals['_LINEITEMCHANGESTATEREASONTYPE']._serialized_end = 3050
    _globals['_ORDER']._serialized_start = 202
    _globals['_ORDER']._serialized_end = 661
    _globals['_LINEITEM']._serialized_start = 664
    _globals['_LINEITEM']._serialized_end = 975
    _globals['_LINEITEMCHANGE']._serialized_start = 978
    _globals['_LINEITEMCHANGE']._serialized_end = 1705
    _globals['_LINEITEMINFO']._serialized_start = 1708
    _globals['_LINEITEMINFO']._serialized_end = 1959
    _globals['_PARAMETER']._serialized_start = 1962
    _globals['_PARAMETER']._serialized_end = 2154
    _globals['_PARAMETER_VALUE']._serialized_start = 2068
    _globals['_PARAMETER_VALUE']._serialized_end = 2154
    _globals['_SUBSCRIPTION']._serialized_start = 2157
    _globals['_SUBSCRIPTION']._serialized_end = 2295