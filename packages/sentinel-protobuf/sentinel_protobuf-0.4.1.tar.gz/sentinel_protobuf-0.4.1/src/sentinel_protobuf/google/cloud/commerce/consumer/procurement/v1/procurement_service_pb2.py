"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/commerce/consumer/procurement/v1/procurement_service.proto')
_sym_db = _symbol_database.Default()
from .......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .......google.api import client_pb2 as google_dot_api_dot_client__pb2
from .......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .......google.cloud.commerce.consumer.procurement.v1 import order_pb2 as google_dot_cloud_dot_commerce_dot_consumer_dot_procurement_dot_v1_dot_order__pb2
from .......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGgoogle/cloud/commerce/consumer/procurement/v1/procurement_service.proto\x12-google.cloud.commerce.consumer.procurement.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a9google/cloud/commerce/consumer/procurement/v1/order.proto\x1a#google/longrunning/operations.proto"\xe5\x01\n\x11PlaceOrderRequest\x12B\n\x06parent\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*cloudbilling.googleapis.com/BillingAccount\x12\x19\n\x0cdisplay_name\x18\x06 \x01(\tB\x03\xe0A\x02\x12X\n\x0eline_item_info\x18\n \x03(\x0b2;.google.cloud.commerce.consumer.procurement.v1.LineItemInfoB\x03\xe0A\x01\x12\x17\n\nrequest_id\x18\x07 \x01(\tB\x03\xe0A\x01"\x14\n\x12PlaceOrderMetadata"$\n\x0fGetOrderRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"_\n\x11ListOrdersRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t"s\n\x12ListOrdersResponse\x12D\n\x06orders\x18\x01 \x03(\x0b24.google.cloud.commerce.consumer.procurement.v1.Order\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x90\x04\n\x12ModifyOrderRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12j\n\rmodifications\x18\x06 \x03(\x0b2N.google.cloud.commerce.consumer.procurement.v1.ModifyOrderRequest.ModificationB\x03\xe0A\x01\x12\x19\n\x0cdisplay_name\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04etag\x18\x04 \x01(\tB\x03\xe0A\x01\x1a\xcc\x02\n\x0cModification\x12\x19\n\x0cline_item_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12[\n\x0bchange_type\x18\x02 \x01(\x0e2A.google.cloud.commerce.consumer.procurement.v1.LineItemChangeTypeB\x03\xe0A\x02\x12\\\n\x12new_line_item_info\x18\x03 \x01(\x0b2;.google.cloud.commerce.consumer.procurement.v1.LineItemInfoB\x03\xe0A\x01\x12f\n\x15auto_renewal_behavior\x18\x04 \x01(\x0e2B.google.cloud.commerce.consumer.procurement.v1.AutoRenewalBehaviorB\x03\xe0A\x01"\x15\n\x13ModifyOrderMetadata"\xc6\x02\n\x12CancelOrderRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04etag\x18\x02 \x01(\tB\x03\xe0A\x01\x12v\n\x13cancellation_policy\x18\x03 \x01(\x0e2T.google.cloud.commerce.consumer.procurement.v1.CancelOrderRequest.CancellationPolicyB\x03\xe0A\x01"\x91\x01\n\x12CancellationPolicy\x12#\n\x1fCANCELLATION_POLICY_UNSPECIFIED\x10\x00\x12*\n&CANCELLATION_POLICY_CANCEL_IMMEDIATELY\x10\x01\x12*\n&CANCELLATION_POLICY_CANCEL_AT_TERM_END\x10\x02"\x15\n\x13CancelOrderMetadata*\x81\x01\n\x13AutoRenewalBehavior\x12%\n!AUTO_RENEWAL_BEHAVIOR_UNSPECIFIED\x10\x00\x12 \n\x1cAUTO_RENEWAL_BEHAVIOR_ENABLE\x10\x01\x12!\n\x1dAUTO_RENEWAL_BEHAVIOR_DISABLE\x10\x022\xe0\x08\n\x1aConsumerProcurementService\x12\xc3\x01\n\nPlaceOrder\x12@.google.cloud.commerce.consumer.procurement.v1.PlaceOrderRequest\x1a\x1d.google.longrunning.Operation"T\xcaA\x1b\n\x05Order\x12\x12PlaceOrderMetadata\x82\xd3\xe4\x93\x020"+/v1/{parent=billingAccounts/*}/orders:place:\x01*\x12\xb6\x01\n\x08GetOrder\x12>.google.cloud.commerce.consumer.procurement.v1.GetOrderRequest\x1a4.google.cloud.commerce.consumer.procurement.v1.Order"4\xdaA\x04name\x82\xd3\xe4\x93\x02\'\x12%/v1/{name=billingAccounts/*/orders/*}\x12\xc9\x01\n\nListOrders\x12@.google.cloud.commerce.consumer.procurement.v1.ListOrdersRequest\x1aA.google.cloud.commerce.consumer.procurement.v1.ListOrdersResponse"6\xdaA\x06parent\x82\xd3\xe4\x93\x02\'\x12%/v1/{parent=billingAccounts/*}/orders\x12\xc7\x01\n\x0bModifyOrder\x12A.google.cloud.commerce.consumer.procurement.v1.ModifyOrderRequest\x1a\x1d.google.longrunning.Operation"V\xcaA\x1c\n\x05Order\x12\x13ModifyOrderMetadata\x82\xd3\xe4\x93\x021",/v1/{name=billingAccounts/*/orders/*}:modify:\x01*\x12\xc7\x01\n\x0bCancelOrder\x12A.google.cloud.commerce.consumer.procurement.v1.CancelOrderRequest\x1a\x1d.google.longrunning.Operation"V\xcaA\x1c\n\x05Order\x12\x13CancelOrderMetadata\x82\xd3\xe4\x93\x021",/v1/{name=billingAccounts/*/orders/*}:cancel:\x01*\x1ac\xcaA/cloudcommerceconsumerprocurement.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x9f\x02\n1com.google.cloud.commerce.consumer.procurement.v1P\x01ZScloud.google.com/go/commerce/consumer/procurement/apiv1/procurementpb;procurementpb\xaa\x02-Google.Cloud.Commerce.Consumer.Procurement.V1\xca\x02-Google\\Cloud\\Commerce\\Consumer\\Procurement\\V1\xea\x022Google::Cloud::Commerce::Consumer::Procurement::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.commerce.consumer.procurement.v1.procurement_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n1com.google.cloud.commerce.consumer.procurement.v1P\x01ZScloud.google.com/go/commerce/consumer/procurement/apiv1/procurementpb;procurementpb\xaa\x02-Google.Cloud.Commerce.Consumer.Procurement.V1\xca\x02-Google\\Cloud\\Commerce\\Consumer\\Procurement\\V1\xea\x022Google::Cloud::Commerce::Consumer::Procurement::V1'
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
    _globals['_MODIFYORDERREQUEST_MODIFICATION'].fields_by_name['line_item_id']._loaded_options = None
    _globals['_MODIFYORDERREQUEST_MODIFICATION'].fields_by_name['line_item_id']._serialized_options = b'\xe0A\x02'
    _globals['_MODIFYORDERREQUEST_MODIFICATION'].fields_by_name['change_type']._loaded_options = None
    _globals['_MODIFYORDERREQUEST_MODIFICATION'].fields_by_name['change_type']._serialized_options = b'\xe0A\x02'
    _globals['_MODIFYORDERREQUEST_MODIFICATION'].fields_by_name['new_line_item_info']._loaded_options = None
    _globals['_MODIFYORDERREQUEST_MODIFICATION'].fields_by_name['new_line_item_info']._serialized_options = b'\xe0A\x01'
    _globals['_MODIFYORDERREQUEST_MODIFICATION'].fields_by_name['auto_renewal_behavior']._loaded_options = None
    _globals['_MODIFYORDERREQUEST_MODIFICATION'].fields_by_name['auto_renewal_behavior']._serialized_options = b'\xe0A\x01'
    _globals['_MODIFYORDERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_MODIFYORDERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_MODIFYORDERREQUEST'].fields_by_name['modifications']._loaded_options = None
    _globals['_MODIFYORDERREQUEST'].fields_by_name['modifications']._serialized_options = b'\xe0A\x01'
    _globals['_MODIFYORDERREQUEST'].fields_by_name['display_name']._loaded_options = None
    _globals['_MODIFYORDERREQUEST'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_MODIFYORDERREQUEST'].fields_by_name['etag']._loaded_options = None
    _globals['_MODIFYORDERREQUEST'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_CANCELORDERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CANCELORDERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_CANCELORDERREQUEST'].fields_by_name['etag']._loaded_options = None
    _globals['_CANCELORDERREQUEST'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_CANCELORDERREQUEST'].fields_by_name['cancellation_policy']._loaded_options = None
    _globals['_CANCELORDERREQUEST'].fields_by_name['cancellation_policy']._serialized_options = b'\xe0A\x01'
    _globals['_CONSUMERPROCUREMENTSERVICE']._loaded_options = None
    _globals['_CONSUMERPROCUREMENTSERVICE']._serialized_options = b'\xcaA/cloudcommerceconsumerprocurement.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CONSUMERPROCUREMENTSERVICE'].methods_by_name['PlaceOrder']._loaded_options = None
    _globals['_CONSUMERPROCUREMENTSERVICE'].methods_by_name['PlaceOrder']._serialized_options = b'\xcaA\x1b\n\x05Order\x12\x12PlaceOrderMetadata\x82\xd3\xe4\x93\x020"+/v1/{parent=billingAccounts/*}/orders:place:\x01*'
    _globals['_CONSUMERPROCUREMENTSERVICE'].methods_by_name['GetOrder']._loaded_options = None
    _globals['_CONSUMERPROCUREMENTSERVICE'].methods_by_name['GetOrder']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02'\x12%/v1/{name=billingAccounts/*/orders/*}"
    _globals['_CONSUMERPROCUREMENTSERVICE'].methods_by_name['ListOrders']._loaded_options = None
    _globals['_CONSUMERPROCUREMENTSERVICE'].methods_by_name['ListOrders']._serialized_options = b"\xdaA\x06parent\x82\xd3\xe4\x93\x02'\x12%/v1/{parent=billingAccounts/*}/orders"
    _globals['_CONSUMERPROCUREMENTSERVICE'].methods_by_name['ModifyOrder']._loaded_options = None
    _globals['_CONSUMERPROCUREMENTSERVICE'].methods_by_name['ModifyOrder']._serialized_options = b'\xcaA\x1c\n\x05Order\x12\x13ModifyOrderMetadata\x82\xd3\xe4\x93\x021",/v1/{name=billingAccounts/*/orders/*}:modify:\x01*'
    _globals['_CONSUMERPROCUREMENTSERVICE'].methods_by_name['CancelOrder']._loaded_options = None
    _globals['_CONSUMERPROCUREMENTSERVICE'].methods_by_name['CancelOrder']._serialized_options = b'\xcaA\x1c\n\x05Order\x12\x13CancelOrderMetadata\x82\xd3\xe4\x93\x021",/v1/{name=billingAccounts/*/orders/*}:cancel:\x01*'
    _globals['_AUTORENEWALBEHAVIOR']._serialized_start = 1746
    _globals['_AUTORENEWALBEHAVIOR']._serialized_end = 1875
    _globals['_PLACEORDERREQUEST']._serialized_start = 334
    _globals['_PLACEORDERREQUEST']._serialized_end = 563
    _globals['_PLACEORDERMETADATA']._serialized_start = 565
    _globals['_PLACEORDERMETADATA']._serialized_end = 585
    _globals['_GETORDERREQUEST']._serialized_start = 587
    _globals['_GETORDERREQUEST']._serialized_end = 623
    _globals['_LISTORDERSREQUEST']._serialized_start = 625
    _globals['_LISTORDERSREQUEST']._serialized_end = 720
    _globals['_LISTORDERSRESPONSE']._serialized_start = 722
    _globals['_LISTORDERSRESPONSE']._serialized_end = 837
    _globals['_MODIFYORDERREQUEST']._serialized_start = 840
    _globals['_MODIFYORDERREQUEST']._serialized_end = 1368
    _globals['_MODIFYORDERREQUEST_MODIFICATION']._serialized_start = 1036
    _globals['_MODIFYORDERREQUEST_MODIFICATION']._serialized_end = 1368
    _globals['_MODIFYORDERMETADATA']._serialized_start = 1370
    _globals['_MODIFYORDERMETADATA']._serialized_end = 1391
    _globals['_CANCELORDERREQUEST']._serialized_start = 1394
    _globals['_CANCELORDERREQUEST']._serialized_end = 1720
    _globals['_CANCELORDERREQUEST_CANCELLATIONPOLICY']._serialized_start = 1575
    _globals['_CANCELORDERREQUEST_CANCELLATIONPOLICY']._serialized_end = 1720
    _globals['_CANCELORDERMETADATA']._serialized_start = 1722
    _globals['_CANCELORDERMETADATA']._serialized_end = 1743
    _globals['_CONSUMERPROCUREMENTSERVICE']._serialized_start = 1878
    _globals['_CONSUMERPROCUREMENTSERVICE']._serialized_end = 2998