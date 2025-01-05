"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/commerce/consumer/procurement/v1alpha1/procurement_service.proto')
_sym_db = _symbol_database.Default()
from .......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .......google.api import client_pb2 as google_dot_api_dot_client__pb2
from .......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .......google.cloud.commerce.consumer.procurement.v1alpha1 import order_pb2 as google_dot_cloud_dot_commerce_dot_consumer_dot_procurement_dot_v1alpha1_dot_order__pb2
from .......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nMgoogle/cloud/commerce/consumer/procurement/v1alpha1/procurement_service.proto\x123google.cloud.commerce.consumer.procurement.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a?google/cloud/commerce/consumer/procurement/v1alpha1/order.proto\x1a#google/longrunning/operations.proto"\xeb\x01\n\x11PlaceOrderRequest\x12B\n\x06parent\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*cloudbilling.googleapis.com/BillingAccount\x12\x19\n\x0cdisplay_name\x18\x06 \x01(\tB\x03\xe0A\x02\x12^\n\x0eline_item_info\x18\n \x03(\x0b2A.google.cloud.commerce.consumer.procurement.v1alpha1.LineItemInfoB\x03\xe0A\x01\x12\x17\n\nrequest_id\x18\x07 \x01(\tB\x03\xe0A\x01"\x14\n\x12PlaceOrderMetadata"$\n\x0fGetOrderRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"_\n\x11ListOrdersRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"y\n\x12ListOrdersResponse\x12J\n\x06orders\x18\x01 \x03(\x0b2:.google.cloud.commerce.consumer.procurement.v1alpha1.Order\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xfc\x05\n\x1aConsumerProcurementService\x12\xcf\x01\n\nPlaceOrder\x12F.google.cloud.commerce.consumer.procurement.v1alpha1.PlaceOrderRequest\x1a\x1d.google.longrunning.Operation"Z\xcaA\x1b\n\x05Order\x12\x12PlaceOrderMetadata\x82\xd3\xe4\x93\x026"1/v1alpha1/{parent=billingAccounts/*}/orders:place:\x01*\x12\xc8\x01\n\x08GetOrder\x12D.google.cloud.commerce.consumer.procurement.v1alpha1.GetOrderRequest\x1a:.google.cloud.commerce.consumer.procurement.v1alpha1.Order":\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1alpha1/{name=billingAccounts/*/orders/*}\x12\xdb\x01\n\nListOrders\x12F.google.cloud.commerce.consumer.procurement.v1alpha1.ListOrdersRequest\x1aG.google.cloud.commerce.consumer.procurement.v1alpha1.ListOrdersResponse"<\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/v1alpha1/{parent=billingAccounts/*}/orders\x1ac\xcaA/cloudcommerceconsumerprocurement.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x96\x01\n7com.google.cloud.commerce.consumer.procurement.v1alpha1P\x01ZYcloud.google.com/go/commerce/consumer/procurement/apiv1alpha1/procurementpb;procurementpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.commerce.consumer.procurement.v1alpha1.procurement_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n7com.google.cloud.commerce.consumer.procurement.v1alpha1P\x01ZYcloud.google.com/go/commerce/consumer/procurement/apiv1alpha1/procurementpb;procurementpb'
    _globals['_PLACEORDERREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_PLACEORDERREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA,\n*cloudbilling.googleapis.com/BillingAccount'
    _globals['_PLACEORDERREQUEST'].fields_by_name['display_name']._loaded_options = None
    _globals['_PLACEORDERREQUEST'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_PLACEORDERREQUEST'].fields_by_name['line_item_info']._loaded_options = None
    _globals['_PLACEORDERREQUEST'].fields_by_name['line_item_info']._serialized_options = b'\xe0A\x01'
    _globals['_PLACEORDERREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_PLACEORDERREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_GETORDERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETORDERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_LISTORDERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTORDERSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_CONSUMERPROCUREMENTSERVICE']._loaded_options = None
    _globals['_CONSUMERPROCUREMENTSERVICE']._serialized_options = b'\xcaA/cloudcommerceconsumerprocurement.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CONSUMERPROCUREMENTSERVICE'].methods_by_name['PlaceOrder']._loaded_options = None
    _globals['_CONSUMERPROCUREMENTSERVICE'].methods_by_name['PlaceOrder']._serialized_options = b'\xcaA\x1b\n\x05Order\x12\x12PlaceOrderMetadata\x82\xd3\xe4\x93\x026"1/v1alpha1/{parent=billingAccounts/*}/orders:place:\x01*'
    _globals['_CONSUMERPROCUREMENTSERVICE'].methods_by_name['GetOrder']._loaded_options = None
    _globals['_CONSUMERPROCUREMENTSERVICE'].methods_by_name['GetOrder']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1alpha1/{name=billingAccounts/*/orders/*}'
    _globals['_CONSUMERPROCUREMENTSERVICE'].methods_by_name['ListOrders']._loaded_options = None
    _globals['_CONSUMERPROCUREMENTSERVICE'].methods_by_name['ListOrders']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/v1alpha1/{parent=billingAccounts/*}/orders'
    _globals['_PLACEORDERREQUEST']._serialized_start = 352
    _globals['_PLACEORDERREQUEST']._serialized_end = 587
    _globals['_PLACEORDERMETADATA']._serialized_start = 589
    _globals['_PLACEORDERMETADATA']._serialized_end = 609
    _globals['_GETORDERREQUEST']._serialized_start = 611
    _globals['_GETORDERREQUEST']._serialized_end = 647
    _globals['_LISTORDERSREQUEST']._serialized_start = 649
    _globals['_LISTORDERSREQUEST']._serialized_end = 744
    _globals['_LISTORDERSRESPONSE']._serialized_start = 746
    _globals['_LISTORDERSRESPONSE']._serialized_end = 867
    _globals['_CONSUMERPROCUREMENTSERVICE']._serialized_start = 870
    _globals['_CONSUMERPROCUREMENTSERVICE']._serialized_end = 1634