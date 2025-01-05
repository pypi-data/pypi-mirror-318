"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/resources/hotel_reconciliation.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v16.enums import hotel_reconciliation_status_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_enums_dot_hotel__reconciliation__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/ads/googleads/v16/resources/hotel_reconciliation.proto\x12"google.ads.googleads.v16.resources\x1a@google/ads/googleads/v16/enums/hotel_reconciliation_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xe3\x04\n\x13HotelReconciliation\x12K\n\rresource_name\x18\x01 \x01(\tB4\xe0A\x05\xfaA.\n,googleads.googleapis.com/HotelReconciliation\x12\x1d\n\rcommission_id\x18\x02 \x01(\tB\x06\xe0A\x02\xe0A\x03\x12\x15\n\x08order_id\x18\x03 \x01(\tB\x03\xe0A\x03\x12;\n\x08campaign\x18\x0b \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/Campaign\x12\x1c\n\x0fhotel_center_id\x18\x04 \x01(\x03B\x03\xe0A\x03\x12\x15\n\x08hotel_id\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rcheck_in_date\x18\x06 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0echeck_out_date\x18\x07 \x01(\tB\x03\xe0A\x03\x12\'\n\x17reconciled_value_micros\x18\x08 \x01(\x03B\x06\xe0A\x02\xe0A\x03\x12\x13\n\x06billed\x18\t \x01(\x08B\x03\xe0A\x03\x12o\n\x06status\x18\n \x01(\x0e2W.google.ads.googleads.v16.enums.HotelReconciliationStatusEnum.HotelReconciliationStatusB\x06\xe0A\x02\xe0A\x03:o\xeaAl\n,googleads.googleapis.com/HotelReconciliation\x12<customers/{customer_id}/hotelReconciliations/{commission_id}B\x8a\x02\n&com.google.ads.googleads.v16.resourcesB\x18HotelReconciliationProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v16/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V16.Resources\xca\x02"Google\\Ads\\GoogleAds\\V16\\Resources\xea\x02&Google::Ads::GoogleAds::V16::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.resources.hotel_reconciliation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v16.resourcesB\x18HotelReconciliationProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v16/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V16.Resources\xca\x02"Google\\Ads\\GoogleAds\\V16\\Resources\xea\x02&Google::Ads::GoogleAds::V16::Resources'
    _globals['_HOTELRECONCILIATION'].fields_by_name['resource_name']._loaded_options = None
    _globals['_HOTELRECONCILIATION'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA.\n,googleads.googleapis.com/HotelReconciliation'
    _globals['_HOTELRECONCILIATION'].fields_by_name['commission_id']._loaded_options = None
    _globals['_HOTELRECONCILIATION'].fields_by_name['commission_id']._serialized_options = b'\xe0A\x02\xe0A\x03'
    _globals['_HOTELRECONCILIATION'].fields_by_name['order_id']._loaded_options = None
    _globals['_HOTELRECONCILIATION'].fields_by_name['order_id']._serialized_options = b'\xe0A\x03'
    _globals['_HOTELRECONCILIATION'].fields_by_name['campaign']._loaded_options = None
    _globals['_HOTELRECONCILIATION'].fields_by_name['campaign']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_HOTELRECONCILIATION'].fields_by_name['hotel_center_id']._loaded_options = None
    _globals['_HOTELRECONCILIATION'].fields_by_name['hotel_center_id']._serialized_options = b'\xe0A\x03'
    _globals['_HOTELRECONCILIATION'].fields_by_name['hotel_id']._loaded_options = None
    _globals['_HOTELRECONCILIATION'].fields_by_name['hotel_id']._serialized_options = b'\xe0A\x03'
    _globals['_HOTELRECONCILIATION'].fields_by_name['check_in_date']._loaded_options = None
    _globals['_HOTELRECONCILIATION'].fields_by_name['check_in_date']._serialized_options = b'\xe0A\x03'
    _globals['_HOTELRECONCILIATION'].fields_by_name['check_out_date']._loaded_options = None
    _globals['_HOTELRECONCILIATION'].fields_by_name['check_out_date']._serialized_options = b'\xe0A\x03'
    _globals['_HOTELRECONCILIATION'].fields_by_name['reconciled_value_micros']._loaded_options = None
    _globals['_HOTELRECONCILIATION'].fields_by_name['reconciled_value_micros']._serialized_options = b'\xe0A\x02\xe0A\x03'
    _globals['_HOTELRECONCILIATION'].fields_by_name['billed']._loaded_options = None
    _globals['_HOTELRECONCILIATION'].fields_by_name['billed']._serialized_options = b'\xe0A\x03'
    _globals['_HOTELRECONCILIATION'].fields_by_name['status']._loaded_options = None
    _globals['_HOTELRECONCILIATION'].fields_by_name['status']._serialized_options = b'\xe0A\x02\xe0A\x03'
    _globals['_HOTELRECONCILIATION']._loaded_options = None
    _globals['_HOTELRECONCILIATION']._serialized_options = b'\xeaAl\n,googleads.googleapis.com/HotelReconciliation\x12<customers/{customer_id}/hotelReconciliations/{commission_id}'
    _globals['_HOTELRECONCILIATION']._serialized_start = 228
    _globals['_HOTELRECONCILIATION']._serialized_end = 839